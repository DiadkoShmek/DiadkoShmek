# Visual identity

Static covers for the profile and four public projects. The shared motif is a
source, a decision and a return to a recorded consequence. The illustrations
are navigation and editorial artwork, not measurements or status indicators.

- Graphite and paper variants follow the reader's preferred colour scheme.
- Compact covers use a separate composition for narrow screens.
- Project accents distinguish workflows, research, source review and 3D review.
- Essential descriptions and links remain ordinary README text.
- Assets contain no animation, remote fonts, tracking or personal information.

Regenerate the editable SVG sources with Python 3; no packages are required:

```sh
python3 design/render.py
python3 design/render.py --check
```

Repository READMEs reference these covers directly. The static social previews
and geometric avatar use the same source. Existing project licences and
attribution remain unchanged.

## Resonance profile entrance · 2026-11-08

The profile's editable content owner is `entry.json`; `profile_entry.py`
renders the bilingual README and its static SVG navigation. `render.py`
remains the single generation/check command. Other project covers and the
avatar retain their existing sources.

Thesis: one House, several clear entrances. The book and engineering results
lead; three original projects follow. Wide and narrow SVGs have separate
compositions, with light/dark palettes. Each whole card links to its real
destination; ordinary text and links below it preserve discovery and meaning
when images are unavailable. Illustrations are static and carry no live status.

The entrance uses only public book/project material. Local Resonance language
sources, private runtime and model weights are not published. Repo statuses
and counts live in their source ledgers instead of decorative numeric badges.

GitHub owns the surrounding layout and sanitizes README markup. The profile
uses native headings, links, pictures and collapsed details; there is no custom
JavaScript, injected CSS, animation, remote font or tracking. Review the native
GitHub rendering as well as light/dark mobile and desktop previews after edits.
