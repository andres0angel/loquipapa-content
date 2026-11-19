# Piezas base de la identidad de LOQUIPAPAS: colores, tipografías convertidas a trazos, logo, mascota.
import os, re, json, math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FS = os.environ.get('FUENTES', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'node_modules', '@fontsource'))

C = dict(crema='#FFF3D6', rojo='#E2412B', noche='#1B1726', papa='#FFC21A', queso='#FFD84A')
ILU = dict(papa_clara='#FFD54A', papa_tostada='#F5B014', boca='#7A1C22', lengua='#FF5A7A', lengua_linea='#D63A5E',
           pan='#F2B04A', pan_tostado='#E8A23D', carne='#6B3A22', lechuga='#7BC043', salchicha='#C8553A', salsa_rosada='#FF8FA3', blanco='#FFFFFF')
N = C['noche']

def out(rel, data, mode='w'):
    p = os.path.join(RAIZ, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, mode, **({} if 'b' in mode else {'encoding': 'utf-8'})) as f: f.write(data)
    return p

class Fuente:
    def __init__(self, carpeta, peso=400):
        self.ruta = f'{FS}/{carpeta}/files/{carpeta}-latin-{peso}-normal.woff'
        self.f = TTFont(self.ruta); self.gs = self.f.getGlyphSet(); self.cmap = self.f.getBestCmap()
        self.upm = self.f['head'].unitsPerEm; self.asc = self.f['hhea'].ascent / self.upm; self.desc = -self.f['hhea'].descent / self.upm
        self.cap = getattr(self.f['OS/2'], 'sCapHeight', 0) / self.upm or .7
    def adv(self, ch, size): return self.gs[self.cmap[ord(ch)]].width * size / self.upm
    def glifo(self, ch, size, x=0, y=0):
        s = size / self.upm; pen = SVGPathPen(self.gs); self.gs[self.cmap[ord(ch)]].draw(TransformPen(pen, (s, 0, 0, -s, x, y)))
        return pen.getCommands()
    def ancho(self, txt, size): return sum(self.adv(c, size) for c in txt)
    def texto(self, txt, size, x=0, y=0, ancla='start'):
        w = self.ancho(txt, size); x -= w if ancla == 'end' else w / 2 if ancla == 'middle' else 0; d = []
        for c in txt:
            if c != ' ': d.append(self.glifo(c, size, x, y))
            x += self.adv(c, size)
        return ' '.join(d)

LG = Fuente('luckiest-guy'); PM = Fuente('permanent-marker'); WS9 = Fuente('work-sans', 900); WS7 = Fuente('work-sans', 700); WS5 = Fuente('work-sans', 500)

DRIP = 'M4 16 C40 6 80 20 120 10 C160 2 200 18 240 8 C262 4 284 10 298 16 L298 28 C292 30 286 30 282 32 L282 50 C282 60 268 60 268 50 L268 34 C250 36 236 34 222 36 L222 68 C222 80 204 80 204 68 L204 36 C186 34 170 36 156 34 L156 46 C156 54 144 54 144 46 L144 34 C128 36 112 34 96 36 L96 58 C96 70 80 70 80 58 L80 34 C62 32 44 34 30 32 L30 44 C30 52 18 52 18 44 L18 32 C12 30 6 30 2 28 Z'

# ---------- Mascota ----------
def pelo(c1=ILU['papa_clara'], c2=ILU['papa_tostada']):
    d = [(53, 4, 46, -50, 60, 40, 0), (73, -26, 62, -28, 80, 26, 1), (93, -28, 58, -12, 100, 20, 0), (113, -44, 72, 4, 120, 18, 1), (133, -30, 60, 18, 140, 20, 0), (153, -28, 64, 34, 160, 26, 1), (173, 6, 44, 52, 180, 40, 0)]
    return ''.join(f'<rect x="{x}" y="{y}" width="14" height="{h}" rx="3" fill="{c2 if k else c1}" stroke="{N}" stroke-width="6" transform="rotate({r} {cx} {cy})"/>' for x, y, h, r, cx, cy, k in d)
