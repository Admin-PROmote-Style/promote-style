# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S

def hero():
    order_btn = '<a class="btn btn-primary" href="seo-basics.html">Start Learning — Free</a>'
    port_btn = '<a class="btn btn-ghost" href="built-seo-ready.html">See a Real SEO-Ready Site</a>'
    return f"""<section class="hero"><div class="wrap">
  <span class="badge-pill">{C.HERO_BADGE}</span>
  <h1>{C.HERO_H1}</h1>
  <p class="lead">{C.HERO_SUB}</p>
  <div class="hero-btns">{order_btn}{port_btn}</div>
</div></section>"""

def trust():
    items = "".join(
        f'<div class="trust-item"><div class="num">{a}</div><div class="lbl">{b}</div></div>'
        for a, b in C.TRUST_ITEMS)
    return f'<section class="trust"><div class="wrap">{items}</div></section>'

def pillars():
    cards = "".join(
        f'<a class="card" href="{p["href"]}"><div class="ic">{p["label"]}</div>'
        f'<h3>{p["title"]}</h3><p>{p["desc"]}</p></a>'
        for p in C.PILLARS)
    return f"""<section class="sec" id="pillars"><div class="wrap">
  <div class="sec-head"><span class="sec-tag">{C.PILLARS_TAG}</span><h2>{C.PILLARS_H2}</h2>
  <p class="lead">{C.PILLARS_SUB}</p></div>
  <div class="cards">{cards}</div>
</div></section>"""

def process():
    steps = "".join(
        f'<div class="process-step"><div class="step-num">{n}</div><h3>{t}</h3><p>{d}</p></div>'
        for n, t, d in C.PROCESS_STEPS)
    return f"""<section class="sec" id="process" style="background:var(--panel);border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)"><div class="wrap">
  <div class="sec-head"><span class="sec-tag">HOW TO USE THIS SITE</span><h2>From "what's SEO?" to actually showing up</h2>
  <p class="lead">A simple order to work through the free content in, whether you're starting from zero or just filling gaps.</p></div>
  <div class="process">{steps}</div>
</div></section>"""

def comparison():
    cards = "".join(
        f'<div class="card{" us" if p["featured"] else ""}"><div class="ic">{p["label"]}</div>'
        f'<h3>{p["title"]}</h3><p>{p["desc"]}</p></div>'
        for p in C.COMPARISON_ITEMS)
    return f"""<section class="sec" id="difference"><div class="wrap">
  <div class="sec-head"><span class="sec-tag">{C.COMPARISON_TAG}</span>
  <h2>{C.COMPARISON_H2}</h2>
  <p class="lead">{C.COMPARISON_SUB}</p></div>
  <div class="cards">{cards}</div>
</div></section>"""

def features():
    cards = "".join(
        f'<div class="card"><div class="ic">{ic}</div><h3>{t}</h3><p>{d}</p></div>'
        for ic, t, d in C.FEATURES)
    return f"""<section class="sec" id="why"><div class="wrap">
  <div class="sec-head"><span class="sec-tag">WHY IT'S FREE</span><h2>Because a resourceful site builds more trust than a locked one</h2></div>
  <div class="cards">{cards}</div>
</div></section>"""

def cta_band():
    return f"""<section class="cta-band"><div class="wrap">
  <h2>{C.CTA_TITLE}</h2><p>{C.CTA_SUB}</p>
  <a class="btn btn-primary" href="contact.html">Talk to mAIntAIn Style</a>
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
