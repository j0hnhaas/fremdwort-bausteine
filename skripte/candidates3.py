# Version 3: Vierseiter. Baut auf candidates.py auf.
# Seiten: A = Vorsilben, K = Wortstämme, E = Nachsilben.
import candidates as base
from candidates import W, OR

C = []
def add(key, pos, inc, exc=None, noun=False, capex=None):
    C.append(dict(key=key, pos=pos, inc=inc, exc=exc, noun=noun, capex=capex))

DROP = {
    # Sammelzeilen, die getrennt werden
    "kilo-/milli-/zenti- (tausend/tausendstel/hundertstel)", "homo-/hetero- (gleich/verschieden)",
    "-ent / -enz", "-ant / -anz", "-ar / -är", "-eur / -euse", "-abel / -ibel", "-ium / -um / -us (lat. Endungen)",
    # Stämme, die als Endung auf die Nachsilben-Seite wandern
    "log (Wort, Lehre, Vernunft)", "graf / graph (schreiben)", "gramm (Geschriebenes)", "phon / fon (Laut, Stimme)",
    "skop (schauen)", "metr / meter (Maß)", "krat (Herrschaft)", "thek (Ablage)", "nom (Gesetz, Ordnung)",
    "path (Leiden, Gefühl)", "phob (Furcht)", "naut (Seefahrer)", "therap (pflegen, heilen)", "sphär (Kugel, Hülle)",
}
for c in base.C:
    if c["key"] in DROP:
        continue
    d = dict(c)
    if d["key"] == "pro- (vor, für)":
        d["exc"] = r"^(pro|pros)$|^proto|^protagon|^proton"
        d["inc"] = r"^pro(?!be|bier|st|sa$|zent|vin|tein|tz)|^provinz"
    C.append(d)

# ---------------- VORSILBEN: getrennt + neu ----------------
add("kilo- (tausend)", "A", r"^kilo")
add("milli- (Tausendstel)", "A", r"^milli(meter|liter|sekund|gramm|ampere|bar|volt|watt|mol|$)")
add("zenti- (Hundertstel)", "A", r"^zenti")
add("hekto- (hundert)", "A", r"^hekt(ar|o)", r"^hektor")
add("dezi-/deka- (zehn, Zehntel)", "A", r"^(dezi(bel|meter|liter|mal)|dekad|deka(?!nat|n))", r"^(dekarbon|dekadent|dekadenz)")
add("homo- (gleich)", "A", r"^homo(?!$|s$)")
add("hetero- (anders, verschieden)", "A", r"^hetero")
add("ambi- (beide, ringsum)", "A", r"^ambi(val|tion|tio|guit|ent)")
add("amphi- (beidseitig, ringsum)", "A", r"^amphi")
add("archi-/arch- (Haupt-, Ur-)", "A", r"^archi(tekt|pel|v)|^archäo")
add("bi- (zwei)", "A", r"^bi(lateral|lingu|när|nom|polar|sexuell|athlon|zeps|ennal|kultur|valent|gam|lanz|kameral|nokel|cycle$x)")
add("tri- (drei)", "A", r"^tri(athlon|o$|os$|ple|logie|kolore|angel|vial|mester|lateral|ennal|pel|plett|umvirat|nität|dent|cep)")
add("quadr-/quart- (vier)", "A", r"^(quadr|quart(al|ett|ier(?!s?$)))")
add("penta-/quint- (fünf)", "A", r"^(penta|quint(ett|essenz))", r"^pentax")
add("hexa-/sext- (sechs)", "A", r"^(hexa(gon|eder|meter)|sext(ett|ant))")
add("okta-/okt- (acht)", "A", r"^okt(a|av|ett|opus)", r"^(oktober|oktay)")
add("mega- / giga- / nano- (groß / riesig / winzig)", "A", r"^$x")  # Platzhalter, unten getrennt
add("giga- (riesig, Milliarde)", "A", r"^giga")
add("nano- (winzig, Milliardstel)", "A", r"^nano")
add("dys- (schlecht, gestört)", "A", r"^dys", r"^dyson")
add("endo- (innen)", "A", r"^endo(?!r)")
add("exo- (außen)", "A", r"^exo(t|gen|plan|skelett|therm|sphär)")
add("eu- (gut, wohl)", "A", r"^eu(phor|than|charist|phem|genik|kalyptus|nuch|logie)")
add("hemi- (halb)", "A", r"^hemi", r"^hemingway")
add("infra- (unterhalb)", "A", r"^infra", r"^infrage")
add("intra- (innerhalb)", "A", r"^intra(?!ns)")
add("intro- (hinein)", "A", r"^intro")
add("iso- (gleich)", "A", r"^iso(top|metr|bar|mer|therm|morph|gon)")
add("omni- (all, ganz)", "A", r"^omni")
add("proto- (erster, Ur-)", "A", r"^proto|^protagon|^proton")
add("quasi- (gleichsam, fast)", "A", r"^quasi")
add("supra- (oberhalb, über)", "A", r"^supra")
add("se- (beiseite, weg)", "A", r"^se(parat|parier|lekt|kret|gregat|zession|duktiv|kundär$x)")
C[:] = [c for c in C if not c["inc"] == r"^$x"]

