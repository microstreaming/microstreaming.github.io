# -*- coding: utf-8 -*-
"""Generador estatico del sitio Micros Streaming.

Uso: python build.py   (escribe los index.html en la raiz del repo)

El contenido vive en content.py (guias) y content_modelos.py (fichas por
modelo). Este modulo solo se ocupa de la plantilla, el marcado comun y los
ficheros auxiliares (sitemap, robots, 404).
"""
import json
import os
import re

import content_guias
import content_modelos
from content import NOT_FOUND, PAGES, SITE

# El contenido se reparte en modulos para no inflar content.py:
# las fichas por modelo y las guias de apoyo van aparte.
content_modelos.add_pages(PAGES, SITE)
content_guias.add_pages(PAGES, SITE)

BASE = SITE["base"]
TODAY = SITE["updated"]

NAV = [
    ("", "Inicio"),
    ("mejores-micros-streaming/", "Mejores micros"),
    ("por-modelo/", "Por modelo"),
    ("microfono-condensador/", "Condensador"),
    ("usb-o-xlr/", "USB o XLR"),
    ("micros-streaming-baratos/", "Baratos"),
    ("microfono-para-telefono/", "Para teléfono"),
]

FOOTER_COLS = [
    ("Guías", [
        ("mejores-micros-streaming/", "Mejores micros"),
        ("usb-o-xlr/", "USB o XLR"),
        ("microfono-condensador/", "Condensador"),
        ("micros-streaming-baratos/", "Baratos"),
        ("microfono-para-telefono/", "Para teléfono"),
    ]),
    ("Por modelo", [
        ("por-modelo/", "Todas las fichas"),
        ("behringer-c1/", "Behringer C-1"),
        ("behringer-c3/", "Behringer C-3"),
        ("hyperx-quadcast-rgb/", "HyperX QuadCast"),
    ]),
    ("Aprender", [
        ("dinamico-vs-condensador/", "Dinámico vs condensador"),
        ("configurar-microfono-obs/", "Micrófono en OBS"),
        ("quitar-ruido-de-fondo/", "Quitar ruido de fondo"),
        ("brazo-y-arana-antivibracion/", "Brazo y araña"),
        ("quienes-somos/", "Quiénes somos"),
    ]),
]

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<rect width="64" height="64" fill="#0D0D0D"/>'
           '<rect x="26" y="14" width="12" height="22" rx="6" fill="#FF4F00"/>'
           '<path d="M20 32a12 12 0 0 0 24 0" stroke="#FF4F00" stroke-width="4" '
           'fill="none" stroke-linecap="round"/>'
           '<path d="M32 44v7" stroke="#FF4F00" stroke-width="4" '
           'stroke-linecap="round"/></svg>')

MONTHS = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
          "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def url(slug):
    return BASE + "/" + slug if slug else BASE + "/"


def rel(slug):
    """Prefijo relativo desde una pagina en `slug` hasta la raiz."""
    depth = slug.count("/") if slug else 0
    return "../" * depth if depth else ""


def human_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return "%d de %s de %d" % (d, MONTHS[m - 1], y)


def nav_html(current, absolute=False):
    out = []
    for slug, label in NAV:
        href = url(slug) if absolute else (rel(current) + slug)
        cur = ' aria-current="page"' if (not absolute and slug == current) else ""
        out.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    return "\n".join(out)


def footer_html(root):
    cols = []
    for title, links in FOOTER_COLS:
        items = "".join('<li><a href="%s%s">%s</a></li>' % (root, s, l)
                        for s, l in links)
        cols.append("<div><h4>%s</h4><ul>%s</ul></div>" % (title, items))
    return "".join(cols)


def breadcrumb(page, current):
    if not current:
        return ""
    return ('<nav class="crumb" aria-label="Ruta"><a href="%s">Inicio</a>'
            '<span class="sep">/</span><span>%s</span></nav>'
            % (rel(current), page["crumb"]))


def toc_html(page):
    if not page.get("toc"):
        return ""
    items = "\n".join('<li><a href="#%s">%s</a></li>' % (i, t) for i, t in page["toc"])
    return ('<aside class="rail"><p class="rail-title">En esta guía</p>'
            '<ol>%s</ol></aside>' % items)


def enhance(body):
    """Envuelve las tablas para que se desplacen en movil sin romper el
    ancho de lectura. Nada mas: el resto del estilo lo pone el CSS."""
    body = body.replace("<table>",
                        '<div class="table-wrap"><div class="table-scroll"><table>')
    body = body.replace("</table>", "</table></div></div>")
    return body


def eyebrow_for(page, slug):
    """Antetitulo del hero.

    No repite la miga de pan: dice que TIPO de pagina es. Las paginas que
    no son ni guia ni ficha se quedan sin el, que es mejor que rellenar.
    """
    if not slug:
        return "Guía independiente &middot; %s" % TODAY[:4]
    return page.get("kind") or ("Guía" if page.get("article") else "")


def display_h1(text):
    """Cursiva editorial en el titular.

    Casi todos los H1 del sitio tienen la forma "Tema: matiz". Poner en
    cursiva lo que va tras los dos puntos da caracter sin tener que
    marcarlo a mano pagina por pagina.
    """
    if ": " in text:
        head, tail = text.split(": ", 1)
        return "%s: <em>%s</em>" % (head, tail)
    return text


