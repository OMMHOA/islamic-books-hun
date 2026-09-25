# Ch7 part 7 (hátramaradottak → ḍirār → küldöttségek → Abū Bakr zarándoklata → Ḍamām → Najrān) + ch7 footnotes
# see opus55-findings.md "Ch7 part 7" / "Ch7 footnotes"; AR pp.316–332
from apply import E

EDITS = [
    # «فجاء المخلفون… يحلفون له، وكانوا بضعة وثمانين رجلاً فقبل منهم… علانيتهم، وبايعهم، واستغفر لهم، ووكل سرائرهم إلى الله»
    E("HUN", "7g.1", "Jöttek a képmutatók, előadták mentségeiket, és hűséget esküdtek neki. Mintegy nyolcvan férfit tettek ki. Ő elfogadta mentségeiket, Allah bocsánatát kérte számukra, és lelküket Allahra (ﷻ) bízta.",
      "Jöttek a hátramaradottak, mentegetőztek előtte, és esküdöztek neki; nyolcvan-egynéhány férfi volt. Ő elfogadta tőlük, amit nyíltan mondtak, hűségesküt vett tőlük, Allah bocsánatát kérte számukra, és rejtett szándékaikat Allahra (ﷻ) bízta."),
    E("ENG", "7g.1", "The hypocrites came and offered their excuses and swore allegiance to him. They comprised about eighty men. He accepted their excuses, asked Allāh's forgiveness for them and left their souls to Allāh (ﷻ).",
      "Those who had stayed behind came, excusing themselves to him and swearing oaths to him; they were eighty-odd men. He accepted their outward professions, took their pledge of allegiance, asked Allāh's forgiveness for them and left their secrets to Allāh (ﷻ)."),
    # Ka'b: dropped first half «إن حدثتك اليوم حديث كذب ترضى به عنى، ليوشكن الله أن يسخطك على»
    E("HUN", "7g.2", "Ám Allahra (ﷻ), tudom: ha ma igazat mondok neked, és megharagszol rám, remélhetem, hogy Allah (ﷻ) megbocsát nekem.",
      "Ám Allahra (ﷻ), tudom: ha ma hazugságot mondanék neked, amellyel elnyerném tetszésedet, Allah (ﷻ) hamarosan ellenem fordítaná haragodat; ha viszont igazat mondok neked, és megharagszol rám miatta, remélhetem, hogy Allah (ﷻ) megbocsát nekem."),
    E("ENG", "7g.2", "However, by Allāh (ﷻ), I know that if I speak the truth to you and you are angry with me, then I am hopeful that Allāh (ﷻ) will forgive me.",
      "However, by Allāh (ﷻ), I know that if I told you a lie today to win your favour, Allāh (ﷻ) would soon turn your anger against me; whereas if I speak the truth to you and you are angry with me for it, then I am hopeful that Allāh (ﷻ) will forgive me."),
    # «أوفى على جبل سلع» / «فأوفى على ذروة الجبل»
    E("HUN", "7g.3", "egy közeli domb felől hangot hallottam, amint valaki torkaszakadtából kiáltja:", "hangot hallottam: valaki felhágott a Sal' hegyre, és torkaszakadtából kiáltotta:"),
    E("ENG", "7g.3", "I heard the voice of someone shouting from a nearly hill at the top of his voice:", "I heard the voice of someone who had climbed Mount Sal' shouting at the top of his voice:"),
    E("HUN", "7g.4", "Ám egy másik, Aslam törzsebeli, felsietett a domb tetejére,", "Ám egy másik, Aslam törzsbeli férfi felsietett a hegy tetejére,"),
    E("ENG", "7g.4", "However, another from Aslam hastened to the top of the hill", "However, another from Aslam hastened to the top of the mountain"),
    E("ENG", "7g.4b", "from the time I said this is to the Prophet (ﷺ)", "from the time I said this to the Prophet (ﷺ)"),
    # Q9:117–119 is quoted with «إلى قوله تعالى»
    E("HUN", "7g.5", "(Allah kegyesen odafordult a Prófétához és a muhādzsirokhoz meg az anṣārokhoz. Ó, ti, akik hisztek!", "(Allah kegyesen odafordult a Prófétához és a muhādzsirokhoz meg az anṣārokhoz… Ó, ti, akik hisztek!"),
    E("ENG", "7g.5", "(Allah has turned in mercy to the Prophet and to the *muhajirīn* and Anṣār. O you who believe!", "(Allah has turned in mercy to the Prophet and to the *muhajirīn* and Anṣār… O you who believe!"),
    # «وكان تخلفنا ـ أيها الثلاثة ـ عن أمر أولئك… ﴿وَعَلَى الثَّلَاثَةِ الَّذِينَ خُلِّفُوا﴾ وليس الذى ذكر الله مما خلفنا عن الغزو…»
    E("HUN", "7g.6", "„Mi hárman a hátramaradásban azokkal szemben említtettünk, akiknek mentségeit a Próféta (ﷺ) elfogadta, amikor hűséget esküdtek neki. Elfogadta hűségesküjüket, és bocsánatot kért számukra. A mi ügyünket azonban elhalasztotta, míg Allah (ﷻ) ítéletet nem mondott (a három hátramaradott). Amit Allah (ﷻ) itt említett, nem a csatától való elmaradásunk oka volt. Valójában azt jelentette, hogy ügyünk későbbre halasztatott, mint azoké, akiknek mentségei elfogadtattak.\"¹⁰⁷",
      "„Minket, hármunkat, elkülönítettek azoktól, akiktől a Próféta (ﷺ) elfogadta [mentségüket], amikor megesküdtek neki: tőlük hűségesküt vett, és bocsánatot kért számukra, a mi ügyünket viszont elhalasztotta, míg Allah (ﷻ) nem döntött felőle. Erről mondta Allah (ﷻ): (És a háromra is, akik hátrahagyattak) (Korán 9: 118). Amit Allah (ﷻ) itt említ, nem arra vonatkozik, hogy elmaradtunk a hadjáratból, hanem arra, hogy minket hátrahagyott, és ügyünket elhalasztotta azokéhoz képest, akik megesküdtek neki, mentegetőztek előtte, és ő elfogadta tőlük.\"¹⁰⁷"),
    E("ENG", "7g.6", "\"The three of us remaining behind was in regard to the others whose excuses the Prophet (ﷺ) accepted when they swore allegiance to him. He accepted their pledge of allegiance and asked for forgiveness for them. However, he postponed our case until Allāh (ﷻ) passed His judgement (the three who were left behind). What Allāh (ﷻ) mentioned here was not the reason for our staying away from the battle. What he really meant was that our case was deferred to a later date beyond that for those whose excuses were accepted.\"¹⁰⁷",
      "\"We three were kept apart from those whose [excuses] the Prophet (ﷺ) accepted when they swore to him: he took their pledge of allegiance and asked forgiveness for them, but he deferred our case until Allāh (ﷻ) decided it. That is why Allāh (ﷻ) said: (And to the three who were left behind) (Qur'ān 9: 118). What Allāh (ﷻ) mentions here does not refer to our staying behind from the campaign; it refers to His leaving us behind and deferring our case apart from those who swore to him, excused themselves to him, and had their excuses accepted.\"¹⁰⁷"),
    # ḍirār: «فتصلى لنا فيه» (no "bless"); «إن شاء الله»; «أمرهما أن يحرقاه ويهدماه… يحملان الشعل الحارقة… فروا مذعورين لمرأى اللهب»
    E("HUN", "7g.7", "és szeretnék, ha eljönne imádkozni bele és megáldaná.", "és szeretnék, ha eljönne, és imádkozna nekik benne."),
    E("ENG", "7g.7", "and would like him to come and pray in it and bless it.", "and would like him to come and pray in it for them."),
    E("HUN", "7g.8", "hogy visszatérte után imádkozik benne, ha Isten akarja.¹⁰⁸", "hogy visszatérte után imádkozik benne, ha Allah akarja.¹⁰⁸"),
    E("ENG", "7g.8", "he had promised to pray in it on his return, God willing.¹⁰⁸", "he had promised to pray in it on his return, if Allāh willed.¹⁰⁸"),
    E("HUN", "7g.9", "elküldte két társát, hogy rombolják földig a mecsetet. Tűzifát vittek magukkal, és a lángok láttán a képmutatók tudták, hogy cselszövésük megbukott.",
      "elküldte két társát, és megparancsolta nekik, hogy gyújtsák fel és rombolják le a mecsetet. A két társ égő fáklyákkal érkezett, és nekiláttak a pusztításnak, miközben a mecset népe még bent volt; ők a lángok láttán rémülten elmenekültek."),
    E("ENG", "7g.9", "he sent two of his Companions to raze the mosque to the ground. They took firewood and at the sight of the flames the hypocrites knew that their plot had failed.",
      "he sent two of his Companions and ordered them to burn and demolish the mosque. The two came carrying burning torches and set about destroying it while its people were inside; they fled in terror at the sight of the flames."),
    # «فاجتمع عمرو بن أمية بعبد يا ليل… وقال له: إنه قد نزل بنا أمر ليست معه هجرة… ورأت ثقيف أن تبعث وفدها»
    E("HUN", "7g.10", "Így 'Āmir ibn Umayyah négyszemközti beszélgetést folytatott 'Abd Yā Layl ibn 'Amrral, és sikerült meggyőznie, hogy küldöttséget kell meneszteni a Prófétához (ﷺ).",
      "Így 'Amr ibn Umayyah felkereste 'Abd Yā Layl ibn 'Amrt, és így szólt hozzá: „Olyan dolog szakadt ránk, amely mellett nincs helye a haragtartásnak. Láttad, mi lett ennek az embernek az ügyéből: az arabok mind felvették az iszlámot, nektek pedig nincs erőtök harcolni ellenük. Gondoljátok hát meg a dolgotokat!\" A Thaqīf úgy döntött, hogy küldöttséget meneszt a Prófétához (ﷺ)."),
    E("ENG", "7g.10", "Thus 'Āmir ibn Umayyah had a tete-a-tete with 'Abd Yā Layl ibn 'Amr, and managed to convince him that a deputation should be sent to the Prophet (ﷺ).",
      "Thus 'Amr ibn Umayyah met with 'Abd Yā Layl ibn 'Amr and said to him: \"Something has befallen us that leaves no room for estrangement between us. You have seen what has become of this man's cause: all the Arabs have accepted Islām, and you have no strength to fight them. So consider your position.\" The Thaqīf decided to send a deputation to the Prophet (ﷺ)."),
    E("ENG", "7g.10b", "They debated long with Prophet (ﷺ) in the desires to gain the concession", "They debated long with the Prophet (ﷺ) in the desire to gain the concession"),
    E("ENG", "7g.10c", "that he should not destory Al-Lāt", "that he should not destroy Al-Lāt"),
    # «ولا مراء فى أن»
    E("HUN", "7g.11", "Nem hazugság, hogy a Thaqīf meghódolása", "Kétségtelen, hogy a Thaqīf meghódolása"),
    E("ENG", "7g.11", "It is no lie that the surrender of the Thaqīf and the their acceptance of Islām, were a great gain", "There is no doubt that the surrender of the Thaqīf and their acceptance of Islām were a great gain"),
    # Sūrat al-Tawbah unified (Barā'ah kept where the author says «براءة»)
    E("HUN", "7g.12", "A Sūrah al Taubah sok oldalnyi megjegyzést", "A Sūrat al-Tawbah sok oldalnyi megjegyzést"),
    E("ENG", "7g.12", "Sūrah al Taubah contains many pages", "Sūrat al-Tawbah contains many pages"),
    E("HUN", "7g.13", "kinyilatkoztatott a Sūrat al tawbah,", "kinyilatkoztatott a Sūrat al-Tawbah,"),
    E("ENG", "7g.13", "Sūrat *al tawbah* was revealed", "Sūrat al-Tawbah was revealed"),
    E("HUN", "7g.14", "a Sūrah al Tawbah elején foglalt törvényeket", "a Sūrat al-Tawbah elején foglalt törvényeket"),
    E("ENG", "7g.14", "the early part of Sūrah *al Tawbah*", "the early part of Sūrat al-Tawbah"),
    # العضباء; «وأجهزت على الوثنية فى بلادهم»; زيد بن يثيع
    E("HUN", "7g.15", "'Alī (رضي الله عنه) Al-'Adhā hátán,", "'Alī (رضي الله عنه) Al-'Aḍbā' hátán,"),
    E("ENG", "7g.15", "'Alī (رضي الله عنه) left on Al-'Adhā,", "'Alī (رضي الله عنه) left on Al-'Aḍbā',"),
    E("HUN", "7g.16", "amely részletesen velük foglalkozott, és kiadta nekik a pogányságot országukban.", "amely részletesen velük foglalkozott, és végzett a pogánysággal országukban."),
    E("ENG", "7g.16", "which dealt with them in detail and delivered them to paganism in their country.", "which dealt with them in detail and finished off paganism in their land."),
    E("HUN", "7g.17", "Zayd ibn Yafi' mondta", "Zayd ibn Yuthay' mondta"),
    E("ENG", "7g.17", "Zayd ibn Yafi' said", "Zayd ibn Yuthay' said"),
    # Q9:1–3 truncated after "better for you"
    E("HUN", "7g.18", "Ha tehát megbánjátok, jobb az nektek.) (Korán 9: 1–3)", "Ha tehát megbánjátok, jobb az nektek; ha pedig hátat fordítotok, tudjátok meg, hogy nem menekülhettek Allah elől. És hirdesd azoknak, akik hitetlenek, a fájdalmas büntetést!) (Korán 9: 1–3)"),
    E("ENG", "7g.18", "So, if you repent, It will be better for you.) (Qur'ān 9: 1-3)", "So, if you repent, it will be better for you; but if you turn away, then know that you cannot escape Allāh. And give tidings to those who disbelieve of a painful punishment.) (Qur'ān 9: 1-3)"),
    # «أيكم ابن عبدالمطلب؟ … أنا ابن عبدالمطلب»
    E("HUN", "7g.19", "„Melyikőtök 'Abdul Muṭṭalib?\"", "„Melyikőtök 'Abdul Muṭṭalib fia?\""),
    E("HUN", "7g.20", "„Én vagyok 'Abdul Muṭṭalib.\"", "„Én vagyok 'Abdul Muṭṭalib fia.\""),
    E("ENG", "7g.19", "\"Which of you is 'Abdul Muṭṭalib.\"", "\"Which of you is the son of 'Abdul Muṭṭalib?\""),
    E("ENG", "7g.20", "\"I am 'Abdul Muṭṭalib.\"", "\"I am the son of 'Abdul Muṭṭalib.\""),
    # fn113 anchor: AR fn(١) sits on «دخل الجنة»
    E("HUN", "7g.21", "belép a Dzsannába.\"\n", "belép a Dzsannába.\"¹¹³\n"),
    E("HUN", "7g.21b", "Al-Lāt és Al-'Uzzā!\"¹¹³", "Al-Lāt és Al-'Uzzā!\""),
    E("ENG", "7g.21", "he shall enter *Jannah*.\"\n", "he shall enter *Jannah*.\"¹¹³\n"),
    E("ENG", "7g.21b", "Al-Lāt and Al-Uzza!\"¹¹³", "Al-Lāt and Al-'Uzzā!\""),
    # «اتق البرص، اتق الجذام، اتق الجنون»
    E("HUN", "7g.22", "„Csillapodj, Ḍamām! Félj a leprától! Félj az őrülettől!\"", "„Csillapodj, Ḍamām! Félj a fehérfoltosságtól! Félj a leprától! Félj az őrülettől!\""),
    E("ENG", "7g.22", "\"Steady, Ḍamām. Fear leprosy. Fear insanity!\"", "\"Steady, Ḍamām! Fear leukoderma! Fear leprosy! Fear insanity!\""),
    # «معاذ الله أن أعبد غير الله أو آمر بعبادة غيره»
    E("HUN", "7g.23", "„Allah (ﷻ) mentsen attól, hogy engem imádjanak Mellette, vagy hogy bárki mást Mellette imádatra rendeljek.", "„Allah (ﷻ) mentsen attól, hogy mást imádjak Allahon kívül, vagy hogy más imádatát parancsoljam!"),
    E("ENG", "7g.23", "\"Allāh (ﷻ) forbid that I should be worshipped besides Him, or that I should order anyone beside Him to be worshipped.", "\"Allāh (ﷻ) forbid that I should worship other than Allāh, or order the worship of another than Him!"),
    # «فأوجسوا خيفة… من يدرى؟ قد يكون محمد صادقًا… فلماذا يبتهلون إلى الله أن يمحقهم؟ … إن هم قبلوا هذه المباهلة. ثم خلصوا نجيا»
    E("HUN", "7g.24", "A küldöttség tudta, hogy igaza van abban az állításában, hogy Jézus hozzá hasonló ember volt, és hogy ők tévedtek, amikor istenséget tulajdonítottak neki. Miért hívnák hát le magukra Isten átkát?",
      "A najrāni küldöttség meghallgatta ezt a javaslatot, és félelem fogta el őket attól, hogy elfogadják. Ki tudja? Lehet, hogy Mohamednek (ﷺ) igaza van abban, hogy Jézus hozzá hasonló ember, ők pedig tévednek, amikor istenséget tulajdonítanak neki. Miért könyörögnének hát Allahhoz, hogy elpusztítsa őket?"),
    E("ENG", "7g.24", "The deputation knew that he were right in his claim that Jesus was human like himself, and they were mistaken in their attribution of divinity to him. Why should they, then, call down the curse of God on themselves?",
      "The deputation from Najran listened to this proposal and grew afraid of accepting it. Who knows? Muhammad (ﷺ) might be truthful in saying that Jesus was a human being like himself, and they might be deluded in ascribing divinity to him. Why, then, should they pray to Allāh to destroy them?"),
    E("HUN", "7g.25", "és félelmük kiterjedt tulajdon családjaik és gyermekeik sorsára.", "és féltették a pusztulástól tulajdon gyermekeiket és családjaikat, ha elfogadják ezt az átokhívást. Azután félrevonultak, hogy titokban tanácskozzanak."),
    E("ENG", "7g.25", "and their fear extended to the fate of their own families and children.", "and they feared destruction for their own children and families if they accepted this imprecation. Then they withdrew to confer in private."),
    # «وإن كان نبيا مرسلاً فلا عناء، فلن يبقى على وجه الأرض منها شعرة ولا ظفر إلا هلك» (scan p.331 checked)
    E("HUN", "7g.26", "Ha pedig igaz Próféta, nincs miért aggódnunk. Egyetlen hajszálunk vagy körmünk sem maradna e földön pusztulás nélkül (ha imába bocsátkozunk).",
      "Ha pedig küldött próféta, akkor nincs mit tennünk: egyetlen hajszálunk vagy körmünk sem maradna a föld színén pusztulás nélkül [ha átokhívásba bocsátkoznánk vele]."),
    E("ENG", "7g.26", "And if he is a true Prophet then there is no need to worry. Not a single hair or nail of our will remain on this earth without being destroyed (if we engage prayer).",
      "And if he is a Prophet sent [by Allāh], then there is nothing we can do: not a single hair or nail of ours would remain on the face of the earth without being destroyed [if we joined in the imprecation with him]."),
    # dropped «ورجع رسول الله ولم يلاعنهم»
    E("HUN", "7g.27", "így szólt: „Szerencsés hitetlen.\" Szerződést kötött velük,", "így szólt: „Szerencsés hitetlen.\" A Próféta (ﷺ) átokhívás nélkül tért vissza, és szerződést kötött velük,"),
    E("ENG", "7g.27", "he said: \"A fortunate unbeliever.\" He concluded a treaty with them", "he said: \"A fortunate unbeliever.\" The Prophet (ﷺ) went back without the imprecation and concluded a treaty with them"),
    # «ولا يغير أسقف من أسقفيته»
    E("HUN", "7g.28", "sem pap nem mozdíttatik el papságából,", "sem püspök nem mozdíttatik el püspökségéből,"),
    E("ENG", "7g.28", "nor will any priest be changed from his priesthood nor monk form his monasticism,", "nor will any bishop be changed from his bishopric nor monk from his monasticism,"),
    # «بعدما ضمن الحرية الدينية لمن سالمه، وكفوا عنه»
    E("HUN", "7g.29", "miután vallásszabadságot szavatolt mindenkinek, aki kívánta, és tartózkodott a beavatkozástól.", "miután vallásszabadságot szavatolt azoknak, akik békét kötöttek vele, és felhagytak az ellenségeskedéssel."),
    E("ENG", "7g.29", "after guaranteeing religious freedom to whoever desired it and abstain from interference.", "after guaranteeing religious freedom to those who made peace with it and refrained from hostility towards it."),
    # «كاتبوا الأسود العنسى، فسار إليهم ـ وهو أحد المتنبئين ـ ثم رحل عنهم إلى اليمن، فملكها حتى قتلته امرأته وأراحت الأرض منه»
    E("HUN", "7g.30", "Najrān például írt Al-Aswad Al-Ansīnak, aki prófétaságot igényelt magának, és menedéket adott neki. Onnan Jemenbe ment, ahol megalapította uralmát, míg tulajdon felesége meg nem ölte.",
      "Najrān keresztényei például levelet váltottak Al-Aswad al-'Ansīval — az álpróféták egyikével —, aki erre hozzájuk ment; onnan Jemenbe vonult, és uralma alá vetette, míg tulajdon felesége meg nem ölte, és meg nem szabadította tőle a földet."),
    E("ENG", "7g.30", "For example, Najran wrote to Al-Aswad Al-Ansī, who claimed prophethood, and gave him shelter. From there he went to Yemen, where he established his rule until he was killed by his wife.",
      "For example, the Christians of Najran corresponded with Al-Aswad al-'Ansī — one of the false claimants to prophethood — and he went to them; from there he moved on to Yemen, which he ruled until his wife killed him and rid the earth of him."),
    E("HUN", "7g.31", "Al-Aswad Al-Ansī támogatásában", "Al-Aswad al-'Ansī támogatásában"),
    E("ENG", "7g.31", "support of Al-Aswad Al-Ansī", "support of Al-Aswad al-'Ansī"),
    # «بالبعكوكة» + fn «صحيفة هزلية»
    E("HUN", "7g.32", "higgyen például Bu'kūkában.¹²¹", "higgyen például az al-Ba'kūkában.¹²¹"),
    E("ENG", "7g.32", "believe, for instance, in Bu'kūkah.¹²¹", "believe, for instance, in al-Ba'kūkah.¹²¹"),
    E("HUN", "7g.33", "¹²¹ Komédia.", "¹²¹ Szatirikus újság."),
    E("ENG", "7g.33", "¹²¹ A comedy.", "¹²¹ A satirical newspaper."),
    # ---- Ch7 footnotes ----
    # fn5 «قتل نفرًا فوداهم عروة إطفاء للفتنة»
    E("HUN", "7g.f5", "Megölt néhány embert, és 'Urwah a vele való barátsággal simította el a helyzetet.", "Megölt néhány embert, és 'Urwah fizette meg értük a vérdíjat, hogy elfojtsa a viszályt."),
    E("ENG", "7g.f5", "He had killed some people and 'Urwah pacified the situation by befriending him.", "He had killed some people, and 'Urwah paid the blood-money for them to quench the strife."),
    # mu'ḍal (AR «معضلاً» pp.264, 290, 294)
    E("HUN", "7g.f27", "²⁷ Gyenge: Ibn Hishām beszélte el Ibn Isḥāqtól zavaros lánccal.", "²⁷ Gyenge: Ibn Hishām beszélte el Ibn Isḥāqtól, Hishām ibn 'Urwah-tól, *mu'ḍal*ként."),
    E("ENG", "7g.f27", "²⁷ Weak: narrated by Ibn Hishām from Ibn Isḥāq with a muddled chain.", "²⁷ Weak: narrated by Ibn Hishām from Ibn Isḥāq from Hishām ibn 'Urwah as *mu'ḍal*."),
    E("HUN", "7g.f28", "²⁸ Nem hiteles: Al-Wāqidī beszélte el zavaros lánccal, és Al-Wāqidī nem elfogadható.", "²⁸ Nem hiteles: Al-Wāqidī beszélte el *mu'ḍal*ként (lásd Al-Bidāyah, 4/198), és Al-Wāqidī elhagyott (*matrūk*) hagyományozó."),
    E("ENG", "7g.f28", "²⁸ Not authentic: narrated by Al-Wāqidi with a muddled chain, and Al-Wāqidi is not acceptable.", "²⁸ Not authentic: narrated by Al-Wāqidi as *mu'ḍal* (see Al-Bidāyah, 4/198), and Al-Wāqidi is abandoned (*matrūk*)."),
    E("HUN", "7g.f64", "⁶⁴ Hiteles hadísz, Ibn Hishām hagyományozta Ibn Isḥāqtól zavaros lánccal, amelyet Ibn Jarīr tisztázott, bár van benne egy gyenge láncszem.", "⁶⁴ Hiteles hadísz: Ibn Hishām hagyományozta Ibn Isḥāqtól *mu'ḍal*ként, Ibn Jarīr azonban összefüggő lánccal közölte tőle, bár van benne egy gyenge láncszem."),
    E("ENG", "7g.f64", "⁶⁴ A sound Ḥadīth transmitted by Ibn Hishām from Ibn Isḥāq with a muddled chain, which was clarified by Ibn Jarīr, though there is a weak link in it.", "⁶⁴ A sound Ḥadīth transmitted by Ibn Hishām from Ibn Isḥāq as *mu'ḍal*; Ibn Jarīr, however, transmitted it from him with a connected chain, though there is a weak link in it."),
    E("HUN", "7g.f71", "⁷¹ Gyenge: Ibn Isḥāq hagyományozta zavaros lánccal.", "⁷¹ Gyenge: Ibn Isḥāq hagyományozta *mu'ḍal*ként."),
    E("ENG", "7g.f71", "⁷¹ Weak: transmitted by Ibn Isḥāq with a muddled chain.", "⁷¹ Weak: transmitted by Ibn Isḥāq as *mu'ḍal*."),
    E("HUN", "7g.f72", "⁷² Gyenge: Ibn Hishām hagyományozta zavaros lánccal.", "⁷² Gyenge: Ibn Hishām hagyományozta *mu'ḍal* lánccal."),
    E("ENG", "7g.f72", "⁷² Weak: transmitted by Ibn Hishām with a muddled chain.", "⁷² Weak: transmitted by Ibn Hishām with a *mu'ḍal* chain."),
    # fn51 closing «ويغنى عنه ما فى المسند (رقم ٣٥٣٦)…»
    E("HUN", "7g.f51", "ha pedig nem, az első láncban van egy meg nem nevezett láncszem.",
      "ha pedig nem, az első láncban van egy meg nem nevezett láncszem. Helyette elegendő, ami a Musnadban (3536. sz.) áll Ibn 'Abbāstól: a Quraish azt mondta: „Mohamedet (ﷺ) és társait legyengítette Yathrib láza.\" Amikor pedig Allah Küldötte (ﷺ) eljött abban az évben, amelyben 'umrát végeztek, így szólt társaihoz: „Szapora, vállringató léptekkel (*raml*) járjátok körül a Házat, hogy lássák a többistenhívők az erőtöket!\" Amikor így tettek, a Quraish azt mondta: „Nem gyengítette le őket.\" Lánca hiteles; Bukhārī *mu'allaq*ként közölte (8/411)."),
    E("ENG", "7g.f51", "and if it is not, the first chain has a link who is not named.",
      "and if it is not, the first chain has a link who is not named. What is in the Musnad (no. 3536) from Ibn 'Abbās suffices instead: the Quraish said: \"Muhammad (ﷺ) and his Companions have been weakened by the fever of Yathrib.\" When the Messenger of Allāh (ﷺ) came in the year in which they performed the 'umrah, he said to his Companions: \"Walk briskly (*raml*) around the House, so that the polytheists may see your strength.\" When they did so, the Quraish said: \"It has not weakened them.\" Its chain is sound; Bukhārī cited it as *mu'allaq* (8/411)."),
    # fn52 «عند ابن هشام عن [ابن] إسحاق حدثنى عبدالله بن أبى بكر مرسلاً»
    E("HUN", "7g.f52", "⁵² 'Abdullāh ibn Abī Bakr hagyományozza Ibn Isḥāqtól, hogy 'Abdullāh ibn Abī Bakr mursalként beszélte el neki.", "⁵² Ibn Hishāmnál Ibn Isḥāqtól: „'Abdullāh ibn Abī Bakr beszélte el nekem\", mursalként."),
    E("ENG", "7g.f52", "⁵² 'Abdullāh ibn Abī Bakr transmits from Ibn Isḥāq that 'Abdullāh ibn Abī Bakr narrated it to him as mursal.", "⁵² In Ibn Hishām from Ibn Isḥāq: \"'Abdullāh ibn Abī Bakr told me,\" as *mursal*."),
    # fn119 / fn120
    E("HUN", "7g.f119", "¹¹⁹ Gyenge: Ibn Abī Muhammad Al Anṣārī hagyományozta, aki ismeretlen.", "¹¹⁹ Gyenge: Muhammad ibn Isḥāq hagyományozta láncával Ibn 'Abbāstól, ahogyan Ibn Kathīr tafsīrjában áll. Láncában van Muhammad ibn Abī Muhammad, vagyis Al-Anṣārī, akiről Al-Dhahabī azt mondta: „Ismeretlen.\" Ibn Ḥibbān viszont megbízhatónak nyilvánította!"),
    E("ENG", "7g.f119", "¹¹⁹ Weak: transmitted by Ibn Abī Muhammad Al Anṣārī, who is unknown.", "¹¹⁹ Weak: narrated by Muhammad ibn Isḥāq with his chain from Ibn 'Abbās, as in Ibn Kathīr's Tafsīr. In it is Muhammad ibn Abī Muhammad, i.e. Al-Anṣārī, of whom Al-Dhahabī said: \"He is unknown.\" Ibn Ḥibbān, however, declared him reliable!"),
    E("HUN", "7g.f120", "¹²⁰ Ennyi szerepel Ibn Isḥāq fent említett mursal hadíszában. A többit nem találtam nála.", "¹²⁰ Eddig terjed Ibn Isḥāq fent említett mursal hadísza (Muhammad ibn Ja'far ibn al-Zubayrtól). A másik változatot most nem találtam meg lánccal ilyen teljes formában."),
    E("ENG", "7g.f120", "¹²⁰ This much comes in the above-mentioned *mursal* Ḥadīth of Ibn Isḥāq. I have not found the rest of it with him.", "¹²⁰ This much comes in the above-mentioned *mursal* Ḥadīth of Ibn Isḥāq (from Muhammad ibn Ja'far ibn al-Zubayr). The other narration I have not found at present with a chain in this complete form."),
]
