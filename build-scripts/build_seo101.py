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
    ("foundations", "Foundations", "Fundamentos"),
    ("keywords", "Keywords", "Palabras Clave"),
    ("backlinks", "Backlinks & Authority", "Backlinks y Autoridad"),
    ("tools", "Free Tools", "Herramientas Gratis"),
    ("mistakes", "Common Mistakes", "Errores Comunes"),
]

def basics_do_first():
    steps = CC.steps_list([
        ("Confirm the site is indexed", "Search <code>site:yourdomain.com</code> on Google — nothing showing up "
         "means nothing else on this list matters yet."),
        ("Set up Google Search Console + GA4", "Both free, both covered in Free Tools below — step one after any "
         "launch, not a someday task."),
        ("Pick 3-5 realistic long-tail keywords", "Specific phrases with real intent behind them, not the single "
         "broadest term in your industry."),
        ("Make sure your main pages actually answer the search", "Homepage and service pages should say the "
         "real thing plainly, not hint at it."),
        ("Check Core Web Vitals and mobile usability", "PageSpeed Insights, free from Google — covered below."),
        ("Claim your business listings", "Google Business Profile first — see the "
         '<a href="#google" style="color:var(--gold);font-weight:700">Business Listings tab</a>.'),
    ], steps_es=[
        ("Confirma que el sitio esté indexado", "Busca <code>site:tudominio.com</code> en Google — si no aparece "
         "nada, nada más en esta lista importa todavía."),
        ("Configura Google Search Console + GA4", "Ambos gratis, ambos cubiertos en Herramientas Gratuitas más "
         "abajo — el primer paso después de cualquier lanzamiento, no un \"algún día\"."),
        ("Elige 3-5 palabras clave de cola larga realistas", "Frases específicas con intención real detrás, no "
         "el término más amplio de tu industria."),
        ("Asegúrate de que tus páginas principales respondan la búsqueda", "La página de inicio y las de "
         "servicios deben decir la respuesta real, sin dar rodeos."),
        ("Revisa Core Web Vitals y la usabilidad en celular", "PageSpeed Insights, gratis de Google — cubierto "
         "más abajo."),
        ("Reclama tus listados de negocio", "Google Business Profile primero — ver la "
         '<a href="#google" style="color:var(--gold);font-weight:700">pestaña de Listados de Negocio</a>.'),
    ])
    tip = CC.tip_box("START WITH THIS",
        "A six-step first pass — work through it once, then use the rest of this tab to go deeper on any step.",
        label_es="EMPIEZA POR AQUÍ",
        es=["Un primer repaso de seis pasos — hazlo una vez, y usa el resto de esta pestaña para profundizar en "
            "cualquier paso."])
    return f'<div class="wrap"><div class="prose">{tip}{steps}</div></div>'

