# Kandidaten für Fremdwort-Bausteine (Version 2).
# pos: A = Vorsilbe (Wortanfang), E = Nachsilbe (Wortende), K = Wortstamm (überall im Wort)
# inc: Regex, die passen muss (auf kleingeschriebene Wortform)
# exc: Regex für Fehltreffer (heimische Wörter, Namen, Marken, andere Herkunft)

C = []
def add(key, pos, inc, exc=None, noun=False, capex=None):
    C.append(dict(key=key, pos=pos, inc=inc, exc=exc, noun=noun, capex=capex))

def W(*ws):
    """Ganze Wörter ausschließen."""
    return r"^(" + "|".join(ws) + r")$"

def OR(*rs):
    return "|".join(f"(?:{r})" for r in rs if r)

# =============== VORSILBEN (Wortanfang) ===============
add("a-/an- (nicht, ohne)", "A",
    r"^(a(sozial|typisch|politisch|symmetr|morph|theis|pathi|synchron|tonal|sexuell|biotisch|moralisch|historisch|rhythm|lkoholfrei$x)|an(archi|omal|alphabet|organisch|onym|ämie|ästhes|aerob|algeti))")
add("ab-/abs- (weg)", "A", r"^ab(norm|solut|solv|strakt|surd|senz|sent|stinen|sorb|szess|lativ|itur|duktion|errat|rupt)")
add("ad- (hinzu, an) inkl. ak-/ag-/as-/at-/ap-", "A",
    r"^(ad(apt|äqu|ministr|vent|verb|vokat|resse|ressier|optier|ditiv|dition|jektiv|jutant|ressat)|ak(zept|zent|kumul|kurat|kreditier|klimat|kord|komod|kusativ|quisit|tiv(?!ität)$x)|ag(gress|glomer)|as(sist|sozi|similier|pekt|piration|sortiment|serv|ketisch$x)|at(trakt|test|tent|tack|mosph$x)|ap(pell|plaus|plik|parat|petit|probier|propri|port$x)|an(nonc|nulli|nekt|nex)|ar(rangier|rogan)|al(lianz|lokat|lusion|literation))")
add("ana- (auf, wieder)", "A", r"^ana(lys|log|tom|chron|mnes|phor|gramm|bolik)")
add("anti- (gegen)", "A", r"^anti(?!k|q|lop|ll|mon|past|ope|gon|och|bes|gua|zip|lles)")
add("apo- (weg, ab)", "A", r"^apo(thek|stel|kalyp|log|stroph|plekt)")
add("auto- (selbst)", "A", r"^auto(mat|mobil|nom|gramm|biogra|krat|didakt|immun|pilot|sugges|typ|zensur|korrektur|fokus|chthon|ark|motive)")
add("de-/des- (weg, ent-)", "A",
    r"^de(aktiv|motiv|zentral|form|fekt|fizit|finit|finier|klar|klin|kret|legat|legier|mont|mask|mobil|moral|nunz|portier|portat|press|riv|sinf|sillus|sorient|stabil|struk|tekt|valv|generi|hydr|regul|kompos|koloni|eskal|kodier|pon|duk|duz|kaden|signi|vot|kontamin|fens|termin|lir|tail|batt|büt|sign|vis|montier|zimier|ser|pot|klamat|lik|kret)",
    r"^de(korum|potenz|sert$|serteur$x)")
add("dia- (durch)", "A", r"^dia(gno|log|gramm|lekt|lyse|lys|bet|spora|gon|phragma|chron|lys|lekt)")
add("dis-/di- (auseinander)", "A",
    r"^dis(kus|kurs|kret|tanz|qualif|kriminier|harmon|po[sn]|sonanz|sens|krepanz|tribu|put|play|kont|kredit|tinkt|parat|lozier|sertation|soziat|proportion|junk|zip(?!lin))|^di(vers|gest|vergen|lemma$x)")
add("epi- (auf, darüber)", "A", r"^epi(dem|sod|log|zent|gramm|gon|phan|gene|kur|lepsie|sk|thel)|^epoche")
add("ex-/e- (aus, heraus)", "A",
    r"^ex(?!cel|cl|ch|tra)|^e(mis|migr|limin|valu|vak|manzip|ruption|lekt(?!r)|vident|volution|vozier|motion|motional|xzess|ffekt|ffizien|ffiz|rupt|dukat|dition|xot)",
    r"^ex$")
