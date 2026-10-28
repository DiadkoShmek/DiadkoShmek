"""Original vector illustration: distinct rooms, common ground and a return path."""
from pathlib import Path
from reportlab.graphics.shapes import Drawing, Rect, Line, Circle, Polygon, String
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

INK=HexColor('#283D38');GREEN=HexColor('#45685D')
COPPER=HexColor('#AD7047');LINE=HexColor('#CCD3C4');PAPER=HexColor('#F5F2EA')

def register_book_fonts(folder=None):
    folder=Path(folder) if folder else Path('/usr/share/fonts/truetype/dejavu')
    for alias,name in [('Book','DejaVuSerif.ttf'),('BookBold','DejaVuSerif-Bold.ttf'),('BookItalic','DejaVuSerif-Italic.ttf')]:
        pdfmetrics.registerFont(TTFont(alias,str(folder/name)))
    pdfmetrics.registerFontFamily('Book',normal='Book',bold='BookBold',italic='BookItalic',boldItalic='BookBold')

def house_plate(mode='whole'):
    d=Drawing(620,380)
    d.add(Circle(310,207,142,strokeColor=LINE,fillColor=None,strokeWidth=.8))
    d.add(Circle(310,207,171,strokeColor=LINE,fillColor=None,strokeWidth=.5))
    d.add(Line(55,71,565,71,strokeColor=GREEN,strokeWidth=1.6))
    d.add(Rect(90,81,440,18,strokeColor=None,fillColor=HexColor('#ECEFE7')))
    d.add(Polygon([85,255,310,343,535,255],strokeColor=INK,fillColor=None,strokeWidth=2))
    d.add(Line(85,249,535,249,strokeColor=COPPER,strokeWidth=1.5))
    for x,h in [(105,122),(198,151),(350,137),(443,110)]:
        d.add(Rect(x,99,72,h,strokeColor=GREEN,fillColor=None,strokeWidth=1.2))
        for yy in range(117,int(99+h-10),25):
            d.add(Line(x+13,yy,x+59,yy,strokeColor=LINE,strokeWidth=.7))
        d.add(Rect(x+25,99,22,28,strokeColor=COPPER,fillColor=PAPER,strokeWidth=1.1))
    d.add(Line(141,87,479,87,strokeColor=COPPER,strokeWidth=1.8))
    for x in (141,234,386,479):d.add(Circle(x,87,3,fillColor=COPPER,strokeColor=None))
    d.add(Circle(310,155,24,fillColor=None,strokeColor=COPPER,strokeWidth=1.4))
    d.add(Line(310,99,310,131,strokeColor=COPPER,strokeWidth=1.1))
    d.add(Line(310,179,310,249,strokeColor=GREEN,strokeWidth=1.1))
    for xx,sgn in [(62,1),(558,-1)]:
        d.add(Line(xx,72,xx+sgn*8,174,strokeColor=GREEN,strokeWidth=1.1))
        for yy in (98,123,148):
            d.add(Line(xx+sgn*2,yy,xx+sgn*21,yy+14,strokeColor=GREEN,strokeWidth=.8))
            d.add(Line(xx+sgn*3,yy+9,xx-sgn*11,yy+22,strokeColor=GREEN,strokeWidth=.8))
    if mode=='memory':
        for y in (285,297,309):d.add(Line(270,y,350,y,strokeColor=COPPER,strokeWidth=1.1))
    elif mode=='work':
        for x in (270,310,350):d.add(Circle(x,291,6,fillColor=PAPER,strokeColor=GREEN))
        d.add(Line(276,291,344,291,strokeColor=COPPER,strokeWidth=1))
    elif mode=='return':
        d.add(Circle(310,291,21,fillColor=None,strokeColor=COPPER,strokeWidth=1.2))
        d.add(Polygon([329,296,337,289,327,286],fillColor=COPPER,strokeColor=None))
    return d

def front_plate(lang):
    d=Drawing(1000,610)
    d.add(Rect(0,0,1000,610,fillColor=PAPER,strokeColor=None))
    d.add(String(65,537,'КНИГА ПРО СПІЛЬНУ РОБОТУ' if lang=='uk' else 'A BOOK ABOUT WORK TOGETHER',fontName='DejaVuSans',fontSize=12,fillColor=COPPER))
    d.add(String(65,425,'Онтологія' if lang=='uk' else 'Ontology',fontName='Book',fontSize=55,fillColor=INK))
    d.add(String(65,356,'Дому' if lang=='uk' else 'of the House',fontName='Book',fontSize=58 if lang=='uk' else 41,fillColor=INK))
    lines=['Намір. Окремість.','Пам’ять. Повернення.'] if lang=='uk' else ['Intent. Difference.','Memory. Return.']
    for i,line in enumerate(lines):d.add(String(67,273-i*27,line,fontName='Book',fontSize=18,fillColor=GREEN))
    art=house_plate();art.scale(.84,.84);art.translate(525,120);d.add(art)
    d.add(Line(65,86,935,86,strokeColor=COPPER,strokeWidth=1))
    d.add(String(65,52,'ВИДАННЯ 2.0 / 2026' if lang=='uk' else 'EDITION 2.0 / 2026',fontName='DejaVuSans',fontSize=11,fillColor=GREEN))
    return d
