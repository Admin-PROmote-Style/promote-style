# -*- coding: utf-8 -*-
"""
build_seo_files.py -- generates robots.txt and sitemap.xml from config.py.
Run as part of build_all.py. Never hand-edit the generated files directly --
add pages to config.NAV_LINKS (plus contact.html, always included) and rerun.

2026-08-17 fix: skip external links (e.g. the "mAIntAIn Style" nav entry
pointing at https://maintain.style) when building the sitemap -- the
original version of this script (copied from SITE/build-scripts/) appended
external hrefs straight onto LIVE_URL, producing malformed sitemap entries
like "https://promote.style/https://maintain.style". Confirmed the same bug
is live in mAIntAIn Style's own sitemap.xml today -- worth a fix there too.
"""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S

def build():
    live = C.LIVE_URL.rstrip("/")
    today = datetime.date.today().isoformat()

    pages = [href for href, _ in C.NAV_LINKS if not href.startswith(("http://", "https://"))]
    if "contact.html" not in pages:
        pages.append("contact.html")

    robots = f"""User-agent: *
Allow: /

Sitemap: {live}/sitemap.xml
"""

    urls = []
    for href in pages:
        loc = live + "/" if href == "index.html" else f"{live}/{href}"
        priority = "1.0" if href == "index.html" else "0.7"
        urls.append(
            f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n"
            f"    <priority>{priority}</priority>\n  </url>"
        )
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(urls) + "\n</urlset>\n")

    for name, content in (("robots.txt", robots), ("sitemap.xml", sitemap)):
        root_path = os.path.join(S.ROOT, name)
        site_path = os.path.join(S.ROOT, "site", name)
        os.makedirs(os.path.dirname(site_path), exist_ok=True)
        for p in (root_path, site_path):
            with open(p, "w", encoding="utf-8") as f:
                f.write(content)
        print("written", p)

if __name__ == "__main__":
    build()
