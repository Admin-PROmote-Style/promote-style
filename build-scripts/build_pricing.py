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
    # 2026-08-24: added data-es to tag/name/period/features (were English-only
    # before -- see the comment above C.PLANS) and a 3-stat "at a glance"
    # strip per card, sourced from each plan's `glance` list in config.py.
    cards = []
    for p in C.PLANS:
        cls = "plan-card featured" if p["featured"] else "plan-card"
        feats = "".join(
            f'<li{CC._es_attr(fe)}>{f}</li>' for f, fe in zip(p["features"], p.get("features_es", [])))
        price_html = (f'<div class="plan-price">{p["price"]}<span{CC._es_attr(p.get("period_es"))}>{p["period"]}</span></div>'
                      if p.get("price") else "")
        glance_html = "".join(
            f'<div class="glance-item"><span class="num"{CC._es_attr(g.get("val_es"))}>{g["val"]}</span>'
            f'<span class="lbl"{CC._es_attr(g.get("lbl_es"))}>{g["lbl"]}</span></div>'
            for g in p.get("glance", []))
        glance_block = f'<div class="at-a-glance">{glance_html}</div>' if glance_html else ""
        cards.append(f"""<div class="{cls}">
  <div class="plan-tag"{CC._es_attr(p.get('tag_es'))}>{p['tag']}</div>
  <h3{CC._es_attr(p.get('name_es'))}>{p['name']}</h3>
  {price_html}
  {glance_block}
  <ul class="plan-features">{feats}</ul>
  <a class="btn {'btn-primary' if p['featured'] else 'btn-ghost'}" href="contact.html" data-es="Empezar">Get started</a>
</div>""")
    cards_html = "".join(cards)
    return f"""<section class="sec"><div class="wrap">
  <div class="plans-grid">{cards_html}</div>
  <p class="plans-intro"{CC._es_attr(C.PLANS_INTRO_ES)}>{C.PLANS_INTRO}</p>
  {daily_cost()}
</div></section>"""

def daily_cost():
    items = "".join(
        f'<div class="daily-item"><div class="amt">{amt}<span>/day</span></div>'
        f'<div class="lbl"{CC._es_attr(p.get("name_es"))}>{p["name"]}</div></div>'
        for p, amt in zip(C.PLANS, C.DAILY_COST_AMOUNTS))
    return f"""<div class="daily-cost">{items}</div>
  <p class="daily-caption"{CC._es_attr(C.DAILY_COST_CAPTION_ES)}>{C.DAILY_COST_CAPTION}</p>"""

def fit_section():
    def _list(items):
        return "".join(f'<li{CC._es_attr(es)}>{en}</li>' for en, es in items)
    return f"""<section class="sec" style="padding-top:10px"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{CC._es_attr(C.FIT_TAG_ES)}>{C.FIT_TAG}</span>
  <h2{CC._es_attr(C.FIT_H2_ES)}>{C.FIT_H2}</h2></div>
  <div class="fit-grid">
    <div class="fit-card yes">
      <h3><span aria-hidden="true">&#10003;</span> <span{CC._es_attr(C.FIT_YES_LABEL_ES)}>{C.FIT_YES_LABEL}</span></h3>
      <ul class="fit-list">{_list(C.FIT_YES_ITEMS)}</ul>
    </div>
    <div class="fit-card no">
      <h3{CC._es_attr(C.FIT_NO_LABEL_ES)}>{C.FIT_NO_LABEL}</h3>
      <ul class="fit-list">{_list(C.FIT_NO_ITEMS)}</ul>
    </div>
  </div>
  <div class="cmp-linkrow">
    <a class="cmp-link" href="#full-compare"{CC._es_attr(C.COMPARE_LINK_ES)}>{C.COMPARE_LINK} <span class="arrow" aria-hidden="true">&darr;</span></a>
  </div>
</div></section>"""

