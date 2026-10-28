#!/usr/bin/env python3
"""Bilingual, code-native vector plates for the House book.

Requires reportlab and DejaVu Sans. No network, scripts or external SVG assets.
Use get_drawing(key, lang) for PDF composition, or export with the CLI.
"""
from __future__ import annotations

import argparse
import math
import os
import re
from pathlib import Path

from reportlab.graphics.shapes import Drawing, Rect, Line, Circle, Polygon, String
from reportlab.graphics import renderSVG
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

WIDTH, HEIGHT = 1000, 550
NAVY = HexColor('#F2EFE6')
PANEL = HexColor('#FFFEFA')
PANEL2 = HexColor('#E4E9E1')
IVORY = HexColor('#283D38')
MUTED = HexColor('#5F7169')
TEAL = HexColor('#45685D')
COPPER = HexColor('#AD7047')
LINE = HexColor('#B1BAA8')
FONT, BOLD = 'DejaVuSans', 'DejaVuSans-Bold'
KEYS = ('house', 'autonomy', 'memory', 'pole', 'gru', 'support', 'fibers',
        'continuity', 'recovery', 'budova', 'section')
_FONT_DIR: Path | None = None


def configure_fonts(font_dir: str | Path | None = None) -> None:
    """Register regular/bold fonts once. Explicit path or HOUSE_FONT_DIR wins."""
    global _FONT_DIR
    if FONT in pdfmetrics.getRegisteredFontNames() and BOLD in pdfmetrics.getRegisteredFontNames():
        return
    explicit = font_dir or os.environ.get('HOUSE_FONT_DIR')
    candidates = [Path(explicit)] if explicit else [
        Path.home() / '.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/share/fonts/truetype',
        Path('/usr/share/fonts/truetype/dejavu'),
        Path('/usr/local/share/fonts'),
    ]
    for folder in candidates:
        if all((folder / n).is_file() for n in ('DejaVuSans.ttf', 'DejaVuSans-Bold.ttf')):
            for alias, name in ((FONT, 'DejaVuSans.ttf'), (BOLD, 'DejaVuSans-Bold.ttf')):
                if alias not in pdfmetrics.getRegisteredFontNames():
                    pdfmetrics.registerFont(TTFont(alias, str(folder / name)))
            _FONT_DIR = folder
            return
    raise FileNotFoundError('DejaVu Sans fonts not found; pass --font-dir or HOUSE_FONT_DIR')


def pick(lang: str, en: str, uk: str) -> str:
    return uk if lang == 'uk' else en


def plate() -> Drawing:
    d = Drawing(WIDTH, HEIGHT)
    d.add(Rect(0, 0, WIDTH, HEIGHT, fillColor=NAVY, strokeColor=None))
    return d


def text(d, x, top, value, size=22, color=IVORY, bold=False, anchor='middle', maxw=None):
    """Coordinates are top-down; explicit line breaks preserve bilingual layout."""
    font = BOLD if bold else FONT
    lines = value.split('\n')
    if size < 19:
        raise ValueError('Plate text must be at least 19 logical pixels')
    for i, line in enumerate(lines):
        if maxw is not None and pdfmetrics.stringWidth(line, font, size) > maxw:
            raise ValueError(f'Text too wide ({maxw}): {line}')
        d.add(String(x, HEIGHT-top-size-i*size*1.28, line, fontName=font,
                     fontSize=size, fillColor=color, textAnchor=anchor))


def rule(d, x1, y1, x2, y2, color=LINE, width=2, dashed=False):
    d.add(Line(x1, HEIGHT-y1, x2, HEIGHT-y2, strokeColor=color,
               strokeWidth=width, strokeDashArray=[6, 6] if dashed else None))


def arrow(d, x1, y1, x2, y2, color=TEAL, dashed=False):
    rule(d, x1, y1, x2, y2, color, 2.2, dashed)
    a = math.atan2(y2-y1, x2-x1)
    pts = []
    for x, y in ((x2, y2), (x2-11*math.cos(a)+5*math.sin(a), y2-11*math.sin(a)-5*math.cos(a)),
                 (x2-11*math.cos(a)-5*math.sin(a), y2-11*math.sin(a)+5*math.cos(a))):
        pts += [x, HEIGHT-y]
    d.add(Polygon(pts, fillColor=color, strokeColor=None))