def cuerpo(piel=C['papa']): return f'<path d="M120 18 C180 14 222 58 220 112 C218 170 178 206 118 206 C60 206 20 168 20 112 C20 56 62 22 120 18 Z" fill="{piel}" stroke="{N}" stroke-width="10"/>'
def linea(d, w=10): return f'<path d="{d}" fill="none" stroke="{N}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def ojo(cx, cy, r, px=0, py=0, pr=None):
    pr = pr or r * .38
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" stroke="{N}" stroke-width="{8 if r > 18 else 7}"/><circle cx="{cx + px}" cy="{cy + py}" r="{pr:.1f}" fill="{N}"/><circle cx="{cx + px + pr * .36:.1f}" cy="{cy + py - pr * .36:.1f}" r="{pr * .32:.1f}" fill="#FFFFFF"/>'
def corazon(cx, cy, s): return f'<path d="M{cx} {cy + s * .9:.1f} C{cx - s * 1.5:.1f} {cy - s * .1:.1f} {cx - s * .8:.1f} {cy - s * 1.1:.1f} {cx} {cy - s * .35:.1f} C{cx + s * .8:.1f} {cy - s * 1.1:.1f} {cx + s * 1.5:.1f} {cy - s * .1:.1f} {cx} {cy + s * .9:.1f} Z" fill="{C["rojo"]}" stroke="{N}" stroke-width="7" stroke-linejoin="round"/>'
BOCA_LOCA = (f'<path d="M66 146 C84 200 162 200 180 140 C146 156 102 158 66 146 Z" fill="{ILU["boca"]}" stroke="{N}" stroke-width="8" stroke-linejoin="round"/>'
             f'<path d="M116 160 L174 150 C181 186 175 214 151 216 C127 218 114 192 116 160 Z" fill="{ILU["lengua"]}" stroke="{N}" stroke-width="7" stroke-linejoin="round"/>'
             f'<path d="M146 178 C148 190 148 200 147 206" fill="none" stroke="{ILU["lengua_linea"]}" stroke-width="4" stroke-linecap="round"/>'
             '<path d="M72 150 C104 162 148 160 176 145 C175 151 173 156 170 160 C146 170 104 172 78 162 C76 158 74 154 72 150 Z" fill="#FFFFFF"/>'
             + linea('M66 146 C102 158 146 156 180 140', 8))
BOCA_FELIZ = (f'<path d="M62 146 C82 204 164 204 184 146 C146 160 100 160 62 146 Z" fill="{ILU["boca"]}" stroke="{N}" stroke-width="8" stroke-linejoin="round"/>'
              '<path d="M70 151 C104 164 146 164 178 151 C177 157 175 161 172 165 C146 174 104 174 76 165 C74 160 72 156 70 151 Z" fill="#FFFFFF"/>'
              f'<path d="M98 188 C110 174 140 174 152 188 C140 197 110 197 98 188 Z" fill="{ILU["lengua"]}"/>' + linea('M62 146 C100 160 146 160 184 146', 8))
EXPRESIONES = {
 'loco': ('Loco (oficial)', linea('M54 72 C66 54 98 52 114 64') + linea('M142 96 L178 102') + ojo(86, 110, 29, 7, -7, 11) + ojo(160, 122, 14, -3, 2, 6) + BOCA_LOCA),
 'feliz': ('Feliz', linea('M56 78 C70 64 96 62 110 72') + linea('M134 74 C148 64 170 66 182 80') + ojo(88, 112, 22, 3, -3) + ojo(156, 112, 22, 3, -3) + BOCA_FELIZ),
 'guino': ('Guiño', linea('M54 72 C66 54 98 52 114 64') + linea('M140 98 L180 100') + ojo(86, 110, 29, 7, -7, 11) + linea('M142 124 C150 112 170 112 178 124', 8) + BOCA_LOCA),
 'sorpresa': ('Sorprendido', linea('M56 60 C70 46 96 46 110 56') + linea('M136 56 C150 46 172 48 184 60') + ojo(86, 110, 26, 0, 0, 7) + ojo(158, 110, 26, 0, 0, 7) + f'<ellipse cx="122" cy="170" rx="18" ry="24" fill="{ILU["boca"]}" stroke="{N}" stroke-width="8"/>'),
 'enamorado': ('Enamorado', linea('M56 70 C70 58 96 58 110 66') + linea('M136 66 C150 58 172 60 184 72') + corazon(86, 112, 22) + corazon(158, 112, 22) + BOCA_FELIZ),
 'antojo': ('Antojado', linea('M54 64 C66 50 98 50 114 60') + linea('M136 62 C150 52 172 54 184 66') + ojo(88, 110, 22, 0, 8) + ojo(156, 110, 22, 0, 8) + BOCA_LOCA + f'<path d="M170 218 C177 229 179 236 170 240 C161 236 163 229 170 218 Z" fill="#9ADCF5" stroke="{N}" stroke-width="5" stroke-linejoin="round"/>'),
 'dormido': ('Dormido', linea('M60 86 C72 80 96 80 108 86') + linea('M138 88 C150 82 170 82 182 88') + linea('M64 112 C74 126 98 126 108 112', 8) + linea('M138 114 C148 128 170 128 180 114', 8) + f'<ellipse cx="124" cy="168" rx="12" ry="9" fill="{ILU["boca"]}" stroke="{N}" stroke-width="7"/>' + linea('M196 38 L218 38 L196 62 L218 62', 7) + linea('M222 4 L236 4 L222 20 L236 20', 5)),
 'picante': ('Picante', linea('M54 64 L110 84') + linea('M188 68 L138 86') + ojo(88, 114, 20, 3, 0) + ojo(156, 114, 20, -3, 0) + f'<path d="M78 152 H170 V178 C150 192 98 192 78 178 Z" fill="#FFFFFF" stroke="{N}" stroke-width="8" stroke-linejoin="round"/>' + linea('M101 154 V184', 5) + linea('M124 154 V187', 5) + linea('M147 154 V184', 5) + f'<path d="M206 70 C214 84 216 92 206 96 C196 92 198 84 206 70 Z" fill="#9ADCF5" stroke="{N}" stroke-width="5" stroke-linejoin="round"/>'),
}
def cabeza(expr='loco', piel=C['papa'], c1=ILU['papa_clara'], c2=ILU['papa_tostada']): return pelo(c1, c2) + cuerpo(piel) + EXPRESIONES[expr][1]
def plano(svg, color): return re.sub(r'(fill|stroke)="(#[0-9A-Fa-f]{6})"', lambda m: f'{m.group(1)}="{color}"', svg)
def tinta(svg, ink, papel):
    osc = {N.upper(), ILU['boca'].upper()}
    def f(m):
        if m.group(1) == 'stroke': return f'stroke="{ink}"'
        return f'fill="{ink if m.group(2).upper() in osc else papel}"'
    return re.sub(r'(fill|stroke)="(#[0-9A-Fa-f]{6})"', f, svg)