add("extra- (außerhalb, besonders)", "A", r"^extra(?!kt|h)")
add("hyper- (über, übermäßig)", "A", r"^hyper(?!ion)")
add("hypo- (unter)", "A", r"^hypo(?!$|-)")
add("in-/im-/il-/ir- (nicht)", "A",
    r"^(in(akzept|aktiv|ad[äa]qu|kompet|kompat|konsequ|konsist|korrekt|stabil|toler|transpar|dir|diskret|diskutabel|effizient|flexib|formell|human|kohärent|kongruent|existent|offiziell|operabel|valid|different|dignat|konsistent|kognito|transitiv|transparen)|im(mobil|materiell|moral|perfekt|plausib|potent|präzis|pertin|possib|mun|patient|mens)|il(legal|legitim|liberal|loyal|logisch|lusion|lusor)|ir(rational|regul|relevant|reversib|real|reparab|reführ$x))")
add("in-/im- (hinein)", "A",
    r"^(in(form|fekt|flat|du[ks]|dustr|stitu|stru|vest|teg|tens|spi|spek|stall|stan[tz]|klu|jekt|itiat|nov|put|ser[ai]t|sist|skri|stinkt|halat|zid|dikat|diz|frastr|vas|kub|kasso|sekt|vent|vit|volv|tim|tuit|tention|spir|zest|kassi)(?<!integ)|im(port|puls|plant|pli|press|provis|migr|pos|ponier|ag(?!e)))")
add("inter- (zwischen)", "A", r"^inter(?!n(?!a|et))")
add("kata-/kat- (herab, gemäß)", "A", r"^kat(astroph|alog|egor|alys|arakt|akomb|apult|heder)")
add("kon-/kom-/kol-/kor-/ko- (mit, zusammen)", "A",
    r"^(kon(?!d(itor)|ig|to(?!r)|nt|nnt)|kom(?!m(?!is|un|en|od|erz|a|it))|kol(lab|leg|lekt|lision|lo[nq]|labor)|kor(re[ksl]|resp|rup|rel)|ko(operat|ordin|existen|autor|alition|härent))",
    r"^(konto|kontos|kontor|kongo|kondom|konrad|könig|kommen|komm$|kommst|kommt|komme|kommend|komisch|kompass|konnte|konnten|konntest)|^konn|^kontroll")
add("kontra-/konter- (gegen)", "A", r"^kontra|^konter|^kontro(vers|ll)")
add("meta- (nach, über, verändert)", "A", r"^meta(?!ll|l|s?$|-)")
add("multi- (viel)", "A", r"^multi")
add("poly- (viel)", "A", r"^poly")
add("mono- (allein, ein)", "A", r"^mono")
add("mega- (groß)", "A", r"^mega(?!n|tron)")
add("mikro- (klein)", "A", r"^mikro")
add("makro- (groß)", "A", r"^makro(?!n)")
add("mini- (klein)", "A", r"^mini(?!ng|str|chm|ster|m)")
add("neo- (neu)", "A", r"^neo(?!s|m$)")
add("ob-/op-/of-/ok- (entgegen)", "A", r"^(ob(jekt|serv|lig|szön|struk|skur|session|stin|tus)|op(pos|ponent|portun)|of(fensiv)|ok(kup|kasion))")
add("pan- (all, ganz)", "A", r"^pan(orama|demi|theon|optik|europ|arab|slaw)")
add("para- (neben, gegen)", "A", r"^para(?!d|t$|mount|celsus|guay|ll$x)|^parallel",
    r"^(parat|para|parade|paraden|paradies)$")
add("per- (durch)", "A", r"^per(fekt|form|man|spekt|vers|zep|kussion|sist|missi|plex|fid|tinent|forier)")
add("peri- (um, herum)", "A", r"^peri(od|pher|meter|skop|naeal$x|kard|ton|stalt|dural)")
add("post- (nach)", "A", r"^post(hum|um$|modern|produkt|traumat|operat|sowjet|faktisch|kolonial|doc|doktor|graduier|natal|partum|pandem|skript|industriell|fossil|punk|rock|kommunist|feminis|strukturalis)")
add("prä- (vor)", "A", r"^prä(?!ch|g)")
add("pro- (vor, für)", "A", r"^pro(?!be|bier|st|sa$|sa |zent|vin|tein|to(?!kol)|tz)|^provinz",
    r"^(pro|pros)$")
