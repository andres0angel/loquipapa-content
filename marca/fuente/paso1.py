from base import *
import struct, colorsys, shutil
# ---------- Logos ----------
for v in VAR:
    out(f'logo/svg/loquipapas-principal-fondo-{v}.svg', logo_apilado(v))
    out(f'logo/svg/loquipapas-linea-fondo-{v}.svg', logo_linea(v))
out('logo/svg/loquipapas-principal-transparente.svg', logo_apilado('crema', False))
out('logo/svg/loquipapas-principal-transparente-claro.svg', logo_apilado('noche', False))
out('logo/svg/loquipapas-linea-transparente.svg', logo_linea('crema', False))
out('logo/svg/loquipapas-linea-transparente-claro.svg', logo_linea('noche', False))
out('logo/svg/loquipapas-una-tinta-negro.svg', logo_apilado(mono=(N, '#FFFFFF')))
out('logo/svg/loquipapas-una-tinta-blanco.svg', logo_apilado(mono=('#FFFFFF', N)))
out('logo/svg/loquipapas-linea-una-tinta-negro.svg', logo_linea(mono=(N, '#FFFFFF')))
out('logo/svg/loquipapas-linea-una-tinta-blanco.svg', logo_linea(mono=('#FFFFFF', N)))
for v in ('rojo', 'crema', 'amarillo', 'noche'): out(f'logo/svg/loquipapas-avatar-{v}.svg', avatar(v))
out('logo/svg/loquipapas-isotipo.svg', isotipo())
out('logo/svg/loquipapas-isotipo-una-tinta-negro.svg', isotipo(mono=(N, '#FFFFFF')))
out('logo/svg/loquipapas-isotipo-una-tinta-blanco.svg', isotipo(mono=('#FFFFFF', N)))
out('logo/svg/favicon.svg', svg(64, 64, f'<rect width="512" height="512" rx="96" fill="{C["rojo"]}"/><g transform="translate(86 120) scale(1.42)">{cabeza()}</g>', '0 0 512 512', 'Loquipapas'))
# ---------- Mascota ----------
for k in EXPRESIONES: out(f'mascota/svg/loqui-{k}.svg', isotipo(k))
PIERNAS = linea('M98 198 L92 256') + linea('M146 200 L152 256') + f'<ellipse cx="82" cy="264" rx="26" ry="13" fill="{C["rojo"]}" stroke="{N}" stroke-width="7"/><ellipse cx="162" cy="264" rx="26" ry="13" fill="{C["rojo"]}" stroke="{N}" stroke-width="7"/>'
def mano(x, y): return f'<circle cx="{x}" cy="{y}" r="16" fill="{C["crema"]}" stroke="{N}" stroke-width="7"/>'
def dedo(d): return f'<path d="{d}" fill="none" stroke="{N}" stroke-width="20" stroke-linecap="round"/><path d="{d}" fill="none" stroke="{C["crema"]}" stroke-width="10" stroke-linecap="round"/>'
CAJITA = (''.join(f'<rect x="{x}" y="{y}" width="10" height="{194 - y}" rx="2" fill="{ILU["papa_tostada"] if i % 2 else ILU["papa_clara"]}" stroke="{N}" stroke-width="5" transform="rotate({r} {x + 5} 190)"/>' for i, (x, y, r) in enumerate([(-60, 150, -14), (-48, 140, -6), (-36, 146, 2), (-24, 138, 8), (-12, 150, 16)]))
          + f'<path d="M-68 188 L8 188 L-2 252 L-58 252 Z" fill="{C["rojo"]}" stroke="{N}" stroke-width="7" stroke-linejoin="round"/><path d="M-64 200 L4 200 L2 212 L-62 212 Z" fill="{C["crema"]}"/>')
