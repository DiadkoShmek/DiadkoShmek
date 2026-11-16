"""Render the bilingual GitHub entrance with the standard library."""

from html import escape
import json
from pathlib import Path


DATA = json.loads(Path(__file__).with_name("entry.json").read_text(encoding="utf-8"))
PROFILE = "https://github.com/DiadkoShmek/DiadkoShmek/blob/main/"
STEM = "resonance-signature"
PALETTES = {
    "dark": ("#0d1117", "#102722", "#f0f6fc", "#344652", "#89e4ca", "#f1cc8d"),
    "light": ("#ffffff", "#e6f5ef", "#142330", "#b8c9d3", "#14694f", "#79510e"),
}


def hero(theme, mobile):
    bg, tint, ink, line, mint, amber = PALETTES[theme]
    width, height = (760, 210) if mobile else (1280, 270)
    title = escape(DATA["brand"])
    word_x, word_y, font_size = (36, 138, 90) if mobile else (52, 178, 130)
    mark = "translate(546 31) scale(.78)" if mobile else "translate(912 33) scale(1.08)"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title>
<desc id="desc">Three connected nodes trace a return path.</desc>
<defs>
  <linearGradient id="surface" x1="0" x2="1" y1="0" y2=".65">
    <stop offset=".42" stop-color="{bg}"/>
    <stop offset="1" stop-color="{tint}"/>
  </linearGradient>
</defs>
<rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="24" fill="url(#surface)" stroke="{line}" stroke-width="2"/>
<text x="{word_x}" y="{word_y}" fill="{ink}" font-family="Arial, Helvetica, sans-serif" font-size="{font_size}" font-weight="700" letter-spacing="-2">{title}</text>
<g transform="{mark}" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path d="M29 148V96a67 67 0 0 1 67-67h48a64 64 0 0 1 0 128H82" stroke="{line}" stroke-width="2"/>
  <path d="M29 148h53a27 27 0 0 0 27-27V78a20 20 0 0 1 20-20h15a35 35 0 0 1 0 70h-7" stroke="{mint}" stroke-width="4"/>
  <path d="M29 148v17a12 12 0 0 0 12 12h103a84 84 0 0 0 0-168" stroke="{line}" stroke-width="2" stroke-dasharray="4 8"/>
  <circle cx="29" cy="148" r="9" fill="{mint}"/>
  <circle cx="109" cy="96" r="8" fill="{bg}" stroke="{mint}" stroke-width="3"/>
  <circle cx="144" cy="58" r="8" fill="{amber}"/>
</g>
</svg>
'''


def readme(lang):
    copy = DATA["languages"][lang]
    links = [
        f'- [{book[lang]["title"]}]({book[lang]["url"]})'
        for book in DATA["books"]
    ]
    return "\n".join([
        f'# {copy["heading"]}',
        "",
        f'> {copy["epigraph"]}',
        "",
        *links,
        "",
        f'[{copy["other_language"]}]({PROFILE}{copy["other_file"]})',
        "",
    ])


def outputs(root):
    for theme in PALETTES:
        for mobile in (False, True):
            suffix = f'{theme}{"-mobile" if mobile else ""}.svg'
            yield root / "assets" / "identity" / f"{STEM}-{suffix}", hero(theme, mobile)
    yield root / "README.md", readme("uk")
    yield root / "README.en.md", readme("en")
