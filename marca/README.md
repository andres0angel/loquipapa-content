# Identidad de marca de LOQUIPAPAS

Todo lo necesario para producir cualquier pieza de la marca: del menú al aviso de la calle, de un post a un video.

**Empieza por el manual:** abre [`index.html`](index.html) o entra a https://andres0angel.github.io/loquipapa-content/marca/. También está en PDF: [`manual-de-marca.pdf`](manual-de-marca.pdf).

## Qué hay

| Carpeta o archivo | Contenido | Formatos |
|---|---|---|
| [`index.html`](index.html) · [`manual-de-marca.pdf`](manual-de-marca.pdf) | Manual completo: esencia, logo, color, tipografía, Loqui, gráficos, iconos, foto y video, voz, aplicaciones, movimiento, redes | HTML, PDF |
| [`logo/`](logo/) | Principal, una línea, una tinta, avatar, isotipo, favicon | SVG, PNG |
| [`mascota/`](mascota/) | Loqui: 8 expresiones y 3 poses de cuerpo entero | SVG, PNG |
| [`colores/`](colores/) | Paleta | JSON, CSS, ASE, GPL |
| [`tipografia/`](tipografia/) | Luckiest Guy, Permanent Marker, Work Sans, con licencias | TTF, WOFF2 |
| [`iconos/`](iconos/) | 16 iconos | SVG, PNG |
| [`patrones/`](patrones/) | Rayos, confeti de papas, cuadros, puntos, bordes de queso | SVG, PNG |
| [`plantillas/`](plantillas/) | Menú, póster, aviso, volante, tarjeta, stickers, empaques, uniforme, señalética, redes | PDF, PNG, HTML |
| [`animaciones/`](animaciones/) | 7 animaciones hechas con código | HTML, MP4, GIF |
| [`voz-y-tono.md`](voz-y-tono.md) | Guía de escritura y banco de frases | Markdown |
| [`PROMPT-MARCA.md`](PROMPT-MARCA.md) | Contexto de marca para pegar en cualquier IA | Markdown |
| [`marca.json`](marca.json) | La identidad completa como datos | JSON |
| [`fuente/`](fuente/) | Programas que generan todo | Python, JavaScript |

## Qué formato usar

- **Imprenta, aviso, bordado, corte de vinilo:** SVG o PDF. Son vectoriales: se agrandan sin perder calidad y las letras ya están convertidas a trazos.
- **Redes, presentaciones, Canva, Word:** PNG.
- **Sitio web:** SVG para logos e iconos, WOFF2 para fuentes, `colores/paleta.css` para los colores.
- **Video:** MP4 de `animaciones/`. El rótulo viene sobre fondo verde para recortarlo en el editor.
- **Adobe:** `colores/paleta.ase` carga los colores en Illustrator, Photoshop e InDesign.

## Editar una plantilla

1. **Sin programar:** abre el PDF en Illustrator, Affinity, Inkscape o Canva y cambia los textos entre corchetes.
2. **Con código:** edita el archivo de `plantillas/html/` y vuelve a exportar.

## Regenerar todo

Hace falta Python 3 con `fonttools`, Node.js y `ffmpeg`.

```bash
cd marca/fuente
npm install        # fuentes y navegador para exportar
python3 paso1.py   # logos, mascota, iconos, patrones, colores, fuentes
python3 paso2.py   # plantillas
python3 paso3.py   # animaciones
python3 paso4.py   # manual y documentos
node exportar.js               # PNG y PDF
node exportar-animaciones.js   # MP4 y GIF
```

`base.py` define los colores, el logo y a Loqui. Un cambio ahí se propaga a todos los archivos.

## Licencias y pendientes

- Las tres tipografías permiten uso comercial (Apache 2.0 y SIL OFL 1.1). Sus licencias están en `tipografia/fuentes/`.
- Los dibujos, el logo y la mascota se crearon para Loquipapas.
- Pendiente: revisar y registrar la marca ante la Superintendencia de Industria y Comercio, y completar usuario de redes, WhatsApp y menú.
