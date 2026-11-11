import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json, unicodedata
from PIL import ImageFont
from herkunft import HA, HE
F='/usr/share/fonts/opentype/inter/'
REG=ImageFont.truetype(F+'Inter-Regular.otf',125); SB=ImageFont.truetype(F+'Inter-SemiBold.otf',125); IT=ImageFont.truetype(F+'Inter-Italic.otf',125)
def w(font,t,s): return font.getlength(t)*s/125
d=json.load(open('daten/zwischen/sheet_data_fit.json'))
for x in d['A']: x['herk']=HA[x['key']]
for x in d['E']: x['herk']=HE[x['key']]
assert all(x['herk'] for p in 'AKE' for x in d[p])
OV={('A','deka-, dezi-'):(None,'zehn'),('A','hetero-'):(None,'anders'),('K','gen'):(None,'Ursprung'),
 ('E','-gen'):(None,'erzeugend'),('E','-graf, -graph'):(None,'Schreiber'),('E','-iatrie, -iater'):(None,'Heilkunde'),
 ('E','-ie'):(None,'Fach, Zustand'),('E','-ieren, -ierung'):(None,'Tätigkeit'),('E','-ist'):(None,'Person, Anhänger'),
 ('E','-pathie, -path'):('-pathie',None),('E','-phon, -fon'):(None,'Laut, Gerät'),('E','-sphäre'):(None,'Hülle, Bereich'),('A','ad-, ak-, at-'):('ad-, ak-, al-, at-',None),('E','-age'):(None,'Tätigkeit, Ort'),('E','-eur'):(None,'Person'),('E','-ium'):(None,'Nomen, oft Ort'),('E','-um'):(None,'Nomen'),('E','-us'):(None,'Nomen')}
for p in 'AKE':
    for x in d[p]:
        o=OV.get((p,x['label']))
        if o:
            if o[0]: x['label']=o[0]
            if o[1]: x['bed']=o[1]
def skey(lbl):
    s=lbl.split(',')[0].strip().lstrip('-').lower()
    s=s.replace('ä','a').replace('ö','o').replace('ü','u').replace('ß','ss')
    return ''.join(ch for ch in s if ch.isalpha())
COLW=224.67; MAX1=COLW-6; MAX2=COLW-26-8-6
bad=[]
for p in 'AKE':
    d[p].sort(key=lambda x:(skey(x['label']), x['label'], x['bed']))
    for x in d[p]:
        l1=w(SB,x['label'],12.5)+w(REG,' (',12.5)+w(IT,x['herk'],12.5)+w(REG,') '+x['bed'],12.5)
        l2=w(REG,x['bsp'],12)
        x['w1']=round(l1); x['w2']=round(l2)
        if l1>MAX1 or l2>MAX2: bad.append((p,x['label'],x['herk'],x['bed'],x['w1'],x['bsp'],x['w2']))
json.dump(d,open('daten/merkblatt-eintraege.json','w'),ensure_ascii=False,indent=1)
print('MAX1',round(MAX1),'MAX2',round(MAX2)); print(*bad,sep='\n'); print(len(bad))
print([x['label'] for x in d['A']][:12]); print([x['label'] for x in d['E']][:14])
