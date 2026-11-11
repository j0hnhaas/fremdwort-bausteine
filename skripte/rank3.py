import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json, re, random, collections
import candidates3 as candidates
TOTAL = sum(json.load(open('daten/korpusgroessen.json')).values())
words=[]
for line in open('daten/zwischen/lex.tsv',encoding='utf-8'):
    w,a,b,c,s,cap=line.rstrip('\n').split('\t'); s=int(s)
    if s>=3: words.append((w,s,int(a),int(b),int(c),int(cap)))
words.sort(key=lambda x:-x[1])
END=['innen','in','en','em','er','es','e','n','s']
def lemma(w):
    w=w.replace('-','')
    for e in END:
        if w.endswith(e) and len(w)-len(e)>=4: return w[:-len(e)]
    return w
out=[]
for c in candidates.C:
    inc=re.compile(c['inc']); exc=re.compile(c['exc']) if c['exc'] else None
    m=[x for x in words if inc.search(x[0]) and not (exc and exc.search(x[0])) and (not c.get('noun') or x[5]>0.5*x[1]) and not (c.get('capex') and re.search(c['capex'],x[0]) and x[5]>0.5*x[1])]
    tok=sum(x[1] for x in m)
    per=[sum(x[i] for x in m)/1 for i in (2,3,4)]
    lem10=len({lemma(x[0]) for x in m if x[1]>=10})
    out.append(dict(key=c['key'],pos=c['pos'],tok=tok,pm=tok/TOTAL*1e6,lemmas=lem10,forms10=sum(1 for x in m if x[1]>=10),
                    per=per,top=[(x[0],x[1]) for x in m[:40]],tail=[x[0] for x in m if 3<=x[1]<100]))
json.dump(out,open('daten/zwischen/rank3.json','w'),ensure_ascii=False)
for p,name in (('A','VORSILBEN'),('E','NACHSILBEN'),('K','STÄMME')):
    print('==',name)
    for i,r in enumerate(sorted([r for r in out if r['pos']==p],key=lambda r:-r['pm']),1):
        sh=[round(v/sum(r['per'])*100) if sum(r['per']) else 0 for v in r['per']]
        print(f"{i:2d}. {r['key']:<48} {r['pm']:7.0f}/Mio  ~{r['lemmas']:4d} Wörter  news/wiki/at={sh}")