POSES = {
 'saludo': ('Saludo con cajita', 'loco', linea('M30 138 C6 150 -10 166 -18 188') + linea('M212 128 C244 118 258 92 256 64') + PIERNAS, CAJITA + mano(-22, 196) + dedo('M250 46 L240 14') + dedo('M262 46 L274 16') + mano(256, 56)),
 'presenta': ('Presentando', 'feliz', linea('M30 132 C-2 122 -22 98 -30 72') + linea('M212 130 C244 120 264 98 272 72') + PIERNAS, mano(-32, 62) + mano(274, 62)),
 'antojado': ('Con la cajita en alto', 'antojo', linea('M30 138 C4 128 -14 110 -20 86') + linea('M212 136 C238 150 252 168 258 188') + PIERNAS, f'<g transform="translate(-2 -112)">{CAJITA}</g>' + mano(-22, 84) + mano(260, 196)),
}
for k, (nom, ex, atras, frente) in POSES.items():
    out(f'mascota/svg/loqui-cuerpo-{k}.svg', svg(480, 420, atras + cabeza(ex) + frente, '-90 -60 400 350', f'Loqui de cuerpo entero: {nom}'))
# ---------- Iconos ----------
def ic(c): return svg(240, 240, f'<g stroke="{N}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">{c}</g>', '0 0 120 120')
def rr(x, y, w, h, r, f): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{f}"/>'
PAPITAS = ''.join(f'<rect x="{x}" y="{y}" width="9" height="{64 - y}" rx="2" fill="{ILU["papa_tostada"] if i % 2 else ILU["papa_clara"]}" transform="rotate({r} {x + 4} 60)"/>' for i, (x, y, r) in enumerate([(34, 30, -14), (44, 20, -7), (55, 26, 0), (66, 18, 6), (77, 30, 14)]))
CAJA = f'<path d="M28 58 L92 58 L84 108 L36 108 Z" fill="{C["rojo"]}"/><path d="M31 68 L89 68 L87 78 L33 78 Z" fill="{C["crema"]}" stroke="none"/>'
ESTR = 'M60 10 L74 44 L110 46 L82 70 L92 106 L60 86 L28 106 L38 70 L10 46 L46 44 Z'
ICONOS = {
 'papas': PAPITAS + CAJA,
 'salchipapa': PAPITAS + f'<path d="M30 52 H90 V64 C90 72 80 72 80 64 V62 H68 V76 C68 86 54 86 54 76 V62 H44 V68 C44 76 34 76 34 68 V62 H30 Z" fill="{C["queso"]}"/>' + f'<path d="M28 70 L92 70 L84 108 L36 108 Z" fill="{C["rojo"]}"/><circle cx="48" cy="46" r="7" fill="{ILU["salchicha"]}"/><circle cx="72" cy="44" r="7" fill="{ILU["salchicha"]}"/>',
 'perro': rr(14, 50, 92, 28, 14, '#D98F2E') + rr(8, 42, 104, 22, 11, ILU['salchicha']) + rr(14, 62, 92, 30, 15, ILU['pan']) + f'<path d="M20 50 L30 40 L40 50 L50 40 L60 50 L70 40 L80 50 L90 40 L100 50" fill="none" stroke="{N}" stroke-width="11"/><path d="M20 50 L30 40 L40 50 L50 40 L60 50 L70 40 L80 50 L90 40 L100 50" fill="none" stroke="{C["queso"]}" stroke-width="5"/>',
 'hamburguesa': rr(18, 84, 84, 20, 10, ILU['pan_tostado']) + rr(14, 68, 92, 18, 9, ILU['carne']) + f'<path d="M16 58 H104 V68 C104 76 94 76 94 68 H78 V78 C78 88 64 88 64 78 V68 H16 Z" fill="{C["queso"]}"/><path d="M12 56 H108 C104 66 98 60 92 66 C86 60 80 66 74 60 C68 66 62 60 56 66 C50 60 44 66 38 60 C32 66 26 60 20 66 C16 62 12 62 12 56 Z" fill="{ILU["lechuga"]}"/><path d="M18 54 C18 18 102 18 102 54 Z" fill="{ILU["pan"]}"/><path d="M44 34 h6 M62 28 h6 M76 38 h6" stroke-width="4" stroke="{C["crema"]}"/>',
 'bebida': f'<path d="M66 30 L76 8" fill="none"/><path d="M38 42 L82 42 L76 108 L44 108 Z" fill="{C["rojo"]}"/>' + rr(32, 30, 56, 12, 5, C['crema']) + f'<path d="M41 60 L79 60 L77 76 L43 76 Z" fill="{C["papa"]}" stroke="none"/>',
 'salsa': rr(40, 50, 40, 58, 12, C['rojo']) + f'<path d="M50 50 L55 28 L65 28 L70 50 Z" fill="{C["crema"]}"/>' + rr(56, 12, 8, 16, 3, C['papa']) + rr(46, 66, 28, 22, 5, C['crema']),
 'queso': f'<path d="M14 28 H106 V52 C106 64 92 64 92 52 V48 H80 V86 C80 100 62 100 62 86 V48 H50 V68 C50 80 36 80 36 68 V48 H28 V58 C28 68 14 68 14 58 Z" fill="{C["queso"]}"/><path d="M26 38 H60" stroke="#FFF6C8" stroke-width="5"/>',
 'para-llevar': f'<path d="M46 40 C46 16 74 16 74 40" fill="none"/><path d="M28 40 H92 L98 108 H22 Z" fill="{C["crema"]}"/><path d="M40 64 C50 84 70 84 80 64 Z" fill="{C["rojo"]}"/>',
 'ubicacion': f'<path d="M60 10 C38 10 22 27 22 48 C22 76 60 110 60 110 C60 110 98 76 98 48 C98 27 82 10 60 10 Z" fill="{C["rojo"]}"/><circle cx="60" cy="47" r="15" fill="{C["crema"]}"/>',
 'horario': f'<circle cx="60" cy="60" r="46" fill="{C["crema"]}"/><path d="M60 32 V60 L80 72" fill="none" stroke-width="8"/>',
 'mensaje': f'<path d="M18 22 H102 V82 H58 L36 104 V82 H18 Z" fill="{C["papa"]}"/><path d="M36 44 H84 M36 60 H68" stroke-width="7"/>',
 'estrella': f'<path d="{ESTR}" fill="{C["papa"]}"/>',
 'picante': f'<path d="M60 8 C82 34 98 50 98 72 C98 96 80 112 60 112 C40 112 22 96 22 72 C22 58 30 48 40 40 C42 52 48 58 54 58 C50 40 52 24 60 8 Z" fill="{C["rojo"]}"/><path d="M60 62 C72 74 78 82 78 92 C78 102 70 108 60 108 C50 108 42 102 42 92 C42 84 50 76 60 62 Z" fill="{C["papa"]}" stroke-width="4"/>',
 'corazon': f'<path d="M60 104 C12 70 10 26 38 20 C50 18 58 26 60 34 C62 26 70 18 82 20 C110 26 108 70 60 104 Z" fill="{C["rojo"]}"/>',
 'segundo-piso': f'<path d="M14 104 H40 V78 H66 V52 H92 V26 H108" fill="none" stroke-width="9"/><path d="M84 14 L108 26 L88 44" fill="none" stroke-width="9" stroke="{C["rojo"]}"/>',
 'combo': PAPITAS.replace('rotate(', 'translate(-18 0) rotate(') + f'<path d="M12 58 L72 58 L66 108 L18 108 Z" fill="{C["rojo"]}"/><path d="M70 56 L106 56 L102 108 L74 108 Z" fill="{C["papa"]}"/>' + rr(66, 46, 44, 10, 4, C['crema']) + '<path d="M94 46 L102 24" fill="none"/>',
}
for k, c in ICONOS.items(): out(f'iconos/svg/icono-{k}.svg', ic(c))
# ---------- Patrones ----------
ray = ''.join(f'<path d="M540 540 L{540 + 1200 * math.cos(math.radians(i * 22.5)):.0f} {540 + 1200 * math.sin(math.radians(i * 22.5)):.0f} L{540 + 1200 * math.cos(math.radians(i * 22.5 + 11.25)):.0f} {540 + 1200 * math.sin(math.radians(i * 22.5 + 11.25)):.0f} Z" fill="{{c}}"/>' for i in range(16))
for nom, a, b in (('amarillo', C['papa'], '#FFD04A'), ('rojo', C['rojo'], '#EC5A45'), ('noche', N, '#262036'), ('crema', C['crema'], '#FFE9B8')):
    out(f'patrones/svg/rayos-{nom}.svg', svg(1080, 1080, f'<rect width="1080" height="1080" fill="{a}"/>' + ray.replace('{c}', b)))
