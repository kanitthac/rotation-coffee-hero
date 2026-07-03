# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single self-contained landing-page hero for "Rotation," a fictional roast-to-order coffee subscription. There's no app, server, or framework — `index.html` is the deliverable, viewable by opening it directly in a browser.

## Build

```
python3 src/build.py
```

Regenerates `index.html` from `src/template.html` by inlining the four font files in `src/fonts/` as base64 `@font-face` data URIs. There is no other build step, no package.json, no test suite, and no linter configured.

**Always edit `src/template.html`, never `index.html` directly** — `index.html` is generated output and gets overwritten by the build script. `index.html` is what you open in a browser to preview; `src/template.html` is the real source.

## Why fonts are embedded as base64

This page originated as a Claude Artifact, whose CSP blocks requests to font CDNs (Google Fonts, etc.) — a `@font-face` pointing at a live URL silently falls back to a system font with no error. `src/build.py` downloads-once-and-embeds instead: the actual woff2 files live in `src/fonts/`, and the build script base64-inlines them into the four `__PLACEHOLDER__` tokens in `template.html`. If a font ever needs to change, replace the woff2 file in `src/fonts/` (same filename) and rerun the build — don't hand-edit base64 in the HTML.

## Design tokens and intent

Colors and type are defined as CSS custom properties in `:root` inside `template.html`, not pulled from a generic UI-kit palette — see the inline comments for the reasoning per token. Two tokens (`--ink-faint`, `--copper-deep`) were specifically tuned (not eyeballed) to clear WCAG AA 4.5:1 contrast against every background they're used on; if you change either, recheck contrast against all their usage sites before committing (`--ink-faint` is used against both `--bg` and `--surface`; `--copper-deep` is a hover background under two different dark text colors — the lighter of the two, `--bg`, is the binding constraint, not the darker one, because a darker hover background closes the gap with dark text rather than opening it).

The page commits to a single dark theme by design (a coffee-roastery palette), not a light/dark toggle — this was a deliberate choice, not an oversight.

## The roast-dial SVG

`.roast-dial` (in the hero's right column) is a hand-built freshness gauge, not a chart library. Two things are easy to get wrong if you touch it:

- The `<svg class="dial-svg">` element is rotated `-90deg` in CSS so the gauge starts at 12 o'clock instead of SVG's native 3-o'clock start point. Every child element (`.dial-track`, `.dial-peak`, `.dial-marker`) must be authored in **un-rotated local coordinates** — i.e. don't compute a point's final on-screen position and hardcode that; compute it in the standard SVG circle parametrization (`φ = 0` at 3 o'clock, increasing clockwise) and let the CSS transform carry it into place.
- `.dial-peak`'s arc uses `pathLength="100"` plus a 4-value `stroke-dasharray` (`0 gap dash 100`) rather than `stroke-dashoffset`, specifically to avoid the offset sign-direction ambiguity for circles. If the freshness window (currently hardcoded as day 3–9 of a 14-day cycle) ever changes, recompute the dasharray as percentages of 14 days, not by eyeballing degrees.
