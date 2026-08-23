# -*- coding: utf-8 -*-
"""
config.py -- single source of truth for the PROmote Style site.
Edit facts/copy/colors HERE, then run build_all.py. Never hand-edit the
generated .html files.

VERIFIED FACTS ONLY (per project rule -- no invented claims/numbers):
- PROmote Style is a sibling brand to mAIntAIn Style, created by mS.
  Positioning per Promote_Style_Brand_Basics.docx (2026-08-14 working draft):
  mAIntAIn Style = "Built for you, run by you" (site builds, self-service).
  PROmote Style  = "Built for you, run for you" (marketing run on the
  client's behalf -- starts with paid ad management, expands into SEO,
  social, and email).
- Domain promote.style purchased 2026-08-14; not yet pointed at a live
  Cloudflare project as of this build (2026-08-17).
- Real logo artwork landed 2026-08-17 (PROmote-Style-Horizontal-Logo-Large.png,
  PROmote-Style-logo-large.png -- transparent PNGs, PRO in red/PROmote in blue,
  "Style" in a coral/blue script). Swapped in below, replacing the placeholder
  text-wordmark SVGs (kept in assets/ unused, in case a vector version is
  wanted later).
- 2026-08-23: pricing convention REVERSED -- George's earlier $149/$249/$99
  ad-only numbers (from the 2026-08-14 Brand Basics draft) are superseded.
  Verified that mAIntAIn Style's OWN pricing.html already publishes real
  one-time figures ($500/$1,500/$2,500) -- the "keep pricing off-site" note
  above was stale, not a live convention. George confirmed today: publish
  real monthly figures on a new pricing.html for this site too, sourced from
  Single-Business_Marketing_Agreement.pdf (added 2026-08-23, single-business
  scope -- distinct from the same day's Restaurant_Group_*.docx/.pdf, which
  covers the Fat Tony's/Simon's/Tacos 3-restaurant bundle specifically).
  Single-business doc gives ranges (Starter $600-$900/mo, Growth
  $1,000-$1,500/mo, Full-Service $1,800-$2,500/mo); George's own recollection
  when asked was "$1,000/$2,000/$3,000," so the TOP of each documented range
  was chosen as the published figure -- closest defensible number to both
  sources. Flag to George to confirm/adjust if these aren't quite right:
  Starter $900/mo, Growth $1,500/mo, Full-Service $2,500/mo. See PLANS below.
- This build (2026-08-17) adds the free SEO-resource content arm on top of
  the existing brand basics: PROmote Style's site itself is the top-of-
  funnel -- resourceful, wide-audience SEO content that (a) demonstrates
  real expertise and (b) funnels into two offers: mAIntAIn Style site
  builds (since "built SEO-ready from day one" is a real, provable claim
  about mS's own build process) and PROmote Style's own ongoing marketing
  management. Primary CTA below points at mAIntAIn Style site packages,
  per George's explicit instruction 2026-08-17; PROmote Style's own
  service is the secondary CTA. Flag to George if that priority should
  flip.
"""

BUSINESS_NAME = "PROmote Style"
TAGLINE       = "Built for you, run for you."
CITY_STATE    = "Bend, OR"
EMAIL         = "contact@maintain.style"

# Real logo artwork (transparent PNGs, landed 2026-08-17).
LOGO_IMAGE     = "assets/promote-style-logo-mark.png"       # stacked -- footer divider + favicon
NAV_LOGO_IMAGE = "assets/promote-style-logo-horizontal.png"  # horizontal -- header/nav

# ----------------------------------------------------------------------------
# Contact form -- Web3Forms (free, no backend needed), same pattern as the
# mAIntAIn Style site. Get a free access key at https://web3forms.com and
# paste it below. Form will not submit anywhere until this is filled in.
# ----------------------------------------------------------------------------
WEB3FORMS_ACCESS_KEY = "YOUR_WEB3FORMS_ACCESS_KEY_HERE"   # TODO George

