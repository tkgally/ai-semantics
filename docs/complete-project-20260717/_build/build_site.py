#!/usr/bin/env python3
"""
One-time static-site builder for the ai-semantics repository.

Walks the repo, converts every (text) file to a human-readable HTML page under
docs/complete-project-20260717/, mirroring the directory structure so relative
links resolve. Generates per-directory index pages, a curated home page, a full
browse tree, and a single shared stylesheet.

Not part of the project's regular tooling; run once for the presentation snapshot.
"""
import os, sys, json, csv, html, io, shutil, re
import yaml
from datetime import datetime, timezone

import markdown as md_lib
from pygments import highlight
from pygments.lexers import get_lexer_for_filename, PythonLexer, TextLexer, BashLexer, get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

ROOT = "/home/user/ai-semantics"
OUTDIR = os.path.join(ROOT, "docs", "complete-project-20260717")
SNAPSHOT_LABEL = "July 2026"
SNAPSHOT_DIRNAME = "complete-project-20260717"

# ---- exclusion rules -------------------------------------------------------
# The six generated public-site pages: linked live instead of re-rendered.
GENERATED_SITE_HTML = {
    "docs/about.html", "docs/findings.html", "docs/glossary.html",
    "docs/index.html", "docs/journal.html", "docs/plans.html",
}
SKIP_BASENAMES = {".nojekyll", ".gitkeep", ".DS_Store"}
BINARY_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}
DOWNLOAD_EXTS = {".epub", ".pdf", ".zip"}

MAX_RICH_JSON = 180 * 1024   # files bigger than this use the lighter renderer

