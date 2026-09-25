# Ch9 + Utószó/Epilogue + back matter — see opus55-findings.md "Ch9", "Utószó", "Back matter"
from apply import E

EDITS = [
    # 9.1
    E("HUN", "9.1", "„Ó, emberek, dicsérem Allahot (ﷻ), mert nincs más isten.", "„Ó, emberek, dicsérem Allahot (ﷻ), akin kívül nincs más isten."),
    E("ENG", "9.1", "\"O people, I praise Allāh (ﷻ), because there is no other god.", "\"O people, I praise Allāh (ﷻ), besides Whom there is no god."),
    # 9.2
    E("HUN", "9.2", "akinek bármije van nálam, adja át, és ne mondja", "akinél van valami, amivel tartozik, adja meg, és ne mondja"),
    # 9.3
    E("HUN", "9.3a", "Reszketett, feje még mindig be volt kötve.", "Lázas volt, feje még mindig be volt kötve."),
    E("ENG", "9.3a", "He was shivering and his head was still bandaged.", "He was feverish and his head was still bandaged."),
    E("HUN", "9.3b", "Borongós, komor délután volt.", "Dél volt, amelyre komorság borult, és amelyet elárasztott a gyengédség."),
    E("ENG", "9.3b", "It was an afternoon clouded with gloom.", "It was a midday shaded by gloom and suffused with tenderness."),
    E("HUN", "9.3c", "ők pedig figyelmesen hallgatták. Amikor érezte", "ők pedig figyelmesen hallgatták — és íme, csodálatos dolgot hallottak tőle. Amikor érezte"),
    E("ENG", "9.3c", "and they listened attentively to him. When he felt", "and they listened attentively to him — and lo, they heard something wondrous from him. When he felt"),
    # 9.4
    E("HUN", "9.4", "csakhogy mindannyiunk közül egyedül Abū Bakr (رضي الله عنه) tudta ezt.", "és Abū Bakr (رضي الله عنه) értette ezt a legjobban mindannyiunk közül."),
    E("ENG", "9.4", "though only Abū Bakr (رضي الله عنه) knew that among all of us.", "and Abū Bakr (رضي الله عنه) was the one among us who understood this best."),
    # 9.5
    E("HUN", "9.5a", "Három nap múlva válságos helyzetben leszel.", "Három nap múlva más parancsa alatt leszel (»a bot szolgája«)."),
    E("ENG", "9.5a", "In three days time you'll be in a critical position.", "In three days' time you will be under another's command ('the slave of the stick')."),
    E("HUN", "9.5b", "akkor a lelkükre köti, hogy igazságosan bánjanak velünk.", "akkor a lelkükre köti, hogy jól bánjanak velünk."),
    E("ENG", "9.5b", "and if not he will enjoin justice upon us.", "and if not, he will enjoin them to treat us well.\""),
    # 9.6
    E("HUN", "9.6a", "és a Próféta (ﷺ) társai azt hitték", "és azok, akik a Prófétát (ﷺ) szerették, azt hitték"),
    E("ENG", "9.6a", "and the Companions of the Prophet (ﷺ) thought", "and those who loved the Prophet (ﷺ) thought"),
    E("HUN", "9.6b", "a nemzetre, amelyet felépített", "az ummára, amelyet megformált"),
    # 9.7
    E("HUN", "9.7a", "mint a szolgák és az alkalmazottak.", "mint a szolgák, az alárendeltek és a rabszolgák."),
    E("ENG", "9.7a", "such as servants and employees.", "such as servants, subordinates and slaves."),
    E("HUN", "9.7b", "a jó holléte felé fordítsa", "a jó sarokköveire irányítsa"),
    E("ENG", "9.7b", "to the whereabouts of goodness", "to the cornerstones of goodness"),
    E("HUN", "9.7c", "tetteik igazságos jutalmát", "tetteik megérdemelt következményét"),
    # 9.8
    E("HUN", "9.8", "legtöbb tanácsa, amikor a halál rátört, az ima volt, meg az, akit jobb kezünk birtokol.", "legtöbb intelme, amikor a halál rátört, ez volt: »Az ima, és akiket jobb kezetek birtokol!«"),
    E("ENG", "9.8", "when death was upon him, was prayers and what one's right hand possessed.", "when death was upon him, was: 'The prayer, and those whom your right hands possess!'"),
    # 9.9
    E("HUN", "9.9a", "meg akarta volna nyugtatni őt teljes őszinteségük felől, megadta neki a lehetőséget, hogy lássa őket földi utolsó imája idején.", "meg akarta volna nyugtatni őt teljes engedelmességük és hű követésük felől, megadta neki, hogy még egyszer, utoljára lássa őket, amíg e világon volt."),
    E("ENG", "9.9a", "wanted to satisfy him about their absolute sincerity, He (ﷻ) granted him the opportunity to see them at the time of his last prayer on earth.", "wanted to reassure him of their complete obedience and faithful following, He (ﷻ) let him witness them one last time while he was still in this world."),
    E("HUN", "9.9b", "egy imám mögött, aki halkan recitált, és bőséges őszinteséggel.", "egy gyengéd recitálású, őszinteséggel teli imám mögött."),
    # 9.10 + 9.11 (+ closing the unclosed quote)
    E("HUN", "9.10", "»Nem, a Legfőbb Társat a paradicsomból.«", "»Nem, a Legfőbb Társat a Paradicsomból.«"),
    E("HUN", "9.11", "Én (magamban) így szóltam: »Választást kaptál, és választottál, Arra, aki az Igazsággal küldött téged.« És Allah Küldötte (ﷺ) elhunyt.¹⁸", "Én így szóltam: »Választást kaptál, és választottál — Arra, Aki az igazsággal küldött téged!« És Allah Küldötte (ﷺ) elhunyt.\"¹⁸"),
    E("ENG", "9.11", "I said (to myself): \"You were given the choice", "I said: \"You were given the choice"),
    # 9.12
    E("HUN", "9.12", "és negyven napig távol volt népétől", "és negyven éjszakára eltávozott népétől"),
    E("ENG", "9.12", "and was away from his people for forty-days", "and was away from his people for forty nights"),
    # 9.13
    E("HUN", "9.13a", "ahol a Próféta (ﷺ) egy sarokban feküdt szemfedőbe burkolva. Odalépett, felfedte a fejét,", "ahol a Próféta (ﷺ) a ház egyik sarkában feküdt, egy csíkos jemeni köpennyel (burd ḥibarah) letakarva. Odalépett, felfedte az arcát,"),
    E("ENG", "9.13a", "where the Prophet (ﷺ) was shrouded in a corner. He came up and uncovered his head,", "where the Prophet (ﷺ) lay in a corner of the house, covered with a striped Yemeni cloak (burd ḥibarah). He came up and uncovered his face,"),
    E("HUN", "9.13b", "Visszahelyezte a kendőt a Próféta (ﷺ) fejére", "Visszahelyezte a leplet a Próféta (ﷺ) arcára"),
    E("ENG", "9.13b", "He replaced the cloth over the Prophet's (ﷺ) head", "He replaced the cloth over the Prophet's (ﷺ) face"),
    # 9.14
    E("HUN", "9.14", "„Apámra és anyámra! Megízlelted", "„Apám és anyám legyen váltságod! Megízlelted"),
    E("ENG", "9.14", "\"By my father and mother! You have tasted", "\"May my father and mother be your ransom! You have tasted"),
    # 9.15
    E("HUN", "9.15", "(Mohamed csupán küldött, [olyan] küldöttek [jártak], amilyenek már elmúltak előtte. Vajon, ha meghal vagy megöletik, sarkon fordultok? Aki visszafordul, semmiben sem árt Allahnak, és Allah megjutalmazza a hálásakat.) (Korán 3: 144)",
      "(Mohamed csupán Küldött; Küldöttek múltak el előtte [is]. Vajon ha meghal vagy megöletik, sarkon fordultok? Aki sarkon fordul, semmit sem árt Allahnak, és Allah megjutalmazza a hálásakat.) (Korán 3: 144)"),
    # 9.16
    E("ENG", "9.16", "they took their Prophet's (ﷺ) graves as mosques.", "they took the graves of their prophets as mosques."),
    # footnotes
    E("HUN", "9.f3a", "Al-'Uqailī hagyományozta a gyenge hadíszok gyűjteményében, valamint Al-Bayhaqī.", "Al-'Uqailī hagyományozta az *Al-Ḍu'afā'* (A gyenge hagyományozók) című művében, valamint Al-Bayhaqī."),
    E("ENG", "9.f3a", "transmitted by Al-'Uqailī in his collection of weak ḥadīths also by Al-Bayhaqī.", "transmitted by Al-'Uqailī in his *Al-Ḍu'afā'* (on weak narrators) and by Al-Bayhaqī."),
    E("HUN", "9.f3b", "Láncában (isnād) és szövegében (matn) rendkívüli homályosság van.", "Láncában (isnād) és szövegében (matn) rendkívüli különösség (gharābah) van."),
    E("ENG", "9.f3b", "In its isnād and matn there is extreme obscurity.", "In its isnād and matn there is extreme strangeness (gharābah)."),
    E("HUN", "9.f4", "⁴ Hiteles (ṣaḥīḥ): a két sejk hagyományozta. Ez Bukhārī változata.", "⁴ Hiteles (ṣaḥīḥ): a két sejk hagyományozta. Ez Bukhārī változata. A másik változatot Ibn Hishām hagyományozta Ibn Isḥāqtól, az ő láncával, Abū Sa'īd ibn al-Mu'allā családjának egy tagjától; ez gyenge, mivel ez a személy ismeretlen."),
    E("ENG", "9.f4", "⁴ Ṣaḥīḥ: transmitted by the two Sheikhs. This is the version of Bukhārī.", "⁴ Ṣaḥīḥ: transmitted by the two Sheikhs. This is the version of Bukhārī. The other version is transmitted by Ibn Hishām from Ibn Isḥāq with his chain from a member of the family of Abū Sa'īd ibn al-Mu'allā; it is weak because that person is unknown."),
    E("HUN", "9.f8", "⁸ Hiteles (ṣaḥīḥ): Al-Tirmidhī és Ibn Hishām hagyományozta.", "⁸ Hiteles (ṣaḥīḥ): Al-Tirmidhī hagyományozta, és jónak (ḥasan) minősítette, valamint Ibn Hishām."),
    E("ENG", "9.f8", "⁸ Ṣaḥīḥ: transmitted by Al Tirmidhī and Ibn Hishām.", "⁸ Ṣaḥīḥ: transmitted by Al Tirmidhī, who graded it ḥasan, and by Ibn Hishām."),
    E("HUN", "9.f10", "Al-Qāsim ibn Mohamedtől, 'Ā'ishah tekintélyére hivatkozva. Gyengének mondta, mivel ez a Mūsā ismeretlen.", "Al-Qāsim ibn Muhammadtól, 'Ā'ishah tekintélyére hivatkozva. Al-Tirmidhī „gharīb\"-nak nevezte, ami itt gyengét jelent, mert ezt a Mūsāt senki sem nyilvánította megbízhatónak, tehát ismeretlen."),
    E("ENG", "9.f10", "He said it was weak because this Mūsā was unknown.", "Al-Tirmidhī called it 'gharīb', meaning weak, because no one declared this Mūsā reliable, so he is unknown."),
    E("HUN", "9.f13", "¹³ A két sejk hagyományozta.", "¹³ Hiteles (ṣaḥīḥ): a két sejk hagyományozta."),
    E("ENG", "9.f13", "¹³ Transmitted by the two Sheikhs.", "¹³ Ṣaḥīḥ: transmitted by the two Sheikhs."),
    E("HUN", "9.f16", "¹⁶ Hiteles (ṣaḥīḥ): Bukhārī, Muszlim és mások hagyományozták Ibn Al-Zuhrītól Anas (رضي الله عنه) tekintélyére hivatkozva, ám megszakadt (munqaṭi', a láncból hiányzik egy láncszem).",
      "¹⁶ Bukhārī, Muszlim és mások hagyományozták Anas (رضي الله عنه) tekintélyére hivatkozva, hasonló szöveggel. Ibn Hishām a könyvben idézett szöveggel hagyományozta Ibn Isḥāqtól, Al-Zuhrītól, Anastól; ez a lánc megszakadt (munqaṭi', a láncból hiányzik egy láncszem)."),
    E("ENG", "9.f16", "¹⁶ Ṣaḥīḥ: transmitted by Bukhārī, Muslim and others on the authority of Ibn Al Zuhrī from Anas (رضي الله عنه) but it is Munqaṭi' (the chain has a missing link.)",
      "¹⁶ Transmitted by Bukhārī, Muslim and others on the authority of Anas (رضي الله عنه) with similar wording. Ibn Hishām transmitted it in the wording of this book from Ibn Isḥāq from Al-Zuhrī from Anas; that chain is Munqaṭi' (it has a missing link)."),
    E("HUN", "9.f18a", "¹⁸ Hiteles (ṣaḥīḥ): Ibn Hishām hagyományozta Ibn Isḥāqtól hiteles lánccal", "¹⁸ Hiteles (ṣaḥīḥ): Ibn Hishām hagyományozta Ibn Isḥāqtól, az ő láncával"),
    E("ENG", "9.f18a", "¹⁸ Ṣaḥīḥ: Transmitted by Ibn Hishām from Ibn Isḥāq with a sound chain from", "¹⁸ Ṣaḥīḥ: Transmitted by Ibn Hishām from Ibn Isḥāq with his chain from"),
    E("HUN", "9.f18b", "Dicsőség Allahnak (ﷻ), hogy sikeres véghez juttatta.", "Hála és dicséret Allahnak (ﷻ), hogy sikerre vitte."),
    # Epilogue
    E("ENG", "E1", "Within a few days the Prophet's (ﷺ) death Islām", "Within a few days of the Prophet's (ﷺ) death Islām"),
    E("HUN", "E2", "a kereszténységgel, amely a félsziget északi részét uralta, megakadályozott", "a kereszténységgel, amely a félsziget északán lesben állt, megakadályozott"),
    E("ENG", "E2", "and Christianity, which controlled the north of the peninsula, prevented", "and Christianity, which lay in wait in the north of the peninsula, prevented"),
    E("HUN", "E3a", "A csataterek szélesebbek, a költségek magasabbak, a veszteségek nagyobbak voltak.", "A csataterek szélesebbek voltak, az utánpótlás egymást követte, a terhek súlyosabbak, a veszteségek nagyobbak lettek."),
    E("ENG", "E3a", "The battle fields were wider, the costs higher and the losses greater.", "The battlefields were wider, reinforcements followed one another, the costs were higher and the losses greater."),
    E("HUN", "E3b", "Szétverték a rómaiakat a határokon, ahol azok a gőgjüket terjesztették.", "Elűzték a rómaiakat a határokról, ahol azok lázongtak és zsarnokoskodtak."),
    E("ENG", "E3b", "They routed the Romans at the borders where the latter had spread their arrogance.", "They drove the Romans away from the borders where the latter had rebelled and tyrannised."),
    E("HUN", "E5", "az iszlám többé nem uralja ummáját, nemhogy a világot kormányozná említésre méltó föld vagy hálára méltó jó felé.", "az iszlám — nagy dicsőség után — többé nem uralja ummáját, nemhogy a világot említésre méltó jámborság vagy hálára méltó jó felé vezetné."),
    E("ENG", "E5", "Islām is no more ruling its Ummah, not to speak of steering the world to a land worth mentioning or to goodness worthy of thanks.", "Islām — after great glory — is no more ruling its Ummah, not to speak of steering the world to any righteousness worth mentioning or to goodness worthy of thanks."),
    E("HUN", "E6", "A többi vallás a halál szélén tengődik, mert a fennálló civilizációk", "A többi vallás az élet peremén tengődik, mert a fennálló vagy lesben álló civilizációk"),
    E("ENG", "E6", "The other religions are living on the brink of death, for the existing civilizations", "The other religions are living on the margins of life, for the existing civilizations, and those lying in wait,"),
    E("HUN", "E7", "és igyekszik learatni a legnagyobb hasznot Izrael számára azáltal, hogy a muszlimok sorain belüli szakadásra játszik.", "és az egymással hadakozó sorok résein átsurranva igyekszik a legnagyobb zsákmányt szerezni Izraelnek."),
    E("ENG", "E7", "Judaism is segregating its flock from the world implant in their hearts hatred for the mankind and to sweep away the greatest benefits for Israel by playing upon the split within the ranks of the Muslims.", "Judaism is segregating its flock from the world to implant in their hearts hatred for mankind and to slip through the gaps in the mutually warring ranks, carrying off the greatest spoils for Israel."),
    E("HUN", "E9", "Ma már csak egy jelentéktelen kisebbségük harcol", "Ma már csak egy csekély kisebbségük harcol"),
    E("ENG", "E9", "Only an insignificant minority of them remain today", "Only a small minority of them remain today"),
    E("HUN", "E10", "A bajkeverők azért gyűlölik az iszlámot", "A hamisság hívei azért gyűlölik az iszlámot"),
    E("ENG", "E10", "The mischief-makers hate Islām", "The champions of falsehood hate Islām"),
    E("HUN", "E11", "Ha nem lett volna cselszövéseknek kitéve, sohasem emelt volna kést, és beérte volna a nyelv használatával a kard helyett.", "Ha békén hagyták volna, rémítgetés nélkül, sohasem terhelte volna vállát lándzsával, és beérte volna a nyelvvel a lándzsahegy helyett."),
    E("ENG", "E11", "Had it not been subjected to intrigue, it would never have lifted a knife and would have contented itself with the use of the tongue instead of the sword.", "Had it been left alone without intimidation, it would never have burdened its shoulder with a spear and would have contented itself with the tongue instead of the spearhead."),
    E("HUN", "E12", "az iszlám erkölcsi és tudományos elvei", "az iszlám tudásbeli és lelki alapjai"),
    E("ENG", "E12", "Islām's moral and scientific principles", "Islām's intellectual and spiritual foundations"),
    E("HUN", "E13", "akik nem hisznek semmilyen Istenben, sem a túlvilágban", "akik nem hisznek semmilyen Istenben, sem az Utolsó Napban"),
    E("ENG", "E13", "who do not believe in any God or in the hereafter", "who do not believe in any God or in a Last Day"),
    E("HUN", "E14", "milyen erős a köteléked az iszlám Prófétájával (ﷺ).\n", "milyen erős a köteléked az iszlám Prófétájával (ﷺ).\n\n*Allah (ﷻ) dicséretével és kegyelméből elkészült.*\n"),
    E("ENG", "E14", "the strength of your connection with the Prophet (ﷺ) of Islām.\n", "the strength of your connection with the Prophet (ﷺ) of Islām.\n\n*Completed by the praise and grace of Allāh (ﷻ).*\n"),
    # Back matter
    E("HUN", "BM1", "*Isrā'*: A Próféta felemelkedése.", "*Isrā'*: A Próféta (ﷺ) éjszakai utazása Mekkából Jeruzsálembe."),
    E("ENG", "BM1", "*Isrā'*: The Prophet's ascension.", "*Isrā'*: The Prophet's (ﷺ) Night Journey from Makkah to Jerusalem."),
    E("HUN", "BM2", "dzsihād", "dzsihád", count=5),
    E("HUN", "BM3", "mielőtt az Ídi imára menne", "mielőtt az ünnepi ('Īd) imára menne"),
    E("HUN", "BM4", "*Mudhammam*: A Mohamed („a dicsért\") névnek a gáncsolást jelentő ellentéte.", "*Mudhammam*: A Mohamed („a dicsért\") név ellentéte: „a gyalázott\"."),
    # 9.10 book-wide: al-Jannah = Paradicsom (capital)
    E("HUN", "9.10bw", "a paradicsomba", "a Paradicsomba", count=3),
    # (1123 "paradicsombeli" is an adjective -> stays lowercase per HU orthography)
    E("HUN", "9.10bw", "örökké tartó paradicsom, vagy", "örökké tartó Paradicsom, vagy"),
    E("HUN", "9.10bw", "teljesítitek, paradicsom jár nektek", "teljesítitek, a Paradicsom jár nektek"),
    E("HUN", "9.10bw", "tiétek a paradicsom.«", "tiétek a Paradicsom.«"),
    E("HUN", "9.10bw", "„A paradicsomban egy ostorcsapásnyi", "„A Paradicsomban egy ostorcsapásnyi"),
]
