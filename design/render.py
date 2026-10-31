#!/usr/bin/env python3
"""Render the static GitHub identity. Python standard library only."""
from __future__ import annotations

import argparse
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "identity"
PROJECTS = {
    "profile": ("Engineering", "with evidence.", "AI SYSTEMS / EVIDENCE / REVIEW", "return"),
    "workflows": ("Evidence-gated", "Agent Workflows", "EXECUTABLE REFERENCES", "gate"),
    "ontology": ("AI Ontology", "Memory. Evidence. Revision.", "RESEARCH / BOOK / PROPOSED PROFILE", "book"),
    "signal": ("Signal Desk", "Sources. Review. Handoff.", "PUBLIC-SOURCE RESEARCH", "sources"),
    "stroika": ("STROIKA", "Architectural review.", "3D / PROJECT REFERENCES", "building"),
}
ACCENTS = {
    "profile": ("#79e0c3", "#176b55"),
    "workflows": ("#79e0c3", "#176b55"),
    "ontology": ("#e6c680", "#79551c"),
    "signal": ("#8ebef1", "#285f98"),
    "stroika": ("#e5ad88", "#8a4925"),
}

def text(x, y, value, size, colour, *, weight=400, mono=False, spacing=None):
    family = "monospace" if mono else "Arial, Helvetica, sans-serif"
    tracking = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{colour}"{tracking}>{escape(value)}</text>')

def motif(kind, ink, line, bg):
    start = f'<g fill="none" stroke="{line}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
    if kind in ("return", "gate"):
        shapes = """
          <path d="M826 102H909V178H1037V254H1130"/>
          <path d="M1130 254V298H826V102" stroke-dasharray="5 9"/>
          <rect x="800" y="76" width="108" height="54" rx="13"/>
          <rect x="957" y="151" width="108" height="54" rx="13"/>
          <rect x="1090" y="227" width="108" height="54" rx="13"/>
        """
        shapes += f'<path d="M917 178H941M930 167L941 178L930 189" stroke="{ink}"/>'
        shapes += f'<rect x="834" y="93" width="37" height="19" rx="4" stroke="{ink}"/>'
        shapes += f'<circle cx="1011" cy="178" r="10" stroke="{ink}"/>'
        shapes += f'<path d="M1121 254H1166" stroke="{ink}"/>'
    elif kind == "book":
        shapes = """
          <path d="M805 81L991 112V283L805 251Z"/>
          <path d="M991 112L1177 81V251L991 283Z"/>
          <path d="M817 268L991 301L1165 268"/>
          <path d="M842 122L946 140M842 157L946 175M842 192L915 205"/>
          <path d="M1030 145L1139 126M1030 182L1139 163M1030 219L1102 206"/>
        """
        shapes += f'<path d="M991 112V283" stroke="{ink}" stroke-width="4"/>'
        shapes += f'<circle cx="991" cy="112" r="7" fill="{bg}" stroke="{ink}"/>'
    elif kind == "sources":
        shapes = """
          <rect x="810" y="82" width="108" height="66" rx="13"/>
          <rect x="810" y="211" width="108" height="66" rx="13"/>
          <rect x="1042" y="118" width="138" height="120" rx="17"/>
          <path d="M918 115H979V177H1042M918 244H979V177"/>
          <path d="M835 105H891M835 124H870M835 234H891M835 253H870"/>
        """
        shapes += f'<path d="M1068 148H1146M1068 177H1129M1068 206H1107" stroke="{ink}"/>'
        shapes += f'<circle cx="979" cy="177" r="8" fill="{bg}" stroke="{ink}"/>'
    else:
        shapes = """
          <path d="M821 143L1004 75L1172 147L991 218Z"/>
          <path d="M821 143V258L991 324L1172 252V147M991 218V324"/>
          <path d="M846 153V248L969 295V212M1013 222V295L1149 242V168"/>
          <path d="M855 189L961 230M855 223L961 264M1020 247L1142 199M1020 278L1142 230"/>
          <path d="M884 169V268M923 188V282M1056 207V285M1101 189V264"/>
        """
        shapes += f'<path d="M821 143L991 218L1172 147" stroke="{ink}" stroke-width="3.5"/>'
    return start + shapes + "</g>"