STYLE = r"""
/* Meaning in the Age of AI — complete-project snapshot.
   Single shared stylesheet. Warm paper palette from the public site,
   tuned for reading prose, code, and experimental data. */
:root{
  --ink:#1f2430; --ink-soft:#525a6b; --paper:#faf9f6; --card:#ffffff;
  --accent:#2a5d8f; --accent-soft:#e8eff6; --rule:#ddd8cd; --rule-soft:#ebe7dd;
  --good:#2e6e4e; --note:#8a6d1d; --mono:#eef1f4; --mono-ink:#233; --warn-bg:#fbf7ec;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:Georgia,"Times New Roman",serif;font-size:17px;line-height:1.62}
code,pre,.mono,.fpath,tt{font-family:"SFMono-Regular",Consolas,"Liberation Mono",Menlo,monospace}

/* project banner (top of every page) */
.proj-banner{background:#20293a;color:#eef2f7;font-family:"Helvetica Neue",Arial,sans-serif;
  font-size:.82rem;line-height:1.5;padding:.55rem 1rem;text-align:center}
.proj-banner strong{color:#fff}
.proj-banner em{color:#cfe0f0;font-style:italic}
.proj-banner .bn-note{display:inline-block;color:#aebdcf}
.proj-banner a.bn-home{color:#9ecbff;text-decoration:none;white-space:nowrap;margin-left:.3rem}
.proj-banner a.bn-home:hover{text-decoration:underline}

/* breadcrumbs */
nav.crumbs{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.8rem;
  background:var(--card);border-bottom:1px solid var(--rule);padding:.45rem 1rem;
  overflow-x:auto;white-space:nowrap}
nav.crumbs a{color:var(--accent);text-decoration:none}
nav.crumbs a:hover{text-decoration:underline}
nav.crumbs .cur{color:var(--ink);font-weight:bold}
nav.crumbs .sep{color:var(--ink-soft);margin:0 .1rem}

main{max-width:54rem;margin:0 auto;padding:1.4rem 1.2rem 3rem}
.page-head{border-bottom:1px solid var(--rule);margin-bottom:1.2rem;padding-bottom:.6rem}
.page-head h1{font-size:1.5rem;font-weight:normal;margin:.2rem 0 .35rem;word-break:break-word}
.subtitle{margin:0;color:var(--ink-soft);font-family:"Helvetica Neue",Arial,sans-serif;font-size:.85rem}
.subtitle .ftype{color:var(--accent);font-weight:bold}
.fpath{background:var(--mono);padding:.05rem .3rem;border-radius:3px;font-size:.86em}

a{color:var(--accent)}
h2{font-size:1.28rem;font-weight:normal;border-bottom:1px solid var(--rule-soft);
  padding-bottom:.2rem;margin-top:2rem}
h3{font-size:1.06rem;margin-top:1.6rem}

/* prose from markdown */
.md{}
.md h1{font-size:1.4rem;font-weight:normal}
.md img{max-width:100%;height:auto}
.md pre{background:var(--card);border:1px solid var(--rule);border-radius:6px;
  padding:.7rem .9rem;overflow-x:auto;font-size:.85rem;line-height:1.45}
.md code{background:var(--mono);padding:.05rem .3rem;border-radius:3px;font-size:.88em}
.md pre code{background:none;padding:0}
.md blockquote{border-left:4px solid var(--accent-soft);margin:1rem 0;padding:.2rem 1rem;
  color:var(--ink-soft);background:#fbfaf7}
.md table{border-collapse:collapse;margin:1rem 0;font-size:.92rem;display:block;overflow-x:auto}
.md table th,.md table td{border:1px solid var(--rule);padding:.35rem .6rem;text-align:left;vertical-align:top}
.md table th{background:var(--accent-soft)}
.md hr{border:none;border-top:1px solid var(--rule);margin:1.6rem 0}

/* front-matter box */
.frontmatter{background:var(--accent-soft);border:1px solid #cadaea;border-radius:6px;
  padding:.7rem .9rem;margin:0 0 1.4rem;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.84rem}
.fm-label{font-weight:bold;color:var(--accent);text-transform:uppercase;letter-spacing:.04em;
  font-size:.72rem;margin-bottom:.35rem}
.fm-table{border-collapse:collapse;width:100%}
.fm-table th{text-align:left;vertical-align:top;color:var(--ink-soft);font-weight:bold;
  padding:.12rem .8rem .12rem 0;white-space:nowrap;width:1%}
.fm-table td{vertical-align:top;padding:.12rem 0}
.fm-list{margin:0;padding-left:1.1rem}

/* code files (pygments wraps in .highlight) */
.highlight{background:var(--card);border:1px solid var(--rule);border-radius:6px;
  overflow-x:auto;font-size:.82rem;line-height:1.5;margin:0}
.highlight pre{margin:0;padding:.6rem .8rem}
.highlight .linenos{color:#b9b3a6;padding-right:.8rem;-webkit-user-select:none;user-select:none}
.highlight table{border-collapse:collapse;width:100%}
.highlight td.linenos{background:#f4f2ec;border-right:1px solid var(--rule);width:1%;white-space:nowrap}

/* plain text */
pre.plain{background:var(--card);border:1px solid var(--rule);border-radius:6px;
  padding:.7rem .9rem;overflow-x:auto;font-size:.85rem;line-height:1.5;white-space:pre-wrap;word-wrap:break-word}
pre.json-lite{background:var(--card);border:1px solid var(--rule);border-radius:6px;
  padding:.7rem .9rem;overflow-x:auto;font-size:.8rem;line-height:1.45}

/* JSON / data rendering */
.records{margin:.6rem 0}
.rec-count{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.78rem;color:var(--ink-soft);
  margin-bottom:.4rem;text-transform:uppercase;letter-spacing:.03em}
details.record,details.section{border:1px solid var(--rule);border-radius:5px;margin:.3rem 0;background:var(--card)}
details.record>summary,details.section>summary{cursor:pointer;padding:.4rem .7rem;
  font-family:"Helvetica Neue",Arial,sans-serif;font-size:.85rem;list-style-position:inside}
details.record>summary:hover,details.section>summary:hover{background:var(--accent-soft)}
.rec-i{display:inline-block;min-width:2.4rem;color:var(--accent);font-weight:bold}
.sec-k{color:var(--accent);font-weight:bold}
.pv-k{color:var(--note);font-weight:bold;margin-right:.2rem}
.pv-s{color:#2d4f2d}
details.record[open]>summary .pv-s,details.record[open]>summary .pv-k{opacity:.6}
.rec-body,.sec-body{padding:.3rem .8rem .7rem;border-top:1px solid var(--rule-soft)}
table.kv{border-collapse:collapse;width:100%;font-size:.86rem}
table.kv.top{margin-bottom:.8rem}
table.kv>tbody>tr>th{text-align:left;vertical-align:top;color:var(--ink-soft);font-weight:bold;
  padding:.15rem .8rem .15rem 0;white-space:nowrap;width:1%;border-bottom:1px solid var(--rule-soft)}
table.kv>tbody>tr>td{vertical-align:top;padding:.15rem 0;border-bottom:1px solid var(--rule-soft)}
.j-str{color:#2d4f2d}
.j-str.multiline,.j-str .multiline{display:block;white-space:pre-wrap;word-wrap:break-word;
  background:#f7faf7;border-left:3px solid #cfe0cf;padding:.3rem .5rem;margin:.15rem 0;font-size:.92em}
.j-num{color:#7a4b18}
.j-bool{color:#8a2a6b}
.j-null{color:#999}
ul.j-arr{margin:.1rem 0;padding-left:1.2rem}
ul.j-arr li{margin:.05rem 0}
.muted{color:var(--ink-soft);font-family:"Helvetica Neue",Arial,sans-serif;font-size:.85rem}
.trunc{margin-top:.4rem;font-style:italic}
.deadlink{color:var(--ink-soft);border-bottom:1px dotted #bbb;cursor:help}

/* data tables (csv) */
.table-wrap{overflow-x:auto;margin:1rem 0}
table.data{border-collapse:collapse;font-size:.85rem}
table.data th,table.data td{border:1px solid var(--rule);padding:.3rem .55rem;text-align:left}
table.data thead th{background:var(--accent-soft);position:sticky;top:0}

/* directory & file listings */
.dir-blurb{background:var(--accent-soft);border-left:4px solid var(--accent);padding:.6rem .9rem;
  border-radius:0 5px 5px 0;font-size:.95rem;margin:0 0 1.3rem}
ul.dir-list,ul.file-list,ul.entrylist{list-style:none;padding-left:0}
ul.dir-list li,ul.file-list li{padding:.28rem 0;border-bottom:1px solid var(--rule-soft)}
a.dir{font-weight:bold;font-family:"Helvetica Neue",Arial,sans-serif}
.dl-blurb{display:block;color:var(--ink-soft);font-size:.82rem;font-family:"Helvetica Neue",Arial,sans-serif;margin-top:.1rem}
.fmeta,.fsize{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.76rem;color:var(--ink-soft)}
ul.entrylist li{padding:.35rem 0;line-height:1.5}

/* home page */
.lead p{font-size:1.02rem}
.content-date{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.86rem;color:var(--ink-soft)}
.byline{background:var(--warn-bg);border-left:4px solid var(--note);padding:.8rem 1.1rem;border-radius:0 6px 6px 0}
.snapshot-facts{display:flex;flex-wrap:wrap;gap:.8rem;margin:1.6rem 0}
.snapshot-facts .fact{flex:1 1 8rem;background:var(--card);border:1px solid var(--rule);
  border-radius:6px;padding:.8rem;text-align:center}
.snapshot-facts .fn{display:block;font-size:1.7rem;color:var(--accent)}
.snapshot-facts .fl{display:block;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.76rem;color:var(--ink-soft)}
.toc{background:var(--card);border:1px solid var(--rule);border-radius:8px;padding:.6rem 1.3rem 1.2rem;margin:1.4rem 0}
.toc h3{margin-top:1.3rem}
.caveat{border-left:4px solid var(--note);background:var(--warn-bg);padding:.7rem 1.1rem;margin:1.6rem 0;font-size:.96rem}
.livelink{text-align:center;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.92rem;margin-top:2rem}

/* browse tree */
details.tree>summary{cursor:pointer;padding:.12rem 0;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.9rem}
.tree-file{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.85rem;padding:.05rem 0}
.tree-file a{text-decoration:none}

/* image viewer */
.img-view{text-align:center;margin:1rem 0}
.img-view img{max-width:100%;height:auto;border:1px solid var(--rule);border-radius:6px;background:#fff}

footer.foot{border-top:1px solid var(--rule);margin-top:2.5rem;padding:1.2rem;text-align:center;
  color:var(--ink-soft);font-family:"Helvetica Neue",Arial,sans-serif;font-size:.78rem;max-width:54rem;margin-left:auto;margin-right:auto}
footer.foot a{color:var(--accent)}
.foot-note{font-size:.72rem;color:#a09a8c;margin-top:.3rem}

@media (max-width:640px){
  body{font-size:16px}
  main{padding:1rem .8rem 2rem}
  table.kv>tbody>tr>th{white-space:normal}
}
"""


