# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

def good_to_know(disclaimer_href):
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
    return f"""<div class="plan-card">
  <h3{CC.A("Good to know")}>Good to know</h3>
  <div class="know">
    <p{CC.A(C.BUNDLE_NOTE)}>{CC._esc(C.BUNDLE_NOTE)}</p>
    <p{CC.A(C.PACKAGES_NOTE)}>{CC._esc(C.PACKAGES_NOTE)}</p>
    <p{CC._es_html_attr(sites_es)}>{sites}</p>
    <p class="fine"{CC._es_html_attr(note_es)}>{note}</p>
  </div>
</div>"""

def plan_grid(disclaimer_href):
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
    cards.append(good_to_know(disclaimer_href))
    return f'<div class="plans-grid plans-4">{"".join(cards)}</div>'

def packages_section(heading="h2", disclaimer_href="#disclaimer"):
    return f"""<style>
.plan-card .know{{margin-top:16px}}
.plan-card .know p{{color:var(--cream);font-size:15px;line-height:1.55;margin:0 0 14px}}
.plan-card .know p.fine{{color:var(--cream-muted);font-size:12.5px;line-height:1.5}}
.plan-card .know a{{color:var(--gold);text-decoration:underline}}
#packages{{padding-bottom:0}}
#support{{padding-top:0}}
</style>
<section class="sec" id="packages"><div class="wrap">
  <div class="sec-head"><{heading}{CC.A(C.PACKAGES_H2)}>{CC._esc(C.PACKAGES_H2)}</{heading}>
  <p class="lead"{CC.A(C.PACKAGES_SUB)}>{CC._esc(C.PACKAGES_SUB)}</p></div>
  {plan_grid(disclaimer_href)}
  <p style="text-align:center;font-size:12px;color:var(--cream-muted);opacity:.7;margin:20px auto"{CC.A(C.PRICES_UPDATED)}>{CC._esc(C.PRICES_UPDATED)}</p>
</div></section>"""

def cursor_run_section():
    link = '<a href="https://cursor.com/pricing" target="_blank" rel="noopener">cursor.com/pricing</a>'
    intro = ("Cursor is the AI service your bots live and work in. Think of it as the office building: "
             "you rent it directly from Cursor each month, and we move your bots in, set them up, and show you how to run them. "
             "You own the account and can cancel anytime.")
    intro_es = ("Cursor es el servicio de IA donde tus bots viven y trabajan. Piénsalo como el edificio de la oficina: "
                "lo rentas directamente a Cursor cada mes, y nosotros instalamos tus bots, los configuramos y te enseñamos a manejarlos. "
                "La cuenta es tuya y puedes cancelar cuando quieras.")
    plans = [
        ("Premium", "$30/month", "$30/mes",
         "The starting plan. Your bots are ready when you need them.",
         "El plan inicial. Tus bots están listos cuando los necesitas.", False),
        ("Super", "$100/month", "$100/mes",
         "A full office of bots working for you around the clock, for about $3.33 a day.",
         "Una oficina completa de bots trabajando para ti día y noche, por unos $3.33 al día.", True),
        ("Ultra", "$200/month", "$200/mes",
         "For busy businesses that keep their bots working hard all day.",
         "Para negocios con mucho movimiento que mantienen a sus bots trabajando todo el día.", False),
    ]
    cols = []
    for name, price, price_es, line, line_es, pick in plans:
        badge = (f'<span class="badge-pill"{CC._es_attr("La que elige la mayoría")}>Most businesses pick this</span>'
                 if pick else "")
        cls = "cursor-col pick" if pick else "cursor-col"
        cols.append(f"""<div class="{cls}">
  {badge}
  <h3{CC._es_attr(name)}>{name}</h3>
  <div class="amt"{CC._es_attr(price_es)}>{CC._esc(price)}</div>
  <p{CC._es_attr(line_es)}>{CC._esc(line)}</p>
</div>""")
    fine = ("Cursor's prices as of November 2026, before taxes. Some optional outside AI models cost extra, billed by Cursor. "
            f"Prices can change; see {link} for current plans.")
    fine_es = ("Precios de Cursor a noviembre de 2026, antes de impuestos. Algunos modelos de IA externos opcionales cuestan aparte y los cobra Cursor. "
               f"Los precios pueden cambiar; consulta {link} para ver los planes actuales.")
    return f"""<style>
.cursor-run .intro{{max-width:720px;margin:-8px auto 36px;text-align:center;color:var(--cream);font-size:17px;line-height:1.6}}
.cursor-cols{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:stretch}}
.cursor-col{{background:var(--panel);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:28px 24px;text-align:center;display:flex;flex-direction:column}}
.cursor-col.pick{{border:1px solid var(--gold)}}
.cursor-col .badge-pill{{display:inline-block;max-width:100%;margin-bottom:14px;white-space:normal;line-height:1.35;box-sizing:border-box}}
.cursor-col h3{{font-size:22px;margin:0 0 6px}}
.cursor-col .amt{{font-size:28px;font-weight:700;margin-bottom:12px}}
.cursor-col p{{color:var(--cream-muted);font-size:15.5px;line-height:1.55;margin:0}}
.cursor-run .fine{{max-width:720px;margin:28px auto 0;text-align:center;color:var(--cream-muted);font-size:13px;line-height:1.5}}
.cursor-run .fine a{{color:var(--gold);text-decoration:underline}}
@media(max-width:767px){{.cursor-cols{{grid-template-columns:1fr}}}}
</style>
<section class="sec cursor-run" id="cursor-run"><div class="wrap">
  <div class="sec-head"><span class="sec-tag"{CC._es_attr("LO QUE CUESTA OPERARLA")}>WHAT IT COSTS TO RUN</span>
  <h2{CC._es_attr("Tu Oficina de Bots funciona con Cursor")}>Your Bot Office runs on Cursor</h2></div>
  <p class="intro"{CC._es_attr(intro_es)}>{CC._esc(intro)}</p>
  <div class="cursor-cols">{"".join(cols)}</div>
  <p class="fine"{CC._es_html_attr(fine_es)}>{fine}</p>
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
        + packages_section("h1", "https://promote.style/index.html#disclaimer")
        + cursor_run_section()
        + support_section()
        + cta_band()
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("pricing.html", html)

if __name__ == "__main__":
    build()
