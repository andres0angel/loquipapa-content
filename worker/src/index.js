// LOQUIPAPAS · publicador
// Guarda las piezas, las programa y las publica en Instagram, Facebook y TikTok.
// Corre en Cloudflare Workers (plan gratuito): D1 para la agenda, KV o R2 para los archivos.

const CORS = {
  'access-control-allow-origin': '*',
  'access-control-allow-headers': 'authorization,content-type',
  'access-control-allow-methods': 'GET,POST,DELETE,OPTIONS',
};
const json = (o, status = 200) =>
  new Response(JSON.stringify(o), { status, headers: { 'content-type': 'application/json', ...CORS } });

const TIPOS = ['reel', 'image', 'story', 'carousel'];
const REDES = ['ig', 'fb', 'tiktok'];
const EXT = { 'video/mp4': 'mp4', 'image/jpeg': 'jpg', 'image/png': 'png' };
const MAX_KV = 25 * 1024 * 1024;

/* ---------- Archivos (KV por defecto, R2 si existe el enlace MEDIA) ---------- */
async function mediaPut(env, key, body, type) {
  if (env.MEDIA) return env.MEDIA.put(key, body, { httpMetadata: { contentType: type } });
  return env.MEDIA_KV.put(key, body, { metadata: { type } });
}
async function mediaGet(env, key) {
  if (env.MEDIA) {
    const o = await env.MEDIA.get(key);
    return o ? { body: o.body, type: o.httpMetadata?.contentType || 'application/octet-stream', size: o.size } : null;
  }
  const r = await env.MEDIA_KV.getWithMetadata(key, 'arrayBuffer');
  return r.value ? { body: r.value, type: r.metadata?.type || 'application/octet-stream', size: r.value.byteLength } : null;
}
async function mediaDel(env, key) {
  return env.MEDIA ? env.MEDIA.delete(key) : env.MEDIA_KV.delete(key);
}

async function serveMedia(req, env, key) {
  const m = await mediaGet(env, key);
  if (!m) return new Response('No existe', { status: 404 });
  const h = { 'content-type': m.type, 'accept-ranges': 'bytes', 'cache-control': 'public, max-age=86400' };
  const range = req.headers.get('range');
  if (range && m.body instanceof ArrayBuffer) {
    const mm = /bytes=(\d*)-(\d*)/.exec(range);
    if (mm) {
      const start = mm[1] ? Number(mm[1]) : 0;
      const end = mm[2] ? Math.min(Number(mm[2]), m.size - 1) : m.size - 1;
      if (start <= end && start < m.size) {
        return new Response(m.body.slice(start, end + 1), {
          status: 206,
          headers: { ...h, 'content-range': `bytes ${start}-${end}/${m.size}`, 'content-length': String(end - start + 1) },
        });
      }
    }
  }
  return new Response(m.body, { headers: { ...h, 'content-length': String(m.size) } });
}

/* ---------- Meta (Instagram y Facebook) ---------- */
async function graph(env, path, params, method = 'POST') {
  const v = env.GRAPH_VERSION || 'v26.0';
  const body = new URLSearchParams({ ...params, access_token: env.META_PAGE_TOKEN });
  const url = `${env.GRAPH_BASE || 'https://graph.facebook.com'}/${v}/${path}`;
  const r = method === 'GET' ? await fetch(`${url}?${body}`) : await fetch(url, { method, body });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || j.error) throw new Error(j.error?.message || `Meta respondió ${r.status}`);
  return j;
}

async function pasoInstagram(env, post, st) {
  const ig = env.IG_USER_ID;
  if (!st.contenedor) {
    const [u] = post.urls;
    let p;
    if (post.tipo === 'image') p = { image_url: u, caption: post.caption };
    else if (post.tipo === 'story') p = /\.mp4$/.test(u) ? { media_type: 'STORIES', video_url: u } : { media_type: 'STORIES', image_url: u };
    else if (post.tipo === 'reel') p = { media_type: 'REELS', video_url: u, caption: post.caption, share_to_feed: 'true' };
    else {
      const hijos = [];
      for (const x of post.urls.slice(0, 10)) hijos.push((await graph(env, `${ig}/media`, { image_url: x, is_carousel_item: 'true' })).id);
      p = { media_type: 'CAROUSEL', children: hijos.join(','), caption: post.caption };
    }
    st.contenedor = (await graph(env, `${ig}/media`, p)).id;
    st.estado = 'procesando';
  }
  const s = await graph(env, st.contenedor, { fields: 'status_code' }, 'GET');
  if (s.status_code === 'FINISHED') {
    st.id = (await graph(env, `${ig}/media_publish`, { creation_id: st.contenedor })).id;
    st.estado = 'publicado';
  } else if (s.status_code === 'ERROR' || s.status_code === 'EXPIRED') {
    throw new Error('Instagram no pudo procesar el archivo (' + s.status_code + ')');
  }
}

