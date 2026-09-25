# Ch2 restorations — run AFTER the fntool shifts (gaps at ¹² and ²⁶). See opus55-findings.md "Ch2".
#  (1) Baḥīra: restore the author's body sentence «والمحققون(١) على أن هذه الرواية موضوعة…» and move
#      al-Albānī's inlined reply + the author's (*) rejoinder back into the footnote list as ¹².
#  (2) Waraqah: restore 'Ā'ishah's ḥadīth of the beginning of revelation (AR pp.69–70) + its fn ²⁶.
import pathlib
from apply import E, FILES

EDITS = []

# ---------- (1) Baḥīra, HUN ----------
h = FILES["HUN"].read_text(encoding="utf-8")
A = "\n\nA nyomozók! Kik ezek a nyomozók?"
if A in h:
    i = h.index(A)
    j = h.index("hogy megöljék!\n", i) + len("hogy megöljék!\n")
    block = h[i:j]                                   # "\n\nA nyomozók! … megöljék!\n"
    paras = block.strip("\n").split("\n\n")
    assert paras[0].startswith("A nyomozók!") and paras[1].startswith("Nem. Bár") and paras[-1].startswith("A hadísz tehát mu'allal"), paras[:2]
    quotes = paras[2:-1]                             # Al-Jazarī … Ibn Kathīr (kept as translated)
    quotes[0] = quotes[0].replace("„Lánca hiteles, elbeszélői a hiteles hagyomány emberei, vagy egyikük az. De Abū Bakr (رضي الله عنه) és Bilāl (رضي الله عنه) említése benne nem hiteles imámjaink szerint, és ez igaz.",
                                  "„Lánca hiteles, elbeszélői a Ṣaḥīḥ elbeszélői. Abū Bakr (رضي الله عنه) és Bilāl (رضي الله عنه) említése benne azonban nem megőrzött; imámjaink tévedésnek tartották (!), és ez így is van (!!).")
    body_new = (" A kutatók (muḥaqqiqūn)¹² azon a véleményen vannak, hogy ez az elbeszélés koholmány: utánzata annak, amit az evangélium-írók mondanak — hogy emberek keresték a Messiást nem sokkal születése után, hogy megöljék —, ez pedig a keresztényeknél annak utánzata, amit a pogányok mondanak: hogy Buddhát, amikor szűz (!) anyja megszülte, ellenségei keresték, hogy megöljék.\n")
    EDITS.append(E("HUN", "2.R1a", "hogy keresésük hiábavaló." + block, "hogy keresésük hiábavaló." + body_new))
    fn = ("¹² Kik ezek a kutatók? És honnan származik az említett koholmány? Ez az elbeszélés a fent említett, Abū Mūsā (رضي الله عنه) által közölt hadíszban szerepel, és láttad, hogy hiteles. Mit árt a hasonlóság, ha [a hadísz] bizonyított? Nem látod-e, hogy amit az evangélium-írók mondanak, hasonlít ahhoz, ami a nemes Koránban bizonyított: hogy a Fáraó kereste Mūsāt (عليه السلام), hogy megölje? El kellene-e hát vetnünk ezt a hasonlóság miatt? Allahra, nem!\n\n"
          "\\* Bár nagyra becsüljük a tudós Sejk Nāṣiruddīn szavait, idézünk itt valamit abból, amit a tudósok és a kutatók e történetről mondtak:\n\n"
          + "\n\n".join(quotes) +
          "\n\nA hadísz tehát mu'allal (rejtett hibát tartalmaz) a hadísz-terminológia tudományában megállapított szabályok szerint. (A szerző.)\n\n")
    EDITS.append(E("HUN", "2.R1b", "\n¹³ Bukhārī Abū Hurairah (رضي الله عنه) tekintélyére", "\n" + fn + "¹³ Bukhārī Abū Hurairah (رضي الله عنه) tekintélyére"))
EDITS.append(E("HUN", "2.R1c", "és minden irányba embereket küldtek elfogására.\" Baḥīra", "és minden útra embereket küldtek ki, hogy elfogják.\" (!) Baḥīra"))

