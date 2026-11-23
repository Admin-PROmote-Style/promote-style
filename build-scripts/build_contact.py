# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

def content():
    return f"""<section class="sec"><div class="wrap">
  <div class="sec-head" style="margin-bottom:28px"><h1>{CC._esc(C.CTA_TITLE)}</h1>
  <p class="lead">{CC._esc(C.CTA_SUB)}</p></div>
  <p style="text-align:center"><a class="btn btn-primary" href="mailto:{C.EMAIL}">{CC._esc(C.CTA_BUTTON)}</a></p>
</div></section>"""

def build():
    html = (
        S.head(C.PAGE_TITLE, C.META_DESC, "contact.html")
        + S.nav("contact.html")
        + content()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("contact.html", html)

if __name__ == "__main__":
    build()
