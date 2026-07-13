# _build/ — how this snapshot was generated

`docs/complete-project-20260717/` is a **one-time, frozen HTML snapshot** of the entire
`ai-semantics` repository as it stood on **2026-07-13**, built so the project could be shared and
explored via a single public link. It is not regenerated during regular sessions and is not part
of the six-page public site in `docs/`.

## What is here

- `build_site.py` — the generator. Walks the repository from the root, converts every text file to
  a readable HTML page (Markdown → rendered HTML with a metadata box for YAML front-matter; Python →
  syntax-highlighted; JSON/JSONL → browsable record views that surface the experiment sentences;
  CSV → tables; images → viewer pages), mirrors the directory structure so relative links resolve,
  rewrites in-page cross-references to point at the generated pages, and writes the shared
  `style.css`, the curated `index.html`, per-directory index pages, and `browse.html`.
- `check_links.py` — verifies every internal link in the generated pages resolves to a real file.

## Design choices worth knowing

- **Nothing is deleted; large data is previewed.** Very long lists inside data files (e.g. raw
  model-call logs with hundreds of records) are capped in the rendered page — 60 items for curated
  files, 12 for `raw/` API dumps — with a visible "truncated for readability" note. Every file in
  the committed repository still has its own page.
- **Six generated public-site pages are linked live, not re-rendered** (`about.html`,
  `findings.html`, `glossary.html`, `index.html`, `journal.html`, `plans.html` in the parent
  `docs/`), to avoid duplicating already-HTML content.
- **Search-engine / scraper / AI-training discouragement** is carried by a `robots`-family
  `<meta>` block on every page, reinforcing the site-root `docs/robots.txt`.

## To regenerate (not normally needed)

Requires Python 3 with `markdown`, `pygments`, and `pyyaml` installed. Running the script **erases
and rewrites** `docs/complete-project-20260717/` from the current repository state:

```
python3 docs/complete-project-20260717/_build/build_site.py
python3 docs/complete-project-20260717/_build/check_links.py
```

(The paths in the scripts are absolute to the build environment; adjust `ROOT`/`OUTDIR` if the repo
lives elsewhere. A regenerate would reflect the repository as it stands *then*, not the 2026-07-13
snapshot.)
