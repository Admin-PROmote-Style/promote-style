# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

def hero():
    # 2026-08-23: was "Start Learning — Free" (primary) / "Build a Real
    # SEO-Ready Site" -> maintain.style (secondary) -- the whole hero sold
    # the free content library with no mention of PROmote Style's own paid
    # service. Now the primary button sells the service itself; the free
    # guides move to secondary instead of disappearing.
    order_btn = ('<a class="btn btn-primary" href="pricing.html" data-es="Ver Precios">'
                 'See Pricing</a>')
    port_btn = ('<a class="btn btn-ghost" href="seo-101.html" '
                'data-es="Guías SEO Gratis">Free SEO Guides</a>')
    return f"""<section class="hero"><div class="wrap">
  <span class="badge-pill"{CC._es_attr(C.HERO_BADGE_ES)}>{C.HERO_BADGE}</span>
  <h1{CC._es_html_attr(C.HERO_H1_ES)}>{C.HERO_H1}</h1>
  <p class="lead"{CC._es_attr(C.HERO_SUB_ES)}>{C.HERO_SUB}</p>
  <div class="hero-btns">{order_btn}{port_btn}</div>
</div></section>"""

def plans_teaser():
    # 2026-08-23: NEW. Reuses C.PLANS directly (same data driving
    # pricing.html) so this teaser can't drift out of sync with the real
    # page -- it renders name/tag/price and links straight to pricing.html.
    cards = []
    for p in C.PLANS:
        cls = "plan-card featured" if p["featured"] else "plan-card"
        cards.append(f"""<a class="{cls}" href="pricing.html" style="text-decoration:none;display:flex;flex-direction:column">
  <div class="plan-tag">{p['tag']}</div>
  <h3>{p['name']}</h3>
  <div class="plan-price">{p['price']}<span>{p['period']}</span></div>
</a>""")
    cards_html = "".join(cards)
    return f"""<section class="sec" style="background:var(--panel);border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{CC._es_attr(C.PLANS_TEASER_TAG_ES)}>{C.PLANS_TEASER_TAG}</span>
  <h2{CC._es_attr(C.PLANS_TEASER_H2_ES)}>{C.PLANS_TEASER_H2}</h2>
  <p class="lead"{CC._es_attr(C.PLANS_TEASER_SUB_ES)}>{C.PLANS_TEASER_SUB}</p></div>
  <div class="plans-grid">{cards_html}</div>
  <p style="text-align:center;margin-top:24px"><a class="btn btn-ghost" href="pricing.html"{CC._es_attr(C.PLANS_TEASER_CTA_ES)}>{C.PLANS_TEASER_CTA}</a></p>
</div></section>"""

def trust():
    items = "".join(
        f'<div class="trust-item"><div class="num"{CC._es_attr(a_es)}>{a}</div>'
        f'<div class="lbl"{CC._es_attr(b_es)}>{b}</div></div>'
        for a, b, a_es, b_es in C.TRUST_ITEMS)
    return f'<section class="trust"><div class="wrap">{items}</div></section>'

def pillars():
    cards = "".join(
        f'<a class="card" href="{p["href"]}"><div class="ic"{CC._es_attr(p.get("label_es"))}>{p["label"]}</div>'
        f'<h3{CC._es_attr(p.get("title_es"))}>{p["title"]}</h3>'
        f'<p{CC._es_attr(p.get("desc_es"))}>{p["desc"]}</p></a>'
        for p in C.PILLARS)
    return f"""<section class="sec" id="pillars"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{CC._es_attr(C.PILLARS_TAG_ES)}>{C.PILLARS_TAG}</span>
  <h2{CC._es_html_attr(C.PILLARS_H2_ES)}>{C.PILLARS_H2}</h2></div>
  <div class="cards">{cards}</div>
</div></section>"""

def process():
    steps = "".join(
        f'<div class="process-step"><div class="step-num">{n}</div>'
        f'<h3{CC._es_attr(t_es)}>{t}</h3><p{CC._es_attr(d_es)}>{d}</p></div>'
        for n, t, d, t_es, d_es in C.PROCESS_STEPS)
    # 2026-08-23: was "HOW TO USE THIS SITE" / "what's SEO? -> showing up in
    # search results" -- framed around working through the free guides. That
    # framing now lives on seo-101.html itself; this section sells becoming
    # a client instead (see PROCESS_STEPS in config.py).
    tag_attr = CC._es_attr("CÓMO FUNCIONA")
    h2_attr = CC._es_html_attr("De la primera conversación a que tu marketing se maneje solo")
    lead_attr = CC._es_attr("Un camino simple y predecible, ya sea que vengas de hacerlo tú mismo o estés cambiando de agencia.")
    return f"""<section class="sec" id="process" style="background:var(--panel);border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{tag_attr}>HOW IT WORKS</span><h2{h2_attr}>From first conversation to your marketing running itself</h2>
  <p class="lead"{lead_attr}>A simple, predictable path whether you're moving from DIY or switching from an agency.</p></div>
  <div class="process">{steps}</div>
</div></section>"""

