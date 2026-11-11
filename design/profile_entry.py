"""Static, bilingual GitHub entrance. No network, runtime dependencies or tracking."""
from html import escape
import json
from pathlib import Path

DATA = json.loads(Path(__file__).with_name("entry.json").read_text(encoding="utf-8"))
RAW = "https://raw.githubusercontent.com/DiadkoShmek/DiadkoShmek/main/assets/identity/"
REPO = "https://github.com/DiadkoShmek/DiadkoShmek/blob/main/"
RESULTS = "https://github.com/DiadkoShmek/engineering-results/blob/main/"
PALETTE = {
    "dark": {"bg": "#0d1117", "panel": "#141d27", "fg": "#f0f6fc", "muted": "#b5c3d2", "line": "#344354", "mint": "#89e4ca", "amber": "#f1cc8d", "blue": "#a6caff", "coral": "#f1b59b"},
    "light": {"bg": "#ffffff", "panel": "#f3f7f9", "fg": "#142330", "muted": "#455a6d", "line": "#b8c9d3", "mint": "#14694f", "amber": "#79510e", "blue": "#235d9c", "coral": "#93472b"},
}


def text(x, y, content, size, colour, weight=400, mono=False, spacing=None):
    family = "monospace" if mono else "Arial, Helvetica, sans-serif"
    tracking = f' letter-spacing="{spacing}"' if spacing else ""
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{colour}"{tracking}>{escape(content)}</text>'


def start(width, height, title, description):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(title)}</title>', f'<desc id="desc">{escape(description)}</desc>']


def hero(theme, mobile=False):
    p = PALETTE[theme]
    w, h = (760, 248) if mobile else (1280, 320)
    out = start(w, h, "Resonance — the House of DiadkoShmek", "Independent AI systems, memory, tools and verifiable engineering. Static illustration of connected parts and their return.")
    out += [f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="26" fill="{p["bg"]}" stroke="{p["line"]}" stroke-width="2"/>',
            f'<path d="M44 64H94" stroke="{p["mint"]}" stroke-width="5" stroke-linecap="round"/>',
            text(111, 72, DATA["account"].upper() + " / THE HOUSE", 23, p["muted"], mono=True),
            text(40, 179 if mobile else 202, DATA["brand"], 108 if mobile else 116, p["fg"], weight=700),
            f'<path d="M45 {h-35}H{w-45}" stroke="{p["line"]}"/>']
    if not mobile:
        out += [f'<g fill="none" stroke="{p["line"]}" stroke-width="2">',
                '<path d="M912 100H1030V150H1160V244H912Z"/>',
                '<path d="M912 100V244M1030 150L912 244M1160 244L1030 150"/>',
                f'<circle cx="912" cy="100" r="19" fill="{p["bg"]}" stroke="{p["mint"]}"/>',
                f'<circle cx="1030" cy="150" r="13" fill="{p["bg"]}" stroke="{p["amber"]}"/>',
                f'<circle cx="1160" cy="244" r="19" fill="{p["bg"]}" stroke="{p["mint"]}"/>',
                f'<circle cx="912" cy="244" r="9" fill="{p["mint"]}" stroke="none"/>', '</g>']
    return "\n".join(out) + "\n</svg>\n"


def card(route, lang, theme, mobile=False):
    p, copy = PALETTE[theme], route[lang]
    w, h = (760, 158) if mobile else (1280, 152)
    accent = p[route["accent"]]
    out = start(w, h, copy["title"], copy["description"])
    out += [f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="{p["panel"]}" stroke="{p["line"]}" stroke-width="2"/>',
            f'<path d="M2 35V{h-35}" stroke="{accent}" stroke-width="4"/>',
            text(32, 44, copy["label"], 23 if mobile else 24, p["muted"], mono=True),
            text(32, 112, copy["title"], 46 if mobile else 57, p["fg"], weight=700),
            f'<g fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M{w-91} {h//2+15}L{w-61} {h//2-15}M{w-87} {h//2-15}H{w-61}V{h//2+11}"/></g>']
    return "\n".join(out) + "\n</svg>\n"


