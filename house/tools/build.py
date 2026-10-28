"""Build the bilingual publication, not the private House runtime.

Usage: python -B tools/build.py [--font-dir DIR] [--pdf-dir DIR]
Requires ReportLab. No network, model calls, runtime imports or private sources.
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    Flowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)
from figures import get_drawing, configure_fonts

ROOT = Path(__file__).resolve().parents[1]
W = A4[0]-40*mm
INK = colors.HexColor('#172C42')
TEAL = colors.HexColor('#176F75')
MUTED = colors.HexColor('#526579')
PALE = colors.HexColor('#F1F5F5')
RULE = colors.HexColor('#D8E2E5')
IVORY = colors.HexColor('#F6F2E9')
GOLD = colors.HexColor('#C59A53')

STYLES = {
    'kicker': ParagraphStyle('kicker',fontName='DejaVuSans-Bold',fontSize=8.0,leading=11,textColor=TEAL,spaceAfter=10),
    'title': ParagraphStyle('title',fontName='DejaVuSans-Bold',fontSize=23,leading=28,textColor=INK,spaceAfter=14),
    'lead': ParagraphStyle('lead',fontName='DejaVuSans',fontSize=11.0,leading=16.1,textColor=INK,spaceAfter=15),
    'body': ParagraphStyle('body',fontName='DejaVuSans',fontSize=10.1,leading=14.7,textColor=INK,spaceAfter=11),
    'heading': ParagraphStyle('heading',fontName='DejaVuSans-Bold',fontSize=11.2,leading=15.8,textColor=TEAL,spaceBefore=5,spaceAfter=7,keepWithNext=True),
    'small': ParagraphStyle('small',fontName='DejaVuSans',fontSize=8.3,leading=11.7,textColor=MUTED,spaceAfter=10),
    'formula': ParagraphStyle('formula',fontName='DejaVuSans',fontSize=9.3,leading=13.2,textColor=TEAL,backColor=PALE,borderPadding=7,spaceBefore=3,spaceAfter=13),
    'cell': ParagraphStyle('cell',fontName='DejaVuSans',fontSize=9.15,leading=12.9,textColor=INK),
    'cellbold': ParagraphStyle('cellbold',fontName='DejaVuSans-Bold',fontSize=9.15,leading=12.9,textColor=INK),
    'th': ParagraphStyle('th',fontName='DejaVuSans-Bold',fontSize=8.6,leading=12,textColor=colors.white),
    'link': ParagraphStyle('link',fontName='DejaVuSans',fontSize=9.3,leading=13.4,textColor=TEAL,spaceAfter=9),
}


def p(text,style='body'):
    return Paragraph(escape(text),STYLES[style])


class Figure(Flowable):
    def __init__(self,key,lang,width=W):
        super().__init__()
        self.drawing=get_drawing(key,lang)
        self.width=width
        self.scale=width/self.drawing.width
        self.height=self.drawing.height*self.scale

    def draw(self):
        self.canv.saveState()
        self.canv.scale(self.scale,self.scale)
        self.drawing.drawOn(self.canv,0,0)
        self.canv.restoreState()


class BookDoc(SimpleDocTemplate):
    def afterFlowable(self,f):
        key=getattr(f,'chapter_key',None)
        if key:
            self.positions[key]=self.page
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(f.getPlainText(),key,0,False)


def draw_cover(c,data,lang):
    c.saveState()
    c.setFillColor(INK);c.rect(0,0,*A4,stroke=0,fill=1)
    c.setFillColor(GOLD);c.setFont('DejaVuSans-Bold',9)
    c.drawString(22*mm,A4[1]-32*mm,'АРХІТЕКТУРНА КНИГА' if lang=='uk' else 'AN ARCHITECTURE BOOK')
    c.setFillColor(IVORY);c.setFont('DejaVuSans-Bold',58 if lang=='en' else 72)
    c.drawString(21*mm,A4[1]-69*mm,data['title'][lang])
    subtitle=Paragraph(escape(data['subtitle'][lang]),ParagraphStyle(
        'cover-sub',parent=STYLES['title'],textColor=IVORY,fontSize=22,leading=29))
    _,h=subtitle.wrap(W,100)
    subtitle.drawOn(c,22*mm,A4[1]-86*mm-h)
    figure=get_drawing('section',lang)
    scale=(A4[0]-44*mm)/figure.width
    c.translate(22*mm,69*mm);c.scale(scale,scale)
    figure.drawOn(c,0,0)
    c.restoreState();c.saveState()
    c.setFillColor(IVORY);c.setFont('DejaVuSans',10.5)
    c.drawString(22*mm,54*mm,data['strapline'][lang])
    c.setStrokeColor(GOLD);c.line(22*mm,39*mm,A4[0]-22*mm,39*mm)
    c.setFillColor(GOLD);c.setFont('DejaVuSans',8.5)
    edition='РЕДАКЦІЯ' if lang=='uk' else 'EDITION'
    c.drawString(22*mm,28*mm,f'{edition} {data["edition"]}   /   {data["date"]}')
    c.restoreState()


def markdown(data,lang):
    folder=ROOT/'book'/lang
    folder.mkdir(parents=True,exist_ok=True)
    toc=[];combined=[f'# {data["title"][lang]}\n\n## {data["subtitle"][lang]}\n\n{data["strapline"][lang]}\n\n']
    for i,ch in enumerate(data['chapters'],1):
        section_number=f'{i:02d}' if i<=22 else ('A' if i==23 else 'B')
        lines=[f'# {section_number}. {ch["title"][lang]}\n\n',ch['lead'][lang]+'\n\n']
        for b in ch['blocks']:
            kind=b['type']
            if kind=='paragraph':lines.append(b[lang]+'\n\n')
            elif kind=='heading':lines.append('## '+b[lang]+'\n\n')
            elif kind=='figure':lines.append(f'![{b[lang]}](../../assets/diagrams/{b["key"]}-{lang}.svg)\n\n*{b[lang]}*\n\n')
            elif kind=='equation':lines.append('$$\n'+b['latex']+'\n$$\n\n')
            elif kind=='table':
                lines.append('| '+' | '.join(b['headers'][lang])+' |\n| --- | --- |\n')
                for row in b['rows']:lines.append('| '+' | '.join(row[lang])+' |\n')
                lines.append('\n')
            elif kind=='links':
                for item in b['items']:lines.append(f'- [{item["label"][lang]}]({item["url"]})\n')
                lines.append('\n')
            else:raise ValueError(kind)
        label='Опори' if lang=='uk' else 'Evidence basis'
        lines.append(label+': '+', '.join(f'[{ref}](../../EVIDENCE.md#{ref.lower()})' for ref in ch['refs'])+'.\n')
        filename=ch['id']+'.md';toc.append(f'- {section_number}. [{ch["title"][lang]}]({filename})')
        if i>1:lines.append(f'\n← [{"Попередній" if lang=="uk" else "Previous"}]({data["chapters"][i-2]["id"]}.md)')
        if i<len(data['chapters']):lines.append(f' | [{"Наступний" if lang=="uk" else "Next"}]({data["chapters"][i]["id"]}.md) →')
        (folder/filename).write_text(''.join(lines)+'\n',encoding='utf-8')
        clean=''.join(lines)
        for marker in ('\n← [Previous]','\n← [Попередній]','\n | [Next]','\n | [Наступний]'):
            clean=clean.split(marker)[0]
        combined.append(clean+'\n\n---\n\n')
    title='Зміст' if lang=='uk' else 'Contents'
    navigation='Українська' if lang=='uk' else 'English'
    single='Суцільна версія' if lang=='uk' else 'Single-page edition'
    (folder/'README.md').write_text(f'# {data["title"][lang]}\n\n{data["subtitle"][lang]}\n\n{navigation} · [PDF](../../pdf/the-house-{lang}.pdf) · [{single}](BOOK.md)\n\n## {title}\n\n'+'\n'.join(toc)+'\n',encoding='utf-8')
    (folder/'BOOK.md').write_text(''.join(combined),encoding='utf-8')


def build_pdf(data,lang,path):
    positions={}
    total=24
    for run in range(3):
        story=[Spacer(1,1),PageBreak()]
        story += [p('ЗМІСТ' if lang=='uk' else 'CONTENTS','kicker'),p(data['subtitle'][lang],'title')]
        rows=[]
        for i,ch in enumerate(data['chapters'],1):
            section_number=f'{i:02d}' if i<=22 else ('A' if i==23 else 'B')
            title=Paragraph(f'<link href="#{ch["id"]}">{section_number}   {escape(ch["title"][lang])}</link>',STYLES['cell'])
            rows.append([title,p(str(positions.get(ch['id'],i+2)),'cellbold')])
        toc=Table(rows,colWidths=[W-25,25]);toc.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),.35,RULE),
            ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
            ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),3),
        ]));story += [toc]
        for i,ch in enumerate(data['chapters'],1):
            while story and isinstance(story[-1],Spacer):story.pop()
            story.append(PageBreak())
            title=p(ch['title'][lang],'title');title.chapter_key=ch['id']
            kicker=(('РОЗДІЛ' if lang=='uk' else 'CHAPTER')+f' {i:02d}') if i<=22 else (('ДОДАТОК' if lang=='uk' else 'APPENDIX')+(' A' if i==23 else ' B'))
            story += [p(kicker,'kicker'),title,p(ch['lead'][lang],'lead')]
            for b in ch['blocks']:
                kind=b['type']
                if kind in ('paragraph','heading'):story.append(p(b[lang],'body' if kind=='paragraph' else 'heading'))
                elif kind=='figure':story += [Figure(b['key'],lang),Spacer(1,5),p(b[lang],'small')]
                elif kind=='equation':story.append(p(b['text'],'formula'))
                elif kind=='links':
                    for item in b['items']:
                        href=escape(item['url'],{'"':'&quot;'})
                        story.append(Paragraph(f'<link href="{href}">{escape(item["label"][lang])}</link>',STYLES['link']))
                elif kind=='table':
                    rows=[[p(t,'th') for t in b['headers'][lang]]]
                    rows += [[p(r[lang][0],'cellbold'),p(r[lang][1],'cell')] for r in b['rows']]
                    t=Table(rows,colWidths=[W*.30,W*.70],repeatRows=1)
                    t.setStyle(TableStyle([
                        ('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),
                        ('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),.4,RULE),
                        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
                        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
                    ]));story += [t,Spacer(1,12)]
            story.append(p(('Опори: ' if lang=='uk' else 'Evidence basis: ')+', '.join(ch['refs'])+'.','small'))

        def page(c,doc):
            if doc.page==1:
                draw_cover(c,data,lang);return
            c.saveState();c.setFillColor(MUTED);c.setFont('DejaVuSans',7.2)
            c.drawString(20*mm,A4[1]-12*mm,data['title'][lang]+' / '+data['subtitle'][lang])
            c.setStrokeColor(RULE);c.line(20*mm,18*mm,A4[0]-20*mm,18*mm)
            c.drawString(20*mm,12*mm,f'{data["date"]} · {data["edition"]}')
            c.drawRightString(A4[0]-20*mm,12*mm,f'{doc.page:02d} / {total:02d}')
            c.restoreState()

        doc=BookDoc(str(path),pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,
            topMargin=22*mm,bottomMargin=24*mm,title=data['title'][lang]+' - '+data['subtitle'][lang],
            author='',subject='First-person architectural publication',pageCompression=1)
        doc.positions={};doc.build(story,onFirstPage=page,onLaterPages=page)
        if doc.positions==positions and doc.page==total:break
        positions=doc.positions.copy();total=doc.page
    return {'pages':doc.page,'chapters':doc.positions,'language':lang,'pdf':path.name}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font-dir',type=Path)
    parser.add_argument('--pdf-dir',type=Path,default=ROOT/'pdf')
    args=parser.parse_args();configure_fonts(args.font_dir)
    data=json.loads((ROOT/'book/manuscript.json').read_text(encoding='utf-8'))
    args.pdf_dir.mkdir(parents=True,exist_ok=True);(ROOT/'pdf').mkdir(exist_ok=True)
    reports=[]
    for lang in ('en','uk'):
        markdown(data,lang)
        path=args.pdf_dir/f'the-house-{lang}.pdf'
        reports.append(build_pdf(data,lang,path))
        destination=ROOT/'pdf'/path.name
        if path.resolve()!=destination.resolve():shutil.copy2(path,destination)
    (ROOT/'publication.json').write_text(json.dumps({'edition':data['edition'],'date':data['date'],'books':reports},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    from check import write_manifest
    write_manifest()
    print(json.dumps(reports,ensure_ascii=False))


if __name__=='__main__':main()
