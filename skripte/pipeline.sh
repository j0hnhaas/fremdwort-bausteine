#!/usr/bin/env bash
# Komplette Auswertung vom Rohkorpus bis zum Merkblatt. Aus dem Repo-Stammverzeichnis aufrufen.
set -euo pipefail
mkdir -p daten/zwischen design merkblatt
python3 skripte/build_lex.py      # Wortlisten zusammenführen -> daten/zwischen/lex.tsv
python3 skripte/rank3.py > daten/zwischen/rangliste.txt   # alle 251 Kandidaten zählen
python3 skripte/auswahl.py        # je Seite die 72 häufigsten
python3 skripte/build_data.py     # Beispielwörter prüfen, Punkte vergeben
python3 skripte/layout_fit.py     # Anzeigeformen kürzen (Stufe 1)
python3 skripte/layout_fit2.py    # Herkunft, alphabetisch, Zeilenbreiten prüfen
python3 skripte/gen_design.py     # Seiten für die Claude-Design-Arbeitsfläche -> design/
python3 skripte/gen_html.py design index.html
sed -i "s/'Source Serif 4', Georgia, serif/'Source Serif 4', Lora, Georgia, serif/g" index.html
google-chrome --headless=new --no-sandbox --no-pdf-header-footer --print-to-pdf=merkblatt/fremdwort-bausteine.pdf "file://$PWD/index.html"