def svg(w, h, cuerpo_, vb=None, titulo=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb or f"0 0 {w:g} {h:g}"}" width="{w:g}" height="{h:g}" role="img"' + (f' aria-label="{titulo}"><title>{titulo}</title>' if titulo else '>') + cuerpo_ + '</svg>'

# ---------- Logo ----------
VAR = {
 'crema': dict(fondo=C['crema'], letras=C['rojo'], sombra=N, desc=N, queso=C['queso']),
 'noche': dict(fondo=N, letras=C['crema'], sombra=C['rojo'], desc=C['papa'], queso=C['queso']),
 'rojo': dict(fondo=C['rojo'], letras=C['crema'], sombra=N, desc=C['papa'], queso=C['queso']),
 'amarillo': dict(fondo=C['papa'], letras=C['rojo'], sombra=N, desc=N, queso=C['crema']),
}
F1 = [('L', 0, -6), ('@', 0, -8), ('Q', -14, 5), ('U', 10, -4), ('I', -8, 7)]
F2 = [('P', 6, -5), ('A', -12, 4), ('P', 8, -7), ('A', -6, 5), ('S', 6, -4)]
def fila(items, S, x, base, v, mono=None):
    """Devuelve (sombra, frente, ancho). '@' es la cara de Loqui en lugar de la O."""
    so, fr = [], []; d = S * .045
    for ch, dy, rot in items:
        if ch == '@':
            w = S; k = S / 240; hy = base - LG.cap * S / 2 - 229 / 200 * S / 2 + dy
            t = f'translate({x + S * .02:.1f} {hy:.1f}) rotate({rot} {w / 2:.1f} {S * .57:.1f}) scale({k:.4f}) translate(0 50)'
            h = cabeza() if not mono else tinta(cabeza(), mono[0], mono[1])
            if v['sombra']: so.append(f'<g transform="translate({d:.1f} {d:.1f}) {t}">{plano(cabeza(), v["sombra"])}</g>')
            fr.append(f'<g transform="{t}">{h}</g>'); x += w + S * .04
        else:
            a = LG.adv(ch, S); cx, cy = x + a / 2, base - LG.cap * S / 2 + dy; p = LG.glifo(ch, S, x, base + dy)
            if v['sombra']: so.append(f'<path d="{p}" fill="{v["sombra"]}" transform="translate({d:.1f} {d:.1f}) rotate({rot} {cx:.1f} {cy:.1f})"/>')
            fr.append(f'<path d="{p}" fill="{v["letras"]}" transform="rotate({rot} {cx:.1f} {cy:.1f})"/>'); x += a
    return ''.join(so), ''.join(fr), x
