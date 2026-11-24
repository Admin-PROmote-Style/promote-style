# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC
import build_pricing as P

HOME_CSS = """
.faq{max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:12px}
.faq details{background:var(--panel);border:1px solid rgba(255,255,255,.08);border-radius:12px;padding:18px 22px}
.faq summary{cursor:pointer;font-weight:700;font-size:17px;color:var(--cream)}
.faq details p{color:var(--cream-muted);margin-top:10px;font-size:15.5px}
.support-list{max-width:760px;margin:0 auto}
#bots .sec-head{max-width:740px}
#advanced .sec-head{max-width:760px}
#advanced .sec-head .lead + .lead{margin-top:14px}
#bots .cards.quad{gap:26px;align-items:stretch}
#advanced .cards.six{grid-template-columns:repeat(3,1fr);gap:22px;align-items:stretch}
#bots .bot-card,#advanced .bot-card{display:flex;flex-direction:column;padding:34px 30px 26px;border:1px solid var(--gold)}
#bots .bot-card h3{font-size:28px;margin-bottom:8px}
#advanced .bot-card h3{font-size:24px;margin-bottom:8px}
#bots .bot-promise,#advanced .bot-promise{color:var(--cream);font-weight:700;font-size:18px;line-height:1.35;margin-bottom:12px}
#bots .bot-intro,#advanced .bot-intro{font-size:15.5px}
#bots .bot-does,#advanced .bot-does{list-style:none;margin:18px 0 0;flex:1}
#bots .bot-does li,#advanced .bot-does li{color:var(--cream-muted);font-size:15px;padding:9px 0;border-top:1px solid rgba(255,255,255,.06);display:flex;gap:10px}
#bots .bot-does li::before,#advanced .bot-does li::before{content:"\\2713";color:var(--gold);font-weight:700;flex:0 0 auto}
#bots .bot-get,#advanced .bot-get{margin-top:22px;padding:14px 16px;border-radius:10px;background:rgba(255,179,71,.10);border:1px solid rgba(255,179,71,.35);color:var(--cream);font-size:15.5px;font-weight:600}
#bots .bot-get strong,#advanced .bot-get strong{color:var(--gold);font-weight:800}
#bots .bot-close,#advanced .bot-close{max-width:720px;margin:36px auto 0;text-align:center;color:var(--cream);font-size:18px;font-weight:600;line-height:1.45}
#advanced .adv-updates{max-width:860px;margin:40px auto 0;padding:32px 34px 16px;border:1px solid var(--gold);text-align:left}
#advanced .adv-updates h3{font-size:26px;margin-bottom:10px}
#advanced .adv-updates > p{font-size:16px;margin-bottom:4px}
#advanced .adv-updates .bot-does{display:grid;grid-template-columns:1fr 1fr;column-gap:28px}
#advanced .hero-btns{margin-top:18px}
.hero .hero-grid{display:grid;grid-template-columns:minmax(0,1fr) 55%;gap:36px;align-items:center}
.hero .hero-copy{text-align:left}
.hero .hero-copy h1,.hero .hero-copy .lead{margin-left:0;margin-right:0;text-align:left}
.hero .hero-copy .hero-btns{justify-content:flex-start}
.hero,.hero-grid{overflow-x:clip}
.hero-art,.hero-art img{display:block;width:100%;max-width:100%;height:auto;margin-left:auto;margin-right:auto}
.hero-art img{-webkit-mask-image:radial-gradient(ellipse 74% 70% at 62% 50%, #000 46%, transparent 78%);mask-image:radial-gradient(ellipse 74% 70% at 62% 50%, #000 46%, transparent 78%)}
@media(max-width:900px){
 .hero .hero-grid{display:block}
 .hero .hero-copy,.hero .hero-copy h1,.hero .hero-copy .lead{text-align:center}
 .hero .hero-copy h1,.hero .hero-copy .lead{margin-left:auto;margin-right:auto}
 .hero .hero-copy .hero-btns{justify-content:center}
 .hero-art{margin-top:32px}
 .hero-art img{border-radius:16px;-webkit-mask-image:none;mask-image:none}
}
@media(max-width:767px){
 .hero-art img{aspect-ratio:4/3}
}
@media(max-width:980px){#advanced .cards.six{grid-template-columns:repeat(2,1fr)}}
@media(max-width:700px){
 #advanced .cards.six{grid-template-columns:1fr}
 #advanced .adv-updates .bot-does{grid-template-columns:1fr}
 #bots .bot-card,#advanced .bot-card{padding:26px 20px 20px}
}
"""

