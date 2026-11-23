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
@media(max-width:980px){#advanced .cards.six{grid-template-columns:repeat(2,1fr)}}
@media(max-width:700px){
 #advanced .cards.six{grid-template-columns:1fr}
 #advanced .adv-updates .bot-does{grid-template-columns:1fr}
 #bots .bot-card,#advanced .bot-card{padding:26px 20px 20px}
}
"""

def hero():
    primary = f'<a class="btn btn-primary" href="#packages">{CC._esc(C.HERO_PRIMARY)}</a>'
    secondary = f'<a class="btn btn-ghost" href="#guides">{CC._esc(C.HERO_SECONDARY)}</a>'
    return f"""<section class="hero"><div class="wrap">
  <h1>{CC._esc(C.HERO_H1)}</h1>
  <p class="lead">{CC._esc(C.HERO_SUB)}</p>
  <div class="hero-btns">{primary}{secondary}</div>
</div></section>"""

def benefits():
    cards = "".join(
        f'<div class="card"><h3>{CC._esc(title)}</h3><p>{CC._esc(body)}</p></div>'
        for title, body in C.BENEFITS)
    return f"""<section class="sec" id="benefits"><div class="wrap">
  <div class="cards">{cards}</div>
</div></section>"""

def _bot_cards(bots):
    cards = []
    for b in bots:
        items = "".join(f"<li>{CC._esc(line)}</li>" for line in b["does"])
        intro = f'<p class="bot-intro">{CC._esc(b["intro"])}</p>' if b.get("intro") else ""
        cards.append(
            f'<article class="card bot-card"><h3>{CC._esc(b["name"])}</h3>'
            f'<p class="bot-promise">{CC._esc(b["promise"])}</p>'
            f'{intro}'
            f'<ul class="bot-does">{items}</ul>'
            f'<p class="bot-get"><strong>You get:</strong> {CC._esc(b["you_get"])}</p></article>')
    return "".join(cards)

def bots():
    return f"""<section class="sec" id="bots"><div class="wrap">
  <div class="sec-head"><h2>{CC._esc(C.BOTS_H2)}</h2>
  <p class="lead">{CC._esc(C.BOTS_SUB)}</p></div>
  <div class="cards quad">{_bot_cards(C.BOTS)}</div>
  <p class="bot-close">{CC._esc(C.BOTS_CLOSE)}</p>
</div></section>"""

def advanced():
    updates = "".join(f"<li>{CC._esc(line)}</li>" for line in C.ADV_UPDATES)
    return f"""<section class="sec" id="advanced"><div class="wrap">
  <div class="sec-head"><h2>{CC._esc(C.ADV_H2)}</h2>
  <p class="lead">{CC._esc(C.ADV_SUB)}</p>
  <p class="lead">{CC._esc(C.ADV_INTRO)}</p></div>
  <div class="cards six">{_bot_cards(C.ADV_BOTS)}</div>
  <div class="card adv-updates"><h3>{CC._esc(C.ADV_UPDATES_H)}</h3>
  <p>{CC._esc(C.ADV_UPDATES_P)}</p>
  <ul class="bot-does">{updates}</ul></div>
  <p class="bot-close">{CC._esc(C.ADV_CLOSE)}</p>
  <div class="hero-btns"><a class="btn btn-primary" href="mailto:{C.EMAIL}">{CC._esc(C.ADV_BUTTON)}</a></div>
</div></section>"""

def support():
    items = "".join(f"<li><span>{CC._esc(line)}</span></li>" for line in C.SUPPORT)
    return f"""<section class="sec" id="support"><div class="wrap">
  <div class="sec-head"><h2>{CC._esc(C.SUPPORT_H2)}</h2></div>
  <div class="split-col includes support-list"><ul class="check-list">{items}</ul></div>
</div></section>"""

def steps():
    blocks = "".join(
        f'<div class="process-step"><div class="step-num">{n}</div>'
        f'<h3>{CC._esc(title)}</h3><p>{CC._esc(body)}</p></div>'
        for n, title, body in C.STEPS)
    return f"""<section class="sec" id="how"><div class="wrap">
  <div class="sec-head"><h2>{CC._esc(C.STEPS_H2)}</h2></div>
  <div class="process">{blocks}</div>
</div></section>"""

def tools():
    return f"""<section class="sec" id="tools"><div class="wrap">
  <div class="sec-head" style="max-width:760px"><h2>{CC._esc(C.TOOLS_H2)}</h2>
  <p class="lead">{CC._esc(C.TOOLS_LEAD)}</p></div>
</div></section>"""

def guides():
    cards = "".join(
        f'<a class="card" href="{p["href"]}"><div class="ic"{CC._es_attr(p.get("label_es"))}>{p["label"]}</div>'
        f'<h3{CC._es_attr(p.get("title_es"))}>{p["title"]}</h3>'
        f'<p{CC._es_attr(p.get("desc_es"))}>{p["desc"]}</p></a>'
        for p in C.PILLARS)
    return f"""<section class="sec" id="guides"><div class="wrap">
  <div class="sec-head"><h2>{CC._esc(C.GUIDES_H2)}</h2></div>
  <div class="cards">{cards}</div>
</div></section>"""

def faq():
    items = "".join(
        f"<details><summary>{CC._esc(q)}</summary><p>{CC._esc(a)}</p></details>"
        for q, a in C.FAQ)
    return f"""<section class="sec" id="faq"><div class="wrap">
  <div class="sec-head"><h2>{CC._esc(C.FAQ_H2)}</h2></div>
  <div class="faq">{items}</div>
</div></section>"""

def build():
    html = (
        S.head(C.PAGE_TITLE, C.META_DESC, "index.html")
        + f"<style>{HOME_CSS}</style>"
        + S.nav("index.html")
        + hero()
        + benefits()
        + bots()
        + advanced()
        + P.packages_section("h2")
        + support()
        + steps()
        + tools()
        + guides()
        + faq()
        + P.cta_band()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("index.html", html)

if __name__ == "__main__":
    build()
