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

ADV_H2 = "Advanced Bot Office"
ADV_SUB = "Everything in Basic, plus a full team of specialist bots."
ADV_INTRO = ("Every business is different. With the Advanced Bot Office, you get every specialist bot below, "
             "set up around how your business runs, plus monthly updates that keep your Bot Office growing.")
ADV_BOTS = [
    dict(name="Finance Bot",
         promise="Know where your money goes.",
         does=[
             "Organizes receipts, invoices, and bills",
             "Flags unusual charges and upcoming due dates",
             "Summarizes weekly sales and spending in plain words",
             "Prepares tidy records for your bookkeeper or accountant",
         ],
         you_get="A clear picture of your finances without digging through paperwork."),
    dict(name="Competition Bot",
         promise="Stay one step ahead.",
         does=[
             "Watches competitors' websites, prices, and promotions",
             "Tracks what they post and how customers respond",
             "Spots new businesses opening nearby",
             "Sends you a short weekly summary of what changed",
         ],
         you_get="Market awareness without spending hours researching."),
    dict(name="Events & Promotions Bot",
         promise="Fill your calendar and your seats.",
         does=[
             "Plans specials, sales, and seasonal promotions",
             "Writes announcements for your website, email, and social posts",
             "Reminds you ahead of holidays and local events",
             "Tracks which promotions worked best",
         ],
         you_get="Promotions that are planned ahead, not thrown together last minute."),
    dict(name="Customer Care Bot",
         promise="Keep customers coming back.",
         does=[
             "Drafts follow-ups and thank-you messages",
             "Answers common questions about hours, services, and policies",
             "Collects feedback and highlights what to improve",
             "Reminds you to reach out to regulars",
         ],
         you_get="Loyal customers who feel remembered."),
    dict(name="Scheduling Bot",
         promise="Your calendar, under control.",
         does=[
             "Keeps track of appointments, bookings, and deadlines",
             "Sends reminders so nothing is missed",
             "Drafts schedules and shift plans for your review",
             "Warns you about conflicts before they happen",
         ],
         you_get="Fewer surprises and smoother days."),
    dict(name="Reports Bot",
         promise="Your business at a glance.",
         does=[
             "Pulls together sales, reviews, social, and website activity",
             "Delivers a simple weekly or monthly report",
             "Highlights what's up, what's down, and what to watch",
             "Suggests next steps in plain words",
         ],
         you_get="Better decisions with less guesswork."),
]
ADV_UPDATES_H = "Your Bot Office keeps getting better."
ADV_UPDATES_P = ("Every month you'll get an email with what's new, fresh ideas for your business, "
                 "and ready-to-use prompts that switch on new bots and features. Just copy, paste, "
                 "and your Bot Office does the rest.")
ADV_UPDATES = [
    "New bots and features as they're released",
    "Seasonal ideas and quick wins",
    "Ready-to-paste prompts to put them to work",
    "Tips to get more from every bot",
]
ADV_CLOSE = "Don't see what you need? We'll design a bot around it."
ADV_BUTTON = "Talk with us"

PACKAGES_H2 = "Simple packages. One-time setup."
PACKAGES_SUB = "No monthly fees from us."
PACKAGES_NOTE = "Your only ongoing cost is your own Cursor plan, billed directly by Cursor."

PLANS = [
    dict(name="Basic Bot Office", price="$500", tag="", featured=False, features=[
        "Social, Reviews, Inbox, and Website bots",
        "Guided account setup",
        "Walkthrough on running your bots",
    ], note=("Website Bot: update your site by chatting with your bots. "
             "It works on any website you own. Sites built by mAIntAIn Style also come with the Client Style editor.")),
    dict(name="Advanced Bot Office", price="$1,000", tag="", featured=False, features=[
        "Everything in Basic",
        "Every specialist bot: Finance, Competition, Events & Promotions, Customer Care, Scheduling, and Reports",
        "A planning session to set each bot up for your business",
        "Custom automations for your routine tasks",
        "Monthly Bot Office updates with new bots and ready-to-use prompts",
    ]),
    dict(name="Full Basic Package", price="$750", tag="", featured=False, features=[
        "Basic website by mAIntAIn Style",
        "Basic Bot Office",
    ]),
    dict(name="Full Advanced Package", price="$1,500", tag="Best value", featured=True, features=[
        "Advanced website by mAIntAIn Style",
        "Advanced Bot Office with every specialist bot",
        "Monthly Bot Office updates",
    ]),
    dict(name="Full Custom Package", price="$2,500", tag="", featured=False, features=[
        "Custom website by mAIntAIn Style, with custom logo design and everything in the Custom Website plan",
        "Advanced Bot Office with every specialist bot",
        "Monthly Bot Office updates",
    ]),
]

PRICING_SUPPORT = [
    "90 days of fixes and tweaks with every package. In a bundle, your website and your Bot Office each get their own 90 days, starting when each one launches.",
    "After that, fixes start at $75.",
    "Bot Office upgrade with the latest bots and features: $500. We rebuild your whole Bot Office with everything new. This also moves a Basic Bot Office up to Advanced.",
    "Fixes needed because of Client Style updates are always free.",
]
BUNDLE_NOTE = ("Already have a mAIntAIn Style website? Add a Bot Office within 90 days of your site's launch "
               "and you still get the bundle price.")
