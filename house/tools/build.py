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
from reportlab.lib.pagesizes import A5 as PAGE_SIZE
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    Flowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)
from figures import get_drawing, configure_fonts
from plates import house_plate, front_plate, register_book_fonts

ROOT = Path(__file__).resolve().parents[1]
W = PAGE_SIZE[0]-28*mm
INK = colors.HexColor('#283D38')
TEAL = colors.HexColor('#45685D')
MUTED = colors.HexColor('#6D756C')
PALE = colors.HexColor('#ECEFE7')
RULE = colors.HexColor('#D7D9CB')
IVORY = colors.HexColor('#F5F2EA')
GOLD = colors.HexColor('#AD7047')

STYLES = {
    'kicker': ParagraphStyle('kicker',fontName='DejaVuSans-Bold',fontSize=8.0,leading=11,textColor=TEAL,spaceAfter=10),
    'title': ParagraphStyle('title',fontName='Book',fontSize=21,leading=26,textColor=INK,spaceAfter=13),
    'lead': ParagraphStyle('lead',fontName='Book',fontSize=10.4,leading=15.4,textColor=INK,spaceAfter=12),
    'body': ParagraphStyle('body',fontName='Book',fontSize=9.5,leading=14.4,textColor=INK,spaceAfter=8),
    'heading': ParagraphStyle('heading',fontName='Book',fontSize=12.0,leading=17.0,textColor=TEAL,spaceBefore=5,spaceAfter=7,keepWithNext=True),
    'small': ParagraphStyle('small',fontName='DejaVuSans',fontSize=7.2,leading=10.8,textColor=MUTED,spaceAfter=10),
    'formula': ParagraphStyle('formula',fontName='DejaVuSans',fontSize=8.6,leading=13.2,textColor=TEAL,backColor=PALE,borderPadding=7,spaceBefore=3,spaceAfter=13),
    'cell': ParagraphStyle('cell',fontName='Book',fontSize=8.2,leading=12.0,textColor=INK),
    'cellbold': ParagraphStyle('cellbold',fontName='DejaVuSans-Bold',fontSize=7.8,leading=11.5,textColor=INK),
    'th': ParagraphStyle('th',fontName='DejaVuSans-Bold',fontSize=7.5,leading=11,textColor=INK),
    'link': ParagraphStyle('link',fontName='DejaVuSans',fontSize=8.5,leading=12.8,textColor=TEAL,spaceAfter=9),
}


def p(text,style='body'):
    return Paragraph(escape(text),STYLES[style])


class Figure(Flowable):
    def __init__(self,key,lang,width=W):
        super().__init__()
        self.drawing=get_drawing(key,lang) if isinstance(key,str) else key
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
    c.setFillColor(IVORY);c.rect(0,0,*PAGE_SIZE,stroke=0,fill=1)
    left=14*mm
    c.setFillColor(GOLD);c.setFont('DejaVuSans',7.0)
    c.drawString(left,PAGE_SIZE[1]-55,'КНИГА ПРО СПІЛЬНУ РОБОТУ' if lang=='uk' else 'A BOOK ABOUT WORK TOGETHER')
    title='Онтологія<br/>Дому' if lang=='uk' else 'Ontology<br/>of the House'
    q=Paragraph(title,ParagraphStyle('cover-title',fontName='Book',fontSize=35 if lang=='uk' else 32,leading=42,textColor=INK))
    _,h=q.wrap(W,150);q.drawOn(c,left,PAGE_SIZE[1]-89-h)
    q=p(data['subtitle'][lang],'lead');_,h=q.wrap(W,80);q.drawOn(c,left,PAGE_SIZE[1]-213-h)
    d=house_plate();scale=W/d.width
    c.saveState();c.translate(left,120);c.scale(scale,scale);d.drawOn(c,0,0);c.restoreState()
    c.setStrokeColor(GOLD);c.setLineWidth(.7);c.line(left,83,PAGE_SIZE[0]-left,83)
    c.setFillColor(INK);c.setFont('BookItalic',9)
    c.drawString(left,66,data['strapline'][lang])
    c.setFillColor(MUTED);c.setFont('DejaVuSans',6.8)
    c.drawString(left,41,('ВИДАННЯ' if lang=='uk' else 'EDITION')+' 2.0 / 2026')
    c.restoreState()