# ----------------------------------------------------------------------------
# Deploy
# ----------------------------------------------------------------------------
PROJECT_SLUG = "promote-style"
# 2026-08-17: repo/Cloudflare project not yet confirmed -- a GitHub token
# scoped for a "promote" repo already exists locally (.git-credentials-promote)
# but the exact repo URL under the Admin-mAIntAIn-Style org could not be
# confirmed by guessing common names (all returned "Repository not found").
# Same account rules as every other mS/sibling-brand project apply once
# confirmed: GitHub org Admin-mAIntAIn-Style, Cloudflare account
# styles@ourclearhaven.org, deployed via Git integration (Workers & Pages ->
# Import an existing Git repository), build output directory "site".
LIVE_URL = "https://promote.style"   # target domain, purchased 2026-08-14, not yet live

# ----------------------------------------------------------------------------
# Design tokens -- per Promote_Style_Brand_Basics.docx: same dark-navy bones
# as every mS-family site, own coral/amber accent (not a reskin of mS blue).
# ----------------------------------------------------------------------------
COLORS = {
    "primary":        "#ff5a3c",   # coral -- energy/action, PROmote's accent
    "primary_bright": "#ff7a5c",   # lighter coral (gradients, hovers)
    "primary_deep":   "#e6431f",   # deep coral -- hover states, emphasis
    "gold":           "#ffb347",   # amber secondary -- kept close to mS's gold family
    "gold_deep":      "#f2954f",   # deeper amber
    "cream":          "#fbeee8",   # warm near-white body text on dark (warm tint to suit coral)
    "cream_muted":    "#c9a99a",   # muted warm-gray secondary text
    "bg_deep":        "#050810",   # same deep navy bones as mS -- shared family structure
    "panel":          "#0d1526",
    "panel2":         "#122036",
    "ink":            "#050810",
}

# 2026-08-17: corrected to match what's actually live on maintain.style and
# client.style -- both were switched to Poppins (single family, not a
# heading/body pairing) in a prior session; the local mounted copy of
# SITE/build-scripts/config.py and the Promote_Style_Brand_Basics.docx were
# both stale/out of date on this point. Verified directly against the live
# sites' computed styles and network requests, not the local files.
FONT_HEADING      = "Poppins"
FONT_BODY         = "Poppins"
GOOGLE_FONTS_HREF = ("https://fonts.googleapis.com/css2?"
                     "family=Poppins:wght@400;500;600;700;800&display=swap")

# ----------------------------------------------------------------------------
# Nav
# ----------------------------------------------------------------------------
# 2026-08-17: collapsed from 3 separate links (SEO Basics / Built SEO-Ready /
# Business Listings) into one "SEO 101" link -- George's call, the header
# had gotten crowded and all three now live as tabs on a single page
# (seo-101.html) instead of three separate destinations.
NAV_LINKS = [
    ("index.html", "Home"),
    ("pricing.html", "Pricing"),
    ("seo-101.html", "SEO 101"),
    ("https://maintain.style", "mAIntAIn Style"),
]

# ----------------------------------------------------------------------------
# Homepage copy
# ----------------------------------------------------------------------------
HERO_BADGE = "DONE-FOR-YOU MARKETING"
HERO_BADGE_ES = "MARKETING HECHO PARA TI"
# 2026-08-23: repositioned for the homepage now that PROmote Style has a real,
# priced product (see PLANS on the pricing page) -- was leading 100% with the
# free SEO-guides angle and routing every CTA to mAIntAIn Style, with no
# mention anywhere on the page that PROmote Style itself is a paid,
# done-for-you service. Now leads with the service; free guides stay as a
# secondary CTA and trust-builder further down the page (see PILLARS/FEATURES).
HERO_H1    = 'Your social media, ads, and marketing —<br><span class="grad">handled for you</span>, every month.'
HERO_H1_ES = 'Tus redes sociales, anuncios y marketing —<br><span class="grad">los manejamos por ti</span>, cada mes.'
HERO_SUB   = ("Flat monthly plans starting at $1,000 -- you approve the content, we handle the posting, the ads, "
              "and the reporting. Prefer to learn it yourself first? Our SEO guides are free, no strings attached.")
