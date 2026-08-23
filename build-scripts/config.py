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
HERO_BADGE = "FREE SEO RESOURCES, NO STRINGS"
HERO_BADGE_ES = "RECURSOS SEO GRATIS, SIN LETRA PEQUEÑA"
# 2026-08-17: shortened per George's exact wording -- was "The most useful
# SEO resource on the internet -- built by people who actually build
# SEO-ready sites," which read as too much text / too promotional for an
# education-first site.
HERO_H1    = 'FREE <span class="grad">SEO resources</span><br>built by people who build<br><span class="grad">SEO-ready sites</span>.'
HERO_H1_ES = 'Recursos <span class="grad">SEO gratis</span><br>hechos por gente que construye<br><span class="grad">sitios listos para SEO</span>.'
HERO_SUB   = ("Real tips, real keyword research, real setup guides — free. No email wall, no drip "
              "campaign. If you like what you learn here, ask us about a site built this way from day one.")
HERO_SUB_ES = ("Consejos reales, investigación de palabras clave real, guías de configuración reales — gratis. "
               "Sin muro de correo, sin campaña de goteo. Si te sirve lo que aprendes aquí, pregúntanos por un "
               "sitio construido así desde el primer día.")

TRUST_ITEMS = [
    ("100% free", "No paywall on any guide", "100% gratis", "Ninguna guía tiene muro de pago"),
    ("Practical, not theoretical", "Steps you can do today", "Práctico, no teórico", "Pasos que puedes hacer hoy"),
    ("Built by site builders", "Not just marketers", "Hecho por quienes construyen sitios", "No solo mercadólogos"),
    (CITY_STATE, "Local & remote", CITY_STATE, "Local y remoto"),
]

