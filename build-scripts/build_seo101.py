# -*- coding: utf-8 -*-
"""
build_seo101.py -- "SEO 101," the single consolidated resource page.

2026-08-17: replaces what used to be three separate pages -- SEO Basics
(build_seo_basics.py), Built SEO-Ready (build_built_seo_ready.py), and
Business Listings (build_listings.py). George's feedback: the header had
too many links for an education-first site, and three separate pages read
as three separate promo pages rather than one resource. All three pillars'
content is preserved verbatim below (just regrouped into tab panels) and
those three old build scripts have been removed -- this file is now the
single source for all of it.

Tabs are plain vanilla JS (matches the hamburger/lang-toggle/back-to-top
pattern already used elsewhere in this codebase): one tab panel visible at
a time, deep-linkable via #basics / #built / #listings, and any anchor
inside a panel (e.g. #keywords, #google) still works from an external link
-- the script figures out which tab owns that anchor, switches to it, then
scrolls to the anchor.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

# ----------------------------------------------------------------------------
# TAB 1 -- SEO Basics (verbatim from the former build_seo_basics.py; content
# grounded in what people actually search for beginner SEO/keyword-research
# questions -- see chat history 2026-08-17 for sources).
# ----------------------------------------------------------------------------
BASICS_JUMP_ITEMS = [
    ("foundations", "Foundations"),
    ("keywords", "Keywords"),
    ("backlinks", "Backlinks & Authority"),
    ("tools", "Free Tools"),
    ("mistakes", "Common Mistakes", "Errores Comunes"),
]

def basics_foundations():
    topics = "".join([
        CC.topic("What is SEO, really?", "Search engine optimization, in one sentence",
            "SEO is making it easy for search engines — and the people using them — to understand what your "
            "page is about, so it shows up when someone searches for it. Everything else is detail on top of that."),
        CC.topic("Why does it matter?", "Free traffic that keeps arriving",
            "Paid ads stop the moment you stop paying. A page that ranks organically keeps bringing visitors "
            "in every day after it's published, for free."),
        CC.topic("How do search engines work?", "Crawl, index, rank",
            "Bots (\"crawlers\") follow links from page to page, copy what they find (\"indexing\"), then rank "
            "indexed pages against each other when someone searches — based on relevance, and increasingly, "
            "on whether the page actually answers the question."),
        CC.topic("Organic vs. paid", "Two very different lanes",
            "Organic results are earned — free listings ranked on relevance. Paid results (ads) are rented — "
            "you're charged per click, and the listing disappears the moment you stop paying."),
        CC.topic("What are backlinks, briefly?", "A vote of confidence from another site",
            "When another site links to yours, search engines read it a bit like an endorsement. More on this "
            "below — it's still one of the strongest ranking signals there is."),
        CC.topic("Is SEO still worth it with AI search?", "Yes — the fundamentals didn't change",
            "AI Overviews and chat-based search change how results get presented, not whether search engines "
            "need to figure out what a page is about and whether to trust it. The mechanics underneath are the "
            "same — write answer-first content, use clear headings, and spell out the actual answer in plain "
            "sentences instead of burying it. That's what gets pulled into an AI summary or answer box.",
            q_es="¿El SEO todavía vale la pena con la búsqueda por IA?",
            h3_es="Sí — lo esencial no cambió",
            body_es="Los resúmenes de IA y la búsqueda conversacional cambian cómo se presentan los resultados, "
            "no si los motores de búsqueda necesitan entender de qué trata una página y si pueden confiar en "
            "ella. La mecánica de fondo es la misma: escribe contenido que responda directo, usa encabezados "
            "claros y da la respuesta real en oraciones simples en vez de esconderla. Eso es lo que termina "
            "apareciendo en un resumen o cuadro de respuesta de IA."),
        CC.topic("Is my site even indexed?", "A ten-second gut check",
            "Search <code>site:yourdomain.com</code> on Google. If nothing shows up, Google hasn't indexed your "
            "site yet — meaning it can't rank for anything, no matter how good the content is. Worth checking "
            "before troubleshooting anything else.",
            q_es="¿Mi sitio siquiera está indexado?",
            h3_es="Una revisión de diez segundos",
            body_es="Busca <code>site:tudominio.com</code> en Google. Si no aparece nada, Google todavía no "
            "indexó tu sitio — lo que significa que no puede posicionarse para nada, sin importar qué tan bueno "
            "sea el contenido. Vale la pena revisarlo antes de solucionar cualquier otra cosa."),
        CC.topic("What do I actually fix first?", "Work in this order",
            "Roughly: can Google reach and read the page at all, does the content actually answer something "
            "real, does it use words people search for, is it fast and usable on mobile — then worry about "
            "backlinks and structured data. Most beginners jump straight to the last two first.",
            q_es="¿Qué debo arreglar primero?",
            h3_es="Trabaja en este orden",
            body_es="En términos generales: si Google puede llegar a la página y leerla, si el contenido "
            "realmente responde algo real, si usa las palabras que la gente busca, si es rápida y funciona "
            "bien en el celular — y después preocúpate por los backlinks y los datos estructurados. La mayoría "
            "de los principiantes saltan directo a estos dos últimos."),
    ])
    return CC.cluster("foundations", "START HERE", "Foundations",
        "The handful of concepts everything else in SEO builds on top of.", topics)

def basics_keywords():
    topics = "".join([
        CC.topic("What are keywords?", "The words people actually type",
            "Keywords are the words and phrases people type into a search engine. Using the right ones — in "
            "the right places — is how a search engine matches your page to their search."),
        CC.topic("Short-tail vs. long-tail", "Broad and busy vs. specific and ready to act",
            "Short-tail keywords (1-2 words) get huge search volume and huge competition — think \"shoes.\" "
            "Long-tail keywords (3+ words) get far less volume but sharper intent and better conversion — "
            "think \"waterproof hiking boots for wide feet.\" Beginners win more, faster, on long-tail."),
        CC.topic("What is search intent?", "What the searcher actually wants",
            "Every search has an intent behind it: learn something, compare options, find a specific site, or "
            "buy something. Content that matches the intent behind a keyword outranks content that just "
            "stuffs the keyword in without answering the actual question."),
        CC.topic("What is keyword difficulty?", "How hard a term is to rank for",
            "A 0-100 score estimating how competitive a keyword is to rank for. As a beginner, look for terms "
            "scoring under roughly 30 — realistic wins instead of head-on competition with sites that have "
            "been building authority for a decade."),
        CC.topic("How much traffic will a keyword bring?", "Volume is only half the picture",
            "A keyword's search volume tells you the ceiling. Combine it with difficulty and intent before "
            "deciding whether it's worth targeting — a lower-volume, high-intent term often converts better "
            "than a high-volume, vague one."),
        CC.topic("Where do I even start?", "Brainstorm, then narrow",
            "List every word or phrase a real customer might type — as broad as you want at first. Then run "
            "that list through a free tool (see below) to see actual volume and difficulty before you write "
            "a single word of content."),
        CC.topic("Not every keyword wants the same thing", "Match the keyword to the right page",
            "A search that sounds ready to buy or book should land on a page that lets them actually do that — "
            "not a blog post. A search that sounds like someone learning wants an explanation, not a sales "
            "pitch. Sending the wrong intent to the wrong page is a quiet, common way to lose a visitor who "
            "was already interested.",
            q_es="No toda palabra clave busca lo mismo",
            h3_es="Empareja la palabra clave con la página correcta",
            body_es="Una búsqueda que suena lista para comprar o reservar debería llevar a una página donde la "
            "persona pueda hacerlo de verdad — no a un artículo de blog. Una búsqueda que suena a alguien "
            "aprendiendo quiere una explicación, no un discurso de venta. Mandar la intención equivocada a la "
            "página equivocada es una forma silenciosa y común de perder a un visitante que ya estaba "
            "interesado."),
    ])
    return CC.cluster("keywords", "THE CORE SKILL", "Keywords: finding what people actually search",
        "This is the part most beginners skip past — and the part that matters most.", topics)

def basics_backlinks():
    topics = "".join([
        CC.topic("What are backlinks?", "Other sites vouching for you",
            "A backlink is a link from another website to yours. Search engines treat backlinks a bit like "
            "recommendations — the more relevant, trustworthy sites linking to you, the more trustworthy your "
            "own page looks by association."),
        CC.topic("Do backlinks still matter?", "Yes — still one of the strongest signals",
            "Content quality and technical setup matter more than they used to, but backlinks remain one of "
            "the clearest trust signals a search engine has. Ignoring them entirely still hurts."),
        CC.topic("How do I get my first ones?", "Start small, start real",
            "Local directories, industry associations, partner or supplier sites, guest posts, and simply "
            "asking a happy customer or partner to link to you are realistic starting points — no need for a "
            "link-building agency on day one."),
        CC.topic("What makes a backlink valuable?", "Relevance and trust over raw count",
            "One link from a site closely related to your industry is worth more than ten from random, "
            "unrelated directories. Quality and relevance beat quantity every time."),
    ])
    return CC.cluster("backlinks", "TRUST SIGNALS", "Backlinks & authority",
        "Why other sites linking to you still matters as much as it ever did.", topics)

def basics_tools():
    topics = "".join([
        CC.topic("Where do I check keyword volume?", "Free options that are genuinely enough to start",
            "Google Keyword Planner, Google Trends, and AnswerThePublic all have usable free tiers — plenty "
            "to get started before ever paying for a tool."),
        CC.topic("Google Search Console", "How Google itself sees your site",
            "Free, and directly from Google — shows what you're already ranking for, what's broken, and which "
            "pages are and aren't indexed. This is step one after any site launch, not a \"someday\" task."),
        CC.topic("Google Analytics (GA4)", "What happens after someone lands on your page",
            "Free traffic and behavior data — where visitors come from, what they do, and where they drop off. "
            "Pairs directly with Search Console's \"who's searching\" with GA4's \"what do they do next.\""),
        CC.topic("Google Trends", "Is interest in a topic rising or falling?",
            "Free, and useful for timing content — spotting seasonal patterns or a topic on its way up before "
            "it peaks."),
        CC.topic("How do I check if my site is fast enough?", "PageSpeed Insights (free, from Google)",
            "Tests your site against Google's three Core Web Vitals: LCP (loading — under 2.5 seconds is good), "
            "INP (responsiveness — under 200 milliseconds), and CLS (visual stability — under 0.1). These are "
            "the actual thresholds Google measures, not vague \"make it faster\" advice.",
            q_es="¿Cómo sé si mi sitio es lo bastante rápido?",
            h3_es="PageSpeed Insights (gratis, de Google)",
            body_es="Evalúa tu sitio con las tres Core Web Vitals de Google: LCP (carga — menos de 2.5 segundos "
            "es bueno), INP (capacidad de respuesta — menos de 200 milisegundos) y CLS (estabilidad visual — "
            "menos de 0.1). Estos son los umbrales reales que mide Google, no un consejo vago de \"hazlo más "
            "rápido\"."),
    ])
    return CC.cluster("tools", "GET SET UP", "Free tools worth using today",
        "No budget required to start doing this properly.", topics)

def basics_mistakes():
    topics = "".join([
        CC.topic("TOO COMPETITIVE", "Targeting keywords you can't realistically win yet",
            "Going straight for the highest-volume term in your industry means competing with sites that have "
            "a decade of authority. Long-tail terms win faster, and add up.",
            q_es="DEMASIADO COMPETIDO", h3_es="Apuntar a palabras clave que todavía no puedes ganar",
            body_es="Ir directo por el término de mayor volumen de tu industria significa competir con sitios "
            "que llevan una década construyendo autoridad. Los términos de cola larga ganan más rápido, y se "
            "acumulan."),
        CC.topic("TOO THIN", "Service pages with no real detail",
            "A page that just names a service without explaining it, who it's for, or what it costs gives "
            "search engines (and visitors) nothing to work with.",
            q_es="DEMASIADO SUPERFICIAL", h3_es="Páginas de servicio sin detalle real",
            body_es="Una página que solo nombra un servicio sin explicarlo, para quién es o cuánto cuesta no "
            "le da nada con qué trabajar a los motores de búsqueda (ni a los visitantes)."),
        CC.topic("NO NEXT STEP", "No clear call-to-action on the homepage",
            "If a visitor has to hunt for how to contact or buy from you, most of them won't bother — and "
            "that's true whether they found you through search or anywhere else.",
            q_es="SIN SIGUIENTE PASO", h3_es="Sin un llamado a la acción claro en la página de inicio",
            body_es="Si un visitante tiene que buscar cómo contactarte o comprarte, la mayoría no se va a "
            "molestar — y eso es cierto sin importar cómo te encontraron."),
        CC.topic("FLYING BLIND", "No analytics or way to see what's working",
            "Without Search Console and GA4 (both free, both covered above) there's no way to tell which pages "
            "are working and which are quietly failing.",
            q_es="VOLANDO A CIEGAS", h3_es="Sin analítica ni forma de ver qué está funcionando",
            body_es="Sin Search Console y GA4 (ambos gratis, ambos cubiertos arriba) no hay forma de saber "
            "qué páginas están funcionando y cuáles están fallando en silencio."),
        CC.topic("LEFT BEHIND", "A slow, outdated site",
            "Speed and mobile usability are ranking factors, not just nice-to-haves — see the Core Web Vitals "
            "tool above.",
            q_es="QUEDÁNDOSE ATRÁS", h3_es="Un sitio lento y desactualizado",
            body_es="La velocidad y la usabilidad en celular son factores de posicionamiento, no solo un "
            "plus — mira la herramienta de Core Web Vitals arriba."),
        CC.topic("INVISIBLE", "Ignoring free business listings",
            "Skipping Google Business Profile and the other free listings covered in the Business Listings "
            "tab is one of the most common, most avoidable gaps.",
            q_es="INVISIBLE", h3_es="Ignorar los listados de negocio gratuitos",
            body_es="Saltarse Google Business Profile y los demás listados gratuitos cubiertos en la pestaña "
            "de Listados de Negocio es uno de los vacíos más comunes y más fáciles de evitar."),
        CC.topic("ONE CHANNEL", "Relying on social media alone",
            "Social posts stop reaching people the moment you stop posting. A page that ranks organically "
            "keeps working in the background, indefinitely.",
            q_es="UN SOLO CANAL", h3_es="Depender solo de redes sociales",
            body_es="Las publicaciones en redes dejan de llegarle a la gente en cuanto dejas de publicar. Una "
            "página que se posiciona de forma orgánica sigue trabajando en segundo plano, indefinidamente."),
    ])
    return CC.cluster("mistakes", "AVOID THESE", "Common mistakes that quietly cost the most",
        "None of these are complicated to fix — they're just easy to overlook.", topics,
        tag_es="EVITA ESTO", h2_es="Los errores comunes que más cuestan, sin que se note",
        lead_es="Ninguno de estos es complicado de arreglar — solo son fáciles de pasar por alto.")

def panel_basics():
    body = (
        CC.jump_nav(BASICS_JUMP_ITEMS)
        + basics_foundations()
        + basics_keywords()
        + basics_backlinks()
        + basics_tools()
        + basics_mistakes()
    )
    return f'<div class="tab-panel" id="tab-basics" data-panel="basics">{body}</div>'

# ----------------------------------------------------------------------------
# TAB 2 -- Built SEO-Ready (verbatim from the former build_built_seo_ready.py;
# every claim verified against mAIntAIn Style's real build script as of
# 2026-08-17, not generic SEO advice).
# ----------------------------------------------------------------------------
BUILT_TECH_ITEMS = [
    ("Real, crawlable HTML", "Every page is generated as plain static HTML -- not a JavaScript app a crawler "
     "has to render first. Search engines can read the whole page immediately, every time."),
    ("Unique title + description, every page", "No page ships with a default \"Home\" title or a copy-pasted "
     "description. Every page gets its own, written for what that specific page is about."),
    ("Canonical tags on every page", "Tells search engines the one true URL for each page, so you never get "
     "penalized for accidental duplicate-content issues."),
    ("Schema markup (JSON-LD), automatically", "Every page includes structured Organization schema -- the "
     "machine-readable data search engines use for rich results. Generated from the same build script, not "
     "bolted on after the fact."),
    ("Open Graph + Twitter Card tags", "When someone shares your site on social media or in a text message, "
     "the preview card shows the right title, description, and image -- not a broken gray box."),
    ("Sitemap.xml + robots.txt, every build", "Generated fresh from the actual page list every time the site "
     "builds -- never manually maintained, never goes stale, never points at a page that no longer exists."),
    ("Fast hosting on the edge", "Hosted on Cloudflare's global network -- pages load quickly wherever the "
     "visitor is, and speed is a real, measurable ranking factor."),
    ("Mobile-responsive by default", "Search engines rank the mobile version of your site first. Every layout "
     "is built mobile-first, not \"desktop site that also sort of works on a phone.\""),
    ("Clean, descriptive URLs", "Pages are named for what they are (pricing.html, contact.html) -- not "
     "auto-generated ID strings a search engine (or a person) can't read."),
    ("Proper heading structure", "One real H1 per page, then a logical H2/H3 hierarchy underneath -- not "
     "styled text pretending to be a heading, which search engines see straight through."),
    ("Free SSL / HTTPS", "The padlock, on by default. Not a paid add-on, not a manual setup step."),
]

def built_tech_grid():
    cards = "".join(
        f'<div class="topic"><h3>{t}</h3><p>{d}</p></div>' for t, d in BUILT_TECH_ITEMS)
    return f"""<section class="sec cluster" id="whats-included"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag">WHAT SHIPS ON EVERY PAGE</span>
  <h2>Not advice. A description of what actually gets built.</h2>
  <p class="lead">Every item below is verified against mAIntAIn Style's real build script, not a generic best-practices list -- if it's here, it's in the code.</p></div>
  <div class="topic-grid">{cards}</div>
