# -*- coding: utf-8 -*-
"""
build_seo_basics.py -- the SEO Basics resource hub. Content grounded in what
people actually search for beginner SEO/keyword-research questions (checked
via web search 2026-08-17 against Mangools, WebFX, Ahrefs Academy, and
Desire Marketing's SEO FAQ, among others -- see chat for sources). Wide,
beginner-friendly audience per George's instruction -- not restaurant/local-
business specific.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

JUMP_ITEMS = [
    ("foundations", "Foundations"),
    ("keywords", "Keywords"),
    ("backlinks", "Backlinks & Authority"),
    ("tools", "Free Tools"),
]

def foundations():
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
            "need to figure out what a page is about and whether to trust it. The mechanics underneath are the same."),
    ])
    return CC.cluster("foundations", "START HERE", "Foundations",
        "The handful of concepts everything else in SEO builds on top of.", topics)

def keywords():
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
    ])
    return CC.cluster("keywords", "THE CORE SKILL", "Keywords: finding what people actually search",
        "This is the part most beginners skip past — and the part that matters most.", topics)

def backlinks():
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

def tools():
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
    ])
    return CC.cluster("tools", "GET SET UP", "Free tools worth using today",
        "No budget required to start doing this properly.", topics)

def build():
    title = "SEO Basics — Free Beginner's Guide to Keywords & Search | PROmote Style"
    desc = ("A free, plain-English SEO basics guide: what SEO actually is, how to find keywords people are "
            "really searching for, why backlinks still matter, and which free tools to use to get started.")
    extra_css = f"<style>{CC.content_css()}</style>"
    html = (
        S.head(title, desc, "seo-basics.html")
        + extra_css
        + S.nav("seo-basics.html")
        + CC.article_hero("SEO BASICS", "SEO basics, explained without the jargon",
              "Everything a total beginner needs to understand search, find the right keywords, and know what "
              "to do next — free, and written for a wide audience, not just marketers.")
        + CC.jump_nav(JUMP_ITEMS)
        + foundations()
        + keywords()
        + backlinks()
        + tools()
        + f'<section class="sec" style="padding-top:0"><div class="wrap">'
          + CC.inline_cta("Curious what a site built with all of this <strong>already done for you</strong> looks like?",
                           "built-seo-ready.html", "See a Built SEO-Ready Site")
          + "</div></section>"
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("seo-basics.html", html)

if __name__ == "__main__":
    build()