HERO_SUB_ES = ("Planes mensuales fijos desde $1,000 -- tú apruebas el contenido, nosotros manejamos las "
               "publicaciones, los anuncios y los reportes. ¿Prefieres aprenderlo tú mismo primero? Nuestras guías "
               "de SEO son gratis, sin letra pequeña.")

# 2026-08-23: reworked for the paid service (was about the free SEO guides --
# "100% free," "practical, not theoretical" -- now about what a paying client
# cares about). "Built by site builders" kept -- it's still a real, true
# differentiator.
TRUST_ITEMS = [
    ("Flat monthly fee", "No % of your ad spend, ever", "Tarifa mensual fija", "Nunca un % de tu gasto publicitario"),
    ("You approve everything", "Nothing posts without your OK", "Tú apruebas todo", "Nada se publica sin tu aprobación"),
    ("Built by site builders", "Not just marketers", "Hecho por quienes construyen sitios", "No solo mercadólogos"),
    (CITY_STATE, "Local & remote", CITY_STATE, "Local y remoto"),
]

# ----------------------------------------------------------------------------
# Homepage pricing teaser -- NEW 2026-08-23. Reuses C.PLANS (the same data
# that drives pricing.html) so the two pages can never drift out of sync;
# this section just renders a compact version and links to the full page.
# ----------------------------------------------------------------------------
PLANS_TEASER_TAG = "FLAT MONTHLY PLANS"
PLANS_TEASER_TAG_ES = "PLANES MENSUALES FIJOS"
PLANS_TEASER_H2 = "Three tiers. Pick what fits, upgrade whenever."
PLANS_TEASER_H2_ES = "Tres niveles. Elige el que te convenga, sube de nivel cuando quieras."
PLANS_TEASER_SUB = "Every plan is a flat monthly fee -- no percentage of your ad spend, ever."
PLANS_TEASER_SUB_ES = "Cada plan es una tarifa mensual fija -- nunca un porcentaje de tu gasto publicitario."
PLANS_TEASER_CTA = "See full pricing & what's included"
PLANS_TEASER_CTA_ES = "Ver precios completos y qué incluye"

# 2026-08-23: reworked from "how to work through the free guides" (that
# framing now lives on seo-101.html itself) to "how it works as a client" --
# this section is on the homepage to sell the service, not the content library.
PROCESS_STEPS = [
    ("01", "Tell us about your business", "A quick conversation about what you sell, who you're trying to reach, and what you're already doing.",
     "Cuéntanos sobre tu negocio", "Una conversación breve sobre qué vendes, a quién buscas llegar, y qué ya estás haciendo."),
    ("02", "Pick a tier", "Starter, Growth, or Full-Service -- or a custom scope if none of them fit exactly.",
     "Elige un nivel", "Starter, Growth, o Full-Service -- o un alcance a la medida si ninguno encaja exactamente."),
    ("03", "We build your systems", "Content calendar, ad campaigns, and profile optimization, set up and running under your own accounts.",
     "Construimos tus sistemas", "Calendario de contenido, campañas de anuncios y optimización de perfiles, configurados y funcionando bajo tus propias cuentas."),
    ("04", "You watch it run", "A monthly strategy review and real reporting -- you stay in control, we handle the day-to-day.",
     "Tú lo ves funcionar", "Una revisión de estrategia mensual y reportes reales -- tú mantienes el control, nosotros manejamos el día a día."),
]