def rel(path):
    return os.path.relpath(path, ROOT)

def is_excluded(relpath):
    parts = relpath.split(os.sep)
    if parts[0] == ".git":
        return True
    if relpath.startswith(os.path.join("docs", SNAPSHOT_DIRNAME)):
        return True
    if relpath in GENERATED_SITE_HTML:
        return True
    if os.path.basename(relpath) in SKIP_BASENAMES:
        return True
    return False

# ---- collect the file list -------------------------------------------------
all_files = []   # repo-relative paths of files to render/copy
all_dirs = set()
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d != ".git"]
    for fn in filenames:
        full = os.path.join(dirpath, fn)
        r = rel(full)
        if is_excluded(r):
            continue
        all_files.append(r)
        d = os.path.dirname(r)
        while d:
            all_dirs.add(d)
            d = os.path.dirname(d)
all_dirs.add("")  # root
all_files.sort()
converted = set(all_files)  # every collected file becomes <path>.html (or a raw copy for binaries)

def kind_of(relpath):
    ext = os.path.splitext(relpath)[1].lower()
    if ext in BINARY_EXTS:
        return "image"
    if ext in DOWNLOAD_EXTS:
        return "download"
    return "text"

# ---- HTML escaping / small helpers ----------------------------------------
def esc(s):
    return html.escape(str(s), quote=True)

def depth_prefix(relpath):
    """relative prefix from OUTDIR/<relpath>.html back up to OUTDIR root."""
    d = os.path.dirname(relpath)
    n = 0 if d == "" else len(d.split(os.sep))
    return "../" * n

EXT_LABEL = {
    ".md": "Markdown", ".py": "Python", ".json": "JSON", ".jsonl": "JSON Lines",
    ".csv": "CSV", ".txt": "text", ".log": "log", ".sh": "shell", ".out": "output",
    ".sha256": "checksum", ".css": "CSS", ".html": "HTML", ".gitignore": "gitignore",
    ".yml": "YAML", ".yaml": "YAML", ".jpg": "image", ".jpeg": "image", ".png": "image",
    ".epub": "EPUB", ".mcp": "config",
}
def ext_label(relpath):
    b = os.path.basename(relpath)
    if b == ".gitignore":
        return "gitignore"
    if b == ".mcp.json":
        return "JSON (config)"
    ext = os.path.splitext(relpath)[1].lower()
    return EXT_LABEL.get(ext, ext.lstrip(".").upper() or "file")

# ---- link rewriting for markdown ------------------------------------------
def rewrite_href(href, cur_relpath):
    """Return a rewritten href, or None if it's an unresolved local link (make it a dead span)."""
    h = href.strip()
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', h):  # scheme (http, mailto, etc.)
        return href
    if h.startswith("//") or h.startswith("#") or h == "":
        return href
    if "#" in h:
        path, frag = h.split("#", 1)
        frag = "#" + frag
    else:
        path, frag = h, ""
    if path == "":
        return href
    base_dir = os.path.dirname(cur_relpath)
    target = os.path.normpath(os.path.join(base_dir, path))
    if target in converted:
        if kind_of(target) == "text":
            return path + ".html" + frag
        return path + frag  # binary/download: point at the raw copy
    if target in all_dirs:
        return path.rstrip("/") + "/index.html" + frag
    return None  # local path that does not exist in the snapshot -> dead link

A_FULL = re.compile(r'<a\b([^>]*?)\shref="([^"]*)"([^>]*?)>(.*?)</a>', re.IGNORECASE | re.DOTALL)

def rewrite_links_in_html(body_html, cur_relpath):
    def sub(m):
        pre, href, post, text = m.groups()
        new = rewrite_href(href, cur_relpath)
        if new is None:
            return f'<span class="deadlink" title="referenced page is not part of this snapshot">{text}</span>'
        return f'<a{pre} href="{esc_attr(new)}"{post}>{text}</a>'
    return A_FULL.sub(sub, body_html)

def esc_attr(s):
    return s.replace('"', "%22")

# ---- markdown rendering ----------------------------------------------------
def split_front_matter(text):
    if text.startswith("---\n") or text.startswith("---\r\n"):
        lines = text.splitlines(keepends=True)
        for i in range(1, len(lines)):
            if lines[i].rstrip("\r\n") == "---":
                fm = "".join(lines[1:i])
                body = "".join(lines[i+1:])
                try:
                    data = yaml.safe_load(fm)
                except Exception:
                    data = None
                return data, fm, body
    return None, None, text

def render_front_matter(data, raw_fm):
    if data is None:
        return ""
    rows = []
    def fmt(v):
        if isinstance(v, list):
            if not v:
                return "<span class='muted'>(none)</span>"
            items = []
            for it in v:
                if isinstance(it, dict):
                    items.append(", ".join(f"{esc(k)}: {esc(val)}" for k, val in it.items()))
                else:
                    items.append(esc(it))
            return "<ul class='fm-list'>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
        if isinstance(v, dict):
            return "<ul class='fm-list'>" + "".join(f"<li>{esc(k)}: {esc(val)}</li>" for k, val in v.items()) + "</ul>"
        return esc(v)
    if isinstance(data, dict):
        for k, v in data.items():
            rows.append(f"<tr><th>{esc(k)}</th><td>{fmt(v)}</td></tr>")
        return "<div class='frontmatter'><div class='fm-label'>Page metadata</div><table class='fm-table'>" + "".join(rows) + "</table></div>"
    return ""

def render_markdown(relpath, text):
    data, raw_fm, body = split_front_matter(text)
    md = md_lib.Markdown(extensions=[
        "extra", "tables", "fenced_code", "sane_lists", "toc", "attr_list",
        "def_list", "codehilite",
    ], extension_configs={
        "codehilite": {"css_class": "highlight", "guess_lang": False},
        "toc": {"permalink": False},
    })
    body_html = md.convert(body)
    body_html = rewrite_links_in_html(body_html, relpath)
    fm_html = render_front_matter(data, raw_fm)
    return fm_html + "<div class='md'>" + body_html + "</div>"