def dot(d, x, y, r=5, color=TEAL):
    d.add(Circle(x, HEIGHT-y, r, fillColor=color, strokeColor=None))


def box(d, x, y, w, h, label='', accent=TEAL, fill=PANEL, size=22, bold=False):
    d.add(Rect(x, HEIGHT-y-h, w, h, rx=12, ry=12, fillColor=fill,
               strokeColor=accent, strokeWidth=1.35))
    if label:
        font = BOLD if bold else FONT
        while size > 19 and any(pdfmetrics.stringWidth(s, font, size) > w-22 for s in label.split('\n')):
            size -= 1
        lines = label.count('\n')+1
        total = size + (lines-1)*size*1.28
        text(d, x+w/2, y+(h-total)/2-2, label, size, bold=bold, maxw=w-22)


def ring(d, x, y, r, label='', color=TEAL, size=22):
    d.add(Circle(x, HEIGHT-y, r, fillColor=PANEL, strokeColor=color, strokeWidth=2))
    if label:
        text(d, x, y-size/2-2, label, size, maxw=2*r-8)


def house(lang):
    d = plate()
    box(d, 300, 30, 360, 62, pick(lang,'Human intent','Людський намір'), COPPER, bold=True)
    arrow(d,480,92,480,121)
    for x, en, uk in [(65,'Engineering','Інженерія'),(365,'Meaning','Смисл'),(665,'Research','Дослідження')]:
        box(d,x,125,260,65,pick(lang,en,uk))
    rule(d,195,206,795,206);rule(d,195,190,195,206);rule(d,795,190,795,206)
    arrow(d,495,190,495,235)
    box(d,65,239,860,82,accent=LINE)
    for x,en,uk in [(177,'Memory','Пам’ять'),(388,'Tools','Інструменти'),(605,'Proof','Доказ'),(815,'Recovery','Відновлення')]:
        text(d,x,264,pick(lang,en,uk),21,maxw=194)
    arrow(d,495,321,495,357)
    for x,en,uk in [(65,'Work packages','Робочі пакети'),(365,'Experiments','Досліди'),(665,'Media','Медіа')]:
        box(d,x,360,260,65,pick(lang,en,uk),COPPER)
    arrow(d,495,425,495,456)
    text(d,495,466,pick(lang,'Observed consequence → next choice','Спостережений наслідок → наступний вибір'),22,maxw=820)
    rule(d,936,392,960,392,COPPER);rule(d,960,392,960,60,COPPER)
    arrow(d,960,60,679,60,COPPER)
    return d


def autonomy(lang):
    d=plate()
    labels=[('Task','Завдання'),('Owner\n+ lease','Власник\n+ строк'),('Worker','Виконавець'),('Review','Перевірка'),('Result','Результат')]
    xs=[35,230,425,620,815]
    for i,(x,(en,uk)) in enumerate(zip(xs,labels)):
        text(d,x+75,104,f'{i+1:02}',20,color=MUTED)
        box(d,x,155,150,108,pick(lang,en,uk),COPPER if i in (0,4) else TEAL,size=21)
        if i<4:arrow(d,x+150,209,x+185,209)
    rule(d,500,263,500,336,COPPER,dashed=True)
    box(d,335,338,330,83,pick(lang,'Uncertainty retained','Невідоме збережено'),COPPER,size=22)
    rule(d,665,379,695,379,COPPER,dashed=True);arrow(d,695,379,695,278,COPPER,dashed=True)
    text(d,500,465,pick(lang,'One owner · bounded work · explicit return','Один власник · обмежена праця · явне повернення'),21,maxw=940)
    return d