def basics_foundations():
    topics = "".join([
        CC.topic("What is SEO, really?", "Search engine optimization, in one sentence",
            "SEO is making it easy for search engines — and the people using them — to understand what your "
            "page is about, so it shows up when someone searches for it. Everything else is detail on top of that.",
            q_es="¿Qué es el SEO, en realidad?", h3_es="Optimización para motores de búsqueda, en una frase",
            body_es="El SEO consiste en ponerle fácil a los motores de búsqueda — y a las personas que los "
            "usan — entender de qué trata tu página, para que aparezca cuando alguien la busque. Todo lo demás "
            "es detalle encima de eso."),
        CC.topic("Why does it matter?", "Free traffic that keeps arriving",
            "Paid ads stop the moment you stop paying. A page that ranks organically keeps bringing visitors "
            "in every day after it's published, for free.",
            q_es="¿Por qué importa?", h3_es="Tráfico gratis que sigue llegando",
            body_es="Los anuncios pagados se detienen en cuanto dejas de pagar. Una página que se posiciona de "
            "forma orgánica sigue trayendo visitantes todos los días después de publicarse, gratis."),
        CC.topic("How do search engines work?", "Crawl, index, rank",
            "Bots (\"crawlers\") follow links from page to page, copy what they find (\"indexing\"), then rank "
            "indexed pages against each other when someone searches — based on relevance, and increasingly, "
            "on whether the page actually answers the question.",
            q_es="¿Cómo funcionan los motores de búsqueda?", h3_es="Rastrear, indexar, posicionar",
            body_es="Los bots (\"rastreadores\") siguen enlaces de página en página, copian lo que encuentran "
            "(\"indexación\"), y luego posicionan las páginas indexadas unas contra otras cuando alguien busca "
            "— según la relevancia, y cada vez más, según si la página realmente responde la pregunta."),
        CC.topic("Organic vs. paid", "Two very different lanes",
            "Organic results are earned — free listings ranked on relevance. Paid results (ads) are rented — "
            "you're charged per click, and the listing disappears the moment you stop paying.",
            q_es="Orgánico vs. pagado", h3_es="Dos carriles muy distintos",
            body_es="Los resultados orgánicos se ganan — listados gratis posicionados por relevancia. Los "
            "resultados pagados (anuncios) se rentan — te cobran por clic, y el listado desaparece en cuanto "
            "dejas de pagar."),
        CC.topic("What are backlinks, briefly?", "A vote of confidence from another site",
            "When another site links to yours, search engines read it a bit like an endorsement. More on this "
            "below — it's still one of the strongest ranking signals there is.",
            q_es="¿Qué son los backlinks, brevemente?", h3_es="Un voto de confianza de otro sitio",
            body_es="Cuando otro sitio enlaza al tuyo, los motores de búsqueda lo interpretan casi como un "
            "respaldo. Más sobre esto más abajo — sigue siendo una de las señales de posicionamiento más "
            "fuertes que existen."),
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
        "The handful of concepts everything else in SEO builds on top of.", topics,
        tag_es="EMPIEZA AQUÍ", h2_es="Fundamentos",
        lead_es="El puñado de conceptos sobre los que se construye todo lo demás en SEO.")

def basics_keywords():
    topics = "".join([
        CC.topic("What are keywords?", "The words people actually type",
            "Keywords are the words and phrases people type into a search engine. Using the right ones — in "
            "the right places — is how a search engine matches your page to their search.",
            q_es="¿Qué son las palabras clave?", h3_es="Las palabras que la gente realmente escribe",
            body_es="Las palabras clave son las palabras y frases que la gente escribe en un motor de "
            "búsqueda. Usar las correctas — en los lugares correctos — es cómo un motor de búsqueda conecta "
            "tu página con su búsqueda."),
        CC.topic("Short-tail vs. long-tail", "Broad and busy vs. specific and ready to act",
            "Short-tail keywords (1-2 words) get huge search volume and huge competition — think \"shoes.\" "
            "Long-tail keywords (3+ words) get far less volume but sharper intent and better conversion — "
            "think \"waterproof hiking boots for wide feet.\" Beginners win more, faster, on long-tail.",
            q_es="Cola corta vs. cola larga", h3_es="Amplio y saturado vs. específico y listo para actuar",
            body_es="Las palabras clave de cola corta (1-2 palabras) tienen mucho volumen de búsqueda y mucha "
            "competencia — piensa en \"zapatos\". Las de cola larga (3+ palabras) tienen mucho menos volumen "
            "pero una intención más clara y mejor conversión — piensa en \"botas de senderismo impermeables "
            "para pie ancho\". Los principiantes ganan más, más rápido, con cola larga."),
        CC.topic("What is search intent?", "What the searcher actually wants",
            "Every search has an intent behind it: learn something, compare options, find a specific site, or "
            "buy something. Content that matches the intent behind a keyword outranks content that just "
            "stuffs the keyword in without answering the actual question.",
            q_es="¿Qué es la intención de búsqueda?", h3_es="Lo que la persona que busca realmente quiere",
            body_es="Toda búsqueda tiene una intención detrás: aprender algo, comparar opciones, encontrar un "
            "sitio específico, o comprar algo. El contenido que coincide con la intención detrás de una "
            "palabra clave supera al contenido que solo la repite sin responder la pregunta real."),
        CC.topic("What is keyword difficulty?", "How hard a term is to rank for",
            "A 0-100 score estimating how competitive a keyword is to rank for. As a beginner, look for terms "
            "scoring under roughly 30 — realistic wins instead of head-on competition with sites that have "
            "been building authority for a decade.",
            q_es="¿Qué es la dificultad de palabra clave?", h3_es="Qué tan difícil es posicionarse por un término",
            body_es="Un puntaje de 0 a 100 que estima qué tan competitivo es posicionarse por una palabra "
            "clave. Como principiante, busca términos con un puntaje menor a 30 aproximadamente — victorias "
            "realistas en vez de competir de frente con sitios que llevan una década construyendo autoridad."),
        CC.topic("How much traffic will a keyword bring?", "Volume is only half the picture",
            "A keyword's search volume tells you the ceiling. Combine it with difficulty and intent before "
            "deciding whether it's worth targeting — a lower-volume, high-intent term often converts better "
            "than a high-volume, vague one.",
            q_es="¿Cuánto tráfico traerá una palabra clave?", h3_es="El volumen es solo la mitad del panorama",
            body_es="El volumen de búsqueda de una palabra clave te dice el techo. Combínalo con la dificultad "
            "y la intención antes de decidir si vale la pena apuntarle — un término de bajo volumen pero alta "
            "intención suele convertir mejor que uno de alto volumen pero vago."),
        CC.topic("Where do I even start?", "Brainstorm, then narrow",
            "List every word or phrase a real customer might type — as broad as you want at first. Then run "
            "that list through a free tool (see below) to see actual volume and difficulty before you write "
            "a single word of content.",
            q_es="¿Por dónde empiezo?", h3_es="Genera ideas, luego reduce",
            body_es="Enlista cada palabra o frase que un cliente real podría escribir — tan amplio como "
            "quieras al principio. Luego pasa esa lista por una herramienta gratuita (ver abajo) para ver el "
            "volumen y la dificultad reales antes de escribir una sola palabra de contenido."),
        CC.topic("Where do keywords actually go?", "The five places that matter most",
            "Title tag, H1, and the first 100-150 words carry the most weight — that's where to use your "
            "primary keyword naturally. After that: the meta description (doesn't affect ranking directly, but "
            "affects whether people click) and image alt text. Everywhere else, write for the reader first.",
            q_es="¿Dónde van realmente las palabras clave?",
            h3_es="Los cinco lugares que más importan",
            body_es="La etiqueta de título, el H1 y las primeras 100-150 palabras son los que más pesan — ahí "
            "es donde va tu palabra clave principal, de forma natural. Después: la meta descripción (no afecta "
            "el posicionamiento directamente, pero sí si la gente hace clic) y el texto alternativo de las "
            "imágenes. En todo lo demás, escribe primero para la persona que lee."),
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
        "This is the part most beginners skip past — and the part that matters most.", topics,
        tag_es="LA HABILIDAD CLAVE", h2_es="Palabras clave: encontrar lo que la gente realmente busca",
        lead_es="Esta es la parte que la mayoría de los principiantes se saltan — y la que más importa.")

def basics_backlinks():
    topics = "".join([
        CC.topic("What are backlinks?", "Other sites vouching for you",
            "A backlink is a link from another website to yours. Search engines treat backlinks a bit like "
            "recommendations — the more relevant, trustworthy sites linking to you, the more trustworthy your "
            "own page looks by association.",
            q_es="¿Qué son los backlinks?", h3_es="Otros sitios que responden por ti",
            body_es="Un backlink es un enlace de otro sitio web hacia el tuyo. Los motores de búsqueda tratan "
            "los backlinks casi como recomendaciones — mientras más sitios relevantes y confiables enlacen "
            "hacia ti, más confiable se ve tu propia página por asociación."),
        CC.topic("Do backlinks still matter?", "Yes — still one of the strongest signals",
            "Content quality and technical setup matter more than they used to, but backlinks remain one of "
            "the clearest trust signals a search engine has. Ignoring them entirely still hurts.",
            q_es="¿Los backlinks todavía importan?", h3_es="Sí — siguen siendo una de las señales más fuertes",
            body_es="La calidad del contenido y la configuración técnica importan más que antes, pero los "
            "backlinks siguen siendo una de las señales de confianza más claras que tiene un motor de "
            "búsqueda. Ignorarlos por completo todavía perjudica."),
        CC.topic("How do I get my first ones?", "Start small, start real",
            "Local directories, industry associations, partner or supplier sites, guest posts, and simply "
            "asking a happy customer or partner to link to you are realistic starting points — no need for a "
            "link-building agency on day one.",
            q_es="¿Cómo consigo los primeros?", h3_es="Empieza pequeño, empieza real",
            body_es="Directorios locales, asociaciones de la industria, sitios de socios o proveedores, "
            "publicaciones como invitado, y simplemente pedirle a un cliente o socio contento que te enlace "
            "son puntos de partida realistas — no hace falta una agencia de link-building desde el primer día."),
        CC.topic("What makes a backlink valuable?", "Relevance and trust over raw count",
            "One link from a site closely related to your industry is worth more than ten from random, "
            "unrelated directories. Quality and relevance beat quantity every time.",
            q_es="¿Qué hace valioso a un backlink?", h3_es="Relevancia y confianza por encima de la cantidad",
            body_es="Un enlace de un sitio estrechamente relacionado con tu industria vale más que diez de "
            "directorios aleatorios y sin relación. La calidad y la relevancia le ganan a la cantidad siempre."),
        CC.topic("Is trust about more than just backlinks?", "Yes — real signals of who's behind the page",
            "Search engines also look for signs that a real, credible source is behind the content: a visible "
            "author or business name, genuine examples instead of generic claims, and a clear, honest \"about\" "
            "or contact page. None of this replaces backlinks — it works alongside them.",
            q_es="¿La confianza depende de algo más que los backlinks?",
            h3_es="Sí — señales reales de quién está detrás de la página",
            body_es="Los motores de búsqueda también buscan señales de que hay una fuente real y creíble "
            "detrás del contenido: un autor o nombre de negocio visible, ejemplos genuinos en vez de "
            "afirmaciones genéricas, y una página de \"quiénes somos\" o contacto clara y honesta. Nada de "
            "esto reemplaza los backlinks — funciona junto con ellos."),
    ])
    return CC.cluster("backlinks", "TRUST SIGNALS", "Backlinks & authority",
        "Why other sites linking to you still matters as much as it ever did.", topics,
        tag_es="SEÑALES DE CONFIANZA", h2_es="Backlinks y autoridad",
        lead_es="Por qué que otros sitios te enlacen sigue importando tanto como siempre.")

def basics_tools():
    topics = "".join([
        CC.topic("Where do I check keyword volume?", "Free options that are genuinely enough to start",
            "Google Keyword Planner, Google Trends, and AnswerThePublic all have usable free tiers — plenty "
            "to get started before ever paying for a tool.",
            q_es="¿Dónde reviso el volumen de una palabra clave?", h3_es="Opciones gratis que de verdad alcanzan para empezar",
            body_es="Google Keyword Planner, Google Trends y AnswerThePublic tienen niveles gratuitos "
            "utilizables — de sobra para empezar antes de pagar por una herramienta."),
        CC.topic("Google Search Console", "How Google itself sees your site",
            "Free, and directly from Google — shows what you're already ranking for, what's broken, and which "
            "pages are and aren't indexed. This is step one after any site launch, not a \"someday\" task.",
            q_es="Google Search Console", h3_es="Cómo ve Google mismo a tu sitio",
            body_es="Gratis, y directo de Google — muestra por qué ya te estás posicionando, qué está roto, y "
            "qué páginas están o no indexadas. Este es el paso uno después de cualquier lanzamiento, no una "
            "tarea para \"algún día\"."),
        CC.topic("Google Analytics (GA4)", "What happens after someone lands on your page",
            "Free traffic and behavior data — where visitors come from, what they do, and where they drop off. "
            "Pairs directly with Search Console's \"who's searching\" with GA4's \"what do they do next.\"",
            q_es="Google Analytics (GA4)", h3_es="Qué pasa después de que alguien llega a tu página",
            body_es="Datos gratis de tráfico y comportamiento — de dónde vienen los visitantes, qué hacen, y "
            "dónde se van. Combina directamente el \"quién está buscando\" de Search Console con el \"qué "
            "hacen después\" de GA4."),
        CC.topic("Google Trends", "Is interest in a topic rising or falling?",
            "Free, and useful for timing content — spotting seasonal patterns or a topic on its way up before "
            "it peaks.",
            q_es="Google Trends", h3_es="¿El interés en un tema está subiendo o bajando?",
            body_es="Gratis, y útil para calcular el momento del contenido — detectar patrones estacionales o "
            "un tema que va en aumento antes de que llegue a su pico."),
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
        "No budget required to start doing this properly.", topics,
        tag_es="CONFIGÚRATE", h2_es="Herramientas gratis que vale la pena usar hoy",
        lead_es="No hace falta presupuesto para empezar a hacer esto bien.")

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
    foundations = basics_foundations()
    keywords = basics_keywords()
    backlinks = basics_backlinks()
    tools = basics_tools()
    mistakes = basics_mistakes()
    checklist = basics_do_first()
    body = (
        CC.jump_nav(BASICS_JUMP_ITEMS)
        + checklist
        + foundations
        + keywords
        + backlinks
        + tools
        + mistakes
    )
    return f'<div class="tab-panel" id="tab-basics" data-panel="basics">{body}</div>'


# ----------------------------------------------------------------------------
# TAB 2 -- Built SEO-Ready (verbatim from the former build_built_seo_ready.py;
# every claim verified against mAIntAIn Style's real build script as of
# 2026-08-17, not generic SEO advice).
# ----------------------------------------------------------------------------
BUILT_TECH_ITEMS = [
    ("Real, crawlable HTML", "Every page is generated as plain static HTML -- not a JavaScript app a crawler "
     "has to render first. Search engines can read the whole page immediately, every time.",
     "HTML real y rastreable", "Cada página se genera como HTML estático simple -- no una aplicación de "
     "JavaScript que un rastreador tiene que procesar primero. Los motores de búsqueda pueden leer la página "
     "completa de inmediato, siempre."),
    ("Unique title + description, every page", "No page ships with a default \"Home\" title or a copy-pasted "
     "description. Every page gets its own, written for what that specific page is about.",
     "Título y descripción únicos, en cada página", "Ninguna página sale con un título genérico de \"Inicio\" "
     "o una descripción copiada y pegada. Cada página tiene la suya, escrita para lo que trata esa página en "
     "específico."),
    ("Canonical tags on every page", "Tells search engines the one true URL for each page, so you never get "
     "penalized for accidental duplicate-content issues.",
     "Etiquetas canónicas en cada página", "Le dice a los motores de búsqueda cuál es la única URL verdadera "
     "de cada página, para que nunca te penalicen por problemas accidentales de contenido duplicado."),
    ("Schema markup (JSON-LD), automatically", "Every page includes structured Organization schema -- the "
     "machine-readable data search engines use for rich results. Generated from the same build script, not "
     "bolted on after the fact.",
     "Schema markup (JSON-LD), automático", "Cada página incluye schema de Organización estructurado -- los "
     "datos legibles por máquina que los motores de búsqueda usan para resultados enriquecidos. Generado "
     "desde el mismo script de construcción, no agregado después."),
    ("Open Graph + Twitter Card tags", "When someone shares your site on social media or in a text message, "
     "the preview card shows the right title, description, and image -- not a broken gray box.",
     "Etiquetas Open Graph + Twitter Card", "Cuando alguien comparte tu sitio en redes sociales o en un "
     "mensaje de texto, la tarjeta de vista previa muestra el título, la descripción y la imagen correctos -- "
     "no una caja gris rota."),
    ("Sitemap.xml + robots.txt, every build", "Generated fresh from the actual page list every time the site "
     "builds -- never manually maintained, never goes stale, never points at a page that no longer exists.",
     "Sitemap.xml + robots.txt, en cada construcción", "Generado desde cero a partir de la lista real de "
     "páginas cada vez que el sitio se construye -- nunca se mantiene a mano, nunca se queda desactualizado, "
     "nunca apunta a una página que ya no existe."),
    ("Fast hosting on the edge", "Hosted on Cloudflare's global network -- pages load quickly wherever the "
     "visitor is, and speed is a real, measurable ranking factor.",
     "Hospedaje rápido en el borde (edge)", "Hospedado en la red global de Cloudflare -- las páginas cargan "
     "rápido sin importar dónde esté el visitante, y la velocidad es un factor de posicionamiento real y "
     "medible."),
    ("Mobile-responsive by default", "Search engines rank the mobile version of your site first. Every layout "
     "is built mobile-first, not \"desktop site that also sort of works on a phone.\"",
     "Adaptable a celular por defecto", "Los motores de búsqueda posicionan primero la versión para celular de "
     "tu sitio. Cada diseño se construye pensando primero en el celular, no como un \"sitio de escritorio que "
     "más o menos funciona en un teléfono\"."),
    ("Clean, descriptive URLs", "Pages are named for what they are (pricing.html, contact.html) -- not "
     "auto-generated ID strings a search engine (or a person) can't read.",
     "URLs limpias y descriptivas", "Las páginas se nombran según lo que son (pricing.html, contact.html) -- "
     "no cadenas de ID autogeneradas que ni un motor de búsqueda (ni una persona) pueden leer."),
    ("Proper heading structure", "One real H1 per page, then a logical H2/H3 hierarchy underneath -- not "
     "styled text pretending to be a heading, which search engines see straight through.",
     "Estructura de encabezados correcta", "Un H1 real por página, y luego una jerarquía lógica de H2/H3 "
     "debajo -- no texto con estilo que finge ser un encabezado, algo que los motores de búsqueda detectan de "
     "inmediato."),
    ("Free SSL / HTTPS", "The padlock, on by default. Not a paid add-on, not a manual setup step.",
     "SSL / HTTPS gratis", "El candado, activado por defecto. No es un complemento de pago, no es un paso de "
     "configuración manual."),
]

def built_tech_grid():
    cards = "".join(
        f'<div class="topic"><h3{CC._es_attr(t_es)}>{t}</h3><p{CC._es_attr(d_es)}>{d}</p></div>'
        for t, d, t_es, d_es in BUILT_TECH_ITEMS)
    tag_attr = CC._es_attr("QUÉ INCLUYE CADA PÁGINA")
    h2_attr = CC._es_attr("No es un consejo. Es una descripción de lo que realmente se construye.")
    lead_attr = CC._es_attr("Cada punto abajo está verificado contra el script de construcción real de "
        "mAIntAIn Style, no una lista genérica de buenas prácticas -- si está aquí, está en el código.")
    return f"""<section class="sec cluster" id="whats-included"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag"{tag_attr}>WHAT SHIPS ON EVERY PAGE</span>
  <h2{h2_attr}>Not advice. A description of what actually gets built.</h2>
  <p class="lead"{lead_attr}>Every item below is verified against mAIntAIn Style's real build script, not a generic best-practices list -- if it's here, it's in the code.</p></div>
  <div class="topic-grid">{cards}</div>
</div></section>"""

def built_comparison():
    items = [
        ("DIY builder (Wix, Squarespace, etc.)", "Some of this is possible, but it's manual, easy to skip a "
         "page on, and drifts out of date as the site grows.",
         "Constructor DIY (Wix, Squarespace, etc.)", "Parte de esto es posible, pero es manual, fácil de "
         "saltarse en una página, y se desactualiza a medida que el sitio crece."),
        ("Typical agency build", "Depends entirely on whether that agency happens to care about SEO -- it's "
         "rarely a checklist, it's whoever built the site remembering to do it.",
         "Construcción típica de agencia", "Depende por completo de si a esa agencia le importa el SEO -- casi "
         "nunca es una lista de verificación, es que quien construyó el sitio se acuerde de hacerlo."),
        ("A mAIntAIn Style build", "Comes from the build script, not a person's memory. Every page gets it, "
         "every time, because skipping it would mean changing the code -- not just forgetting a step.",
         "Una construcción de mAIntAIn Style", "Viene del script de construcción, no de la memoria de una "
         "persona. Cada página lo recibe, siempre, porque saltárselo significaría cambiar el código -- no solo "
         "olvidar un paso."),
    ]
    cards = "".join(
        f'<div class="topic"><span class="q"{CC._es_attr(a_es)}>{a}</span><p{CC._es_attr(b_es)}>{b}</p></div>'
        for a, b, a_es, b_es in items)
    tag_attr = CC._es_attr("POR QUÉ ES CONSISTENTE")
    h2_attr = CC._es_attr("La diferencia está en dónde vive la lista de verificación")
    return f"""<section class="sec" style="background:var(--panel);border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag"{tag_attr}>WHY IT'S CONSISTENT</span><h2{h2_attr}>The difference is where the checklist lives</h2></div>
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
    return f"""<section class="sec cluster" style="padding-top:64px"><div class="wrap">
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
                "written page on a technically broken foundation still struggles to rank.",
                label_es="VALE LA PENA SABERLO",
                es=["Nada de esto reemplaza el trabajo de contenido y palabras clave cubierto en la pestaña de "
                    "<a href=\"#basics\" style=\"color:var(--gold);font-weight:700\">SEO Basics</a> -- es el "
                    "piso técnico sobre el que toda página debería pararse antes de que ese trabajo siquiera "
                    "empiece. Una página perfectamente escrita sobre una base técnicamente rota igual tiene "
                    "problemas para posicionarse."])
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
    ], steps_es=[
        ("Ve a google.com/business e inicia sesión", "Usa la cuenta de Google que tu negocio ya usa, o crea "
         "una dedicada al negocio -- no una personal a la que un empleado podría perder acceso."),
        ("Busca el nombre de tu negocio primero", "Si ya existe un listado (a veces se crea automáticamente a "
         "partir de reseñas o datos de mapas), reclámalo en vez de crear un duplicado."),
        ("Ingresa los datos de tu negocio", "Nombre legal exacto, dirección, teléfono, categoría y horario -- "
         "esto se vuelve la versión de referencia que otros directorios suelen tomar."),
        ("Elige un método de verificación", "Usualmente una postal enviada a la dirección del negocio, a veces "
         "teléfono o correo para negocios elegibles -- sigue el que Google te ofrezca."),
        ("Completa el perfil después de verificar", "Agrega fotos, una descripción, servicios/productos, y "
         "mantén el horario al día -- un perfil sin verificar o vacío se posiciona peor que uno completo."),
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
    tag_attr = CC._es_attr("LO MÁS IMPORTANTE")
    h2_attr = CC._es_attr("Google Business Profile")
    lead_attr = CC._es_attr("El listado de mayor impacto para búsquedas locales y Google Maps -- haz este "
        "primero si no haces nada más.")
    return f"""<section class="sec cluster" id="google"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag"{tag_attr}>MOST IMPORTANT</span><h2{h2_attr}>Google Business Profile</h2>
  <p class="lead"{lead_attr}>The single highest-impact listing for local search and Google Maps -- do this one first if you do nothing else.</p></div>
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
    ], steps_es=[
        ("Ve a Bing Places for Business", "Inicia sesión con una cuenta de Microsoft."),
        ("Importa desde Google, o agrégalo a mano", "Bing ofrece una importación directa desde un Google "
         "Business Profile existente, que suele ser más rápido que empezar de cero."),
        ("Verifica tu listado", "Opciones similares a Google -- teléfono, postal o correo según la "
         "elegibilidad."),
        ("Mantenlo sincronizado con Google", "Bing sigue impulsando una parte importante de las búsquedas y "
         "los asistentes de voz -- no dejes que se desactualice solo porque Google se lleva la atención."),
    ])
    tag_attr = CC._es_attr("NO TE SALTES ESTE")
    h2_attr = CC._es_attr("Bing Places for Business")
    lead_attr = CC._es_attr("Menos participación de búsqueda que Google, pero gratis, rápido de configurar, y "
        "sigue siendo tráfico real.")
    return f"""<section class="sec cluster" id="bing"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag"{tag_attr}>DON'T SKIP THIS ONE</span><h2{h2_attr}>Bing Places for Business</h2>
  <p class="lead"{lead_attr}>Smaller share of search than Google, but free, fast to set up, and still real traffic.</p></div>
  <div class="prose">{steps}</div>
</div></section>"""

def listings_apple():
    steps = CC.steps_list([
        ("Go to Apple Business Connect", "Sign in with an Apple ID."),
        ("Claim or add your location", "Apple will try to match an existing listing from Apple Maps data first."),
        ("Verify ownership", "Options vary by business type -- phone verification is common."),
        ("Fill out the profile", "Hours, photos, and a short description show up directly in Apple Maps and Siri results."),
    ], steps_es=[
        ("Ve a Apple Business Connect", "Inicia sesión con un Apple ID."),
        ("Reclama o agrega tu ubicación", "Apple intentará primero encontrar un listado existente a partir de "
         "datos de Apple Maps."),
        ("Verifica la propiedad", "Las opciones varían según el tipo de negocio -- la verificación por "
         "teléfono es común."),
        ("Completa el perfil", "El horario, las fotos y una breve descripción aparecen directamente en Apple "
         "Maps y en los resultados de Siri."),
    ])
    tag_attr = CC._es_attr("PARTICIPACIÓN EN CRECIMIENTO")
    h2_attr = CC._es_attr("Apple Business Connect")
    lead_attr = CC._es_attr("Todo usuario de iPhone que busca en Apple Maps o le pregunta a Siri por un "
        "negocio toma la información de este listado.")
    return f"""<section class="sec cluster" id="apple"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag"{tag_attr}>GROWING SHARE</span><h2{h2_attr}>Apple Business Connect</h2>
  <p class="lead"{lead_attr}>Every iPhone user searching Apple Maps or asking Siri for a business pulls from this listing.</p></div>
  <div class="prose">{steps}</div>
</div></section>"""

def listings_nap():
    body = CC.tip_box("NAP = NAME, ADDRESS, PHONE",
        "Every listing above should show the <strong>exact same</strong> business name, address, and phone "
        "number -- down to how the street type is abbreviated (\"St\" vs \"Street\"). Inconsistent NAP data "
        "across listings is one of the most common, most avoidable reasons a business underperforms in local "
        "search -- it actively confuses search engines about which listing is authoritative.",
        "Keep a single reference doc with the exact, final wording of your name/address/phone, and copy from "
        "it every time -- never retype it from memory into a new directory.",
        label_es="NAP = NOMBRE, DIRECCIÓN, TELÉFONO",
        es=["Cada listado de arriba debería mostrar exactamente el mismo nombre de negocio, dirección y "
            "teléfono -- <strong>exactamente igual</strong>, hasta cómo se abrevia el tipo de calle (\"Av.\" "
            "vs \"Avenida\"). Los datos NAP inconsistentes entre listados son una de las razones más comunes "
            "y más evitables de que un negocio tenga bajo rendimiento en búsquedas locales -- confunde "
            "activamente a los motores de búsqueda sobre qué listado es el autoritativo.",
            "Mantén un solo documento de referencia con la redacción exacta y final de tu nombre/dirección/"
            "teléfono, y cópialo de ahí cada vez -- nunca lo vuelvas a escribir de memoria en un nuevo "
            "directorio."])
    tag_attr = CC._es_attr("EL ERROR MÁS COMÚN")
    h2_attr = CC._es_attr("Mantén cada listado consistente")
    return f"""<section class="sec" style="background:var(--panel);border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)" id="nap"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag"{tag_attr}>THE MOST COMMON MISTAKE</span><h2{h2_attr}>Keep every listing consistent</h2></div>
  <div class="prose">{body}</div>
</div></section>"""

LISTINGS_JUMP_ITEMS = [
    ("google", "Google Business Profile", "Google Business Profile"),
    ("bing", "Bing Places", "Bing Places"),
    ("apple", "Apple Business Connect", "Apple Business Connect"),
    ("nap", "Staying Consistent", "Mantén la Consistencia"),
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
  <button class="tab-btn active" type="button" data-tab="basics" role="tab" aria-selected="true" data-es="SEO Basics">SEO Basics</button>
  <button class="tab-btn" type="button" data-tab="built" role="tab" aria-selected="false" data-es="Built SEO-Ready">Built SEO-Ready</button>
  <button class="tab-btn" type="button" data-tab="listings" role="tab" aria-selected="false" data-es="Listados de Negocio">Business Listings</button>
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
              "listings — three tabs, no jargon, written for a wide audience, not just marketers.",
              tag_es="SEO 101", h1_es="Todo gratis, en un solo lugar",
              lead_es="Lo básico de SEO, qué incluye realmente un sitio bien listo para SEO, y cómo configurar "
              "tus listados de negocio — tres pestañas, sin jerga, escrito para un público amplio, no solo "
              "para mercadólogos.")
        + tabs_nav()
        + panel_basics()
        + panel_built()
        + panel_listings()
        + f'<section class="sec" style="padding-top:0"><div class="wrap">'
          + CC.inline_cta("Want a site built with all of this already done for you?",
                           "https://maintain.style/portfolio.html", "View SEO-Ready Sites",
                           text_es="¿Quieres un sitio construido con todo esto ya hecho por ti?",
                           label_es="Ver Sitios Listos para SEO")
          + "</div></section>"
        + S.footer()
        + S.back_to_top()
        + tabs_script()
        + S.close_html()
    )
    S.write_page("seo-101.html", html)

if __name__ == "__main__":
    build()