</div></section>"""

def built_comparison():
    items = [
        ("DIY builder (Wix, Squarespace, etc.)", "Some of this is possible, but it's manual, easy to skip a "
         "page on, and drifts out of date as the site grows."),
        ("Typical agency build", "Depends entirely on whether that agency happens to care about SEO -- it's "
         "rarely a checklist, it's whoever built the site remembering to do it."),
        ("A mAIntAIn Style build", "Comes from the build script, not a person's memory. Every page gets it, "
         "every time, because skipping it would mean changing the code -- not just forgetting a step."),
    ]
    cards = "".join(
        f'<div class="topic"><span class="q">{a}</span><p>{b}</p></div>' for a, b in items)
    return f"""<section class="sec" style="background:var(--panel);border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag">WHY IT'S CONSISTENT</span><h2>The difference is where the checklist lives</h2></div>
  <div class="topic-grid">{cards}</div>
</div></section>"""

UPGRADE_SIGNS = [
    ("Loads slowly",
     "Every extra second before a page is usable costs visitors, and Google measures it directly (see Core Web Vitals in the SEO Basics tab).",
     "Carga lento",
     "Cada segundo extra antes de que una página sea usable cuesta visitantes, y Google lo mide directamente (ver Core Web Vitals en la pestaña de SEO Basics)."),
    ("Hard to update yourself",
     "If changing a price or a photo means calling someone and waiting days, the site is working against you, not for you.",
     "Difícil de actualizar tú mismo",
     "Si cambiar un precio o una foto significa llamar a alguien y esperar días, el sitio está trabajando en tu contra, no a tu favor."),
    ("Doesn't convert visitors",
     "Traffic that never turns into a call, booking, or sale is a leak, not a win.",
     "No convierte visitantes",
     "El tráfico que nunca se convierte en una llamada, una reserva o una venta es una fuga, no una ganancia."),
    ("Isn't mobile-friendly",
     "Google ranks the mobile version of a site first -- if that experience is broken, everything else on this list matters less.",
     "No es amigable con el celular",
     "Google posiciona primero la versión para celular de un sitio -- si esa experiencia está rota, todo lo demás en esta lista importa menos."),
    ("Missing basic pages",
     "No clear services page, no easy way to contact you, or pages built for a business that no longer exists.",
     "Faltan páginas básicas",
     "Sin una página clara de servicios, sin una forma fácil de contactarte, o páginas hechas para un negocio que ya no existe."),
    ("Feels outdated or confusing",
     "Visitors judge trustworthiness fast. A site that looks abandoned reads as a business that might be too.",
     "Se siente desactualizado o confuso",
     "Los visitantes juzgan la confiabilidad rápido. Un sitio que se ve abandonado se lee como un negocio que también podría estarlo."),
]

def built_upgrade_signs():
    cards = "".join(
        f'<div class="topic"><h3{CC._es_attr(t_es)}>{t}</h3><p{CC._es_html_attr(d_es)}>{d}</p></div>'
        for t, d, t_es, d_es in UPGRADE_SIGNS)
    tag_attr = CC._es_attr("VALE LA PENA PREGUNTAR")
    h2_attr = CC._es_html_attr("Señales de que podría ser hora de actualizar")
    lead_attr = CC._es_attr("Ninguna de estas significa empezar de cero -- solo vale la pena mirarlas con honestidad.")
    return f"""<section class="sec cluster"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag"{tag_attr}>WORTH ASKING</span>
  <h2{h2_attr}>Signs it might be time to upgrade</h2>
  <p class="lead"{lead_attr}>None of these mean start over from scratch -- they're just worth an honest look.</p></div>
  <div class="topic-grid">{cards}</div>
