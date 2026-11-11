# Fremdwörter knacken – die häufigsten Fremdwort-Bausteine

Ein Merkblatt mit den **216 häufigsten Vorsilben, Wortstämmen und Nachsilben** deutscher Fremdwörter, gezählt in 44,7 Millionen Wörtern heutiger Texte. Jedes 20. Wort in den untersuchten Texten enthält mindestens einen der häufigsten Bausteine.

- **Merkblatt ansehen:** https://j0hnhaas.github.io/fremdwort-bausteine/
- **PDF (A4, 4 Seiten):** [`merkblatt/fremdwort-bausteine.pdf`](merkblatt/fremdwort-bausteine.pdf)
- **Vollständige Rangliste aller 251 geprüften Bausteine:** [`daten/rangliste.csv`](daten/rangliste.csv)

Zusammengestellt von John Haas (2026) mit Claude Pro. Version 1.

## Aufbau des Merkblatts

| Seite | Inhalt |
|---|---|
| 1 | Anleitung: Aufbau eines Fremdworts, Lesehilfe, zerlegte Beispielwörter, Tipps, Methode, Quellen |
| 2 | 72 Vorsilben (am Wortanfang) |
| 3 | 72 Wortstämme (Kern der Bedeutung) |
| 4 | 72 Nachsilben (am Wortende) |

Jeder Eintrag zeigt den Baustein, in Klammern die Herkunftssprache (*lat.*, *griech.*, *franz.*), die Ursprungsbedeutung, zwei Beispielwörter und die Häufigkeit als fünf Punkte. Die Einträge sind alphabetisch geordnet wie in einem Lexikon.

| Punkte | Vorkommen je 1 Million Wörter |
|---|---|
| ●●●●● | 1.000 und mehr |
| ●●●● | 300–999 |
| ●●● | 100–299 |
| ●● | 30–99 |
| ● | unter 30 |

## Methode

1. **Daten:** drei Textsammlungen der [Leipzig Corpora Collection](https://wortschatz.uni-leipzig.de/en/download/deu) mit je 1 Million Sätzen: Nachrichten 2024, deutsche Wikipedia 2021, österreichische Webseiten 2023. Zusammen 44,7 Millionen Wörter. Verwendet werden nur die Wortlisten mit Häufigkeiten (`*-words.txt`).
2. **Kandidaten:** 251 mögliche Bausteine (82 Vorsilben, 88 Stämme, 81 Nachsilben), jeweils als regulärer Ausdruck mit Ausschlussliste (`skripte/candidates.py`, `skripte/candidates3.py`).
3. **Zählung:** Vorsilben zählen nur am Wortanfang, Nachsilben nur am Wortende (mit Flexionsendungen), Stämme an jeder Stelle. Maß ist die Zahl der Vorkommen je 1 Million Wörter. Ein Wort zählt für jeden Baustein, den es enthält.
4. **Bereinigung:** Gleich lautende deutsche Wörter, Namen und Marken sind ausgeschlossen (etwa *konnte* bei kon-, *Antilope* bei anti-, *Schaden* bei -ade). Die häufigsten Treffer jedes Bausteins wurden von Hand geprüft, seltene in Stichproben.
5. **Auswahl:** je Seite die 72 häufigsten. Jeder Baustein steht nur auf einer Seite, und zwar dort, wo er meistens vorkommt (-logie bei den Nachsilben, bio bei den Stämmen).
6. **Prüfung:** Alle 216 Beispielwörter sind automatisch gegen Korpus und Zählregel geprüft. Die Ranglisten sind in allen drei Textsorten fast gleich (Rangkorrelation 0,91 bis 0,98).

**Grenzen:** Die Werte sind Näherungen. Vorsilben im Inneren von Zusammensetzungen (Bundes-präsident) werden nicht erfasst. Herkunft und Bedeutung sind vereinfacht und geben die Ursprungsbedeutung an. Bedeutungsangaben und Beispielauswahl sind eigene Formulierungen; ein Wörterbuch wurde nicht verwendet.

## Selbst nachrechnen

Voraussetzungen: Python 3 mit Pillow, die Schrift Inter (für die Zeilenbreiten) und Google Chrome (nur für das PDF).

```bash
# 1. Korpora von https://wortschatz.uni-leipzig.de/en/download/deu laden:
#    deu_news_2024_1M, deu_wikipedia_2021_1M, deu-at_web_2023_1M
# 2. Nur die Wortlisten entpacken und nach daten/roh/ legen:
mkdir -p daten/roh
for f in deu_news_2024_1M deu_wikipedia_2021_1M deu-at_web_2023_1M; do
  tar -xzf "$f.tar.gz" --strip-components=1 -C daten/roh "$f/$f-words.txt"
done
# 3. Alles neu berechnen (ca. 1 Minute):
bash skripte/pipeline.sh
```

Die Pipeline erzeugt die Dateien in `daten/`, `design/`, `index.html` und `merkblatt/` neu; das Ergebnis ist byte-gleich mit dem Stand im Repo.

## Inhalt des Repos

| Pfad | Inhalt |
|---|---|
| `index.html` | Merkblatt als Webseite (GitHub Pages), druckbar auf A4 |
| `merkblatt/` | Merkblatt als PDF |
| `daten/rangliste.csv` | alle 251 Bausteine mit Häufigkeit, Treffern je Textsorte, häufigsten Wortformen und den Texten des Merkblatts |
| `daten/merkblatt-eintraege.json` | die 216 Einträge des Merkblatts |
| `daten/korpusgroessen.json` | Wortzahl je Textsammlung |
| `skripte/` | Zählung, Auswahl, Prüfung und Satz |
| `design/` | Quelldateien der vier Seiten für Claude Design |

## Quellen und Lizenz

Daten: Leipzig Corpora Collection (2024): German news corpus based on material from 2024; (2021): German Wikipedia corpus based on material from 2021; (2023): German (Austria) web corpus based on material from 2023. Leipzig Corpora Collection. Dataset. Lizenz [CC BY](https://wortschatz.uni-leipzig.de/en/usage). Zitierweise: D. Goldhahn, T. Eckart, U. Quasthoff: *Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages.* LREC 2012.

Dieses Repo steht unter der MIT-Lizenz, siehe [`LICENSE`](LICENSE).