add("pseudo- (falsch, schein-)", "A", r"^pseudo")
add("re- (zurück, wieder)", "A",
    r"^re(?=(akt|form|port|stau|volu|zept|kord|serv|son|spek|sult|sort|ssour|fer|flex|krut|levan|pertoi|präsent|produ|siden|signa|zens|zess|duk|duz|lat|klam|bell|cherch|naiss|strik|vis|vue|cycl|habil|integr|konstru|organ|novi|pariert|parat|kapitul|kultiv|aktivi|stitu|tour|vanche|kompen|kreat|plik|petit|kurs|spond|pressi|prise|mis|fug|frain|spir|sist|tusch|sign|cyc|trospek|mak|monstr|lax|ze[nps]|kru))")
add("retro- (zurück)", "A", r"^retro")
add("semi- (halb)", "A", r"^semi(final|profess|kondukt|condu|kolon|otik|transpar|automat|arid|-)")
add("sub- (unter)", "A", r"^sub(?!aru|s?$)")
add("super- (über)", "A", r"^super(?!man)")
add("syn-/sym- (zusammen)", "A", r"^sy(n|m)(?!n?$)")
add("tele- (fern)", "A", r"^tele")
add("trans- (hinüber)", "A", r"^trans")
add("ultra- (jenseits, äußerst)", "A", r"^ultra(?!man)")
add("uni- (eins)", "A", r"^uni(form|kat|lateral|sex|versal|versell|versum|on|son|kum|t[ey]?$|ted)", r"^(unicef|unix)$")
add("vize- (anstelle)", "A", r"^vize")
add("homo-/hetero- (gleich/verschieden)", "A", r"^(homo(?!$|s$)|hetero)")
add("kilo-/milli-/zenti- (tausend/tausendstel/hundertstel)", "A", r"^(kilo|milli(?!on|ard|e$)|zenti)")

# =============== NACHSILBEN (Wortende) ===============
LAND = r"(spanien|italien|(?<!fant)asien|australien|belgien|bulgarien|kroatien|serbien|slowenien|rumänien|albanien|armenien|georgien|indien|indonesien|kolumbien|bolivien|syrien|libyen|tunesien|algerien|kalifornien|sizilien|sardinien|mazedonien|bosnien|britannien|skandinavien|katalonien|andalusien|kastilien|brasilien|arabien|mesopotamien|sibirien|äthiopien|mauretanien|venezien|apulien|kalabrien|ligurien|umbrien|kantabrien|asturien|galicien|galizien|slawonien|dalmatien|istrien|tasmanien|polynesien|patagonien|kampanien|tschetschenien|lettland$x|lombardei$x|pommern$x|tansanien|kenien$x|liberien|nigerien$x|ostindien|westindien|kleinasien|ostasien|zentralasien|südostasien|vorderasien|mikronesien|melanesien|abessinien|anatolien|kilikien|lykien|phrygien|thessalien|mazedonien|makedonien|kappadokien|karthagien$x|lusitanien|numidien|gallien|germanien|hispanien|rätien|pannonien|dakien|thrakien|illyrien|samarien|judäa$x|korinthien$x|zilizien|julien)$"
add("-ion (-tion, -sion, -ation)", "E", r"ion(en|s)?$",
    OR(r"^(ion|ionen)$", r"(million|millionen|millions|pavillon|champion|champions|skorpion)$", W("lion","lions")))
add("-ität (-tät)", "E", r"ität(en)?$")
add("-ismus", "E", r"(ismus|ismen)$", r"^(rhythm|rheumat)")
add("-ist (-isten, -istin)", "E", r"[a-zäöü]{3}ist(en|in|innen)?$",
    OR(r"(?<!ath)eist(en|in|innen)?$", r"(?<!a)(?<!y)listen$", r"(kisten|pisten|fristen|frist)$", r"christ(en|in|innen)?$", W("nisten", "zwisten", "misten", "gerüst$x")))
add("-ie (-ien)", "E", r"[a-zäöü]{2}ie(n)?$",
    OR(LAND, r"ei(e|en)$", r"(schien|schienen|spien|schrien|erschien|beschien|knie|knien)$", r"(medien|materialien|mineralien|fossilien|utensilien|reptilien|insignien|personalien|naturalien|immobilien$x)$", W("sowie", "wie", "sie", "die", "nie")))