def full_compare():
    def _cell(v, featured):
        cls = "featured-col" if featured else ""
        if v == "check":
            return f'<td class="check {cls}">&#10003;</td>'
        if v == "dash":
            return f'<td class="dash {cls}">&mdash;</td>'
        en, es = v
        return f'<td class="cmp-val {cls}"{CC._es_attr(es)}>{en}</td>'

    head_cells = []
    for i, p in enumerate(C.PLANS):
        cls = ' class="featured-col"' if p["featured"] else ""
        pill = '<span class="popular-pill" data-es="Más Popular">Most Popular</span>' if p["featured"] else ""
        head_cells.append(
            f'<th{cls}>{pill}<div class="cmp-plan"><span class="name"{CC._es_attr(p.get("name_es"))}>{p["name"]}</span>'
            f'<span class="price">{p["price"]}<span{CC._es_attr(p.get("period_es"))}>{p["period"]}</span></span></div></th>')
    header_row = "<tr><th></th>" + "".join(head_cells) + "</tr>"

    body_rows = []
    for group in C.COMPARE_GROUPS:
        body_rows.append(
            f'<tr class="row-group"><td colspan="4"{CC._es_attr(group.get("name_es"))}>{group["name"]}</td></tr>')
        for row in group["rows"]:
            cells = "".join(_cell(v, C.PLANS[i]["featured"]) for i, v in enumerate(row["values"]))
            body_rows.append(f'<tr><td{CC._es_attr(row.get("label_es"))}>{row["label"]}</td>{cells}</tr>')

    cta_cells = "".join(
        f'<td class="{"featured-col" if p["featured"] else ""}">'
        f'<a class="btn {"btn-primary" if p["featured"] else "btn-ghost"}" href="contact.html" data-es="Empezar">Get started</a></td>'
        for p in C.PLANS)
    body_rows.append(f'<tr class="cmp-cta-row"><td></td>{cta_cells}</tr>')

    return f"""<section id="full-compare" class="sec" style="background:var(--panel);border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)">
  <div class="wrap sec-head"><span class="sec-tag"{CC._es_attr(C.COMPARE_TAG_ES)}>{C.COMPARE_TAG}</span>
  <h2{CC._es_attr(C.COMPARE_H2_ES)}>{C.COMPARE_H2}</h2>
  <p class="lead"{CC._es_attr(C.COMPARE_LEAD_ES)}>{C.COMPARE_LEAD}</p></div>
  <div class="wrap">
    <p class="cmp-swipe-hint" data-es="Desliza para ver los 3 niveles &rarr;">Swipe to see all 3 tiers &rarr;</p>
    <div class="cmp-outer"><div class="cmp-wrap"><table class="cmp">
      <thead>{header_row}</thead>
      <tbody>{"".join(body_rows)}</tbody>
    </table></div><div class="cmp-fade" aria-hidden="true"></div></div>
  </div>
</section>"""

