# Baut aus den vier Canvas-Seiten eine eigenständige, druckbare HTML-Datei (A4, 4 Seiten).
import re, json, sys, os
SRC = sys.argv[1] if len(sys.argv) > 1 else 'design/project'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'index.html'
PAGES = ['Main', 'Vorsilben', 'Wortstaemme', 'Nachsilben']
css = None; secs = []
for p in PAGES:
    s = open(f'{SRC}/{p}.dc.html', encoding='utf-8').read()
    props = json.loads(re.search(r"data-props='(.*?)'", s, re.S).group(1))
    acc = props['accent']['default']
    helmet = re.search(r'<helmet>(.*?)</helmet>', s, re.S).group(1)
    if css is None:
        css = re.search(r'<style>(.*?)</style>', helmet, re.S).group(1)
    body = re.search(r'</helmet>(.*?)</x-dc>', s, re.S).group(1).strip()
    body = body.replace('{{accent}}', acc)
    secs.append(f'<section class="page" aria-label="Seite {len(secs)+1}">\n{body}\n</section>')
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,500;0,600;0,700;1,400&amp;family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&amp;display=swap" rel="stylesheet">')
zoom = '\n'.join(f'@media (max-width: {w}px) {{ .page {{ zoom: {z}; }} }}' for w, z in
                 [(840, .9), (760, .82), (680, .74), (600, .66), (530, .58), (460, .5), (400, .44)])
html = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fremdwörter knacken – Die häufigsten Vorsilben, Wortstämme und Nachsilben</title>
<meta name="description" content="Merkblatt mit den 216 häufigsten Vorsilben, Wortstämmen und Nachsilben deutscher Fremdwörter, gezählt in 44,7 Millionen Wörtern.">
{FONTS}
<style>
{css.strip()}
html{{background:#EFEAE4}}
body{{font-family:Inter,system-ui,sans-serif;color:#1B1B1B}}
h1,h2{{font-family:inherit}}
.page h1{{font-family:'Source Serif 4',Lora,Georgia,serif}}
.bar{{max-width:794px;margin:0 auto;padding:20px 12px 4px 12px;display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center;font-size:14px;line-height:20px}}
.bar strong{{font-size:15px;margin-right:auto}}
.bar a{{color:#9B2F58;font-weight:600}}
.page{{width:794px;height:1123px;margin:16px auto 28px auto;background:#ffffff;box-shadow:0 1px 3px rgba(0,0,0,.12),0 8px 24px rgba(0,0,0,.08);overflow:hidden}}
.note{{max-width:794px;margin:0 auto 40px auto;padding:0 12px;font-size:13px;line-height:19px;color:#555555}}
{zoom}
@page{{size:A4;margin:0}}
@media print{{
  html,body{{background:#ffffff}}
  .bar,.note{{display:none}}
  .page{{zoom:1;margin:0;box-shadow:none;width:210mm;height:297mm;break-after:page}}
  .page:last-of-type{{break-after:auto}}
}}
</style>
</head>
<body>
<nav class="bar" aria-label="Downloads">
<strong>Fremdwörter knacken</strong>
<a href="merkblatt/fremdwort-bausteine.pdf">PDF herunterladen</a>
<a href="daten/rangliste.csv">Rangliste (CSV)</a>
<a href="https://github.com/j0hnhaas/fremdwort-bausteine">Quellcode und Methode</a>
</nav>
{chr(10).join(secs)}
<p class="note">Zum Ausdrucken: Strg+P bzw. Cmd+P, Papierformat A4, Ränder „Keine“, Hintergrundgrafiken an.</p>
</body>
</html>
'''
open(OUT, 'w', encoding='utf-8').write(html)
print(OUT, len(html))
