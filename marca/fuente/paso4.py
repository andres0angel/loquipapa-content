# Manual de marca (HTML), documentos de apoyo y datos para máquinas.
from base import *
import glob
pal = json.load(open(os.path.join(RAIZ, 'colores/paleta.json'), encoding='utf-8'))
DIR = 'Carrera 94 # 65C-01, 2º piso · Robledo, Medellín'
def lista(xs): return '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
def fig(src, pie, cls='', ancho=''):
    alt = re.sub(r'<small>.*?</small>', '', pie).replace('"', '')
    return f'<figure class="{cls}"><div class="marco"><img loading="lazy" src="{src}" alt="{alt}" style="{ancho}"></div><figcaption>{pie}</figcaption></figure>'
def nombres(carpeta, pref=''): return sorted(os.path.basename(x)[:-4] for x in glob.glob(os.path.join(RAIZ, carpeta, 'svg', pref + '*.svg')))

# ---------- Contenido de voz (se reutiliza en varios archivos) ----------
RASGOS = [('Loca', 'Exagerada a propósito. Si algo lleva queso, lleva mucho queso.'), ('Antojadora', 'Todo lo que dice o muestra debe dar hambre.'), ('Cercana', 'Habla como un amigo del barrio, de tú, sin tecnicismos.'), ('Generosa', 'Porciones grandes, humor abundante, cero tacañería.'), ('Segura', 'Frases cortas y afirmativas. No pide permiso para antojar.')]
SI = ['Frases cortas: una idea por línea.', 'Español neutro que se entiende en cualquier ciudad.', 'Humor exagerado sobre la comida y el antojo.', 'Verbos de acción: mira, prueba, sube, etiqueta, guarda.', 'Mayúsculas sostenidas solo en titulares.']
NO = ['Groserías o humor que se burle de personas.', 'Promesas que no se pueden cumplir ("las mejores del mundo").', 'Precios, fechas o promociones inventadas.', 'Textos largos sobre la imagen.', 'Signos de exclamación en fila o emojis en exceso.']
GANCHOS = ['NO VEAS ESTO CON HAMBRE', 'ADVERTENCIA: ANTOJO INMEDIATO', 'SI TIENES DIETA, SIGUE DE LARGO', 'PAUSA. MIRA ESTE QUESO.', 'TU ANTOJO TE ESTÁ BUSCANDO', '¿Y ESTE LOCO QUIÉN ES?', 'RESPONDE SIN PENSAR', 'ESTO VA A GENERAR PELEA', 'PARA DOS. O PARA UNO CON GANAS.', 'PELADA HOY. FRITA HOY.', 'LA CARA LO DICE TODO', 'ES QUINCENA. YA SABES.']
REMATES = ['con queso hasta donde aguante', 'recién hechas, como debe ser', 'crocantes por fuera, suaves por dentro', 'papa de nacimiento, loco por vocación', 'compartir es opcional', 'nada de congelados']
LLAMADOS = ['ETIQUETA AL QUE TE LAS DEBE', 'MÁNDALE ESTO AL QUE INVITA', 'GUÁRDALO PARA EL ANTOJO', 'SUBE AL 2º PISO', 'COMENTA TU EQUIPO', 'PÍDELO POR WHATSAPP']
HASHTAGS = '#Loquipapas #PapasLocas #Salchipapas #Robledo #Medellin #ComidaRapida'
MOV = [('Caída con rebote', 'Las letras y los ingredientes caen desde arriba y rebotan una vez.', '0,55 s · cubic-bezier(.3, 1.6, .5, 1)'), ('Golpe', 'Los titulares entran grandes y se asientan de un golpe.', '0,32 s · de escala 2,6 a 1'), ('Chorreo', 'El queso crece de arriba hacia abajo, nunca aparece de repente.', '1 s · cubic-bezier(.2, .9, .3, 1)'), ('Brote', 'Loqui aparece girando desde cero, como si saltara.', '0,6 s · cubic-bezier(.3, 1.7, .5, 1)'), ('Vida', 'Loqui nunca está quieto: parpadea, mueve la lengua y el pelo.', 'Ciclo de 4 s que empata con sí mismo'), ('Rayos', 'El fondo de rayos gira muy lento para dar energía sin distraer.', '32 s por vuelta, lineal')]
APLIC = [('menu-carta-A4', 'Menú carta', 'A4 vertical'), ('poster-calle-50x70', 'Póster de calle', '50 × 70 cm'), ('aviso-fachada-3x1', 'Aviso de fachada', 'Proporción 3 : 1'), ('volante-A5', 'Volante', 'A5'), ('tarjeta-fidelidad-frente', 'Tarjeta de fidelidad, frente', '9 × 5,5 cm'), ('tarjeta-fidelidad-respaldo', 'Tarjeta de fidelidad, respaldo', '9 × 5,5 cm'), ('sticker-sello-7cm', 'Sticker sello', '7 cm'), ('sticker-loqui-6cm', 'Sticker Loqui troquelado', '6 cm'), ('empaques-referencia', 'Empaques', 'Referencia visual'), ('uniforme-referencia', 'Uniforme', 'Referencia visual'), ('senaletica', 'Señalética del local', 'Hoja A4'), ('redes-post-1080x1350', 'Post', '1080 × 1350 px'), ('redes-historia-1080x1920', 'Historia o reel', '1080 × 1920 px'), ('redes-portada-1640x624', 'Portada de Facebook', '1640 × 624 px'), ('redes-destacadas', 'Portadas de destacadas', '6 círculos')]
ANIMS = [('logo-entrada', 'Entrada del logo', True), ('loqui-vivo', 'Loqui vivo (bucle)', True), ('loqui-expresiones', 'Sticker de expresiones', True), ('cargando', 'Cargando', True), ('cierre-video', 'Cierre de video', False), ('transicion-queso', 'Transición de queso', False), ('rotulo-inferior', 'Rótulo para presentar personas', False)]
LOGOS = [('loquipapas-principal-fondo-crema', 'Principal sobre crema', 'La versión oficial. Úsala siempre que haya espacio.'), ('loquipapas-principal-fondo-amarillo', 'Principal sobre amarillo', 'Para piezas de antojo y fondos de rayos.'), ('loquipapas-principal-fondo-rojo', 'Principal sobre rojo', 'Para empaques y fondos rojos.'), ('loquipapas-principal-fondo-noche', 'Principal sobre noche', 'Para aviso luminoso y piezas nocturnas.'), ('loquipapas-linea-fondo-crema', 'Una línea', 'Encabezados, firmas, formatos horizontales.'), ('loquipapas-linea-fondo-noche', 'Una línea sobre noche', 'Fachada y camiseta.'), ('loquipapas-una-tinta-negro', 'Una tinta, negro', 'Sellos, facturas, grabado, fotocopias.'), ('loquipapas-avatar-rojo', 'Avatar', 'Foto de perfil en redes.'), ('loquipapas-isotipo', 'Isotipo: Loqui', 'Cuando el nombre ya está cerca o el espacio es mínimo.')]
MAL = [('transform:scaleX(1.45)', 'No lo estires ni lo aplastes'), ('filter:hue-rotate(110deg)', 'No cambies los colores'), ('transform:rotate(-24deg) scale(.8)', 'No lo gires'), ('filter:drop-shadow(0 0 14px #000) blur(1px)', 'No le pongas sombras, brillos ni desenfoques'), ('opacity:.35', 'No lo uses transparente'), ('', 'No lo pongas sobre fondos recargados')]