PRICING_EXTRA_CSS = """
.at-a-glance{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:20px;padding:14px;background:rgba(255,255,255,.03);border-radius:10px;border:1px solid rgba(255,255,255,.06)}
.glance-item{text-align:center}
.glance-item .num{display:block;font-size:18px;font-weight:800;color:var(--gold);font-family:var(--font-head)}
.glance-item .lbl{display:block;font-size:10px;color:var(--cream-muted);text-transform:uppercase;letter-spacing:.04em;margin-top:2px}
.daily-cost{display:flex;justify-content:center;gap:0;flex-wrap:wrap;max-width:720px;margin:30px auto 0;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:12px;overflow:hidden}
.daily-item{flex:1;min-width:160px;text-align:center;padding:16px 18px;border-left:1px solid rgba(255,255,255,.07)}
.daily-item:first-child{border-left:0}
.daily-item .amt{font-family:var(--font-head);font-weight:800;font-size:19px;color:var(--gold)}
.daily-item .amt span{font-size:12px;font-weight:600;color:var(--cream-muted)}
.daily-item .lbl{font-size:11.5px;color:var(--cream-muted);margin-top:3px}
.daily-caption{text-align:center;font-size:12.5px;color:var(--cream-muted);max-width:600px;margin:12px auto 0}
.fit-grid{display:grid;grid-template-columns:1fr 1fr;gap:22px;max-width:920px;margin:0 auto}
/* 2026-08-24: this grid had NO mobile breakpoint at all -- stayed 2 columns
   even on phones, squishing every line of text. Site convention (see
   .addon-grid/.split-grid/.plans-grid in site_common.py) collapses 2-col
   grids to 1 col at max-width:900px -- match it here. */
@media(max-width:900px){.fit-grid{grid-template-columns:1fr}}
.fit-card{background:var(--panel);border-radius:14px;padding:26px 28px}
.fit-card.yes{border:1px solid rgba(61,220,132,.35)}
.fit-card.no{border:1px solid rgba(255,255,255,.10)}
.fit-card h3{font-size:16px;display:flex;align-items:center;gap:8px;margin-bottom:14px}
.fit-card.yes h3{color:#3ddc84}
.fit-card.no h3{color:var(--cream-muted)}
.fit-list{list-style:none}
.fit-list li{padding:8px 0 8px 24px;position:relative;font-size:14px;color:var(--cream-muted);border-top:1px solid rgba(255,255,255,.05)}
.fit-list li:first-child{border-top:0}
.fit-card.yes .fit-list li::before{content:"\\2713";position:absolute;left:0;color:#3ddc84;font-weight:700}
.fit-card.no .fit-list li::before{content:"\\2013";position:absolute;left:2px;color:rgba(255,255,255,.35);font-weight:700}
.cmp-linkrow{text-align:center;margin:38px 0 0}
.cmp-link{display:inline-flex;align-items:center;gap:8px;color:var(--gold);font-weight:700;font-size:14px;text-decoration:none;cursor:pointer}
.cmp-link .arrow{transition:transform .2s ease}
.cmp-link:hover .arrow{transform:translateY(3px)}
.cmp-outer{position:relative}
.cmp-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;border-radius:16px;border:1px solid rgba(255,255,255,.08);background:var(--panel2)}
/* 2026-08-24: the table scrolled fine on mobile but gave no hint that it
   did -- the cut-off right edge just looked like the table ended there.
   Adds an explicit "swipe" label (mobile only) plus a static edge fade so
   the cut-off column reads as "more here", not "that's all of it". */
.cmp-swipe-hint{display:none;text-align:center;align-items:center;justify-content:center;gap:6px;color:var(--gold);font-weight:700;font-size:12.5px;letter-spacing:.02em;margin-bottom:10px}
@media(max-width:900px){.cmp-swipe-hint{display:flex}}
.cmp-fade{display:none;position:absolute;top:1px;right:1px;bottom:1px;width:36px;border-radius:0 16px 16px 0;background:linear-gradient(to right,transparent,var(--panel2) 80%);pointer-events:none}
@media(max-width:900px){.cmp-fade{display:block}}
table.cmp{width:100%;border-collapse:collapse;min-width:640px}
table.cmp th,table.cmp td{padding:15px 20px;text-align:center;border-bottom:1px solid rgba(255,255,255,.06)}
table.cmp th:first-child,table.cmp td:first-child{text-align:left;color:var(--cream-muted);font-size:14px;font-weight:500;width:34%}
table.cmp thead th{padding-top:24px}
.cmp-plan{font-family:var(--font-head);font-weight:700}
.cmp-plan .name{font-size:16px;display:block}
.cmp-plan .price{font-size:22px;font-weight:800;color:var(--gold);display:block;margin-top:8px}
.cmp-plan .price span{font-size:11px;font-weight:600;color:var(--cream-muted)}
th.featured-col,td.featured-col{background:linear-gradient(180deg,rgba(255,179,71,.10),rgba(255,179,71,.03))}
th.featured-col{position:relative}
.popular-pill{position:absolute;top:6px;left:50%;transform:translateX(-50%);background:linear-gradient(100deg,var(--gold),var(--gold-deep));color:var(--ink);font-size:10px;font-weight:800;letter-spacing:.06em;padding:4px 12px;border-radius:999px;text-transform:uppercase;white-space:nowrap}
.cmp-val{font-size:14px;color:var(--cream)}
.check{color:#3ddc84;font-size:16px}
.dash{color:rgba(255,255,255,.25)}
tbody tr:last-child td{border-bottom:0}
tr.row-group td{background:rgba(255,255,255,.02);color:var(--gold);font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;text-align:left;padding:11px 20px}
.cmp-cta-row td{padding:20px 20px 24px;border-bottom:0}
@media(max-width:720px){table.cmp{min-width:560px}}
/* Add-on cards -- gold frame + the same pulsing coral glow used site-wide
   on .card (pillars/why-it's-free sections use this exact combo: gold
   border, coral animated glow via the shared cardGlowPulse keyframes
   already defined in site_common.py's base_css()). Reuses the animation
   name rather than redefining it. */
.addon-card{border:1px solid var(--gold);box-shadow:0 12px 28px rgba(0,0,0,.35),0 0 46px rgba(var(--primary-rgb),.28);animation:cardGlowPulse 4s ease-in-out infinite}
@media(prefers-reduced-motion:reduce){.addon-card{animation:none}}
"""

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
    extra_css = f"<style>{PRICING_EXTRA_CSS}</style>"
    html = (
        S.head(title, desc, "pricing.html")
        + extra_css
        + S.nav("pricing.html")
        + hero()
        + plans()
        + fit_section()
        + full_compare()
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