def memory(lang):
    d=plate()
    box(d,38,175,180,115,pick(lang,'Source bytes\n+ hash','Байти джерела\n+ хеш'),COPPER,size=20)
    arrow(d,218,232,260,232)
    for i in range(3):
        box(d,269+i*7,167+i*10,178,94,'',accent=LINE if i<2 else TEAL)
    text(d,372,201,pick(lang,'Fragments','Фрагменти'),21,maxw=154)
    arrow(d,466,232,509,232)
    for a,b in [((554,186),(625,219)),((625,219),(558,275)),((625,219),(681,168)),((625,219),(681,279))]:rule(d,*a,*b)
    for x,y in [(554,186),(625,219),(558,275),(681,168),(681,279)]:dot(d,x,y,9)
    text(d,615,315,pick(lang,'Graph / index','Граф / індекс'),21,maxw=210)
    arrow(d,706,232,751,232)
    box(d,767,175,193,115,pick(lang,'Retrieval\n+ citations','Пошук\n+ цитати'),size=21)
    rule(d,128,308,128,390,LINE,dashed=True);rule(d,128,390,865,390,LINE,dashed=True)
    arrow(d,865,390,865,306,TEAL,dashed=True)
    box(d,315,362,400,63,pick(lang,'Source + freshness check','Звірка джерела й свіжості'),COPPER,size=21)
    text(d,500,470,pick(lang,'A retrieved claim still needs its source','Знайдене твердження потребує джерела'),21,maxw=930)
    return d


def pole(lang):
    d=plate()
    labels=[('Corpus','Корпус'),('Fragments\ntime · links','Фрагменти\nчас · зв’язки'),('BM25','BM25'),('Citations','Цитати'),('Lexical\ngate','Лексичний\nконтроль')]
    xs=[30,225,420,615,810]
    for i,(x,(en,uk)) in enumerate(zip(xs,labels)):
        box(d,x,156,160,110,pick(lang,en,uk),COPPER if i==0 else TEAL,size=20)
        if i<4:arrow(d,x+160,211,x+185,211)
    rule(d,305,266,305,366,COPPER)
    arrow(d,305,366,438,366,COPPER)
    box(d,445,328,300,78,pick(lang,'Separate dataset','Окремий датасет'),COPPER,size=22)
    text(d,595,430,pick(lang,'Explicit selection + lineage','Явний відбір + походження'),20,maxw=510)
    text(d,500,69,pick(lang,'Retrieval path','Шлях пошуку'),24,bold=True)
    return d


def gru(lang):
    d=plate()
    box(d,35,210,167,100,pick(lang,'Character\nembedding','Символьний\nембединг'),COPPER,size=20)
    arrow(d,202,260,248,260)
    box(d,260,104,193,66,pick(lang,'Previous h','Попередній h'),COPPER,size=21)
    box(d,270,210,170,64,pick(lang,'Reset gate r','Вентиль r'),size=20)
    box(d,270,317,170,64,pick(lang,'Update gate z','Вентиль z'),size=20)
    rule(d,355,170,355,194,TEAL);arrow(d,355,194,355,210)
    rule(d,250,242,250,349,LINE);arrow(d,250,349,270,349)
    rule(d,250,242,270,242,TEAL)
    arrow(d,440,242,500,260);arrow(d,440,349,500,280)
    rule(d,453,137,532,137,COPPER);arrow(d,532,137,532,225,COPPER)
    ring(d,550,270,49,'h',TEAL,30)
    arrow(d,599,270,650,270)
    box(d,661,214,140,110,pick(lang,'Softmax\n+ loss','Softmax\n+ втрата'),size=20)
    arrow(d,801,270,840,270)
    box(d,850,214,120,110,'BPTT\nAdam',COPPER,size=20)
    rule(d,910,324,910,443,COPPER);rule(d,910,443,355,443,COPPER)
    arrow(d,355,443,355,393,COPPER)
    text(d,500,481,pick(lang,'Conceptual training step','Концептуальний крок навчання'),21,maxw=900)
    return d


def support(lang):
    d=plate()
    labels=[('Reserve','Резерв'),('Load','Модель\nу пам’яті'),('Run','Виконання'),('Cleanup','Звільнення'),('Accept','Прийняття')]
    for i,(en,uk) in enumerate(labels):
        x=30+i*195
        box(d,x,190,160,94,pick(lang,en,uk),COPPER if i in (0,4) else TEAL,size=20)
        if i<4:arrow(d,x+160,237,x+185,237)
    box(d,250,68,500,62,pick(lang,'Exact turn · exact source','Точний хід · точне джерело'),COPPER,size=22)
    rule(d,305,130,305,173,LINE,dashed=True);rule(d,890,130,890,173,LINE,dashed=True)
    rule(d,750,100,890,100,LINE,dashed=True);rule(d,890,100,890,130,LINE,dashed=True)
    rule(d,500,284,500,353,COPPER)
    box(d,300,361,400,76,pick(lang,'Failure keeps its reason','Відмова зберігає причину'),COPPER,size=22)
    text(d,500,478,pick(lang,'Resource release precedes result admission','Ресурси звільняються до прийняття результату'),21,maxw=930)
    return d