PROCESS_STEPS = [
    ("01", "Learn the basics", "Start with SEO Basics — keywords, search intent, and the fundamentals in plain English.",
     "Aprende lo básico", "Empieza con SEO Basics — palabras clave, intención de búsqueda y lo esencial en español claro."),
    ("02", "See it done right", "Built SEO-Ready shows exactly what a properly-built site includes, with real examples.",
     "Mira cómo se hace bien", "Built SEO-Ready muestra exactamente qué incluye un sitio bien construido, con ejemplos reales."),
    ("03", "Claim your listings", "Set up Google Business Profile, Bing Places, and the rest so you show up where people search.",
     "Reclama tus listados", "Configura Google Business Profile, Bing Places y el resto para que aparezcas donde la gente busca."),
    ("04", "Get help if you want it", "Keep learning free, or let us build the SEO-ready site (or run the marketing) for you.",
     "Pide ayuda si la quieres", "Sigue aprendiendo gratis, o deja que construyamos el sitio listo para SEO (o llevemos tu marketing) por ti."),
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

CTA_TITLE = "Want a site that's SEO-ready before it even launches?"
CTA_TITLE_ES = "¿Quieres un sitio listo para SEO antes de que siquiera se lance?"
CTA_SUB   = "mAIntAIn Style builds sites with the fundamentals from these guides baked in from day one — schema, sitemap, speed, structure, all of it. See what that actually looks like."
CTA_SUB_ES = ("mAIntAIn Style construye sitios con lo esencial de estas guías integrado desde el primer día — "
              "schema, sitemap, velocidad, estructura, todo. Mira cómo se ve eso en la práctica.")

# ----------------------------------------------------------------------------
# Comparison section (homepage) -- sells against the two real alternatives a
# small business owner weighs when it comes to marketing/promotion.
# ----------------------------------------------------------------------------
# 2026-08-17: dropped COMPARISON_SUB ("What matters isn't how much content
# exists...") per George's request -- the h2 alone carries the section.
COMPARISON_TAG = "THE DIFFERENCE"
COMPARISON_TAG_ES = "LA DIFERENCIA"
COMPARISON_H2  = "Three ways to learn SEO. Only one doesn't waste your time."
COMPARISON_H2_ES = "Tres formas de aprender SEO. Solo una no te hace perder el tiempo."

COMPARISON_ITEMS = [
    dict(label="RANDOM BLOG POSTS", title="Outdated, contradictory, vague",
         desc="Search \"how to do SEO\" and get a thousand takes, half from 2019, most written to rank for the term rather than actually explain it.",
         featured=False,
         label_es="ARTÍCULOS DE BLOG AL AZAR", title_es="Desactualizados, contradictorios, vagos",
         desc_es="Busca \"cómo hacer SEO\" y encuentra mil opiniones distintas, la mitad de 2019, la mayoría escritas para posicionarse por el término en vez de explicarlo de verdad."),
    dict(label="PAID SEO COURSES", title="Locked behind a price tag",
         desc="The good information exists — behind a $200 course or a \"book a call\" wall before you've learned anything at all.",
         featured=False,
         label_es="CURSOS DE SEO DE PAGO", title_es="Encerrados detrás de un precio",
         desc_es="La buena información existe — detrás de un curso de $200 o un muro de \"agenda una llamada\" antes de que hayas aprendido algo siquiera."),
    dict(label=BUSINESS_NAME.upper(), title="Free, current, and provable",
         desc="Every guide here is free and written by people who build SEO-ready sites for a living — and who'll show you exactly what that looks like, not just tell you.",
         featured=True,
         label_es=BUSINESS_NAME.upper(), title_es="Gratis, actual y demostrable",
         desc_es="Cada guía aquí es gratis y está escrita por gente que construye sitios listos para SEO para vivir — y que te va a mostrar exactamente cómo se ve eso, no solo contártelo."),
]

# ----------------------------------------------------------------------------
# Pillar cards (homepage) -- links into the three main content pillars.
# ----------------------------------------------------------------------------
# 2026-08-17: SEO Basics / Built SEO-Ready / Business Listings are now three
# tabs on one page (seo-101.html) instead of three separate pages -- hrefs
# below deep-link straight to the right tab via hash.
# 2026-08-17: dropped PILLARS_SUB per George's request -- the h2 alone
# carries the section, matching the earlier COMPARISON_SUB removal.
PILLARS_TAG = "START HERE"
PILLARS_TAG_ES = "EMPIEZA AQUÍ"
PILLARS_H2  = "One page, three tabs<br>Pick your starting point"
PILLARS_H2_ES = "Una página, tres pestañas<br>Elige tu punto de partida"

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
    dict(name="Starter", tag="For businesses just getting going", price="$900", period="/month",
         featured=False,
         features=[
             "4-6 posts/month (Facebook, Instagram, Google Business)",
             "Basic photo editing",
             "Light community management",
             "Minimal ad management (boosted posts only)",
             "1-2 website updates/month",
             "Monthly analytics report",
         ]),
    dict(name="Growth", tag="Most popular", price="$1,500", period="/month",
         featured=True,
         features=[
             "Everything in Starter",
             "8-12 posts/month",
             "Weekly Reels/TikTok-style videos",
             "Full community management",
             "Ad campaign setup + optimization (Meta + Google)",
             "2-4 website updates/month",
             "Monthly strategy meeting",
         ]),
    dict(name="Full-Service", tag="For aggressive growth", price="$2,500", period="/month",
         featured=False,
         features=[
             "Everything in Growth",
             "12-20 posts/month",
             "Weekly video content",
             "Reputation management (reviews + responses)",
             "Email/SMS marketing campaigns",
             "Seasonal campaign planning",
             "Monthly photography session",
             "Unlimited website updates",
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
    ("Website Updates", "Menu changes, hours, promos, new photos -- handled for you every month."),
    ("Google Business Profile Optimization", "Kept accurate and active so you show up where people search."),
    ("Monthly Analytics + Strategy Review", "A real look at what worked, not just a vanity-metrics PDF."),
]
INCLUDED_ITEMS_ES = [
    ("Gestión de Redes Sociales", "Publicaciones en Facebook, Instagram y Google Business Profile en un horario real, no esporádico."),
    ("Producción de Video Corto", "Contenido de video estilo Reels/TikTok, según tu nivel."),
    ("Gestión de Publicidad", "Configuración y optimización continua de campañas -- nosotros lo manejamos, tú lo apruebas."),
    ("Actualizaciones del Sitio Web", "Cambios de menú, horarios, promociones, fotos nuevas -- gestionado por nosotros cada mes."),
    ("Optimización de Google Business Profile", "Mantenido preciso y activo para que aparezcas donde la gente busca."),
    ("Revisión Mensual de Analítica + Estrategia", "Una mirada real a qué funcionó, no solo un PDF de métricas de vanidad."),
]

# ----------------------------------------------------------------------------
# Add-ons (pricing page) -- Multi-Location/Restaurant Group upgrade, sourced
# from the same doc. Shown as a range, not a flat figure, since scope
# genuinely varies with number of locations (unlike the three core tiers).
# ----------------------------------------------------------------------------
ADDONS_TAG = "ADD-ON"
ADDONS_TAG_ES = "COMPLEMENTO"
ADDONS_H2 = "Running more than one location?"
ADDONS_H2_ES = "¿Llevas más de una ubicación?"
ADDONS_SUB = "Layer this on top of any single-business tier above."
ADDONS_SUB_ES = "Agrega esto sobre cualquier nivel de negocio individual de arriba."

ADDON_MULTI_LOCATION = dict(
    name="Multi-Location / Restaurant Group Add-On", price="+$1,200-$2,000", period="/month",
    features=[
        "Cross-brand content calendar",
        "Shared campaigns across locations",
        "Multi-location ad management",
        "Unified Google Business optimization",
        "Website updates across all locations",
        "Group analytics + strategy",
    ],
)
ADDON_MULTI_LOCATION_ES = dict(
    name="Complemento Multi-Ubicación / Grupo de Restaurantes",
    features=[
        "Calendario de contenido entre marcas",
        "Campañas compartidas entre ubicaciones",
        "Gestión de anuncios multi-ubicación",
        "Optimización unificada de Google Business",
        "Actualizaciones del sitio en todas las ubicaciones",
        "Analítica y estrategia grupal",
    ],
)

PRICING_CTA_H2 = "Not sure which tier fits?"
PRICING_CTA_H2_ES = "¿No estás seguro de qué nivel te conviene?"
PRICING_CTA_SUB = "Tell us about your business and we'll recommend one -- or build a custom scope if none of these fit exactly."
PRICING_CTA_SUB_ES = "Cuéntanos sobre tu negocio y te recomendaremos uno -- o armamos un alcance a la medida si ninguno encaja exactamente."

# ----------------------------------------------------------------------------
# Back-to-top icon -- reuse mS's blue arrow until a coral-family icon exists.
# TODO George: swap for a coral/amber variant to match this site's palette.
# ----------------------------------------------------------------------------
TOTOP_ICON = "assets/totop-arrow.svg"