# ---------------- NACHSILBEN: getrennt + neu ----------------
add("-ent (Person, Eigenschaft)", "E", r"[a-zäöü]{2}ent(e|en|er|es|em|in|innen|s)?$",
    OR(r"ment(e|en|er|es|s)?$", r"(prozent|prozente|prozenten|prozents)$", r"dient(e|en|est|et)?$", r"(event|events|talent|talente|talenten|talents)$",
       r"(rente|renten|trient|vincent|vincents|laurent|clement|sorrent)$", W("ente","enten","gent","gents","kent"), r"(stock|wild|bade|gummi|zeitungs)enten?$"))
add("-enz (Zustand, Eigenschaft)", "E", r"[a-zäöü]{2}enz(en)?$", OR(r"(grenz|grenzen|kredenz|kredenzen|florenz|konstanz)$", W("lenz")))
add("-ant (Person, Eigenschaft)", "E", r"[a-zäöü]{2}ant(e|en|er|es|em|in|innen|s)?$",
    OR(r"(tante|tanten|kante|kanten|plant|plante|planten|geplant|geplante|geplanten|geplanter|geplantes|geplantem|eingeplant|verplant)$", W("grant","rant","brant")))
add("-anz (Zustand)", "E", r"[a-zäöü]{2}anz(en)?$",
    OR(r"(?<!is)(?<!bs)(?<!ns)tanz(en)?$", r"(glanz|schwanz|kranz|pflanz|schanz|wanz|franz)(en)?$", W("ganz","ranzen"), r"schulranzen"))
add("-ar (Eigenschaft, Sache)", "E", r"[a-zäöü]{2}(ular|inar|entar|orar|itar|iar|plar|ntar|ikar|nar)(e|en|er|es|em|s|in|innen)?$")
add("-är (Eigenschaft, Person)", "E", r"[a-zäöü]{2}är(e|en|er|es|em|s|in|innen)?$",
    r"(bär|bären|sphäre|sphären|affäre|affären|klär|kläre|klären|erklären|aufklären)$")
add("-eur (Person)", "E", r"[a-zäöü]{2}eur(e|en|in|innen|s)?$", r"euro")
add("-euse (Person, weiblich)", "E", r"[a-zäöü]{2}euse(n)?$", r"schleuse")
add("-abel (möglich, -bar)", "E", r"[a-zäöü]{2}(abel|able|ablen|abler|ables|ablem)$",
    r"(gabel|gabeln|schnabel|kabel|säbel|fabel|nabel|isabel|mirabel|kabeln|kabels)$")
add("-ibel (möglich, -bar)", "E", r"[a-zäöü]{2}(ibel|ible|iblen|ibler|ibles|iblem)$", r"(bibel|fibel|giebel|zwiebel)$")
add("-um (lat. Nomen)", "E", r"[a-zäöü]{2}[^aeiouäöüi]um$",
    OR(r"(?<!da)(?<!quan)(?<!fak)(?<!vo)(?<!spek)(?<!sep)(?<!ul)tum$",
       r"(darum|warum|herum|rum|drum|ringsum|wiederum|rundum|reihum|andersrum|bochum|stumm|dumm)$", r"(?<!is)(?<!thm)(?<!m)mus$"))
add("-ium (lat. Nomen)", "E", r"[a-zäöü]{2}ium$")
add("-us (lat. Nomen)", "E", r"[a-zäöü]{2}[^aeiouäöü]us$",
    OR(r"ismus$", r"(markus|marcus|jesus|christus|franziskus|belarus|klaus|haus|maus|laus|graus|kraus|schmaus|aus|plus|minus|bus|cyprus|paulus|matthäus|petrus|augustus|julius|lucius|titus|brutus|cornelius|columbus|nikolaus|kurfürst$x)$"))