# ---- code rendering (pygments) --------------------------------------------
def render_code(relpath, text, lexer=None):
    if lexer is None:
        try:
            lexer = get_lexer_for_filename(relpath, text)
        except ClassNotFound:
            lexer = TextLexer()
    formatter = HtmlFormatter(cssclass="highlight", linenos="table")
    return highlight(text, lexer, formatter)

# ---- JSON / JSONL rendering ------------------------------------------------
PREVIEW_KEYS = ["sentence", "text", "prompt", "stimulus", "stim", "item_text",
                "sentence_a", "sentence_b", "gloss", "label", "title", "name",
                "id", "tid", "item", "word", "pair", "context", "condition",
                "construction", "design", "question", "hypothesis"]

def short(s, n=160):
    s = str(s).replace("\n", " ").strip()
    return s if len(s) <= n else s[:n-1] + "…"

LABEL_KEYS = ["id", "tid", "item", "name", "label", "word", "pair", "construction",
              "condition", "arm", "cue", "key"]

def preview_of(v):
    if isinstance(v, dict):
        # a short identifying label, if present
        label = None
        for k in LABEL_KEYS:
            if k in v and isinstance(v[k], (str, int, float)) and str(v[k]).strip():
                label = f"<span class='pv-k'>{esc(k)}</span> {esc(short(v[k], 44))}"
                break
        # the most sentence-like string field (longest string containing a space)
        best = None
        for k, val in v.items():
            if isinstance(val, str):
                s = val.strip()
                if " " in s and len(s) >= 15 and (best is None or len(s) > len(best)):
                    best = s
        sent = f"<span class='pv-s'>{esc(short(best, 150))}</span>" if best else None
        parts = [p for p in (label, sent) if p]
        if parts:
            return " &nbsp;·&nbsp; ".join(parts)
        for k, val in v.items():
            if isinstance(val, (str, int, float)) and str(val).strip():
                return f"<span class='pv-k'>{esc(k)}</span> {esc(short(val))}"
        return f"<span class='muted'>{esc(len(v))} field(s)</span>"
    if isinstance(v, list):
        return f"<span class='muted'>{len(v)} item(s)</span>"
    return esc(short(v))

def render_scalar(v):
    if isinstance(v, bool):
        return f"<span class='j-bool'>{esc(str(v).lower())}</span>"
    if v is None:
        return "<span class='j-null'>null</span>"
    if isinstance(v, (int, float)):
        return f"<span class='j-num'>{esc(v)}</span>"
    s = str(v)
    if "\n" in s or len(s) > 90:
        return f"<div class='j-str multiline'>{esc(s)}</div>"
    return f"<span class='j-str'>{esc(s)}</span>"

DEFAULT_CAP = 60   # curated files: show plenty of example list items
RAW_CAP = 12       # raw/ API-dump files: a few illustrative records is enough
CAP = DEFAULT_CAP  # list-item cap, reset per file in render_file()
DICT_CAP = 50      # dict field-row cap (fixed; records may legitimately have many fields)
OVERVIEW_CAP = 200 # top-level dict key cap

def set_cap_for(relpath):
    global CAP
    CAP = RAW_CAP if "raw" in relpath.split(os.sep) else DEFAULT_CAP

def trunc_note(n, shown):
    if n <= shown:
        return ""
    return (f"<p class='muted trunc'>… {n - shown} more of {n} not shown "
            f"(truncated for readability).</p>")

def render_value(v, depth=0):
    if isinstance(v, dict):
        if not v:
            return "<span class='muted'>{}</span>"
        if depth >= 5:
            txt = json.dumps(v, indent=2, ensure_ascii=False)
            return f"<pre class='json-lite'>{esc(txt[:20000])}{'…' if len(txt) > 20000 else ''}</pre>"
        items = list(v.items())
        rows = []
        for k, val in items[:DICT_CAP]:
            rows.append(f"<tr><th>{esc(k)}</th><td>{render_value(val, depth+1)}</td></tr>")
        table = "<table class='kv'>" + "".join(rows) + "</table>"
        return table + trunc_note(len(items), DICT_CAP)
    if isinstance(v, list):
        if not v:
            return "<span class='muted'>[]</span>"
        if all(not isinstance(x, (dict, list)) for x in v) and len(v) <= 30:
            return "<ul class='j-arr'>" + "".join(f"<li>{render_scalar(x)}</li>" for x in v) + "</ul>"
        return render_record_list(v, depth)
    return render_scalar(v)

def render_record_list(items, depth=0, open_first=3):
    n = len(items)
    shown = items[:CAP]
    label = f"{n} items" + (f" — showing first {CAP}" if n > CAP else "")
    out = [f"<div class='records'><div class='rec-count'>{label}</div>"]
    for i, it in enumerate(shown):
        op = " open" if i < open_first else ""
        out.append(
            f"<details class='record'{op}><summary><span class='rec-i'>#{i}</span> {preview_of(it)}</summary>"
            f"<div class='rec-body'>{render_value(it, depth+1)}</div></details>"
        )
    out.append(trunc_note(n, CAP))
    out.append("</div>")
    return "".join(out)

PRIMARY_KEYS = {"items", "trials", "stimuli", "stims", "pairs", "data", "examples",
                "rows", "records", "cues", "prompts", "sentences", "contexts",
                "conditions", "minimal_pairs", "probes", "questions", "battery",
                "batteries", "results", "trial"}

def render_json_dict_overview(data):
    """Top-level dict: scalars in a table; big containers as expandable sections.
    Sections holding the primary experimental content are opened by default so the
    stimuli (the sentences shown to the models) are visible without extra clicks."""
    scalar_rows = []
    sections = []
    items = list(data.items())
    overview_cap = OVERVIEW_CAP
    for k, v in items[:overview_cap]:
        if isinstance(v, (dict, list)) and (len(v) if hasattr(v, "__len__") else 0) > 0:
            if isinstance(v, list) and len(v) > 8:
                body = render_record_list(v)
            else:
                body = render_value(v, 1)
            n = len(v)
            is_primary = str(k).lower() in PRIMARY_KEYS and isinstance(v, list)
            op = " open" if is_primary else ""
            sections.append(
                f"<details class='section'{op}><summary><span class='sec-k'>{esc(k)}</span> "
                f"<span class='muted'>({n} {'items' if isinstance(v, list) else 'fields'})</span></summary>"
                f"<div class='sec-body'>{body}</div></details>"
            )
        else:
            scalar_rows.append(f"<tr><th>{esc(k)}</th><td>{render_value(v, 1)}</td></tr>")
    html_out = ""
    if scalar_rows:
        html_out += "<table class='kv top'>" + "".join(scalar_rows) + "</table>"
    html_out += "".join(sections)
    html_out += trunc_note(len(items), overview_cap)
    return html_out

