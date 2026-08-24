# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

def hero():
    return f"""<section class="hero" style="padding:70px 0 30px"><div class="wrap">
  <span class="badge-pill"{CC._es_attr(C.PRICING_HERO_TAG_ES)}>{C.PRICING_HERO_TAG}</span>
  <h1 style="font-size:clamp(30px,4.6vw,46px)"{CC._es_html_attr(C.PRICING_HERO_H1_ES)}>{C.PRICING_HERO_H1}</h1>
</div></section>"""

def plans():
    cards = []
    for p in C.PLANS:
        cls = "plan-card featured" if p["featured"] else "plan-card"
        feats = "".join(f'<li>{f}</li>' for f in p["features"])
        price_html = (f'<div class="plan-price">{p["price"]}<span>{p["period"]}</span></div>'
                      if p.get("price") else "")
        cards.append(f"""<div class="{cls}">
  <div class="plan-tag">{p['tag']}</div>
  <h3>{p['name']}</h3>
  {price_html}
  <ul class="plan-features">{feats}</ul>
  <a class="btn {'btn-primary' if p['featured'] else 'btn-ghost'}" href="contact.html" data-es="Empezar">Get started</a>
</div>""")
    cards_html = "".join(cards)
    return f"""<section class="sec"><div class="wrap">
  <div class="plans-grid">{cards_html}</div>
  <p class="plans-intro"{CC._es_attr(C.PLANS_INTRO_ES)}>{C.PLANS_INTRO}</p>
</div></section>"""

def included():
    items = "".join(
        f'<li><div><strong{CC._es_attr(te)}>{t}</strong><span{CC._es_attr(de)}>{d}</span></div></li>'
        for (t, d), (te, de) in zip(C.INCLUDED_ITEMS, C.INCLUDED_ITEMS_ES))
    return f"""<section class="sec" style="background:var(--panel);border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{CC._es_attr(C.INCLUDED_TAG_ES)}>{C.INCLUDED_TAG}</span>
  <h2{CC._es_attr(C.INCLUDED_H2_ES)}>{C.INCLUDED_H2}</h2></div>
  <div class="split-grid" style="grid-template-columns:1fr;max-width:760px">
    <div class="split-col includes"><ul class="check-list">{items}</ul></div>
  </div>
</div></section>"""

def addons():
    cards = []
    for a, ae in zip(C.ADDONS, C.ADDONS_ES):
        cards.append(f"""<div class="addon-card">
  <h4{CC._es_attr(ae['name'])}>{a['name']}</h4>
  <div class="addon-price"{CC._es_attr(ae.get('price_es', ''))}>{a['price']}</div>
  <p{CC._es_attr(ae['desc'])}>{a['desc']}</p>
</div>""")
    cards_html = "".join(cards)
    return f"""<section class="sec"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{CC._es_attr(C.ADDONS_TAG_ES)}>{C.ADDONS_TAG}</span>
  <h2{CC._es_attr(C.ADDONS_H2_ES)}>{C.ADDONS_H2}</h2>
  <p class="lead"{CC._es_attr(C.ADDONS_SUB_ES)}>{C.ADDONS_SUB}</p></div>
  <div class="addon-grid">{cards_html}</div>
  <p class="hosting-note" data-es="Los materiales impresos se cotizan con un precio exacto antes de comenzar el trabajo; los demás complementos se facturan al precio indicado.">Print & in-store materials are quoted exactly before work begins; every other add-on is billed at the price shown.</p>
</div></section>"""

def cta_band():
    return f"""<section class="cta-band"><div class="wrap">
  <h2{CC._es_attr(C.PRICING_CTA_H2_ES)}>{C.PRICING_CTA_H2}</h2>
  <p{CC._es_attr(C.PRICING_CTA_SUB_ES)}>{C.PRICING_CTA_SUB}</p>
  <a class="btn btn-primary" href="contact.html" data-es="Iniciar un proyecto">Start a Project</a>
</div></section>"""

def build():
    title = f"Pricing — {C.BUSINESS_NAME}"
    desc = "PROmote Style monthly marketing management pricing: Starter $1,000/mo, Growth $2,000/mo, Full-Service $3,000/mo. Flat fee, no percentage of ad spend."
    html = (
        S.head(title, desc, "pricing.html")
        + S.nav("pricing.html")
        + hero()
        + plans()
        + included()
        + addons()
        + cta_band()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("pricing.html", html)

if __name__ == "__main__":
    build()
