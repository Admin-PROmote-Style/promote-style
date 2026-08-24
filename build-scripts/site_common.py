# -*- coding: utf-8 -*-
"""
site_common.py -- shared layout (head, nav, footer, base CSS) for every page
of the mAIntAIn Style site. Edit facts/copy/colors in config.py, not here.
"""
import os, sys, base64, mimetypes, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # mAIntAInStyles/

# Same envelope icon used in every client site's footer (see e.g.
# CLIENTS/Fat_Tonys/site/build-scripts/site_common.py _SVG_MAIL) -- added here
# 2026-08-15 so the mS site footer matches client-site styling.
_SVG_MAIL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
             'stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/>'
             '<path d="M3 7l9 6 9-6"/></svg>')

def embed_img(value):
    if not value:
        return ""
    if value.startswith(("http://", "https://", "data:")):
        return value
    path = value if os.path.isabs(value) else os.path.join(ROOT, value)
    if os.path.exists(path):
        mime = mimetypes.guess_type(path)[0] or "image/png"
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        return f"data:{mime};base64,{b64}"
    return value

def _hex_to_rgb(h):
    h = h.lstrip("#")
    return f"{int(h[0:2],16)},{int(h[2:4],16)},{int(h[4:6],16)}"

def css_root():
    k = C.COLORS
    return f""":root{{
  --primary:{k['primary']}; --primary-bright:{k['primary_bright']};
  --gold:{k['gold']}; --gold-deep:{k['gold_deep']};
  --cream:{k['cream']}; --cream-muted:{k['cream_muted']};
  --bg-deep:{k['bg_deep']}; --panel:{k['panel']}; --panel2:{k['panel2']}; --ink:{k['ink']};
  --primary-deep:{k.get('primary_deep', k['bg_deep'])};
  --primary-rgb:{_hex_to_rgb(k['primary'])};
  --gold-rgb:{_hex_to_rgb(k['gold'])};
  --font-head:'{C.FONT_HEADING}',system-ui,sans-serif;
  --font-body:'{C.FONT_BODY}',system-ui,Arial,sans-serif;
}}"""

