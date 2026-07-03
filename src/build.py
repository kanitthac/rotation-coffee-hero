#!/usr/bin/env python3
"""Injects base64-encoded font data into template.html, writes ../index.html.

The Artifact/browser CSP blocks live webfont requests, so fonts are embedded
as @font-face data URIs rather than linked. Run this after editing
template.html or swapping a font file in fonts/.
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).parent
TEMPLATE = ROOT / "template.html"
OUTPUT = ROOT.parent / "index.html"

FONT_MAP = {
    "__ZILLASLAB_700__": "fonts/zillaslab-700.woff2",
    "__WORKSANS_400__": "fonts/worksans-400.woff2",
    "__WORKSANS_600__": "fonts/worksans-600.woff2",
    "__PLEXMONO_500__": "fonts/plexmono-500.woff2",
}


def main():
    html = TEMPLATE.read_text()

    for placeholder, font_path in FONT_MAP.items():
        if placeholder not in html:
            raise SystemExit(f"template.html is missing placeholder {placeholder}")
        data = (ROOT / font_path).read_bytes()
        html = html.replace(placeholder, base64.b64encode(data).decode("ascii"))

    OUTPUT.write_text(html)
    print(f"wrote {OUTPUT} ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