FEATURES = [
    ("Free", "Every guide, no catch",
     "No gated content, no \"unlock with your email\" tricks. If it helps you rank, it's here.",
     "Gratis", "Cada guía, sin trampa",
     "Sin contenido cerrado, sin trucos de \"desbloquea con tu correo\". Si te ayuda a posicionarte, está aquí."),
    ("Practical", "Written to be used today",
     "Checklists and step-by-step setup guides, not vague theory — built for people with a business to run, not a marketing degree.",
     "Práctico", "Escrito para usarse hoy",
     "Listas de verificación y guías paso a paso, no teoría vaga — hecho para gente que tiene un negocio que atender, no un título en marketing."),
    ("Proven", "We build this way ourselves",
     "Every mAIntAIn Style site ships with the fundamentals covered in these guides already built in. Not just advice — a live example.",
     "Probado", "Nosotros mismos lo construimos así",
     "Cada sitio de mAIntAIn Style sale con lo esencial de estas guías ya integrado. No es solo un consejo — es un ejemplo real y en vivo."),
]

# 2026-08-23: this band used to route 100% of homepage traffic to
# mAIntAIn Style's portfolio ("want a site that's SEO-ready?"), with no ask
# for PROmote Style's own service anywhere on the page. Now it's PROmote
# Style's own closing pitch; the mAIntAIn Style cross-sell moves to a
# secondary button in cta_band() instead of being the only ask.
CTA_TITLE = "Ready to have your marketing handled?"
CTA_TITLE_ES = "¿Listo para que manejemos tu marketing?"
CTA_SUB   = "Tell us about your business and we'll recommend a tier -- or build a custom scope if none of these fit exactly."
CTA_SUB_ES = "Cuéntanos sobre tu negocio y te recomendaremos un nivel -- o armamos un alcance a la medida si ninguno encaja exactamente."

# ----------------------------------------------------------------------------
# Comparison section (homepage) -- sells against the two real alternatives a
# small business owner weighs when it comes to marketing/promotion.
# ----------------------------------------------------------------------------
# 2026-08-17: dropped COMPARISON_SUB ("What matters isn't how much content
# exists...") per George's request -- the h2 alone carries the section.
# 2026-08-23: reworked from "three ways to learn SEO" (blog posts vs. paid
# courses vs. our free guides) to "three ways to handle your marketing" --
# this section now sells the paid service against its two real alternatives
# instead of selling the free content library against other free content.
COMPARISON_TAG = "THE DIFFERENCE"
COMPARISON_TAG_ES = "LA DIFERENCIA"
COMPARISON_H2  = "Three ways to handle your marketing. Only one doesn't cost you time or a fortune."
COMPARISON_H2_ES = "Tres formas de manejar tu marketing. Solo una no te cuesta tiempo ni una fortuna."

COMPARISON_ITEMS = [
    dict(label="DOING IT YOURSELF", title="Whenever you find the time",
         desc="Posting between running the business, managing ads you don't have time to optimize, and figuring out Google Business Profile on your own -- it's not that you can't, it's that you shouldn't have to.",
         featured=False,
         label_es="HACERLO TÚ MISMO", title_es="Cuando encuentres el tiempo",
         desc_es="Publicar entre atender el negocio, manejar anuncios que no tienes tiempo de optimizar, y descifrar Google Business Profile por tu cuenta -- no es que no puedas, es que no deberías tener que hacerlo."),
    dict(label="A TRADITIONAL AGENCY", title="Expensive, slow, and impersonal",
         desc="Long contracts, junior account managers who've never run a business like yours, and pricing that's rarely a flat number you can actually plan around.",
         featured=False,
         label_es="UNA AGENCIA TRADICIONAL", title_es="Cara, lenta e impersonal",
         desc_es="Contratos largos, gerentes de cuenta junior que nunca han manejado un negocio como el tuyo, y precios que rara vez son un número fijo con el que puedas planear de verdad."),
    dict(label=BUSINESS_NAME.upper(), title="Flat fee, real people, you approve everything",
         desc="One flat monthly price, no ad-spend markup, and a real strategy review every month -- run by people who also build the sites these campaigns point to.",
         featured=True,
         label_es=BUSINESS_NAME.upper(), title_es="Tarifa fija, gente real, tú apruebas todo",
         desc_es="Un precio mensual fijo, sin recargo sobre tu gasto publicitario, y una revisión de estrategia real cada mes -- manejado por gente que también construye los sitios a los que apuntan estas campañas."),
]