import random; random.seed(7)
def confeti(bg, cols):
    t = ''.join(f'<rect x="{x}" y="{y}" width="16" height="{h}" rx="4" fill="{cols[i % len(cols)]}" stroke="{N}" stroke-width="5" transform="rotate({r} {x + 8} {y + h / 2})"/>' for i, (x, y, h, r) in enumerate([(40, 30, 70, 20), (150, 60, 56, -35), (260, 20, 64, 70), (330, 110, 70, -10), (60, 170, 60, -60), (190, 190, 72, 15), (300, 250, 58, 45), (90, 300, 66, 5), (220, 320, 60, -25), (350, 340, 50, 80), (20, 370, 20, 0), (140, 110, 20, 40)]))
    return svg(800, 800, f'<defs><pattern id="p" width="400" height="400" patternUnits="userSpaceOnUse">{t}</pattern></defs><rect width="800" height="800" fill="{bg}"/><rect width="800" height="800" fill="url(#p)"/>')
out('patrones/svg/papas-confeti-crema.svg', confeti(C['crema'], [ILU['papa_clara'], ILU['papa_tostada'], C['rojo']]))
out('patrones/svg/papas-confeti-rojo.svg', confeti(C['rojo'], [ILU['papa_clara'], ILU['papa_tostada'], C['crema']]))
out('patrones/svg/papas-confeti-noche.svg', confeti(N, [ILU['papa_clara'], ILU['papa_tostada'], C['rojo']]))
out('patrones/svg/cuadros-picnic.svg', svg(800, 800, f'<defs><pattern id="p" width="160" height="160" patternUnits="userSpaceOnUse"><rect width="160" height="160" fill="{C["crema"]}"/><rect width="80" height="160" fill="{C["rojo"]}" opacity=".55"/><rect width="160" height="80" fill="{C["rojo"]}" opacity=".55"/></pattern></defs><rect width="800" height="800" fill="url(#p)"/>'))
out('patrones/svg/puntos-amarillo.svg', svg(800, 800, f'<defs><pattern id="p" width="80" height="80" patternUnits="userSpaceOnUse"><rect width="80" height="80" fill="{C["papa"]}"/><circle cx="20" cy="20" r="9" fill="{C["rojo"]}"/><circle cx="60" cy="60" r="9" fill="{C["rojo"]}"/></pattern></defs><rect width="800" height="800" fill="url(#p)"/>'))
for nom, f in (('amarillo', C['queso']), ('crema', C['crema'])):
    out(f'patrones/svg/queso-borde-{nom}.svg', svg(1200, 208, ''.join(f'<path d="{DRIP}" fill="{f}" stroke="{N}" stroke-width="2.4" stroke-linejoin="round" transform="translate({i * 596} 0) scale(2)"/>' for i in range(2)), '0 0 1196 208'))
