# LOQUIPAPAS · generador y publicador de contenido

| Parte | Qué hace | Dónde está | Costo |
|---|---|---|---|
| `index.html` | Crea reels, posts, carruseles, historias, guiones e ideas con la identidad de Loquipapas. Lleva el calendario. | https://andres0angel.github.io/loquipapa-content/ | Gratis (GitHub Pages) |
| `worker/` | Guarda los archivos, los programa y los publica en Instagram, Facebook y TikTok. Da textos e imágenes con IA gratuita. | https://loquipapas-publicador.loquipapas.workers.dev | Gratis (Cloudflare, plan Free) |

No hay pagos mensuales. Todo corre dentro de los cupos gratuitos de GitHub y Cloudflare.

## Identidad de marca

La carpeta [`marca/`](marca/) tiene el manual completo y todos los archivos de la marca: logo, Loqui, colores, tipografías, iconos, patrones, plantillas para imprimir y para redes, y animaciones. Manual en línea: https://andres0angel.github.io/loquipapa-content/marca/

## Estado actual

- **Funcionando:** la app publicada, el servidor desplegado, la base de datos (D1 `loquipapas`), el almacén de archivos (KV `loquipapas-media`) y la tarea que revisa cada 5 minutos qué toca publicar.
- **Despliegue automático:** cada cambio en la rama `main` actualiza la app y el servidor sin hacer nada más.
- **Pendiente:** conectar Instagram, Facebook y TikTok (sección 2). Hasta entonces las publicaciones programadas quedan guardadas y se marcan "Esta red no está conectada".

## 1. Uso diario

1. Abre la app y entra a **Conexiones**. La dirección del servidor ya viene escrita; escribe la clave de la app (`APP_TOKEN`) y pulsa **Probar conexión**.
2. En **Crear** elige pieza, estilo, campaña, escena y producto. Ajusta los textos o pide sugerencias.
3. **Descargar** baja el archivo. **Guardar en calendario** deja la idea con fecha. **Programar publicación** crea el archivo, lo sube y queda en cola.
4. En **Calendario**, **Crear plan de 14 días** arma dos semanas de borradores y **Actualizar estado** trae el resultado de cada publicación.

## 2. Conectar las redes

### Instagram y Facebook

1. Convierte la cuenta de Instagram en **profesional** y enlázala a la **página de Facebook** del negocio.
2. En [developers.facebook.com](https://developers.facebook.com) crea una app de tipo negocio con los permisos `pages_manage_posts`, `pages_read_engagement`, `instagram_basic` e `instagram_content_publish`.
3. Genera un token de usuario de larga duración y, con él, el **token de la página** (consulta `me/accounts`).
4. Anota el identificador de la página y el de la cuenta de Instagram (`{page-id}?fields=instagram_business_account`).
5. En Cloudflare → `loquipapas-publicador` → **Settings** → **Variables and secrets**, agrega como secretos: `META_PAGE_TOKEN`, `FB_PAGE_ID` e `IG_USER_ID`.

### TikTok

1. En [developers.tiktok.com](https://developers.tiktok.com) crea una app con **Content Posting API** y el permiso `video.publish`.
2. Verifica en esa app el dominio del servidor (TikTok lo exige para descargar el video desde una dirección web).
3. Agrega en Cloudflare los secretos `TIKTOK_CLIENT_KEY` y `TIKTOK_CLIENT_SECRET`, autoriza tu cuenta y guarda los tokens:

```bash
curl -X POST https://loquipapas-publicador.loquipapas.workers.dev/api/tiktok/token \
  -H "Authorization: Bearer TU_CLAVE" -H "Content-Type: application/json" \
  -d '{"access_token":"...","refresh_token":"...","expires_in":86400}'
```

Mientras TikTok no apruebe la app, los videos quedan **privados** (`TIKTOK_PRIVACY = "SELF_ONLY"` en `worker/wrangler.toml`). Después de la aprobación cámbialo a `PUBLIC_TO_EVERYONE`.

### WhatsApp

WhatsApp no ofrece una forma oficial de publicar estados automáticamente. El calendario genera un recordatorio para el calendario del celular y la pieza queda lista para subirla a mano.

## 3. IA gratuita

El servidor usa Workers AI de Cloudflare, que incluye un cupo diario sin costo:

- **Sugerir con IA:** textos nuevos para el gancho, las líneas, el remate y el llamado.
- **Crear foto con IA gratis:** una foto de comida para los posts e historias de estilo humanista.

Si el cupo del día se agota, la app avisa y sigue funcionando con su banco propio de textos. Las fotos hechas con IA son inventadas: deben parecerse a lo que se vende y las redes piden marcarlas como contenido generado con IA.

## Cómo funciona por dentro

- El generador dibuja cada pieza con código sobre un lienzo. Los videos se graban en el navegador en tiempo real.
- Al programar, la app sube el archivo (`POST /api/media`) y crea la publicación (`POST /api/posts`).
- Cada 5 minutos el servidor envía a cada red lo que ya llegó a su hora. Instagram procesa los videos en dos pasos, así que un reel puede tardar hasta 10 minutos.
- Los archivos se borran del servidor 3 días después de publicados.
- El servidor crea sus tablas solo la primera vez y recuerda su dirección pública.

## Límites conocidos

- Cada archivo puede pesar hasta 25 MB. Para más, activa R2 en `worker/wrangler.toml`.
- Las redes exigen video en MP4. Chrome de escritorio actualizado lo graba así; si el navegador solo puede grabar en WebM, la app lo avisa y no lo sube.
- La publicación de posts, carruseles, reels e historias se probó contra un servicio simulado de Meta y TikTok, no contra las redes reales. La primera publicación real conviene hacerla con una pieza de prueba.
- Las historias se publican solo en Instagram. A TikTok solo van videos.
- El calendario vive en el navegador donde se creó. Usa **Descargar copia** para respaldarlo.

## Desarrollo local del servidor

```bash
cd worker
npm install
npx wrangler dev
```
