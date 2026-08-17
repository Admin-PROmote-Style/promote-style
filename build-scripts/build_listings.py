# -*- coding: utf-8 -*-
"""
build_listings.py -- search engine business listing setup guide. Covers the
accounts a business needs to claim to show up in local/map search: Google
Business Profile, Bing Places, Apple Business Connect, plus NAP consistency.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C
import site_common as S
import content_common as CC

JUMP_ITEMS = [
    ("google", "Google Business Profile"),
    ("bing", "Bing Places"),
    ("apple", "Apple Business Connect"),
    ("nap", "Staying Consistent"),
]

def google():
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
    return f"""<section class="sec cluster" id="google"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag">MOST IMPORTANT</span><h2>Google Business Profile</h2>
  <p class="lead">The single highest-impact listing for local search and Google Maps -- do this one first if you do nothing else.</p></div>
  <div class="prose">{steps}</div>
</div></section>"""

def bing():
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

def apple():
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

def nap():
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

def build():
    title = "Search Engine Business Listings Setup Guide | PROmote Style"
    desc = ("Step-by-step setup for Google Business Profile, Bing Places, and Apple Business Connect -- plus "
            "why NAP consistency across listings matters more than most businesses realize.")
    extra_css = f"<style>{CC.content_css()}</style>"
    html = (
        S.head(title, desc, "listings.html")
        + extra_css
        + S.nav("listings.html")
        + CC.article_hero("BUSINESS LISTINGS", "Get your business set up where people search",
              "Free accounts, real steps, done in one sitting. This is what actually gets you found on Google "
              "Maps, Bing, and Apple Maps.")
        + CC.jump_nav(JUMP_ITEMS)
        + google()
        + bing()
        + apple()
        + nap()
        + f'<section class="sec" style="padding-top:0"><div class="wrap">'
          + CC.inline_cta("Want your listings and your site working together instead of set up once and forgotten?",
                           "https://maintain.style", "Talk to mAIntAIn Style")
          + "</div></section>"
        + S.footer()
        + S.back_to_top()
        + S.close_html()
    )
    S.write_page("listings.html", html)

if __name__ == "__main__":
    build()
