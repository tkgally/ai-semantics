#!/usr/bin/env python3
"""
Build a valid EPUB 3 from the essay Markdown using only the Python standard
library (no pandoc, no third-party deps).

Supports the small Markdown subset the essay uses:
  - `# ` level-1 headings  -> chapter boundaries
  - `## `/`### ` headings   -> h2/h3 (defensive; essay has none)
  - blank-line-separated paragraphs
  - **bold** / *italic*
  - `> ` blockquotes, `- ` lists, `---` rules (defensive)
HTML special characters are escaped; em dashes and other UTF-8 pass through.

Output structure (EPUB 3):
  mimetype                      (FIRST entry, STORED/uncompressed)
  META-INF/container.xml        (points to the OPF)
  OEBPS/content.opf             (metadata + manifest + spine)
  OEBPS/nav.xhtml               (EPUB 3 navigation document / TOC)
  OEBPS/style.css               (reading typography)
  OEBPS/title.xhtml             (title page)
  OEBPS/ch01.xhtml ...          (one XHTML file per chapter)
"""

import datetime
import html
import os
import re
import sys
import uuid
import zipfile

SRC = "meaning-in-the-age-of-ai.md"
OUT = "meaning-in-the-age-of-ai.epub"


# --------------------------------------------------------------------------
# Front-matter + chapter parsing
# --------------------------------------------------------------------------
def parse_front_matter(text):
    meta = {}
    lines = text.split("\n")
    body_start = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            line = lines[i]
            if ":" in line:
                k, v = line.split(":", 1)
                v = v.strip()
                if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                    v = v[1:-1]
                meta[k.strip()] = v
            i += 1
        body_start = i + 1
    body = "\n".join(lines[body_start:])
    return meta, body


def split_chapters(body):
    chapters = []
    title = None
    buf = []
    for line in body.split("\n"):
        m = re.match(r"^#\s+(.*)$", line)  # single '#' only ('## ' fails \s+)
        if m:
            if title is not None:
                chapters.append((title, "\n".join(buf)))
            title = m.group(1).strip()
            buf = []
        else:
            if title is not None:
                buf.append(line)
    if title is not None:
        chapters.append((title, "\n".join(buf)))
    return chapters


# --------------------------------------------------------------------------
# Markdown -> XHTML
# --------------------------------------------------------------------------
def inline(text):
    text = html.escape(text, quote=False)  # & < >  (leave quotes literal)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def blocks_to_html(md):
    lines = md.split("\n")
    out = []
    i, n = 0, len(lines)
    while i < n:
        s = lines[i].strip()
        if s == "":
            i += 1
            continue
        if s in ("---", "***", "* * *"):
            out.append("<hr/>")
            i += 1
            continue
        m = re.match(r"^(#{2,6})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2).strip()), lvl))
            i += 1
            continue
        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = " ".join(x.strip() for x in buf if x.strip())
            out.append("<blockquote><p>%s</p></blockquote>" % inline(inner))
            continue
        if re.match(r"^[-*+]\s+", s):
            items = []
            while i < n and re.match(r"^[-*+]\s+", lines[i].strip()):
                items.append("<li>%s</li>" % inline(re.sub(r"^[-*+]\s+", "", lines[i].strip())))
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        # paragraph
        buf = []
        while i < n:
            cs = lines[i].strip()
            if (cs == "" or cs in ("---", "***", "* * *")
                    or cs.startswith(">")
                    or re.match(r"^#{1,6}\s", cs)
                    or re.match(r"^[-*+]\s+", cs)):
                break
            buf.append(cs)
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(buf)))
    return "\n".join(out)


# --------------------------------------------------------------------------
# Document templates
# --------------------------------------------------------------------------
def xhtml_page(title, body_inner, lang):
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" '
        'xmlns:epub="http://www.idpf.org/2007/ops" '
        'lang="__LANG__" xml:lang="__LANG__">\n'
        '<head>\n<meta charset="utf-8"/>\n<title>__TITLE__</title>\n'
        '<link rel="stylesheet" type="text/css" href="style.css"/>\n'
        '</head>\n<body>\n__BODY__\n</body>\n</html>\n'
    ).replace("__LANG__", lang).replace("__TITLE__", html.escape(title)).replace("__BODY__", body_inner)


