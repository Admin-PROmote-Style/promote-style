# -*- coding: utf-8 -*-
"""
build_built_seo_ready.py -- the proof/sales page. Every technical claim here
is verified against mAIntAIn Style's actual build_common.py implementation
(SITE/build-scripts/site_common.py) as of 2026-08-17 -- not generic SEO
advice, a description of what this family of sites' build script literally
outputs on every page. Do not add a claim here without checking it against
site_common.py first.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

TECH_ITEMS = [
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

def tech_grid():
    cards = "".join(
        f'<div class="topic"><h3>{t}</h3><p>{d}</p></div>' for t, d in TECH_ITEMS)
    return f"""<section class="sec cluster" id="whats-included"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag">WHAT SHIPS ON EVERY PAGE</span>
  <h2>Not advice. A description of what actually gets built.</h2>
  <p class="lead">Every item below is verified against mAIntAIn Style's real build script, not a generic best-practices list -- if it's here, it's in the code.</p></div>
  <div class="topic-grid">{cards}</div>
</div></section>"""

def comparison():
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

def build():
    title = "Built SEO-Ready — What a Properly-Built Site Actually Includes | PROmote Style"
    desc = ("A concrete, verified look at what \"SEO-ready\" should mean technically -- schema markup, sitemap, "
            "canonical tags, mobile-first, and more -- and how mAIntAIn Style sites ship with it by default.")
    extra_css = f"<style>{CC.content_css()}</style>"
    html = (
        S.head(title, desc, "built-seo-ready.html")
        + extra_css
        + S.nav("built-seo-ready.html")
        + CC.article_hero("BUILT SEO-READY", "“SEO-ready” shouldn't be a marketing phrase",
              "It should be a checklist you can actually verify. Here's exactly what that means technically -- "
              "and proof it's not just a claim.")
        + tech_grid()
        + comparison()
        + f'<section class="sec"><div class="wrap"><div class="prose">'
          + CC.tip_box("WORTH KNOWING",
                "None of this replaces content and keyword work covered in <a href=\"seo-basics.html\" "
                "style=\"color:var(--gold);font-weight:700\">SEO Basics</a> -- it's the technical floor every "
                "page should stand on before that work even starts. A perfectly-written page on a technically "
                "broken foundation still struggles to rank.")
          + "</div></div></section>"
        + f'<section class="sec" style="padding-top:0"><div class="wrap">'
          + CC.inline_cta("Want a site built this way from the first day it goes live, "
                           "not retrofitted later?", "https://maintain.style", "Talk to mAIntAIn Style")
          + "</div></section>"
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("built-seo-ready.html", html)

if __name__ == "__main__":
    build()
