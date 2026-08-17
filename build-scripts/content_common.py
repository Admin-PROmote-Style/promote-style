# -*- coding: utf-8 -*-
"""
content_common.py -- ADDITIVE CSS/helpers for long-form resource pages
(SEO Basics, Built SEO-Ready, Business Listings). Kept separate from
site_common.py on purpose: site_common.py is shared mS-family scaffolding
(nav/footer/hero/cards geometry) and is "rarely edited" per house rule.
Nothing here overrides or removes anything in site_common's base_css() --
it only adds new component classes for prose/guide-style content that the
fixed scaffolding doesn't need to cover (client sites are short marketing
pages, not long-form guides).
"""

import html as _html

def _esc(s):
    return _html.escape(s, quote=True) if s else ""

def _es_attr(text):
    """textContent-swap attribute for plain-text fields."""
    return f' data-es="{_esc(text)}"' if text else ""

def _es_html_attr(text):
    """innerHTML-swap attribute for fields that may contain inline markup
    (e.g. <code>, <strong>). Safe for plain text too."""
    return f' data-es-html="{_esc(text)}"' if text else ""

def content_css():
    return """
.article-hero{padding:64px 0 48px;text-align:center}
.article-hero h1{font-size:clamp(28px,4.2vw,44px);max-width:820px;margin:0 auto 16px}
.article-hero .lead{max-width:680px;margin:0 auto}
.cluster{padding:0 0 64px}
.cluster-head{max-width:760px;margin:0 auto 28px}
.cluster-head .sec-tag{display:block;margin-bottom:8px}
.cluster-head h2{font-size:clamp(22px,3vw,30px);margin-bottom:10px}
.topic-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}
.topic{background:var(--panel);border:1px solid rgba(255,255,255,.07);border-radius:14px;padding:24px 26px}
.topic h3{font-size:18px;margin-bottom:8px}
.topic p{color:var(--cream-muted);font-size:14.5px;margin-bottom:0}
.topic .q{color:var(--gold);font-weight:700;font-size:12.5px;letter-spacing:.05em;text-transform:uppercase;display:block;margin-bottom:8px}
.tip-box{background:var(--panel2);border-left:4px solid var(--gold);border-radius:10px;padding:20px 24px;margin:28px 0}
.tip-box .lbl{color:var(--gold);font-weight:700;font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;display:block;margin-bottom:8px}
.tip-box p{color:var(--cream);font-size:15px;margin:0}
.tip-box p+p{margin-top:10px}
.steps-list{counter-reset:step;margin:24px 0}
.steps-list .step{display:flex;gap:18px;padding:18px 0;border-top:1px solid rgba(255,255,255,.07)}
.steps-list .step:first-child{border-top:0}
.steps-list .step .n{counter-increment:step;flex:0 0 auto;width:36px;height:36px;border-radius:50%;background:var(--panel);border:1.5px solid var(--gold-deep);color:var(--gold);font-family:var(--font-head);font-weight:700;display:flex;align-items:center;justify-content:center;font-size:14px}
.steps-list .step .body h4{font-size:16.5px;margin-bottom:6px}
.steps-list .step .body p{color:var(--cream-muted);font-size:14.5px;margin:0}
.prose{max-width:760px;margin:0 auto}
.prose p{color:var(--cream-muted);font-size:15.5px;margin-bottom:16px}
.prose h3{font-size:19px;margin:30px 0 10px}
.inline-cta{background:linear-gradient(135deg,var(--panel2),var(--panel));border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:26px 28px;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;margin:36px 0}
.inline-cta p{margin:0;font-size:15px;color:var(--cream);max-width:520px}
.inline-cta p strong{color:var(--gold)}
.jump-nav{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin:26px 0 8px}
.jump-nav a{font-size:13px;font-weight:700;color:var(--cream-muted);background:var(--panel);border:1px solid rgba(255,255,255,.1);padding:8px 16px;border-radius:999px}
.jump-nav a:hover{color:var(--cream);border-color:var(--gold)}
/* tabs -- 2026-08-17: added for seo-101.html, which consolidates what used
   to be three separate pages (SEO Basics / Built SEO-Ready / Business
   Listings) into one page switched with tabs -- George's call, so the
   nav header only needs one link ("SEO 101") instead of three, and the
   site reads as one resource hub instead of three separate promo pages. */
.tabs-nav{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;padding:8px 0 12px}
.tab-btn{font-family:var(--font-body);font-weight:700;font-size:14.5px;letter-spacing:.01em;color:var(--cream-muted);background:var(--panel);border:1.5px solid rgba(255,255,255,.12);padding:13px 26px;border-radius:999px;cursor:pointer;transition:all .2s ease}
.tab-btn:hover{color:var(--cream);border-color:rgba(255,255,255,.32)}
.tab-btn.active{color:var(--ink);background:linear-gradient(100deg,var(--gold),var(--gold-deep));border-color:transparent}
.tab-panel[hidden]{display:none}
@media(max-width:900px){.topic-grid{grid-template-columns:1fr}.inline-cta{flex-direction:column;align-items:flex-start}}
@media(max-width:600px){.tabs-nav{gap:8px}.tab-btn{padding:10px 18px;font-size:13px}}
"""