add("-ik", "E", r"[a-zäöü]{2}ik(en|s)?$", OR(r"(blick|klick|eik|eiks|eiken|risiken|dominik|henrik|patrik|fredrik|ulrik|heinrik)$", W("antik","antiken","antike","erik")))
add("-iker (-ikerin)", "E", r"[a-zäöü]{2}iker(in|innen|n|s)?$")
add("-ieren (-iert, -ierung)", "E",
    r"[a-zäöü]{2}(ieren|iert|ierte|ierten|iertes|ierter|iertem|ierst|ierung|ierungen)$",
    OR(r"eier(t|te|ten|tes|ter|tem|ung|ungen)?$", r"(frieren|friert|gefriert|verlieren|verliert|schmieren|schmiert|gieren|giert)$",
       r"(^|ver|ge|aus)zier(en|t|te|ten|tes|ter|tem|ung)$",
       W("tieren","bieren","stieren","nieren","vieren")), capex=r"ieren$")

add("-iv", "E", r"[a-zäöü]{2}iv(e|en|er|es|em|s)?$", r"(olive|oliven|oliver|archiv|archive|archiven|archivs|ziv$x)$")
add("-ell (-iell, -uell)", "E",
    r"(iell|uell|onell|inell|rell|mell|modell|kartell|bordell|pastell|kastell|karussell|aquarell|appell)(e|en|er|es|em|s)?$",
    r"(grell|grelle|grellen|greller)$|quell")
add("-al (-ial, -ual)", "E",
    r"[a-zäöü]{2}(ial|ual|nal|ral|kal|gal|dal|val|bal|pal|ental|ital|otal|utal|ontal|ormal|imal|ermal|xal|zal|tal)(e|en|er|es|em|s)?$",
    OR(r"(saal|qual|quale|qualen|wal|schal|schale|schalen|aal)$", r"(?<!or)(?<!im)(?<!erm)mal(e|en|s)?$", W("regal","regale","regalen"),
       r"(?<!en)(?<!i)(?<!o)(?<!u)(?<!on)tal(e|en|er|es|em|s)?$",
       r"portugal", W("ural")))
add("-ant / -anz", "E", r"[a-zäöü]{2}(ant|anz)(e|en|er|es|em|in|innen|s)?$",
    OR(r"(?<!is)(?<!bs)(?<!ns)tanz(e|en|er|es|em|t|te|ten|st)?$", r"(glanz|schwanz|kranz|pflanz|schanz|wanz|franz)(e|en|er|es|em|t|te|ten|st)?$", W("ganz","ganze","ganzen","ganzer","ganzes","ganzem","lanze","lanzen","ranzen"), r"schulranzen",
       r"(tante|tanten|kante|kanten|plant|plante|planten|geplant|geplante|geplanten|geplanter|geplantes|geplantem|eingeplant|verplant)$",
       W("grant","rant","brant")))
add("-ent / -enz", "E", r"[a-zäöü]{2}(ent|enz)(e|en|er|es|em|in|innen|s)?$",
    OR(r"ment(e|en|er|es|s)?$", r"(prozent|prozente|prozenten|prozents)$", r"dient(e|en|est|et)?$", r"(event|events|talent|talente|talenten|talents)$",
       r"(grenz|grenze|grenzen|kredenz|kredenzen|florenz|konstanz|rente|renten|trient|vincent|vincents|laurent|clement|sorrent)$", W("lenz","ente","enten","gent","gents","kent"), r"(stock|wild|bade|gummi|zeitungs)enten?$"))
add("-ment (-mente)", "E", r"[a-zäöü]{2}ment(e|en|s|es)?$", r"(konsument|konsumenten|konsumentin|ferment$x)$")
add("-ur (-uren)", "E", r"[a-zäöü]{2}[^aeiouäöüh]ur(en)?$", r"(spur|spuren|flur|fluren|schnur|schwur|singapur|kur$x)$")
add("-or (-oren, -orin)", "E", r"(at|it|ut|kt|pt|ss|ns|ent|vest|ast|mot|aut|ens|sp?ons|tum|hum|terr|horr|lab|ten)or(en|in|innen|s)?$",
    OR(r"(sieg|eigen|stadt|burg|garagen|führungs|ausgleichs|anschluss|treffer|kopfball|elfmeter|ehren|siegtor$x)tor(e|en|es|s)?$",
       r"(viktor|hektor|nestor$x)$"))
add("-at (-ate, -aten)", "E", r"[a-zäöü]{2}at(e|en|s|es|in|innen)?$",
    OR(r"(?<!pa)(?<!se)(?<!fe)(?<!nt)(?<!te)(?<!ka)(?<!ad)(?<!dr)rat(e|en|es|s|in|innen)?$", r"räte(n)?$",
       r"(?<!zi)(?<!tten)(?<!ul)(?<!bi)(?<!es)tat(e|en|s|es)?$",
       r"(aat|aate|aaten|aates|aats)$", r"(monat|monate|monaten|monats|heimat|heimaten)$", r"hat$", r"(baten|^bat)$",
       r"(update|updates|state|trade|estate|private$x)$", r"(braten|raten|beraten|geraten|verraten|heiraten|traten)$"))