def comparison():
    cards = "".join(
        f'<div class="card{" us" if p["featured"] else ""}"><div class="ic"{CC._es_attr(p.get("label_es"))}>{p["label"]}</div>'
        f'<h3{CC._es_attr(p.get("title_es"))}>{p["title"]}</h3>'
        f'<p{CC._es_attr(p.get("desc_es"))}>{p["desc"]}</p></div>'
        for p in C.COMPARISON_ITEMS)
    return f"""<section class="sec" id="difference"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{CC._es_attr(C.COMPARISON_TAG_ES)}>{C.COMPARISON_TAG}</span>
  <h2{CC._es_attr(C.COMPARISON_H2_ES)}>{C.COMPARISON_H2}</h2></div>
  <div class="cards">{cards}</div>
</div></section>"""

def features():
    cards = "".join(
        f'<div class="card"><div class="ic"{CC._es_attr(ic_es)}>{ic}</div>'
        f'<h3{CC._es_attr(t_es)}>{t}</h3><p{CC._es_attr(d_es)}>{d}</p></div>'
        for ic, t, d, ic_es, t_es, d_es in C.FEATURES)
    # 2026-08-23: kept the same three cards (Free/Practical/Proven), just
    # reframed the section header slightly now that it sits below the paid
    # pitch instead of being the whole homepage's premise -- it's supporting
    # proof ("we're confident enough to give real expertise away free"),
    # not the main event.
    tag_attr = CC._es_attr("POR QUÉ LO REGALAMOS")
    h2_attr = CC._es_attr("Porque un negocio que regala experiencia real es uno en el que puedes confiar tu marketing")
    return f"""<section class="sec" id="why"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{tag_attr}>WHY WE GIVE IT AWAY FREE</span><h2{h2_attr}>Because a business that gives away real expertise for free is one you can trust to run your marketing</h2></div>
  <div class="cards">{cards}</div>
</div></section>"""

def cta_band():
    # 2026-08-23: this used to route 100% of homepage traffic to
    # mAIntAIn Style's portfolio with no ask for PROmote Style's own
    # service anywhere on the page ("Talk to mAIntAIn Style" -> maintain.style,
    # then later "View SEO-Ready Sites" -> maintain.style/portfolio.html).
    # Now PROmote Style's own contact form is the primary ask; the
    # mAIntAIn Style cross-sell is kept as a secondary button, not the
    # only one.
    primary = ('<a class="btn btn-primary" href="contact.html" data-es="Iniciar un Proyecto">'
               'Start a Project</a>')
    secondary = ('<a class="btn btn-ghost" href="https://maintain.style" '
                 'data-es="¿También Necesitas un Sitio? Mira mAIntAIn Style">Also Need a Site? See mAIntAIn Style</a>')
    return f"""<section class="cta-band"><div class="wrap">
  <h2{CC._es_attr(C.CTA_TITLE_ES)}>{C.CTA_TITLE}</h2><p{CC._es_attr(C.CTA_SUB_ES)}>{C.CTA_SUB}</p>
  <div class="hero-btns">{primary}{secondary}</div>
</div></section>"""

def build():
    # 2026-08-23: was hero -> trust -> pillars -> process -> comparison ->
    # features -> cta_band, i.e. sell the free content, funnel to
    # mAIntAIn Style. Reordered now that PROmote Style has a real priced
    # product: sell the service and show the price early, free content
    # moves down as supporting proof rather than the main event.
    title = f"{C.BUSINESS_NAME} — {C.TAGLINE} Social media & marketing management, plus free SEO guides."
    desc = C.HERO_SUB
    html = (
        S.head(title, desc, "index.html")
        + S.nav("index.html")
        + hero()
        + plans_teaser()
        + trust()
        + comparison()
        + process()
        + pillars()
        + features()
        + cta_band()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("index.html", html)

if __name__ == "__main__":
    build()
