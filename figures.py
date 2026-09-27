# -*- coding: utf-8 -*-
"""Diagramas del sitio, en SVG generado.

Son ilustraciones propias, no fotos de catalogo: explican el concepto de
la pagina donde aparecen, pesan unos pocos kB, se adaptan al tema claro y
oscuro porque usan currentColor, y no dependen de ninguna peticion extra.

Se insertan en el contenido con el marcador [[fig:nombre]], que build.py
sustituye al generar.
"""
import math

ACCENT = "#FF4F00"


# ---------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------
def _polar(fn, cx, cy, radius, steps=144):
    """Convierte una funcion polar r(theta) en puntos de poligono.

    El frente del microfono apunta hacia arriba, que es como se dibujan
    siempre los patrones en las fichas tecnicas.
    """
    pts = []
    for i in range(steps + 1):
        th = 2 * math.pi * i / steps
        r = max(0.0, fn(th)) * radius
        pts.append((cx + r * math.sin(th), cy - r * math.cos(th)))
    return " ".join("%.2f,%.2f" % p for p in pts)


PATTERNS = [
    ("Cardioide", lambda t: (1 + math.cos(t)) / 2),
    ("Supercardioide", lambda t: abs(0.37 + 0.63 * math.cos(t))),
    ("Omnidireccional", lambda t: 1.0),
    ("Bidireccional", lambda t: abs(math.cos(t))),
]


def _figure(svg, caption, label):
    return ('<figure class="fig">'
            '<div class="fig-art" role="img" aria-label="%s">%s</div>'
            '<figcaption>%s</figcaption></figure>' % (label, svg, caption))


# ---------------------------------------------------------------------
# 1. Patrones polares
# ---------------------------------------------------------------------
def patrones():
    cells = []
    for idx, (name, fn) in enumerate(PATTERNS):
        cx = 60 + idx * 130
        cy = 62
        rings = "".join(
            '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="currentColor" '
            'stroke-width="1" opacity=".18"/>' % (cx, cy, r)
            for r in (14, 28, 42))
        shape = ('<polygon points="%s" fill="%s" fill-opacity=".14" '
                 'stroke="%s" stroke-width="2" stroke-linejoin="round"/>'
                 % (_polar(fn, cx, cy, 42), ACCENT, ACCENT))
        mic = ('<circle cx="%d" cy="%d" r="3.4" fill="currentColor"/>' % (cx, cy))
        txt = ('<text x="%d" y="124" text-anchor="middle" fill="currentColor" '
               'font-size="11" letter-spacing="1.1" opacity=".75">%s</text>'
               % (cx, name.upper()))
        cells.append(rings + shape + mic + txt)

    svg = ('<svg viewBox="0 0 540 136" xmlns="http://www.w3.org/2000/svg" '
           'width="100%%" height="auto">%s</svg>' % "".join(cells))
    return _figure(
        svg,
        "Desde dónde escucha cada patrón. El punto es el micrófono; el frente "
        "apunta hacia arriba. Para hablar tú solo quieres siempre cardioide.",
        "Cuatro diagramas de patrón polar: cardioide, supercardioide, "
        "omnidireccional y bidireccional")


# ---------------------------------------------------------------------
# 2. Dinamico vs condensador
# ---------------------------------------------------------------------
def capsulas():
    svg = '''<svg viewBox="0 0 540 190" xmlns="http://www.w3.org/2000/svg" width="100%" height="auto">
<g stroke="currentColor" fill="none" stroke-width="1.6">
  <text x="10" y="18" fill="currentColor" font-size="11" letter-spacing="1.1" opacity=".75" stroke="none">DINÁMICO</text>
  <rect x="14" y="34" width="215" height="120" opacity=".22"/>
  <path d="M60 52 L60 136" stroke-width="2.4"/>
  <path d="M60 52 Q84 94 60 136" stroke-width="2.4" stroke="''' + ACCENT + '''"/>
  <g stroke="''' + ACCENT + '''" stroke-width="2">
    <path d="M84 74 h30 v40 h-30"/>
    <path d="M84 82 h30 M84 90 h30 M84 98 h30 M84 106 h30"/>
  </g>
  <rect x="122" y="60" width="44" height="68" opacity=".5"/>
  <text x="144" y="99" fill="currentColor" font-size="13" text-anchor="middle" stroke="none" opacity=".6">N/S</text>
  <path d="M178 94 h38" stroke-width="2"/>
  <path d="M208 88 l10 6 -10 6" stroke-width="2"/>
  <text x="34" y="172" fill="currentColor" font-size="10.5" stroke="none" opacity=".72">Bobina pesada · poco sensible</text>
</g>
<g stroke="currentColor" fill="none" stroke-width="1.6">
  <text x="300" y="18" fill="currentColor" font-size="11" letter-spacing="1.1" opacity=".75" stroke="none">CONDENSADOR</text>
  <rect x="304" y="34" width="222" height="120" opacity=".22"/>
  <path d="M350 52 L350 136" stroke-width="2.4" stroke="''' + ACCENT + '''"/>
  <path d="M372 52 L372 136" stroke-width="2.4" opacity=".55"/>
  <g stroke="''' + ACCENT + '''" stroke-width="1.2" opacity=".85">
    <path d="M352 66 h18 M352 80 h18 M352 94 h18 M352 108 h18 M352 122 h18"/>
  </g>
  <text x="361" y="44" fill="''' + ACCENT + '''" font-size="10" text-anchor="middle" stroke="none">+48 V</text>
  <path d="M392 94 h44" stroke-width="2"/>
  <path d="M428 88 l10 6 -10 6" stroke-width="2"/>
  <text x="324" y="172" fill="currentColor" font-size="10.5" stroke="none" opacity=".72">Lámina finísima · muy sensible</text>
</g>
</svg>'''
    return _figure(
        svg,
        "Lo que se mueve dentro de la cápsula explica todo lo demás: una bobina "
        "de cobre pesa y solo reacciona a lo que llega fuerte; una lámina "
        "metalizada reacciona a casi todo, incluido el cuarto.",
        "Corte esquemático de una cápsula dinámica con bobina e imán frente a "
        "una cápsula de condensador con diafragma y placa fija")


