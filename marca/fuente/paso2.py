# Plantillas listas para editar: se generan como HTML y luego se exportan a PDF (vector) y PNG.
from base import *
def f(rel): return open(os.path.join(RAIZ, rel), encoding='utf-8').read()
def img(rel, estilo=''): return f'<img src="../../{rel}" style="{estilo}" alt="">'
DIR = 'Carrera 94 # 65C-01 · 2º piso'; BARRIO = 'Robledo, Medellín'
CSS = '''@font-face{font-family:"Luckiest Guy";src:url(../../tipografia/fuentes/LuckiestGuy-400.woff2) format("woff2")}
@font-face{font-family:"Permanent Marker";src:url(../../tipografia/fuentes/PermanentMarker-400.woff2) format("woff2")}
@font-face{font-family:"Work Sans";font-weight:500;src:url(../../tipografia/fuentes/WorkSans-500.woff2) format("woff2")}
@font-face{font-family:"Work Sans";font-weight:700;src:url(../../tipografia/fuentes/WorkSans-700.woff2) format("woff2")}
@font-face{font-family:"Work Sans";font-weight:900;src:url(../../tipografia/fuentes/WorkSans-900.woff2) format("woff2")}
:root{--crema:#FFF3D6;--rojo:#E2412B;--noche:#1B1726;--papa:#FFC21A;--queso:#FFD84A}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;padding:0}
body{font-family:"Work Sans",sans-serif;font-weight:500;color:var(--noche)}
.hoja{position:relative;overflow:hidden}
.t{font-family:"Luckiest Guy",sans-serif;font-weight:400;line-height:.95;margin:0}
.m{font-family:"Permanent Marker",cursive;line-height:1;margin:0}
.s{text-shadow:.045em .045em 0 var(--noche)}.sr{text-shadow:.045em .045em 0 var(--rojo)}
.abs{position:absolute}.c{text-align:center}
img{display:block}'''
def pagina(nombre, w, h, cuerpo, unidad='mm', extra=''):
    html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Loquipapas · {nombre}</title><style>{CSS}@page{{size:{w}{unidad} {h}{unidad};margin:0}}.hoja{{width:{w}{unidad};height:{h}{unidad}}}{extra}</style></head><body><div class="hoja" data-w="{w}" data-h="{h}" data-u="{unidad}">{cuerpo}</div></body></html>'
    out(f'plantillas/html/{nombre}.html', html)
LINEA_CLARO = 'logo/svg/loquipapas-linea-transparente-claro.svg'; LINEA = 'logo/svg/loquipapas-linea-transparente.svg'
PRINC = 'logo/svg/loquipapas-principal-transparente.svg'; PRINC_CLARO = 'logo/svg/loquipapas-principal-transparente-claro.svg'

# 1 · Menú carta A4
def seccion(icono, titulo, n=3):
    its = ''.join('<div class="it"><div class="fila"><b>[Nombre del producto]</b><i></i><span>$ [precio]</span></div><p>[Ingredientes principales en una línea]</p></div>' for _ in range(n))
    return f'<section><h2 class="t">{img(f"iconos/svg/icono-{icono}.svg", "width:11mm;height:11mm")}{titulo}</h2>{its}</section>'
pagina('menu-carta-A4', 210, 297, f'''
<header class="abs" style="left:0;top:0;width:100%;height:58mm;background:var(--rojo);display:flex;align-items:center;justify-content:center">{img(LINEA_CLARO, "width:150mm")}</header>
{img("patrones/svg/queso-borde-amarillo.svg", "position:absolute;left:-2mm;top:52mm;width:214mm")}
<main class="abs" style="left:14mm;right:14mm;top:84mm;columns:2;column-gap:10mm">
{seccion("papas", "PAPAS LOCAS", 3)}{seccion("salchipapa", "SALCHIPAPAS", 3)}{seccion("perro", "PERROS Y PERRAS", 3)}{seccion("hamburguesa", "HAMBURGUESAS", 3)}{seccion("queso", "ADICIONES", 2)}{seccion("bebida", "BEBIDAS", 2)}
</main>
<footer class="abs" style="left:0;bottom:0;width:100%;height:30mm;background:var(--noche);color:var(--crema);padding:6mm 14mm;font-weight:900;font-size:4.2mm;line-height:1.5">
{DIR}<br><span style="color:var(--papa)">{BARRIO}</span> · WhatsApp [número] · [@usuario]</footer>
{img("mascota/svg/loqui-cuerpo-saludo.svg", "position:absolute;right:6mm;bottom:8mm;width:46mm")}
''', extra='''section{break-inside:avoid;margin-bottom:7mm}h2{font-size:8.6mm;color:var(--rojo);text-shadow:.05em .05em 0 var(--noche);display:flex;align-items:center;gap:2.5mm;margin-bottom:3mm}
.it{margin-bottom:2.6mm}.fila{display:flex;align-items:baseline;gap:1.5mm;font-size:3.9mm}.fila b{font-weight:900}.fila i{flex:1;border-bottom:.5mm dotted var(--noche);transform:translateY(-1mm)}.fila span{font-weight:900;color:var(--rojo);white-space:nowrap}
.it p{margin:.6mm 0 0;font-size:3.1mm;line-height:1.3}''')