def base_css():
    return css_root() + """
/* 2026-08-23: native dissolve transition between pages on this site.
   Same-origin only (Chrome/Edge 126+, Safari 18.2+) -- Firefox and any
   cross-domain link (e.g. to maintain.style or client.style) just fall
   back to a normal instant navigation, no breakage either way. */
@view-transition{navigation:auto}
::view-transition-old(root),::view-transition-new(root){animation-duration:.4s}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--font-body);color:var(--cream);background:var(--bg-deep);line-height:1.6;
  background-image:radial-gradient(ellipse 900px 500px at 15% -10%,rgba(0,143,255,.30),transparent 60%),
                    radial-gradient(ellipse 700px 500px at 100% 0%,rgba(255,209,93,.16),transparent 55%);
  background-repeat:no-repeat}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
h1,h2,h3{font-family:var(--font-head);line-height:1.15;font-weight:700;letter-spacing:-.01em}
.wrap{max-width:1180px;margin:0 auto;padding:0 32px}
.grad{background:linear-gradient(100deg,var(--primary-bright) 10%,var(--gold) 90%);-webkit-background-clip:text;background-clip:text;color:transparent}
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 28px;border-radius:8px;font-weight:700;font-family:var(--font-body);cursor:pointer;border:0;transition:all .25s ease;font-size:15px}
.btn-primary{background:linear-gradient(100deg,var(--gold),var(--gold-deep));color:var(--ink)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(255,209,93,.40)}
.btn-ghost{background:rgba(255,255,255,.03);border:1.5px solid rgba(255,255,255,.18);color:var(--cream)}
.btn-ghost:hover{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.35);transform:translateY(-2px)}
/* nav */
.nav{position:sticky;top:0;z-index:50;background:rgba(9,12,20,.86);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.07);padding:18px 0}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:18px}
.brand{display:flex;align-items:center}
.brand img{height:60px;width:auto}
.nav-links{display:flex;gap:34px;align-items:center}
.nav-links a{font-weight:500;font-size:14px;letter-spacing:.3px;color:var(--cream-muted);padding:4px 0;border-bottom:2px solid transparent}
.nav-links a:hover{color:var(--cream)}
.nav-links a.active{color:var(--cream);border-bottom-color:var(--gold)}
.nav-cta{display:flex;gap:10px;align-items:center}
.hamb{display:none;background:none;border:0;color:var(--cream);font-size:26px;cursor:pointer}
.mobile-menu{display:none;flex-direction:column;background:var(--panel);padding:16px 22px;gap:14px;border-bottom:1px solid rgba(255,255,255,.07)}
.mobile-menu.open{display:flex}
.mobile-menu a{color:var(--cream-muted);font-weight:600}
/* sections */
.sec{padding:88px 0;scroll-margin-top:116px}
.sec-tag{color:var(--gold);font-weight:700;letter-spacing:.14em;font-size:12.5px;text-transform:uppercase}
.sec h2{font-size:clamp(26px,3.6vw,38px);margin:10px 0 16px}
.sec-head{text-align:center;max-width:680px;margin:0 auto 40px}
.sec-head .sec-tag{display:block;margin-bottom:10px}
.sec-head h2{margin-bottom:14px}
.lead{color:var(--cream-muted);font-size:17px;max-width:640px}
.sec-head .lead{margin:0 auto}
.badge-pill{display:inline-block;background:rgba(255,209,93,.14);border:1px solid rgba(255,209,93,.45);color:var(--gold);font-size:12px;font-weight:700;padding:7px 16px;border-radius:999px;letter-spacing:.08em;margin-bottom:26px}
/* hero */
.hero{background:radial-gradient(ellipse 1100px 380px at 50% -40px,rgba(var(--primary-rgb),.38) 0%,rgba(var(--primary-rgb),0) 75%) var(--bg-deep);padding:96px 0 76px;text-align:center;position:relative}
.hero h1{font-size:clamp(34px,5.4vw,58px);line-height:1.14;margin-bottom:22px;max-width:900px;margin-left:auto;margin-right:auto}
.hero .lead{font-size:18px;max-width:620px;margin:0 auto 34px}
.hero-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
/* trust strip */
.trust{background:var(--panel);padding:28px 0;border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)}
.trust .wrap{display:flex;justify-content:space-around;text-align:center;flex-wrap:wrap;gap:22px}
.trust-item .num{font-size:15px;font-weight:700;color:var(--cream)}
.trust-item .lbl{font-size:12px;color:var(--cream-muted);margin-top:3px}
/* process */
.process{display:grid;grid-template-columns:repeat(4,1fr);gap:26px;counter-reset:step}
.process-step{background:var(--panel);border:1.5px solid var(--gold-deep);border-radius:14px;padding:26px 22px;position:relative;box-shadow:0 0 0 1px rgba(255,209,93,.30),0 12px 28px rgba(0,0,0,.35)}
.process-step .step-num{font-family:var(--font-head);font-size:15px;font-weight:700;color:var(--gold);border:1.5px solid var(--gold-deep);border-radius:50%;width:38px;height:38px;display:flex;align-items:center;justify-content:center;margin-bottom:16px}
.process-step h3{font-size:19px;margin-bottom:8px}
.process-step p{color:var(--cream-muted);font-size:14.5px}
/* feature cards */
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.card{background:var(--panel);border:1px solid rgba(255,255,255,.07);border-radius:14px;padding:28px;box-shadow:0 12px 28px rgba(0,0,0,.35),0 0 46px rgba(var(--primary-rgb),.28)}
/* 2026-08-17: pulsing glow now on every card with the red/coral glow
   site-wide (:not(.us) excludes the featured comparison card, which has
   its own static gold treatment). Gold outline on pillars + "why it's
   free" cards; the first two (non-featured) comparison cards get a red
   outline instead to match their glow color. */
.card:not(.us){animation:cardGlowPulse 4s ease-in-out infinite}
@keyframes cardGlowPulse{
  0%,100%{box-shadow:0 12px 28px rgba(0,0,0,.35),0 0 46px rgba(var(--primary-rgb),.28)}
  50%{box-shadow:0 12px 28px rgba(0,0,0,.35),0 0 68px rgba(var(--primary-rgb),.52)}
}
@media(prefers-reduced-motion:reduce){.card:not(.us){animation:none}}
#pillars .card,#why .card{border:1px solid var(--gold)}
#difference .card:not(.us){border:1px solid var(--primary)}
.card .ic{font-family:var(--font-head);font-weight:700;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);margin-bottom:14px}
.card h3{font-size:21px;margin-bottom:10px}
.card p{color:var(--cream-muted);font-size:15px}
/* portfolio */
.portfolio-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:26px;max-width:900px;margin:0 auto}
.port-card{display:block;background:var(--panel);border:1px solid rgba(255,255,255,.07);border-radius:16px;overflow:hidden;transition:transform .25s ease,box-shadow .25s ease;color:inherit;text-decoration:none}
.port-card:hover{transform:translateY(-4px);box-shadow:0 20px 40px rgba(0,0,0,.4)}
a.port-card{cursor:pointer}
.port-preview{aspect-ratio:16/10;position:relative;display:flex;flex-direction:column;overflow:hidden}
.port-preview .chrome{background:rgba(0,0,0,.28);padding:9px 12px;display:flex;gap:6px;position:relative;z-index:2}
.port-preview .chrome span{width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,.35)}
.port-preview .fill{flex:1;display:flex;align-items:center;justify-content:center;font-family:var(--font-head);font-weight:700;font-size:15px;color:rgba(255,255,255,.85);text-align:center;padding:18px}
.port-preview.c-primary{background:linear-gradient(135deg,var(--primary),#232c42)}
.port-preview.c-primary_bright{background:linear-gradient(135deg,var(--primary-bright),var(--primary))}
.port-preview.c-gold{background:linear-gradient(135deg,var(--gold-deep),#2a2210)}
.port-preview.c-slate{background:linear-gradient(135deg,var(--panel2),var(--cream-muted))}
.port-preview .shot{flex:1;position:relative;overflow:hidden}
.port-preview .shot img{position:absolute;top:0;left:0;width:100%;height:auto;min-height:100%;object-fit:cover;object-position:top center;transition:transform .35s ease}
.port-card:hover .shot img{transform:scale(1.04)}
/* back to top */
.totop{position:fixed;bottom:28px;right:28px;width:54px;height:54px;background:none;border:0;cursor:pointer;padding:0;opacity:0;pointer-events:none;transform:translateY(16px) rotate(-15deg);transition:opacity .3s ease,transform .3s ease;z-index:999;filter:drop-shadow(0 4px 10px rgba(0,0,0,.5))}
.totop img{width:100%;height:100%;object-fit:contain}
.totop.show{opacity:1;pointer-events:auto;transform:translateY(0) rotate(0deg)}
.totop.show:hover{transform:translateY(-3px) rotate(12deg) scale(1.12);filter:drop-shadow(0 8px 16px rgba(0,0,0,.6))}
.port-body{padding:22px 24px 26px}
.port-cat{font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold)}
.port-body h3{font-size:20px;margin:8px 0 8px}
.port-body p{color:var(--cream-muted);font-size:14.5px;margin-bottom:16px}
.port-foot{display:flex;align-items:center;justify-content:space-between;gap:10px}
.status-pill{font-size:11.5px;font-weight:700;padding:5px 12px;border-radius:999px;background:rgba(255,255,255,.06);color:var(--cream-muted);border:1px solid rgba(255,255,255,.1)}
.status-pill.live{background:rgba(255,209,93,.14);color:var(--gold);border-color:rgba(255,209,93,.45)}
.port-link{font-size:13.5px;font-weight:700;color:var(--cream)}
.port-card:hover .port-link{color:var(--gold)}
/* pricing */
.plans-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:stretch}
.plan-card{background:var(--panel);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:32px 28px;display:flex;flex-direction:column}
/* 2026-08-24, George's call: each tier gets its own frame/glow color so the
   3 cards read as distinct at a glance -- Starter + Full-Service in blue
   (reuses the same blue already used as an ambient background accent, see
   body's radial-gradient above), Growth (.featured) upgraded from a static
   gold shadow to the same pulsing-glow treatment used elsewhere on the site
   (cardGlowPulse pattern), just in gold instead of coral. Applies wherever
   .plans-grid/.plan-card is used -- pricing.html AND the homepage teaser
   share this file, so both stay in sync automatically. */
.plans-grid .plan-card:first-child,.plans-grid .plan-card:last-child{border:1px solid rgba(0,143,255,.55);animation:planGlowBlue 4s ease-in-out infinite}
@keyframes planGlowBlue{
  0%,100%{box-shadow:0 12px 28px rgba(0,0,0,.35),0 0 46px rgba(0,143,255,.28)}
  50%{box-shadow:0 12px 28px rgba(0,0,0,.35),0 0 68px rgba(0,143,255,.50)}
}
.plan-card.featured{border-color:var(--gold);background:linear-gradient(180deg,var(--panel2),var(--panel));animation:planGlowGold 4s ease-in-out infinite}
@keyframes planGlowGold{
  0%,100%{box-shadow:0 0 0 1px rgba(255,209,93,.30),0 20px 50px rgba(255,209,93,.10),0 0 46px rgba(var(--gold-rgb),.28)}
  50%{box-shadow:0 0 0 1px rgba(255,209,93,.30),0 20px 50px rgba(255,209,93,.10),0 0 68px rgba(var(--gold-rgb),.50)}
}
@media(prefers-reduced-motion:reduce){.plans-grid .plan-card:first-child,.plans-grid .plan-card:last-child,.plan-card.featured{animation:none}}
.plan-tag{font-size:11.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);margin-bottom:10px}
.plan-card h3{font-size:24px;margin-bottom:4px}
.plan-price{font-family:var(--font-head);font-size:34px;font-weight:800;color:var(--cream);margin-bottom:18px;display:flex;align-items:baseline;gap:6px}
.plan-price span{font-family:var(--font-body);font-size:13px;font-weight:600;color:var(--cream-muted)}
.plan-card.featured .plan-price{color:var(--gold)}
.plan-features{list-style:none;margin:0 0 26px;flex:1}
.plan-features li{color:var(--cream-muted);font-size:14.5px;padding:9px 0;border-top:1px solid rgba(255,255,255,.06);display:flex;gap:10px}
.plan-features li:first-child{border-top:0}
.plan-features li::before{content:"\\2713";color:var(--gold);font-weight:700}
.plans-intro{max-width:760px;margin:36px auto 50px;text-align:center;color:var(--cream-muted);font-size:16px}
/* comparison (home) */
.card.us{border-color:var(--gold);background:linear-gradient(180deg,var(--panel2),var(--panel));animation:cardGlowPulseGold 4s ease-in-out infinite}
@keyframes cardGlowPulseGold{
  0%,100%{box-shadow:0 0 0 1px rgba(var(--gold-rgb),.4),0 20px 50px rgba(var(--gold-rgb),.14),0 0 48px rgba(var(--gold-rgb),.44)}
  50%{box-shadow:0 0 0 1px rgba(var(--gold-rgb),.55),0 20px 50px rgba(var(--gold-rgb),.2),0 0 68px rgba(var(--gold-rgb),.62)}
}
@media(prefers-reduced-motion:reduce){.card.us{animation:none;box-shadow:0 0 0 1px rgba(var(--gold-rgb),.4),0 20px 50px rgba(var(--gold-rgb),.14),0 0 48px rgba(var(--gold-rgb),.44)}}
/* hosting include/limits (pricing) */
.split-grid{display:grid;grid-template-columns:1fr 1fr;gap:32px;max-width:900px;margin:0 auto}
.split-col{background:var(--panel);border:1px solid rgba(255,255,255,.07);border-radius:14px;padding:26px 28px}
.split-col h3{font-size:16px;margin-bottom:14px;text-transform:uppercase;letter-spacing:.06em}
.split-col.includes h3{color:var(--gold)}
.split-col.limits h3{color:var(--cream-muted)}
.check-list,.x-list{list-style:none}
.check-list li,.x-list li{display:flex;gap:10px;align-items:flex-start;padding:11px 0;border-top:1px solid rgba(255,255,255,.06);font-size:14px}
.check-list li:first-child,.x-list li:first-child{border-top:0}
.check-list li::before{content:"\\2713";color:var(--gold);font-weight:700;flex:0 0 auto;line-height:1.5}
.x-list li::before{content:"\\2014";color:var(--cream-muted);font-weight:700;flex:0 0 auto;line-height:1.5}
.check-list li strong,.x-list li strong{color:var(--cream);display:block;font-size:14.5px;margin-bottom:2px}
.check-list li span,.x-list li span{color:var(--cream-muted)}
.hosting-note{max-width:640px;margin:34px auto 0;text-align:center;color:var(--cream-muted);font-size:15px}
/* addons (pricing) */
.addon-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;max-width:900px;margin:0 auto 20px}
.addon-grid>div:last-child:nth-child(odd){grid-column:1/-1}
.addon-card{background:var(--panel);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:20px 22px}
.addon-card h4{font-size:15.5px;margin-bottom:6px}
.addon-price{color:var(--gold);font-weight:700;font-size:14px;margin-bottom:8px}
.addon-card p{color:var(--cream-muted);font-size:13.5px}
/* contact form */
.contact-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:start}
.form-panel{background:var(--panel);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:34px}
.field{margin-bottom:18px}
.field label{display:block;font-size:13px;font-weight:600;color:var(--cream-muted);margin-bottom:7px}
.field input,.field textarea{width:100%;background:var(--bg-deep);border:1px solid rgba(255,255,255,.14);border-radius:8px;padding:12px 14px;color:var(--cream);font-family:var(--font-body);font-size:15px}
.field input:focus,.field textarea:focus{outline:none;border-color:var(--gold)}
.field textarea{resize:vertical;min-height:120px}
.contact-side h3{font-size:19px;margin-bottom:10px}
.contact-side p{color:var(--cream-muted);font-size:14.5px;margin-bottom:22px}
.contact-side a.email{color:var(--gold);font-weight:700}
.form-note{font-size:12.5px;color:var(--cream-muted);margin-top:10px}
/* cta band -- 2026-08-17: comment said this "matches hero's radial glow
   instead of the diagonal linear-gradient", but the actual background rule
   below was never changed -- it still had the old
   linear-gradient(135deg,var(--primary),#3a0f08), which is exactly the hard
   dark corner (bottom-right) the comment describes fixing. Caught live on
   the pricing page's "Not sure which tier fits?" band 2026-08-24 and
   actually applied the radial-glow treatment this time, using the same
   technique as .hero (radial highlight over a flat base) instead of a
   directional gradient. */
.cta-band{background:radial-gradient(ellipse 1100px 380px at 50% -40px,rgba(255,255,255,.14) 0%,rgba(255,255,255,0) 70%) var(--primary-deep);text-align:center;padding:64px 32px;border-radius:0;border-top:1px solid rgba(255,255,255,.08);border-bottom:1px solid rgba(255,255,255,.08);position:relative;overflow:hidden}
.cta-band::before{content:"";position:absolute;width:420px;height:420px;border-radius:50%;background:rgba(255,255,255,.06);top:-160px;right:-120px;animation:ctaFloat1 14s ease-in-out infinite;pointer-events:none}
.cta-band::after{content:"";position:absolute;width:280px;height:280px;border-radius:50%;background:rgba(255,179,71,.08);bottom:-120px;left:-80px;animation:ctaFloat2 16s ease-in-out infinite;pointer-events:none}
.cta-band .wrap{position:relative;z-index:1}
@keyframes ctaFloat1{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(-24px,26px) scale(1.12)}}
@keyframes ctaFloat2{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(22px,-18px) scale(1.15)}}
@media(prefers-reduced-motion:reduce){.cta-band::before,.cta-band::after{animation:none}}
.cta-band h2{font-size:clamp(24px,3.6vw,36px);color:var(--cream);margin-bottom:12px;max-width:760px;margin-left:auto;margin-right:auto}
.cta-band p{color:var(--cream);opacity:.9;margin-bottom:26px;max-width:560px;margin-left:auto;margin-right:auto}
/* footer */
.logo-divider{background:radial-gradient(ellipse 1100px 380px at 50% -40px,rgba(var(--primary-rgb),.38) 0%,rgba(var(--primary-rgb),0) 75%) var(--bg-deep);padding:54px 0 60px;text-align:center;border-top:1px solid rgba(255,255,255,.06)}
.logo-divider img{width:280px;max-width:60vw;height:auto;margin:0 auto}
.foot{background:var(--bg-deep);padding:40px 0 30px;text-align:center}
.foot a.email{color:var(--gold);font-weight:700;font-size:15px;display:inline-flex;align-items:center;gap:8px}
.foot a.email svg{width:18px;height:18px;flex-shrink:0}
.foot-links{display:flex;justify-content:center;gap:26px;margin:18px 0;flex-wrap:wrap}
.foot-links a{color:var(--cream-muted);font-size:13.5px}
.foot-links a:hover{color:var(--cream)}
.copyright{margin-top:22px;padding-top:18px;border-top:1px solid rgba(255,255,255,.08);font-size:12px;color:var(--cream-muted);opacity:.7}
/* responsive */
@media(max-width:900px){
 .process{grid-template-columns:1fr 1fr}
 .cards{grid-template-columns:1fr}
 .portfolio-grid{grid-template-columns:1fr}
 .plans-grid{grid-template-columns:1fr}
 .contact-grid{grid-template-columns:1fr}
 .split-grid,.addon-grid{grid-template-columns:1fr}
 .nav-links,.nav-cta{display:none}.hamb{display:block}
 .sec{padding:60px 0}
}
@media(max-width:560px){.process{grid-template-columns:1fr}}
/* lang toggle -- 2026-08-17: corrected against the real reference,
   fattonysbend.com -- the pill sits just BELOW the header, floating in
   the hero's top-right corner, not inline inside the nav row (my first
   pass here nested it centered inside the header itself, which visually
   broke the family look). Still a child of <nav>, but anchored to the
   header's bottom edge (top:100%) instead of its vertical middle -- so
   it tracks the header's real height automatically (no hardcoded pixel
   guess to go stale when a font/logo change alters header height) while
   preserving the "small tag hanging just under the header" placement
   every other mS-family site uses. nav's position:sticky is the
   positioning context this resolves against. */
.lang-toggle{position:absolute;top:calc(100% + 8px);right:20px;background:rgba(9,12,20,.75);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.18);color:var(--cream);font-size:11px;font-weight:700;letter-spacing:.06em;padding:5px 12px;border-radius:999px;cursor:pointer;font-family:var(--font-body);z-index:60;box-shadow:0 4px 12px rgba(0,0,0,.35);transition:background .2s ease}
.lang-toggle:hover{background:rgba(9,12,20,.95)}
@media(max-width:900px){.lang-toggle{right:16px}}
"""

