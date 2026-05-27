#!/usr/bin/env python3
"""Build professional, self-contained HTML legal pages from the Markdown sources.

No third-party dependencies — handles the Markdown subset used in PRIVACY.md /
TERMS.md (headings, bold, italic, inline code, links, bullet/numbered lists,
horizontal rules, blockquotes, paragraphs). Run:  python3 build.py
"""
import html
import re
import pathlib

ROOT = pathlib.Path(__file__).parent


# ---------- inline ----------
def render_inline(text: str) -> str:
    # 1. stash inline code so its contents aren't reformatted
    code = []
    def _stash(m):
        code.append(m.group(1))
        return f"\x00C{len(code)-1}\x00"
    text = re.sub(r"`([^`]+)`", _stash, text)
    # 2. escape HTML
    text = html.escape(text, quote=False)
    # 3. links [label](url)
    def _link(m):
        label, url = m.group(1), m.group(2)
        ext = ' target="_blank" rel="noopener"' if url.startswith("http") else ""
        return f'<a href="{url}"{ext}>{label}</a>'
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link, text)
    # 4. bold then italic
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    # 5. restore code (escaped)
    for i, c in enumerate(code):
        text = text.replace(f"\x00C{i}\x00", f"<code>{html.escape(c, quote=False)}</code>")
    return text


# ---------- block ----------
def render_body(md: str) -> str:
    lines = md.split("\n")
    out, para, i, n = [], [], 0, len(lines)

    def flush():
        if para:
            joined = " ".join(l.strip() for l in para).strip()
            if joined:
                out.append(f"<p>{render_inline(joined)}</p>")
            para.clear()

    while i < n:
        raw = lines[i]
        s = raw.strip()
        if not s:
            flush(); i += 1; continue
        if s == "---":
            flush(); out.append("<hr>"); i += 1; continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            flush(); lvl = len(m.group(1))
            out.append(f"<h{lvl}>{render_inline(m.group(2).strip())}</h{lvl}>"); i += 1; continue
        if s.startswith(">"):
            flush(); bq = []
            while i < n and lines[i].strip().startswith(">"):
                bq.append(render_inline(lines[i].strip()[1:].strip())); i += 1
            out.append("<blockquote>" + "<br>".join(bq) + "</blockquote>"); continue
        if re.match(r"^[-*]\s+", s):
            flush(); items = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append("<li>" + render_inline(re.sub(r"^[-*]\s+", "", lines[i].strip())) + "</li>"); i += 1
            out.append("<ul>" + "".join(items) + "</ul>"); continue
        if re.match(r"^\d+\.\s+", s):
            flush(); items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append("<li>" + render_inline(re.sub(r"^\d+\.\s+", "", lines[i].strip())) + "</li>"); i += 1
            out.append("<ol>" + "".join(items) + "</ol>"); continue
        para.append(raw); i += 1
    flush()
    return "\n".join(out)


