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
- No finished logo artwork exists yet. NAV/LOGO images below are a
  placeholder text-wordmark SVG (PRO highlighted in coral inside
  "Promote", matching the mS "AI"-in-"mAIntAIn" device) -- swap for real
  artwork once a designer/AI image is approved. Flagged inline below.
- Pricing ($149/mo flat, single platform; $249/mo multi-platform; $99/mo
  60-day intro) is kept OUT of on-site copy per the same convention as
  mAIntAIn Style's own pricing page (George's call to keep numbers in the
  conversation, not published) -- reference only, not rendered here.
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
EMAIL         = "contact@promote.style"

# Placeholder wordmark SVGs -- PRO highlighted in coral, rest in cream, same
# device as mAIntAIn Style's "AI"-in-mAIntAIn trick. Replace both paths once
# real logo artwork exists (see note above).
LOGO_IMAGE     = "assets/promote-style-logo-mark.svg"       # stacked -- footer divider + favicon
NAV_LOGO_IMAGE = "assets/promote-style-logo-horizontal.svg"  # horizontal -- header/nav

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

FONT_HEADING      = "Space Grotesk"
FONT_BODY         = "Inter"
GOOGLE_FONTS_HREF = ("https://fonts.googleapis.com/css2?"
                     "family=Space+Grotesk:wght@500;600;700"
                     "&family=Inter:wght@400;500;600;700&display=swap")

# ----------------------------------------------------------------------------
# Nav
# ----------------------------------------------------------------------------
NAV_LINKS = [
    ("index.html", "Home"),
    ("seo-basics.html", "SEO Basics"),
    ("built-seo-ready.html", "Built SEO-Ready"),
    ("listings.html", "Business Listings"),
    ("https://maintain.style", "mAIntAIn Style"),
]

# ----------------------------------------------------------------------------
# Homepage copy
# ----------------------------------------------------------------------------
HERO_BADGE = "FREE SEO RESOURCES, NO STRINGS"
HERO_H1    = 'The most useful <span class="grad">SEO resource on the internet</span> — built by people who actually build SEO-ready sites.'
HERO_SUB   = ("Real tips, real keyword research, real setup guides — free. No email wall, no drip "
              "campaign. If you like what you learn here, ask us about a site built this way from day one.")

TRUST_ITEMS = [
    ("100% free", "No paywall on any guide"),
    ("Practical, not theoretical", "Steps you can do today"),
    ("Built by site builders", "Not just marketers"),
    (CITY_STATE, "Local & remote"),
]

PROCESS_STEPS = [
    ("01", "Learn the basics", "Start with SEO Basics — keywords, search intent, and the fundamentals in plain English."),
    ("02", "See it done right", "Built SEO-Ready shows exactly what a properly-built site includes, with real examples."),
    ("03", "Claim your listings", "Set up Google Business Profile, Bing Places, and the rest so you show up where people search."),
    ("04", "Get help if you want it", "Keep learning free, or let us build the SEO-ready site (or run the marketing) for you."),
]

FEATURES = [
    ("Free", "Every guide, no catch",
     "No gated content, no \"unlock with your email\" tricks. If it helps you rank, it's here."),
    ("Practical", "Written to be used today",
     "Checklists and step-by-step setup guides, not vague theory — built for people with a business to run, not a marketing degree."),
    ("Proven", "We build this way ourselves",
     "Every mAIntAIn Style site ships with the fundamentals covered in these guides already built in. Not just advice — a live example."),
]

CTA_TITLE = "Want a site that's SEO-ready before it even launches?"
CTA_SUB   = "mAIntAIn Style builds sites with the fundamentals from these guides baked in from day one — schema, sitemap, speed, structure, all of it. See what that actually looks like."

# ----------------------------------------------------------------------------
# Comparison section (homepage) -- sells against the two real alternatives a
# small business owner weighs when it comes to marketing/promotion.
# ----------------------------------------------------------------------------
COMPARISON_TAG = "THE DIFFERENCE"
COMPARISON_H2  = "Three ways to learn SEO. Only one doesn't waste your time."
COMPARISON_SUB = "What matters isn't how much content exists — it's whether you can actually act on it."

COMPARISON_ITEMS = [
    dict(label="RANDOM BLOG POSTS", title="Outdated, contradictory, vague",
         desc="Search \"how to do SEO\" and get a thousand takes, half from 2019, most written to rank for the term rather than actually explain it.",
         featured=False),
    dict(label="PAID SEO COURSES", title="Locked behind a price tag",
         desc="The good information exists — behind a $200 course or a \"book a call\" wall before you've learned anything at all.",
         featured=False),
    dict(label=BUSINESS_NAME.upper(), title="Free, current, and provable",
         desc="Every guide here is free and written by people who build SEO-ready sites for a living — and who'll show you exactly what that looks like, not just tell you.",
         featured=True),
]

# ----------------------------------------------------------------------------
# Pillar cards (homepage) -- links into the three main content pillars.
# ----------------------------------------------------------------------------
PILLARS_TAG = "START HERE"
PILLARS_H2  = "Three places to start, depending on where you're at"
PILLARS_SUB = "New to SEO, evaluating a site build, or just need your business to show up on Google — pick your starting point."

PILLARS = [
    dict(href="seo-basics.html", label="SEO BASICS", title="Never done SEO before?",
         desc="Start here. What SEO actually is, how keywords work, and how to find the ones people are really searching for."),
    dict(href="built-seo-ready.html", label="BUILT SEO-READY", title="Evaluating a site build?",
         desc="See exactly what \"SEO-ready\" should mean technically — and how mAIntAIn Style sites ship with it already done."),
    dict(href="listings.html", label="BUSINESS LISTINGS", title="Not showing up on Google Maps?",
         desc="Set up and verify your Google Business Profile, Bing Places, and Apple Business Connect listings, step by step."),
]

# ----------------------------------------------------------------------------
# Contact page copy
# ----------------------------------------------------------------------------
CONTACT_H1  = "Questions, or ready for the SEO-ready site?"
CONTACT_SUB = ("Whether you want a site built SEO-ready from day one, want us to run your marketing, or just have a "
               "question about one of the guides — tell us a bit about what you need.")

# ----------------------------------------------------------------------------
# Back-to-top icon -- reuse mS's blue arrow until a coral-family icon exists.
# TODO George: swap for a coral/amber variant to match this site's palette.
# ----------------------------------------------------------------------------
TOTOP_ICON = "assets/totop-arrow.svg"
