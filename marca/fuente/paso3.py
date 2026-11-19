# Animaciones hechas con código (SVG + CSS). Cada archivo es autónomo y se puede abrir en el navegador.
from base import *
FUENTES = '''@font-face{font-family:"Luckiest Guy";src:url(../../tipografia/fuentes/LuckiestGuy-400.woff2) format("woff2")}
@font-face{font-family:"Permanent Marker";src:url(../../tipografia/fuentes/PermanentMarker-400.woff2) format("woff2")}
@font-face{font-family:"Work Sans";font-weight:900;src:url(../../tipografia/fuentes/WorkSans-900.woff2) format("woff2")}'''
def anim(nombre, w, h, dur, cuerpo, css, fondo=C['crema'], nota=''):
    out(f'animaciones/html/{nombre}.html', f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Loquipapas · {nombre}</title>
<!-- {nota} Duración del ciclo: {dur} s. Tamaño de referencia: {w} x {h}. -->
<style>{FUENTES}
html,body{{margin:0;height:100%;background:{fondo};overflow:hidden}}
#escena{{width:100vw;height:100vh;display:block}}
.pelo,.ojo,.lengua,.ceja,.flota,.l,.cara,.queso,.desc,.b,.c0,.c1,.c2,.c3,.c4,.c5,.r1,.r2,.r3,.e{{transform-box:fill-box}}
{css}
@media (prefers-reduced-motion:reduce){{*{{animation:none !important}}}}</style></head>
<body data-w="{w}" data-h="{h}" data-dur="{dur}"><svg id="escena" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">{cuerpo}</svg></body></html>''')

# Cabeza con partes separadas para animar
def cabeza_viva(expr='loco'):
    d = [(53, 4, 46, -50, 60, 40, 0), (73, -26, 62, -28, 80, 26, 1), (93, -28, 58, -12, 100, 20, 0), (113, -44, 72, 4, 120, 18, 1), (133, -30, 60, 18, 140, 20, 0), (153, -28, 64, 34, 160, 26, 1), (173, 6, 44, 52, 180, 40, 0)]
    p = ''.join(f'<g transform="rotate({r} {cx} {cy})"><rect class="pelo" style="--i:{i}" x="{x}" y="{y}" width="14" height="{h}" rx="3" fill="{ILU["papa_tostada"] if k else ILU["papa_clara"]}" stroke="{N}" stroke-width="6"/></g>' for i, (x, y, h, r, cx, cy, k) in enumerate(d))
    cejas = '<g class="ceja">' + linea('M54 72 C66 54 98 52 114 64') + '</g>' + linea('M142 96 L178 102')
    ojos = f'<g class="ojo">{ojo(86, 110, 29, 7, -7, 11)}</g><g class="ojo">{ojo(160, 122, 14, -3, 2, 6)}</g>'
    boca = (f'<path d="M66 146 C84 200 162 200 180 140 C146 156 102 158 66 146 Z" fill="{ILU["boca"]}" stroke="{N}" stroke-width="8" stroke-linejoin="round"/>'
            f'<g class="lengua"><path d="M116 160 L174 150 C181 186 175 214 151 216 C127 218 114 192 116 160 Z" fill="{ILU["lengua"]}" stroke="{N}" stroke-width="7" stroke-linejoin="round"/><path d="M146 178 C148 190 148 200 147 206" fill="none" stroke="{ILU["lengua_linea"]}" stroke-width="4" stroke-linecap="round"/></g>'
            '<path d="M72 150 C104 162 148 160 176 145 C175 151 173 156 170 160 C146 170 104 172 78 162 C76 158 74 154 72 150 Z" fill="#FFFFFF"/>' + linea('M66 146 C102 158 146 156 180 140', 8))
    return p + cuerpo() + cejas + ojos + boca
VIVO = '''.pelo{transform-origin:50% 100%;animation:pelo 1s ease-in-out infinite alternate;animation-delay:calc(var(--i) * -.14s)}
@keyframes pelo{from{transform:rotate(-7deg)}to{transform:rotate(7deg)}}
.ojo{transform-origin:center;animation:parpadeo 4s infinite}
@keyframes parpadeo{0%,44%,50%,90%,96%,100%{transform:scaleY(1)}47%,93%{transform:scaleY(.08)}}
.lengua{transform-origin:40% 0;animation:lengua .5s ease-in-out infinite alternate}
@keyframes lengua{from{transform:rotate(-6deg)}to{transform:rotate(7deg) scaleY(1.06)}}
.ceja{animation:ceja 2s ease-in-out infinite alternate}
@keyframes ceja{from{transform:translateY(0)}to{transform:translateY(-7px)}}
.flota{transform-origin:center;animation:flota 2s ease-in-out infinite alternate}
@keyframes flota{from{transform:translateY(8px) rotate(-3deg)}to{transform:translateY(-8px) rotate(3deg)}}'''
def rayos(cx, cy, r, color): return '<g class="rayos">' + ''.join(f'<path d="M{cx} {cy} L{cx + r * math.cos(math.radians(i * 22.5)):.0f} {cy + r * math.sin(math.radians(i * 22.5)):.0f} L{cx + r * math.cos(math.radians(i * 22.5 + 11.25)):.0f} {cy + r * math.sin(math.radians(i * 22.5 + 11.25)):.0f} Z" fill="{color}"/>' for i in range(16)) + '</g>'
RAYOS = '.rayos{transform-box:view-box;animation:giro 32s linear infinite}@keyframes giro{to{transform:rotate(360deg)}}'

# 1 · Entrada del logo
def logo_animable(S=200, var='crema'):
    v = VAR[var]; d = S * .045; pad = S * .42; w1, w2 = ancho_fila(F1, S), ancho_fila(F2, S); W = max(w1, w2) + pad * 2; b1 = pad + S * .62 + LG.cap * S; b2 = b1 + S * .94; g = []; i = 0
    for items, base, x in ((F1, b1, (W - w1) / 2), (F2, b2, (W - w2) / 2)):
        for ch, dy, rot in items:
            if ch == '@':
                k = S / 240; hy = base - LG.cap * S / 2 - 229 / 200 * S / 2 + dy; t = f'translate({x + S * .02:.1f} {hy:.1f}) rotate({rot} {S / 2:.1f} {S * .57:.1f}) scale({k:.4f}) translate(0 50)'
                g.append(f'<g class="cara"><g transform="translate({d:.1f} {d:.1f}) {t}">{plano(cabeza(), v["sombra"])}</g><g transform="{t}">{cabeza_viva()}</g></g>'); x += S * 1.04
            else:
                a = LG.adv(ch, S); cx, cy = x + a / 2, base - LG.cap * S / 2 + dy; p = LG.glifo(ch, S, x, base + dy)
                g.append(f'<g class="l" style="--i:{i}"><path d="{p}" fill="{v["sombra"]}" transform="translate({d:.1f} {d:.1f}) rotate({rot} {cx:.1f} {cy:.1f})"/><path d="{p}" fill="{v["letras"]}" transform="rotate({rot} {cx:.1f} {cy:.1f})"/></g>'); x += a
            i += 1
    x2 = (W - w2) / 2; q = '<g class="queso">' + queso(x2 - S * .1, b2 - LG.cap * S - S * .17, w2 + S * .2, S * .6, v['queso']) + '</g>'
    ty = b2 + S * .66; ds = S * .42
    desc = f'<g class="desc"><path d="{PM.texto("papas locas", ds, W / 2, ty, "middle")}" fill="{v["desc"]}" transform="rotate(-5 {W / 2:.1f} {ty - ds * .3:.1f})"/></g>'
    return ''.join(g) + q + desc, W, ty + pad * .75
lg, LW, LH = logo_animable()
ENTRADA = '''.l{transform-origin:center;animation:caer .55s cubic-bezier(.3,1.6,.5,1) both;animation-delay:calc(.25s + var(--i) * .09s)}
@keyframes caer{from{transform:translateY(-900px) rotate(-25deg);opacity:0}30%{opacity:1}}
.cara{transform-origin:center;animation:brotar .6s cubic-bezier(.3,1.7,.5,1) .34s both}
@keyframes brotar{from{transform:scale(0) rotate(-200deg)}}
.queso{transform-origin:50% 0;animation:chorrear 1s cubic-bezier(.2,.9,.3,1) 1.25s both}
@keyframes chorrear{from{transform:scaleY(0);opacity:0}15%{opacity:1}}
.desc{animation:escribir .7s ease-out 1.9s both}
@keyframes escribir{from{clip-path:inset(-20% 100% -20% 0)}to{clip-path:inset(-20% -5% -20% 0)}}'''
k = 900 / LW
anim('logo-entrada', 1080, 1080, 4, f'<rect width="1080" height="1080" fill="{C["crema"]}"/><g transform="translate(90 {(1080 - LH * k) / 2:.0f}) scale({k:.4f})">{lg}</g>', ENTRADA + VIVO.split('.flota')[0], nota='Entrada del logo: las letras caen, Loqui brota, el queso chorrea y se escribe el descriptor.')

# 2 · Loqui vivo (bucle)
anim('loqui-vivo', 1080, 1080, 4, f'<rect width="1080" height="1080" fill="{C["papa"]}"/>{rayos(540, 540, 1100, "#FFD04A")}<g transform="translate(540 540)"><g class="flota"><g transform="translate(-420 -420) scale(3.5)"><g transform="translate(9 9)">{plano(cabeza(), N)}</g>{cabeza_viva()}</g></g></g>', VIVO + RAYOS, C['papa'], 'Loqui en reposo: parpadea, mueve la lengua y el pelo. Bucle perfecto de 4 segundos.')

# 3 · Cargando
barras = ''.join(f'<g transform="rotate({r} {x + 22} 330)"><rect class="b" style="--i:{i}" x="{x}" y="{y}" width="44" height="{340 - y}" rx="9" fill="{ILU["papa_tostada"] if i % 2 else ILU["papa_clara"]}" stroke="{N}" stroke-width="12"/></g>' for i, (x, y, r) in enumerate([(176, 150, -12), (228, 110, -6), (278, 130, 0), (328, 100, 6), (380, 150, 12)]))
anim('cargando', 600, 600, 2, f'<rect width="600" height="600" fill="{C["crema"]}"/>{barras}<path d="M150 320 L450 320 L420 520 L180 520 Z" fill="{C["rojo"]}" stroke="{N}" stroke-width="14" stroke-linejoin="round"/><path d="M158 360 L442 360 L436 400 L164 400 Z" fill="{C["crema"]}"/><text x="300" y="580" text-anchor="middle" font-family="Luckiest Guy" font-size="44" fill="{N}">CARGANDO</text>',
     '.b{transform-origin:50% 100%;animation:saltar .5s ease-in-out infinite alternate;animation-delay:calc(var(--i) * -.2s)}@keyframes saltar{from{transform:translateY(40px)}to{transform:translateY(-34px)}}', nota='Indicador de carga para web o pantallas.')

# 4 · Transición de queso
gotas = ''.join(f'<rect x="{x}" y="1900" width="120" height="{h}" rx="60" fill="{C["queso"]}" stroke="{N}" stroke-width="14"/>' for x, h in [(40, 380), (220, 620), (410, 300), (600, 700), (790, 420), (950, 560)])
anim('transicion-queso', 1080, 1920, 2, f'<rect width="1080" height="1920" fill="{N}"/><text x="540" y="1000" text-anchor="middle" font-family="Luckiest Guy" font-size="200" fill="{C["crema"]}">ANTES</text><g class="b"><rect width="1080" height="1920" fill="{C["papa"]}"/><text x="540" y="1000" text-anchor="middle" font-family="Luckiest Guy" font-size="200" fill="{C["rojo"]}">DESPUÉS</text></g><g class="q">{gotas}<rect x="-20" y="-700" width="1120" height="2660" fill="{C["queso"]}" stroke="{N}" stroke-width="14"/>{gotas.replace(f"stroke=\"{N}\" stroke-width=\"14\"", "")}<rect x="120" y="-500" width="26" height="2200" rx="13" fill="#FFF6C8"/></g>',
     '.q{transform-box:view-box;animation:bajar 2s cubic-bezier(.5,0,.5,1) infinite}@keyframes bajar{0%{transform:translateY(-2800px)}100%{transform:translateY(2700px)}}.b{animation:cambio 2s steps(1) infinite}@keyframes cambio{0%{opacity:0}50%{opacity:1}}', N, 'Transición entre dos tomas: el queso baja, tapa la pantalla y deja ver la toma siguiente.')

# 5 · Rótulo inferior
anim('rotulo-inferior', 1080, 1920, 4, f'<rect width="1080" height="1920" fill="#00B140"/><g class="r1"><rect x="60" y="1500" width="800" height="150" rx="40" fill="{C["rojo"]}" stroke="{N}" stroke-width="12"/><text x="250" y="1604" font-family="Luckiest Guy" font-size="84" fill="{C["crema"]}">[NOMBRE]</text></g><g class="r2"><rect x="200" y="1640" width="560" height="90" rx="30" fill="{N}"/><text x="240" y="1702" font-family="Work Sans" font-weight="900" font-size="46" fill="{C["papa"]}">[cargo o dato]</text></g><g class="r3" transform="translate(30 1440) scale(.95)"><g transform="translate(8 8)">{plano(cabeza(), N)}</g>{cabeza_viva()}</g>',
     '.r1{animation:r1 4s cubic-bezier(.2,1.2,.4,1) infinite}@keyframes r1{0%{transform:translateX(-1100px)}12%,84%{transform:translateX(0)}96%,100%{transform:translateX(-1100px)}}.r2{animation:r2 4s cubic-bezier(.2,1.2,.4,1) infinite}@keyframes r2{0%,6%{transform:translateX(-1100px)}18%,80%{transform:translateX(0)}92%,100%{transform:translateX(-1100px)}}.r3{transform-origin:center;animation:r3 4s cubic-bezier(.3,1.7,.5,1) infinite}@keyframes r3{0%,10%{scale:0}22%,82%{scale:1}90%,100%{scale:0}}' + VIVO.split('.flota')[0], '#00B140', 'Rótulo para presentar personas en video. Fondo verde para recortarlo en el editor.')

# 6 · Cierre de video
cx = 540
anim('cierre-video', 1080, 1920, 4, f'<rect width="1080" height="1920" fill="{C["papa"]}"/>{rayos(540, 1150, 1700, "#FFD04A")}'
     f'<g class="c0"><path d="{LG.texto("LOQUIPAPAS", 96, cx, 250, "middle")}" fill="{N}" transform="translate(5 5)"/><path d="{LG.texto("LOQUIPAPAS", 96, cx, 250, "middle")}" fill="{C["rojo"]}"/></g>'
     f'<g class="c1"><path d="{LG.texto("PAPAS", 300, cx, 590, "middle")}" fill="{N}" transform="translate(13 13)"/><path d="{LG.texto("PAPAS", 300, cx, 590, "middle")}" fill="{C["rojo"]}"/></g>'
     f'<g class="c2"><path d="{LG.texto("LOCAS", 300, cx, 880, "middle")}" fill="{N}" transform="translate(13 13)"/><path d="{LG.texto("LOCAS", 300, cx, 880, "middle")}" fill="{C["rojo"]}"/></g>'
     f'<g class="queso">{queso(70, 340, 940, 170, C["crema"])}</g>'
     f'<g class="c3"><path d="{PM.texto("con queso hasta donde aguante", 58, cx, 1010, "middle")}" fill="{N}" transform="rotate(-3 540 1000)"/></g>'
     f'<g class="c4"><g transform="translate(190 1100) scale(2.9)"><g transform="translate(8 8)">{plano(cabeza(), N)}</g>{cabeza_viva()}</g></g>'
     f'<g class="c5"><rect x="90" y="1660" width="900" height="180" rx="40" fill="{N}"/><path d="{WS9.texto("Carrera 94 # 65C-01 · 2º piso", 48, cx, 1738, "middle")}" fill="{C["crema"]}"/><path d="{WS9.texto("Robledo, Medellín", 48, cx, 1800, "middle")}" fill="{C["papa"]}"/></g>',
     '''.c0,.c1,.c2{transform-origin:center;animation:golpe .32s cubic-bezier(.2,1.4,.4,1) both}.c0{animation-delay:.1s}.c1{animation-delay:.25s}.c2{animation-delay:.5s}
@keyframes golpe{from{transform:scale(2.6);opacity:0}}
.queso{transform-origin:50% 0;animation:chorrear 1s cubic-bezier(.2,.9,.3,1) .55s both}@keyframes chorrear{from{transform:scaleY(0);opacity:0}15%{opacity:1}}
.c3{animation:aparece .3s ease-out 1.1s both}@keyframes aparece{from{opacity:0;transform:translateY(20px)}}
.c4{animation:sube .55s cubic-bezier(.3,1.5,.5,1) .8s both}@keyframes sube{from{transform:translateY(1100px)}}
.c5{animation:aparece .35s ease-out 1.5s both}''' + RAYOS + VIVO.split('.flota')[0], C['papa'], 'Cierre de marca para cualquier video vertical.')

# 7 · Sticker animado con las expresiones
caras = ''.join(f'<g class="e" style="--i:{i}"><g transform="translate(8 8)">{plano(cabeza(k), N)}</g>{cabeza(k)}</g>' for i, k in enumerate(EXPRESIONES))
anim('loqui-expresiones', 512, 512, 4, f'<rect width="512" height="512" fill="{C["crema"]}"/><circle cx="256" cy="268" r="226" fill="{C["rojo"]}" stroke="{N}" stroke-width="12"/><g transform="translate(96 132) scale(1.34)"><g class="flota">{caras}</g></g>',
     '.e{opacity:0;animation:turno 4s steps(1) infinite;animation-delay:calc(var(--i) * .5s)}@keyframes turno{0%{opacity:1}12.5%{opacity:0}}' + '.flota' + VIVO.split('.flota')[1], nota='Sticker animado: las ocho expresiones de Loqui.')
print('animaciones listas')