def svg(project, theme="dark", mobile=False):
    first, second, label, kind = PROJECTS[project]
    dark = theme == "dark"
    bg, fg, muted, line = (("#0d1117", "#f0f6fc", "#9da7b3", "#303b48") if dark
                           else ("#f6f8fa", "#17212d", "#57606a", "#c7d0d9"))
    accent = ACCENTS[project][0 if dark else 1]
    width, height = (760, 320) if mobile else (1280, 360)
    title = first + " — " + second
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">{escape(title)}</title>",
        f"<desc id=\"desc\">{escape(label)}. Static editorial illustration of linked records.</desc>",
        f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="22" fill="{bg}" stroke="{line}" stroke-width="2"/>',
    ]
    if mobile:
        parts += [
            f'<path d="M40 43H100" stroke="{accent}" stroke-width="5" stroke-linecap="round"/>',
            text(40, 126, first, 59 if project == "workflows" else 66, fg, weight=700),
            text(40, 201, second, 55 if project in ("profile", "workflows") else 35, accent, weight=700),
            text(40, 272, "DIADKOSHMEK" if project == "profile" else label, 21, muted, mono=True, spacing="1.1"),
            f'<path d="M663 250H711V298H663Z" fill="none" stroke="{line}" stroke-width="2"/>',
            f'<circle cx="711" cy="250" r="6" fill="{accent}"/>',
        ]
    else:
        parts += [
            text(58, 66, label, 20, muted, mono=True, spacing="1.7"),
            text(55, 162, first, 70 if project != "stroika" else 84, fg, weight=700),
            text(58, 237, second, 62 if project in ("profile", "workflows") else 36, accent, weight=700),
            f'<path d="M58 293H126" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>',
            text(148, 300, "DIADKOSHMEK", 20, muted, mono=True, spacing="1.8"),
            motif(kind, accent, line, bg),
        ]
    return "\n".join(parts) + "\n</svg>\n"

def social_svg(project):
    cover = svg(project)
    body = cover.split('>', 1)[1].rsplit('</svg>', 1)[0]
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" viewBox="0 0 1280 640" role="img">\n'
            '<rect width="1280" height="640" fill="#0d1117"/>\n'
            '<g transform="translate(0 128)">' + body + '</g>\n'
            + text(58, 565, "SOURCES / DECISIONS / CONSEQUENCES", 24, "#9da7b3", mono=True, spacing="1.2")
            + '\n</svg>\n')

def avatar():
    return """<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512" role="img" aria-labelledby="title">
<title id="title">DiadkoShmek geometric D mark</title>
<rect width="512" height="512" rx="104" fill="#0d1117"/>
<path d="M159 111H249C341 111 398 168 398 256S341 401 249 401H159" fill="none" stroke="#79e0c3" stroke-width="38" stroke-linecap="square"/>
<path d="M159 181V331" fill="none" stroke="#f0f6fc" stroke-width="38"/>
<circle cx="159" cy="111" r="19" fill="#e6c680"/>
</svg>
"""

def outputs(only=None):
    for project in PROJECTS:
        if only and project != only:
            continue
        for theme in ("dark", "light"):
            for mobile in (False, True):
                name = f"{project}-{theme}{'-mobile' if mobile else ''}.svg"
                yield OUT / name, svg(project, theme, mobile)
        yield OUT / f"{project}-social.svg", social_svg(project)
    if not only or only == "profile":
        yield OUT / "avatar.svg", avatar()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--only", choices=PROJECTS)
    args = parser.parse_args()
    for path, content in outputs(args.only):
        if args.check:
            if not path.exists() or path.read_text() != content:
                raise SystemExit(f"Identity asset differs: {path.relative_to(ROOT)}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    print("Identity assets match source" if args.check else "Identity assets rendered")

if __name__ == "__main__":
    main()