# 2 · Póster de calle 50 x 70 cm
pagina('poster-calle-50x70', 500, 700, f'''
<div class="abs" style="inset:0;background:url(../../patrones/svg/rayos-amarillo.svg) center/170% no-repeat"></div>
<div class="abs c" style="left:0;right:0;top:34mm">{img(LINEA, "width:250mm;margin:0 auto")}</div>
<h1 class="t s abs c" style="left:0;right:0;top:112mm;font-size:150mm;color:var(--rojo);transform:rotate(-3deg)">PAPAS<br>LOCAS</h1>
{img("patrones/svg/queso-borde-crema.svg", "position:absolute;left:28mm;top:96mm;width:444mm;transform:rotate(-3deg)")}
<p class="m abs c" style="left:0;right:0;top:392mm;font-size:30mm;transform:rotate(-3deg)">con queso hasta donde aguante</p>
{img("mascota/svg/loqui-cuerpo-saludo.svg", "position:absolute;left:120mm;top:440mm;width:260mm")}
<div class="abs" style="left:0;right:0;bottom:0;height:86mm;background:var(--noche);color:var(--crema);display:flex;align-items:center;justify-content:space-between;padding:0 30mm">
<div><div class="t" style="font-size:40mm;color:var(--papa)">SUBE AL 2º PISO</div><div style="font-weight:900;font-size:15mm;margin-top:3mm">{DIR.split(" · ")[0]} · {BARRIO}</div></div>
{img("iconos/svg/icono-segundo-piso.svg", "width:62mm;filter:invert(1) hue-rotate(180deg)")}</div>''')

# 3 · Aviso de fachada 3 x 1 m (proporción 3:1)
pagina('aviso-fachada-3x1', 600, 200, f'''
<div class="abs" style="inset:0;background:var(--noche)"></div>
<div class="abs" style="left:26mm;top:0;bottom:0;display:flex;align-items:center">{img("logo/svg/loquipapas-linea-transparente-claro.svg", "width:548mm")}</div>''')

# 4 · Volante A5
chips = ''.join(f'<span>{x}</span>' for x in ('Salchipapas', 'Perros', 'Perras', 'Hamburguesas'))
pagina('volante-A5', 148, 210, f'''
<div class="abs" style="inset:0;background:var(--rojo)"></div>
<div class="abs c" style="left:0;right:0;top:9mm">{img(PRINC_CLARO, "width:118mm;margin:0 auto")}</div>
<p class="m abs c" style="left:0;right:0;top:126mm;font-size:8.4mm;color:var(--crema);transform:rotate(-3deg)">con queso hasta donde aguante</p>
<div class="abs chips" style="left:10mm;right:10mm;top:142mm">{chips}</div>
{img("mascota/svg/loqui-antojo.svg", "position:absolute;right:-12mm;bottom:20mm;width:62mm;transform:rotate(-10deg)")}
<div class="abs" style="left:10mm;bottom:10mm;width:92mm;background:var(--noche);color:var(--crema);border-radius:4mm;padding:4mm 5mm;font-weight:900;font-size:4mm;line-height:1.45">{DIR}<br><span style="color:var(--papa)">{BARRIO}</span><br>WhatsApp [número] · [@usuario]</div>''',
 extra='.chips{display:flex;flex-wrap:wrap;gap:2.5mm;justify-content:center}.chips span{background:var(--crema);border:.8mm solid var(--noche);border-radius:99mm;padding:1.6mm 4mm;font-weight:900;font-size:4.4mm}')