# ---------- Manual ----------
sw = ''.join(f'''<div class="sw"><div class="col" style="background:{c["hex"]};{"border:3px solid #1B1726" if c["id"] in ("crema", "papa", "queso") else ""}"></div><h4>{c["nombre"]}</h4><p class="uso">{c["uso"]}</p>
<dl><dt>HEX</dt><dd>{c["hex"]}</dd><dt>RGB</dt><dd>{", ".join(map(str, c["rgb"]))}</dd><dt>CMYK</dt><dd>{", ".join(map(str, c["cmyk_aprox"]))}</dd><dt>HSL</dt><dd>{c["hsl"][0]}°, {c["hsl"][1]}%, {c["hsl"][2]}%</dd></dl></div>''' for c in pal['principal'])
swi = ''.join(f'<div class="swi"><i style="background:{c["hex"]}"></i><b>{c["nombre"]}</b><span>{c["hex"]}</span></div>' for c in pal['ilustracion'])
NOMC = {c['id']: c['nombre'] for c in pal['principal']}; HEX = {c['id']: c['hex'] for c in pal['principal']}
comb = ''.join(f'<div class="comb" style="background:{HEX[x["fondo"]]};color:{HEX[x["texto"]]}"><b>Aa</b><span>{NOMC[x["texto"]]} sobre {NOMC[x["fondo"]]}<br>{x["razon"]} : 1 · {x["sirve_para"]}</span></div>' for x in sorted(pal['contraste'], key=lambda x: -x['razon']) if x['razon'] >= 3)
malos = ''.join(f'<figure class="mal"><div class="marco" style="{"background:url(patrones/png/cuadros-picnic.png) center/60%" if not st else ""}"><img src="logo/png/loquipapas-principal-transparente.png" alt="" style="{st}"></div><figcaption>{t}</figcaption></figure>' for st, t in MAL)
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Manual de marca · Loquipapas</title>
<link rel="icon" href="logo/svg/favicon.svg">
<style>
@font-face{{font-family:"Luckiest Guy";src:url(tipografia/fuentes/LuckiestGuy-400.woff2) format("woff2");font-display:swap}}
@font-face{{font-family:"Permanent Marker";src:url(tipografia/fuentes/PermanentMarker-400.woff2) format("woff2");font-display:swap}}
@font-face{{font-family:"Work Sans";font-weight:500;src:url(tipografia/fuentes/WorkSans-500.woff2) format("woff2");font-display:swap}}
@font-face{{font-family:"Work Sans";font-weight:700;src:url(tipografia/fuentes/WorkSans-700.woff2) format("woff2");font-display:swap}}
@font-face{{font-family:"Work Sans";font-weight:900;src:url(tipografia/fuentes/WorkSans-900.woff2) format("woff2");font-display:swap}}
:root{{--crema:#FFF3D6;--rojo:#E2412B;--noche:#1B1726;--papa:#FFC21A;--queso:#FFD84A}}
*{{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--crema);color:var(--noche);font:500 17px/1.55 "Work Sans",system-ui,sans-serif}}
img{{max-width:100%;height:auto;display:block}}
a{{color:var(--rojo);font-weight:700}}a:hover{{color:var(--noche)}}
h1,h2,h3{{font-family:"Luckiest Guy",sans-serif;font-weight:400;line-height:1;margin:0;text-wrap:balance}}
h2{{font-size:clamp(40px,7vw,76px);color:var(--rojo);text-shadow:.045em .045em 0 var(--noche);margin-bottom:10px}}
h3{{font-size:clamp(24px,3.4vw,34px);margin:44px 0 12px}}
h4{{font-size:18px;font-weight:900;margin:0 0 4px}}
p{{margin:0 0 14px;max-width:68ch}}ul{{margin:0 0 14px;padding-left:22px;max-width:68ch}}li{{margin-bottom:5px}}
.num{{font-family:"Permanent Marker",cursive;font-size:24px;display:inline-block;transform:rotate(-4deg);margin-bottom:6px}}
.intro{{font-size:20px;font-weight:700;max-width:60ch}}
nav{{position:sticky;top:0;z-index:5;background:var(--noche);padding:10px 16px;display:flex;gap:6px 16px;flex-wrap:wrap;align-items:center}}
nav a{{color:var(--crema);text-decoration:none;font-size:14px;font-weight:700;padding:6px 2px}}nav a:hover{{color:var(--papa)}}nav img{{height:30px;margin-right:8px}}
header.portada{{background:var(--papa) url(patrones/svg/rayos-amarillo.svg) center/cover;padding:8vh 16px 0;text-align:center;border-bottom:8px solid var(--noche);overflow:hidden}}
header.portada img.logo{{width:min(620px,86vw);margin:0 auto}}header.portada p{{font-family:"Permanent Marker",cursive;font-size:clamp(22px,4vw,38px);margin:10px auto 0;transform:rotate(-3deg)}}
header.portada img.loqui{{width:min(360px,60vw);margin:24px auto -6px}}
section{{padding:72px 16px;border-bottom:4px solid var(--noche)}}section>.in{{max-width:1120px;margin:0 auto}}
section.rojo{{background:var(--rojo);color:var(--crema)}}section.rojo h2{{color:var(--crema)}}section.rojo a{{color:var(--papa)}}
section.noche{{background:var(--noche);color:var(--crema)}}section.noche h2{{color:var(--papa);text-shadow:.045em .045em 0 var(--rojo)}}section.noche a{{color:var(--papa)}}
section.amarillo{{background:var(--papa)}}
.g{{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(min(100%,var(--m,240px)),1fr));margin:18px 0}}
figure{{margin:0;min-width:0}}.marco{{background:#fff;border:3px solid var(--noche);border-radius:16px;overflow:hidden;display:flex;align-items:center;justify-content:center;aspect-ratio:var(--ar,4/3);padding:var(--pad,0)}}
.marco img{{max-height:100%;object-fit:contain}}figcaption{{font-size:14px;font-weight:700;margin-top:6px;line-height:1.3}}figcaption small{{display:block;font-weight:500;opacity:.85}}
.cuadros .marco{{background:repeating-conic-gradient(#fff 0 25%,#EFE6CF 0 50%) 0 0/24px 24px}}
.tarj{{background:#fff;color:var(--noche);border:3px solid var(--noche);border-radius:16px;padding:18px}}.tarj p:last-child,.tarj ul:last-child{{margin-bottom:0}}
.sw .col{{height:120px;border-radius:14px}}.sw h4{{margin-top:10px}}.sw .uso{{font-size:14px;margin-bottom:8px;min-height:3.1em}}
dl{{display:grid;grid-template-columns:auto 1fr;gap:2px 10px;margin:0;font-size:14px}}dt{{font-weight:900}}dd{{margin:0;font-variant-numeric:tabular-nums}}
.swi{{display:flex;align-items:center;gap:10px;font-size:14px}}.swi i{{width:38px;height:38px;border-radius:10px;border:2px solid var(--noche);flex:none}}.swi b{{flex:1}}
.comb{{border:3px solid var(--noche);border-radius:14px;padding:14px;display:flex;gap:14px;align-items:center}}.comb b{{font-family:"Luckiest Guy";font-size:44px;font-weight:400;line-height:1}}.comb span{{font-size:13px;font-weight:700;line-height:1.3}}
.prop{{display:flex;height:64px;border:3px solid var(--noche);border-radius:14px;overflow:hidden;margin:14px 0;font-size:13px;font-weight:900}}.prop div{{display:flex;align-items:center;justify-content:center;text-align:center;padding:2px}}
.espec{{background:#fff;color:var(--noche);border:3px solid var(--noche);border-radius:16px;padding:22px;overflow:hidden}}
.mal .marco{{position:relative}}.mal .marco::after{{content:"✕";position:absolute;right:8px;top:4px;font:900 30px "Work Sans";color:var(--rojo)}}
.resp{{position:relative;display:inline-block;padding:9%;border:3px dashed var(--rojo);background:#fff;border-radius:8px;max-width:520px}}.resp::before{{content:"x";position:absolute;left:3%;top:42%;font-weight:900;color:var(--rojo)}}.resp::after{{content:"x";position:absolute;left:48%;top:1%;font-weight:900;color:var(--rojo)}}
table{{border-collapse:collapse;width:100%;font-size:15px;background:#fff;color:var(--noche);border:3px solid var(--noche)}}th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid #D9CFB6;vertical-align:top}}th{{background:var(--noche);color:var(--crema)}}
.tabla{{overflow-x:auto;margin:14px 0}}code{{background:#fff;color:var(--noche);border:1px solid #CFC4A8;border-radius:6px;padding:1px 6px;font-size:14px;word-break:break-word}}
.chips{{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 18px}}.chips span{{background:var(--crema);color:var(--noche);border:3px solid var(--noche);border-radius:99px;padding:6px 14px;font-weight:900;font-size:15px}}
.frase{{font-family:"Permanent Marker",cursive;font-size:24px;transform:rotate(-2deg);display:inline-block}}
footer{{padding:40px 16px;text-align:center;background:var(--noche);color:var(--crema);font-size:14px}}
@media print{{nav{{display:none}}section{{padding:30px 0;break-inside:auto}}h2,h3{{break-after:avoid}}figure,.tarj,.sw,.comb{{break-inside:avoid}}body{{font-size:13px}}header.portada{{padding-top:60px}}@page{{size:A4;margin:14mm}}}}
</style></head><body>
<nav aria-label="Secciones del manual"><img src="logo/svg/loquipapas-linea-transparente-claro.svg" alt="Loquipapas">
<a href="#esencia">Esencia</a><a href="#logo">Logo</a><a href="#color">Color</a><a href="#tipografia">Tipografía</a><a href="#loqui">Loqui</a><a href="#graficos">Gráficos</a><a href="#iconos">Iconos</a><a href="#foto">Foto y video</a><a href="#voz">Voz</a><a href="#aplicaciones">Aplicaciones</a><a href="#movimiento">Movimiento</a><a href="#redes">Redes</a><a href="#archivos">Archivos</a></nav>
<header class="portada"><img class="logo" src="logo/svg/loquipapas-principal-transparente.svg" alt="Loquipapas, papas locas"><p>Manual de identidad de marca</p><img class="loqui" src="mascota/svg/loqui-cuerpo-saludo.svg" alt="Loqui saluda con una cajita de papas"></header>

<section id="esencia"><div class="in"><span class="num">01</span><h2>Esencia</h2>
<p class="intro">Loquipapas es comida rápida de barrio hecha con locura: papas, salchipapas, perros y hamburguesas con queso hasta donde aguante, en un segundo piso de Robledo, Medellín.</p>
<div class="g" style="--m:300px"><div class="tarj"><h4>Promesa</h4><p>Porciones generosas, recién hechas, que dan antojo desde que las ves.</p></div><div class="tarj"><h4>Público</h4><p>Jóvenes y estudiantes de 18 a 28 años que deciden qué comer mirando el celular y salen en plan con amigos.</p></div><div class="tarj"><h4>Posición</h4><p>La opción más divertida y cargada del sector. No compite por ser la más fina, sino la más antojadora.</p></div><div class="tarj"><h4>El nombre</h4><p>"Loqui" es el loco de la casa: la mascota. "Papas" es lo que hacemos. El descriptor "papas locas" explica el producto a quien no nos conoce.</p></div></div>
<h3>Personalidad</h3><div class="g" style="--m:200px">{"".join(f'<div class="tarj"><h4>{a}</h4><p>{b}</p></div>' for a, b in RASGOS)}</div>
<h3>Los cinco elementos que hacen la marca</h3>{lista(['<b>El letrero:</b> letras gruesas rojas, cada una un poco torcida, con sombra dura.', '<b>Loqui:</b> la cara loca que reemplaza la O.', '<b>El queso derretido:</b> chorrea sobre titulares y bordes.', '<b>El contorno noche:</b> todo dibujo lleva línea gruesa oscura.', '<b>Rojo, amarillo y crema:</b> siempre juntos, con noche como tinta.'])}</div></section>

<section id="logo" class="amarillo"><div class="in"><span class="num">02</span><h2>Logo</h2><p class="intro">El logo es un letrero: LOQUI arriba, PAPAS abajo, con Loqui como la letra O y queso derretido sobre PAPAS.</p>
<div class="g" style="--m:250px">{"".join(fig(f"logo/png/{a}.png", f"{b}<small>{c}</small>") for a, b, c in LOGOS)}</div>
<h3>Cuál usar</h3><div class="tabla"><table><tr><th>Situación</th><th>Versión</th></tr><tr><td>Hay espacio y el formato es vertical o cuadrado</td><td>Principal (apilado)</td></tr><tr><td>Formato horizontal, encabezados, firma de piezas</td><td>Una línea</td></tr><tr><td>Menos de 25 mm o 120 px de ancho</td><td>Isotipo (Loqui) o avatar</td></tr><tr><td>Una sola tinta: sello, factura, grabado, bordado simple</td><td>Una tinta, negro o blanco</td></tr><tr><td>Foto de perfil</td><td>Avatar sobre rojo</td></tr></table></div>
<h3>Área de respeto</h3><p>Deja alrededor del logo un espacio libre igual a la altura de la letra L (x). Nada entra en esa zona: ni texto, ni bordes, ni fotos.</p><div class="resp"><img src="logo/png/loquipapas-principal-transparente.png" alt="Logo con su área de respeto marcada"></div>
<h3>Tamaños mínimos</h3><div class="tabla"><table><tr><th>Versión</th><th>Impreso</th><th>Pantalla</th></tr><tr><td>Principal</td><td>30 mm de ancho</td><td>160 px</td></tr><tr><td>Una línea</td><td>35 mm de ancho</td><td>180 px</td></tr><tr><td>Isotipo</td><td>10 mm</td><td>32 px</td></tr></table></div>
<p>Por debajo de esos tamaños el queso y el descriptor dejan de leerse: usa el isotipo.</p>
<h3>Lo que no se hace</h3><div class="g" style="--m:160px">{malos}</div></div></section>

<section id="color"><div class="in"><span class="num">03</span><h2>Color</h2><p class="intro">Cinco colores. Rojo, amarillo y crema hacen el ruido; noche dibuja y escribe; queso da el brillo.</p>
<div class="g" style="--m:190px">{sw}</div><p><small>Los valores CMYK son una conversión de referencia. Antes de imprimir, pide prueba de color a la imprenta.</small></p>
<h3>Proporción</h3><p>En una pieza típica, el fondo ocupa la mayor parte y el rojo lleva el mensaje.</p>
<div class="prop"><div style="flex:45;background:var(--papa)">Papa o crema 45 %</div><div style="flex:25;background:var(--rojo);color:var(--crema)">Rojo 25 %</div><div style="flex:15;background:var(--crema)">Crema 15 %</div><div style="flex:10;background:var(--noche);color:var(--crema)">Noche 10 %</div><div style="flex:5;background:var(--queso)">5 %</div></div>
<h3>Combinaciones para texto</h3><p>Solo estas combinaciones tienen contraste suficiente. La razón indica cuánto se distingue el texto del fondo: desde 4,5 sirve para texto normal y desde 3 solo para títulos grandes.</p><div class="g" style="--m:240px">{comb}</div>
<p>Rojo sobre amarillo y crema sobre amarillo no alcanzan contraste por color: por eso los titulares rojos sobre amarillo siempre llevan <b>sombra dura noche</b>, que es la que los hace legibles.</p>
<h3>Colores de ilustración</h3><p>Solo para dibujar comida y a Loqui. No se usan en fondos ni en texto.</p><div class="g" style="--m:220px">{swi}</div></div></section>

<section id="tipografia" class="rojo"><div class="in"><span class="num">04</span><h2>Tipografía</h2><p class="intro">Tres letras, cada una con un trabajo.</p>
<div class="g" style="--m:320px">
<div class="espec"><h4>Luckiest Guy · titulares</h4><div style="font:400 64px/1 'Luckiest Guy';color:var(--rojo);text-shadow:.045em .045em 0 var(--noche);margin:10px 0">NO VEAS ESTO CON HAMBRE</div><p>Siempre en mayúsculas, con sombra dura. Para el nombre, titulares y llamados cortos. Máximo 6 palabras.</p></div>
<div class="espec"><h4>Permanent Marker · acento</h4><div style="font:400 40px/1.1 'Permanent Marker';margin:14px 0;transform:rotate(-3deg)">con queso hasta donde aguante</div><p>En minúsculas, inclinada entre 3° y 5°. Para el descriptor y la frase de remate. Una sola línea por pieza.</p></div>
<div class="espec"><h4>Work Sans · texto</h4><div style="font:900 26px/1.2 'Work Sans';margin:12px 0">Carrera 94 # 65C-01 · 2º piso</div><div style="font:500 17px/1.5 'Work Sans'">Para todo lo que hay que leer: direcciones, menú, descripciones. Peso 900 para datos importantes, 700 para subtítulos, 500 para párrafos.</div></div></div>
<h3>Reglas</h3>{lista(['<b>Sombra dura:</b> desplazada abajo y a la derecha un 4,5 % del tamaño de la letra, sin difuminar. En CSS: <code>text-shadow: .045em .045em 0 #1B1726</code>.', '<b>Jerarquía:</b> titular (Luckiest Guy) → remate (Marker) → dato (Work Sans 900). Nunca dos titulares compitiendo.', '<b>Interlineado de titulares:</b> 0,95. Las líneas van pegadas, como un letrero.', '<b>En el logo</b> cada letra va girada unos grados. En los titulares normales, no: se gira el bloque completo entre 2° y 3°.', '<b>No uses</b> otras fuentes, ni Luckiest Guy para párrafos, ni Marker en mayúsculas sostenidas.'])}
<p>Las tres fuentes son libres para uso comercial: Luckiest Guy y Permanent Marker bajo licencia Apache 2.0, Work Sans bajo SIL Open Font License 1.1. Los archivos para instalar están en <a href="tipografia/fuentes/">tipografia/fuentes</a>.</p></div></section>

<section id="loqui"><div class="in"><span class="num">05</span><h2>Loqui</h2><p class="intro">Loqui es una papa loca con pelo de papas fritas. Es la cara de la marca: aparece en el logo, presenta el contenido y habla en primera persona.</p>
<div class="g" style="--m:300px"><div class="tarj"><h4>Cómo es</h4>{lista(['Papa dorada, redonda e imperfecta.', 'Siete papas fritas por pelo, alternando clara y tostada.', 'Ojo izquierdo grande, ojo derecho pequeño, una ceja levantada.', 'Lengua afuera hacia un lado.', 'Contorno noche grueso en todo el dibujo.'])}</div><div class="tarj"><h4>Cómo se comporta</h4>{lista(['Exagerado, juguetón, siempre antojado.', 'Habla en español neutro, sin groserías.', 'Se burla de sí mismo, nunca de la gente.', 'Su saludo es la V con dos dedos.'])}</div><div class="tarj"><h4>Lo que nunca</h4>{lista(['No lleva gorra ni ropa.', 'No levanta un solo dedo: siempre dos, en V.', 'No cambia de color ni pierde el contorno.', 'No se dibuja como papa cruda, papa frita suelta ni salchicha.', 'No se usa en versión realista o en 3D.'])}</div></div>
<h3>Expresiones</h3><div class="g cuadros" style="--m:150px;--ar:1/1">{"".join(fig(f"mascota/png/loqui-{k}.png", EXPRESIONES[k][0]) for k in EXPRESIONES)}</div>
<h3>Cuerpo entero</h3><div class="g cuadros" style="--m:260px;--ar:8/7">{fig("mascota/png/loqui-cuerpo-saludo.png", "Saludo con cajita<small>La pose oficial</small>")}{fig("mascota/png/loqui-cuerpo-presenta.png", "Presentando<small>Para anunciar algo</small>")}{fig("mascota/png/loqui-cuerpo-antojado.png", "Con la cajita en alto<small>Para producto</small>")}</div>
<h3>Cuándo usar cada expresión</h3><div class="tabla"><table><tr><th>Expresión</th><th>Úsala para</th></tr><tr><td>Loco</td><td>Logo, avatar y todo uso general</td></tr><tr><td>Feliz</td><td>Agradecer, dar la bienvenida</td></tr><tr><td>Guiño</td><td>Complicidad, datos curiosos, tarjeta de fidelidad</td></tr><tr><td>Sorprendido</td><td>Novedades, ganchos de pregunta</td></tr><tr><td>Enamorado</td><td>Producto estrella, reseñas de clientes</td></tr><tr><td>Antojado</td><td>Fotos de comida, antojo</td></tr><tr><td>Dormido</td><td>Cerrado, fuera de horario</td></tr><tr><td>Picante</td><td>Salsas, retos, avisos de espera</td></tr></table></div></div></section>

<section id="graficos" class="amarillo"><div class="in"><span class="num">06</span><h2>Elementos gráficos</h2><p class="intro">Piezas que acompañan al logo y hacen que cualquier diseño se reconozca como Loquipapas aunque no aparezca el nombre.</p>
<div class="g" style="--m:210px;--ar:1/1">{"".join(fig(f"patrones/png/{n}.png", t) for n, t in [("rayos-amarillo", "Rayos<small>Fondo de energía. También en rojo, crema y noche.</small>"), ("papas-confeti-crema", "Confeti de papas<small>Empaques, fondos suaves.</small>"), ("papas-confeti-rojo", "Confeti sobre rojo"), ("cuadros-picnic", "Cuadros<small>Papel de bandeja, manteles.</small>"), ("puntos-amarillo", "Puntos<small>Detalle, cintas, bordes.</small>")])}</div>
<div class="g" style="--m:420px;--ar:6/1;--pad:12px">{fig("patrones/png/queso-borde-amarillo.png", "Borde de queso amarillo<small>Sobre titulares en fondo crema, rojo o noche.</small>")}{fig("patrones/png/queso-borde-crema.png", "Borde de queso crema<small>Sobre titulares en fondo amarillo.</small>")}</div>
<h3>Reglas de dibujo</h3>{lista(['<b>Contorno:</b> línea noche gruesa en todo objeto dibujado, con esquinas redondeadas.', '<b>Sombra dura:</b> los objetos y títulos proyectan una sombra sólida abajo a la derecha, sin difuminar.', '<b>Formas redondeadas:</b> botones y etiquetas en forma de píldora, tarjetas con esquinas de 16 a 34 px.', '<b>Queso:</b> siempre chorrea desde arriba. Tapa como máximo el tercio superior de las letras.', '<b>Un solo fondo fuerte por pieza:</b> rayos o confeti, no los dos.'])}</div></section>

<section id="iconos"><div class="in"><span class="num">07</span><h2>Iconos</h2><p class="intro">Dieciséis iconos con el mismo trazo que Loqui, para menú, señalética, redes y web.</p>
<div class="g cuadros" style="--m:110px;--ar:1/1;--pad:10px">{"".join(fig(f"iconos/svg/{n}.svg", n.replace("icono-", "").replace("-", " ").capitalize()) for n in nombres("iconos"))}</div>
<p>Para un icono nuevo: lienzo de 120 × 120, trazo noche de 6 de grosor con puntas redondas, y solo colores de la paleta.</p></div></section>

<section id="foto" class="noche"><div class="in"><span class="num">08</span><h2>Foto y video</h2><p class="intro">La comida real es lo que más vende. La ilustración da personalidad; la foto da hambre.</p>
<div class="g" style="--m:300px"><div class="tarj"><h4>Así sí</h4>{lista(['Primer plano: la comida llena el cuadro.', 'Recién servida, con vapor y queso brillante.', 'Luz cálida de lado; nunca la lámpara encima.', 'Caja roja con franja crema, bandeja roja, papel crema.', 'Manos y caras reales, sin posar.', 'Fondo oscuro o desenfocado para que resalten rojo y amarillo.'])}</div><div class="tarj"><h4>Así no</h4>{lista(['Platos fríos, queso opaco o papas blandas.', 'Flash directo o luz blanca de oficina.', 'Fotos de banco de imágenes.', 'Otras marcas visibles en el cuadro.', 'Filtros que cambien el color de la comida.', 'La obra o el local antes de estar terminado.'])}</div><div class="tarj"><h4>Video</h4>{lista(['Vertical 9:16, entre 8 y 25 segundos.', 'El primer segundo ya muestra comida o acción.', 'Debe entenderse sin sonido: texto corto en pantalla.', 'Cámara lenta para el queso y la fritura.', 'Tomas de 2 a 4 segundos, cortadas al ritmo.', 'Cierra con la caja al centro y el cierre de marca.'])}</div></div>
<h3>Contenido hecho con IA</h3><p>Se permite como apoyo, con tres condiciones: la comida debe parecerse a la que se vende, no se presenta como clientes reales, y al publicar se marca como contenido generado con IA. El texto base para pedir imágenes y videos está en <a href="PROMPT-MARCA.md">PROMPT-MARCA.md</a>.</p></div></section>

<section id="voz"><div class="in"><span class="num">09</span><h2>Voz y tono</h2><p class="intro">Loquipapas habla como un amigo que siempre tiene hambre y siempre invita.</p>
<div class="g" style="--m:320px"><div class="tarj"><h4>Así sí</h4>{lista(SI)}</div><div class="tarj"><h4>Así no</h4>{lista(NO)}</div></div>
<h3>Ganchos</h3><div class="chips">{"".join(f"<span>{g}</span>" for g in GANCHOS)}</div>
<h3>Remates</h3><p>{"".join(f'<span class="frase">{r}</span><br>' for r in REMATES)}</p>
<h3>Llamados a la acción</h3><div class="chips">{"".join(f"<span>{g}</span>" for g in LLAMADOS)}</div>
<h3>Antes y después</h3><div class="tabla"><table><tr><th>En vez de</th><th>Di</th></tr><tr><td>Ofrecemos deliciosas papas a la francesa con queso.</td><td>PAPAS. QUESO. MÁS QUESO.</td></tr><tr><td>Los invitamos a visitar nuestro establecimiento.</td><td>SUBE AL 2º PISO.</td></tr><tr><td>¡¡¡Las mejores salchipapas de Medellín!!!</td><td>NO VEAS ESTO CON HAMBRE.</td></tr><tr><td>Comparte esta publicación con tus amigos.</td><td>ETIQUETA AL QUE TE LAS DEBE.</td></tr></table></div>
<p>Etiquetas de base: <code>{HASHTAGS}</code>. La guía completa está en <a href="voz-y-tono.md">voz-y-tono.md</a>.</p></div></section>

<section id="aplicaciones" class="rojo"><div class="in"><span class="num">10</span><h2>Aplicaciones</h2><p class="intro">Plantillas listas. Cada una viene en PDF vectorial para imprenta, PNG para ver y HTML para editar. Los textos entre corchetes son los que se reemplazan.</p>
<div class="g" style="--m:230px;--ar:1/1;--pad:10px">{"".join(f'<figure><a href="plantillas/pdf/{a}.pdf"><div class="marco"><img loading="lazy" src="plantillas/png/{a}.png" alt="{b}"></div></a><figcaption>{b}<small>{c} · <a href="plantillas/pdf/{a}.pdf">PDF</a> · <a href="plantillas/png/{a}.png">PNG</a> · <a href="plantillas/html/{a}.html">HTML</a></small></figcaption></figure>' for a, b, c in APLIC)}</div>
<p>Los empaques y el uniforme son referencias visuales de cómo se aplica la marca, no planos de producción: la imprenta o el confeccionista ajusta medidas y troqueles.</p></div></section>

<section id="movimiento" class="amarillo"><div class="in"><span class="num">11</span><h2>Movimiento</h2><p class="intro">La marca se mueve como la comida: cae, rebota, chorrea. Todas las animaciones están hechas con código, así que se pueden editar, escalar sin perder calidad y usar en la web.</p>
<div class="g" style="--m:230px;--ar:1/1">{"".join(fig(f"animaciones/gif/{a}.gif", f'{b}<small><a href="animaciones/html/{a}.html">Ver en vivo</a> · <a href="animaciones/mp4/{a}.mp4">MP4</a> · <a href="animaciones/gif/{a}.gif">GIF</a></small>') for a, b, g_ in ANIMS if g_)}</div>
<div class="g" style="--m:200px">{"".join(f'<div class="tarj"><h4>{b}</h4><p><a href="animaciones/html/{a}.html">Ver en vivo</a> · <a href="animaciones/mp4/{a}.mp4">MP4</a></p></div>' for a, b, g_ in ANIMS if not g_)}</div>
<h3>Principios</h3><div class="tabla"><table><tr><th>Movimiento</th><th>Qué hace</th><th>Tiempo y curva</th></tr>{"".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in MOV)}</table></div>
{lista(['Nada aparece con fundido suave: las cosas entran con peso.', 'Un solo movimiento principal a la vez; el resto acompaña.', 'Los bucles duran 2 o 4 segundos para que empaten con el ritmo de la música.', 'Respeta a quien prefiere menos movimiento: las animaciones se detienen si el dispositivo lo pide.'])}</div></section>

<section id="redes"><div class="in"><span class="num">12</span><h2>Redes sociales</h2><p class="intro">Formatos, zonas seguras y ritmo de publicación.</p>
<div class="tabla"><table><tr><th>Pieza</th><th>Tamaño</th><th>Zona segura</th></tr><tr><td>Reel, historia, TikTok</td><td>1080 × 1920 px</td><td>Deja libres 250 px arriba y 250 px abajo</td></tr><tr><td>Post y carrusel</td><td>1080 × 1350 px</td><td>Margen de 70 px en todos los lados</td></tr><tr><td>Foto de perfil</td><td>512 × 512 px</td><td>Usa el avatar: la red lo recorta en círculo</td></tr><tr><td>Portada de Facebook</td><td>1640 × 624 px</td><td>Lo importante al centro</td></tr></table></div>
<h3>Ritmo semanal sugerido</h3><div class="tabla"><table><tr><th>Día</th><th>Pieza</th><th>Tema</th></tr><tr><td>Lunes</td><td>Reel</td><td>Antojo de producto</td></tr><tr><td>Martes</td><td>Historia</td><td>Interacción: esto o aquello</td></tr><tr><td>Miércoles</td><td>Carrusel</td><td>Loqui</td></tr><tr><td>Jueves</td><td>Reel grabado</td><td>Así se hace</td></tr><tr><td>Viernes</td><td>Reel</td><td>Plan de fin de semana</td></tr><tr><td>Sábado</td><td>Post</td><td>Clientes</td></tr><tr><td>Domingo</td><td>Historia</td><td>Antojo</td></tr></table></div>
<p>El <a href="../">generador de contenido</a> produce estas piezas con la identidad ya aplicada.</p></div></section>

<section id="archivos" class="noche"><div class="in"><span class="num">13</span><h2>Archivos</h2><p class="intro">Todo lo que entrega este manual y para qué sirve cada formato.</p>
<div class="tabla"><table><tr><th>Carpeta</th><th>Contenido</th><th>Formatos</th></tr>
<tr><td><a href="logo/">logo/</a></td><td>Principal, una línea, una tinta, avatar, isotipo y favicon</td><td>SVG (vector, para imprenta y web) y PNG a 2000 px</td></tr>
<tr><td><a href="mascota/">mascota/</a></td><td>Ocho expresiones y tres poses de cuerpo entero</td><td>SVG y PNG con fondo transparente</td></tr>
<tr><td><a href="colores/">colores/</a></td><td>Paleta completa</td><td>JSON, CSS, ASE (Adobe), GPL (GIMP, Inkscape)</td></tr>
<tr><td><a href="tipografia/">tipografia/</a></td><td>Las tres fuentes con sus licencias</td><td>TTF para instalar, WOFF2 para web</td></tr>
<tr><td><a href="iconos/">iconos/</a></td><td>Dieciséis iconos</td><td>SVG y PNG</td></tr>
<tr><td><a href="patrones/">patrones/</a></td><td>Rayos, confeti, cuadros, puntos, bordes de queso</td><td>SVG y PNG</td></tr>
<tr><td><a href="plantillas/">plantillas/</a></td><td>Menú, póster, aviso, volante, tarjeta, stickers, empaques, uniforme, señalética, redes</td><td>PDF vectorial, PNG, HTML editable</td></tr>
<tr><td><a href="animaciones/">animaciones/</a></td><td>Siete animaciones hechas con código</td><td>HTML (fuente), MP4, GIF</td></tr>
<tr><td><a href="voz-y-tono.md">voz-y-tono.md</a></td><td>Guía de escritura y banco de frases</td><td>Markdown</td></tr>
<tr><td><a href="PROMPT-MARCA.md">PROMPT-MARCA.md</a></td><td>Contexto de marca para pegar en cualquier IA</td><td>Markdown</td></tr>
<tr><td><a href="marca.json">marca.json</a></td><td>Toda la identidad en formato de datos</td><td>JSON</td></tr>
<tr><td><a href="fuente/">fuente/</a></td><td>Los programas que generan todo lo anterior</td><td>Python y JavaScript</td></tr></table></div>
<h3>Pendientes</h3>{lista(['Revisar y registrar "Loquipapas" en el registro de marcas de la Superintendencia de Industria y Comercio (clases 43, 29 y 30).', 'Reservar el usuario en Instagram, TikTok y Facebook, y reemplazar <code>[@usuario]</code> y <code>[número]</code> en las plantillas.', 'Completar nombres y precios del menú.', 'Pedir prueba de color a la imprenta antes del primer tiraje.'])}</div></section>
<footer>Manual de identidad de Loquipapas · {DIR}</footer></body></html>'''
out('index.html', html)

# ---------- Documentos de apoyo ----------
out('voz-y-tono.md', f'''# Voz y tono de Loquipapas

Loquipapas habla como un amigo que siempre tiene hambre y siempre invita.

## Personalidad

''' + ''.join(f'- **{a}.** {b}\n' for a, b in RASGOS) + '''
## Reglas de escritura

### Así sí
''' + ''.join(f'- {x}\n' for x in SI) + '''
### Así no
''' + ''.join(f'- {x}\n' for x in NO) + '''
## Estructura de una pieza

| Parte | Qué es | Letra | Largo |
|---|---|---|---|
| Gancho | Lo primero que se lee. Frena el dedo. | Luckiest Guy, mayúsculas | Hasta 6 palabras |
| Líneas | Una idea por línea, al ritmo del video. | Luckiest Guy, mayúsculas | 1 a 3 palabras cada una |
| Remate | La frase con gracia que cierra la idea. | Permanent Marker, minúsculas | Hasta 7 palabras |
| Llamado | Qué debe hacer la persona. | Luckiest Guy o Work Sans 900 | Hasta 6 palabras |

## Banco de frases

### Ganchos
''' + ''.join(f'- {x}\n' for x in GANCHOS) + '''
### Remates
''' + ''.join(f'- {x}\n' for x in REMATES) + '''
### Llamados a la acción
''' + ''.join(f'- {x}\n' for x in LLAMADOS) + f'''
### Etiquetas
`{HASHTAGS}`

## Cómo habla Loqui

Loqui habla en primera persona, en español neutro y sin groserías. Es exagerado, se burla de sí mismo y nunca de la gente.

- "Hola, soy Loqui. Papa de nacimiento. Loco por vocación."
- "Mi pelo es 100 % papa frita. No se toca. Bueno… una."
- "Vengo a traer papas locas."

## Respuestas en redes

| Situación | Tono | Ejemplo |
|---|---|---|
| Comentario positivo | Agradecido y juguetón | "Así nos gusta. La próxima con más queso." |
| Pregunta por precio u horario | Directo, sin chiste | "Estamos en la {DIR}. Horario: [horario]." |
| Queja | Serio, sin humor, con solución | "Lamentamos lo que pasó. Escríbenos por mensaje con tu pedido y lo resolvemos hoy." |
| Etiqueta a un amigo | Cómplice | "Ya quedó notificado. Que invite." |

## Descripción modelo

```
No veas esto con hambre.
Con queso hasta donde aguante.

Etiqueta al que te las debe.
{DIR}

{HASHTAGS}
```
''')
out('PROMPT-MARCA.md', f'''# Contexto de marca para usar con cualquier IA

Copia el bloque que necesites y pégalo antes de tu pedido. Sirve para asistentes de texto, generadores de imagen y generadores de video.

## 1. Contexto general (para pedir textos, ideas o diseños)

```
Trabajas para LOQUIPAPAS, un negocio de comida rápida en Medellín, Colombia ({DIR}).
Vende papas locas, salchipapas, perros, perras y hamburguesas con mucho queso.
Descriptor: "papas locas". Frase de marca: "con queso hasta donde aguante".
Público: jóvenes y estudiantes de 18 a 28 años.
Personalidad: loca, antojadora, cercana, generosa y segura.
Voz: español neutro, de tú, frases cortas, humor exagerado sobre la comida, sin groserías.
Mascota: Loqui, una papa dorada con pelo de siete papas fritas, un ojo grande y uno pequeño,
una ceja levantada y la lengua afuera. No lleva gorra ni ropa. Saluda con la V de dos dedos.
Colores: rojo salsa #E2412B, amarillo papa #FFC21A, crema #FFF3D6, noche #1B1726, queso #FFD84A.
Tipografías: Luckiest Guy (titulares en mayúsculas con sombra dura), Permanent Marker (remate
en minúsculas, inclinado), Work Sans (texto).
Estilo gráfico: contorno oscuro grueso, sombra dura sin difuminar, queso derretido que chorrea
sobre los titulares, fondos de rayos amarillos.
No inventes precios, fechas, horarios ni promociones. Si falta un dato, déjalo entre corchetes.
```

## 2. Estructura de un texto para redes

```
Escribe para LOQUIPAPAS con esta estructura:
- Gancho: hasta 6 palabras, en mayúsculas.
- Líneas: 5 a 7 frases de 1 a 3 palabras.
- Remate: hasta 7 palabras, en minúsculas.
- Llamado a la acción: hasta 6 palabras, en mayúsculas.
Tema: [tema]. Producto: [producto].
```

## 3. Imagen de comida (en inglés suele dar mejor resultado)

```
Close-up street food photography of [DISH], steaming, served in a plain red paper box with one
cream stripe on a red tray with cream paper. Warm side light at about 3200 K, glossy melted
cheese, shallow depth of field, dark softly blurred background with red and yellow accents.
Vertical composition with calm empty space in the top third. Vivid appetizing colors.
No text, no logos, no brand names, no people.
```

Platos, en inglés:

| Producto | Descripción |
|---|---|
| Salchipapa | thick golden french fries loaded with sliced fried sausages, melted yellow cheese and a zig-zag of pink sauce |
| Papas con queso | thick golden french fries drowned in melted yellow cheddar cheese sauce |
| Perro | a Colombian street-style hot dog overloaded with melted cheese, crushed potato chips and zig-zag sauces |
| Hamburguesa | a tall juicy cheeseburger with thick melted cheese dripping down the patty, lettuce and tomato |

## 4. Video con personas

```
FORMAT: vertical 9:16 video, 8 seconds, 24 fps, photorealistic live-action commercial, shallow
depth of field, natural handheld micro-movement.
BRAND WORLD: Loquipapas, a bold and playful Colombian street-food brand from Medellín. The
palette must dominate every frame: salsa red (#E2412B), fries yellow (#FFC21A), warm cream
(#FFF3D6) and deep night purple-black (#1B1726). Food is served in a plain red paper box with
one cream stripe, on red trays with cream paper. Staff wear plain red aprons and plain yellow caps.
LOCATION: a small, spotless second-floor street-food spot in Medellín at dusk, open counter
kitchen, warm practical bulbs, city lights softly out of focus.
CAST: young Colombian adults aged 20 to 28, casual streetwear in neutral colors, genuine expressions.
SHOT: [describe the action].
CAMERA: [describe framing and movement].
LIGHT: warm key light from the side, soft fill, glossy highlights on the cheese, visible steam.
AUDIO: natural sound only, no music, no voice-over.
HARD RULES: no on-screen text, captions, logos, watermarks or brand names. Keep the top third
calm for titles. Natural hands and faces. Food must look real and freshly made.
```

El generador de contenido arma este texto completo para cada campaña, con tres clips: gancho, deseo y remate.

## 5. Ilustración de Loqui

Las IA de imagen no reproducen bien a Loqui. Usa siempre los archivos de `mascota/`. Si necesitas una pose nueva, pídela a un ilustrador con esta descripción:

```
Personaje: papa dorada (#FFC21A), redonda e imperfecta, con contorno oscuro grueso (#1B1726).
Pelo: siete papas fritas rectas en abanico, alternando #FFD54A y #F5B014.
Cara: ojo izquierdo grande y ojo derecho pequeño, ambos blancos con pupila oscura; ceja izquierda
levantada y ceja derecha recta; boca abierta color #7A1C22 con dientes blancos y lengua rosada
(#FF5A7A) afuera hacia la derecha.
Cuerpo: brazos y piernas de línea oscura, manos crema, zapatos rojos. Sin gorra ni ropa.
Estilo: plano, sin degradados, sombra dura abajo a la derecha.
```

## 6. Antes de publicar algo hecho con IA

- La comida se parece a la que se vende.
- No hay letras, logos ni marcas ajenas en la imagen.
- Manos, dientes y caras sin deformaciones.
- No se presenta como clientes reales.
- Se marca como contenido generado con IA en la red.
''')
marca = dict(nombre='LOQUIPAPAS', descriptor='papas locas', frase='con queso hasta donde aguante', direccion=DIR, ciudad='Medellín, Colombia',
 productos=['Papas locas', 'Salchipapas', 'Perros', 'Perras', 'Hamburguesas'], publico='Jóvenes y estudiantes de 18 a 28 años',
 personalidad=[a for a, _ in RASGOS], colores={c['id']: c['hex'] for c in pal['principal']}, colores_ilustracion={c['id']: c['hex'] for c in pal['ilustracion']},
 tipografia=dict(titulares=dict(familia='Luckiest Guy', uso='Mayúsculas con sombra dura', licencia='Apache-2.0'), acento=dict(familia='Permanent Marker', uso='Remate en minúsculas, inclinado 3 a 5 grados', licencia='Apache-2.0'), texto=dict(familia='Work Sans', pesos=[500, 700, 900], licencia='OFL-1.1')),
 estilo=dict(contorno='Línea noche gruesa con esquinas redondeadas', sombra='Dura, 4,5 % del tamaño, abajo a la derecha, sin difuminar', queso='Chorrea desde arriba sobre titulares y bordes', fondos=['rayos', 'confeti de papas', 'cuadros', 'puntos']),
 logo=dict(principal='logo/svg/loquipapas-principal-fondo-crema.svg', linea='logo/svg/loquipapas-linea-fondo-crema.svg', una_tinta='logo/svg/loquipapas-una-tinta-negro.svg', avatar='logo/svg/loquipapas-avatar-rojo.svg', isotipo='logo/svg/loquipapas-isotipo.svg', minimos=dict(principal_mm=30, linea_mm=35, isotipo_mm=10, principal_px=160, linea_px=180, isotipo_px=32), respeto='Altura de la letra L'),
 mascota=dict(nombre='Loqui', descripcion='Papa dorada con pelo de siete papas fritas, ojo grande, ojo pequeño, ceja levantada y lengua afuera', expresiones={k: f'mascota/svg/loqui-{k}.svg' for k in EXPRESIONES}, poses=['saludo', 'presenta', 'antojado'], prohibido=['gorra o ropa', 'un solo dedo levantado', 'cambiar el color', 'papa cruda, papa frita suelta o salchicha', 'versión realista o 3D']),
 voz=dict(idioma='Español neutro, de tú', si=SI, no=NO, ganchos=GANCHOS, remates=REMATES, llamados=LLAMADOS, etiquetas=HASHTAGS.split()),
 movimiento=[dict(nombre=a, descripcion=b, tiempo=c) for a, b, c in MOV],
 redes=dict(reel='1080x1920', post='1080x1350', perfil='512x512', portada_facebook='1640x624', zona_segura_vertical_px=250),
 pendientes=['Registro de marca ante la SIC', 'Usuario de redes', 'Número de WhatsApp', 'Nombres y precios del menú'])
out('marca.json', json.dumps(marca, ensure_ascii=False, indent=1))
out('tipografia/README.md', '''# Tipografías de Loquipapas

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
''')
out('README.md', f'''# Identidad de marca de LOQUIPAPAS

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

Hace falta Python 3 con `fonttools`, Node.js con `playwright`, y `ffmpeg`.

```bash
cd marca/fuente
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
''')
print('manual listo')