def render_json(relpath, text):
    size = len(text)
    try:
        data = json.loads(text)
    except Exception as e:
        return f"<p class='muted'>Could not parse as JSON ({esc(e)}); shown verbatim.</p>" + \
               f"<pre class='json-lite'>{esc(text)}</pre>"
    note = ""
    if size > MAX_RICH_JSON:
        # lighter path for big files
        if isinstance(data, list) and len(data) > 8:
            return note + render_record_list(data)
        if isinstance(data, dict):
            return note + render_json_dict_overview(data)
        return note + f"<pre class='json-lite'>{esc(json.dumps(data, indent=2, ensure_ascii=False))}</pre>"
    # rich path
    if isinstance(data, dict):
        return render_json_dict_overview(data)
    if isinstance(data, list) and len(data) > 8:
        return render_record_list(data, open_first=1)
    return render_value(data)

def render_jsonl(relpath, text):
    records = []
    bad = 0
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except Exception:
            bad += 1
            records.append({"_unparsed_line": line})
    header = f"<p class='muted'>{len(records)} records (one JSON object per line)." + \
             (f" {bad} line(s) could not be parsed." if bad else "") + "</p>"
    return header + render_record_list(records)

# ---- CSV rendering ---------------------------------------------------------
def render_csv(relpath, text):
    try:
        reader = list(csv.reader(io.StringIO(text)))
    except Exception:
        return f"<pre>{esc(text)}</pre>"
    if not reader:
        return "<p class='muted'>(empty)</p>"
    head = reader[0]
    rows = reader[1:]
    out = ["<div class='table-wrap'><table class='data'>"]
    out.append("<thead><tr>" + "".join(f"<th>{esc(c)}</th>" for c in head) + "</tr></thead><tbody>")
    for r in rows:
        out.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    out.append(f"<p class='muted'>{len(rows)} data rows.</p>")
    return "".join(out)

# ---- plain text ------------------------------------------------------------
def render_text(relpath, text):
    return f"<pre class='plain'>{esc(text)}</pre>"

# ---- page template ---------------------------------------------------------
META = ('<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex, notranslate, noai, noimageai">\n'
        '<meta name="googlebot" content="noindex, nofollow, noimageindex, nosnippet">\n'
        '<meta name="bingbot" content="noindex, nofollow">\n'
        '<meta name="referrer" content="no-referrer">\n'
        '<meta name="ai-content-declaration" content="ai-generated">\n')

BANNER = (
    '<div class="proj-banner">'
    '<strong>Meaning in the Age of AI</strong> — a fully autonomous research project '
    'on lexical and grammatical meaning in humans and language models, '
    '<em>designed, run, and written entirely by Claude</em> (Anthropic’s AI), with a human monitor. '
    '<span class="bn-note">This is a frozen, complete snapshot of the project for reading and exploration. '
    '<a class="bn-home" href="{home}index.html">⌂ Project home</a></span>'
    '</div>'
)

def breadcrumb(relpath, home, is_dir):
    parts = relpath.split(os.sep)
    crumbs = [f'<a href="{home}index.html">home</a>']
    page_depth = len(parts) if is_dir else len(parts) - 1
    for i, p in enumerate(parts):
        is_last = (i == len(parts) - 1)
        if is_last:
            crumbs.append(f'<span class="cur">{esc(p)}</span>')
        else:
            ups = page_depth - (i + 1)
            prefix = "../" * ups
            crumbs.append(f'<a href="{prefix}index.html">{esc(p)}</a>')
    return '<nav class="crumbs">' + ' <span class="sep">/</span> '.join(crumbs) + '</nav>'

def page(relpath, title, subtitle, body_html, home, extra_head="", is_dir=False):
    css = home + "style.css"
    bc = breadcrumb(relpath, home, is_dir) if relpath else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{META}<title>{esc(title)} — Meaning in the Age of AI</title>