</div></section>"""

def panel_built():
    body = (
        built_tech_grid()
        + built_comparison()
        + built_upgrade_signs()
        + f'<section class="sec"><div class="wrap"><div class="prose">'
          + CC.tip_box("WORTH KNOWING",
                "None of this replaces content and keyword work covered in the "
                "<a href=\"#basics\" style=\"color:var(--gold);font-weight:700\">SEO Basics</a> tab -- it's "
                "the technical floor every page should stand on before that work even starts. A perfectly-"
                "written page on a technically broken foundation still struggles to rank.")
          + "</div></div></section>"
    )
    return f'<div class="tab-panel" id="tab-built" data-panel="built" hidden>{body}</div>'

# ----------------------------------------------------------------------------
# TAB 3 -- Business Listings (verbatim from the former build_listings.py).
# ----------------------------------------------------------------------------
def listings_google():
    steps = CC.steps_list([
        ("Go to google.com/business and sign in", "Use the Google account your business already uses, or "
         "create one dedicated to the business -- not a personal one an employee might lose access to."),
        ("Search for your business name first", "If a listing already exists (sometimes created automatically "
         "from reviews or map data), claim it instead of creating a duplicate."),
        ("Enter your business details", "Exact legal name, address, phone number, category, and hours -- this "
         "becomes the reference version other directories often pull from."),
        ("Choose a verification method", "Usually a postcard mailed to the business address, sometimes phone "
         "or email for eligible businesses -- follow whichever Google offers."),
        ("Complete the profile after verifying", "Add photos, a description, services/products, and keep "
         "hours current -- an unverified or empty profile ranks worse than a complete one."),
    ])
    tip = CC.tip_box("AFTER YOU'RE SET UP",
        "Reviews matter more when they arrive steadily over time than in one sudden burst -- a pile of reviews "
        "all posted the same week can actually look suspicious to both customers and Google. Asking happy "
        "customers as you go beats a one-time push.",
        label_es="DESPUÉS DE CONFIGURARLO",
        es=["Las reseñas importan más cuando llegan de forma constante a lo largo del tiempo que en una sola "
            "ráfaga -- un montón de reseñas publicadas la misma semana puede parecer sospechoso tanto para "
            "los clientes como para Google. Pedirlas sobre la marcha a clientes contentos funciona mejor que "
            "un solo empujón puntual."])
    return f"""<section class="sec cluster" id="google"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag">MOST IMPORTANT</span><h2>Google Business Profile</h2>
  <p class="lead">The single highest-impact listing for local search and Google Maps -- do this one first if you do nothing else.</p></div>
  <div class="prose">{steps}{tip}</div>