def ancho_fila(items, S): return sum(S * 1.04 if c == '@' else LG.adv(c, S) for c, _, _ in items)
def queso(x, y, w, h, fill, extra=True, borde=N):
    k = f'translate({x:.1f} {y:.1f}) scale({w / 300:.4f} {h / 104:.4f})'
    s = f'<g transform="{k}">' + (f'<path d="{DRIP}" fill="{N}" opacity=".3" transform="translate(0 4)"/>' if extra else '') + f'<path d="{DRIP}" fill="{fill}" stroke="{borde}" stroke-linejoin="round" vector-effect="non-scaling-stroke" style="stroke-width:5px"/>'
    if extra: s += '<path d="M30 16 C56 10 84 18 108 12 M170 10 C190 6 212 12 230 8 M209 44 L209 62 M85 42 L85 54" fill="none" stroke="#FFF6C8" stroke-width="3" stroke-linecap="round"/>' + f'<path d="M213 84 C219 92 221 97 213 100 C205 97 207 92 213 84 Z M88 74 C92 80 93 83 88 85 C83 83 84 80 88 74 Z" fill="{fill}" stroke="{N}" stroke-width="2"/>'
    return s + '</g>'
def logo_apilado(var='crema', fondo=True, S=200, mono=None):
    v = dict(VAR[var]);
    if mono: v.update(letras=mono[0], sombra=None, desc=mono[0], queso=mono[1])
    w1, w2 = ancho_fila(F1, S), ancho_fila(F2, S); pad = S * .42; W = max(w1, w2) + pad * 2; lh = S * .92
    b1 = pad + S * .62 + LG.cap * S; b2 = b1 + lh + S * .02
    s1, f1, _ = fila(F1, S, (W - w1) / 2, b1, v, mono); x2 = (W - w2) / 2; s2, f2, _ = fila(F2, S, x2, b2, v, mono)
    q = queso(x2 - S * .1, b2 - LG.cap * S - S * .17, w2 + S * .2, S * .6, v['queso'], not mono, mono[0] if mono else N)
    ty = b2 + S * .3 + S * .36; ds = S * .42; tw = PM.ancho('papas locas', ds)
    desc = f'<path d="{PM.texto("papas locas", ds, W / 2, ty, "middle")}" fill="{v["desc"]}" transform="rotate(-5 {W / 2:.1f} {ty - ds * .3:.1f})"/>'
    H = ty + pad * .75
    bg = f'<rect width="{W:.0f}" height="{H:.0f}" fill="{v["fondo"]}"/>' if fondo and not mono else ''
    return svg(round(W), round(H), bg + s1 + s2 + f1 + f2 + q + desc, titulo='Logo de Loquipapas, papas locas')
FL = [('L', 0, -5), ('@', 0, -7), ('Q', -6, 4), ('U', 5, -3), ('I', -4, 5), ('P', 3, -4), ('A', -6, 3), ('P', 4, -5), ('A', -3, 4), ('S', 3, -3)]
def logo_linea(var='crema', fondo=True, S=120, mono=None, desc=True):
    v = dict(VAR[var])
    if mono: v.update(letras=mono[0], sombra=None, desc=mono[0])
    w = ancho_fila(FL, S); pad = S * .4; W = w + pad * 2; b = pad + S * .5 + LG.cap * S
    so, fr, _ = fila(FL, S, pad, b, v, mono); ds = S * .36; ty = b + S * .5; H = (ty if desc else b) + pad * .8
    d = f'<path d="{PM.texto("papas locas", ds, W - pad, ty, "end")}" fill="{v["desc"]}" transform="rotate(-3 {W - pad - 100:.1f} {ty:.1f})"/>' if desc else ''
    bg = f'<rect width="{W:.0f}" height="{H:.0f}" fill="{v["fondo"]}"/>' if fondo and not mono else ''
    return svg(round(W), round(H), bg + so + fr + d, titulo='Logo de Loquipapas en una línea')
def avatar(var='rojo', expr='loco', S=512):
    f = {'rojo': C['rojo'], 'crema': C['crema'], 'amarillo': C['papa'], 'noche': N}[var]
    return svg(S, S, f'<circle cx="256" cy="256" r="246" fill="{f}" stroke="{N}" stroke-width="16"/><g transform="translate(86 120) scale(1.42)">{cabeza(expr)}</g>', '0 0 512 512', 'Loqui, la mascota de Loquipapas')
def isotipo(expr='loco', mono=None, piel=C['papa']):
    h = cabeza(expr, piel); h = tinta(h, mono[0], mono[1]) if mono else h
    return svg(480, 550, h, '-8 -56 256 290', f'Loqui: {EXPRESIONES[expr][0]}')
