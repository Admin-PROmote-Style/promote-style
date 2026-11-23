# -*- coding: utf-8 -*-
"""
config.py -- single source of truth for the PROmote Style site.
Edit facts/copy here, then run build_all.py. Never hand-edit the generated
.html files.

Visible copy is the Chair's text from 2026-11-22 23:31 PT. Do not add lines.
"""

BUSINESS_NAME = "PROmote Style"
EMAIL         = "promote@maintain.style"
CITY_STATE    = "Bend, Oregon"

LOGO_IMAGE     = "assets/promote-style-logo-mark.png"
NAV_LOGO_IMAGE = "assets/promote-style-logo-horizontal.png"

WEB3FORMS_ACCESS_KEY = "3856a294-ecef-4bd8-8a8c-68fd92e47037"   # live 2026-08-24 -- separate, dedicated Web3Forms account tied to promote@maintain.style, distinct from George's OCH account

PROJECT_SLUG = "promote-style"
LIVE_URL = "https://promote.style"

COLORS = {
    "primary":        "#ff5a3c",
    "primary_bright": "#ff7a5c",
    "primary_deep":   "#e6431f",
    "gold":           "#ffb347",
    "gold_deep":      "#f2954f",
    "cream":          "#fbeee8",
    "cream_muted":    "#c9a99a",
    "bg_deep":        "#050810",
    "panel":          "#0d1526",
    "panel2":         "#122036",
    "ink":            "#050810",
}

FONT_HEADING      = "Poppins"
FONT_BODY         = "Poppins"
GOOGLE_FONTS_HREF = ("https://fonts.googleapis.com/css2?"
                     "family=Poppins:wght@400;500;600;700;800&display=swap")

NAV_LINKS = [
    ("index.html", "Home"),
    ("pricing.html", "Pricing"),
    ("seo-101.html", "SEO 101"),
    ("https://maintain.style", "mAIntAIn Style"),
    ("https://client.style", "Client Style"),
]

PAGE_TITLE = "PROmote Style | Your Own AI Marketing Team"
META_DESC = ("AI bots that post to social media, reply to reviews, handle your inbox, "
             "and update your website. One-time setup, no monthly fees from us.")

HERO_H1 = "Your own AI marketing team."
HERO_SUB = ("PROmote Style sets up a team of AI bots that keep your business visible: "
            "posting to social media, replying to reviews, handling your inbox, and "
            "keeping your website up to date. You stay in control.")
HERO_PRIMARY = "See the packages"
HERO_SECONDARY = "Free marketing guides"

BENEFITS = [
    ("Always on.", "Your bots work every day, even when you're busy running your business."),
    ("You approve everything.", "Nothing goes public without your OK."),
    ("Yours to keep.", "Your accounts, your bots, your content. No lock-in."),
]

BOTS_H2 = "Meet your Bot Office"
BOTS_SUB = ("Four helpers that take routine work off your plate, so you can focus on running your business.")
BOTS_CLOSE = ("You stay in control. Your bots draft, suggest, and prepare; nothing goes public without your OK.")
BOTS = [
    dict(name="Social Bot",
         promise="Never stare at a blank post again.",
         intro="Your Social Bot is your creative partner for social media. It helps you come up with ideas, write posts, and keep a steady schedule.",
         does=[
             "Brainstorms post ideas around your products, events, promotions, and seasons",
             "Writes captions in your brand's voice, ready to use or tweak",
             "Turns one idea into versions for different platforms",
             "Suggests hashtags, timing, and calls to action",
             "Plans a content calendar so you're never scrambling",
             "Posts to X automatically on your schedule, once you approve",
         ],
         you_get="Fresh, on-brand posts every week without the writer's block."),
    dict(name="Reviews Bot",
         promise="Every review gets a thoughtful reply.",
         intro="Reviews shape how new customers see you. Your Reviews Bot makes sure no one is ignored.",
         does=[
             "Drafts warm thank-yous for happy customers",
             "Writes calm, professional responses to complaints",
             "Flags reviews that need your personal attention",
             "Spots patterns in what customers praise or complain about",
         ],
         you_get="A reputation that shows you care, in minutes instead of hours."),
    dict(name="Inbox Bot",
         promise="Nothing important slips through.",
         intro="Your Inbox Bot reads through the noise and surfaces what matters.",
         does=[
             "Sorts customer emails, inquiries, and orders from the clutter",
             "Drafts clear replies for you to review and send",
             "Highlights time-sensitive messages first",
             "Summarizes your inbox so you can catch up fast",
         ],
         you_get="Faster responses and fewer missed opportunities."),
    dict(name="Website Bot",
         promise="Update your website by just asking.",
         intro="Powered by Client Style, your Website Bot keeps your site current without a developer.",
         does=[
             "Updates hours, prices, specials, and announcements in plain words",
             "Adds new photos, products, and pages",
             "Keeps your information consistent and accurate",
             "Every change waits for your approval before going live",
         ],
         you_get="A website that's always up to date, without the hassle."),
]

PACKAGES_H2 = "Simple packages. One-time setup."
PACKAGES_SUB = "No monthly fees from us."
PACKAGES_NOTE = "Your only ongoing cost is your own Cursor plan, billed directly by Cursor."

PLANS = [
    dict(name="Basic Bot Office", price="$500", tag="", featured=False, features=[
        "Social, Reviews, Inbox, and Website bots",
        "Guided account setup",
        "Walkthrough on running your bots",
    ]),
    dict(name="Advanced Bot Office", price="$1,000", tag="", featured=False, features=[
        "Everything in Basic",
        "Bots customized for your type of business",
        "Extra automations for specials, updates, and events",
    ]),
    dict(name="Full Basic Package", price="$750", tag="", featured=False, features=[
        "Basic website by mAIntAIn Style",
        "Basic Bot Office",
    ]),
    dict(name="Full Advanced Package", price="$1,500", tag="Best value", featured=True, features=[
        "Advanced website by mAIntAIn Style",
        "Advanced Bot Office",
    ]),
]

SUPPORT_H2 = "Support that's included"
SUPPORT = [
    "90 days of fixes and tweaks included with every package",
    "After that, fixes start at $75",
    "Bot Office upgrades with the latest features: $500",
]

STEPS_H2 = "How it works"
STEPS = [
    ("01", "Talk with us.", "Tell us about your business and goals."),
    ("02", "Choose your package.", "Bot Office alone, or bundled with a new website."),
    ("03", "We set it all up.", "Accounts, bots, and testing, done for you."),
    ("04", "You're in control.", "Ask your bots for what you need and approve what goes out."),
]

TOOLS_H2 = "Works with your favorite tools"
TOOLS_LEAD = "Want to reach Facebook and Instagram too? Your Bot Office pairs well with tools like Buffer and Metricool."

GUIDES_H2 = "Learn it yourself, free."
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

FAQ_H2 = "FAQ"
FAQ = [
    ("Do I have to post anything myself?",
     "No. Your bots prepare posts and replies; you just approve them."),
    ("Are there monthly fees?",
     "Not from us. You only pay for your own Cursor plan."),
    ("What if I need help later?",
     "Every package includes 90 days of fixes. After that, fixes start at $75."),
    ("Do I need a new website?",
     "No, but your bots can do the most with a mAIntAIn Style website."),
]

CTA_TITLE = "Ready to meet your AI marketing team?"
CTA_SUB = "Tell us about your business and we'll recommend the right package."
CTA_BUTTON = "Get started"

FOOTER_LINE = "PROmote Style — a mAIntAIn Style company. Bend, Oregon."

TOTOP_ICON = "assets/totop-arrow.svg"