# ---------- Colores ----------
def rgb(h): return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
def cmyk(h):
    r, g, b = [x / 255 for x in rgb(h)]; k = 1 - max(r, g, b)
    return (0, 0, 0, 100) if k == 1 else tuple(round(100 * x) for x in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k))
def hsl(h): r, g, b = [x / 255 for x in rgb(h)]; hh, l, s = colorsys.rgb_to_hls(r, g, b); return (round(hh * 360), round(s * 100), round(l * 100))
def lum(h): return sum(c * (x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4) for c, x in zip((.2126, .7152, .0722), [v / 255 for v in rgb(h)]))
def contraste(a, b): la, lb = sorted((lum(a), lum(b)), reverse=True); return round((la + .05) / (lb + .05), 2)
NOM = dict(crema=('Crema', 'Fondo principal, empaques, respiro'), rojo=('Rojo salsa', 'Color de marca: letras del logo, llamados, cajas'), noche=('Noche', 'Contornos, sombras, texto, fondos nocturnos'), papa=('Papa', 'Energía: fondos de antojo, la piel de Loqui, acentos'), queso=('Queso', 'El queso derretido y brillos'))
NOMI = dict(papa_clara='Papa frita clara', papa_tostada='Papa frita tostada', boca='Boca', lengua='Lengua', lengua_linea='Línea de la lengua', pan='Pan', pan_tostado='Pan tostado', carne='Carne', lechuga='Lechuga', salchicha='Salchicha', salsa_rosada='Salsa rosada', blanco='Blanco')
pal = {'principal': [dict(id=k, nombre=NOM[k][0], uso=NOM[k][1], hex=v, rgb=rgb(v), cmyk_aprox=cmyk(v), hsl=hsl(v)) for k, v in C.items()],
       'ilustracion': [dict(id=k, nombre=NOMI[k], hex=v, rgb=rgb(v), cmyk_aprox=cmyk(v)) for k, v in ILU.items()],
       'contraste': [dict(texto=a, fondo=b, razon=contraste(C[a], C[b]), sirve_para='texto normal' if contraste(C[a], C[b]) >= 4.5 else 'solo títulos grandes' if contraste(C[a], C[b]) >= 3 else 'no usar para texto') for a in C for b in C if a != b],
       'nota': 'Los valores CMYK son una conversión de referencia. Para impresión, pide prueba de color a la imprenta.'}
