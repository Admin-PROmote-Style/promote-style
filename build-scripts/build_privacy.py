# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

def content():
    blocks = [
        ("PROmote Style",
         "A mAIntAIn Style company based in Bend, Oregon. Email: promote@maintain.style."),
        ("Messages you send us",
         "When you email us or use the contact form, we receive your name, business name, email, and message. We use it only to reply about your Bot Office. We do not sell it."),
        ("Your Bot Office accounts",
         "The accounts we help you set up (such as Cursor or X) belong to you and are covered by those companies' own privacy policies."),
    ]
    body = "".join(
        f"<h2{CC.A(h)}>{CC._esc(h)}</h2><p{CC.A(p)}>{CC._esc(p)}</p>"
        for h, p in blocks)
    intro = "What this site collects, and how it is used."
    return f"""<section class="sec"><div class="wrap">
  <div class="sec-head"><h1{CC.A("Privacy")}>Privacy</h1>
  <p class="lead"{CC.A(intro)}>{CC._esc(intro)}</p></div>
  <div class="disclaimer-body">{body}</div>
</div></section>"""

def build():
    html = (
        S.head(C.PRIVACY_TITLE, C.PRIVACY_DESC, "privacy.html")
        + S.nav("privacy.html")
        + content()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("privacy.html", html)

if __name__ == "__main__":
    build()
