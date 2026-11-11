import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import re, json, importlib
import candidates3 as cand, entries
importlib.reload(entries)
lex={}; cap={}
for line in open('daten/zwischen/lex.tsv',encoding='utf-8'):
    w,a,b,c,s,cp=line.rstrip('\n').split('\t'); lex[w]=int(s); cap[w]=int(cp)
C={c['key']:c for c in cand.C}
r={x['key']:x for x in json.load(open('daten/zwischen/rank3.json'))}
sel=json.load(open('daten/zwischen/auswahl.json'))
def dots(pm):
    return 5 if pm>=1000 else 4 if pm>=300 else 3 if pm>=100 else 2 if pm>=30 else 1
out={}; problems=[]
for p,E in (('A',entries.A),('K',entries.K),('E',entries.E)):
    miss=set(sel[p])-set(E); extra=set(E)-set(sel[p])
    if miss or extra: problems.append((p,'fehlend',miss,'zuviel',extra))
    rows=[]
    for i,k in enumerate(sel[p],1):
        if k not in E: continue
        t=E[k]; c=C[k]
        inc=re.compile(c['inc']); exc=re.compile(c['exc']) if c['exc'] else None
        for w in t[2].split(', '):
            lw=w.lower()
            ok= lw in lex and inc.search(lw) and not (exc and exc.search(lw))
            if not ok: problems.append((k,w,lex.get(lw)))
        rows.append(dict(rang=i,label=t[0],bed=t[1],bsp=t[2],herk=(t[3] if len(t)>3 else ''),pm=round(r[k]['pm'],1),dots=dots(r[k]['pm']),key=k))
    out[p]=rows
json.dump(out,open('daten/zwischen/sheet_data.json','w'),ensure_ascii=False,indent=1)
print('Probleme:',problems)
print({p:len(v) for p,v in out.items()})