CSS = """@namespace epub "http://www.idpf.org/2007/ops";
html { font-size: 100%; }
body {
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.55;
  margin: 1em 1.2em;
  text-align: left;
  color: #1a1a1a;
  -webkit-hyphens: auto;
  hyphens: auto;
}
h1 {
  font-size: 1.5em;
  line-height: 1.2;
  margin: 1.3em 0 0.8em;
  font-weight: bold;
  text-align: left;
  page-break-before: always;
  break-before: page;
}
h2 { font-size: 1.2em; margin: 1.3em 0 0.5em; font-weight: bold; }
h3 { font-size: 1.05em; margin: 1.1em 0 0.4em; font-weight: bold; }
p { margin: 0 0 0.9em; }
blockquote { margin: 1em 1.6em; font-style: italic; color: #333; }
em { font-style: italic; }
strong { font-weight: bold; }
hr { border: none; border-top: 1px solid #999; margin: 1.6em 22%; }
.titlepage { text-align: center; margin-top: 22%; }
.titlepage .book-title {
  font-size: 2.1em; line-height: 1.15; font-weight: bold;
  page-break-before: avoid; break-before: avoid; margin: 0 0 0.35em;
}
.titlepage .book-subtitle { font-size: 1.15em; font-style: italic; color: #444; margin: 0 0 2.5em; }
.titlepage .book-author { font-size: 1.05em; margin: 2.5em 0 0.2em; }
.titlepage .book-date { color: #666; font-size: 0.95em; }
nav#toc ol { list-style-type: none; padding-left: 0; }
nav#toc li { margin: 0.45em 0; }
nav#toc a { text-decoration: none; color: #1a1a1a; }
"""