add("-isieren (-isierung)", "E", r"[a-zäöü]{2}(isieren|isiert|isierte|isierten|isiertes|isierter|isiertem|isierst|isierung|isierungen)$", capex=r"ieren$")
add("-em (griech. Ergebnis)", "E", r"(problem|system|theorem|emblem|ödem|lexem|morphem|phonem|diadem|extrem$x)(e|en|s|es)?$")
add("-ma (griech. Ergebnis)", "E", r"(thema|schema|drama|dilemma|trauma|klima|paradigma|stigma|dogma|prisma|komma|asthma|plasma|aroma|charisma|panorama|karma|magma|ödema$x)(s|ta|ten|men)?$|(themen|schemata|dramen|dilemmata|traumata|dogmen|prismen)$",
    r"(klimaanlage$x)")
add("-esk (in der Art von)", "E", r"[a-zäöü]{2}esk(e|en|er|es|em)?$", r"(desk|fresk)")
add("-oid (ähnlich)", "E", r"[a-zäöü]{2}oid(e|en|s)?$")
add("-esse (Eigenschaft)", "E", r"(finesse|delikatesse|raffinesse|noblesse|akkuratesse|politesse|hostess|baronesse|komtesse|stewardess)(n|en)?$")
add("-and (wer etwas erfährt)", "E", r"(doktor|prob|diplom|matur|konfirm|habilit|summ|multiplik|examin|ordin|informand$x)and(en|in|innen)?$")
add("-ose (Krankheit, Zustand)", "E",
    r"(hypnose|narkose|neurose|psychose|tuberkulose|thrombose|arthrose|sklerose|osmose|symbiose|metamorphose|dermatose|fibrose|nekrose|osteoporose|endometriose|skoliose|zirrhose|mykose|zyanose|glukose|laktose|fruktose|zellulose|stenose|borreliose|neurodermitis$x|apotheose|toxoplasmose|leptospirose)(n)?$")
add("-itis (Entzündung)", "E", r"[a-zäöü]{3}itis$", r"(graffitis|wapitis)")
add("-om (Geschwulst)", "E", r"(karzinom|melanom|myom|glaukom|lipom|sarkom|lymphom|adenom|fibrom|hämatom|angiom|gliom|blastom|meningeom)(e|en|s)?$")
add("-in (Wirkstoff)", "E", r"(protein|vitamin|insulin|koffein|nikotin|benzin|kerosin|adrenalin|penizillin|penicillin|serotonin|dopamin|melatonin|histamin|morphin|heroin|kokain|aspirin|chinin|keratin|kreatin|lanolin|glyzerin|glycerin|paraffin|vaselin|gelatine$x|testosteron$x)(e|en|s)?$")
add("-on (griech. Ding)", "E", r"(stadion|lexikon|elektron|proton|neutron|photon|hormon|ozon|polygon|pentagon|hexagon|pantheon|kanon|organon|phänomen$x)(s|en|e)?$|(stadien|lexika|hormone|elektronen|protonen|neutronen|photonen)$", r"(kanone|kanonen|zone|zonen)$")
add("-log (Rede, Wort)", "E", r"(dialog|katalog|monolog|prolog|epilog|analog|dekalog)(e|en|s|es)?$")
add("-logie (-logisch)", "E", r"(logie|logien|logisch|logische|logischen|logischer|logisches|logischem)$", r"^(logisch|logische|logischen|logischer|logisches|logischem|unlogisch)$")
add("-loge (Fachmann, Fachfrau)", "E", r"olog(e|en|in|innen)$", r"(monolog|dialog|katalog|prolog|epilog|analog)(e|en)$")
add("-graf/-graph (Schreiber, Gerät)", "E", r"(graf|graph|grafen|graphen|grafin|grafinnen)$",
    r"(^graf$|^grafen$|landgraf|markgraf|burggraf|pfalzgraf|reichsgraf|landgrafen|markgrafen|burggrafen|pfalzgrafen)")
add("-grafie/-graphie (-grafisch)", "E", r"(grafie|graphie|grafien|graphien|grafisch|graphisch|grafische|graphische|grafischen|graphischen|grafischer|graphischer|grafisches|graphisches)$",
    r"^(grafisch|graphisch|grafische|grafischen|grafischer|grafisches)$")
