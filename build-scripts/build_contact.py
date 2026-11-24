# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

def content():
    key = (C.WEB3FORMS_ACCESS_KEY or "").strip()
    email = f'<p style="text-align:center;margin-top:22px"><a class="btn btn-ghost" href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>'
    if not key:
        return f"""<section class="sec"><div class="wrap">
  <div class="sec-head"><h1{CC.A(C.CTA_TITLE)}>{CC._esc(C.CTA_TITLE)}</h1>
  <p class="lead"{CC.A(C.CTA_SUB)}>{CC._esc(C.CTA_SUB)}</p></div>
  {email}
</div></section>"""
    form = f"""<div class="form-panel" style="max-width:640px;margin:0 auto">
  <form action="https://api.web3forms.com/submit" method="POST">
    <input type="hidden" name="access_key" value="{key}">
    <input type="hidden" name="subject" value="New PROmote Style inquiry">
    <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">
    <div class="field"><label for="name"{CC.A("Name")}>Name</label><input id="name" name="name" type="text" required></div>
    <div class="field"><label for="business"{CC.A("Business name")}>Business name</label><input id="business" name="business" type="text"></div>
    <div class="field"><label for="email"{CC.A("Email")}>Email</label><input id="email" name="email" type="email" required></div>
    <div class="field"><label for="message"{CC.A("What would you like your Bot Office to help with?")}>What would you like your Bot Office to help with?</label><textarea id="message" name="message" required></textarea></div>
    <button class="btn btn-primary" type="submit" style="width:100%;justify-content:center"{CC.A("Send")}>Send</button>
    <p class="form-note"{CC.A("We reply personally.")}>We reply personally.</p>
  </form>
</div>"""
    return f"""<section class="sec"><div class="wrap">
  <div class="sec-head"><h1{CC.A(C.CTA_TITLE)}>{CC._esc(C.CTA_TITLE)}</h1>
  <p class="lead"{CC.A(C.CTA_SUB)}>{CC._esc(C.CTA_SUB)}</p></div>
  {form}
  {email}
</div></section>"""

def build():
    html = (
        S.head(C.CONTACT_TITLE, C.CONTACT_DESC, "contact.html")
        + S.nav("contact.html")
        + content()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("contact.html", html)

if __name__ == "__main__":
    build()
