# Ch7 part 5 (Ḥunayn → zsákmány → Anṣār → Hawāzin → Ṭā'if → hazatérés) — see opus55-findings.md "Ch7 part 5"
from apply import E

HUN_ANSAR = ("Ő távozott, és ők szétszéledtek.⁹⁰\n\n"
    "Az anṣārok a hívások történetében egyedülálló példái azoknak a férfiaknak, akiken a nagy üzenetek felépülnek: amikor pedig az üzenet már szilárdan áll a szárán, túljut megpróbáltatásai és terhei napjain, gyümölcsei lecsüngenek, és termése megédesedik, más kezek jönnek, és leszakítják, amit csak kívánnak! S nem érik be ennyivel: még a telepítők kezére is rácsapnak, hogy a lehullott gyümölcsből se keveset, se sokat ne szedhessenek fel!!\n\n"
    "Ezt nem a zsákmány itteni elosztásához fűzzük megjegyzésként — hiszen e bölcs elosztás helyessége világossá vált.\n\n"
    "Ám az anṣārok erényei között — és feltételezve, hogy a vallásért és az emberek iránta való megnyeréséért e világ fölé emelkedtek — megemlítjük, hogy a kormányzás ügyei eltávolodtak tőlük, és mások kaparintották meg, noha ők alkalmasak voltak rá. Még harminc év sem telt el, és már a ṭulaqā' [a Mekka elfoglalásakor szabadon bocsátott egykori ellenségek] kezében volt.\n\n"
    "Kétségtelen, hogy akik egészen Allahnak (ﷻ) szentelték magukat, teljes jutalmukat elnyerik, és hogy a világ dolga túl csekély ahhoz, hogy a hit embere bánkódjék miatta. Mégis megkérdezzük: vajon maguknak az üzeneteknek az érdekét szolgálta-e, hogy mások ilyen előnyt élvezzenek? Vagy az iszlám balszerencséje volt, hogy ilyen fajta uralkodókkal találkozott, akik félreállították az elsőket és a segítőket, a vallás gyeplőjét pedig azok ragadták meg, akik utolsóként léptek be abba, és a legkevésbé értettek hozzá?!")
ENG_ANSAR = ("He left and they dispersed.⁹⁰\n\n"
    "The Anṣār are, in the history of the calls to Allāh, a unique example of the men on whom the great messages are built: then, when the message stands firm on its stem, has passed the days of its trial and burden, and its fruits hang low and its harvest has grown sweet, other hands come and pluck what they please! Nor are they content with that: they even strike the hands of the planters, so that they may not pick up a little or a lot of the fallen fruit!!\n\n"
    "We do not say this as a comment on the distribution of the spoils here, for the wisdom of that sound division has become clear.\n\n"
    "But we mention, among the virtues of the Anṣār — and presuming that they rose above this world for the sake of the religion and of winning people over to it — that the affairs of government moved away from them and were taken by others, although they were qualified for them. Not thirty years had passed before power was in the hands of the ṭulaqā' [the former enemies set free at the conquest of Makkah].\n\n"
    "There is no doubt that those who devoted themselves wholly to Allāh (ﷻ) will receive their full reward, and that the affairs of this world are too lowly for a man of faith to grieve over them. Yet we ask: was it in the interest of the messages themselves that others should be preferred in this way? Or was it Islām's misfortune to meet this kind of ruler, so that those who were foremost and those who had given it support were pushed aside, and the reins of the religion were held by those who were the last to enter it and had the least insight into it?!")

