# -*- coding: utf-8 -*-
"""Genera una miniatura por pagina, en PNG de 1200x630.

Para que sirven: son la imagen que aparece cuando alguien comparte un
enlace del sitio en WhatsApp, X, Discord, Telegram, LinkedIn o Slack. Sin
ella, el enlace sale como un bloque de texto gris que nadie pulsa.

Por que PNG y no SVG: las plataformas sociales no renderizan SVG en
`og:image`. Es el unico sitio del proyecto donde el formato vectorial no
sirve.

El diseno es el mismo sistema editorial del sitio: fondo plano, serif
para el titular, filete de 1px y el naranja usado con cuentagotas.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
MARGEN = 84

BLANCO = (255, 255, 255)
TINTA = (17, 17, 17)
SUAVE = (107, 107, 107)
FILETE = (229, 229, 229)
ACENTO = (255, 79, 0)

FUENTES = "C:/Windows/Fonts/"
SERIF = FUENTES + "cambria.ttc"
SERIF_CURSIVA = FUENTES + "cambriai.ttf"
SANS = FUENTES + "calibrib.ttf"


def _fuente(ruta, tam):
    try:
        return ImageFont.truetype(ruta, tam)
    except Exception:
        return ImageFont.load_default()


def _ancho(draw, texto, fuente):
    return draw.textlength(texto, font=fuente)


def _espaciado(draw, xy, texto, fuente, color, extra=3.2):
    """Dibuja texto con separacion entre letras. Pillow no la soporta,
    asi que se dibuja caracter a caracter."""
    x, y = xy
    for ch in texto:
        draw.text((x, y), ch, font=fuente, fill=color)
        x += _ancho(draw, ch, fuente) + extra
    return x


def _partir(draw, texto, fuente, ancho_max):
    """Reparte el titular en lineas sin cortar palabras."""
    palabras = texto.split()
    lineas, actual = [], ""
    for p in palabras:
        prueba = (actual + " " + p).strip()
        if _ancho(draw, prueba, fuente) <= ancho_max or not actual:
            actual = prueba
        else:
            lineas.append(actual)
            actual = p
    if actual:
        lineas.append(actual)
    return lineas


def _nombre(slug):
    return slug.strip("/").replace("/", "-") or "home"


def _dibujar(titulo, etiqueta, destino):
    img = Image.new("RGB", (W, H), BLANCO)
    d = ImageDraw.Draw(img)

    f_etiqueta = _fuente(SANS, 21)
    f_pie = _fuente(SANS, 22)
    f_marca_serif = _fuente(SERIF, 34)
    f_marca_cursiva = _fuente(SERIF_CURSIVA, 34)

    # Antetitulo: filete de acento + etiqueta en versales espaciadas.
    y = 92
    if etiqueta:
        d.rectangle([MARGEN, y + 11, MARGEN + 46, y + 13], fill=ACENTO)
        _espaciado(d, (MARGEN + 64, y), etiqueta.upper(), f_etiqueta, SUAVE)

    # Titular: se reduce el cuerpo hasta que quepa en tres lineas.
    ancho_max = W - MARGEN * 2
    for tam in (74, 68, 62, 56, 50, 46):
        f_titulo = _fuente(SERIF, tam)
        lineas = _partir(d, titulo, f_titulo, ancho_max)
        if len(lineas) <= 3:
            break
    alto_linea = int(tam * 1.14)

    y = 196
    for linea in lineas[:3]:
        d.text((MARGEN, y), linea, font=f_titulo, fill=TINTA)
        y += alto_linea

    # Pie: filete fino, marca a la izquierda y dominio a la derecha.
    y_filete = H - 132
    d.rectangle([MARGEN, y_filete, W - MARGEN, y_filete + 1], fill=FILETE)

    y_marca = y_filete + 34
    x = MARGEN
    d.text((x, y_marca), "Micros", font=f_marca_serif, fill=TINTA)
    x += _ancho(d, "Micros", f_marca_serif)
    d.text((x, y_marca), "Streaming", font=f_marca_cursiva, fill=ACENTO)

    dominio = "microstreaming.github.io"
    d.text((W - MARGEN - _ancho(d, dominio, f_pie), y_marca + 10),
           dominio, font=f_pie, fill=SUAVE)

    os.makedirs(os.path.dirname(destino), exist_ok=True)
    img.save(destino, "PNG", optimize=True)


def generar(PAGES, root_dir):
    """Crea una miniatura por pagina y devuelve cuantas escribio."""
    salida = os.path.join(root_dir, "assets", "og")
    n = 0
    for slug, page in PAGES.items():
        etiqueta = page.get("kind") or ("Guía" if page.get("article") else "")
        if not slug:
            etiqueta = "Streaming · Creadores · Podcast · Homestudio"
        _dibujar(page["h1"], etiqueta,
                 os.path.join(salida, _nombre(slug) + ".png"))
        n += 1
    return n


def ruta_og(slug):
    """Ruta publica de la miniatura, relativa a la raiz del sitio."""
    return "assets/og/%s.png" % _nombre(slug)