async function pasoFacebook(env, post, st) {
  const pg = env.FB_PAGE_ID;
  if (post.tipo === 'story') { st.estado = 'omitido'; st.error = 'Las historias no se publican en Facebook desde aquí'; return; }
  if (post.tipo === 'reel') st.id = (await graph(env, `${pg}/videos`, { file_url: post.urls[0], description: post.caption })).id;
  else if (post.tipo === 'image') st.id = (await graph(env, `${pg}/photos`, { url: post.urls[0], caption: post.caption })).id;
  else {
    const p = { message: post.caption };
    let i = 0;
    for (const x of post.urls.slice(0, 10)) {
      const f = await graph(env, `${pg}/photos`, { url: x, published: 'false' });
      p[`attached_media[${i++}]`] = JSON.stringify({ media_fbid: f.id });
    }
    st.id = (await graph(env, `${pg}/feed`, p)).id;
  }
  st.estado = 'publicado';
}

/* ---------- TikTok ---------- */
async function ajuste(env, clave, valor) {
  if (valor === undefined) return (await env.DB.prepare('SELECT valor FROM ajustes WHERE clave=?').bind(clave).first())?.valor ?? null;
  await env.DB.prepare('INSERT INTO ajustes(clave,valor) VALUES(?,?) ON CONFLICT(clave) DO UPDATE SET valor=excluded.valor').bind(clave, valor).run();
}
async function tokenTikTok(env) {
  const raw = await ajuste(env, 'tiktok');
  if (!raw) return null;
  const t = JSON.parse(raw);
  if (t.expira > Date.now() + 60000) return t.access_token;
  if (!t.refresh_token || !env.TIKTOK_CLIENT_KEY) return null;
  const r = await fetch(`${env.TIKTOK_BASE || 'https://open.tiktokapis.com'}/v2/oauth/token/`, {
    method: 'POST',
    body: new URLSearchParams({ client_key: env.TIKTOK_CLIENT_KEY, client_secret: env.TIKTOK_CLIENT_SECRET, grant_type: 'refresh_token', refresh_token: t.refresh_token }),
  });
  const j = await r.json().catch(() => ({}));
  if (!j.access_token) throw new Error('TikTok no renovó el acceso: ' + (j.error_description || r.status));
  await ajuste(env, 'tiktok', JSON.stringify({ access_token: j.access_token, refresh_token: j.refresh_token || t.refresh_token, expira: Date.now() + j.expires_in * 1000 }));
  return j.access_token;
}
async function pasoTikTok(env, post, st) {
  if (post.tipo !== 'reel') { st.estado = 'omitido'; st.error = 'A TikTok solo se envían videos'; return; }
  const token = await tokenTikTok(env);
  if (!token) throw new Error('TikTok no está conectado');
  const r = await fetch(`${env.TIKTOK_BASE || 'https://open.tiktokapis.com'}/v2/post/publish/video/init/`, {
    method: 'POST',
    headers: { authorization: 'Bearer ' + token, 'content-type': 'application/json; charset=UTF-8' },
    body: JSON.stringify({
      post_info: { title: (post.caption || '').slice(0, 2200), privacy_level: env.TIKTOK_PRIVACY || 'SELF_ONLY' },
      source_info: { source: 'PULL_FROM_URL', video_url: post.urls[0] },
    }),
  });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || (j.error && j.error.code !== 'ok')) throw new Error(j.error?.message || `TikTok respondió ${r.status}`);
  st.id = j.data?.publish_id;
  st.estado = 'publicado';
}

/* ---------- Tablas (se crean solas la primera vez) ---------- */
let listo = false;
async function preparar(env) {
  if (listo) return;
  await env.DB.batch([
    env.DB.prepare("CREATE TABLE IF NOT EXISTS posts(id TEXT PRIMARY KEY, cuando INTEGER NOT NULL, tipo TEXT NOT NULL, caption TEXT, media TEXT NOT NULL, redes TEXT NOT NULL, estado TEXT NOT NULL DEFAULT 'programado', detalle TEXT NOT NULL DEFAULT '{}', creado INTEGER NOT NULL)"),
    env.DB.prepare('CREATE INDEX IF NOT EXISTS posts_pendientes ON posts(estado, cuando)'),
    env.DB.prepare('CREATE TABLE IF NOT EXISTS ajustes(clave TEXT PRIMARY KEY, valor TEXT NOT NULL)'),
  ]);
  listo = true;
}

/* ---------- Agenda ---------- */
const conectadas = async (env) => ({
  ig: !!(env.IG_USER_ID && env.META_PAGE_TOKEN),
  fb: !!(env.FB_PAGE_ID && env.META_PAGE_TOKEN),
  tiktok: !!(await ajuste(env, 'tiktok')),
});
const PASOS = { ig: pasoInstagram, fb: pasoFacebook, tiktok: pasoTikTok };
const FINAL = ['publicado', 'error', 'omitido'];