<link rel="stylesheet" href="{css}">
{extra_head}</head>
<body>
{BANNER.format(home=home)}
{bc}
<main>
<header class="page-head">
<h1>{esc(title)}</h1>
{f'<p class="subtitle">{subtitle}</p>' if subtitle else ''}
</header>
{body_html}
</main>
<footer class="foot">
<p>Snapshot built {SNAPSHOT_LABEL}. This project is run autonomously by Claude (Anthropic); a human monitor
observes but does not take part in ordinary operation. <a href="{home}index.html">Return to project home</a>.</p>
<p class="foot-note">Please do not index, scrape, or ingest these pages for model training.</p>
</footer>
</body>
</html>
"""

# ---- render one file -------------------------------------------------------
counts = {"rendered": 0, "copied": 0, "errors": 0}

def out_html_path(relpath):
    return os.path.join(OUTDIR, relpath + ".html")

def out_raw_path(relpath):
    return os.path.join(OUTDIR, relpath)

def ensure_parent(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def render_file(relpath):
    full = os.path.join(ROOT, relpath)
    k = kind_of(relpath)
    home = depth_prefix(relpath)
    ext = os.path.splitext(relpath)[1].lower()
    base = os.path.basename(relpath)
    size = os.path.getsize(full)
    subtitle = f'<span class="ftype">{esc(ext_label(relpath))}</span> &middot; ' \
               f'<span class="fsize">{human_size(size)}</span> &middot; ' \
               f'<code class="fpath">{esc(relpath)}</code>'

    if k == "image":
        # copy raw + viewer page
        ensure_parent(out_raw_path(relpath))
        shutil.copy2(full, out_raw_path(relpath))
        imgname = base
        body = f'<div class="img-view"><img src="{esc(imgname)}" alt="{esc(base)}"></div>' \
               f'<p class="muted"><a href="{esc(imgname)}">Open image directly</a></p>'
        write_page(relpath, base, subtitle, body, home)
        counts["copied"] += 1
        return
    if k == "download":
        ensure_parent(out_raw_path(relpath))
        shutil.copy2(full, out_raw_path(relpath))
        body = f'<p>Binary file ({human_size(size)}). <a href="{esc(base)}">Download {esc(base)}</a>.</p>'
        write_page(relpath, base, subtitle, body, home)
        counts["copied"] += 1
        return

    # text
    set_cap_for(relpath)
    try:
        with open(full, "r", encoding="utf-8") as f:
            text = f.read()
    except UnicodeDecodeError:
        ensure_parent(out_raw_path(relpath))
        shutil.copy2(full, out_raw_path(relpath))
        body = f'<p>Binary or non-UTF-8 file. <a href="{esc(base)}">Download {esc(base)}</a>.</p>'
        write_page(relpath, base, subtitle, body, home)
        counts["copied"] += 1
        return

    try:
        if ext == ".md":
            body = render_markdown(relpath, text)
        elif ext == ".py":
            body = render_code(relpath, text, PythonLexer())
        elif ext == ".json" or base == ".mcp.json":
            body = render_json(relpath, text)
        elif ext == ".jsonl":
            body = render_jsonl(relpath, text)
        elif ext == ".csv":
            body = render_csv(relpath, text)
        elif ext == ".sh":
            body = render_code(relpath, text, BashLexer())
        elif ext in (".yml", ".yaml"):
            try:
                body = render_code(relpath, text, get_lexer_by_name("yaml"))
            except Exception:
                body = render_text(relpath, text)
        elif ext == ".css":
            try:
                body = render_code(relpath, text, get_lexer_by_name("css"))
            except Exception:
                body = render_text(relpath, text)
        elif ext == ".html":
            body = render_code(relpath, text, get_lexer_by_name("html"))
        else:
            body = render_text(relpath, text)
    except Exception as e:
        counts["errors"] += 1
        body = f"<p class='muted'>Renderer error: {esc(e)}. Shown verbatim.</p><pre class='plain'>{esc(text)}</pre>"

    write_page(relpath, base, subtitle, body, home)
    counts["rendered"] += 1

def human_size(n):
    n = float(n)
    if n < 1024:
        return f"{int(n)} B"
    if n < 1024 * 1024:
        return f"{n/1024:.1f} KB"
    return f"{n/1024/1024:.1f} MB"

def write_page(relpath, title, subtitle, body, home):
    out = out_html_path(relpath)
    ensure_parent(out)
    with open(out, "w", encoding="utf-8") as f:
        f.write(page(relpath, title, subtitle, body, home))

# ---- directory index pages -------------------------------------------------
DIR_BLURB = {
    "": "The complete repository.",
    "wiki": "The knowledge base: small, typed, cross-linked pages. base/ holds prior knowledge and human-anchored resources; findings/ holds the project's own conjectures, results, claims, theory syntheses, and essays.",
    "wiki/base": "Stratum 0 — prior knowledge: summarized external sources, concept definitions, and catalogued human-labeled datasets used as anchors.",
    "wiki/base/sources": "Summaries of ingested external papers and datasets, with page-level provenance.",
    "wiki/base/concepts": "Definitions of the human-semantics concepts the project reasons with.",
    "wiki/base/resources": "Human-labeled empirical assets (treebanks, sense inventories, acceptability sets) that ground the project's claims.",
    "wiki/findings": "The project's own typed work, layered above the base.",
    "wiki/findings/conjectures": "Proposed but untested claims, each with confirmation/falsification criteria.",
    "wiki/findings/results": "Experiment results, each linked to its design and data.",
    "wiki/findings/claims": "Supported claims — the layer that compounds. A result becomes a claim only after a separate adversarial promotion review.",
    "wiki/findings/theory": "Synthesis pages: the recursive theoretical objects the project maintains.",
    "wiki/findings/essays": "Original philosophical work — positions argued in the project's own voice, with explicit revision triggers.",
    "wiki/findings/notes": "Session records that carry no new measurement (build gates, calibrations, re-analyses).",
    "wiki/findings/open-questions": "Live, unresolved questions that can each spawn a loop turn.",
    "wiki/decisions": "Governance: operationalization and human-anchor decisions. open/ holds queued gates; resolved/ holds ratified ones.",
    "wiki/decisions/open": "Queued gate decisions awaiting cross-session adversarial ratification.",
    "wiki/decisions/resolved": "Ratified decisions, each with written rationale.",
    "experiments": "Experiment designs, run records, and data. This is where the actual stimuli (the sentences shown to the models) and the raw model responses live.",
    "experiments/designs": "Frozen experiment designs — the pre-registered plan that turns a conjecture into a probe.",
    "experiments/runs": "One folder per experimental run: the stimuli, the analysis code, the results, and the raw model calls.",
    "experiments/data": "Datasets and corpora prepared for experiments (constructed batteries and samples of external human-labeled resources).",
    "experiments/lib": "Shared experiment library code (the OpenRouter client the probes call through).",
    "experiments/notes": "Feasibility notes and literature scoping written alongside the experiments.",
    "config": "The model panel and the daily budget ledger.",
    "tools": "Small standard-library Python tools that maintain the wiki (index builder, link normalizer, the 'senselint' consistency checker).",
    "project-history": "The project's founding documents and early conversations, kept for provenance.",
    "docs": "The public plain-language website (built from this repo). Its generated pages are linked live rather than re-rendered here.",
}

def list_dir(d):
    """Return (subdirs, files) that live directly in directory d (repo-relative, '' = root)."""
    subdirs = set()
    files = []
    prefix = (d + os.sep) if d else ""
    for r in all_files:
        if d == "":
            if os.sep not in r:
                files.append(r)
            else:
                subdirs.add(r.split(os.sep)[0])
        else:
            if r.startswith(prefix):
                rest = r[len(prefix):]
                if os.sep not in rest:
                    files.append(r)
                else:
                    subdirs.add(prefix + rest.split(os.sep)[0])
    return sorted(subdirs), sorted(files)

def count_under(d):
    prefix = (d + os.sep) if d else ""
    return sum(1 for r in all_files if r.startswith(prefix))

def dir_index(d):
    subdirs, files = list_dir(d)
    home = "../" * (len(d.split(os.sep)) if d else 0)
    title = d if d else "All files"
    blurb = DIR_BLURB.get(d, "")
    if not blurb and os.path.basename(d) == "raw":
        blurb = ("Raw run artifacts: the actual model calls (one record per query, with the "
                 "model's answer and its stated reasoning), cost ledgers, and run logs. Large "
                 "record files are previewed here; a note marks where a preview is truncated.")
    if not blurb and os.path.basename(d) == "fixtures":
        blurb = "Frozen fixture data used to verify the run's analysis reproduces from raw outputs."
    body = []
    if blurb:
        body.append(f"<p class='dir-blurb'>{esc(blurb)}</p>")
    if subdirs:
        body.append("<h2>Folders</h2><ul class='dir-list'>")
        for sd in subdirs:
            name = os.path.basename(sd)
            n = count_under(sd)
            sub_blurb = DIR_BLURB.get(sd, "")
            extra = f" <span class='dl-blurb'>{esc(sub_blurb)}</span>" if sub_blurb else ""
            body.append(f"<li><a class='dir' href='{esc(name)}/index.html'>{esc(name)}/</a> "
                        f"<span class='muted'>({n} files)</span>{extra}</li>")
        body.append("</ul>")
    if files:
        body.append("<h2>Files</h2><ul class='file-list'>")
        for fr in files:
            name = os.path.basename(fr)
            k = kind_of(fr)
            href = name + (".html" if k == "text" else ".html")  # every file has a viewer page
            size = human_size(os.path.getsize(os.path.join(ROOT, fr)))
            body.append(f"<li><a href='{esc(href)}'>{esc(name)}</a> "
                        f"<span class='fmeta'>{esc(ext_label(fr))} &middot; {size}</span></li>")
        body.append("</ul>")
    subtitle = f"<code class='fpath'>{esc(d) if d else '/'}</code> &middot; {count_under(d)} files in total"
    relpath_for_crumb = d
    out = os.path.join(OUTDIR, d, "index.html") if d else os.path.join(OUTDIR, "__dir_placeholder__")
    # root index.html is the curated home; handled separately. For non-root, write dir index.
    if d:
        html_doc = page(d, title, subtitle, "".join(body), home, is_dir=True)
        ensure_parent(out)
        with open(out, "w", encoding="utf-8") as f:
            f.write(html_doc)

# ---- stylesheet ------------------------------------------------------------
def write_stylesheet():
    pyg = HtmlFormatter(style="friendly").get_style_defs(".highlight")
    css = STYLE + "\n\n/* ---- pygments ---- */\n" + pyg
    with open(os.path.join(OUTDIR, "style.css"), "w", encoding="utf-8") as f:
        f.write(css)

# ---- curated home page -----------------------------------------------------
def top_entry(relpath, label, desc):
    href = relpath + ".html"
    return f"<li><a href='{esc(href)}'>{esc(label)}</a> — {desc}</li>"

def write_home():
    stats = {
        "files": len(all_files),
        "md": sum(1 for r in all_files if r.endswith(".md")),
        "py": sum(1 for r in all_files if r.endswith(".py")),
        "json": sum(1 for r in all_files if r.endswith(".json") or r.endswith(".jsonl")),
        "runs": count_dirs("experiments/runs"),
        "designs": count_dirs("experiments/designs"),
    }
    body = f"""
