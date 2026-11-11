# Wählt je Seite die 72 häufigsten Bausteine aus.
import json
r = json.load(open('daten/zwischen/rank3.json', encoding='utf-8'))
sel = {p: [x['key'] for x in sorted([x for x in r if x['pos'] == p], key=lambda x: -x['pm'])[:72]] for p in 'AKE'}
json.dump(sel, open('daten/zwischen/auswahl.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