add("-ar / -är", "E", r"[a-zäöü]{2}(är|ular|inar|entar|orar|itar|iar|plar|ntar|ikar|nar)(e|en|er|es|em|s|in|innen)?$",
    r"(bär|bären|sphäre|sphären|affäre|affären|klär|kläre|klären|erklären|aufklären|geklärt$x)$")
add("-eur / -euse", "E", r"[a-zäöü]{2}(eur|euse)(e|en|in|innen|s)?$", r"(schleuse|schleusen|euro)$")
add("-age (-agen)", "E",
    r"(garage|etage|massage|reportage|sabotage|spionage|passage|blamage|courage|bandage|collage|plantage|drainage|staffage|visage|persiflage|stellage|takelage|kartonage|equipage|camouflage|kolportage|gage)(n)?$")
add("-ette (-etten)", "E", r"[a-zäöü]{2}ette(n)?$",
    r"((?<!eti)kette|(?<!eti)ketten|wette|wetten|fette|fetten|bette|betten|stette|klette|kletten|^rette|^retten|komplette|kompletten|amstetten|henriette|annette|bernadette|jeanette|nanette|colette|antoinette|odette|juliette|georgette|babette|lafette$x)$")
add("-ade (-aden)", "E", r"[a-zäöü]{2}ade(n)?$",
    OR(r"(sch|gn|m|w|pf|fl|tr|st|b|f)aden$", r"(?<!l)laden$", W("gerade","geraden","schade","grade","gnade","pfade","bade","fade","made","wade","lade","stade","trade"), r"(schublade|bundeslade|loaden|berchtesgaden|gerade|geraden|gnade|grade|blade|trade|upgrade)$"))
add("-ös (-öse)", "E", r"[a-zäöü]{2}ös(e|en|er|es|em)?$",
    r"(bös|böse|bösen|böser|böses|getöse|schös|löser|lösern|lösers|gekröse)$|(?<!da)(?<!bu)lös(e|en|t|te|ten)?$")
add("-abel / -ibel", "E", r"[a-zäöü]{2}(abel|ibel|able|ible|ablen|iblen|abler|ibler|ables|ibles|ablem|iblem)$",
    r"(gabel|gabeln|schnabel|kabel|säbel|fabel|nabel|bibel|fibel|giebel|zwiebel|isabel|mirabel|kabeln|kabels)$")
add("-ine (-inen)", "E", r"[a-zäöü]{2}[^e]ine(n)?$",
    r"(line|linen)$|(termin|vitamin|magazin|disziplin|kamin|benzin|protein|medizin|delfin|delphin|rubin|insulin|nikotin|koffein|harlekin|cousin|pinguin|alpin|philippin|argentin|palästin|florentin|byzantin|latin|doktrin|ukrain|onlin|offlin|feminin|maskulin|kristallin|bergamin|resin|cabrin)e(n)?$|(trine|christine|martine|sabine|nadine|carine|karine|janine|corinne$x|jacqueline|caroline|karoline|pauline|josefine|katharine|wilhelmine|ernestine|valentine|catherine$x)$")
add("-ium / -um / -us (lat. Endungen)", "E", r"[a-zäöü]{2}(ium|[^aeiouäöü]um|[^aeiouäöü]us)$",
    OR(r"ismus$", r"(?<!da)(?<!quan)(?<!fak)(?<!vo)(?<!spek)(?<!sep)(?<!ul)tum$",
       r"(darum|warum|herum|rum|drum|ringsum|wiederum|rundum|reihum|andersrum|bochum|stumm|dumm)$", r"(?<!is)(?<!thm)(?<!m)mus$",
       r"(markus|marcus|jesus|christus|franziskus|belarus|lukas$x|klaus|haus|maus|laus|graus|kraus|schmaus|aus|plus|minus|bus|nus$x|cyprus|zypern$x|venus$x|paulus|matthäus|petrus|thomas$x|augustus|julius|lucius|titus|brutus|cornelius|columbus)$"))

