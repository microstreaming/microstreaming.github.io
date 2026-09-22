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

import content_modelos
from content import NOT_FOUND, PAGES, SITE

# Las fichas por modelo viven en su propio modulo para no inflar content.py.
content_modelos.add_pages(PAGES, SITE)

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
        ("quienes-somos/", "Quiénes somos"),
    ]),
]

# --- Iconos en linea (sin peticiones extra) -------------------------------
ICON_MIC = ('<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" '
            'stroke-linecap="round" aria-hidden="true">'
            '<rect x="9" y="2" width="6" height="11" rx="3"/>'
            '<path d="M5 11a7 7 0 0 0 14 0"/><path d="M12 18v3"/></svg>')
ICON_SUN = ('<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
            '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2'
            'M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>')
ICON_MOON = ('<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
             'aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>')
ICON_BURGER = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
               'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
               '<path d="M4 7h16M4 12h16M4 17h16"/></svg>')
ICON_ARROW = ('<svg class="arrow" width="15" height="15" viewBox="0 0 24 24" fill="none" '
              'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
              'stroke-linejoin="round" aria-hidden="true">'
              '<path d="M7 17L17 7M9 7h8v8"/></svg>')

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
           '<stop offset="0" stop-color="#ff6a2b"/><stop offset="1" stop-color="#2ad4ee"/>'
           '</linearGradient></defs>'
           '<rect width="64" height="64" rx="14" fill="#06080c"/>'
           '<rect x="25" y="13" width="14" height="24" rx="7" fill="url(#g)"/>'
           '<path d="M19 31a13 13 0 0 0 26 0" stroke="url(#g)" stroke-width="4.5" '
           'fill="none" stroke-linecap="round"/>'
           '<path d="M32 44v7" stroke="url(#g)" stroke-width="4.5" stroke-linecap="round"/>'
           '</svg>')

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
    """Retoques de marcado sobre el HTML de contenido.

    - Envuelve cada tabla para que pueda desplazarse en movil sin romper
      el ancho de lectura.
    - Anade la flecha de las tarjetas enlazadas.
    """
    body = re.sub(r"<table>", '<div class="table-wrap"><div class="table-scroll"><table>',
                  body)
    body = re.sub(r"</table>", "</table></div></div>", body)
    body = body.replace('<a class="tile" href=', '<a class="tile" data-tile href=')
    body = re.sub(r'(<a class="tile" data-tile href="[^"]*">)',
                  r"\1" + ICON_ARROW, body)
    body = body.replace(' data-tile', '')
    return body


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
<meta name="theme-color" content="#06080c" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#fbfcfe" media="(prefers-color-scheme: light)">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap">
<link rel="stylesheet" href="{root}assets/style.css">
{boot}
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<div class="progress" aria-hidden="true"></div>
<a class="skip" href="#contenido">Saltar al contenido</a>

<header class="site">
  <div class="wrap bar">
    <a class="brand" href="{root}">
      <span class="mark">{icon_mic}</span>Micros<em>Streaming</em>
    </a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle" hidden>
    <label class="burger" for="nav-toggle" aria-label="Abrir menú">{icon_burger}</label>
    <nav class="main" aria-label="Principal">{nav}</nav>
    <button class="theme-btn" type="button" aria-label="Cambiar tema">{icon_sun}{icon_moon}</button>
  </div>
</header>

<section class="hero">
  <div class="wrap">
    {crumb}
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <ul class="meta">
      <li><span class="dot"></span>Actualizado el {updated_h}</li>
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
        <a class="brand" href="{root}"><span class="mark">{icon_mic}</span>Micros<em>Streaming</em></a>
        <p>Guías de micrófonos para streaming, podcast y locución. Escritas para que decidas tú, no para que compres más.</p>
      </div>
      {footer_cols}
    </div>
    <div class="legal">
      <span>&copy; {year} {sitename}</span>
      <span>Hecho con HTML estático. Sin rastreadores.</span>
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
        h1=page["h1"], lede=page["lede"],
        toc="" if absolute_nav else toc_html(page),
        body=enhance(page["body"]), faq=faq_html(page),
        jsonld=jsonld(page, slug), updated_h=human_date(TODAY),
        boot=THEME_BOOT, icon_mic=ICON_MIC, icon_sun=ICON_SUN,
        icon_moon=ICON_MOON, icon_burger=ICON_BURGER,
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