def head(title, description, path="index.html"):
    icon = embed_img(C.LOGO_IMAGE)
    live = C.LIVE_URL.rstrip("/")
    canonical = f"{live}/{path}" if path != "index.html" else f"{live}/"
    # og:image needs a real fetchable URL, not the base64 data URI used for
    # the inline favicon/logo -- points at the real file copied into
    # site/assets/ by build_all.py's copy_assets() step.
    og_image = f"{live}/{C.LOGO_IMAGE}"
    org_schema = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"{C.BUSINESS_NAME}",
"description":"{C.TAGLINE}","url":"{live}/","logo":"{og_image}",
"areaServed":"{C.CITY_STATE}","email":"{C.EMAIL}"}}
</script>"""
    return f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:site_name" content="{C.BUSINESS_NAME}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">
<link rel="icon" href="{icon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{C.GOOGLE_FONTS_HREF}" rel="stylesheet">
<style>{base_css()}</style>
{org_schema}
</head><body>"""

def copy_assets():
    """Copies assets/ into site/assets/ as real files (not base64) so
    og:image/twitter:image and any future direct-linked images have a real
    URL to point at once deployed. Safe to call every build."""
    import shutil
    src = os.path.join(ROOT, "assets")
    dst = os.path.join(ROOT, "site", "assets")
    if not os.path.isdir(src):
        return
    os.makedirs(dst, exist_ok=True)
    for fname in os.listdir(src):
        if fname.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".webp")):
            shutil.copy2(os.path.join(src, fname), os.path.join(dst, fname))