LOGO = (
    '<svg class="mark" width="30" height="30" viewBox="0 0 32 32" aria-hidden="true">'
    '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#ff9a3d"/><stop offset="1" stop-color="#ef3e2a"/>'
    '</linearGradient></defs>'
    '<rect width="32" height="32" rx="8" fill="url(#g)"/>'
    '<path d="M9 23 L15 9 a1.6 1.6 0 0 1 2.9 0 L24 23" fill="none" stroke="#fff" '
    'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
    '<circle cx="16" cy="23" r="2.1" fill="#fff"/></svg>'
)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Haulbeam</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<style>
:root{{--ink:#16181d;--muted:#6b7280;--line:#ececf0;--bg:#fff;--page:#f4f5f7;--a:#ee4a27;}}
*{{box-sizing:border-box;}}
html{{-webkit-text-size-adjust:100%;}}
body{{margin:0;background:var(--page);color:var(--ink);
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
line-height:1.66;font-size:16px;}}
a{{color:var(--a);}}
.bar{{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.86);backdrop-filter:saturate(160%) blur(10px);
border-bottom:1px solid var(--line);}}
.bar .in{{max-width:840px;margin:0 auto;padding:13px 22px;display:flex;align-items:center;gap:11px;}}
.brand{{display:flex;align-items:center;gap:9px;font-weight:750;font-size:17px;letter-spacing:.2px;text-decoration:none;color:var(--ink);}}
.brand .mark{{display:block;border-radius:8px;}}
.nav{{margin-left:auto;display:flex;gap:6px;}}
.nav a{{font-size:14px;color:var(--muted);text-decoration:none;padding:6px 11px;border-radius:8px;}}
.nav a:hover{{color:var(--ink);background:#f0f1f4;}}
.nav a.on{{color:var(--a);font-weight:600;}}
.wrap{{max-width:760px;margin:30px auto 70px;background:var(--bg);border:1px solid var(--line);
border-radius:16px;padding:46px clamp(20px,5vw,56px);box-shadow:0 1px 2px rgba(16,24,40,.04),0 10px 30px rgba(16,24,40,.05);}}
h1{{font-size:clamp(26px,5vw,33px);line-height:1.18;letter-spacing:-.5px;margin:0 0 6px;}}
h2{{font-size:20px;letter-spacing:-.2px;margin:2em 0 .5em;padding-top:1.1em;border-top:1px solid var(--line);}}
h3{{font-size:16.5px;margin:1.5em 0 .4em;}}
p,li{{font-size:15.5px;color:#26282e;}}
ul,ol{{padding-left:22px;}}
li{{margin:.32em 0;}}
strong{{font-weight:660;color:var(--ink);}}
hr{{border:0;border-top:1px solid var(--line);margin:1.7em 0;}}
code{{background:#f1f1f4;padding:1.5px 6px;border-radius:6px;font-size:13.5px;
font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:#b23218;}}
blockquote{{margin:1.3em 0;padding:15px 20px;background:#fff7f3;border:1px solid #fbe0d3;
border-left:3px solid var(--a);border-radius:10px;color:#34261f;font-size:14.5px;}}
blockquote strong{{color:#7a2e16;}}
.meta{{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 8px;}}
.pill{{display:inline-block;font-size:12.5px;color:var(--muted);background:#f3f4f6;
border:1px solid var(--line);border-radius:999px;padding:4px 11px;}}
.lead em{{color:var(--muted);}}
footer{{max-width:760px;margin:0 auto 56px;padding:0 22px;color:var(--muted);font-size:13px;
display:flex;flex-wrap:wrap;gap:6px 16px;align-items:center;}}
footer a{{color:var(--muted);text-decoration:none;}}
footer a:hover{{color:var(--a);}}
footer .sp{{margin-left:auto;}}
/* index cards */
.cards{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:26px 0 6px;}}
@media(max-width:560px){{.cards{{grid-template-columns:1fr;}}}}
.card{{display:block;text-decoration:none;color:inherit;border:1px solid var(--line);
border-radius:14px;padding:22px;transition:border-color .15s,box-shadow .15s,transform .15s;background:#fff;}}
.card:hover{{border-color:#f6cab8;box-shadow:0 8px 24px rgba(16,24,40,.07);transform:translateY(-1px);}}
.card h3{{margin:.1em 0 .35em;font-size:17px;}}
.card p{{margin:0;font-size:14px;color:var(--muted);}}
.card .go{{margin-top:14px;font-size:13.5px;font-weight:600;color:var(--a);}}
</style>
</head>
<body>
<div class="bar"><div class="in">
<a class="brand" href="index.html">{logo}<span>Haulbeam</span></a>
<nav class="nav"><a href="privacy.html"{p_on}>Privacy</a><a href="terms.html"{t_on}>Terms</a></nav>
</div></div>
<main class="wrap">
{body}
</main>
<footer>
<span>© 2026 Haulbeam</span><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a>
<a class="sp" href="mailto:support@famlok.online">support@famlok.online</a>
</footer>
</body>
</html>
"""


def build_doc(md_name, out_name, title, desc, active):
    md = (ROOT / md_name).read_text(encoding="utf-8")
    body = render_body(md)
    html_out = PAGE.format(
        title=title, desc=desc, logo=LOGO, body=body,
        p_on=' class="on"' if active == "privacy" else "",
        t_on=' class="on"' if active == "terms" else "",
    )
    (ROOT / out_name).write_text(html_out, encoding="utf-8")
    print(f"  wrote {out_name}  ({len(html_out):,} bytes)")


INDEX_BODY = """<h1>Haulbeam — Legal</h1>
<p class="lead"><em>Truck-safe navigation for Australia. The documents below explain how Haulbeam handles your information and the terms that apply when you use the app.</em></p>
<div class="cards">
<a class="card" href="privacy.html"><h3>Privacy Policy</h3><p>What we collect, how it's used, who we share it with, and how to access or delete your data.</p><div class="go">Read the Privacy Policy →</div></a>
<a class="card" href="terms.html"><h3>Terms of Use</h3><p>The agreement for using Haulbeam, including the safety disclaimer and subscription terms.</p><div class="go">Read the Terms of Use →</div></a>
</div>
<hr>
<p style="font-size:13.5px;color:#6b7280;">Questions? Contact <a href="mailto:support@famlok.online">support@famlok.online</a>.</p>"""


def main():
    print("Building Haulbeam legal pages…")
    build_doc("PRIVACY.md", "privacy.html", "Privacy Policy",
              "How Haulbeam collects, uses, stores and shares your information.", "privacy")
    build_doc("TERMS.md", "terms.html", "Terms of Use",
              "The terms that apply when you use the Haulbeam app.", "terms")
    idx = PAGE.format(title="Legal", desc="Haulbeam privacy policy and terms of use.",
                      logo=LOGO, body=INDEX_BODY, p_on="", t_on="")
    (ROOT / "index.html").write_text(idx, encoding="utf-8")
    print("  wrote index.html")
    print("Done.")


if __name__ == "__main__":
    main()