# ---------------------------------------------------------------------
# 3. Cadena USB frente a XLR
# ---------------------------------------------------------------------
def _box(x, y, w, label, accent=False):
    color = ACCENT if accent else "currentColor"
    return ('<rect x="%d" y="%d" width="%d" height="38" fill="none" '
            'stroke="%s" stroke-width="1.6" opacity="%s"/>'
            '<text x="%d" y="%d" text-anchor="middle" fill="currentColor" '
            'font-size="11" opacity=".85">%s</text>'
            % (x, y, w, color, "1" if accent else ".45",
               x + w // 2, y + 23, label))


def _arrow(x, y, length):
    return ('<path d="M%d %d h%d" stroke="currentColor" stroke-width="1.6" '
            'opacity=".5"/><path d="M%d %d l8 5 -8 5" stroke="currentColor" '
            'stroke-width="1.6" fill="none" opacity=".5"/>'
            % (x, y, length, x + length - 8, y - 5))


def cadena():
    parts = ['<svg viewBox="0 0 540 176" xmlns="http://www.w3.org/2000/svg" '
             'width="100%" height="auto">']
    parts.append('<text x="10" y="18" fill="currentColor" font-size="11" '
                 'letter-spacing="1.1" opacity=".75">RUTA USB</text>')
    parts.append(_box(10, 30, 130, "Micrófono USB", True))
    parts.append(_arrow(146, 49, 40))
    parts.append(_box(192, 30, 130, "Ordenador"))
    parts.append('<text x="336" y="53" fill="currentColor" font-size="10.5" '
                 'opacity=".72">Conversión dentro del micro</text>')

    parts.append('<text x="10" y="106" fill="currentColor" font-size="11" '
                 'letter-spacing="1.1" opacity=".75">RUTA XLR</text>')
    parts.append(_box(10, 118, 108, "Micrófono XLR", True))
    parts.append(_arrow(124, 137, 34))
    parts.append(_box(164, 118, 120, "Interfaz +48 V", True))
    parts.append(_arrow(290, 137, 34))
    parts.append(_box(330, 118, 108, "Ordenador"))
    parts.append('<text x="450" y="141" fill="currentColor" font-size="10.5" '
                 'opacity=".72">Piezas separables</text>')
    parts.append("</svg>")
    return _figure(
        "".join(parts),
        "La diferencia no es la calidad: es dónde ocurre la conversión y qué "
        "puedes cambiar después sin tirar el resto.",
        "Diagrama comparando la cadena de señal de un micrófono USB con la de "
        "un micrófono XLR a través de una interfaz de audio")


# ---------------------------------------------------------------------
# 4. Distancia y relacion voz / cuarto
# ---------------------------------------------------------------------
def distancia():
    svg = '''<svg viewBox="0 0 540 170" xmlns="http://www.w3.org/2000/svg" width="100%" height="auto">
<rect x="12" y="16" width="516" height="120" fill="none" stroke="currentColor" stroke-width="1" opacity=".22"/>
<text x="24" y="36" fill="currentColor" font-size="10.5" opacity=".6">LA HABITACIÓN SUENA IGUAL EN LOS DOS CASOS</text>
<g stroke="currentColor" fill="none">
  <circle cx="92" cy="92" r="13" stroke-width="1.6"/>
  <path d="M105 92 h34" stroke-width="1.6" opacity=".5"/>
  <rect x="139" y="78" width="12" height="28" rx="6" fill="''' + ACCENT + '''" stroke="none"/>
  <text x="122" y="122" fill="currentColor" font-size="10.5" text-anchor="middle" opacity=".72">10 cm</text>
  <rect x="86" y="46" width="70" height="12" fill="''' + ACCENT + '''" stroke="none"/>
  <rect x="156" y="46" width="14" height="12" fill="currentColor" stroke="none" opacity=".35"/>
</g>
<g stroke="currentColor" fill="none">
  <circle cx="320" cy="92" r="13" stroke-width="1.6"/>
  <path d="M333 92 h130" stroke-width="1.6" opacity=".5"/>
  <rect x="463" y="78" width="12" height="28" rx="6" fill="''' + ACCENT + '''" stroke="none"/>
  <text x="398" y="122" fill="currentColor" font-size="10.5" text-anchor="middle" opacity=".72">50 cm</text>
  <rect x="314" y="46" width="26" height="12" fill="''' + ACCENT + '''" stroke="none"/>
  <rect x="340" y="46" width="58" height="12" fill="currentColor" stroke="none" opacity=".35"/>
</g>
<text x="24" y="158" fill="''' + ACCENT + '''" font-size="10.5">Voz</text>
<text x="66" y="158" fill="currentColor" font-size="10.5" opacity=".55">Cuarto</text>
</svg>'''
    return _figure(
        svg,
        "Acercarte no reduce el ruido de la habitación: sube tu voz por encima "
        "de él. Es la mejora más grande que existe y no cuesta nada.",
        "Comparación entre hablar a 10 cm y a 50 cm del micrófono, y la "
        "proporción de voz frente a sonido de la habitación en cada caso")


# ---------------------------------------------------------------------
# 5. Cadena de filtros de OBS
# ---------------------------------------------------------------------
def filtros():
    etapas = ["Paso alto", "Puerta", "Compresor", "Ganancia", "Limitador"]
    parts = ['<svg viewBox="0 0 540 118" xmlns="http://www.w3.org/2000/svg" '
             'width="100%" height="auto">']
    x = 6
    for i, nombre in enumerate(etapas):
        parts.append(_box(x, 34, 92, nombre, accent=(i in (0, 2))))
        parts.append('<text x="%d" y="26" fill="currentColor" font-size="10" '
                     'opacity=".5">0%d</text>' % (x + 4, i + 1))
        if i < len(etapas) - 1:
            parts.append(_arrow(x + 96, 53, 12))
        x += 108
    parts.append('<text x="6" y="100" fill="currentColor" font-size="10.5" '
                 'opacity=".72">Cada filtro trabaja sobre lo que le entrega el '
                 'anterior: por eso el orden no es opcional.</text>')
    parts.append("</svg>")
    return _figure(
        "".join(parts),
        "El orden de la cadena en OBS. Comprimir antes de limpiar amplifica "
        "justo el ruido que luego intentarás quitar.",
        "Cadena de cinco filtros de audio en orden: filtro paso alto, puerta "
        "de ruido, compresor, ganancia y limitador")


# ---------------------------------------------------------------------
# 6. Montaje: brazo, arana y antipop
# ---------------------------------------------------------------------
def montaje():
    svg = '''<svg viewBox="0 0 540 200" xmlns="http://www.w3.org/2000/svg" width="100%" height="auto">
<g stroke="currentColor" fill="none" stroke-width="1.8">
  <path d="M40 186 h300" opacity=".35"/>
  <rect x="56" y="162" width="34" height="24" opacity=".6"/>
  <path d="M73 162 V128" stroke-width="2.2"/>
  <path d="M73 128 L150 74" stroke-width="2.2"/>
  <path d="M150 74 L244 96" stroke-width="2.2"/>
  <circle cx="73" cy="128" r="4.5" fill="currentColor" stroke="none" opacity=".8"/>
  <circle cx="150" cy="74" r="4.5" fill="currentColor" stroke="none" opacity=".8"/>
  <ellipse cx="268" cy="100" rx="26" ry="34" stroke="''' + ACCENT + '''" stroke-width="2"/>
  <g stroke="''' + ACCENT + '''" stroke-width="1.2" opacity=".75">
    <path d="M246 84 L262 94 M246 116 L262 106 M290 84 L274 94 M290 116 L274 106"/>
  </g>
  <rect x="258" y="82" width="20" height="38" rx="10" fill="''' + ACCENT + '''" stroke="none"/>
  <circle cx="316" cy="100" r="22" stroke-width="1.6" opacity=".55"/>
  <path d="M316 78 v44" stroke-width="1" opacity=".35"/>
</g>
<g fill="currentColor" font-size="10.5" opacity=".72">
  <text x="14" y="180">Pinza</text>
  <text x="120" y="60">Brazo</text>
  <text x="232" y="158">Araña</text>
  <text x="300" y="158">Antipop</text>
</g>
</svg>'''
    return _figure(
        svg,
        "El montaje completo. La araña corta las vibraciones que viajan por la "
        "mesa; el brazo es lo que te permite hablar cerca sin apoyar nada.",
        "Esquema de un brazo articulado anclado con pinza a la mesa, con araña "
        "antivibración, micrófono y filtro antipop")


FIGURES = {
    "patrones": patrones,
    "capsulas": capsulas,
    "cadena": cadena,
    "distancia": distancia,
    "filtros": filtros,
    "montaje": montaje,
}


def render(name):
    fn = FIGURES.get(name)
    if fn is None:
        raise KeyError("No existe la figura %r. Disponibles: %s"
                       % (name, ", ".join(sorted(FIGURES))))
    return fn()
