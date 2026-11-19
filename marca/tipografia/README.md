# Tipografías de Loquipapas

| Fuente | Uso | Licencia | Descarga completa |
|---|---|---|---|
| Luckiest Guy | Nombre, titulares y llamados. Mayúsculas con sombra dura. | Apache 2.0 | https://fonts.google.com/specimen/Luckiest+Guy |
| Permanent Marker | Descriptor y frase de remate. Minúsculas, inclinada. | Apache 2.0 | https://fonts.google.com/specimen/Permanent+Marker |
| Work Sans (500, 700, 900) | Todo el texto de lectura. | SIL Open Font License 1.1 | https://fonts.google.com/specimen/Work+Sans |

## Archivos

- `fuentes/*.ttf`: para instalar en el computador y usar en Canva, Illustrator, Photoshop, Word o cualquier programa.
- `fuentes/*.woff2`: para sitios web.
- `fuentes/LICENCIA-*.txt`: el texto de cada licencia. Las tres permiten uso comercial.

Los archivos incluidos traen el alfabeto latino básico (suficiente para español, con tildes, ñ y signos de apertura). Si necesitas otros idiomas, descarga la familia completa desde el enlace de la tabla.

## En una página web

```html
<link href="https://fonts.googleapis.com/css2?family=Luckiest+Guy&family=Permanent+Marker&family=Work+Sans:wght@500;700;900&display=swap" rel="stylesheet">
```

```css
.titular { font-family: "Luckiest Guy", sans-serif; text-transform: uppercase; line-height: .95; color: #E2412B; text-shadow: .045em .045em 0 #1B1726; }
.remate  { font-family: "Permanent Marker", cursive; transform: rotate(-3deg); }
.texto   { font-family: "Work Sans", system-ui, sans-serif; font-weight: 500; }
```
