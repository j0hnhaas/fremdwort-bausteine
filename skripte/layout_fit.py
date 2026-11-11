import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json
from PIL import ImageFont
F='/usr/share/fonts/opentype/inter/'
reg=ImageFont.truetype(F+'Inter-Regular.otf',125); sb=ImageFont.truetype(F+'Inter-SemiBold.otf',125)
def w(font,txt,size): return font.getlength(txt)*size/125
OV={ # (label, meaning, examples) – kürzere Anzeigeformen
 ('A','kon-/kom-/kol-/kor-/ko- (mit, zusammen)'):('kon-, kom-','mit, zusammen',None),
 ('A','ad- (hinzu, an) inkl. ak-/ag-/as-/at-/ap-'):('ad-, ak-, at-','hinzu, an',None),
 ('A','archi-/arch- (Haupt-, Ur-)'):(None,'Haupt-, Ur-',None),
 ('A','ob-/op-/of-/ok- (entgegen)'):(None,'entgegen',None),
 ('A','pseudo- (falsch, schein-)'):(None,None,'Pseudonym'),
 ('K','organ (Werkzeug)'):(None,None,'Organisation, Organ'),
 ('K','leg / lekt (lesen, wählen)'):(None,'lesen, wählen',None),
 ('E','-ieren (-iert, -ierung)'):('-ieren, -ierung','Verb, Vorgang',None),
 ('E','-ion (-tion, -sion, -ation)'):('-ion, -tion','Vorgang, Ergebnis',None),
 ('E','-or (-oren, -orin)'):(None,'Person, Gerät',None),
 ('E','-isieren (-isierung)'):('-isieren',None,None),
 ('E','-ist (-isten, -istin)'):(None,'Person mit Beruf, Haltung',None),
 ('E','-ier (-iere)'):(None,'Person, Sache',None),
 ('E','-ium (lat. Nomen)'):(None,'lat. Nomen, oft Ort',None),
 ('E','-iker (-ikerin)'):(None,'Fachperson (zu -ik)',None),
 ('E','-gramm (Geschriebenes)'):(None,'Schrift, Gewicht',None),
 ('E','-ismus'):(None,'Lehre, Haltung',None),
 ('E','-grafie/-graphie (-grafisch)'):('-grafie','Beschreibung',None),
 ('E','-nomie (-nomisch)'):(None,'Gesetz, Lehre',None),
 ('E','-loge (Fachmann, Fachfrau)'):(None,'Fachperson',None),
 ('E','-graf/-graph (Schreiber, Gerät)'):('-graf, -graph','Schreiber, Gerät',None),
}
d=json.load(open('daten/zwischen/sheet_data.json'))
MAX=188; bad=[]
for p in 'AKE':
    for x in d[p]:
        o=OV.get((p,x['key']))
        if o:
            if o[0]: x['label']=o[0]
            if o[1]: x['bed']=o[1]
            if o[2]: x['bsp']=o[2]
        l1=w(sb,x['label'],12.5)+w(reg,' · '+x['bed'],12.5)
        l2=w(reg,x['bsp'],12)+(6+w(sb,x['herk'],10.5) if x['herk'] else 0)
        x['w1']=round(l1); x['w2']=round(l2)
        if l1>MAX or l2>MAX: bad.append((p,x['rang'],x['label'],x['bed'],round(l1),x['bsp'],round(l2)))
json.dump(d,open('daten/zwischen/sheet_data_fit.json','w'),ensure_ascii=False,indent=1)
print(bad); print('max w1',max(x['w1'] for p in 'AKE' for x in d[p]),'max w2',max(x['w2'] for p in 'AKE' for x in d[p]))
