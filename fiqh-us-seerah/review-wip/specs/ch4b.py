# Ch4 part 2 (A Próféta hidzsrája → Letelepedés) — see opus55-findings.md "Ch4 part 2"
# (fn14 misanchor + dropped p.126 fn(١) and p.129 Abū Nu'aym fn are left for the footnote-restoration phase)
from apply import E

HUN_SIRMAH_OLD = "Egy madīnai költő mondta: Mintegy tíz évig élt a Quraish között, azon tűnődve, talál-e valaha barátot vagy nyájas embert. Messziről jött zarándokokhoz szólt, mégsem látott senkit, aki menedéket adna neki vagy megértené. Amikor aztán hozzánk jött, és elméje eltökélt volt — örvendezve és elégedetten Taybában (Medinában), a zsarnok pedig messze, nem félve többé akaratától, és ő sem félve az emberek közül való lázadótól —, feláldoztuk érte törvényes vagyonunkat és önmagunkat háború és béke idején. Ellenségeivé lettünk minden ellenségének, még ha kebelbarátaink voltak is; és tudtuk, hogy nincs más Úr Allahon (ﷻ) kívül, és Allah (ﷻ) Könyve a mi egyetlen vezetőnk."
HUN_SIRMAH_NEW = ("Egy medinai költő mondta:\n\n"
    "*Tíz-egynéhány évet töltött a Quraish között, emlegetve: bárcsak találna barátot, segítőt!*\n\n"
    "*A vásárok zarándokainak ajánlotta magát, de nem látott senkit, aki befogadná, sem senkit, aki megértené.*\n\n"
    "*Amikor aztán hozzánk jött, és vándorútja véget ért, boldogan és elégedetten élt Ṭaybában,*\n\n"
    "*és nem kellett többé tartania sem távoli zsarnok elnyomásától, sem az emberek közül való támadótól.*\n\n"
    "*Vagyonunk javát áldoztuk érte, és önmagunkat is — a csatában és a kölcsönös segítségben;*\n\n"
    "*ellenségei lettünk mindenkinek, aki ellensége volt, még ha hű kebelbarátunk volt is,*\n\n"
    "*és tudjuk, hogy nincs más Úr Allahon (ﷻ) kívül, és hogy Allah (ﷻ) Könyve lett a vezetőnk.*")
ENG_SIRMAH_OLD = "A poet from Madīnah said: He had lived with the Quraish for about ten years, wondering if he would ever meet a friend or a pleasant man. He spoke to the pilgrims from afar, yet saw no-one to give him shelter or understand. So when he came to us and his mind was made up, being joyful and pleased at Taybah (Madīnah), and the tyrant far away no longer fearing his will, and he not fearing a rebel from the mankind, we sacrificed our lawful wealth for him and ourselves in times of war and peace. We became foes of his enemies, all of them, even though they had been our bosom friends, and we knew that there was no Lord save Allāh (ﷻ), and the Book of Allāh (ﷻ) was our only guide."
ENG_SIRMAH_NEW = ("A poet from Madīnah said:\n\n"
    "*He stayed among the Quraish some ten-odd years, reminding them, hoping to meet a friend and helper;*\n\n"
    "*he offered himself to the pilgrims at the fairs, but saw none to shelter him and none to heed.*\n\n"
    "*Then when he came to us and his journeying came to rest, he became happy and content in Ṭaybah,*\n\n"
    "*no longer fearing the oppression of a distant tyrant, nor fearing any aggressor among men.*\n\n"
    "*We gave him the best of our wealth, and ourselves too, in battle and in mutual support;*\n\n"
    "*we are the enemies of whoever among all men is his enemy, even if he be a sincere, dear friend,*\n\n"
    "*and we know that there is no Lord but Allāh (ﷻ), and that the Book of Allāh (ﷻ) has become our guide.*")

