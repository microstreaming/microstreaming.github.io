# -*- coding: utf-8 -*-
"""Generador estatico del sitio Micros Streaming.

Uso: python build.py   (escribe los index.html en la raiz del repo)
"""
import json
import os

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


def url(slug):
    return BASE + "/" + slug if slug else BASE + "/"


def rel(slug):
    """Prefijo relativo desde una pagina en `slug` hasta la raiz."""
    depth = slug.count("/") if slug else 0
    return "../" * depth if depth else ""


def nav_html(current):
    out = []
    for slug, label in NAV:
        cur = ' aria-current="page"' if slug == current else ""
        out.append('<a href="%s%s"%s>%s</a>' % (rel(current), slug, cur, label))
    return "\n".join(out)


def breadcrumb(page, current):
    if not current:
        return ""
    return ('<div class="crumb"><a href="%s">Inicio</a> &rsaquo; <span>%s</span></div>'
            % (rel(current), page["crumb"]))


def toc_html(page):
    if not page.get("toc"):
        return ""
    items = "\n".join('<li><a href="#%s">%s</a></li>' % (i, t) for i, t in page["toc"])
    return '<nav class="toc"><strong>En esta guía</strong><ol>%s</ol></nav>' % items


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
                {"@type": "ListItem", "position": 2, "name": page["crumb"], "item": url(slug)},
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
<meta name="theme-color" content="#0f1115">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{root}assets/style.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<header class="site">
  <div class="wrap">
    <a class="brand" href="{root}">&#127908; Micros<span>Streaming</span></a>
    <nav class="main">{nav}</nav>
  </div>
</header>
<div class="wrap">{crumb}</div>
<div class="hero">
  <div class="wrap">
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <p class="meta">Actualizado el {updated_h} &middot; Gu&iacute;a independiente &middot; Sin enlaces patrocinados</p>
  </div>
</div>
<main>
  <div class="wrap">
    {toc}
    {body}
    {faq}
    <div class="disc">Sitio informativo e independiente. No vendemos micr&oacute;fonos ni recibimos pago por recomendar marcas. Los precios citados son rangos orientativos y cambian seg&uacute;n tienda, pa&iacute;s e importaci&oacute;n: confirma siempre el precio en el comercio antes de comprar.</div>
  </div>
</main>
<footer class="site">
  <div class="wrap cols">
    <div><strong>{sitename}</strong><br>Gu&iacute;as de micr&oacute;fonos para streaming, podcast y locuci&oacute;n.</div>
    <div>
      <a href="{root}">Inicio</a> &middot;
      <a href="{root}mejores-micros-streaming/">Mejores micros</a> &middot;
      <a href="{root}usb-o-xlr/">USB o XLR</a> &middot;
      <a href="{root}quienes-somos/">Qui&eacute;nes somos</a>
    </div>
  </div>
</footer>
</body>
</html>
"""

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<rect width="64" height="64" rx="14" fill="#0f1115"/>'
           '<rect x="24" y="12" width="16" height="26" rx="8" fill="#ff6b35"/>'
           '<path d="M18 32a14 14 0 0 0 28 0" stroke="#ff6b35" stroke-width="4" '
           'fill="none" stroke-linecap="round"/>'
           '<path d="M32 46v8M24 54h16" stroke="#ff6b35" stroke-width="4" '
           'stroke-linecap="round"/></svg>')

MONTHS = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
          "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def human_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return "%d de %s de %d" % (d, MONTHS[m - 1], y)


def build():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    written = []
    for slug, page in PAGES.items():
        html = TPL.format(
            title=page["title"], desc=page["desc"], canonical=url(slug),
            ogtype="article" if page.get("article") else "website",
            sitename=SITE["name"], root=rel(slug) or "./",
            nav=nav_html(slug), crumb=breadcrumb(page, slug),
            h1=page["h1"], lede=page["lede"], toc=toc_html(page),
            body=page["body"], faq=faq_html(page),
            jsonld=jsonld(page, slug), updated_h=human_date(TODAY),
        )
        out_dir = os.path.join(root_dir, *[p for p in slug.split("/") if p])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(html)
        written.append(slug)

    assets = os.path.join(root_dir, "assets")
    os.makedirs(assets, exist_ok=True)
    with open(os.path.join(assets, "favicon.svg"), "w", encoding="utf-8") as fh:
        fh.write(FAVICON)

    # 404 personalizada (GitHub Pages la sirve desde la raiz del sitio).
    # Usa URLs absolutas porque puede mostrarse en cualquier ruta.
    nf = NOT_FOUND
    html404 = TPL.format(
        title=nf["title"], desc=nf["desc"], canonical=BASE + "/",
        ogtype="website", sitename=SITE["name"], root=BASE + "/",
        nav="\n".join('<a href="%s">%s</a>' % (url(s), l) for s, l in NAV),
        crumb="", h1=nf["h1"], lede=nf["lede"], toc="",
        body=nf["body"], faq="", jsonld=jsonld(nf, ""),
        updated_h=human_date(TODAY),
    ).replace('content="index,follow', 'content="noindex,follow')
    with open(os.path.join(root_dir, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(html404)

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

    print("Generadas %d paginas + sitemap + robots" % len(written))
    for s in written:
        print("  ", url(s))


if __name__ == "__main__":
    build()
