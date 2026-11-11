import re, sys, collections, json
files = {
 'news2024': 'daten/roh/deu_news_2024_1M-words.txt',
 'wiki2021': 'daten/roh/deu_wikipedia_2021_1M-words.txt',
 'atweb2023': 'daten/roh/deu-at_web_2023_1M-words.txt',
}
alpha = re.compile(r"^[a-zäöüß]+(?:-[a-zäöüß]+)*$")
lex = collections.defaultdict(lambda: [0,0,0])
cap = collections.Counter()  # capitalized count (to tell nouns)
totals = {}
for i,(k,p) in enumerate(files.items()):
    tot = 0
    with open(p, encoding='utf-8', errors='replace') as fh:
        for line in fh:
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 3: continue
            w, f = parts[1], int(parts[2])
            lw = w.lower()
            if not alpha.match(lw): continue
            tot += f
            lex[lw][i] += f
            if w[:1].isupper(): cap[lw] += f
    totals[k] = tot
print(totals, sum(totals.values()))
with open('daten/zwischen/lex.tsv','w',encoding='utf-8') as out:
    for w,(a,b,c) in lex.items():
        s=a+b+c
        out.write(f"{w}\t{a}\t{b}\t{c}\t{s}\t{cap[w]}\n")
json.dump(totals, open('daten/korpusgroessen.json','w'))
print(len(lex))
