# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

def hero():
    order_btn = ('<a class="btn btn-primary" href="seo-101.html" data-es="Empieza a Aprender — Gratis">'
                 'Start Learning — Free</a>')
    # 2026-08-17: was "See a Real SEO-Ready Site" linking to the internal
    # proof page -- George's call: don't promise "see" a site without
    # showing one. Points straight at maintain.style now, which lets that
    # site finish the sale directly instead of routing through this one's
    # contact form.
    port_btn = ('<a class="btn btn-ghost" href="https://maintain.style" '
                'data-es="Construye un Sitio Real Listo para SEO">Build a Real SEO-Ready Site</a>')
    return f"""<section class="hero"><div class="wrap">
  <span class="badge-pill"{CC._es_attr(C.HERO_BADGE_ES)}>{C.HERO_BADGE}</span>
  <h1{CC._es_html_attr(C.HERO_H1_ES)}>{C.HERO_H1}</h1>
  <p class="lead"{CC._es_attr(C.HERO_SUB_ES)}>{C.HERO_SUB}</p>
  <div class="hero-btns">{order_btn}{port_btn}</div>
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
    tag_attr = CC._es_attr("CÓMO USAR ESTE SITIO")
    h2_attr = CC._es_html_attr('De "¿qué es el SEO?" a de verdad aparecer en los resultados de búsqueda')
    lead_attr = CC._es_attr("Un orden simple para trabajar el contenido gratuito, sea que empieces desde cero o solo estés llenando huecos.")
    return f"""<section class="sec" id="process" style="background:var(--panel);border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{tag_attr}>HOW TO USE THIS SITE</span><h2{h2_attr}>From "what's SEO?" to actually showing up in search results</h2>
  <p class="lead"{lead_attr}>A simple order to work through the free content in, whether you're starting from zero or just filling gaps.</p></div>
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
    tag_attr = CC._es_attr("POR QUÉ ES GRATIS")
    h2_attr = CC._es_attr("Porque un sitio con recursos genera más confianza que uno cerrado")
    return f"""<section class="sec" id="why"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{tag_attr}>WHY IT'S FREE</span><h2{h2_attr}>Because a resourceful site builds more trust than a locked one</h2></div>
  <div class="cards">{cards}</div>
</div></section>"""

def cta_band():
    # 2026-08-17: routes straight to maintain.style's portfolio page instead
    # of this site's own contact.html -- George's call: let people actually
    # see the SEO-ready sites mS has built (proof) rather than a generic
    # "talk to us" ask. Was "Talk to mAIntAIn Style" -> maintain.style.
    return f"""<section class="cta-band"><div class="wrap">
  <h2{CC._es_attr(C.CTA_TITLE_ES)}>{C.CTA_TITLE}</h2><p{CC._es_attr(C.CTA_SUB_ES)}>{C.CTA_SUB}</p>
  <a class="btn btn-primary" href="https://maintain.style/portfolio.html" data-es="Ver Sitios Listos para SEO">View SEO-Ready Sites</a>
</div></section>"""

def build():
    title = f"{C.BUSINESS_NAME} — {C.TAGLINE} Free SEO resources for everyone."
    desc = C.HERO_SUB
    html = (
        S.head(title, desc, "index.html")
        + S.nav("index.html")
        + hero()
        + trust()
        + pillars()
        + process()
        + comparison()
        + features()
        + cta_band()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("index.html", html)

if __name__ == "__main__":
    build()