# ---------- (1) Baḥīra, ENG ----------
g = FILES["ENG"].read_text(encoding="utf-8")
B = "\n\nThe investigators! Who are these investigators?"
if B in g:
    i = g.index(B)
    j = g.index("who wanted to kill him!\n", i) + len("who wanted to kill him!\n")
    block = g[i:j]
    paras = block.strip("\n").split("\n\n")
    assert paras[0].startswith("The investigators!") and paras[1].startswith("No. Although") and paras[-1].startswith("Therefore the Hadīth is mu'allal"), paras[:2]
    quotes = paras[2:-1]
    quotes[0] = quotes[0].replace("\"Its chain is sound and its narrators are those of the authentic tradition or one of them. But the mention of Abū Bakr (رضي الله عنه) and Bilāl (رضي الله عنه) in it is not authentic according to our imāms, and this is true.",
                                  "\"Its chain is sound and its narrators are the narrators of the Ṣaḥīḥ. But the mention of Abū Bakr (رضي الله عنه) and Bilāl (رضي الله عنه) in it is not preserved; our imāms counted it an error (!), and so it is (!!).")
    body_new = (" The investigators (muḥaqqiqūn)¹² hold that this report is fabricated, in imitation of what the Gospel-writers say — that some people sought the Messiah soon after his birth in order to kill him — which, among the Christians, in turn imitates what the pagans say: that the Buddha, when his virgin (!) mother gave birth to him, was sought by his enemies who wanted to kill him.\n")
    EDITS.append(E("ENG", "2.R1a", "that their search was futile." + block, "that their search was futile." + body_new))
    fn = ("¹²Who are these investigators? And where did the said fabrication come from? This account is in the above-mentioned Hadīth narrated by Abū Mūsā (رضي الله عنه), and you have seen that it is authentic. What harm does the resemblance do once it is established? Do you not see that what the Gospel-writers mention resembles what is established in the noble Qur'ān of Pharaoh's seeking Moses (عليه السلام) in order to kill him? Should we then reject this because of the said resemblance? By Allāh, no!\n\n"
          "\\* With all our appreciation of the words of the learned Sheikh Nāṣiruddīn, we quote here some of what the scholars and investigators have said about this story:\n\n"
          + "\n\n".join(quotes) +
          "\n\nTherefore the Hadīth is mu'allal (contains a hidden defect) according to the rules laid down by the scholars in the science of Ḥadīth terminology. (Author.)\n\n")
    EDITS.append(E("ENG", "2.R1b", "\n¹³Bukhārī narrates on the authority of Abū Hurairah", "\n" + fn + "¹³Bukhārī narrates on the authority of Abū Hurairah"))
EDITS.append(E("ENG", "2.R1c", "and men have been sent in all directions to arrest him. Baḥīra argued", "and men have been sent out on every road to arrest him.\" (!) Baḥīra argued"))

# ---------- (2) Waraqah ----------
HUN_W = """'Ā'ishah, a hívők anyja elbeszélte: „A kinyilatkoztatás Allah Küldöttének (ﷺ) igaz álmokkal kezdődött álmában: nem látott olyan álmot, amely ne teljesült volna be, akár a hajnal hasadása. Azután megkedvelte a magányt: a Ḥirā' barlangjába vonult el, és ott végezte a taḥannuthot — azaz az istenszolgálatot — számos éjszakán át, mielőtt visszatért volna családjához, és útravalót vitt magával ehhez; majd visszatért Khadījahhoz, és újabb hasonló útravalót vitt. Míg aztán váratlanul rátört az Igazság, amikor a Ḥirā' barlangjában volt. Eljött hozzá az angyal, és így szólt: »Olvass!« Ő azt felelte: »Nem tudok olvasni.« [A Próféta (ﷺ)] elmondta: »Erre megragadott, és addig szorított, míg a végső kimerülésig nem jutottam, majd elengedett, és így szólt: 'Olvass!' Azt feleltem: 'Nem tudok olvasni.' Erre megragadott, és másodszor is addig szorított, míg a végső kimerülésig nem jutottam, majd elengedett, és így szólt: 'Olvass!' Azt feleltem: 'Nem tudok olvasni.' Erre megragadott, és harmadszor is addig szorított, míg a végső kimerülésig nem jutottam, majd elengedett, és így szólt: (Olvass! A te Rabbod nevében, aki teremtett, Megteremtette az embert vérrögből…) (Korán 96: 1–2)«

Allah Küldötte (ﷺ) reszketve tért vissza vele, míg be nem lépett Khadījah bint Khuwaylidhoz, és így szólt: »Takarjatok be, takarjatok be!« Betakarták, míg el nem múlt róla a rémület. Ekkor így szólt Khadījahhoz: »Ó, Khadījah, mi történt velem?« — és elmondta neki, mi történt, majd hozzátette: »Féltem magamat…«

Khadījah így felelt neki: »Nem úgy van! Örvendj, mert Allahra (ﷻ), Allah (ﷻ) soha nem fog megszégyeníteni téged: ápolod a rokoni kötelékeket, igazat szólsz, terhet vállalsz a gyámoltalanért, gondoskodsz a nincstelenről, megvendégeled a vendéget, és segítesz az igaz ügyek csapásaiban.«

Majd Khadījah elvitte őt Waraqah ibn Nawfalhoz — Khadījah unokatestvéréhez —, aki a dzsáhilijja idején kereszténnyé lett. Héber írással írt, és az Evangéliumból annyit írt le héberül, amennyit Allah (ﷻ) akart, hogy leírjon. Idős ember volt, aki megvakult. Khadījah így szólt hozzá: »Ó, unokatestvérem, hallgasd meg testvéred fiát!«

Waraqah megkérdezte tőle: »Testvérem fia, mit látsz?« Allah Küldötte (ﷺ) elmondta neki, amit látott, mire Waraqah így szólt: »Ez az a Nāmūs [Jibrīl], akit Allah (ﷻ) Mūsāhoz (عليه السلام) küldött le. Bárcsak fiatal volnék akkor! Bárcsak életben lennék, amikor néped elűz téged!«

Allah Küldötte (ﷺ) megkérdezte: »Hát elűznek engem?« Ő így felelt: »Igen! Soha egyetlen ember sem hozott olyat, amilyet te hoztál, anélkül, hogy ellenségesen ne bántak volna vele. Ha megérem a te napodat, teljes erőmmel melletted állok.« Nem sokkal később aztán Waraqah meghalt, és a kinyilatkoztatás egy időre megszakadt."²⁶"""