def fibers(lang):
    d=plate()
    text(d,175,58,pick(lang,'Two histories','Дві історії'),24,bold=True,maxw=300)
    for y,a,b in [(160,'A','B'),(320,'B','A')]:
        ring(d,105,y,34,a,COPPER,27);arrow(d,145,y,204,y,LINE);ring(d,245,y,34,b,TEAL,27)
    arrow(d,292,160,432,223);arrow(d,292,320,432,257)
    box(d,440,188,230,105,pick(lang,'Same counts\nA = 1, B = 1','Однакові суми\nA = 1, B = 1'),size=21)
    arrow(d,670,240,725,240,COPPER)
    box(d,744,146,218,187,pick(lang,'First event?\n\nA or B','Перша подія?\n\nA чи B'),COPPER,size=23)
    rule(d,128,386,878,386,LINE,dashed=True)
    text(d,500,422,pick(lang,'Aggregation loses the order','Агрегація втрачає порядок'),25,bold=True,maxw=920)
    text(d,500,474,pick(lang,'Equal input cannot identify both answers','Однаковий вхід не розрізнить обидві відповіді'),21,maxw=940)
    return d


def continuity(lang):
    d=plate()
    items=[(70,100,'Decision','Рішення'),(375,100,'Effect','Дія'),(680,100,'Observation','Спостереження'),
           (680,340,'Assessment','Оцінка'),(375,340,'Accepted\nrevision','Прийнята\nревізія'),(70,340,'Later\ndecision','Наступне\nрішення')]
    for x,y,en,uk in items:box(d,x,y,250,92,pick(lang,en,uk),COPPER if x==70 else TEAL,size=22)
    arrow(d,320,146,375,146);arrow(d,625,146,680,146);arrow(d,805,192,805,340)
    arrow(d,680,386,625,386);arrow(d,375,386,320,386)
    rule(d,195,340,195,270,COPPER);rule(d,195,270,500,270,COPPER,dashed=True)
    text(d,500,223,pick(lang,'Available ≠ used','Доступне ≠ використане'),22,color=COPPER,maxw=490)
    text(d,500,486,pick(lang,'Continuity is a checked return','Наступність — перевірене повернення'),22,maxw=940)
    return d


def recovery(lang):
    d=plate()
    box(d,45,80,250,100,pick(lang,'Exact request\nID + payload','Точний запит\nID + вміст'),COPPER,size=22)
    box(d,375,80,250,100,pick(lang,'CAS revision','CAS-ревізія'),size=22)
    box(d,705,80,250,100,pick(lang,'Stored receipt','Квитанція'),size=22)
    arrow(d,295,130,375,130);arrow(d,625,130,705,130)
    rule(d,830,180,830,245,COPPER,dashed=True);rule(d,830,245,170,245,COPPER,dashed=True)
    text(d,500,208,pick(lang,'Reply lost','Відповідь втрачено'),20,color=COPPER,maxw=450)
    arrow(d,170,245,170,294,COPPER)
    box(d,45,303,250,92,pick(lang,'Same request','Той самий запит'),COPPER,size=21)
    arrow(d,295,349,705,349,TEAL)
    box(d,705,303,250,92,pick(lang,'Same receipt','Та сама квитанція'),size=21)
    box(d,345,439,310,66,pick(lang,'Stale write refused','Застарілий запис відхилено'),COPPER,size=19)
    rule(d,500,180,500,200,LINE);rule(d,500,270,500,439,COPPER,dashed=True)
    return d


