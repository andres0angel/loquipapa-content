# LOQUIPAPAS · generador y publicador de contenido

Dos piezas que trabajan juntas:

| Parte | Qué hace | Dónde corre | Costo |
|---|---|---|---|
| `index.html` | Crea reels, posts, carruseles, historias, guiones e ideas con la identidad de Loquipapas. Lleva el calendario. | En el navegador (Chrome de escritorio) | Gratis |
| `worker/` | Guarda los archivos, los programa y los publica en Instagram, Facebook y TikTok a la hora elegida. | Cloudflare Workers | Plan gratuito |

El generador funciona solo: se puede abrir con doble clic y descargar las piezas sin instalar nada. El publicador es opcional y solo hace falta para programar publicaciones automáticas.

## 1. Poner el generador en internet (GitHub Pages)

1. En GitHub abre este repositorio → **Settings** → **Pages**.
2. En **Source** elige **Deploy from a branch**, rama `main`, carpeta `/ (root)`, y guarda.
3. En uno o dos minutos queda en `https://andres0angel.github.io/loquipapa-content/`.

## 2. Crear el servidor de publicación (Cloudflare)

Necesitas una cuenta gratuita de Cloudflare y Node.js instalado.

```bash
cd worker
npm install
npx wrangler login

# Base de datos y almacén de archivos
npx wrangler d1 create loquipapas
npx wrangler kv namespace create MEDIA_KV
```

Cada comando imprime un identificador. Pégalos en `worker/wrangler.toml`, en `database_id` y en el `id` de `kv_namespaces`. Luego:

```bash
npm run db                 # crea las tablas
npx wrangler secret put APP_TOKEN   # inventa una clave larga; es la que escribes en la app
npm run deploy
```

El despliegue muestra la dirección del servidor, parecida a `https://loquipapas-publicador.TU-USUARIO.workers.dev`. Cópiala en `PUBLIC_URL` dentro de `wrangler.toml` y ejecuta `npm run deploy` otra vez.

En el generador abre **Conexiones**, escribe esa dirección y la clave, y pulsa **Probar conexión**.

## 3. Conectar las redes

Sin este paso el servidor guarda y programa, pero marca cada publicación con el error "Esta red no está conectada".

### Instagram y Facebook

1. Convierte la cuenta de Instagram en **profesional** y enlázala a la **página de Facebook** del negocio.
2. En [developers.facebook.com](https://developers.facebook.com) crea una app de tipo negocio y añade los permisos `pages_manage_posts`, `pages_read_engagement`, `instagram_basic` e `instagram_content_publish`.
3. Genera un token de usuario de larga duración y, con él, el **token de la página** (consulta `me/accounts`). El token de página obtenido así no vence.
4. Anota el identificador de la página y el de la cuenta de Instagram (`{page-id}?fields=instagram_business_account`).

```bash
npx wrangler secret put META_PAGE_TOKEN
npx wrangler secret put FB_PAGE_ID
npx wrangler secret put IG_USER_ID
```

### TikTok

1. En [developers.tiktok.com](https://developers.tiktok.com) crea una app con el producto **Content Posting API** y el permiso `video.publish`.
2. Verifica en esa app el dominio de tu servidor (TikTok lo exige para descargar el video desde una dirección web).
3. Autoriza tu cuenta y guarda los tokens en el servidor:

```bash
npx wrangler secret put TIKTOK_CLIENT_KEY
npx wrangler secret put TIKTOK_CLIENT_SECRET
curl -X POST https://TU-SERVIDOR/api/tiktok/token \
  -H "Authorization: Bearer TU_CLAVE" -H "Content-Type: application/json" \
  -d '{"access_token":"...","refresh_token":"...","expires_in":86400}'
```

Mientras TikTok no apruebe la app, los videos quedan **privados** en la cuenta (`TIKTOK_PRIVACY = "SELF_ONLY"`). Después de la aprobación cambia ese valor a `PUBLIC_TO_EVERYONE` en `wrangler.toml`.

### WhatsApp

WhatsApp no ofrece una forma oficial de publicar estados automáticamente. El calendario genera un recordatorio para el calendario del celular y la pieza queda lista para subirla a mano.

## Cómo funciona por dentro

- El generador dibuja cada pieza con código sobre un lienzo; no usa inteligencia artificial. Los videos se graban en el navegador en tiempo real.
- Al programar, el generador sube el archivo al servidor (`POST /api/media`) y crea la publicación (`POST /api/posts`).
- Cada 5 minutos el servidor revisa qué publicaciones ya llegaron a su hora y las envía a cada red. Instagram procesa los videos en dos pasos, así que un reel puede tardar hasta 10 minutos en aparecer.
- Los archivos se borran del servidor 3 días después de publicados.

## Límites conocidos

- Cada archivo puede pesar hasta 25 MB (límite de KV). Para archivos más grandes activa R2 en `wrangler.toml`.
- Las redes exigen video en MP4. Chrome de escritorio actualizado lo graba así; si el navegador solo puede grabar en WebM, la app lo avisa y no lo sube.
- La publicación en Instagram, Facebook y TikTok se probó contra un servicio simulado, no contra las redes reales. La primera publicación real conviene hacerla con una pieza de prueba.
- El calendario vive en el navegador donde se creó. Usa **Descargar copia** para respaldarlo.
