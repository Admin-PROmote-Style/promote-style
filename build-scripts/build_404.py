# -*- coding: utf-8 -*-
# Real "page not found" page. Cloudflare Pages serves a top-level 404.html with
# a true 404 status for unknown addresses. Without this file Pages falls back to
# the homepage with a 200 for every bad URL (soft 404: bad for search engines).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S


def content():
    return """<section class="sec"><div class="wrap" style="text-align:center;padding:80px 0">
  <span class="sec-tag" data-es="404">404</span>
  <h1 data-es="No encontramos esa p&aacute;gina">We can't find that page</h1>
  <p class="lead" data-es="Puede que el enlace est&eacute; viejo o mal escrito.">The link may be old or mistyped.</p>
  <p style="margin-top:28px"><a class="btn btn-primary" href="/" data-es="Ir al inicio">Go to the homepage</a></p>
</div></section>"""


def build():
    title = "Page not found - " + C.BUSINESS_NAME
    desc = "That page does not exist. Head back to the PROmote Style homepage."
    head = S.head(title, desc, "404.html")
    # never index or canonicalise the error page
    head = head.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex">', 1)
    html = (
        head
        + S.nav("")
        + content()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("404.html", html)


if __name__ == "__main__":
    build()