def markdown(data,lang):
    folder=ROOT/'book'/lang
    folder.mkdir(parents=True,exist_ok=True)
    toc=[];combined=[f'# {data["title"][lang]}\n\n## {data["subtitle"][lang]}\n\n{data["strapline"][lang]}\n\n']
    for i,ch in enumerate(data['chapters'],1):
        section_number=f'{i:02d}' if i<=22 else ('A' if i==23 else 'B')
        part=next((a for a in data.get('parts',[]) if a['before']==ch['id']),None)
        if part:
            toc.append('\n### '+part['title'][lang]+'\n')
            combined.append('\n## '+part['title'][lang]+'\n\n*'+part['question'][lang]+'*\n\n')
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
        intro = ('Дім починається з наміру й набуває форми у відносинах, пам’яті та роботі. Книга веде від питання про спільність до механізмів, а потім повертається до наслідків, заради яких їх будують.' if lang=='uk' else 'The House begins with intent and takes form through relations, memory and work. This book moves from a question about working together to mechanisms, then returns to the consequences they serve.')
        note = ('Це авторський виклад від першої особи, підготовлений у співпраці з AI. Особисту біографію до видання не включено. Поняттєва позиція, виконуваний механізм і дослід мають різну доказову вагу. Джерельні опори винесені в кінець розділів.' if lang=='uk' else 'This first-person account was developed in collaboration with AI. Personal biography is outside the edition. A conceptual position, an executable mechanism and an experiment carry different kinds of evidence. Source notes are placed at chapter ends.')
        story += [p('ПРО ЦЮ КНИГУ' if lang=='uk' else 'ABOUT THIS BOOK','kicker'),p('Спосіб читати' if lang=='uk' else 'A way to read','title'),p(intro),p(note),PageBreak()]
        story += [p('ЗМІСТ' if lang=='uk' else 'CONTENTS','kicker'),p(data['subtitle'][lang],'title')]
        rows=[]
        for i,ch in enumerate(data['chapters'],1):
            part=next((a for a in data.get('parts',[]) if a['before']==ch['id']),None)
            if part: rows.append([p(part['title'][lang],'heading'),p('','small')])
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
            part=next((a for a in data.get('parts',[]) if a['before']==ch['id']),None)
            if part:
                n=data['parts'].index(part)+1
                story += [Spacer(1,24),p(('РУХ ' if lang=='uk' else 'MOVEMENT ')+str(n),'kicker'),p(part['title'][lang],'title'),p(part['question'][lang],'lead'),Spacer(1,18),Figure(house_plate(part['plate']),lang),PageBreak()]
            title=p(ch['title'][lang],'title');title.chapter_key=ch['id']
            kicker=(('РОЗДІЛ' if lang=='uk' else 'CHAPTER')+f' {i:02d}') if i<=22 else (('ДОДАТОК' if lang=='uk' else 'APPENDIX')+(' A' if i==23 else ' B'))
            story += [p(kicker+' / '+', '.join(ch['refs']),'kicker'),title,p(ch['lead'][lang],'lead')]
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
                        ('BACKGROUND',(0,0),(-1,0),PALE),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),
                        ('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),.4,RULE),
                        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
                        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
                    ]));story += [t,Spacer(1,12)]


        def page(c,doc):
            if doc.page==1:
                draw_cover(c,data,lang);return
            c.saveState();c.setFillColor(MUTED);c.setFont('DejaVuSans',6.2)
            c.drawString(14*mm,PAGE_SIZE[1]-12*mm,data['title'][lang]+' / '+data['subtitle'][lang])
            c.setStrokeColor(RULE);c.line(14*mm,18*mm,PAGE_SIZE[0]-14*mm,18*mm)
            c.drawString(14*mm,12*mm,f'{data["date"]} · {data["edition"]}')
            c.drawRightString(PAGE_SIZE[0]-14*mm,12*mm,str(doc.page))
            c.restoreState()

        doc=BookDoc(str(path),pagesize=PAGE_SIZE,leftMargin=14*mm,rightMargin=14*mm,
            topMargin=16*mm,bottomMargin=17*mm,title=data['title'][lang]+' - '+data['subtitle'][lang],
            author='DiadkoShmek',subject='Ontology of the House: intent, memory and shared work',pageCompression=1)
        doc.positions={};doc.build(story,onFirstPage=page,onLaterPages=page)
        if doc.positions==positions and doc.page==total:break
        positions=doc.positions.copy();total=doc.page
    return {'pages':doc.page,'chapters':doc.positions,'language':lang,'pdf':path.name}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font-dir',type=Path)
    parser.add_argument('--pdf-dir',type=Path,default=ROOT/'pdf')
    args=parser.parse_args();configure_fonts(args.font_dir);register_book_fonts(args.font_dir)
    data=json.loads((ROOT/'book/manuscript.json').read_text(encoding='utf-8'))
    args.pdf_dir.mkdir(parents=True,exist_ok=True);(ROOT/'pdf').mkdir(exist_ok=True)
    from reportlab.graphics import renderSVG
    renderSVG.drawToFile(house_plate(),str(ROOT/'assets/cover.svg'))
    for lang in ('uk','en'):
        renderSVG.drawToFile(front_plate(lang),str(ROOT/'assets'/f'front-{lang}.svg'))
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