add("-gramm (Geschriebenes)", "E", r"gramm(e|en|s)?$", r"instagram")
add("-phon/-fon (Laut, Gerät)", "E", r"(phon|fon|phone|fone|phons|fons|phonen|fonen)$", r"(fond|alfons|montafon|vodafone|iphone|iphones)$")
add("-phonie/-fonie (Klang)", "E", r"(phonie|fonie|phonien|fonien|phonisch|fonisch|phonische|fonische)$")
add("-skop (Gerät zum Schauen)", "E", r"skop(e|en|s)?$")
add("-skopie (Untersuchung)", "E", r"skopie(n)?$|skopisch(e|en|er|es)?$")
add("-meter (Maß, Messgerät)", "E", r"(meter|metern|meters)$")
add("-metrie (Messung, -metrisch)", "E", r"(metrie|metrien|metrisch|metrische|metrischen|metrischer|metrisches)$")
add("-kratie (-kratisch)", "E", r"(kratie|kratien|kratisch|kratische|kratischen|kratischer|kratisches)$")
add("-krat (Herrschender)", "E", r"okrat(en|in|innen)?$", r"(sokrat|hippokrat)")
add("-thek (Sammlung, Ablage)", "E", r"thek(e|en|ar|are|aren|arin)?$")
add("-nom (Kundiger)", "E", r"(ökonom|astronom|gastronom|agronom|ergonom|taxonom|metronom)(e|en|in|innen|s)?$")
add("-nomie (-nomisch)", "E", r"(nomie|nomien|nomisch|nomische|nomischen|nomischer|nomisches)$")
add("-sophie (Weisheit)", "E", r"(sophie|sophisch|sophische|sophischen|sophischer|soph|sophen|sophin)$", r"^(sophie)$")
add("-therapie (Behandlung)", "E", r"(therapie|therapien|therapeut|therapeuten|therapeutin|therapeutinnen|therapeutisch|therapeutische|therapeutischen)$")
add("-pathie/-path (Leiden, Gefühl)", "E", r"(pathie|pathien|pathisch|pathische|pathischen|path|pathen)$", r"^(path)$")
add("-phob/-phobie (Furcht)", "E", r"(phob|phobe|phoben|phober|phobie|phobien|phobisch)$")
add("-phil/-philie (Vorliebe)", "E", r"(phil|phile|philen|philie)$", r"^(phil|phils)$|theophil|pamphil")
add("-naut (Fahrer)", "E", r"naut(en|in|innen)?$", r"(arnaut|juggernaut)")
add("-drom (Lauf, Bahn)", "E", r"drom(e|en|s)?$")
add("-zid (tötend)", "E", r"(pestizid|herbizid|insektizid|fungizid|suizid|genozid|femizid|biozid|homizid|rodentizid)(e|en|s|al|ale|alen)?$")
add("-gen (erzeugend)", "E", r"(homogen|heterogen|allergen|kollagen|pathogen|karzinogen|androgen|östrogen|antigen|fotogen|telegen|halogen|endogen|exogen|biogen|hypoallergen)(e|en|er|es|em)?$", r"kantig")

# --- Nachträge Nachsilben ---
add("-istik (Fachgebiet)", "E", r"[a-zäöü]{2}istik(en)?$")
add("-ator (Person, Gerät)", "E", r"[a-zäöü]{2}ator(en|in|innen|s)?$")
add("-elle (Verkleinerung)", "E", r"(tabelle|novelle|kapelle|bagatelle|libelle|sardelle|zitadelle|frikadelle|karamelle|querelle|organelle|morelle|flanelle|bordelle$x|frikadelle)(n)?$")
add("-lyse (Auflösung, Zerlegung)", "E", r"(lyse|lysen|lytisch|lytische|lytischen|lytischer|lytisches|lytik|lytiker|lytikerin|lytikern)$")
add("-these (Setzung, Annahme)", "E", r"(these|thesen|thetisch|thetische|thetischen)$", r"(ästhet|pathet)")
add("-gnose (Erkenntnis)", "E", r"(gnose|gnosen|gnostik|gnostisch|gnostische|gnostischen|gnostiziert|gnostizieren)$")
add("-sphäre (Kugel, Hülle, Bereich)", "E", r"sphär(e|en|isch|ische|ischen)$")
add("-archie (Herrschaft)", "E", r"(archie|archien|archisch|archische|archischen|archat|archen)$", r"^archie$|schnarch")
add("-iatrie (Heilkunde)", "E", r"(iatrie|iater|iaterin|iatern|iatrisch|iatrische|iatrischen)$")

# Stamm-Korrekturen
for c in C:
    if c["key"]=="tradi (übergeben)": c["inc"]=r"tradition|tradier"
    if c["key"]=="bio (Leben)": c["exc"]=r"(fabio|dubio)"
    if c["key"]=="lok (Ort)": c["exc"]=r"kilokal"
    if c["key"]=="duk / duz (führen)": c["exc"]=r"^duke"
    if c["key"]=="medi (Mitte)": c["exc"]=r"(medizin|medikament|medit|immediate)"
    if c["key"]=="gen (Ursprung, Erzeugung)": c["inc"]=c["inc"].replace("genre","^genre|-genre|genres$")
    if c["key"]=="-ine (-inen)": c["exc"]=c["exc"]+"|catherine"