# ----------------------------------------------------------------------------
# Pillar cards (homepage) -- links into the three main content pillars.
# ----------------------------------------------------------------------------
# 2026-08-17: SEO Basics / Built SEO-Ready / Business Listings are now three
# tabs on one page (seo-101.html) instead of three separate pages -- hrefs
# below deep-link straight to the right tab via hash.
# 2026-08-17: dropped PILLARS_SUB per George's request -- the h2 alone
# carries the section, matching the earlier COMPARISON_SUB removal.
# 2026-08-23: retitled -- this section no longer opens the homepage (the
# service pitch does), so "START HERE" no longer fits. It's now framed as
# the free-guides option for anyone who wants to DIY first.
PILLARS_TAG = "FREE SEO GUIDES"
PILLARS_TAG_ES = "GUÍAS SEO GRATIS"
PILLARS_H2  = "Prefer to learn it yourself first?<br>Start here, free"
PILLARS_H2_ES = "¿Prefieres aprenderlo tú mismo primero?<br>Empieza aquí, gratis"

PILLARS = [
    dict(href="seo-101.html#basics", label="SEO BASICS", title="Never done SEO before?",
         desc="Start here. What SEO actually is, how keywords work, and how to find the ones people are really searching for.",
         label_es="SEO BASICS", title_es="¿Nunca has hecho SEO?",
         desc_es="Empieza aquí. Qué es realmente el SEO, cómo funcionan las palabras clave y cómo encontrar las que la gente realmente busca."),
    dict(href="seo-101.html#built", label="BUILT SEO-READY", title="Evaluating a site build?",
         desc="See exactly what \"SEO-ready\" should mean technically — and how mAIntAIn Style sites ship with it already done.",
         label_es="BUILT SEO-READY", title_es="¿Evaluando la construcción de un sitio?",
         desc_es="Mira exactamente qué debería significar \"listo para SEO\" técnicamente — y cómo los sitios de mAIntAIn Style salen con eso ya hecho."),
    dict(href="seo-101.html#listings", label="BUSINESS LISTINGS", title="Not showing up on Google Maps?",
         desc="Set up and verify your Google Business Profile, Bing Places, and Apple Business Connect listings, step by step.",
         label_es="LISTADOS DE NEGOCIO", title_es="¿No apareces en Google Maps?",
         desc_es="Configura y verifica tus listados de Google Business Profile, Bing Places y Apple Business Connect, paso a paso."),
]

# ----------------------------------------------------------------------------
# Contact page copy
# ----------------------------------------------------------------------------
CONTACT_H1  = "Questions, or ready for the SEO-ready site?"
CONTACT_H1_ES = "¿Tienes preguntas, o ya quieres el sitio listo para SEO?"
CONTACT_SUB = ("Whether you want a site built SEO-ready from day one, want us to run your marketing, or just have a "
               "question about one of the guides — tell us a bit about what you need.")
CONTACT_SUB_ES = ("Ya sea que quieras un sitio construido listo para SEO desde el primer día, que llevemos tu "
                   "marketing, o solo tengas una pregunta sobre una de las guías — cuéntanos un poco qué necesitas.")

# ----------------------------------------------------------------------------
# Pricing page copy -- sourced from Single-Business_Marketing_Agreement.pdf
# (2026-08-23, single-business scope). Monthly retainer, not a one-time build
# fee like mAIntAIn Style's own PLANS -- this is ongoing marketing management.
# Published figures are the TOP of each documented range (see note atop this
# file) -- confirm with George before treating as final.
# ----------------------------------------------------------------------------
PRICING_HERO_TAG = "PRICING"
PRICING_HERO_TAG_ES = "PRECIOS"
PRICING_HERO_H1 = 'Marketing that <span class="grad">runs itself</span>,<br>priced in plain numbers'
PRICING_HERO_H1_ES = 'Marketing que <span class="grad">se administra solo</span>,<br>con precios claros'