</div></section>"""

def listings_bing():
    steps = CC.steps_list([
        ("Go to Bing Places for Business", "Sign in with a Microsoft account."),
        ("Import from Google, or add manually", "Bing offers a straightforward import from an existing Google "
         "Business Profile, which is usually faster than starting from scratch."),
        ("Verify your listing", "Similar options to Google -- phone, postcard, or email depending on eligibility."),
        ("Keep it in sync with Google", "Bing still powers a meaningful share of search and voice assistants -- "
         "don't let it go stale just because Google gets the attention."),
    ])
    return f"""<section class="sec cluster" id="bing"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag">DON'T SKIP THIS ONE</span><h2>Bing Places for Business</h2>
  <p class="lead">Smaller share of search than Google, but free, fast to set up, and still real traffic.</p></div>
  <div class="prose">{steps}</div>
</div></section>"""

def listings_apple():
    steps = CC.steps_list([
        ("Go to Apple Business Connect", "Sign in with an Apple ID."),
        ("Claim or add your location", "Apple will try to match an existing listing from Apple Maps data first."),
        ("Verify ownership", "Options vary by business type -- phone verification is common."),
        ("Fill out the profile", "Hours, photos, and a short description show up directly in Apple Maps and Siri results."),
    ])
    return f"""<section class="sec cluster" id="apple"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag">GROWING SHARE</span><h2>Apple Business Connect</h2>
  <p class="lead">Every iPhone user searching Apple Maps or asking Siri for a business pulls from this listing.</p></div>
  <div class="prose">{steps}</div>