# 5 · Tarjeta de fidelidad 9 x 5,5 cm (frente y respaldo)
sellos = ''.join(f'<i>{i + 1}</i>' for i in range(8))
pagina('tarjeta-fidelidad-frente', 90, 55, f'<div class="abs" style="inset:0;background:var(--papa)"></div><div class="abs" style="inset:0;display:flex;align-items:center;justify-content:center">{img(PRINC, "height:50mm")}</div>')
pagina('tarjeta-fidelidad-respaldo', 90, 55, f'''<div class="abs" style="inset:0;background:var(--crema)"></div>
<div class="t abs" style="left:5mm;top:4.5mm;font-size:6.4mm;color:var(--rojo);text-shadow:.05em .05em 0 var(--noche)">TU TARJETA LOCA</div>
<div class="abs sellos" style="left:5mm;top:14mm;width:62mm">{sellos}</div>
<p class="abs" style="left:5mm;bottom:3.5mm;width:60mm;margin:0;font-size:2.7mm;font-weight:700;line-height:1.3">Junta 8 sellos y [beneficio]. Un sello por compra de [condición].</p>
{img("mascota/svg/loqui-guino.svg", "position:absolute;right:-4mm;bottom:-5mm;width:23mm;transform:rotate(-8deg)")}''',
 extra='.sellos{display:grid;grid-template-columns:repeat(4,1fr);gap:2.2mm}.sellos i{aspect-ratio:1;border:.6mm dashed var(--noche);border-radius:50%;display:flex;align-items:center;justify-content:center;font-style:normal;font-weight:900;font-size:3.6mm;color:#B9AD92;background:#fff}')

# 6 · Sticker sello 7 cm
pagina('sticker-sello-7cm', 70, 70, f'''<svg viewBox="0 0 700 700" style="position:absolute;inset:0;width:100%;height:100%"><circle cx="350" cy="350" r="338" fill="#E2412B" stroke="#1B1726" stroke-width="14"/><circle cx="350" cy="350" r="238" fill="#FFF3D6" stroke="#1B1726" stroke-width="10"/>
<defs><path id="a" d="M350 350 m-282 0 a282 282 0 1 1 564 0"/><path id="b" d="M350 350 m-300 0 a300 300 0 0 0 600 0"/></defs>
<text font-family="Luckiest Guy" font-size="74" fill="#FFF3D6" text-anchor="middle" letter-spacing="6"><textPath href="#a" startOffset="50%">LOQUIPAPAS</textPath></text>
<text font-family="Permanent Marker" font-size="50" fill="#FFC21A" text-anchor="middle" letter-spacing="3"><textPath href="#b" startOffset="50%">papas locas · Medellín</textPath></text></svg>
{img("logo/svg/loquipapas-isotipo.svg", "position:absolute;left:17mm;top:12.5mm;width:36mm")}''')
pagina('sticker-loqui-6cm', 60, 66, f'<svg viewBox="-28 -76 296 330" style="position:absolute;inset:0;width:100%;height:100%"><g stroke="#FFFFFF" stroke-width="34" stroke-linejoin="round" fill="#FFFFFF">{plano(cabeza(), "#FFFFFF")}</g>{cabeza()}</svg>')

# 7 · Empaques (referencia visual, no es troquel)
pagina('empaques-referencia', 297, 210, f'''<div class="abs" style="inset:0;background:var(--crema)"></div>
<div class="t abs" style="left:14mm;top:10mm;font-size:9mm;color:var(--rojo);text-shadow:.05em .05em 0 var(--noche)">EMPAQUES</div><p class="abs" style="left:14mm;top:20mm;margin:0;font-size:3.4mm;font-weight:700">Referencia visual de aplicación. No es un plano de troquel: la imprenta ajusta medidas.</p>
<svg viewBox="0 0 2970 2100" style="position:absolute;inset:0;width:100%;height:100%"><g stroke="#1B1726" stroke-width="12" stroke-linejoin="round">
<path d="M220 700 L1000 700 L900 1800 L320 1800 Z" fill="#E2412B"/><path d="M236 880 L984 880 L970 1030 L250 1030 Z" fill="#FFF3D6" stroke="none"/>
<path d="M1200 620 H1900 L1960 1800 H1140 Z" fill="#FFF3D6"/><path d="M1400 620 C1400 420 1700 420 1700 620" fill="none"/>
<path d="M2180 900 L2760 900 L2690 1800 L2250 1800 Z" fill="#E2412B"/><rect x="2140" y="800" width="660" height="110" rx="40" fill="#FFF3D6"/><path d="M2500 800 L2580 560" fill="none"/><path d="M2204 1180 L2736 1180 L2718 1420 L2222 1420 Z" fill="#FFC21A" stroke="none"/></g></svg>
{img(LINEA_CLARO, "position:absolute;left:35mm;top:118mm;width:54mm")}{img("logo/svg/loquipapas-isotipo.svg", "position:absolute;left:46mm;top:136mm;width:30mm")}
{img(PRINC, "position:absolute;left:122mm;top:82mm;width:66mm")}{img("logo/svg/loquipapas-isotipo.svg", "position:absolute;left:232mm;top:117mm;width:28mm")}
<p class="abs c" style="left:22mm;top:186mm;width:78mm;margin:0;font-weight:900;font-size:3.6mm">Caja de papas: roja con franja crema</p><p class="abs c" style="left:114mm;top:186mm;width:82mm;margin:0;font-weight:900;font-size:3.6mm">Bolsa para llevar: crema con logo</p><p class="abs c" style="left:214mm;top:186mm;width:66mm;margin:0;font-weight:900;font-size:3.6mm">Vaso: rojo con franja amarilla</p>''')

