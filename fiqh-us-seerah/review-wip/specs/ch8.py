# Ch8 — A hívők anyái (AR pp.333–353); see opus55-findings.md "## Ch8" (+ items found while re-reading the AR)
from apply import E

EDITS = [
    # dropped «وحسبه أن يوفق فى رعايتها وكفالة أولاده منها . . !» (AR p.333)
    E("HUN", "8.1", "az áll összhangban, hogy a férfinak csak egy felesége legyen.", "az áll összhangban, hogy a férfi érje be egyetlen asszonnyal, és ne lépjen túl rajta. Elég neki, ha sikerrel gondoskodik róla, és eltartja a tőle született gyermekeit…!"),
    E("ENG", "8.1", "in keeping with the development of civilization and the interests of the mankind that a man should have only one wife.", "in keeping with the development of civilization and the interests of mankind, a man should content himself with one wife and not go beyond her. It is enough for him to succeed in caring for her and supporting his children by her…!"),
    # «فالغرْم على قدر الغُنْم، والمتع الميسرة تتبعها حقوق ثقيلة»
    E("HUN", "8.2", "Az adók a gazdagsághoz igazodnak, és ahol könnyítés adatik, ott súlyosabb kötelesség követi.", "A teher a haszonnal arányos, és a könnyen elérhető élvezeteket súlyos kötelességek követik."),
    E("ENG", "8.2", "Taxes go in accordance with riches and when facilities are provided they are followed by heavier duties.", "Liability is in proportion to gain, and easy pleasures are followed by heavy obligations."),
    # dropped «الذى يعدد يجب أن يكون قادرا على النفقة اللازمة»
    E("HUN", "8.3", "akkor az számára nem megengedett.\n\nHa a törvény", "akkor az számára nem megengedett. Aki több feleséget vesz, annak képesnek kell lennie a szükséges eltartásukra.\n\nHa a törvény"),
    E("ENG", "8.3", "then it is not permissible for him.\n\nIf the law considers", "then it is not permissible for him. He who takes more than one wife must be able to bear the necessary maintenance.\n\nIf the law considers"),
    # Q4:3 as a Qur'ān quote; ENG missing closing quotes
    E("HUN", "8.4", "máskülönben érje be eggyel: „Ha pedig féltek, hogy nem tudtok igazságosak lenni, akkor csak egyet.\" (Korán 4: 3)", "máskülönben érje be eggyel: (Ha pedig féltek, hogy nem tudtok igazságosak lenni, akkor csak egyet [vegyetek el].) (Korán 4: 3)"),
    E("ENG", "8.4", "otherwise let him be content with one only: \"And if you fear you may not deal justly, then one.\" (Qur'ān 4: 3)", "otherwise let him be content with one only: (And if you fear you may not deal justly, then [marry] one.) (Qur'ān 4: 3)"),
    E("ENG", "8.4b", "whether he preserved it or destroyed it.²", "whether he preserved it or destroyed it.\"²"),
    E("ENG", "8.4c", "cause those whom he maintains to perish.³", "cause those whom he maintains to perish.\"³"),
    # «داعر وديوث أو قواد»
    E("HUN", "8.5", "hogy többségük vagy kicsapongó, vagy nők kerítője és futtatója.", "hogy többségük vagy kicsapongó, vagy asszonyai erkölcstelenségét eltűrő férj (dayyūth), vagy kerítő."),
    E("ENG", "8.5", "the majority of them are either licentious, or pimps-or-procurers of women.", "the majority of them are either debauchees, or men who condone their womenfolk's indecency (dayyūth), or pimps."),
    # «إن تقييد مباح ليس مما يعى سياسة التشريع فى الإسلام»
    E("HUN", "8.6", "A megengedett korlátozása annak bizonyítéka, hogy valaki nem érti az iszlám törvényét.", "Megengedett dolgot korlátozni nem tartozik az iszlám törvényhozási politikájához."),
    E("ENG", "8.6", "To restrict the permissible is proof of one's lack of understanding of Islāmic law.", "To restrict what is permissible is not part of Islām's legislative policy."),
    # honorifics (HUN)
    E("HUN", "8.7", "Khadījah akkor halt meg, amikor a Próféta alig múlt 50 éves.", "Khadījah akkor halt meg, amikor a Próféta (ﷺ) alig múlt 50 éves."),
    E("HUN", "8.7b", "akár szemernyi is megtalálható volt a Próféta házaiban.", "akár szemernyi is megtalálható volt a Próféta (ﷺ) házaiban."),
    E("ENG", "8.7b", "was to be found in the houses of the Prophet.", "was to be found in the houses of the Prophet (ﷺ)."),
    E("HUN", "8.7c", "hogy a Próféta rokonságát hadifogolyként tartják.", "hogy a Próféta (ﷺ) rokonságát hadifogolyként tartják."),
    # «فلأى مؤمن أن يستمتع بأربع نسوة»
    E("HUN", "8.8", "Minden hívőnek joga van élvezni feleségei társaságát,", "Bármely hívőnek joga van négy feleség társaságát élvezni,"),
    E("ENG", "8.8", "Every believer has their right to enjoy the company of his wives,", "Every believer has the right to enjoy the company of four wives,"),
    # «إن حملة الرسالات الإنسانية المحدودة تعييهم هموم العيش… فكيف بصاحب الرسالة العظمى؟ وقد لقى من العرب ما رأيت!»
    E("HUN", "8.9", "A kevés valóban nagy jelentőségű személyiséget bizony annyira lefoglalják az emberek gondjai, hogy aligha élveznek akár egy órányi pihenést is, legfeljebb hogy kissé erőt gyűjtsenek, mielőtt folytatnák véget nem érő munkájukat. Milyen lett volna hát a próféták legnagyobbikának helyzete, akit az arabok úgy fogadtak, ahogyan azt már jeleztük?",
      "Még a korlátozott, emberi küldetések hordozóit is annyira kimerítik a megélhetés gondjai és a népek bajai, hogy csak annyi pihenés jut nekik, amennyi alatt kissé erőt gyűjtenek, mielőtt újra nekilátnának fáradságos munkájuknak. Milyen lett volna hát a legnagyobb küldetés hordozójának helyzete, akit az arabok úgy fogadtak, ahogyan láttad?"),
    E("ENG", "8.9", "Surely the few personalities of great importance are so fully occupied with the problems of the people that they hardly enjoy an hour's rest except to recuperate a little before resuming their endless toil. What then would have been the situation of the greatest of prophets, who met with the kind of reception from the Arabs as we have indicated?",
      "Even the bearers of limited, human missions are so worn out by the cares of livelihood and the problems of nations that they hardly enjoy an hour's rest except to recuperate a little before resuming their weary toil. What then of the bearer of the greatest mission, who met with the kind of reception from the Arabs that you have seen?"),
    # «وقبل أخوها وهو يؤدى حق السمع والطاعة فحسب»; Q33:36 verse end
    E("HUN", "8.10", "Így hozzáment Zaydhoz, bár vonakodó szívvel.", "Így hozzáment Zaydhoz, bár vonakodó szívvel, fivére pedig csupán engedelmességből fogadta el."),
    E("ENG", "8.10", "Thus she married Zayd, though with reluctance in her heart.", "Thus she married Zayd, though with reluctance in her heart, and her brother accepted it merely out of obedience."),
    E("HUN", "8.11", "azután maguk igényeljenek bármi beleszólást ügyükbe.) (Korán 33: 36)", "azután maguk igényeljenek bármi beleszólást ügyükbe. Aki pedig engedetlen Allahhal és az Ő küldöttével szemben, az nyilvánvaló tévelygésbe esett.) (Korán 33: 36)"),
    E("ENG", "8.11", "(And it does not for a believing man or a believing woman, when Allah and His messenger have decided an affair [for them], that they should [after that] claim any say in their affair.) (Qur'ān 33: 36)",
      "(And it is not for a believing man or a believing woman, when Allah and His messenger have decided an affair [for them], that they should [after that] claim any say in their affair. And whoever disobeys Allah and His messenger has strayed into plain error.) (Qur'ān 33: 36)"),
    # non-Qur'ān saying in parentheses
    E("HUN", "8.12", "Amikor meg akarsz nyugtatni valakit, azt mondod: (Ne félj senkitől, csak Allahtól.)", "Amikor meg akarsz nyugtatni valakit, azt mondod neki: „Ne félj senkitől, csak Allahtól!\""),
    E("ENG", "8.12", "When you want to reassure people, you say, (Fear no-one but Allah.)", "When you want to reassure people, you say, \"Fear no-one but Allāh!\""),
    # «وما فى رفِّى شىء يأكله ذو كبد إلا شطر شعير فى رفّ لى»
    E("HUN", "8.13", "„Allah Küldötte (ﷺ) meghalt, és szekrényemben nem volt hús, amit ehettem volna. Csak egy darab árpakenyér volt az egyik polcomon.\"", "„Allah Küldötte (ﷺ) meghalt, és polcomon nem volt semmi, amit élőlény megehetett volna, csak egy kevés árpa az egyik polcomon.\""),
    E("ENG", "8.13", "\"Allāh's Messenger (ﷺ) died, and in my cupboard there was no meat to eat. There was only a piece of barley-bread in one of my shelves.\"", "\"Allāh's Messenger (ﷺ) died, and there was nothing on my shelf that any living creature could eat, except some barley on a shelf of mine.\""),
    # «اللهم اجعل رزق آل محمد قوتًا»
    E("HUN", "8.14", "„Ó, Allah (ﷻ), adj Mohamed (ﷺ) családjának táplálékot!\"", "„Ó, Allah (ﷻ), tedd Mohamed (ﷺ) családjának ellátását éppen elegendővé!\""),
    E("ENG", "8.14", "\"O Allāh (ﷻ), provide Muhammad's (ﷺ) family with nourishment.\"", "\"O Allāh (ﷻ), make the provision of Muhammad's (ﷺ) family bare sufficiency.\""),
    # «طلق نساءه جملة»
    E("HUN", "8.15", "hogy a Próféta (ﷺ) végleg elvált feleségeitől.", "hogy a Próféta (ﷺ) egyszerre elvált valamennyi feleségétől."),
    # «ابنة زيد» — no honorific in AR
    E("HUN", "8.16", "láttad volna Zayd (رضي الله عنه) leányát", "láttad volna Zayd leányát"),
    E("ENG", "8.16", "Nevertheless some lose atmosphere was still pressing heavily on the place, so 'Umar (رضي الله عنه) decided that he would speak to the Prophet (ﷺ) and make him laugh. He said: \"O Messenger of Allāh (ﷻ), if you had seen Zayd's (رضي الله عنه) daughter",
      "Nevertheless a gloomy atmosphere was still pressing heavily on the place, so 'Umar (رضي الله عنه) decided that he would speak to the Prophet (ﷺ) and make him laugh. He said: \"O Messenger of Allāh (ﷻ), if you had seen Zayd's daughter"),
    # «رغبة لم تتجاوز المباحات المشتهاة»
    E("HUN", "8.17", "hogy kitörölje elméjükből a vágyakozás utolsó nyomait is, amely nem jutott túl a heves kérlelés szakaszán.", "hogy kitörölje lelkükből annak a vágynak az utolsó nyomát is, amely soha nem lépett túl a megengedett, áhított dolgokon."),
    E("ENG", "8.17", "to erase from their minds the last traces of desire which had not passed the stage of eager discussion.", "to erase from their souls the last traces of a desire which had never gone beyond coveted permissible things."),
    # «فقام النبى مصليا بالناس ثم قال»
    E("HUN", "8.18", "Erre a Próféta (ﷺ) kiállt az emberek közé, és így szólt:", "Erre a Próféta (ﷺ) imát vezetett az embereknek, majd így szólt:"),
    E("ENG", "8.18", "Upon this, the Prophet (ﷺ) stood up amid the people and said:", "Upon this, the Prophet (ﷺ) stood up and led the people in prayer, then said:"),
    # «ومعاذ راكب، ورسول الله ﷺ يمشى تحت راحلته»
    E("HUN", "8.19", "és lova mellett gyalogolt, miközben az Jemenbe indult.", "és gyalog ment Mu'ādh hátasa mellett, miközben az Jemenbe indult."),
    E("ENG", "8.19", "and walked beside his horse as he was leaving for Yemen.", "and walked beside Mu'ādh's mount as he was leaving for Yemen."),
    # «دجالان»
    E("HUN", "8.20", "két trónkövetelő jelent meg", "két szélhámos jelent meg"),
    E("ENG", "8.20", "There appeared two pretenders in the Banu Ḥanifah", "There appeared two impostors in the Banu Ḥanifah"),
    # أبو دجانة → Dujānah
    E("HUN", "8.21", "miután Abū Dajānahot bízta meg", "miután Abū Dujānahot bízta meg"),
    E("ENG", "8.21", "having appointed Abū Dajānah to be in charge", "having appointed Abū Dujānah to be in charge"),
    E("HUN", "8.21b", "„Abū Dajānah al Sa'idīt tette meg", "„Abū Dujānah al-Sā'idīt tette meg"),
    E("ENG", "8.21b", "\"He made Abū Dajānah al Sa'idī the one in charge", "\"He made Abū Dujānah al-Sā'idī the one in charge"),
    # AR author slip «دم ربيعة بن الحارث» (ḥadīth: Ibn Rabī'ah) — keep + translator's note per policy
    E("HUN", "8.22", "Rabī'ah ibn al Ḥārith ibn 'Abdul Muṭṭālib vére, akit a Banū Layth nevelt fel,", "Rabī'ah ibn al Ḥārith ibn 'Abdul Muṭṭālib vére [így az arab eredetiben; a hadísz hiteles változataiban Rabī'ah fiáé — maga Rabī'ah túlélte a Prófétát — a ford.], akit a Banū Layth nevelt fel,"),
    E("ENG", "8.22", "the blood of Rabi'ah ibn al Ḥārith ibn 'Abdul Muṭṭālib, who was fostered", "the blood of Rabi'ah ibn al Ḥārith ibn 'Abdul Muṭṭālib [thus in the Arabic original; in the authentic versions of the ḥadīth it is the blood of Rabī'ah's son — Rabī'ah himself outlived the Prophet — translator's note], who was fostered"),
    # Prophet's tail after Q9:37 «ويحرموا ما أحل الله»
    E("HUN", "8.23", "így megengedik azt, amit Allah megtiltott.) (Korán 9: 37)", "így megengedik azt, amit Allah megtiltott.) (Korán 9: 37) — „…és megtiltják azt, amit Allah (ﷻ) megengedett.\""),
    E("ENG", "8.23", "so they allow that which Allah has forbidden.) (Qur'ān 9: 37)", "so they allow that which Allah has forbidden.) (Qur'ān 9: 37) — \"…and forbid that which Allāh (ﷻ) has permitted.\""),
    # Farwah: «لما قدم للقتل» / «بلغ سراة المسلمين»
    E("HUN", "8.24", "Azt mondják, hogy amikor felakasztani készültek, ezt a verspárt mondta el:\n\n*Mondjátok meg a muszlimok fejének,", "Azt mondják, hogy amikor kivégzésre vezették, ezt a verset mondta el:\n\n*Mondjátok meg a muszlimok előkelőinek,"),
    E("ENG", "8.24", "It is said that when he was about to be hanged he recited this couplet of poetry: \"Tell the head of the Muslims that I have surrendered to my Lord my bones and my blood.\"",
      "It is said that when he was brought forward to be killed he recited this verse:\n\n*Tell the nobles of the Muslims that I have surrendered to my Lord my bones and my blood.*"),
]