</div></section>"""

def listings_nap():
    body = CC.tip_box("NAP = NAME, ADDRESS, PHONE",
        "Every listing above should show the <strong>exact same</strong> business name, address, and phone "
        "number -- down to how the street type is abbreviated (\"St\" vs \"Street\"). Inconsistent NAP data "
        "across listings is one of the most common, most avoidable reasons a business underperforms in local "
        "search -- it actively confuses search engines about which listing is authoritative.",
        "Keep a single reference doc with the exact, final wording of your name/address/phone, and copy from "
        "it every time -- never retype it from memory into a new directory.")
    return f"""<section class="sec" style="background:var(--panel);border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)" id="nap"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag">THE MOST COMMON MISTAKE</span><h2>Keep every listing consistent</h2></div>
  <div class="prose">{body}</div>
</div></section>"""

LISTINGS_JUMP_ITEMS = [
    ("google", "Google Business Profile"),
    ("bing", "Bing Places"),
    ("apple", "Apple Business Connect"),
    ("nap", "Staying Consistent"),
]

def panel_listings():
    body = (
        CC.jump_nav(LISTINGS_JUMP_ITEMS)
        + listings_google()
        + listings_bing()
        + listings_apple()
        + listings_nap()
    )
    return f'<div class="tab-panel" id="tab-listings" data-panel="listings" hidden>{body}</div>'

# ----------------------------------------------------------------------------
# Tabs shell + switching script
# ----------------------------------------------------------------------------
def tabs_nav():
    return f"""<div class="wrap"><div class="tabs-nav" role="tablist">
  <button class="tab-btn active" type="button" data-tab="basics" role="tab" aria-selected="true">SEO Basics</button>
  <button class="tab-btn" type="button" data-tab="built" role="tab" aria-selected="false">Built SEO-Ready</button>
  <button class="tab-btn" type="button" data-tab="listings" role="tab" aria-selected="false">Business Listings</button>