# 8 · Uniforme
pagina('uniforme-referencia', 297, 210, f'''<div class="abs" style="inset:0;background:var(--crema)"></div>
<div class="t abs" style="left:14mm;top:10mm;font-size:9mm;color:var(--rojo);text-shadow:.05em .05em 0 var(--noche)">UNIFORME</div>
<svg viewBox="0 0 2970 2100" style="position:absolute;inset:0;width:100%;height:100%"><g stroke="#1B1726" stroke-width="12" stroke-linejoin="round">
<path d="M560 520 C640 600 860 600 940 520 L1010 820 C1090 840 1160 900 1180 1000 L1180 1820 H320 L320 1000 C340 900 410 840 490 820 Z" fill="#E2412B"/><path d="M560 520 C560 380 940 380 940 520" fill="none"/><rect x="560" y="1300" width="380" height="260" rx="30" fill="#C7361F"/>
<path d="M1700 1180 C1700 820 2420 820 2420 1180 Z" fill="#FFC21A"/><path d="M1660 1180 H2460 C2680 1180 2760 1290 2700 1330 C2520 1260 2200 1250 1660 1260 Z" fill="#E2412B"/>
<path d="M1560 1500 H2560 V1900 H1560 Z" fill="#1B1726"/></g></svg>
{img(LINEA_CLARO, "position:absolute;left:46mm;top:92mm;width:58mm")}{img("logo/svg/loquipapas-isotipo.svg", "position:absolute;left:193mm;top:86mm;width:26mm")}{img(LINEA_CLARO, "position:absolute;left:168mm;top:160mm;width:76mm")}
<p class="abs c" style="left:30mm;top:188mm;width:90mm;margin:0;font-weight:900;font-size:3.6mm">Delantal rojo con logo en una línea</p><p class="abs c" style="left:160mm;top:138mm;width:92mm;margin:0;font-weight:900;font-size:3.6mm">Gorra amarilla con visera roja y Loqui</p><p class="abs c" style="left:156mm;top:193mm;width:100mm;margin:0;font-weight:900;font-size:3.6mm">Camiseta noche con logo claro</p>''')

# 9 · Señalética
def senal(txt, bg, col, sh, icono=None, extra=''):
    return f'<div style="background:{bg};border:1.4mm solid var(--noche);border-radius:6mm;display:flex;align-items:center;justify-content:center;gap:5mm;padding:4mm">' + (img(f'iconos/svg/icono-{icono}.svg', 'width:22mm') if icono else '') + f'<span class="t" style="font-size:17mm;color:{col};text-shadow:.05em .05em 0 {sh};{extra}">{txt}</span></div>'
pagina('senaletica', 297, 210, f'''<div class="abs" style="inset:0;background:var(--crema)"></div><div class="abs" style="inset:12mm;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,1fr);gap:6mm">
{senal("ABIERTO", "var(--papa)", "var(--rojo)", "var(--noche)")}{senal("CERRADO", "var(--noche)", "var(--crema)", "var(--rojo)")}
{senal("PIDE AQUÍ", "var(--rojo)", "var(--crema)", "var(--noche)", "mensaje")}{senal("RECOGE AQUÍ", "var(--crema)", "var(--rojo)", "var(--noche)", "para-llevar")}
{senal("SUBE AL 2º PISO", "var(--papa)", "var(--rojo)", "var(--noche)", "segundo-piso", "font-size:13mm")}{senal("SALSAS", "var(--crema)", "var(--rojo)", "var(--noche)", "salsa")}
{senal("BAÑOS", "var(--noche)", "var(--papa)", "var(--rojo)")}{senal("GRACIAS, VUELVE", "var(--rojo)", "var(--crema)", "var(--noche)", "corazon", "font-size:12mm")}</div>''')

