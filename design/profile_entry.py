"""Render the bilingual GitHub entrance with the standard library."""

from html import escape
import json
from pathlib import Path


DATA = json.loads(Path(__file__).with_name("entry.json").read_text(encoding="utf-8"))
PROFILE = "https://github.com/DiadkoShmek/DiadkoShmek/blob/main/"
RESULTS = "https://github.com/DiadkoShmek/engineering-results/blob/main/"
RAW = "https://raw.githubusercontent.com/DiadkoShmek/DiadkoShmek/main/assets/identity/"
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


def picture():
    return f'''<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="{RAW}{STEM}-dark-mobile.svg">
  <source media="(max-width: 600px)" srcset="{RAW}{STEM}-light-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="{RAW}{STEM}-dark.svg">
  <img src="{RAW}{STEM}-light.svg" alt="Resonance" width="1280">
</picture>'''


def readme(lang):
    copy = DATA["languages"][lang]
    book, results = (route[lang] for route in DATA["primary"])
    book_pdf = f"{PROFILE}house/pdf/the-house-{lang}.pdf"
    stroika = "https://github.com/DiadkoShmek/mae7-viewer"
    originals = "https://github.com/DiadkoShmek?tab=repositories&type=source"
    lines = [
        picture(),
        f'\n**{copy["intro"]}**',
        f'\n- **[{book["title"]}]({book["url"]})** — {book["description"]} [PDF]({book_pdf})',
        f'- **[{results["title"]}]({results["url"]})** — {results["description"]}',
        f'\n[{copy["other_language"]}]({PROFILE}{copy["other_file"]})',
        f'\n## {copy["projects"]}\n',
    ]
    for project in DATA["projects"]:
        lines.append(f'- **[{project["title"]}]({project["url"]})** — {project[lang]}')
    lines[-1] += f' [{"Код" if lang == "uk" else "Code"}]({stroika})'
    lines.extend([
        f'\n[{"Усі власні репозиторії" if lang == "uk" else "All original repositories"}]({originals})',
        f'\n<details>\n<summary>{copy["archive"]}</summary>\n',
        f'[{"Усі PR та їхні статуси" if lang == "uk" else "All PRs and their statuses"}]({RESULTS}PR_STATUS{"" if lang == "uk" else ".en"}.md) · '
        f'[{"Кейси з першоджерелами" if lang == "uk" else "Source-linked case reports"}]({RESULTS}reports/README.md)',
        '\n</details>',
        f'\n<details>\n<summary>{copy["method"]}</summary>\n',
    ])
    if lang == "uk":
        lines.append("Напрям і відповідальність — мої. Розробка й перевірки — з AI-інструментами. Прототипи мають описані умови та межі перевірок.")
    else:
        lines.append("I direct the work and own follow-up. Development and verification use AI tools. The prototypes document their test conditions and limits.")
    lines.extend([
        f'\n[{"Журнал" if lang == "uk" else "Journal"}]({PROFILE}RESULTS{"" if lang == "uk" else ".en"}.md) · '
        f'[{"Метод роботи" if lang == "uk" else "Engineering method"}]({PROFILE}ENGINEERING.md) · '
        f'[{"Перевірки профілю" if lang == "uk" else "Profile checks"}]({PROFILE}.github/workflows/profile-proof.yml)',
        '\n[Agent Workflows](https://github.com/DiadkoShmek/evidence-gated-agent-workflows/blob/main/run_proof.py): `python3 run_proof.py`.',
        '\n</details>',
    ])
    return "\n".join(lines) + "\n"


def outputs(root):
    for theme in PALETTES:
        for mobile in (False, True):
            suffix = f'{theme}{"-mobile" if mobile else ""}.svg'
            yield root / "assets" / "identity" / f"{STEM}-{suffix}", hero(theme, mobile)
    yield root / "README.md", readme("uk")
    yield root / "README.en.md", readme("en")
