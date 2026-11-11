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

## Resonance profile entrance

`entry.json` owns the bilingual content. `profile_entry.py` generates the
README and its compact masthead. A three-node return path carries the shared
identity into the masthead's separate narrow and wide compositions, each with
light and dark palettes.

The book and engineering results lead directly to their sources. Three
original projects follow in a native text list. GitHub headings, links and
collapsed details keep navigation available with images disabled. The current
PR inventory and result counts are maintained in the engineering-results
repository. Review the live GitHub rendering and mobile width after edits.