# 10 · Redes sociales (en pixeles)
pagina('redes-post-1080x1350', 1080, 1350, f'''<div class="abs" style="inset:0;background:var(--papa)"></div><div class="abs" style="left:70px;top:70px">{img(LINEA, "width:420px")}</div>
<h1 class="t s abs c" style="left:60px;right:60px;top:250px;font-size:190px;color:var(--rojo)">[TITULAR<br>CORTO]</h1>{img("patrones/svg/queso-borde-crema.svg", "position:absolute;left:50px;top:192px;width:980px")}
<p class="m abs c" style="left:0;right:0;top:680px;font-size:58px;transform:rotate(-3deg)">[frase de remate]</p>
{img("mascota/svg/loqui-loco.svg", "position:absolute;left:330px;top:760px;width:420px")}
<div class="abs c" style="left:70px;right:70px;bottom:60px;background:var(--noche);color:var(--crema);border:6px solid var(--noche);border-radius:34px;padding:30px;font-weight:900;font-size:48px">[LLAMADO A LA ACCIÓN]</div>''', 'px')
pagina('redes-historia-1080x1920', 1080, 1920, f'''<div class="abs" style="inset:0;background:url(../../patrones/svg/rayos-rojo.svg) center/260% no-repeat"></div><div class="abs" style="left:70px;top:250px">{img(LINEA_CLARO, "width:460px")}</div>
<h1 class="t s abs c" style="left:60px;right:60px;top:460px;font-size:210px;color:var(--crema)">[TITULAR<br>CORTO]</h1>
<p class="m abs c" style="left:0;right:0;top:930px;font-size:64px;color:var(--papa);transform:rotate(-3deg)">[frase de remate]</p>
{img("mascota/svg/loqui-cuerpo-presenta.svg", "position:absolute;left:190px;top:1020px;width:700px")}
<div class="abs c" style="left:70px;right:70px;bottom:270px;background:var(--papa);border:6px solid var(--noche);border-radius:34px;padding:30px;font-weight:900;font-size:50px">[LLAMADO A LA ACCIÓN]</div>
<p class="abs c" style="left:0;right:0;bottom:60px;margin:0;font-size:26px;font-weight:700;color:var(--crema);opacity:.8">Deja libres los 250 px de arriba y de abajo: ahí van los botones de la red.</p>''', 'px')
pagina('redes-portada-1640x624', 1640, 624, f'''<div class="abs" style="inset:0;background:url(../../patrones/svg/rayos-amarillo.svg) center/130% no-repeat"></div>
<div class="abs" style="left:90px;top:0;bottom:0;display:flex;align-items:center">{img(LINEA, "width:900px")}</div>{img("mascota/svg/loqui-cuerpo-saludo.svg", "position:absolute;right:120px;top:70px;width:520px")}''', 'px')
dest = ''.join(f'<div><div class="circ" style="background:{bg}">{img(f"iconos/svg/icono-{ic}.svg", "width:150px")}</div><b>{t}</b></div>' for ic, t, bg in (('papas', 'Menú', 'var(--papa)'), ('combo', 'Combos', 'var(--crema)'), ('ubicacion', 'Dónde', 'var(--papa)'), ('estrella', 'Clientes', 'var(--crema)'), ('horario', 'Horario', 'var(--papa)'), ('mensaje', 'Pedidos', 'var(--crema)')))
pagina('redes-destacadas', 1800, 420, f'<div class="abs" style="inset:0;background:var(--noche)"></div><div class="abs dest" style="inset:40px">{dest}</div>', 'px',
 extra='.dest{display:grid;grid-template-columns:repeat(6,1fr);gap:20px;color:var(--crema);text-align:center;font-size:30px}.circ{width:250px;height:250px;border-radius:50%;border:8px solid var(--rojo);margin:0 auto 14px;display:flex;align-items:center;justify-content:center}')
print('plantillas listas')
