#!/usr/bin/env python3
"""Verify every internal href/src in the generated snapshot resolves to a real file."""
import os, re, sys
from urllib.parse import unquote

OUT = "/home/user/ai-semantics/docs/complete-project-20260717"
HREF = re.compile(r'(?:href|src)="([^"]*)"', re.IGNORECASE)

broken = []
external = 0
total = 0
by_source = {}

for dirpath, _, files in os.walk(OUT):
    for fn in files:
        if not fn.endswith(".html"):
            continue
        p = os.path.join(dirpath, fn)
        with open(p, encoding="utf-8") as f:
            htmltext = f.read()
        for m in HREF.finditer(htmltext):
            href = m.group(1)
            total += 1
            h = href.strip()
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', h) or h.startswith("//") or h.startswith("#") or h == "":
                external += 1
                continue
            # strip fragment / query
            path = h.split("#", 1)[0].split("?", 1)[0]
            if path == "":
                continue
            path = unquote(path)
            target = os.path.normpath(os.path.join(dirpath, path))
            if not os.path.exists(target):
                rp = os.path.relpath(p, OUT)
                broken.append((rp, href, os.path.relpath(target, OUT)))
                by_source[rp] = by_source.get(rp, 0) + 1

print(f"Total link occurrences: {total}")
print(f"External/anchor (skipped): {external}")
print(f"Internal checked: {total - external}")
print(f"BROKEN: {len(broken)}")
if broken:
    print("\n--- sample broken (first 40) ---")
    for rp, href, tgt in broken[:40]:
        print(f"  [{rp}]  href={href}  -> missing {tgt}")
    print("\n--- sources with most broken links ---")
    for rp, n in sorted(by_source.items(), key=lambda x: -x[1])[:20]:
        print(f"  {n:4d}  {rp}")