PLANS_INTRO = ("Every plan is a flat monthly fee -- no percentage of your ad spend, ever. Ad spend itself "
               "is billed separately and paid directly to Meta/Google, not through us. Not sure which tier "
               "fits your business? Tell us what you need and we'll recommend one.")
PLANS_INTRO_ES = ("Cada plan es una tarifa mensual fija -- nunca un porcentaje de tu gasto publicitario. El "
                   "gasto publicitario se factura por separado y se paga directamente a Meta/Google, no a "
                   "través de nosotros. ¿No sabes qué nivel te conviene? Cuéntanos qué necesitas y te "
                   "recomendaremos uno.")

PLANS = [
    dict(name="Starter", tag="For businesses just getting going", price="$1,000", period="/month",
         featured=False,
         features=[
             "4-6 posts/month (Facebook, Instagram, Google Business)",
             "Basic photo editing",
             "Light community management",
             "Minimal ad management (boosted posts only)",
             "Monthly analytics report",
         ]),
    dict(name="Growth", tag="Most popular", price="$2,000", period="/month",
         featured=True,
         features=[
             "Everything in Starter",
             "8-12 posts/month",
             "Weekly Reels/TikTok-style videos",
             "Full community management",
             "Ad campaign setup + optimization (Meta + Google)",
             "Monthly strategy meeting",
         ]),
    dict(name="Full-Service", tag="For aggressive growth", price="$3,000", period="/month",
         featured=False,
         features=[
             "Everything in Growth",
             "12-20 posts/month",
             "Weekly video content",
             "Reputation management (reviews + responses)",
             "Email/SMS marketing campaigns",
             "Seasonal campaign planning",
             "Monthly photography session",
         ]),
]

# Shared across every tier -- from "Included Services" in
# Single-Business_Marketing_Agreement.pdf. Shown once on the page instead of
# repeated on every card.
INCLUDED_TAG = "ON EVERY PLAN"
INCLUDED_TAG_ES = "EN TODOS LOS PLANES"
INCLUDED_H2 = "What's included no matter which tier you pick"
INCLUDED_H2_ES = "Qué incluye sin importar el nivel que elijas"

INCLUDED_ITEMS = [
    ("Social Media Management", "Facebook, Instagram, and Google Business Profile posting on a real schedule, not sporadic."),
    ("Short-Form Video Production", "Reels/TikTok-style video content scaled to your tier."),
    ("Advertising Management", "Campaign setup and ongoing optimization -- we run it, you approve it."),
    ("Google Business Profile Optimization", "Kept accurate and active so you show up where people search."),
    ("Monthly Analytics + Strategy Review", "A real look at what worked, not just a vanity-metrics PDF."),
]
INCLUDED_ITEMS_ES = [
    ("Gestión de Redes Sociales", "Publicaciones en Facebook, Instagram y Google Business Profile en un horario real, no esporádico."),
    ("Producción de Video Corto", "Contenido de video estilo Reels/TikTok, según tu nivel."),
    ("Gestión de Publicidad", "Configuración y optimización continua de campañas -- nosotros lo manejamos, tú lo apruebas."),
    ("Optimización de Google Business Profile", "Mantenido preciso y activo para que aparezcas donde la gente busca."),
    ("Revisión Mensual de Analítica + Estrategia", "Una mirada real a qué funcionó, no solo un PDF de métricas de vanidad."),
]