out('colores/paleta.json', json.dumps(pal, ensure_ascii=False, indent=1))
out('colores/paleta.css', ':root{\n' + ''.join(f'  --lq-{k}: {v};\n' for k, v in C.items()) + ''.join(f'  --lq-{k.replace("_", "-")}: {v};\n' for k, v in ILU.items()) + '  --lq-fuente-titulos: "Luckiest Guy", sans-serif;\n  --lq-fuente-acento: "Permanent Marker", cursive;\n  --lq-fuente-texto: "Work Sans", system-ui, sans-serif;\n  --lq-sombra-dura: 0.045em 0.045em 0 var(--lq-noche);\n  --lq-contorno: 0.06em solid var(--lq-noche);\n}\n')
out('colores/paleta.gpl', 'GIMP Palette\nName: Loquipapas\nColumns: 5\n#\n' + ''.join('%3d %3d %3d\t%s\n' % (*rgb(v), NOM[k][0]) for k, v in C.items()) + ''.join('%3d %3d %3d\t%s\n' % (*rgb(v), NOMI[k]) for k, v in ILU.items()))
def ase(cols):
    b = b''
    for name, h in cols:
        n = (name + '\0').encode('utf-16-be'); blk = struct.pack('>H', len(name) + 1) + n + b'RGB ' + struct.pack('>fff', *[x / 255 for x in rgb(h)]) + struct.pack('>H', 0)
        b += struct.pack('>HI', 1, len(blk)) + blk
    return b'ASEF' + struct.pack('>HHI', 1, 0, len(cols)) + b
out('colores/paleta.ase', ase([(NOM[k][0], v) for k, v in C.items()] + [(NOMI[k], v) for k, v in ILU.items()]), 'wb')
# ---------- Tipografías instalables ----------
for carp, pesos, nom in (('luckiest-guy', [400], 'LuckiestGuy'), ('permanent-marker', [400], 'PermanentMarker'), ('work-sans', [500, 700, 900], 'WorkSans')):
    for p in pesos:
        f = TTFont(f'{FS}/{carp}/files/{carp}-latin-{p}-normal.woff'); f.flavor = None
        f.save(os.path.join(RAIZ, 'tipografia', 'x')) if False else None
        os.makedirs(os.path.join(RAIZ, 'tipografia', 'fuentes'), exist_ok=True); f.save(os.path.join(RAIZ, 'tipografia', 'fuentes', f'{nom}-{p}.ttf'))
        shutil.copy(f'{FS}/{carp}/files/{carp}-latin-{p}-normal.woff2', os.path.join(RAIZ, 'tipografia', 'fuentes', f'{nom}-{p}.woff2'))
    shutil.copy(f'{FS}/{carp}/LICENSE', os.path.join(RAIZ, 'tipografia', 'fuentes', f'LICENCIA-{nom}.txt'))
print('ok', sum(len(f) for _, _, f in os.walk(RAIZ)))