NAV_LABELS_ES = {
    "Home": "Inicio",
    "Portfolio": "Portafolio",
    "Plans": "Planes",
    "Pricing": "Precios",
    "SEO 101": "Fundamentos SEO",
    # "mAIntAIn Style" intentionally omitted -- it's a brand name, not translated.
}

def _es_attr(label):
    es = NAV_LABELS_ES.get(label)
    return f' data-es="{es}"' if es else ""

def _ext_attr(href):
    return ' target="_blank" rel="noopener"' if href.startswith("http") else ""

def nav(active=""):
    def _link(href, label):
        cls = ' class="active"' if href == active else ""
        return f'<a href="{href}"{cls}{_ext_attr(href)}{_es_attr(label)}>{label}</a>'
    links = "".join(_link(href, label) for href, label in C.NAV_LINKS)
    mob_links = "".join(f'<a href="{href}"{_ext_attr(href)}{_es_attr(label)}>{label}</a>' for href, label in C.NAV_LINKS)
    return f"""<nav class="nav"><div class="wrap">
  <a class="brand" href="index.html"><img src="{embed_img(C.NAV_LOGO_IMAGE)}" alt="{C.BUSINESS_NAME} logo"></a>
  <div class="nav-links">
    {links}
  </div>
  <div class="nav-cta">
    <a class="btn btn-primary" href="contact.html" data-es="Iniciar un proyecto">Start a Project</a>
  </div>
  <button class="hamb" onclick="document.getElementById('mm').classList.toggle('open')">&#9776;</button>
</div>
<div class="mobile-menu" id="mm">
  {mob_links}
  <a href="contact.html" data-es="Iniciar un proyecto">Start a Project</a>
</div>
<button class="lang-toggle" id="langToggle" type="button" aria-label="Switch language">ESP</button>
</nav>"""

