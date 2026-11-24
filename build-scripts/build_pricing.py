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
        tag = f'<div class="plan-tag"{CC.A(p["tag"])}>{CC._esc(p["tag"])}</div>' if p.get("tag") else ""
        feats = "".join(f"<li{CC.A(f)}>{CC._esc(f)}</li>" for f in p["features"])
        note = (f'<p style="margin-top:14px;color:var(--cream-muted);font-size:13.5px;line-height:1.5"{CC.A(p["note"])}>{CC._esc(p["note"])}</p>'
                if p.get("note") else "")
        cards.append(f"""<div class="{cls}">
  {tag}
  <h3{CC.A(p["name"])}>{CC._esc(p["name"])}</h3>
  <div class="plan-price">{CC._esc(p["price"])}</div>
  <ul class="plan-features">{feats}</ul>
  {note}
</div>""")
    return f'<div class="plans-grid plans-4">{"".join(cards)}</div>'

def package_notes(disclaimer_href):
    note = ("PROmote Style provides setup and support services only. "
            "Cursor and other third-party tools are owned and operated by their own companies. "
            f'See our <a href="{disclaimer_href}">Service Disclaimer</a>.')
    note_es = ("PROmote Style solo ofrece servicios de configuración y soporte. "
               "Cursor y las otras herramientas de terceros pertenecen a sus propias empresas y ellas las operan. "
               f'Consulta nuestro <a href="{disclaimer_href}">Descargo de servicio</a>.')
    sites = ('Full packages include a new website built by mAIntAIn Style. '
             'See what each website includes at <a href="https://maintain.style/pricing.html">maintain.style/pricing</a>.')
    sites_es = ('Los paquetes completos incluyen un sitio nuevo hecho por mAIntAIn Style. '
                'Mira qué incluye cada sitio en <a href="https://maintain.style/pricing.html">maintain.style/pricing</a>.')
    return (f'<p class="plans-intro"{CC.A(C.BUNDLE_NOTE)}>{CC._esc(C.BUNDLE_NOTE)}</p>'
            f'<p class="plans-intro"{CC.A(C.PACKAGES_NOTE)}>{CC._esc(C.PACKAGES_NOTE)}</p>'
            f'<p class="plans-note"{CC._es_html_attr(note_es)}>{note}</p>'
            f'<p class="plans-note"{CC._es_html_attr(sites_es)}>{sites}</p>')

def packages_section(heading="h2", disclaimer_href="#disclaimer"):
    return f"""<section class="sec" id="packages"><div class="wrap">
  <div class="sec-head"><{heading}{CC.A(C.PACKAGES_H2)}>{CC._esc(C.PACKAGES_H2)}</{heading}>
  <p class="lead"{CC.A(C.PACKAGES_SUB)}>{CC._esc(C.PACKAGES_SUB)}</p></div>
  {plan_grid()}
  {package_notes(disclaimer_href)}
</div></section>"""

def support_section():
    items = "".join(f"<li{CC.A(line)}><span>{CC._esc(line)}</span></li>" for line in C.PRICING_SUPPORT)
    return f"""<section class="sec" id="support"><div class="wrap">
  <div class="sec-head"><h2{CC.A(C.SUPPORT_H2)}>{CC._esc(C.SUPPORT_H2)}</h2></div>
  <div class="split-col includes support-list"><ul class="check-list">{items}</ul></div>
</div></section>"""

def cta_band():
    return f"""<section class="cta-band"><div class="wrap">
  <h2{CC.A(C.CTA_TITLE)}>{CC._esc(C.CTA_TITLE)}</h2>
  <p{CC.A(C.CTA_SUB)}>{CC._esc(C.CTA_SUB)}</p>
  <div class="hero-btns"><a class="btn btn-primary" href="contact.html"{CC.A(C.CTA_BUTTON)}>{CC._esc(C.CTA_BUTTON)}</a></div>
</div></section>"""

def build():
    html = (
        S.head(C.PRICING_TITLE, C.PRICING_DESC, "pricing.html")
        + S.nav("pricing.html")
        + packages_section("h1", "index.html#disclaimer")
        + support_section()
        + cta_band()
        + f'<p class="wrap" style="text-align:center;font-size:12px;color:var(--cream-muted);opacity:.7;margin:0 auto 28px"{CC.A(C.PRICES_UPDATED)}>{CC._esc(C.PRICES_UPDATED)}</p>'
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("pricing.html", html)

if __name__ == "__main__":
    build()