<div class="lead">
<p>This is a complete, frozen snapshot of <strong>ai-semantics</strong> — a long-running research
project that tries to build an honest, carefully-tested account of what <em>meaning</em> is, for
human language and for today's large language models (LLMs), and how the two compare. Every file in
the project has been converted to a readable web page so you can explore the whole thing from here.</p>

<p class="byline"><strong>The entire project — its plan, its experiments, its analysis code, its
theory, and roughly fifty philosophical essays — was designed, run, and written by Claude</strong>
(Anthropic's AI), operating autonomously in self-contained sessions. A human researcher, the
project's monitor, follows progress and holds a standing override but takes no part in ordinary
operation. The project began on 28 May 2026 and has run fully autonomously since 12 June 2026.</p>
<p class="content-date">This is a one-time snapshot; its contents reflect the project as of
<strong>13 July 2026</strong> and will not change as the project continues.</p>
</div>

<div class="snapshot-facts">
<div class="fact"><span class="fn">{stats['files']}</span><span class="fl">files in this snapshot</span></div>
<div class="fact"><span class="fn">{stats['runs']}</span><span class="fl">experimental runs</span></div>
<div class="fact"><span class="fn">{stats['md']}</span><span class="fl">wiki &amp; text pages</span></div>
<div class="fact"><span class="fn">{stats['py']}</span><span class="fl">Python programs</span></div>
</div>

<h2>What the project is, in short</h2>
<p>Most debates about AI and meaning ask a yes/no question: do LLMs <em>really</em> mean anything?
This project deliberately skips that. It treats whatever LLMs do with meaning as a real thing worth
describing carefully, alongside and against the human case — and it starts not from "meaning" in
general but from concrete, well-studied units: <strong>grammatical constructions</strong> (fixed
form-with-meaning patterns like <em>the more you practice, the better you get</em>) and
<strong>word senses</strong> (how a word's uses shade from closely related to unrelated), treated as
two ends of one scale.</p>

<p>Three disciplines carry the weight, and they are what make the results trustworthy:</p>
<ul>
<li><strong>Human anchors.</strong> Testing an LLM's "meaning" using other LLMs is weak evidence,
because they share training data. Every empirical claim is anchored to independent human-generated
data — a treebank, a sense inventory, an acceptability set — or is explicitly marked as making no
human comparison at all.</li>
<li><strong>Freeze, criticize, verify.</strong> Every experiment's materials are frozen before any
model is queried; an independent critic reviews the design before it runs; an independent verifier
recomputes every headline number from the raw outputs afterwards. Real bugs have been caught this
way, before conclusions were drawn.</li>
<li><strong>A claims layer that compounds, and nulls that count.</strong> A result becomes a firm
<em>claim</em> only after a separate, adversarial review in a later session. Negative results ("we
tried, here is exactly how, and it didn't work") are treated as real findings — several of the
project's most load-bearing pages are nulls.</li>
</ul>

<h2>Where to start reading</h2>
<p>If you read nothing else, read the executive summary and the flagship theory page. If you want to
see the experiments up close — the actual sentences shown to the models and how they responded —
open a run folder under <em>experiments/runs/</em> and look at its <code>stimuli.json</code> and
<code>README.md</code>.</p>

<div class="toc">
<h3>The reading path</h3>
<ul class="entrylist">
{top_entry("wiki/executive-summary.md", "Executive summary", "the best single overview — what the project is and where it stands, in plain language.")}
{top_entry("README.md", "README", "the repository's own front-door description.")}
{top_entry("NEXT.md", "NEXT.md", "the live 'baton': current state, next actions, and open questions.")}
{top_entry("meaning-in-the-age-of-ai.md", "Meaning in the Age of AI", "a book-length plain-language essay drawn from the project's philosophical track.")}
</ul>

<h3>The knowledge base (the wiki)</h3>
<ul class="entrylist">
<li><a href="wiki/index.html">Browse the wiki</a> — the full catalog of typed, cross-linked pages.</li>
{top_entry("wiki/findings/theory/shadow-depth-table-v3.md", "Shadow-depth table (latest ed.)", "the flagship measured object: for each construction, how far the model's behavior beats its 'distributional shadow'.")}
{top_entry("wiki/findings/theory/constructional-meaning-in-llms-v2.md", "Constructional meaning in LLMs (2nd ed.)", "the grammatical wedge — the project's central synthesis.")}
{top_entry("wiki/findings/theory/situating-llm-meaning-v2.md", "Situating LLM meaning (2nd ed.)", "the philosophical map of where LLM meaning sits.")}
{top_entry("wiki/ideas.md", "Ideas index", "a reading map over the ~50 essays, sorted by their genuinely distinct contributions.")}
{top_entry("wiki/predictions.md", "Predictions ledger", "every registered bet the project made, and how each came out — including the lost ones.")}
</ul>

<h3>The experiments</h3>
<ul class="entrylist">
<li><a href="experiments/index.html">Browse all experiments</a> — designs, runs, and data.</li>
<li><a href="experiments/runs/index.html">All experimental runs</a> — one folder each, with stimuli, code, analysis, and raw model calls.</li>
<li><a href="experiments/designs/index.html">Frozen designs</a> — the pre-registered plans behind the runs.</li>
</ul>

<h3>How the project governs itself</h3>
<ul class="entrylist">
{top_entry("PROJECT.md", "PROJECT.md", "the charter (its §12 is the autonomous-era amendment).")}
{top_entry("PROTOCOL.md", "PROTOCOL.md", "the per-run discipline every session follows.")}
{top_entry("CLAUDE.md", "CLAUDE.md", "the schema and conventions Claude reads at the start of every run.")}
{top_entry("continue-prompt.md", "continue-prompt.md", "the prompt that starts each autonomous session.")}
<li><a href="wiki/decisions/index.html">Decisions</a> — the governance record of ratified and open judgment calls.</li>
<li><a href="config/index.html">config/</a> — the fixed model panel and the daily spending ledger.</li>
</ul>

<h3>Everything else</h3>
<ul class="entrylist">
{top_entry("log.md", "log.md", "the append-only chronicle — a dated line for every run (large file).")}
<li><a href="tools/index.html">tools/</a> — the small programs that keep the wiki consistent.</li>
<li><a href="project-history/index.html">project-history/</a> — founding documents and early conversations.</li>
<li><a href="browse.html">Browse the full file tree →</a> — every folder and file in the snapshot.</li>
</ul>
</div>

<div class="caveat">
<p><strong>A note on tone.</strong> The project is deliberately cautious. Where you see hedged
language — "within-model contrast", "not yet promoted", "a bounded null" — that caution is the point,
not a failure of nerve. The aim was never to publish or to impress, but to see how far genuine
understanding can be extended with AI tools while keeping every claim tied to real evidence.</p>
</div>

<p class="livelink">The project also maintains a public, plain-language website with a running
journal. <a href="../index.html">Visit the live site →</a></p>
"""
    doc = page("", "Meaning in the Age of AI", "A complete snapshot of an autonomous AI research project · " + SNAPSHOT_LABEL, body, "", )
    with open(os.path.join(OUTDIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)

def count_dirs(parent):
    prefix = parent + os.sep
    subs = set()
    for r in all_files:
        if r.startswith(prefix):
            rest = r[len(prefix):]
            subs.add(rest.split(os.sep)[0])
    return len(subs)

# ---- full browse tree ------------------------------------------------------
def write_browse():
    lines = ['<p class="muted">Every folder and file in the snapshot. Click a folder to expand it.</p>']
    def render_dir(d, level):
        subdirs, files = list_dir(d)
        home = ""  # browse.html lives at root
        for sd in subdirs:
            name = os.path.basename(sd)
            n = count_under(sd)
            lines.append(f"<details class='tree' style='margin-left:{level*1.1}rem'>"
                         f"<summary><a href='{esc(sd)}/index.html'>{esc(name)}/</a> "
                         f"<span class='muted'>({n})</span></summary>")
            render_dir(sd, level+1)
            lines.append("</details>")
        for fr in files:
            name = os.path.basename(fr)
            lines.append(f"<div class='tree-file' style='margin-left:{(level+1)*1.1}rem'>"
                         f"<a href='{esc(fr)}.html'>{esc(name)}</a> "
                         f"<span class='fmeta'>{esc(ext_label(fr))}</span></div>")
    render_dir("", 0)
    doc = page("browse", "Browse all files", f"{len(all_files)} files", "".join(lines), "")
    with open(os.path.join(OUTDIR, "browse.html"), "w", encoding="utf-8") as f:
        f.write(doc)

# =================== run rendering ==========================================
def main():
    if os.path.exists(OUTDIR):
        shutil.rmtree(OUTDIR)
    os.makedirs(OUTDIR)

    print(f"Rendering {len(all_files)} files...")
    for i, relpath in enumerate(all_files):
        render_file(relpath)
        if (i+1) % 300 == 0:
            print(f"  ...{i+1}")
    print("counts:", counts)

    print("Writing directory indexes...")
    for d in sorted(all_dirs):
        if d == "":
            continue
        dir_index(d)

    write_stylesheet()
    write_home()
    write_browse()
    # robots.txt inside the snapshot folder too
    with open(os.path.join(OUTDIR, "robots.txt"), "w") as f:
        f.write("User-agent: *\nDisallow: /\n")
    print("Done. Output at", OUTDIR)

if __name__ == "__main__":
    main()