def jsonld(page, slug):
    graph = [
        {
            "@type": "WebSite",
            "@id": BASE + "/#website",
            "url": BASE + "/",
            "name": SITE["name"],
            "inLanguage": "es",
            "publisher": {"@id": BASE + "/#org"},
        },
        {
            "@type": "Organization",
            "@id": BASE + "/#org",
            "name": SITE["name"],
            "url": BASE + "/",
            "description": SITE["desc"],
        },
        {
            "@type": "WebPage",
            "@id": url(slug) + "#webpage",
            "url": url(slug),
            "name": page["title"],
            "description": page["desc"],
            "inLanguage": "es",
            "isPartOf": {"@id": BASE + "/#website"},
            "dateModified": TODAY,
        },
    ]
    if page.get("article"):
        graph.append({
            "@type": "Article",
            "@id": url(slug) + "#article",
            "headline": page["h1"],
            "description": page["desc"],
            "inLanguage": "es",
            "datePublished": SITE["published"],
            "dateModified": TODAY,
            "author": {"@id": BASE + "/#org"},
            "publisher": {"@id": BASE + "/#org"},
            "mainEntityOfPage": {"@id": url(slug) + "#webpage"},
        })
    if page.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "@id": url(slug) + "#faq",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in page["faq"]
            ],
        })
    if slug:
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE + "/"},
                {"@type": "ListItem", "position": 2, "name": page["crumb"],
                 "item": url(slug)},
            ],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False)


def faq_html(page):
    if not page.get("faq"):
        return ""
    blocks = "\n".join(
        "<details><summary>%s</summary><p>%s</p></details>" % (q, a)
        for q, a in page["faq"])
    return '<h2 id="faq">Preguntas frecuentes</h2>\n' + blocks


# Evita el parpadeo de tema: se aplica antes de pintar.
THEME_BOOT = ('<script>try{var t=localStorage.getItem("ms-theme");'
              'if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>')

TPL = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta property="og:type" content="{ogtype}">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{sitename}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0D0D0D" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{root}assets/style.css">
{boot}
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>

<header class="site">
  <div class="wrap bar">
    <a class="brand" href="{root}">Micros<em>Streaming</em></a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle" hidden>
    <label class="burger" for="nav-toggle">Menú</label>
    <nav class="main" aria-label="Principal">{nav}</nav>
    <button class="theme-btn" type="button">Tema</button>
  </div>
</header>

<section class="hero">
  <div class="wrap">
    {crumb}
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <ul class="meta">
      <li>Actualizado <b>{updated_h}</b></li>
      <li>Guía independiente</li>
      <li>Sin enlaces patrocinados</li>
    </ul>
  </div>
</section>

<main id="contenido">
  <div class="wrap layout">
    <article class="prose">
      {body}
      {faq}
      <div class="disc">Sitio informativo e independiente. No vendemos micrófonos ni recibimos pago por recomendar marcas. Los precios citados son rangos orientativos y cambian según tienda, país e importación: confirma siempre el precio en el comercio antes de comprar.</div>
    </article>
    {toc}
  </div>
</main>

<footer class="site">
  <div class="wrap">
    <div class="cols">
      <div class="about">
        <a class="brand" href="{root}">Micros<em>Streaming</em></a>
        <p>Guías de micrófonos para streaming, podcast y locución. Escritas para que decidas tú, no para que compres más.</p>
      </div>
      {footer_cols}
    </div>
    <div class="legal">
      <span>&copy; {year} {sitename}</span>
      <span>HTML estático. Sin rastreadores.</span>
    </div>
  </div>
</footer>

<script src="{root}assets/app.js" defer></script>
</body>
</html>
"""


def render(page, slug, absolute_nav=False):
    root = (BASE + "/") if absolute_nav else (rel(slug) or "./")
    return TPL.format(
        title=page["title"], desc=page["desc"], canonical=url(slug),
        ogtype="article" if page.get("article") else "website",
        sitename=SITE["name"], root=root,
        nav=nav_html(slug, absolute=absolute_nav),
        crumb="" if absolute_nav else breadcrumb(page, slug),
        eyebrow=eyebrow_for(page, slug),
        h1=display_h1(page["h1"]), lede=page["lede"],
        toc="" if absolute_nav else toc_html(page),
        body=enhance(page["body"]), faq=faq_html(page),
        jsonld=jsonld(page, slug), updated_h=human_date(TODAY),
        boot=THEME_BOOT,
        footer_cols=footer_html(root), year=TODAY[:4],
    )


def build():
    root_dir = os.path.dirname(os.path.abspath(__file__))

    for slug, page in PAGES.items():
        out_dir = os.path.join(root_dir, *[p for p in slug.split("/") if p])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(render(page, slug))

    # 404: GitHub Pages la sirve en cualquier ruta, asi que todo va absoluto.
    html404 = render(NOT_FOUND, "", absolute_nav=True).replace(
        'content="index,follow', 'content="noindex,follow')
    with open(os.path.join(root_dir, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(html404)

    assets = os.path.join(root_dir, "assets")
    os.makedirs(assets, exist_ok=True)
    with open(os.path.join(assets, "favicon.svg"), "w", encoding="utf-8") as fh:
        fh.write(FAVICON)

    urls = "".join(
        "<url><loc>%s</loc><lastmod>%s</lastmod><changefreq>weekly</changefreq>"
        "<priority>%s</priority></url>" % (url(s), TODAY, "1.0" if not s else "0.8")
        for s in PAGES)
    with open(os.path.join(root_dir, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                 + urls + "</urlset>")

    with open(os.path.join(root_dir, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)

    with open(os.path.join(root_dir, ".nojekyll"), "w", encoding="utf-8") as fh:
        fh.write("")

    print("Generadas %d paginas + 404 + sitemap + robots" % len(PAGES))


if __name__ == "__main__":
    build()