</div></div>"""

def tabs_script():
    return """<script>(function(){
  var MAP = {basics:['foundations','keywords','backlinks','tools','mistakes'],
             built:['whats-included'],
             listings:['google','bing','apple','nap']};
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab-btn'));
  var panels = Array.prototype.slice.call(document.querySelectorAll('.tab-panel'));
  function activate(name){
    tabs.forEach(function(b){
      var on = b.dataset.tab===name;
      b.classList.toggle('active', on);
      b.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    panels.forEach(function(p){ p.hidden = p.dataset.panel!==name; });
  }
  tabs.forEach(function(b){
    b.addEventListener('click', function(){
      activate(b.dataset.tab);
      history.replaceState(null, '', '#'+b.dataset.tab);
    });
  });
  function fromHash(scroll){
    var h = (location.hash || '').replace('#','');
    if(!h) return;
    if(MAP[h]){ activate(h); return; }
    for(var key in MAP){
      if(MAP[key].indexOf(h) !== -1){
        activate(key);
        if(scroll){
          setTimeout(function(){
            var el = document.getElementById(h);
            if(el) el.scrollIntoView({behavior:'smooth', block:'start'});
          }, 30);
        }
        return;
      }
    }
  }
  fromHash(true);
  window.addEventListener('hashchange', function(){ fromHash(true); });
})();</script>"""

def build():
    title = "SEO 101 — Free SEO Basics, Built SEO-Ready Proof & Business Listings | PROmote Style"
    desc = ("Everything free to learn SEO in one place: plain-English SEO basics and keyword research, what a "
            "technically SEO-ready site actually includes, and how to set up Google, Bing, and Apple business listings.")
    extra_css = f"<style>{CC.content_css()}</style>"
    html = (
        S.head(title, desc, "seo-101.html")
        + extra_css
        + S.nav("seo-101.html")
        + CC.article_hero("SEO 101", "Everything free, in one place",
              "SEO basics, what a properly SEO-ready site actually includes, and how to set up your business "
              "listings — three tabs, no jargon, written for a wide audience, not just marketers.")
        + tabs_nav()
        + panel_basics()
        + panel_built()
        + panel_listings()
        + f'<section class="sec" style="padding-top:0"><div class="wrap">'
          + CC.inline_cta("Want a site built with all of this already done for you?",
                           "https://maintain.style/portfolio.html", "View SEO-Ready Sites")
          + "</div></section>"
        + S.footer()
        + S.back_to_top()
        + tabs_script()
        + S.close_html()
    )
    S.write_page("seo-101.html", html)

if __name__ == "__main__":
    build()
