# -*- coding: utf-8 -*-
"""Builds the static legal site into docs/ (GitHub Pages serves that folder).

  python build.py           final build: refuses to run while a placeholder is left
  python build.py --draft   builds anyway, placeholders stay visible
"""
import html
import json
import os
import sys

from content import GOOGLE_ADS_URL, LANGS, PRIVACY_URL_GOOGLE

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "docs")
draft = "--draft" in sys.argv

with open(os.path.join(HERE, "site.json"), encoding="utf-8") as f:
    site = json.load(f)

left = [k for k in ("NAME", "ADDRESS", "EMAIL") if site[k].startswith("[")]
if left and not draft:
    sys.exit(f"Placeholders left in site.json: {', '.join(left)}. Fill them in or use --draft.")

CSS = """
:root { color-scheme: light dark; --bg:#fff; --fg:#1d2127; --muted:#5b6370; --line:#d8dce3; --accent:#1d4cc2; }
@media (prefers-color-scheme: dark) { :root { --bg:#1b1e24; --fg:#e8eaee; --muted:#a3aab6; --line:#343a45; --accent:#8fb0ff; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }
main { max-width:760px; margin:0 auto; padding:24px 20px 64px; }
nav { display:flex; flex-wrap:wrap; gap:6px 18px; padding-bottom:14px; border-bottom:1px solid var(--line); margin-bottom:22px; }
nav a { color:var(--accent); text-decoration:none; font-weight:600; }
nav a.on { color:var(--fg); border-bottom:2px solid var(--fg); }
h1 { font-size:1.7rem; line-height:1.25; margin:0 0 4px; }
h2 { font-size:1.15rem; margin:30px 0 6px; }
p, li { margin:8px 0; } ul { padding-inline-start:22px; }
.meta { color:var(--muted); font-size:.92rem; margin:0 0 8px; }
a { color:var(--accent); }
.langs { display:flex; flex-wrap:wrap; gap:10px; margin:12px 0 28px; }
.langs a { border:1px solid var(--line); border-radius:8px; padding:8px 14px; text-decoration:none; font-weight:600; }
.pick h2 { margin-top:22px; }
"""


def fill(text):
    return (text.replace("{NAME}", html.escape(site["NAME"])).replace("{ADDRESS}", html.escape(site["ADDRESS"]))
            .replace("{EMAIL}", f'<a href="mailto:{html.escape(site["EMAIL"])}">{html.escape(site["EMAIL"])}</a>'))


def para(p):
    text = html.escape(p, quote=False)
    text = text.replace("{G1}", f'<a href="{PRIVACY_URL_GOOGLE}">{PRIVACY_URL_GOOGLE}</a>')
    text = text.replace("{G2}", f'<a href="{GOOGLE_ADS_URL}">{GOOGLE_ADS_URL}</a>')
    # placeholders were escaped as text: braces survive html.escape
    return fill(text.replace(html.escape(site["NAME"]), site["NAME"]))


def sections_html(sections):
    out = []
    for heading, paras in sections:
        out.append(f"<h2>{html.escape(heading)}</h2>")
        for p in paras:
            if isinstance(p, list):
                out.append("<ul>" + "".join(f"<li>{fill(para(i))}</li>" for i in p) + "</ul>")
            else:
                out.append(f"<p>{fill(para(p))}</p>")
    return "\n".join(out)


def nav_html(lang, current):
    n = LANGS[lang]["nav"]
    items = [("index.html", n["home"], "home"), (f"privacy-{lang}.html", n["privacy"], "privacy"),
             (f"support-{lang}.html", n["support"], "support"), (f"legal-{lang}.html", n["legal"], "legal")]
    links = "".join(f'<a href="{href}"{" class=on" if key == current else ""}>{html.escape(label)}</a>' for href, label, key in items)
    other = "".join(f'<a href="{page(current if current != "home" else "privacy", l)}">{LANGS[l]["name"]}</a>'
                    for l in LANGS if l != lang)
    return f"<nav>{links}<span style='flex:1'></span>{other}</nav>"


def page(kind, lang):
    return "index.html" if kind == "home" else f"{kind}-{lang}.html"


def write(name, lang, title, body, current):
    L = LANGS[lang]
    doc = f"""<!doctype html>
<html lang="{lang}" dir="{L['dir']}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><style>{CSS}</style></head>
<body><main>
{nav_html(lang, current)}
<h1>{html.escape(title)}</h1>
{body}
</main></body></html>
"""
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(doc)


os.makedirs(OUT, exist_ok=True)
for old in os.listdir(OUT):
    if old.endswith(".html"):
        os.remove(os.path.join(OUT, old))
open(os.path.join(OUT, ".nojekyll"), "w").close()

for lang, L in LANGS.items():
    upd = f'<p class="meta">{html.escape(L["updated_label"])}: {html.escape(site["UPDATED"][lang])}</p>'
    write(f"privacy-{lang}.html", lang, L["privacy_title"], upd + sections_html(L["privacy"]), "privacy")
    write(f"support-{lang}.html", lang, L["support_title"], sections_html(L["support"]), "support")
    write(f"legal-{lang}.html", lang, L["legal_title"], sections_html(L["legal"]), "legal")

# Language chooser
cards = []
for lang, L in LANGS.items():
    n = L["nav"]
    cards.append(f'<div class="pick" lang="{lang}" dir="{L["dir"]}"><h2>{html.escape(L["name"])}</h2>'
                 f'<a href="privacy-{lang}.html">{html.escape(n["privacy"])}</a> · '
                 f'<a href="support-{lang}.html">{html.escape(n["support"])}</a> · '
                 f'<a href="legal-{lang}.html">{html.escape(n["legal"])}</a></div>')
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Nailgoal</title><style>{CSS}</style></head>
<body><main><h1>Nailgoal</h1>
<p class="meta">Privacy · Datenschutz · Gizlilik · Confidentialité · Privacy · Privasi · Конфиденциальность · プライバシー · 개인정보 · الخصوصية</p>
{''.join(cards)}
</main></body></html>
""")

print("built", len(os.listdir(OUT)), "files into", OUT, "(draft)" if draft else "")
