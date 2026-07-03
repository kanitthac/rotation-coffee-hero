# Rotation — coffee subscription hero

A single hero-section landing page for **Rotation**, a fictional coffee subscription built around freshness: beans roasted to order and shipped within 48 hours, timed to arrive as your last bag runs out.

## View it

Open `index.html` directly in a browser. It's fully self-contained — fonts are embedded, no server or build step required to view it.

## Build

```
python3 src/build.py
```

Regenerates `index.html` from `src/template.html`, inlining the fonts in `src/fonts/` as base64 `@font-face` data URIs. Edit `src/template.html`, not `index.html` — the build script overwrites the latter.

## Structure

- `index.html` — generated output; open this to view the page
- `src/template.html` — page source
- `src/build.py` — build script
- `src/fonts/` — Zilla Slab, Work Sans, and IBM Plex Mono (woff2)

For design rationale and implementation notes — color tokens, the roast-dial SVG math, accessibility contrast checks — see [CLAUDE.md](CLAUDE.md).