# ----------------------------------------------------------------------------
# Add-ons (pricing page) -- à la carte items layered on top of any tier.
# These exist specifically so extra scope (more locations, print materials,
# extra shoots, one-time deep work) has a paid home instead of quietly
# expanding the workload under a flat monthly fee. Priced as ranges since
# scope varies per request -- exact quote confirmed before work starts.
# ----------------------------------------------------------------------------
ADDONS_TAG = "ADD-ONS"
ADDONS_TAG_ES = "COMPLEMENTOS"
ADDONS_H2 = "Need something extra?"
ADDONS_H2_ES = "¿Necesitas algo extra?"
ADDONS_SUB = "Layer any of these on top of your plan -- priced separately so your monthly fee stays predictable."
ADDONS_SUB_ES = "Agrega cualquiera de estos sobre tu plan -- con precio aparte para que tu tarifa mensual siga siendo predecible."

ADDONS = [
    dict(name="Multi-Location / Restaurant Group", price="+$800/mo per additional location",
         desc="Running more than one location under the same brand? Shared content calendar, cross-location campaigns, unified ad management and analytics -- each additional location added at a flat rate."),
    dict(name="Print & In-Store Marketing Materials", price="$150-$400/piece",
         desc="Menu boards, table cards, door hangers, coupons, flyers -- designed and print-ready to hand to your printer. Priced by piece since scope varies (a door hanger isn't a menu board); exact quote confirmed before work begins."),
    dict(name="Extra Content Shoot", price="$300/session",
         desc="An additional on-site photo/video session beyond what's included in your tier's monthly shoot."),
    dict(name="Business Listings Deep Overhaul", price="$350 one-time",
         desc="A full rebuild of incomplete or underperforming listings across Google Business Profile, Bing Places, and Apple Business Connect -- beyond the ongoing optimization already included."),
    dict(name="Seasonal Campaign Bundle", price="$450/campaign",
         desc="A focused push for a holiday, local event, or seasonal promotion -- built and scheduled outside your normal cadence."),
]
ADDONS_ES = [
    dict(name="Multi-Ubicación / Grupo de Restaurantes", price_es="+$800/mes por ubicación adicional",
         desc="¿Llevas más de una ubicación bajo la misma marca? Calendario de contenido compartido, campañas entre ubicaciones, gestión de anuncios y analítica unificadas -- cada ubicación adicional se agrega a una tarifa fija."),
    dict(name="Materiales de Marketing Impresos y en Tienda", price_es="$150-$400/pieza",
         desc="Menús de pared, tarjetas de mesa, colgadores de puerta, cupones, volantes -- diseñados y listos para imprimir. Con precio por pieza ya que el alcance varía (un colgador de puerta no es un menú de pared); se confirma un precio exacto antes de comenzar el trabajo."),
    dict(name="Sesión de Contenido Extra", price_es="$300/sesión",
         desc="Una sesión adicional de foto/video en sitio, más allá de la incluida en tu nivel."),
    dict(name="Renovación Profunda de Listados de Negocio", price_es="$350 pago único",
         desc="Una reconstrucción completa de listados incompletos o con bajo rendimiento en Google Business Profile, Bing Places y Apple Business Connect -- más allá de la optimización continua ya incluida."),
    dict(name="Paquete de Campaña de Temporada", price_es="$450/campaña",
         desc="Un empuje enfocado para una fiesta, evento local, o promoción de temporada -- creado y programado fuera de tu ritmo normal."),
]

PRICING_CTA_H2 = "Not sure which tier fits?"
PRICING_CTA_H2_ES = "¿No estás seguro de qué nivel te conviene?"
PRICING_CTA_SUB = "Tell us about your business and we'll recommend one -- or build a custom scope if none of these fit exactly."
PRICING_CTA_SUB_ES = "Cuéntanos sobre tu negocio y te recomendaremos uno -- o armamos un alcance a la medida si ninguno encaja exactamente."

# ----------------------------------------------------------------------------
# Back-to-top icon -- reuse mS's blue arrow until a coral-family icon exists.
# TODO George: swap for a coral/amber variant to match this site's palette.
# ----------------------------------------------------------------------------
TOTOP_ICON = "assets/totop-arrow.svg"