EDITS = [
    E("HUN", "4.2102", "»Allah (ﷻ) megparancsolta nekem, hogy elinduljak és kivándoroljak.«", "»Allah (ﷻ) megengedte nekem, hogy elinduljak és kivándoroljak.«"),
    E("ENG", "4.2102", "\"Allāh (ﷻ) has ordered me to leave and migrate.\"", "\"Allāh (ﷻ) has permitted me to leave and migrate.\""),
    E("HUN", "4.2160", "Aztán teljes iramban engedték a hátasokat.\n", "Aztán teljes iramban engedték a hátasokat, és nappalt éjszakához toldva haladtak.\n\n*A keleti szél hasadéka [a messzeség] nyelte el a tevék mellét, s ezután senki sem tudta, merre tartanak.*\n"),
    E("ENG", "4.2160", "Then they let the mounts go at full speed.\n", "Then they let the mounts go at full speed, joining day to night.\n\n*The rent of the east wind [the far distance] swallowed the breasts of the camels, and after that no one knew where they were heading.*\n"),
    E("HUN", "4.2162", "Amikor Madhlaj körzete mellett haladtak el,", "Amikor a Banū Mudlij szállásai mellett haladtak el,"),
    E("ENG", "4.2162", "When they (the Makkans) passed by the district of Madhlaj", "When they passed by the encampment of the Banū Mudlij"),
    E("HUN", "4.2180", "Az utazók rászoktak a déli pihenőre bármilyen árnyékban; és a mélyen fekvő vidékeken, ahol minden árnyékot vet rájuk, amikor a nap delelőn áll, az elernyedt utazók összeszedik magukat, hogy szembenézzenek a kiszáradással és az álmossággal.",
      "Az utazók rászoktak, hogy a déli pihenőre bármilyen árnyékba húzódjanak, a lapályokon, ahol delente mindennek a talpa alatt van az árnyéka; majd amikor a nap nyugovóra hajlik, a fáradt hátasok újra útnak indulnak, dacolva a kiszáradással és az álmossággal."),
    E("ENG", "4.2180", "Travellers have developed the habit of taking a siesta under any shade, and in low lying lands where everything casts a shadow on them when the sun is in deadline, the languid travellers stir themselves to face the dehydration and sleepiness.",
      "Travellers have developed the habit of taking their midday rest in any shade, in low-lying lands where at noon everything stands on its own shadow; then, when the sun declines towards setting, the weary mounts move on again, battling dehydration and sleepiness."),
    E("HUN", "4.2186", "Abū Na'im elbeszéli,", "Abū Nu'aym elbeszéli,"),
    E("ENG", "4.2186", "Abū Na'im narrates", "Abū Nu'aym narrates"),
    E("HUN", "4.2188", "Nálad keresek menedéket kegyed megvonásától és bosszúd hirtelenségétől, áldásaid elvételétől és haragod eljövetelétől. És nincs erő,", "Nálad keresek menedéket kegyed megvonásától és bosszúd hirtelenségétől, áldásaid elvételétől és haragod eljövetelétől. Hozzád fordulok, hogy elnyerjem tetszésedet, ahogy csak tőlem telik. És nincs erő,"),
    E("ENG", "4.2188", "and the coming of Your wrath. And there is no power or might save in you.\"", "and the coming of Your wrath. To You I turn, seeking Your pleasure, as best I can. And there is no power or might save in You.\""),
    E("HUN", "4.2196", "*Megpihentek e vidéken, majd továbbutaztak. És sikeres az, aki Mohamed (ﷺ) társává lesz.\"*", "*Jámborsággal szálltak meg nála, majd továbbutaztak. És sikeres az, aki Mohamed (ﷺ) társává lesz.*\n\n*Örüljenek Ka'b fiai leányuk szállásának, amelynek ülőhelye a hívőknek lesben álló őrhely!\"*"),
    E("ENG", "4.2196", "*They stayed in the area and then travelled on. And successful is he who becomes Muhammad's (ﷺ) Companion.\"*", "*They alighted there in righteousness and then travelled on. And successful is he who becomes Muhammad's (ﷺ) Companion.*\n\n*Let the sons of Ka'b rejoice in their maiden's abode, whose seat is a watchpost for the believers!\"*"),
    E("HUN", "4.2204", "A hívás tizenharmadik évében, Rabi'i 12-én", "A hívás tizenharmadik évében, Rabī' al-Awwal 12-én"),
    E("ENG", "4.2204", "On 12 Rabi'i in the thirteenth year of the call,", "On 12 Rabī' al-Awwal in the thirteenth year of the call,"),
    E("HUN", "4.2204b", "amikor az egyik zsidó, aki a maga dolgáért mászott fel egy dombra,", "amikor az egyik zsidó, aki a maga dolgáért felment egyik erődtornyukra,"),
    E("ENG", "4.2204b", "when one of the Jews, who had climbed up a hillock for his own reasons,", "when one of the Jews, who had climbed one of their fortified towers for his own reasons,"),
    E("HUN", "4.2206", "Ott jön a ti emberetek! Ott a nagyapátok, akire vártok!\"", "Ott jön a ti emberetek! Itt a szerencsétek, akire vártok!\""),
    E("ENG", "4.2206", "There is your man now arriving! There is your grandfather whom you are awaiting!\"", "There is your man now arriving! Here is your good fortune which you have been awaiting!\""),
    E("HUN", "4.2208", "Al-Barra' (رضي الله عنه) mondta:", "Al-Barā' (رضي الله عنه) mondta:"),
    E("ENG", "4.2208", "Al-Barra' (رضي الله عنه) said:", "Al-Barā' (رضي الله عنه) said:"),
    E("HUN", "4.2222", "ezt kérve *Kafūrtól*: „Abul Misk, maradt-e valami a pohárban, ami az enyém lehet? Rövid idő múlva meggazdagszom, és akkor te iszol.\"", "ezt kérve *Kāfūrtól*: „Abū al-Misk, maradt-e valami a pohárban, ami az enyém lehet? Hiszen régóta dalolok [dicséretedet], te pedig iszol!\""),
    E("ENG", "4.2222", "by asking *Kafūr*: \"Abul Misk, is there anything left in the cup that I can have? I shall become rich in a short while, and then you will drink.\"", "by asking *Kāfūr*: \"Abū al-Misk, is there anything left in the cup that I can have? For I have long been singing [your praises] while you drink!\""),
    E("ENG", "4.2222b", "how he travelled from Syria to Egyt and", "how he travelled from Syria to Egypt and"),
    E("HUN", "4.2238", HUN_SIRMAH_OLD, HUN_SIRMAH_NEW),
    E("ENG", "4.2238", ENG_SIRMAH_OLD, ENG_SIRMAH_NEW),
    # footnotes
    E("HUN", "4.f1a", "Aḥmad valóban elbeszélte Al-Barra ibn 'Azib tekintélyére hivatkozva,", "Aḥmad valóban elbeszélte Al-Barā' ibn 'Āzib tekintélyére hivatkozva,"),
    E("ENG", "4.f1a", "Aḥmad narrated on the authority of Al-Barra ibn 'Azib", "Aḥmad narrated on the authority of Al-Barā' ibn 'Āzib"),
    E("HUN", "4.f1b", "Al Haythami is elbeszéli Abū Y'ala tekintélyére hivatkozva, és azt mondja, lánca erős. Aḥmad láncában azonban ott van Yazīd ibn Abi Ziyāda,", "Al-Haythamī Abū Ya'lā [gyűjteményére] is visszavezeti, és azt mondja, lánca erős. Aḥmad láncában azonban ott van Yazīd ibn Abī Ziyād,"),
    E("ENG", "4.f1b", "Al Haythami also narrates it on the authority of Abū Y'ala and says that its chain is strong. However, in Aḥmad's chain there is Yazīd ibn Abi Ziyāda,", "Al-Haythamī also attributes it to [the collection of] Abū Ya'lā and says that its chain is strong. However, in Aḥmad's chain there is Yazīd ibn Abī Ziyād,"),
    E("HUN", "4.f11a", "Qābūs ibn Abū Zibyan útján,", "Qābūs ibn Abī Ẓabyān útján,"),
    E("ENG", "4.f11a", "Qābūs ibn Abū Zibyan from his father", "Qābūs ibn Abī Ẓabyān from his father"),
    E("HUN", "4.f11b", "E kijelentésben van kétség, mivel Al-Dhahabi említette Abū Zibyant *Al Mizanjában*, és közölte, hogy Ibn Ḥibbān ezt mondja róla: rossz az emlékezete. Olyan dolgokat közöl apjától, amelyeknek nincs alapjuk. Olykor *marfū'*-ként közli, ami mursal, és musnadként, ami *mauqūf*.",
      "Ez azonban kétséges, mert Qābūs ibn Abī Ẓabyānt Al-Dhahabī felvette az *Al-Mīzān*ba, és idézte Ibn Ḥibbānt, aki ezt mondja róla: rossz az emlékezete; egyedül közöl apjától olyan dolgokat, amelyeknek nincs alapjuk; olykor *marfū'*-ként közli, ami mursal, és musnadként, ami *mauqūf*. Ezért mondja róla Al-Ḥāfiẓ [Ibn Ḥajar] a *Taqrīb*ban: „gyengeség van benne\"."),
    E("ENG", "4.f11b", "There is doubt in this statement since Al-Dhahabi has mentioned Abū Zibyan in his *Al Mizan*, and has reported that Ibn Ḥibbān, says about him: He has a bad memory. He reports things from his father which have no basis. Sometimes he would report as *marfū'* what is mursal and as musnad what is *mauqūf*.",
      "There is doubt about this, since Al-Dhahabī included Qābūs ibn Abī Ẓabyān in his *Al-Mīzān* and reported that Ibn Ḥibbān says about him: He has a bad memory; he alone reports things from his father which have no basis; sometimes he would report as *marfū'* what is mursal and as musnad what is *mauqūf*. For this reason Al-Ḥāfiẓ [Ibn Ḥajar] says of him in the *Taqrīb*: \"There is weakness in him.\""),
    E("HUN", "4.f13", "Ibn Ḥarir azonban", "Ibn Jarīr azonban"),
    E("ENG", "4.f13", "However, Ibn Ḥarir named him", "However, Ibn Jarīr named him"),
    E("HUN", "4.f14", "A láncban ott van 'Uthmān Al-Jazari, akiről a szerző azt mondta, jó.", "A láncban ott van 'Uthmān Al-Jazarī; a szerző e láncot jónak (ḥasan) minősítette."),
    E("ENG", "4.f14", "The chain contains 'Uthmān Al-Jazari which the author said is good.", "The chain contains 'Uthmān Al-Jazarī; the author graded this chain as good (ḥasan)."),
    E("HUN", "4.f16", "¹⁶ Isnādja zavaros.", "¹⁶ Isnādja mu'ḍal (két vagy több egymást követő láncszem hiányzik belőle)."),
    E("ENG", "4.f16", "¹⁶ Its isnād is mixed up.", "¹⁶ Its isnād is mu'ḍal (two or more consecutive links are missing)."),
    E("HUN", "4.f17", "Ezt a hadíszt *mursalként* elbeszélve találtam Al-Ḥākimnál Hishām Ibn Habīsh tekintélyére hivatkozva, és azt mondta, lánca hiteles. Ez azonban kétséges.",
      "Később a hadíszt összefüggő lánccal (*mawṣūl*) is megtaláltam: Al-Ḥākim beszélte el Hishām ibn Ḥubaysh hadíszaként, és azt mondta, lánca hiteles, Al-Dhahabī pedig egyetértett vele. Amit mondtak, az azonban kétséges."),
    E("ENG", "4.f17", "I found this Ḥadīth narrated as *Mursal* by Al-Ḥākim on the authority of Hishām Ibn Habīsh, and he said it had a sound chain. However, there is doubt about this.",
      "Later I found this Ḥadīth narrated with a connected chain (*mawṣūl*) by Al-Ḥākim from the Ḥadīth of Hishām ibn Ḥubaysh; he said it had a sound chain, and Al-Dhahabī agreed. However, there is doubt about what they said."),
]