def budova(lang):
    d=plate()
    box(d,40,75,220,91,pick(lang,'Source revision A','Ревізія джерела A'),COPPER,size=20)
    arrow(d,260,120,339,120)
    box(d,345,75,220,91,pick(lang,'Part revision A','Ревізія деталі A'),size=20)
    arrow(d,565,120,664,120)
    box(d,680,58,270,128,pick(lang,'Frozen package A','Незмінний комплект A'),COPPER,size=21)
    # Paper layers below the package make its role tangible.
    for y in (194,202):rule(d,695,y,935,y,LINE)
    arrow(d,455,166,455,304,LINE)
    box(d,345,314,220,105,pick(lang,'Later head B','Нова ревізія B'),size=21)
    text(d,455,447,pick(lang,'New selection','Новий вибір'),20,color=MUTED,maxw=260)
    arrow(d,815,202,815,340,COPPER)
    box(d,670,353,280,77,pick(lang,'Returned fact → A','Повернений факт → A'),COPPER,size=21)
    rule(d,670,391,610,391,COPPER);rule(d,610,391,610,245,COPPER);rule(d,610,245,455,245,COPPER)
    arrow(d,455,245,455,184,COPPER)
    text(d,500,494,pick(lang,'B does not rewrite the issued A package','B не переписує вже виданий комплект A'),22,maxw=940)
    return d


def section(lang):
    """Quiet architectural section: structure, shared spine and return circulation."""
    d=plate()
    # Ground and an open sectional roof.
    rule(d,95,464,921,464,COPPER,3)
    rule(d,150,153,500,56,COPPER,2.5);rule(d,500,56,850,153,COPPER,2.5)
    rule(d,150,153,150,451,LINE,3);rule(d,850,153,850,451,LINE,3)
    # Three floors, open rooms, one continuous infrastructure spine.
    for y in (220,327,434):
        rule(d,150,y,850,y,IVORY,2)
        for x in (180,392,604):
            d.add(Rect(x,HEIGHT-y+14,180,49,fillColor=PANEL,strokeColor=None))
            rule(d,x+18,y-18,x+158,y-18,TEAL,2)
    for x in (378,590):rule(d,x,165,x,434,LINE,1.5)
    d.add(Rect(786,HEIGHT-434,26,272,fillColor=TEAL,strokeColor=None))
    for y in (196,303,410):
        dot(d,799,y,6,NAVY);rule(d,745,y,786,y,TEAL,2)
    # Return path outside the section, with one visible upwards arrow.
    rule(d,878,433,916,433,COPPER);rule(d,916,433,916,130,COPPER)
    arrow(d,916,130,861,130,COPPER)
    text(d,485,163,pick(lang,'Agents','Агенти'),20,color=MUTED,maxw=500)
    text(d,485,270,pick(lang,'Shared infrastructure','Спільна інфраструктура'),20,color=MUTED,maxw=540)
    text(d,485,377,pick(lang,'Applications','Застосунки'),20,color=MUTED,maxw=500)
    return d


_SCENES = {name: globals()[name] for name in KEYS}


def get_drawing(key: str, lang: str = 'en') -> Drawing:
    """Return a standalone 1000×550 vector Drawing for en or uk."""
    if key not in _SCENES:
        raise ValueError(f'Unknown figure {key!r}; choose from {", ".join(KEYS)}')
    if lang not in ('en', 'uk'):
        raise ValueError('Figure language must be en or uk')
    configure_fonts()
    return _SCENES[key](lang)


def export_svg(key: str, lang: str, output: Path) -> None:
    raw = renderSVG.drawToString(get_drawing(key, lang))
    raw = re.sub(r'<!DOCTYPE[^>]*>', '', raw, flags=re.DOTALL)
    raw = raw.replace('<title>...</title>', f'<title>{key} / {lang}</title>')
    raw = raw.replace('<desc>...</desc>', '<desc>Code-native architecture illustration; conceptual relationships and explicit boundaries.</desc>')
    # reportlab aliases are correct for embedded PDF; standalone SVG needs a
    # browser-safe family stack and an explicit weight for the bold alias.
    raw = raw.replace('font-family: DejaVuSans-Bold;', 'font-family: DejaVu Sans, Arial, sans-serif; font-weight: 700;')
    raw = raw.replace('font-family: DejaVuSans;', 'font-family: DejaVu Sans, Arial, sans-serif;')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(raw, encoding='utf-8')


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output-root',type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('--font-dir',type=Path)
    p.add_argument('--key',choices=KEYS,action='append')
    p.add_argument('--lang',choices=('en','uk'),action='append')
    a=p.parse_args()
    configure_fonts(a.font_dir)
    for key in a.key or KEYS:
        for lang in a.lang or ('en','uk'):
            export_svg(key,lang,a.output_root/'assets'/'diagrams'/f'{key}-{lang}.svg')


if __name__=='__main__':
    main()