def picture(stem, alt, target=None):
    lines = [f'<a href="{escape(target, quote=True)}">'] if target else []
    lines += ['<picture>',
              f'  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="{RAW}{stem}-dark-mobile.svg">',
              f'  <source media="(max-width: 600px)" srcset="{RAW}{stem}-light-mobile.svg">',
              f'  <source media="(prefers-color-scheme: dark)" srcset="{RAW}{stem}-dark.svg">',
              f'  <img src="{RAW}{stem}-light.svg" alt="{escape(alt, quote=True)}" width="1280">', '</picture>']
    if target:
        lines.append('</a>')
    return "\n".join(lines)


def readme(lang):
    copy = DATA["languages"][lang]
    routes = DATA["routes"]
    primary_links = [f'[{route[lang]["title"]}]({route[lang]["url"]})' for route in routes[:2]]
    primary_links.append(f'[{copy["other_language"]}]({REPO}{copy["other_file"]})')
    lines = [picture("resonance", "Resonance — independent AI systems, memory and engineering"),
             f'\n**{copy["intro"]}**', "\n" + " · ".join(primary_links)]
    for i, route in enumerate(DATA["routes"]):
        c = route[lang]
        if i == 2:
            lines.append(f'\n## {copy["projects"]}')
        lines += ["\n" + picture(f'entry-{route["id"]}-{lang}', c["title"] + " — " + c["action"], c["url"]),
                  f'\n{c["description"]} **[{c["action"]}]({c["url"]})**']
        if route["id"] == "house":
            lines[-1] += f' · [PDF]({REPO}house/pdf/the-house-{lang}.pdf)'
        if route["id"] == "results":
            lines.append(f'\n[{"Журнал" if lang == "uk" else "Journal"}]({REPO}RESULTS{"" if lang == "uk" else ".en"}.md) · [{"Метод роботи" if lang == "uk" else "Engineering method"}]({REPO}ENGINEERING.md)')
        if route["id"] == "stroika":
            lines.append(f'\n[{"Код STROIKA" if lang == "uk" else "STROIKA code"}](https://github.com/DiadkoShmek/mae7-viewer)')
    lines += [f'\n[{"Усі власні репозиторії" if lang == "uk" else "All original repositories"}](https://github.com/DiadkoShmek?tab=repositories&type=source)',
              f'\n<details>\n<summary>{copy["archive"]}</summary>\n',
              f'[{"Усі PR та їхні статуси" if lang == "uk" else "All PRs and their statuses"}]({RESULTS}PR_STATUS{"" if lang == "uk" else ".en"}.md) · '
              f'[{"Кейси з першоджерелами" if lang == "uk" else "Source-linked case reports"}]({RESULTS}reports/README.md)',
              '\n</details>', f'\n<details>\n<summary>{copy["method"]}</summary>\n']
    if lang == "uk":
        lines += ['Напрям і відповідальність — мої. Розробка й перевірки — з AI-інструментами. Прототипи мають описані умови та межі перевірок.',
                  '\n[Agent Workflows](https://github.com/DiadkoShmek/evidence-gated-agent-workflows/blob/main/run_proof.py): `python3 run_proof.py`. [Перевірки профілю](' + REPO + '.github/workflows/profile-proof.yml). Питання — через Issues проєктів.']
    else:
        lines += ['I direct the work and own follow-up. Development and verification use AI tools. The prototypes document their test conditions and limits.',
                  '\n[Agent Workflows](https://github.com/DiadkoShmek/evidence-gated-agent-workflows/blob/main/run_proof.py): `python3 run_proof.py`. [Profile checks](' + REPO + '.github/workflows/profile-proof.yml). Questions — through project Issues.']
    lines.append('\n</details>')
    return "\n".join(lines) + "\n"


def outputs(root):
    folder = root / "assets" / "identity"
    for theme in ("dark", "light"):
        for mobile in (False, True):
            suffix = f'{theme}{"-mobile" if mobile else ""}.svg'
            yield folder / f'resonance-{suffix}', hero(theme, mobile)
            for lang in DATA["languages"]:
                for route in DATA["routes"]:
                    yield folder / f'entry-{route["id"]}-{lang}-{suffix}', card(route, lang, theme, mobile)
    yield root / "README.md", readme("uk")
    yield root / "README.en.md", readme("en")