def hero():
    primary = f'<a class="btn btn-primary" href="pricing.html"{CC.A(C.HERO_PRIMARY)}>{CC._esc(C.HERO_PRIMARY)}</a>'
    secondary = f'<a class="btn btn-ghost" href="#guides"{CC.A(C.HERO_SECONDARY)}>{CC._esc(C.HERO_SECONDARY)}</a>'
    alt = "A team of AI bots at their desks handling social posts, reviews, email, and website updates."
    alt_es = "Un equipo de bots de IA en sus escritorios, encargados de publicaciones, reseñas, correo y actualizaciones del sitio."
    art = (f'<picture class="hero-art">'
           f'<source media="(max-width: 767px)" srcset="assets/bot-office-hero-mobile.webp" type="image/webp">'
           f'<source media="(max-width: 767px)" srcset="assets/bot-office-hero-mobile.jpg" type="image/jpeg">'
           f'<source srcset="assets/bot-office-hero.webp" type="image/webp">'
           f'<img src="assets/bot-office-hero.jpg" width="1280" height="720" alt="{CC._esc(alt)}" '
           f'data-es-alt="{CC._esc(alt_es)}" fetchpriority="high"></picture>')
    return f"""<section class="hero"><div class="wrap hero-grid">
  <div class="hero-copy">
  <h1{CC.A(C.HERO_H1)}>{CC._esc(C.HERO_H1)}</h1>
  <p class="lead"{CC.A(C.HERO_SUB)}>{CC._esc(C.HERO_SUB)}</p>
  <div class="hero-btns">{primary}{secondary}</div>
  </div>
  {art}
</div></section>"""

def benefits():
    cards = "".join(
        f'<div class="card"><h3{CC.A(title)}>{CC._esc(title)}</h3><p{CC.A(body)}>{CC._esc(body)}</p></div>'
        for title, body in C.BENEFITS)
    return f"""<section class="sec" id="benefits"><div class="wrap">
  <h2 class="sr-only"{CC.A("Why a Bot Office")}>Why a Bot Office</h2>
  <div class="cards">{cards}</div>
</div></section>"""

def _bot_cards(bots):
    cards = []
    for b in bots:
        items = "".join(f"<li{CC.A(line)}>{CC._esc(line)}</li>" for line in b["does"])
        intro = f'<p class="bot-intro"{CC.A(b["intro"])}>{CC._esc(b["intro"])}</p>' if b.get("intro") else ""
        cards.append(
            f'<article class="card bot-card"><h3{CC.A(b["name"])}>{CC._esc(b["name"])}</h3>'
            f'<p class="bot-promise"{CC.A(b["promise"])}>{CC._esc(b["promise"])}</p>'
            f'{intro}'
            f'<ul class="bot-does">{items}</ul>'
            f'{CC.you_get(b["you_get"])}</article>')
    return "".join(cards)

def bots():
    return f"""<section class="sec" id="bots"><div class="wrap">
  <div class="sec-head"><h2{CC.A(C.BOTS_H2)}>{CC._esc(C.BOTS_H2)}</h2>
  <p class="lead"{CC.A(C.BOTS_SUB)}>{CC._esc(C.BOTS_SUB)}</p></div>
  <div class="cards quad">{_bot_cards(C.BOTS)}</div>
  <p class="bot-close"{CC.A(C.BOTS_CLOSE)}>{CC._esc(C.BOTS_CLOSE)}</p>
</div></section>"""

def advanced():
    updates = "".join(f"<li{CC.A(line)}>{CC._esc(line)}</li>" for line in C.ADV_UPDATES)
    return f"""<section class="sec" id="advanced"><div class="wrap">
  <div class="sec-head"><h2{CC.A(C.ADV_H2)}>{CC._esc(C.ADV_H2)}</h2>
  <p class="lead"{CC.A(C.ADV_SUB)}>{CC._esc(C.ADV_SUB)}</p>
  <p class="lead"{CC.A(C.ADV_INTRO)}>{CC._esc(C.ADV_INTRO)}</p></div>
  <div class="cards six">{_bot_cards(C.ADV_BOTS)}</div>
  <div class="card adv-updates"><h3{CC.A(C.ADV_UPDATES_H)}>{CC._esc(C.ADV_UPDATES_H)}</h3>
  <p{CC.A(C.ADV_UPDATES_P)}>{CC._esc(C.ADV_UPDATES_P)}</p>
  <ul class="bot-does">{updates}</ul></div>
  <p class="bot-close"{CC.A(C.ADV_CLOSE)}>{CC._esc(C.ADV_CLOSE)}</p>
  <div class="hero-btns"><a class="btn btn-primary" href="mailto:{C.EMAIL}"{CC.A(C.ADV_BUTTON)}>{CC._esc(C.ADV_BUTTON)}</a></div>
</div></section>"""