async function procesar(env, fila, origen) {
  const post = { ...fila, urls: JSON.parse(fila.media).map((k) => `${origen}/media/${k}`) };
  const det = JSON.parse(fila.detalle || '{}');
  const ok = await conectadas(env);
  for (const red of JSON.parse(fila.redes)) {
    const st = (det[red] ||= { estado: 'pendiente', intentos: 0 });
    if (FINAL.includes(st.estado)) continue;
    st.intentos++;
    try {
      if (!ok[red]) throw new Error('Esta red no está conectada');
      await PASOS[red](env, post, st);
      if (!FINAL.includes(st.estado) && st.intentos > 24) throw new Error('Se agotó el tiempo de espera');
    } catch (e) {
      st.estado = 'error';
      st.error = String(e.message || e).slice(0, 300);
    }
  }
  const est = Object.values(det).map((s) => s.estado);
  const estado = est.some((e) => !FINAL.includes(e)) ? 'procesando'
    : est.every((e) => e === 'error') ? 'error'
    : est.some((e) => e === 'error') ? 'parcial' : 'publicado';
  await env.DB.prepare('UPDATE posts SET estado=?, detalle=? WHERE id=?').bind(estado, JSON.stringify(det), fila.id).run();
  return { id: fila.id, estado, detalle: det };
}

const vista = (f) => ({ id: f.id, cuando: f.cuando, tipo: f.tipo, caption: f.caption, redes: JSON.parse(f.redes), estado: f.estado, detalle: JSON.parse(f.detalle || '{}') });