CONTAINER = (
    '<?xml version="1.0" encoding="utf-8"?>\n'
    '<container version="1.0" '
    'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
    '  <rootfiles>\n'
    '    <rootfile full-path="OEBPS/content.opf" '
    'media-type="application/oebps-package+xml"/>\n'
    '  </rootfiles>\n'
    '</container>\n'
)


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------
def main():
    if not os.path.exists(SRC):
        sys.exit("source not found: %s" % SRC)
    with open(SRC, encoding="utf-8") as f:
        raw = f.read()

    meta, body = parse_front_matter(raw)
    title = meta.get("title", "Untitled")
    subtitle = meta.get("subtitle", "")
    author = meta.get("author", "")
    date = meta.get("date", datetime.date.today().isoformat())
    lang = meta.get("language", "en")

    chapters = split_chapters(body)
    if not chapters:
        sys.exit("no '# ' chapters found")

    # Per-chapter XHTML
    chapter_files = []  # (filename, id, title, xhtml)
    for idx, (ch_title, ch_md) in enumerate(chapters, start=1):
        fn = "ch%02d.xhtml" % idx
        cid = "ch%02d" % idx
        inner = ('<section epub:type="chapter">\n<h1>%s</h1>\n%s\n</section>'
                 % (inline(ch_title), blocks_to_html(ch_md)))
        chapter_files.append((fn, cid, ch_title, xhtml_page(ch_title, inner, lang)))

    # Title page
    tp_inner = ['<section epub:type="titlepage" class="titlepage" role="doc-cover">']
    tp_inner.append('<h1 class="book-title">%s</h1>' % inline(title))
    if subtitle:
        tp_inner.append('<p class="book-subtitle">%s</p>' % inline(subtitle))
    if author:
        tp_inner.append('<p class="book-author">%s</p>' % inline(author))
    if date:
        tp_inner.append('<p class="book-date">%s</p>' % inline(date))
    tp_inner.append('</section>')
    title_xhtml = xhtml_page(title, "\n".join(tp_inner), lang)

    # Nav / TOC
    toc_items = ['<li><a href="title.xhtml">Title page</a></li>']
    for fn, cid, ch_title, _ in chapter_files:
        toc_items.append('<li><a href="%s">%s</a></li>' % (fn, html.escape(ch_title)))
    nav_inner = (
        '<nav epub:type="toc" id="toc" role="doc-toc">\n'
        '<h1>Contents</h1>\n<ol>\n' + "\n".join(toc_items) + "\n</ol>\n</nav>\n"
        '<nav epub:type="landmarks" id="landmarks" hidden="hidden">\n<ol>\n'
        '<li><a epub:type="titlepage" href="title.xhtml">Title page</a></li>\n'
        '<li><a epub:type="bodymatter" href="%s">Begin reading</a></li>\n'
        '</ol>\n</nav>\n' % chapter_files[0][0]
    )
    nav_xhtml = xhtml_page("Contents", nav_inner, lang)

    # content.opf
    book_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, "ai-semantics::" + title)
    modified = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    manifest = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="css" href="style.css" media-type="text/css"/>',
        '<item id="titlepage" href="title.xhtml" media-type="application/xhtml+xml"/>',
    ]
    spine = ['<itemref idref="titlepage"/>', '<itemref idref="nav"/>']
    for fn, cid, _, _ in chapter_files:
        manifest.append('<item id="%s" href="%s" media-type="application/xhtml+xml"/>' % (cid, fn))
        spine.append('<itemref idref="%s"/>' % cid)

    full_title = title + (": " + subtitle if subtitle else "")
    opf = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
        'unique-identifier="book-id" xml:lang="__LANG__">\n'
        '  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
        '    <dc:identifier id="book-id">urn:uuid:__UUID__</dc:identifier>\n'
        '    <dc:title>__TITLE__</dc:title>\n'
        '    <dc:creator>__AUTHOR__</dc:creator>\n'
        '    <dc:language>__LANG__</dc:language>\n'
        '    <dc:date>__DATE__</dc:date>\n'
        '    <meta property="dcterms:modified">__MODIFIED__</meta>\n'
        '  </metadata>\n'
        '  <manifest>\n    __MANIFEST__\n  </manifest>\n'
        '  <spine>\n    __SPINE__\n  </spine>\n'
        '</package>\n'
    )
    opf = (opf.replace("__LANG__", lang)
              .replace("__UUID__", str(book_uuid))
              .replace("__TITLE__", html.escape(full_title))
              .replace("__AUTHOR__", html.escape(author))
              .replace("__DATE__", html.escape(date))
              .replace("__MODIFIED__", modified)
              .replace("__MANIFEST__", "\n    ".join(manifest))
              .replace("__SPINE__", "\n    ".join(spine)))

    # Assemble the zip: mimetype FIRST and STORED, everything else DEFLATED.
    if os.path.exists(OUT):
        os.remove(OUT)
    with zipfile.ZipFile(OUT, "w") as z:
        zi = zipfile.ZipInfo("mimetype")
        zi.compress_type = zipfile.ZIP_STORED
        z.writestr(zi, "application/epub+zip")

        def add(name, data):
            info = zipfile.ZipInfo(name)
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)

        add("META-INF/container.xml", CONTAINER)
        add("OEBPS/content.opf", opf)
        add("OEBPS/nav.xhtml", nav_xhtml)
        add("OEBPS/style.css", CSS)
        add("OEBPS/title.xhtml", title_xhtml)
        for fn, _, _, xhtml in chapter_files:
            add("OEBPS/" + fn, xhtml)

    print("Built %s" % OUT)
    print("  title:    %s" % full_title)
    print("  author:   %s" % author)
    print("  language: %s" % lang)
    print("  chapters: %d (+ title page, nav)" % len(chapter_files))
    print("  uuid:     urn:uuid:%s" % book_uuid)


if __name__ == "__main__":
    main()
