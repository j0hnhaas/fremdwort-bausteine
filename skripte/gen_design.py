import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json, os, html
from PIL import ImageFont

ROOT = 'design'
os.makedirs(ROOT, exist_ok=True)
d = json.load(open('daten/merkblatt-eintraege.json', encoding='utf-8'))

F = '/usr/share/fonts/opentype/inter/'
REG = ImageFont.truetype(F + 'Inter-Regular.otf', 125)
SB = ImageFont.truetype(F + 'Inter-SemiBold.otf', 125)
def tw(font, txt, size):
    return font.getlength(txt) * size / 125
def lines(txt, width, size, font=REG):
    words = txt.split(' '); n = 1; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if tw(font, t, size) > width:
            n += 1; cur = w
        else:
            cur = t
    return n

COL = {'A': '#C4523A', 'K': '#8A6410', 'E': '#9B2F58'}
INK = '#1B1B1B'; GREY = '#555555'; GREY2 = '#6B6B6B'; RULE = '#DADADA'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""><link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,500;0,600;0,700;1,400&amp;family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&amp;display=swap" rel="stylesheet">'

def esc(s):
    return html.escape(s, quote=True)

def head(title):
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>{esc(title)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0;background:#ffffff}}
a{{color:#9B2F58}}a:hover{{color:#6E1F3E}}
.e{{padding:4px 0 0 0;border-bottom:1px solid {RULE};overflow:hidden;box-sizing:border-box}}
.r{{font-size:12px;line-height:15px;color:{GREY2};font-variant-numeric:tabular-nums;font-weight:500}}
.d{{display:flex;gap:1.5px;flex:none}}
.d span{{width:4px;height:4px;border-radius:2px;box-sizing:border-box}}
.l1{{font-size:12.5px;line-height:15px;white-space:nowrap;color:{INK}}}
.l1 b{{font-weight:600}}
.l1 i{{font-style:italic;color:{GREY}}}
.l2{{font-size:12px;line-height:14.5px;white-space:nowrap;color:{GREY};display:flex;justify-content:space-between;align-items:center;gap:8px}}
.h{{font-size:10.5px;font-weight:600;letter-spacing:0.02em;color:{GREY2}}}
</style>
</helmet>
'''

def tail(props):
    return f'''</x-dc>
<script type="text/x-dc" data-dc-script data-props='{json.dumps(props, ensure_ascii=False)}'>
class Component extends DCLogic {{
renderVals() {{
return {{ accent: this.props.accent ?? '{props["accent"]["default"]}' }};
}}
}}
</script>
</body>
</html>
'''

def dots(n, accent_hole, legend=False):
    out = []
    for i in range(5):
        if i < n:
            out.append(f'<span style="background: {accent_hole}"></span>')
        else:
            out.append('<span style="border: 1px solid #BDBDBD"></span>')
    st = ' style="margin-top: 0"' if legend else ''
    return f'<div class="d"{st} aria-hidden="true">' + ''.join(out) + '</div>'

FOOT = ('Häufigkeit = Vorkommen je 1 Million Wörter in 44,7 Mio. Wörtern aus Nachrichten (2024), deutscher Wikipedia (2021) '
        'und österreichischen Webseiten (2023). Daten: Leipzig Corpora Collection, Lizenz CC BY.')
LEG = [(5, 'über 1.000'), (4, '300–999'), (3, '100–299'), (2, '30–99'), (1, 'unter 30')]

PAGES = [
    ('A', 'Vorsilben.dc.html', 'Vorsilben', 2,
     'Sie stehen am Wortanfang und verändern die Bedeutung. Die 72 häufigsten, alphabetisch geordnet.'),
    ('K', 'Wortstaemme.dc.html', 'Wortstämme', 3,
     'Sie tragen den Kern der Bedeutung. Die 72 häufigsten, alphabetisch geordnet.'),
    ('E', 'Nachsilben.dc.html', 'Nachsilben', 4,
     'Sie stehen am Wortende und bestimmen oft die Wortart. Die 72 häufigsten, alphabetisch geordnet.'),
]

def content_page(p, fname, title, num, sub):
    accent = COL[p]; H = '{{accent}}'
    rows = d[p]
    assert len(rows) == 72
    legend = ' '.join(
        f'<span style="display: inline-flex; align-items: center; gap: 5px; margin-right: 12px">{dots(n, H, True)}<span>{t}</span></span>'
        for n, t in LEG)
    items = []
    for x in rows:
        items.append(
            f'<div class="e"><div class="l1"><b style="color: {H}">{esc(x["label"])}</b> (<i>{esc(x["herk"])}</i>) {esc(x["bed"])}</div>'
            f'<div class="l2"><span>{esc(x["bsp"])}</span>{dots(x["dots"], H)}</div></div>')
    sub_lines = lines(sub, 714, 13.5)
    foot_lines = lines(FOOT, 640, 12)
    body = f'''<div style="width: 794px; height: 1123px; box-sizing: border-box; padding: 36px 40px 30px 40px; display: flex; flex-direction: column; font-family: Inter, system-ui, sans-serif; color: {INK}; background: #ffffff">
<div style="font-size: 12px; line-height: 16px; letter-spacing: 0.08em; text-transform: uppercase; color: {GREY2}; font-weight: 600">Fremdwörter knacken · Seite {num} von 4</div>
<div style="display: flex; align-items: baseline; gap: 14px; margin-top: 6px">
<h1 style="margin: 0; font-family: 'Source Serif 4', Georgia, serif; font-size: 34px; line-height: 40px; font-weight: 700; color: {H}">{title}</h1>
<div style="height: 3px; flex: 1 1 auto; background: {H}; align-self: center; opacity: 0.25"></div>
</div>
<p style="margin: 6px 0 0 0; font-size: 13.5px; line-height: 18px; color: {GREY}">{esc(sub)}</p>
<div style="margin-top: 8px; font-size: 12px; line-height: 16px; color: {GREY}; display: flex; align-items: center; flex-wrap: wrap"><span style="margin-right: 10px; font-weight: 600; color: {INK}">Häufigkeit:</span>{legend}</div>
<div style="margin-top: 14px; height: 876px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); grid-template-rows: repeat(24, minmax(0, 1fr)); grid-auto-flow: column; column-gap: 20px; border-top: 2px solid {H}">
{chr(10).join(items)}
</div>
<div style="margin-top: auto; padding-top: 10px; display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; font-size: 12px; line-height: 15px; color: {GREY2}">
<span style="max-width: 640px">{esc(FOOT)}</span>
<span style="font-weight: 600; color: {INK}">{num}</span>
</div>
</div>
'''
    props = {"accent": {"editor": "color", "default": accent, "options": [COL['A'], COL['K'], COL['E'], '#1B1B1B']},
             "$preview": {"width": 794, "height": 1123}}
    # Höhenbudget
    hgt = 36 + 16 + 6 + 40 + 6 + 18 * sub_lines + 8 + 16 + 14 + 876 + 10 + 15 * foot_lines + 30
    return head(f'{title} – Fremdwörter knacken') + body + tail(props), hgt, sub_lines, foot_lines

budgets = {}
for p, fname, title, num, sub in PAGES:
    src, hgt, sl, fl = content_page(p, fname, title, num, sub)
    open(f'{ROOT}/{fname}', 'w', encoding='utf-8').write(src)
    budgets[fname] = (hgt, sl, fl, len(src))
print(budgets)

# ======================= Seite 1 =======================
V, S, N = COL['A'], COL['K'], COL['E']
LEAD = ('Viele Fremdwörter bestehen aus wenigen lateinischen und griechischen Bausteinen. Wer diese Bausteine kennt, '
        'kann unbekannte Wörter oft selbst entschlüsseln. Die Seiten 2 bis 4 zeigen je 72 Bausteine, sortiert danach, '
        'wie oft sie in heutigen Texten vorkommen.')
HOW = [
    ('Fett', 'der Baustein; in Klammern seine Herkunft: lat. = lateinisch, griech. = griechisch, franz. = französisch.'),
    ('Danach', 'die Ursprungsbedeutung, darunter zwei Beispiele.'),
    ('Punkte', 'Häufigkeit: fünf = über 1.000, einer = unter 30 je Million Wörter.'),
]
EX = [
    ('Produkt', [('pro', V), ('dukt', S)], 'das Hervor-Geführte', 'Erzeugnis'),
    ('international', [('inter', V), ('nat', S), ('ion', N), ('al', N)], 'zwischen den Völkern', 'zwischenstaatlich'),
    ('Transport', [('trans', V), ('port', S)], 'das Hinüber-Tragen', 'Beförderung'),
    ('Reaktion', [('re', V), ('akt', S), ('ion', N)], 'das Zurück-Handeln', 'Antwort auf etwas'),
    ('Demokratie', [('demo', S), ('kratie', N)], 'Volks-Herrschaft', 'Herrschaft des Volkes'),
    ('Autobiografie', [('auto', V), ('bio', S), ('grafie', N)], 'Selbst-Leben-Beschreibung', 'eigene Lebensgeschichte'),
]
TIPS = [
    ('Lautangleichung.', 'kon- wird zu kom-, kol-, kor-, ko- (Kombination, Kollege, korrekt). Ebenso in- zu im-, il-, ir- und ad- zu ak-, al-, at-.'),
    ('Ein Stamm, mehrere Formen.', 'fakt, fekt, fiz (Faktor, Effekt, offiziell) oder zept, zip (Konzept, Prinzip).'),
    ('Gleiche Form, andere Bedeutung.', 'in- heißt „hinein“ (Import) oder „nicht“ (indirekt). Der Satz entscheidet.'),
    ('Griechisch = Lateinisch.', 'syn- = kon- (zusammen), hyper- = super- (über), poly- = multi- (viel), mono- = uni- (eins).'),
    ('Vorsicht, Doppelgänger.', 'Antilope hat kein anti-, konnte kein kon-, Regen kein reg-.'),
    ('Urbedeutung ist ein Hinweis.', 'Ein Projekt ist kein „Wurf“ mehr.'),
]
METHOD = ('Gezählt wurde in drei frei lizenzierten Textsammlungen der Leipzig Corpora Collection (Nachrichten 2024, Wikipedia 2021, '
          'österreichische Webseiten 2023; zusammen 44,7 Mio. Wörter). Geprüft wurden 251 mögliche Bausteine: Vorsilben nur am '
          'Wortanfang, Nachsilben nur am Wortende, Stämme an jeder Stelle. Gleich lautende deutsche Wörter, Namen und Marken wurden '
          'ausgeschlossen, die häufigsten Treffer von Hand geprüft. Alle drei Textsorten ergeben fast dieselben Ranglisten. '
          'Werte gerundet, Bedeutungen vereinfacht. Stand: November 2026.')
SRC = ('Daten: Leipzig Corpora Collection: German news corpus (2024), German Wikipedia corpus (2021), German (Austria) web corpus (2023). '
       'Datasets, Lizenz CC BY, corpora.uni-leipzig.de')

def part_spans(parts):
    out = []
    for i, (t, c) in enumerate(parts):
        if i: out.append(f'<span style="color: {GREY2}"> · </span>')
        out.append(f'<span style="color: {c}; font-weight: 600">{t}</span>')
    return ''.join(out)

W = 714
LEFTW, RIGHTW, GAP = 330, 356, 28
tipw = (W - 28) / 2

# Höhenbudget Seite 1
h = 40                                   # Rand oben
h += 16 + 6                              # Kicker
h += 52 + 4                              # Titel
sub1 = 'Die 216 häufigsten Vorsilben, Wortstämme und Nachsilben – gezählt in 44,7 Millionen Wörtern. Zusammengestellt von John Haas (2026) mit Claude Pro – Lizenz MIT – Version 1'
h += 23 * lines(sub1, W, 17) + 14
h += 22 * lines(LEAD, W, 15) + 18
how_h = 22 + 8 + 40 + 10 + sum(18 * lines(a + ': ' + b, RIGHTW - 14, 13) + 5 for a, b in HOW)
diag_h = 22 + 8 + 64 + 6 + 34 + 10 + 20
h += max(how_h, diag_h) + 16
h += 22 + 8 + 26 + len(EX) * 25 + 16           # Tabelle
tip_heights = [18.5 * lines(a + ' ' + b, tipw - 14, 13) + 6 for a, b in TIPS]
h += 22 + 8 + max(sum(tip_heights[:3]), sum(tip_heights[3:])) + 16
h += 18 + 16.5 * lines(METHOD, W, 12) + 6 + 16.5 * lines(SRC, W, 12)
h += 36                                  # Rand unten
print('Seite 1 Höhe ~', round(h), '| how', round(how_h), 'diag', diag_h, 'tips', [round(x) for x in tip_heights],
      'method lines', lines(METHOD, W, 12), 'src lines', lines(SRC, W, 12))

def p1():
    H = '{{accent}}'
    how = ''.join(f'<li style="margin: 0 0 5px 0"><b style="font-weight: 600; color: {INK}">{esc(a)}:</b> {esc(b)}</li>' for a, b in HOW)
    sample = (f'<div class="e" style="width: 224px; border-top: 1px solid {RULE}">'
              f'<div class="l1"><b style="color: {V}">kon-, kom-, kol-</b> (<i>lat.</i>) mit, zusammen</div>'
              f'<div class="l2"><span>Kontakt, Kombination</span>{dots(5, V)}</div></div>')
    rows = ''.join(
        f'<tr><td style="padding: 0 10px 0 0; height: 25px; border-bottom: 1px solid {RULE}; font-weight: 600">{w}</td>'
        f'<td style="padding: 0 10px 0 0; border-bottom: 1px solid {RULE}">{part_spans(pp)}</td>'
        f'<td style="padding: 0 10px 0 0; border-bottom: 1px solid {RULE}; color: {GREY}">{esc(lit)}</td>'
        f'<td style="padding: 0; border-bottom: 1px solid {RULE}">{esc(now)}</td></tr>'
        for w, pp, lit, now in EX)
    def tiplist(ts):
        return ''.join(f'<li style="margin: 0 0 6px 0"><b style="font-weight: 600; color: {INK}">{esc(a)}</b> {esc(b)}</li>' for a, b in ts)
    box = lambda t, c: (f'<div style="padding: 10px 16px; border-radius: 6px; background: {c}; color: #ffffff; '
                        f'font-family: \'Source Serif 4\', Georgia, serif; font-size: 30px; line-height: 44px; font-weight: 700">{t}</div>')
    lab = lambda a, b, c: (f'<div style="font-size: 12px; line-height: 16px; color: {GREY}"><b style="color: {c}; font-weight: 600">{a}</b><br>{b}</div>')
    hstyle = f'margin: 0; font-size: 16px; line-height: 22px; font-weight: 700; color: {INK}'
    body = f'''<div style="width: 794px; height: 1123px; box-sizing: border-box; padding: 40px 40px 36px 40px; display: flex; flex-direction: column; font-family: Inter, system-ui, sans-serif; color: {INK}; background: #ffffff">
<div style="font-size: 12px; line-height: 16px; letter-spacing: 0.08em; text-transform: uppercase; color: {GREY2}; font-weight: 600">Merkblatt · Seite 1 von 4</div>
<h1 style="margin: 6px 0 0 0; font-family: 'Source Serif 4', Georgia, serif; font-size: 46px; line-height: 52px; font-weight: 700; color: {H}">Fremdwörter knacken</h1>
<p style="margin: 4px 0 0 0; font-size: 17px; line-height: 23px; color: {GREY}">{esc(sub1)}</p>
<p style="margin: 14px 0 0 0; font-size: 15px; line-height: 22px">{esc(LEAD)}</p>
<div style="margin-top: 18px; display: flex; gap: {GAP}px; align-items: flex-start">
<div style="width: {LEFTW}px; flex: none">
<h2 style="{hstyle}">So ist ein Fremdwort gebaut</h2>
<div style="margin-top: 8px; display: flex; gap: 6px; align-items: flex-start">
<div style="display: flex; flex-direction: column; gap: 6px">{box('Kon', V)}{lab('Vorsilbe', 'zusammen', V)}</div>
<div style="display: flex; flex-direction: column; gap: 6px">{box('struk', S)}{lab('Wortstamm', 'bauen', S)}</div>
<div style="display: flex; flex-direction: column; gap: 6px">{box('tion', N)}{lab('Nachsilbe', 'Vorgang', N)}</div>
</div>
<p style="margin: 10px 0 0 0; font-size: 13.5px; line-height: 20px">Konstruktion = das Zusammen-Bauen</p>
</div>
<div style="width: {RIGHTW}px; flex: none">
<h2 style="{hstyle}">So liest du die Silben</h2>
<div style="margin-top: 8px; height: 40px; display: flex; align-items: flex-start">{sample}</div>
<ul style="margin: 10px 0 0 0; padding: 0 0 0 14px; font-size: 13px; line-height: 18px; color: {GREY}">{how}</ul>
</div>
</div>
<h2 style="{hstyle}; margin-top: 16px">Bausteine im Einsatz</h2>
<table style="margin-top: 8px; width: 100%; border-collapse: collapse; font-size: 13.5px; line-height: 18px">
<thead><tr style="text-align: left; color: {GREY2}; font-size: 12px">
<th style="padding: 0 10px 4px 0; height: 22px; border-bottom: 1.5px solid {INK}; font-weight: 600">Wort</th>
<th style="padding: 0 10px 4px 0; border-bottom: 1.5px solid {INK}; font-weight: 600"><span style="color: {V}">Vorsilbe</span> · <span style="color: {S}">Stamm</span> · <span style="color: {N}">Nachsilbe</span></th>
<th style="padding: 0 10px 4px 0; border-bottom: 1.5px solid {INK}; font-weight: 600">Wörtlich</th>
<th style="padding: 0 0 4px 0; border-bottom: 1.5px solid {INK}; font-weight: 600">Heute</th></tr></thead>
<tbody>{rows}</tbody>
</table>
<h2 style="{hstyle}; margin-top: 16px">Tipps zum Entschlüsseln</h2>
<div style="margin-top: 8px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: 28px; font-size: 13px; line-height: 18.5px; color: {GREY}">
<ul style="margin: 0; padding: 0 0 0 14px">{tiplist(TIPS[:3])}</ul>
<ul style="margin: 0; padding: 0 0 0 14px">{tiplist(TIPS[3:])}</ul>
</div>
<div style="margin-top: 16px; padding-top: 10px; border-top: 1px solid {RULE}; font-size: 12px; line-height: 16.5px; color: {GREY2}">
<div style="font-weight: 600; color: {INK}">Wie gezählt wurde</div>
<p style="margin: 2px 0 0 0">{esc(METHOD)}</p>
<p style="margin: 6px 0 0 0">{esc(SRC)}</p>
</div>
</div>
'''
    props = {"accent": {"editor": "color", "default": INK, "options": [INK, V, S, N]}, "$preview": {"width": 794, "height": 1123}}
    return head('Fremdwörter knacken – Anleitung') + body + tail(props)

open(f'{ROOT}/Main.dc.html', 'w', encoding='utf-8').write(p1())
canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": "2026-11-10T17:55:00Z"},
          "title": "Fremdwörter knacken – Merkblatt A4 (4 Seiten)", "launch": {"view": "canvas"}, "pages": [],
          "boards": {"Main.dc.html": {"x": 0, "y": 0, "w": 794, "h": 1123, "title": "Seite 1 – Anleitung"},
                     "Vorsilben.dc.html": {"x": 874, "y": 0, "w": 794, "h": 1123, "title": "Seite 2 – Vorsilben"},
                     "Wortstaemme.dc.html": {"x": 1748, "y": 0, "w": 794, "h": 1123, "title": "Seite 3 – Wortstämme"},
                     "Nachsilben.dc.html": {"x": 2622, "y": 0, "w": 794, "h": 1123, "title": "Seite 4 – Nachsilben"}},
          "order": ["Main.dc.html", "Vorsilben.dc.html", "Wortstaemme.dc.html", "Nachsilben.dc.html"],
          "notes": {}, "designSystems": []}
json.dump(canvas, open(f'{ROOT}/canvas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