def article_hero(tag, h1, lead, tag_es=None, h1_es=None, lead_es=None):
    return f"""<section class="article-hero"><div class="wrap">
  <span class="badge-pill"{_es_attr(tag_es)}>{tag}</span><h1{_es_html_attr(h1_es)}>{h1}</h1><p class="lead"{_es_attr(lead_es)}>{lead}</p>
</div></section>"""

def jump_nav(items):
    """items: list of (anchor, label) or (anchor, label, label_es).
    Spanish translation is opt-in per item -- untranslated items are simply
    left in English when the ESP toggle is on, until they're backfilled."""
    def _link(item):
        anchor, label = item[0], item[1]
        label_es = item[2] if len(item) > 2 else None
        return f'<a href="#{anchor}"{_es_attr(label_es)}>{label}</a>'
    links = "".join(_link(i) for i in items)
    return f'<div class="wrap"><nav class="jump-nav">{links}</nav></div>'

def cluster(anchor, tag, h2, lead, topics_html, tag_es=None, h2_es=None, lead_es=None):
    return f"""<section class="sec cluster" id="{anchor}"><div class="wrap">
  <div class="cluster-head"><span class="sec-tag"{_es_attr(tag_es)}>{tag}</span><h2{_es_html_attr(h2_es)}>{h2}</h2><p class="lead"{_es_attr(lead_es)}>{lead}</p></div>
  <div class="topic-grid">{topics_html}</div>
</div></section>"""

def topic(q, h3, body, q_es=None, h3_es=None, body_es=None):
    return f'<div class="topic"><span class="q"{_es_attr(q_es)}>{q}</span><h3{_es_attr(h3_es)}>{h3}</h3><p{_es_html_attr(body_es)}>{body}</p></div>'

def tip_box(label, *paragraphs, label_es=None, es=None):
    """es: optional list of Spanish paragraph strings, same order as paragraphs.
    Missing/short entries just stay English until translated."""
    parts = []
    for i, p in enumerate(paragraphs):
        p_es = es[i] if es and i < len(es) else None
        parts.append(f'<p{_es_html_attr(p_es)}>{p}</p>')
    return f'<div class="tip-box"><span class="lbl"{_es_attr(label_es)}>{label}</span>{"".join(parts)}</div>'

def steps_list(steps, steps_es=None):
    """steps_es: optional list of (title_es, desc_es) tuples parallel to steps."""
    items = []
    for i, (t, d) in enumerate(steps):
        t_es, d_es = (steps_es[i] if steps_es and i < len(steps_es) else (None, None))
        items.append(
            f'<div class="step"><div class="n"></div><div class="body">'
            f'<h4{_es_attr(t_es)}>{t}</h4><p{_es_html_attr(d_es)}>{d}</p></div></div>')
    return f'<div class="steps-list">{"".join(items)}</div>'

def inline_cta(text, href, label, text_es=None, label_es=None):
    return (f'<div class="inline-cta"><p{_es_html_attr(text_es)}>{text}</p>'
            f'<a class="btn btn-primary" href="{href}"{_es_attr(label_es)}>{label}</a></div>')