def footer():
    yr = datetime.date.today().year
    links = "".join(f'<a href="{href}"{_ext_attr(href)}{_es_attr(label)}>{label}</a>' for href, label in C.NAV_LINKS)
    return f"""<section class="logo-divider"><img src="{embed_img(C.LOGO_IMAGE)}" alt="{C.BUSINESS_NAME} logo"></section>
<footer class="foot"><div class="wrap">
  <a class="email" href="mailto:{C.EMAIL}">{_SVG_MAIL}<span>{C.EMAIL}</span></a>
  <div class="foot-links">{links}<a href="contact.html" data-es="Contacto">Contact</a></div>
  <p class="copyright" data-es="&copy; {yr} {C.BUSINESS_NAME}. Con sede en {C.CITY_STATE}.">&copy; {yr} {C.BUSINESS_NAME}. Based in {C.CITY_STATE}.</p>
</div></footer>"""

def back_to_top():
    icon = getattr(C, "TOTOP_ICON", "")
    inner = f'<img src="{embed_img(icon)}" alt="">' if icon else "&#8593;"
    return (f'<button class="totop" id="totop" aria-label="Back to top"\n'
            " onclick=\"window.scrollTo({top:0,behavior:'smooth'})\">" + inner + "</button>\n"
            "<script>window.addEventListener('scroll',function(){\n"
            " document.getElementById('totop').classList.toggle('show',window.scrollY>320);},{passive:true});</script>")