ENG_W = """'Ā'ishah, the Mother of the Believers, said: "Revelation began for the Messenger of Allāh (ﷺ) with true dreams in his sleep: he never saw a dream but it came like the breaking of dawn. Then solitude was made dear to him, and he would seclude himself in the cave of Ḥirā', devoting himself there to taḥannuth — that is, worship — for a number of nights before returning to his family, taking provisions for it; then he would return to Khadījah and take provisions for a similar stay, until the Truth came upon him suddenly while he was in the cave of Ḥirā'. The angel came to him and said: 'Read!' He said: 'I cannot read.' He said: 'Then he seized me and pressed me until I could bear no more, then released me and said: "Read!" I said: "I cannot read." So he seized me and pressed me a second time until I could bear no more, then released me and said: "Read!" I said: "I cannot read." So he seized me and pressed me a third time until I could bear no more, then released me and said: (Read: In the name of your Lord Who creates, Creates man from a clot…) (Qur'ān 96: 1-2)'

The Messenger of Allāh (ﷺ) returned with it, trembling, until he came in to Khadījah bint Khuwaylid and said: 'Wrap me up! Wrap me up!' They wrapped him up until his fear left him. Then he said to Khadījah: 'O Khadījah, what is the matter with me?' He told her what had happened and said: 'I feared for myself…'

Khadījah said to him: 'Never! Rejoice, for by Allāh (ﷻ), Allāh (ﷻ) will never disgrace you. You keep the ties of kinship, you speak the truth, you bear the burden of the weak, you provide for the destitute, you honour the guest and you help those afflicted by the calamities of truth.'

Then Khadījah took him to Waraqah ibn Nawfal — Khadījah's cousin — who had become a Christian in the time of Jāhilīyah. He used to write in Hebrew script, and he would write from the Gospel in Hebrew as much as Allāh (ﷻ) willed him to write. He was a very old man who had become blind. Khadījah said to him: 'O cousin, listen to your brother's son!'

Waraqah said to him: 'O son of my brother, what do you see?' The Messenger of Allāh (ﷺ) told him what he had seen, and Waraqah said to him: 'This is the Nāmūs [Jibrīl] whom Allāh (ﷻ) sent down to Moses (عليه السلام). Would that I were a young man then! Would that I might be alive when your people drive you out!'

The Messenger of Allāh (ﷺ) said: 'Will they drive me out?' He said: 'Yes! No man has ever come with the like of what you have brought without being treated with enmity. If I live to see your day, I shall support you with all my strength.' Then before long Waraqah died, and the revelation paused for a while."²⁶"""

EDITS += [
    E("HUN", "2.R2a", "(Korán 42: 52–53)\n\nMintha az előző negyven év", "(Korán 42: 52–53)\n\n" + HUN_W + "\n\nMintha az előző negyven év"),
    E("ENG", "2.R2a", "(Qur'ān 42: 52-53)\n\nIt was as if the previous forty years", "(Qur'ān 42: 52-53)\n\n" + ENG_W + "\n\nIt was as if the previous forty years"),
    E("HUN", "2.R2b", "\n²⁷ A szerző egy hiteles hadíszra utal", "\n²⁶ Egy hiteles hadísz, amelyet Bukhārī és Muszlim elbeszélt.\n\n²⁷ A szerző egy hiteles hadíszra utal"),
    E("ENG", "2.R2b", "\n²⁷The author is referring", "\n²⁶An authentic Hadīth narrated by Bukhārī and Muslim.\n\n²⁷The author is referring"),
]