# =============== WORTSTÄMME (überall im Wort) ===============
add("akt / ag (handeln, tun)", "K",
    r"(^|[^tfprlkd])akt|^agier|agent|^agenda|reagier|interagier|redakt|redigier",
    OR(r"(kontakt|takt|fakt|pakt|trakt|lakt|katarakt|charakt|artefakt|abstrakt|extrakt|kompakt|kontrakt|vertrakt|nackt|bakter|exakt$x)", r"(magen|wagen|tagen|lagen|klagen|sagen|plagen)t$x"))
add("form (Gestalt)", "K", r"form", r"(formel1$x)")
add("polit / poliz (Stadt, Bürger)", "K", r"(polit|poliz|metropol|kosmopolit|akropolis)", r"polizz")
add("fakt / fekt / fiz (machen)", "K", r"(fakt|fekt|fizi|fikat|fizit|fizier|fikation|offiz|profit)")
add("duk / duz (führen)", "K", r"(duk(?!at)|duz)")
add("sozi (Gefährte, Gemeinschaft)", "K", r"sozi")
add("nat (geboren, Herkunft)", "K", r"(^|inter|multi|trans|supra|ur)nation|(^|[^g])natur|^nativ|pränatal|postnatal|^naiv", r"(signatur|nominativ$x)")
add("sta / sist / stit (stehen, stellen)", "K",
    r"(stitu|station|statist|^status|statut|stabil|existen|existier|assist|resist|konsist|persist|insist|distanz|konstan|instan[zt]|substan)")
add("pos / pon (setzen, stellen)", "K", r"(posit|kompon|oppon|expon|depon|propon|dispos|kompos|expos|oppos|propos|impos|transpos|präpos|deposit|^depot)")
add("gen (Ursprung, Erzeugung)", "K",
    r"(homogen|heterogen|halogen|kollagen|pathogen|allergen|karzinogen|androgen|östrogen|antigen|fotogen|telegen|genetik|genetisch|genom(?!m)|genese|gentechn|generation|generator|generell|generier|genre|^gender|-gender|^gen(e|s)?$|^genial|^genie(?!ß))")
add("mot / mob (bewegen)", "K", r"(motor|motiv|motion|mobil|promot|lokomot|emotion|remot)", r"mobbing")
add("log (Wort, Lehre, Vernunft)", "K",
    r"(logie|logisch|logik|logist|logos|^logo|ologe|ologin|dialog|katalog|prolog|epilog|monolog|analog|ideolog)",
    r"(blog|login|logout|vlog|logbuch|logging|loggen)")
add("jekt (werfen)", "K", r"jekt")
add("zent (Mitte)", "K", r"(zentr|zentral|zentrum|zentren)")
add("techn (Kunst, Können)", "K", r"techn")
add("struk / stru (bauen)", "K", r"(struk|strum|struier)", r"strumpf")
add("zept / zip / kap (nehmen, fassen)", "K", r"(zept|zipat|zipier|prinzip|partizip|kapazit|akzept|antizip|emanzip)")
add("leg / lekt (lesen, wählen)", "K",
    r"((?<!f)lekt(?!r)|lektür|kolleg|intellig|eleg[ai]n|legende$|legenden$|^legende|legendär|selekt|kollekt|dialekt)",
    r"(grundlegend|zulegend|festlegend|offenlegend|darlegend|hinterlegend|elektr)")
add("gramm (Geschriebenes)", "K", r"gramm", r"instagram")
add("kult (pflegen, bebauen)", "K", r"kult", r"(fakult|okkult)")
add("vers / vert (wenden)", "K",
    r"((uni|di|kontro|re|kon|in|per|sub|tra|ad)vers|^version|version$|versionen$|konvert|vertikal|invert|advert|divert)",
    r"(versch|einverst|einvers)")
add("vis / vid (sehen)", "K", r"(video|vision|visit|visum|visuell|visuali|evident|provis|revis|supervis|improvis|visier)", r"(division|devise|provision)")
add("kurs / kurr (laufen)", "K", r"(kurs|kurr|kurier|konkurs)", r"(kursk|skurr)")
add("spekt / spek (schauen)", "K", r"(spekt|spekul|spektr|spektak|spizier|spezies)")
add("graf / graph (schreiben)", "K", r"(graf|graph)", r"(^graf$|^grafen$|gräfin|landgraf|markgraf|burggraf|pfalzgraf|reichsgraf|grafschaft)")
add("demo (Volk)", "K", r"(demokr|demogr|epidem|pandem|^endem|endemisch|demoskop|demagog)")
add("trakt (ziehen)", "K", r"(trakt|kontrah)")
add("foto / phot (Licht)", "K", r"(foto|phot)")
add("geo (Erde)", "K", r"(geolog|geometr|geograf|geograph|geopolit|geowiss|geotherm|geodät|geophys|geozentr|geochem|geopark|geodaten|geoinformat|geomorph|geostrateg|geotop|geosphär|^geo$|^geos$)")
add("miss / mitt (schicken)", "K",
    r"(mission|missar|missär|kompromiss|emitt(?!el|eil)|komitee|demiss|emiss|premiss|transmiss|permiss|submiss|intermitt|remitt)")