def lang_script():
    return """<script>(function(){
  var LANG_KEY='site_lang';
  function getLang(){try{return localStorage.getItem(LANG_KEY)||'en';}catch(e){return 'en';}}
  function setLang(l){try{localStorage.setItem(LANG_KEY,l);}catch(e){}}
  function apply(lang){
    document.querySelectorAll('[data-es]').forEach(function(el){
      if(el.dataset.enOrig===undefined) el.dataset.enOrig=el.textContent;
      el.textContent = lang==='es' ? el.dataset.es : el.dataset.enOrig;
    });
    document.querySelectorAll('[data-es-html]').forEach(function(el){
      if(el.dataset.enOrigHtml===undefined) el.dataset.enOrigHtml=el.innerHTML;
      el.innerHTML = lang==='es' ? el.dataset.esHtml : el.dataset.enOrigHtml;
    });
    document.querySelectorAll('[data-es-placeholder]').forEach(function(el){
      if(el.dataset.enOrigPlaceholder===undefined) el.dataset.enOrigPlaceholder=el.getAttribute('placeholder')||'';
      el.setAttribute('placeholder', lang==='es' ? el.dataset.esPlaceholder : el.dataset.enOrigPlaceholder);
    });
    document.documentElement.setAttribute('lang', lang);
    var btn=document.getElementById('langToggle');
    if(btn) btn.textContent = lang==='es' ? 'ENG' : 'ESP';
  }
  document.addEventListener('DOMContentLoaded', function(){
    apply(getLang());
    var btn=document.getElementById('langToggle');
    if(btn) btn.addEventListener('click', function(){
      var next = getLang()==='es' ? 'en' : 'es';
      setLang(next);
      apply(next);
    });
  });
})();</script>"""

def close_html():
    return lang_script() + "</body></html>"

def write_page(name, html):
    site_dir = os.path.join(ROOT, "site")
    os.makedirs(site_dir, exist_ok=True)
    root_path = os.path.join(ROOT, name)
    site_path = os.path.join(site_dir, name)
    for p in (root_path, site_path):
        with open(p, "w", encoding="utf-8") as f:
            f.write(html)