def support():
    items = "".join(f"<li{CC.A(line)}><span>{CC._esc(line)}</span></li>" for line in C.SUPPORT)
    return f"""<section class="sec" id="support"><div class="wrap">
  <div class="sec-head"><h2{CC.A(C.SUPPORT_H2)}>{CC._esc(C.SUPPORT_H2)}</h2></div>
  <div class="split-col includes support-list"><ul class="check-list">{items}</ul></div>
</div></section>"""

def steps():
    blocks = "".join(
        f'<div class="process-step"><div class="step-num">{n}</div>'
        f'<h3{CC.A(title)}>{CC._esc(title)}</h3><p{CC.A(body)}>{CC._esc(body)}</p></div>'
        for n, title, body in C.STEPS)
    return f"""<section class="sec" id="how"><div class="wrap">
  <div class="sec-head"><h2{CC.A(C.STEPS_H2)}>{CC._esc(C.STEPS_H2)}</h2></div>
  <div class="process">{blocks}</div>
</div></section>"""

def tools():
    return f"""<section class="sec" id="tools"><div class="wrap">
  <div class="sec-head" style="max-width:760px"><h2{CC.A(C.TOOLS_H2)}>{CC._esc(C.TOOLS_H2)}</h2>
  <p class="lead"{CC.A(C.TOOLS_LEAD)}>{CC._esc(C.TOOLS_LEAD)}</p></div>
</div></section>"""

def guides():
    cards = "".join(
        f'<a class="card" href="{p["href"]}"><div class="ic"{CC._es_attr(p.get("label_es"))}>{p["label"]}</div>'
        f'<h3{CC._es_attr(p.get("title_es"))}>{p["title"]}</h3>'
        f'<p{CC._es_attr(p.get("desc_es"))}>{p["desc"]}</p></a>'
        for p in C.PILLARS)
    return f"""<section class="sec" id="guides"><div class="wrap">
  <div class="sec-head"><h2{CC.A(C.GUIDES_H2)}>{CC._esc(C.GUIDES_H2)}</h2></div>
  <div class="cards">{cards}</div>
</div></section>"""

def _faq_answer(a):
    import copy_es
    if a.endswith("See our Service Disclaimer for details."):
        html = a.replace(
            "Service Disclaimer",
            '<a href="#disclaimer">Service Disclaimer</a>')
        es = copy_es.ES[a].replace(
            "Descargo de servicio",
            '<a href="#disclaimer">Descargo de servicio</a>')
        return f'<p{CC._es_html_attr(es)}>{html}</p>'
    return f'<p{CC.A(a)}>{CC._esc(a)}</p>'

def faq():
    items = "".join(
        f"<details><summary{CC.A(q)}>{CC._esc(q)}</summary>{_faq_answer(a)}</details>"
        for q, a in C.FAQ)
    return f"""<section class="sec" id="faq"><div class="wrap">
  <div class="sec-head"><h2{CC.A(C.FAQ_H2)}>{CC._esc(C.FAQ_H2)}</h2></div>
  <div class="faq">{items}</div>
</div></section>"""

def pricing_teaser():
    heading = "Simple, one-time pricing"
    text = "Bot Offices start at $500. You own everything. No monthly fees from us."
    return f"""<section class="sec" id="pricing"><div class="wrap">
  <div class="sec-head"><h2{CC.A(heading)}>{CC._esc(heading)}</h2>
  <p class="lead"{CC.A(text)}>{CC._esc(text)}</p></div>
  <div class="hero-btns"><a class="btn btn-primary" href="pricing.html"{CC.A(C.HERO_PRIMARY)}>{CC._esc(C.HERO_PRIMARY)}</a></div>
</div></section>"""

def disclaimer():
    body = "".join(
        f"<p{CC._es_attr(es)}>{CC._esc(en)}</p>"
        for en, es in zip(C.DISCLAIMER, C.DISCLAIMER_ES))
    return f"""<section class="sec" id="disclaimer"><div class="wrap">
  <div class="sec-head"><h2{CC.A("Service Disclaimer")}>Service Disclaimer</h2></div>
  <div class="disclaimer-body">{body}</div>
</div></section>"""

def faq_jsonld():
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in C.FAQ
        ],
    }
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False) + "\n</script>"

def build():
    html = (
        S.head(C.PAGE_TITLE, C.META_DESC, "index.html", extra=faq_jsonld())
        + f"<style>{HOME_CSS}</style>"
        + S.nav("index.html")
        + hero()
        + benefits()
        + bots()
        + advanced()
        + pricing_teaser()
        + support()
        + steps()
        + tools()
        + guides()
        + faq()
        + disclaimer()
        + P.cta_band()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("index.html", html)

if __name__ == "__main__":
    build()