EDITS = [
    E("HUN", "7.5261", "a nyilak, amelyekkel jāhilīyájában a jósokat kérdezte,", "a jósnyilak, amelyekkel jāhilīyájában sorsot vetett,"),
    E("ENG", "7.5261", "the arrows with which he had consulted the oracles in his jahilīyah", "the divining arrows with which he used to cast lots in his jahilīyah"),
    E("HUN", "7.5263", "„Hallgass! Hasítsa fel Isten a szádat! Istenre, inkább győzzön le engem egy Quraish-beli férfi, mint egy Hawāzin-beli.\"", "„Hallgass! Hasítsa fel Isten a szádat! Istenre, inkább legyen uram egy Quraish-beli férfi, mint egy Hawāzin-beli.\""),
    E("ENG", "7.5263", "\"Shut up! May God split you mouth! By God, I should prefer a man from the Quraish to defeat me than a man from the Hawāzin.\"", "\"Shut up! May God split your mouth! By God, I would rather have a man from the Quraish as my master than a man from the Hawāzin.\""),
    E("HUN", "7.5273a", "Ezalatt a Próféta (ﷺ) öszvérén ülve ezt kiáltotta: „Én Allah Prófétája (ﷺ) vagyok, és ez az igazság; én 'Abdul Muṭṭalib fia vagyok!\"⁸¹ És így fohászkodott:",
      "Ezalatt a Próféta (ﷺ) öszvérén ülve ezt kiáltotta:\n\n*„Én vagyok a Próféta — ez nem hazugság;*\n\n*én vagyok 'Abd al-Muṭṭalib fia!\"*⁸¹\n\nÉs így fohászkodott:"),
    E("ENG", "7.5273a", "All this time, the Prophet (ﷺ) on his mule was shouting: \"I am the Prophet of Allāh (ﷺ) and this the truth; I am the son of 'Abdul Muṭṭalib.⁸¹ He was also supplicating:",
      "All this time, the Prophet (ﷺ) on his mule was shouting:\n\n*\"I am the Prophet — this is no lie;*\n\n*I am the son of 'Abd al-Muṭṭalib!\"*⁸¹\n\nHe was also supplicating:"),
    E("HUN", "7.5273b", "„Vereséget szenvedtek, Mohamed (ﷺ) Urára!\" — és nem sokkal ezután a Thaqīf és szövetségesei hátat fordítottak és megfutamodtak.",
      "„Vereséget szenvedtek, Mohamed (ﷺ) Urára!\" Al-'Abbās elmondta: „Odanéztem, és a harc — úgy láttam — ugyanúgy folyt; ám alighogy rájuk hajította [a kavicsokat], azt láttam, hogy élük egyre tompul, soraik pedig hátrálnak.\" Nem kellett sokáig várni, és a Thaqīf emberei meg szövetségeseik hátat fordítva menekültek — s egyszer csak azt látták, hogy övéiket megkötözött foglyokként viszik!"),
    E("ENG", "7.5273b", "\"They are defeated, by the Lord of Muhammad (ﷺ),\" and it was not long before the Thaqīf and their allies had turned their backs in flight.",
      "\"They are defeated, by the Lord of Muhammad (ﷺ)!\" Al-'Abbās said: \"I looked, and the fighting, as far as I could see, was going on as before; but no sooner had he thrown [the pebbles] at them than I saw their edge grow ever blunter and their cause turn to retreat.\" It was not long before the men of Thaqīf and their allies were fleeing headlong — and suddenly they saw their own people led away as bound captives!"),
    E("HUN", "7.5279", "majd utána unokaöccse, Abū Mūsā al-Ash'arī vette fel a zászlót,", "majd utána unokatestvére [így az arab eredetiben; a történeti források szerint unokaöccse volt — a ford.], Abū Mūsā al-Ash'arī vette fel a zászlót,"),
    E("ENG", "7.5279", "and after him his nephew, Abū Mūsā al-Ash'ārī took up the banner", "and after him his cousin [thus in the Arabic original; according to the historical sources he was his nephew — translator's note], Abū Mūsā al-Ash'arī, took up the banner"),
    E("HUN", "7.5283", "Bár tíz éjszakát várt, senki sem jött.⁸⁴", "Tíz-egynéhány éjszakát várt, de senki sem jött.⁸⁴"),
    E("ENG", "7.5283", "Although he waited ten nights, no-one came.⁸⁴", "He waited ten-odd nights, but no-one came.⁸⁴"),
    E("HUN", "7.5299", "Abū Ṭalḥah, az iszlám kevés igazi harcosának egyike,", "Abū Ṭalḥah, a muszlimok egyik híres lovasa,"),
    E("ENG", "7.5299", "Abū Ṭalḥah, one of the few warriors of Islām,", "Abū Ṭalḥah, one of the renowned horsemen of the Muslims,"),
    E("HUN", "7.5305", "„Allah Küldötte (ﷺ), ezután megölöm a szabadon bocsátottakat,", "„Allah Küldötte (ﷺ), ölesd meg ezután a szabadon bocsátottakat,"),
    E("ENG", "7.5305", "Messenger of Allāh (ﷺ), after that I shall kill the freedmen", "\"Messenger of Allāh (ﷺ), kill after this the freedmen"),
    E("HUN", "7.5357", "Ő távozott, és ők szétszéledtek.⁹⁰", HUN_ANSAR),
    E("ENG", "7.5357", "He left and they dispersed.⁹⁰", ENG_ANSAR),
    E("HUN", "7.5363", "„Nekem csak az van, amit láttok.", "„Velem vannak azok, akiket láttok [és akiknek szintén részük van a zsákmányban]."),
    E("ENG", "7.5363", "\"I have only what you see.", "\"With me are those whom you see [who also have a share in the spoils]."),
    E("HUN", "7.5375", "— ez olyan hadviselési mód volt, amelyet azok nagyon jól ismertek, mert művelték már azelőtt, és értették a támadás meg a védekezés legjobb módjait.", "— a muszlimoknak ugyanis régi tapasztalatuk volt ebben a hadviselési módban: ostromoltak már korábban is, és ismerték a támadás és a védekezés legjobb módjait."),
    E("ENG", "7.5375", ", a method of war with which they were very familiar because they had done it before and understood the best means of attack and defence.", " — for the Muslims had long experience of this method of war: they had laid sieges before and knew the best means of attack and defence."),
    E("HUN", "7.5393", "'Attāb ibn Usayyidot", "'Attāb ibn Usaydot"),
    E("ENG", "7.5393", "'Attāb ibn Usayyid", "'Attāb ibn Usayd"),
    E("HUN", "7.5405", "miközben arcuk a visszatérő győztesre mosolygott.", "miközben arcuk a visszatérő győztesre mosolygott — pedig azt szerették volna, bárcsak soha ne látnák többé az alakját."),
    E("ENG", "7.5405", "while their faces were smiling at the returning victor.", "while their faces were smiling at the returning victor — though they wished they would never see his figure again."),
]
EDITS += [
    E("ENG", "7.5263b", "Kildah ibn al-Junayd exclaimed: Indeed! Today the magic is broken!\" Ṣafwān ibn Umayyah, though still a polytheist, paid to him in reply:",
      "Kildah ibn al-Junayd exclaimed: \"Indeed! Today the magic is broken!\" Ṣafwān ibn Umayyah, though still a polytheist, said to him in reply:"),
]