async function api(req, env, url) {
  const auth = req.headers.get('authorization') || '';
  if (!env.APP_TOKEN || auth !== 'Bearer ' + env.APP_TOKEN) return json({ error: 'Clave incorrecta' }, 401);
  const p = url.pathname, m = req.method;
  await preparar(env);
  // Recuerda la dirección pública para que la tarea programada arme los enlaces de los archivos.
  if ((await ajuste(env, 'origen')) !== url.origin) await ajuste(env, 'origen', url.origin);

  if (p === '/api/status' && m === 'GET') return json({ ok: true, redes: await conectadas(env), almacen: env.MEDIA ? 'r2' : 'kv', ia: !!env.AI });

  if (p === '/api/media' && m === 'POST') {
    const type = (req.headers.get('content-type') || '').split(';')[0];
    if (!EXT[type]) return json({ error: 'Formato no admitido. Usa MP4, JPG o PNG.' }, 415);
    const body = await req.arrayBuffer();
    if (!body.byteLength) return json({ error: 'Archivo vacío' }, 400);
    if (!env.MEDIA && body.byteLength > MAX_KV) return json({ error: 'El archivo supera 25 MB' }, 413);
    const key = `${crypto.randomUUID()}.${EXT[type]}`;
    await mediaPut(env, key, body, type);
    return json({ key, url: `${url.origin}/media/${key}` });
  }

  if (p === '/api/posts' && m === 'GET') {
    const r = await env.DB.prepare('SELECT * FROM posts ORDER BY cuando DESC LIMIT 200').all();
    return json({ posts: r.results.map(vista) });
  }

  if (p === '/api/posts' && m === 'POST') {
    const b = await req.json().catch(() => null);
    if (!b) return json({ error: 'Datos inválidos' }, 400);
    const redes = (b.redes || []).filter((r) => REDES.includes(r));
    const media = (b.media || []).filter((k) => /^[\w-]+\.(mp4|jpg|png)$/.test(k));
    const cuando = Number(b.cuando);
    if (!TIPOS.includes(b.tipo) || !redes.length || !media.length || !Number.isFinite(cuando)) return json({ error: 'Faltan datos: tipo, redes, archivos o fecha' }, 400);
    const id = crypto.randomUUID();
    await env.DB.prepare('INSERT INTO posts(id,cuando,tipo,caption,media,redes,estado,detalle,creado) VALUES(?,?,?,?,?,?,?,?,?)')
      .bind(id, cuando, b.tipo, String(b.caption || '').slice(0, 2200), JSON.stringify(media), JSON.stringify(redes), 'programado', '{}', Date.now()).run();
    return json({ id, estado: 'programado' }, 201);
  }

  const mm = /^\/api\/posts\/([\w-]+)(\/publish)?$/.exec(p);
  if (mm) {
    const fila = await env.DB.prepare('SELECT * FROM posts WHERE id=?').bind(mm[1]).first();
    if (!fila) return json({ error: 'No existe' }, 404);
    if (m === 'DELETE' && !mm[2]) {
      for (const k of JSON.parse(fila.media)) await mediaDel(env, k);
      await env.DB.prepare('DELETE FROM posts WHERE id=?').bind(fila.id).run();
      return json({ ok: true });
    }
    if (m === 'POST' && mm[2]) {
      if (fila.estado === 'publicado') return json({ error: 'Ya se publicó' }, 409);
      return json(await procesar(env, fila, url.origin));
    }
  }

  // IA gratuita de Cloudflare (Workers AI): textos e imágenes dentro de la cuota diaria sin costo.
  if (p === '/api/ideas' && m === 'POST') {
    if (!env.AI) return json({ error: 'La IA gratuita no está activada en el servidor' }, 501);
    const b = await req.json().catch(() => ({}));
    // Cloudflare retira modelos con el tiempo: se prueba una lista hasta que uno responda.
    const modelos = [env.AI_MODEL, '@cf/meta/llama-3.3-70b-instruct-fp8-fast', '@cf/meta/llama-4-scout-17b-16e-instruct', '@cf/mistralai/mistral-small-3.1-24b-instruct'].filter(Boolean);
    let texto = '', fallo = '';
    for (const modelo of modelos) {
      try {
        const r = await env.AI.run(modelo, {
          messages: [
            { role: 'system', content: String(b.sistema || '').slice(0, 2000) },
            { role: 'user', content: String(b.pedido || '').slice(0, 1000) },
          ],
          max_tokens: 400,
          temperature: 1,
        });
        texto = r?.response ?? r?.choices?.[0]?.message?.content ?? '';
        if (texto && typeof texto === 'object') texto = JSON.stringify(texto);
        if (texto) break;
      } catch (e) {
        fallo = String(e.message || e).slice(0, 200);
      }
    }
    if (!texto) return json({ error: 'La IA no respondió. ' + (fallo || 'Puede haberse agotado la cuota gratuita de hoy.') }, 502);
    return json({ texto });
  }

  if (p === '/api/imagen' && m === 'POST') {
    if (!env.AI) return json({ error: 'La IA gratuita no está activada en el servidor' }, 501);
    const b = await req.json().catch(() => ({}));
    const r = await env.AI.run(env.AI_IMAGE_MODEL || '@cf/black-forest-labs/flux-1-schnell', { prompt: String(b.descripcion || '').slice(0, 1500), steps: 4 });
    let b64 = typeof r?.image === 'string' ? r.image : null;
    if (!b64 && r) {
      const buf = new Uint8Array(await new Response(r).arrayBuffer());
      let bin = '';
      for (let i = 0; i < buf.length; i += 0x8000) bin += String.fromCharCode(...buf.subarray(i, i + 0x8000));
      b64 = btoa(bin);
    }
    if (!b64) return json({ error: 'La IA no devolvió imagen. Puede haberse agotado la cuota gratuita de hoy.' }, 502);
    return json({ imagen: 'data:image/jpeg;base64,' + b64 });
  }

  if (p === '/api/tiktok/token' && m === 'POST') {
    const b = await req.json().catch(() => null);
    if (!b?.access_token) return json({ error: 'Falta access_token' }, 400);
    await ajuste(env, 'tiktok', JSON.stringify({ access_token: b.access_token, refresh_token: b.refresh_token || null, expira: Date.now() + (Number(b.expires_in) || 86400) * 1000 }));
    return json({ ok: true });
  }
  return json({ error: 'Ruta desconocida' }, 404);
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS });
    try {
      if (url.pathname.startsWith('/media/') && (req.method === 'GET' || req.method === 'HEAD')) return serveMedia(req, env, url.pathname.slice(7));
      if (url.pathname.startsWith('/api/')) return await api(req, env, url);
      return new Response('LOQUIPAPAS · publicador activo', { headers: CORS });
    } catch (e) {
      return json({ error: String(e.message || e) }, 500);
    }
  },

  // Cada 5 minutos: publica lo que ya llegó a su hora y limpia archivos viejos.
  async scheduled(event, env) {
    await preparar(env);
    const origen = env.PUBLIC_URL || (await ajuste(env, 'origen'));
    if (!origen) return;
    const ahora = Date.now();
    const due = await env.DB.prepare("SELECT * FROM posts WHERE estado IN ('programado','procesando') AND cuando<=? ORDER BY cuando LIMIT 5").bind(ahora).all();
    for (const f of due.results) await procesar(env, f, origen.replace(/\/$/, ''));
    const viejos = await env.DB.prepare("SELECT id,media FROM posts WHERE estado='publicado' AND cuando<? AND media!='[]' LIMIT 5").bind(ahora - 3 * 86400000).all();
    for (const f of viejos.results) {
      for (const k of JSON.parse(f.media)) await mediaDel(env, k);
      await env.DB.prepare("UPDATE posts SET media='[]' WHERE id=?").bind(f.id).run();
    }
  },
};