PRICES_UPDATED = "Prices updated November 2026."

SUPPORT_H2 = "Support that's included"
SUPPORT = [
    "90 days of fixes and tweaks with every package. In a bundle, your website and your Bot Office each get their own 90 days, starting when each one launches.",
    "After that, fixes start at $75.",
    "Bot Office upgrade with the latest bots and features: $500. We rebuild your whole Bot Office with everything new. This also moves a Basic Bot Office up to Advanced.",
    "Fixes needed because of Client Style updates are always free.",
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
    ("Do you manage my social media or ads?",
     "No. Your bots draft posts and replies, and the tools you choose publish them only after you approve. We set everything up and support our setup work."),
    ("How do I get new bots and features?",
     "Every month we email you updates, ideas, and ready-to-use prompts to switch on new bots. Copy, paste, and your Bot Office does the rest."),
    ("Are there monthly fees?",
     "Not from us. You only pay for your own Cursor plan."),
    ("What if I need help later?",
     "Every package includes 90 days of fixes, and bundles get a separate 90 days for the website and the Bot Office. After that, fixes start at $75."),
    ("Do I need a new website?",
     "No, but your bots can do the most with a mAIntAIn Style website."),
    ("Who is responsible for Cursor and the other tools?",
     "Each tool is run by its own company, and you hold the account directly. We set everything up and support our setup work, but we don't control those services. See our Service Disclaimer for details."),
]

PRICING_TITLE = "Bot Office Pricing | One-Time Setup, No Monthly Fees From Us | PROmote Style"
PRICING_DESC = ("Basic Bot Office $500, Advanced Bot Office $1,000, or bundle a new website from $750. "
                "One-time setup, no monthly fees from us.")
CONTACT_TITLE = "Contact PROmote Style | Set Up Your Bot Office"
CONTACT_DESC = "Tell us about your business and we'll recommend the right Bot Office package. Based in Bend, Oregon."
PRIVACY_TITLE = "Privacy | PROmote Style"
PRIVACY_DESC = "What PROmote Style collects when you contact us, and how it is used."

DISCLAIMER = [
    "PROmote Style, a mAIntAIn Style company, provides a one-time setup service. We help you create your own accounts and configure AI bots and related tools for your business. We also provide the support described on this site: 90 days of included fixes, paid fixes after that, optional upgrades, and monthly update emails.",
    "Your accounts are yours. Cursor, X, Buffer, Metricool, and any other third-party services you use are owned and operated by their own companies. You sign up for them directly, agree to their terms, and pay them directly. PROmote Style is not affiliated with, endorsed by, or acting on behalf of any of them.",
    "We are not responsible for third-party services. This includes their availability, outages, pricing, plan or feature changes, policies, data handling, security, or account decisions such as suspensions.",
    "You review and approve your bots' work. AI tools can make mistakes. Your bots draft, suggest, and prepare content, but you are responsible for reviewing and approving anything before it is posted, sent, published, or acted on. Finance, scheduling, and other bot outputs are for your information and are not professional financial, legal, or tax advice.",
    "Our responsibility is limited to our setup and support services. To the fullest extent allowed by law, PROmote Style is not liable for losses or damages arising from your use of AI tools or third-party services, or from content you approve.",
]
DISCLAIMER_ES = [
    "PROmote Style, una empresa de mAIntAIn Style, ofrece un servicio de configuración de una sola vez. Te ayudamos a crear tus propias cuentas y a configurar bots de IA y herramientas relacionadas para tu negocio. También damos el soporte descrito en este sitio: 90 días de arreglos incluidos, arreglos de pago después, mejoras opcionales y correos mensuales de actualización.",
    "Tus cuentas son tuyas. Cursor, X, Buffer, Metricool y cualquier otro servicio de terceros que uses pertenecen a sus propias empresas y ellas los operan. Te registras directamente, aceptas sus términos y les pagas directamente. PROmote Style no está afiliado a ellos, no cuenta con su respaldo y no actúa en su nombre.",
    "No somos responsables de los servicios de terceros. Esto incluye su disponibilidad, interrupciones, precios, cambios de plan o de funciones, políticas, manejo de datos, seguridad o decisiones de cuenta como las suspensiones.",
    "Tú revisas y apruebas el trabajo de tus bots. Las herramientas de IA pueden equivocarse. Tus bots redactan, sugieren y preparan contenido, pero tú eres responsable de revisar y aprobar cualquier cosa antes de que se publique, se envíe o se actúe sobre ella. Las salidas de finanzas, agenda y otros bots son para tu información y no son asesoría financiera, legal ni fiscal.",
    "Nuestra responsabilidad se limita a nuestros servicios de configuración y soporte. Hasta donde la ley lo permite, PROmote Style no es responsable de pérdidas o daños que surjan de tu uso de herramientas de IA o de servicios de terceros, ni del contenido que tú apruebas.",
]

CTA_TITLE = "Ready to meet your AI marketing team?"
CTA_SUB = "Tell us about your business and we'll recommend the right package."
CTA_BUTTON = "Get started"

FOOTER_LINE = "PROmote Style — a mAIntAIn Style company. Bend, Oregon."

TOTOP_ICON = "assets/totop-arrow.svg"
