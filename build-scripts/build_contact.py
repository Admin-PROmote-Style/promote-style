# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S

def content():
    key = C.WEB3FORMS_ACCESS_KEY
    form = f"""<div class="form-panel">
  <form action="https://api.web3forms.com/submit" method="POST">
    <input type="hidden" name="access_key" value="{key}">
    <input type="hidden" name="subject" value="New inquiry — PROmote Style">
    <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">
    <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" required></div>
    <div class="field"><label for="business">Business name</label><input id="business" name="business" type="text"></div>
    <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required></div>
    <div class="field"><label for="message">What do you need?</label><textarea id="message" name="message" required placeholder="A site built SEO-ready, help with marketing, or just a question about one of the guides — tell us what's going on."></textarea></div>
    <button class="btn btn-primary" type="submit" style="width:100%;justify-content:center">Send</button>
    <p class="form-note">We reply personally — no auto-responders, no sales queue.</p>
  </form>
</div>"""
    side = f"""<div class="contact-side">
  <h3>Prefer email?</h3>
  <p>Send details straight to us and we'll get back to you.</p>
  <a class="email" href="mailto:{C.EMAIL}">{C.EMAIL}</a>
  <h3 style="margin-top:32px">Based in {C.CITY_STATE}</h3>
  <p>Working with local and remote clients — everything is handled online.</p>
  <h3 style="margin-top:32px">Just want the site?</h3>
  <p>mAIntAIn Style builds sites SEO-ready from day one — <a href="https://maintain.style" style="color:var(--gold);font-weight:700">see their work directly</a>.</p>
</div>"""
    return f"""<section class="sec"><div class="wrap">
  <div class="sec-head" style="margin-bottom:50px"><span class="sec-tag">CONTACT</span><h2>{C.CONTACT_H1}</h2>
  <p class="lead">{C.CONTACT_SUB}</p></div>
  <div class="contact-grid">{form}{side}</div>
</div></section>"""

def build():
    title = f"Contact — {C.BUSINESS_NAME}"
    desc = "Get a site built SEO-ready from day one, or let PROmote Style run your marketing for you."
    html = (
        S.head(title, desc, "contact.html")
        + S.nav("contact.html")
        + content()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("contact.html", html)

if __name__ == "__main__":
    build()