add("medi (Mitte)", "K", r"(medi(en|um|al|at|ator|ation)|intermedi)", r"(medizin|medikament|medit)")
add("phon / fon (Laut, Stimme)", "K", r"(phon|fon(?!d|ds|t|ta|tä|tan|tän))", r"(fonds|fondu|font|fontane|fontäne|alfons|montafon|vodafone|iphone)")
add("press (drücken)", "K", r"press", r"(zypress|wordpress|pressbaum)")
add("bio (Leben)", "K", r"bio(?!n)", r"fabio")
add("plik / plex (falten)", "K", r"(plik|plex|plizi|pliz|kompliz)")
add("psych (Seele)", "K", r"psych")
add("tend / tens (spannen)", "K", r"(tendenz|tendier|intens|extens|intend|intention)", r"nintendo")
add("gress / grad (schreiten, Stufe)", "K", r"(gress|gradu|degrad|retrograd|^grad(e|en|s)?$|grad$)", r"(^grade$|belgrad)")
add("port (tragen)", "K", r"(export|import|transport|report|support|deport|rapport|portemonnaie|portfolio|^porto$|portabel|portable|apport)")
add("nom (Gesetz, Ordnung)", "K", r"(ökonom|astronom|autonom|gastronom|agronom|taxonom|metronom|ergonom|heteronom)")
add("erg (Werk, Arbeit)", "K", r"(energ|ergonom|synerg|allerg|chirurg|liturg|dramaturg)", r"nergebn")
add("phys (Natur)", "K", r"phys(?!alis)")
add("therap (pflegen, heilen)", "K", r"therap")
add("sphär (Kugel, Hülle)", "K", r"sphär")
add("kreat (schaffen)", "K", r"kreat", r"(kreatin|pankreat)")
add("ple (füllen)", "K", r"(komplett|plenar|plenum|komplement|supplement)")
add("integ (ganz, unberührt)", "K", r"integ")
add("nov (neu)", "K", r"(innov|renov|novell|novum|novize|novität)")
add("fer / lat (tragen, bringen)", "K", r"(konfer|referen|referat|referent|transfer|offerte|differen|präfer|interfer|relat|translat|legislat)")
add("vent / ven (kommen)", "K", r"(event|konvent|prävent|intervent|advent|invent|interven|subvent|souvenir)")
add("sequ / sek (folgen)", "K", r"(konsequ|sequenz|exekut|^sekund|sekunde)")
add("lok (Ort)", "K", r"(lokal|lokomot|lokation|allokat|dislok|lokalisier)")
add("mun (Pflicht, gemeinsam)", "K", r"(kommun|(^|[^t])immun)")
add("man (Hand)", "K", r"(manuell|manuskript|manöv|manufakt|manipul|mandat|manikür|emanzip|management|manager)")
add("kapit (Kopf, Haupt)", "K", r"kapit(?!za)|kapitän")
add("ziv (Bürger)", "K", r"zivil")
add("human (Mensch)", "K", r"human", r"schumann")
add("rupt (brechen)", "K", r"rupt")
add("vok / voz (rufen)", "K", r"(provo[kz]|vokal|advokat|vokabel|evoz|invok)")
add("solv / solut (lösen)", "K", r"(absolv|absolut|resolu|solvent)")
add("aud (hören)", "K", r"(audio|audienz|auditor|audition|audiovis)", r"claudio")
add("jur / jus (Recht)", "K", r"(jurist|juris|justiz|justier|^jury$|^jus$)")
add("pens / pend (wägen, zahlen)", "K", r"(pension|kompens|dispens|stipend|suspend)")
add("dynam (Kraft)", "K", r"dyna[mns]")
add("zykl / cycl (Kreis)", "K", r"(zykl|cycl)")
add("theo (Gott)", "K", r"(theolog|atheis|theokrat|pantheon|monothe|polythe)")
add("chron (Zeit)", "K", r"chron")
add("path (Leiden, Gefühl)", "K", r"path", r"^path$")
add("nym (Name)", "K", r"nym", r"(nymph|hieronym)")
add("kred (glauben, vertrauen)", "K", r"(kredit|akkredit|kredib)")
add("dikt / diz (sagen)", "K", r"(dikt|indiz|prädikat|dedikat|indikat)", r"benedikt")
add("ped / päd (Kind, Erziehung)", "K", r"(päd(?!er)|pädag|enzyklop)")
add("flex / flekt (biegen)", "K", r"(flex|flekt)")
add("sens / sent (fühlen)", "K", r"(sensib|sensor|sensation|sensuel|konsens|nonsens|dissens|sentiment)")
add("puls (stoßen)", "K", r"puls")
add("therm (Wärme)", "K", r"therm")
add("hydr / aqua (Wasser)", "K", r"(hydr|aqua(?!plan))", r"^(hydra|aqua)$")
add("kosm (Welt, Ordnung, Schmuck)", "K", r"kosm", r"kokos")
add("skript / skrib (schreiben)", "K", r"(skript|skrib|script)")
add("naut (Seefahrer)", "K", r"naut(?!o)", r"(arnaut|donaut)")
add("morph (Gestalt)", "K", r"morph", r"(morphin|morphium|morpheus|morphosys)")
add("öko (Haus, Haushalt)", "K", r"öko")
add("elektr (Bernstein, Elektrizität)", "K", r"elektr")
add("astro / aster (Stern)", "K", r"(astro|asteroid|desaster)", r"(astrid|gastro|katastroph)")
add("neuro (Nerv)", "K", r"(neuro|neural|neuron|neurit|neurot)")
add("phil (lieben)", "K", r"phil(?!ipp|ip|lip|ly|li$)", r"^(phil|phils)$|theophil|philadelph|syphil")
add("phob (Furcht)", "K", r"phob")
add("krat (Herrschaft)", "K", r"(krat(?!z)|kratie)", r"(krater|kratz|sokrat|hippokrat|lukrat)")
add("metr / meter (Maß)", "K", r"(meter|metern|meters|metrie|metrisch)")
add("skop (schauen)", "K", r"skop", r"(skopp|skopje)")
add("thek (Ablage)", "K", r"thek")

