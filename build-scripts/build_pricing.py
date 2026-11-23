# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

def plan_grid():
    cards = []
    for p in C.PLANS:
        cls = "plan-card featured" if p["featured"] else "plan-card"
        tag = f'<div class="plan-tag">{CC._esc(p["tag"])}</div>' if p.get("tag") else ""
        feats = "".join(f"<li>{CC._esc(f)}</li>" for f in p["features"])
        cards.append(f"""<div class="{cls}">
  {tag}
  <h3>{CC._esc(p["name"])}</h3>
  <div class="plan-price">{CC._esc(p["price"])}</div>
  <ul class="plan-features">{feats}</ul>
</div>""")
    return f'<div class="plans-grid plans-4">{"".join(cards)}</div>'

def packages_section(heading="h2"):
    return f"""<section class="sec" id="packages"><div class="wrap">
  <div class="sec-head"><{heading}>{CC._esc(C.PACKAGES_H2)}</{heading}>
  <p class="lead">{CC._esc(C.PACKAGES_SUB)}</p></div>
  {plan_grid()}
  <p class="plans-intro">{CC._esc(C.PACKAGES_NOTE)}</p>
</div></section>"""

def cta_band():
    return f"""<section class="cta-band"><div class="wrap">
  <h2>{CC._esc(C.CTA_TITLE)}</h2>
  <p>{CC._esc(C.CTA_SUB)}</p>
  <div class="hero-btns"><a class="btn btn-primary" href="mailto:{C.EMAIL}">{CC._esc(C.CTA_BUTTON)}</a></div>
</div></section>"""

def build():
    html = (
        S.head(C.PAGE_TITLE, C.META_DESC, "pricing.html")
        + S.nav("pricing.html")
        + packages_section("h1")
        + cta_band()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("pricing.html", html)

if __name__ == "__main__":
    build()