# --- Nachträge nach Datenprüfung ---
add("-ier (-iere)", "E", r"[a-zäöü]{2}ier(e|s|in|innen)?$",
    OR(r"(tier|tiere|tieren|tiers|bier|biere|bieren|biers|vier|hier|schier|gier|zier|stier|stiere|pier|begier|eier|feier|meier|maier|mayer|bayer|geier|leier|reier|schleier|steier|dreier|zweier|vierer|weiher|brauer)$", r"eier(n|s)?$", r"(?<!re)(?<!kla)vier$", W("viere", "vieren", "papierene"), r"(trier|spanier|kanadier|australier|argentinier|indonesier|tunesier|belgier|georgier|syrier|algerier|indier|bolivier|armenier|albanier|kalifornier|sardinier|mazedonier|bosnier|äthiopier|ligurier|kalabrier|umbrier|patagonier|tschetschenier|dalmatier|istrier|tasmanier|polynesier|liberier|anatolier|gallier|kolumbier|sizilier|asturier|kantabrier|andalusier|katalonier|kastilier|slowenier|kroatier|serbier|rumänier|bulgarier|mesopotamier|sibirier|mauretanier|nigerier|tansanier|kenier)(n|s|in|innen)?$"), noun=True)
add("spez (Art, Gattung)", "K", r"spez(i|ies)")
add("fin (Ende, Grenze)", "K", r"(^final|finale|definit|definier|infinit|^finish|finit)")
add("real (Sache, wirklich)", "K", r"real", r"(areal|real-madrid|montreal)")
add("norm (Regel, Maß)", "K", r"norm", r"(normand|norman|^norma$)")
add("ident (derselbe)", "K", r"(^|[^s])ident", r"evident")
add("organ (Werkzeug)", "K", r"organ", r"(vorgang|vorgäng|morgan)")
add("funk (verrichten)", "K", r"(funktion|fungier)")
add("situ (Lage)", "K", r"situ")
add("tradi (übergeben)", "K", r"tradi")
add("reg / rekt (lenken, richten)", "K", r"(region|regier|regent|regie|regime|regul|rektor|direkt|korrekt|rektion|rekti(?!on$x))", r"(regen$|regenbogen)")
add("par (bereiten)", "K", r"(parität|apparat|präpar|reparat|reparier|separ|^parat$)")
