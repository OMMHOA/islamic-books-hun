# Ch7 part 4 (Mekka meghódítása) — see opus55-findings.md "Ch7 part 4"
from apply import E

HUN_AMR = ("A Khuzā'ah megrémült attól, ami velük történt, és elküldték 'Amr ibn Sālimot Allah Küldöttéhez (ﷺ), hogy beszámoljon neki. Amikor Medinába érkezett, megállt a Próféta (ﷺ) előtt, aki a mecsetben ült az emberek között, és így szólt:\n\n"
    "*„Uram, Mohamedet (ﷺ) kérlek atyánk és az ő atyja ősi szövetségére:*\n\n"
    "*ti voltatok a gyermek, mi a szülő; azután békét kötöttünk, és sosem vontuk vissza kezünket.*\n\n"
    "*Segíts hát — Allah (ﷻ) vezéreljen! — kész segítséggel, és hívd Allah (ﷻ) szolgáit, hogy erősítésül jöjjenek,*\n\n"
    "*köztük Allah Küldöttével (ﷺ), aki harcra készen áll, fehér, mint a magasra hágó telihold,*\n\n"
    "*s ha megalázás éri, arca elsötétül — tengerként habzó, áradó hadban.*\n\n"
    "*A Quraish megszegte neked tett ígéretét, és felrúgta megerősített szövetségedet;*\n\n"
    "*lest vetettek nekem Kadā'nál, és azt gondolták, senkit sem hívok segítségül,*\n\n"
    "*pedig ők a hitványabbak és kevesebben vannak; éjjel törtek ránk al-Watīrnál, míg aludtunk,*\n\n"
    "*és meggyilkoltak bennünket, miközben meghajoltunk és leborultunk.\"*\n\n"
    "Allah Küldötte (ﷺ) így felelt neki: „Megsegíttetel, ó, 'Amr ibn Sālim!\"⁵⁹")
ENG_AMR = ("The Khuzā'ah were terrified by what happened to them, and they sent 'Amr ibn Sālim to the Messenger of Allāh (ﷺ) to tell him their story. When he reached Madīnah he stood before the Prophet (ﷺ), who was sitting in the mosque among the people, and said:\n\n"
    "*\"O Lord, I adjure Muhammad (ﷺ) by the ancient alliance of our father and his father:*\n\n"
    "*you were the children and we the parent; then we made peace and never withdrew our hand.*\n\n"
    "*So help, may Allāh (ﷻ) guide you, with ready help, and call the servants of Allāh (ﷻ) to come as reinforcement,*\n\n"
    "*among them the Messenger of Allāh (ﷺ), stripped for battle, fair as the full moon rising high,*\n\n"
    "*whose face darkens if he is subjected to humiliation — in a host like the sea, flowing and foaming.*\n\n"
    "*The Quraish have broken their promise to you and violated your firm covenant;*\n\n"
    "*they set an ambush for me at Kadā' and claimed that I would call on no one,*\n\n"
    "*yet they are baser and fewer in number; they fell upon us by night at al-Watīr as we slept,*\n\n"
    "*and killed us as we bowed and prostrated.\"*\n\n"
    "The Messenger of Allāh (ﷺ) replied: \"You shall be helped, O 'Amr ibn Sālim!\"⁵⁹")

EDITS = [
    E("HUN", "7.5017", "„Ma nincs Isten, Banū Bakr! Végezzétek a dolgotokat!\"", "„Ma nincs Isten, Banū Bakr! Álljatok bosszút!\""),
    E("ENG", "7.5017", "\"There is no God today, Banū Bakr, Carry out your task!\"", "\"There is no God today, Banū Bakr! Take your revenge!\""),
    E("HUN", "7.5019", "A Khuzā'ah megrémült attól, ami velük történt, és elküldték 'Āmir ibn Sālimot a Prófétához (ﷺ), hogy tudassa vele a hírt. A beszámolót hallva a Próféta (ﷺ) megígérte, hogy segítségükre siet.⁵⁹", HUN_AMR),
    E("ENG", "7.5019", "The Khuzā'ah were terrified by what happened to them, and they sent 'Āmir ibn Sālim to the Prophet (ﷺ) to tell him the news. Upon hearing the account, the Prophet (ﷺ) promised to come to their aid.⁵⁹", ENG_AMR),
    E("HUN", "7.5027", "Elment 'Umarhoz (رضي الله عنه), de ő is visszautasította.", "Elment 'Umarhoz (رضي الله عنه), de ő így szólt: „Hogy én járjak közben értetek Allah Küldöttjénél (ﷺ)? Allahra (ﷻ), ha csak a hangyákat találnám, azokkal is harcolnék ellenetek!\""),
    E("ENG", "7.5027", "He went to 'Umar (رضي الله عنه) but the latter refused also.", "He went to 'Umar (رضي الله عنه), who said: \"Should I intercede for you with the Messenger of Allāh (ﷺ)? By Allāh (ﷻ), if I found nothing but ants, I would fight you with them!\""),
    E("HUN", "7.5051", "az bizony letévedt a helyes útról.⁶² (Korán 60: 1)", "az bizony letévedt a helyes útról.)⁶² (Korán 60: 1)"),
    E("ENG", "7.5051", "he has indeed strayed from the right way.⁶² (Qur'ān 60: 1)", "he has indeed strayed from the right way.)⁶² (Qur'ān 60: 1)"),
    E("HUN", "7.5059", "és 'Abdullāh ibn Abī 'Umayyah is elhagyta Mekkát, és Abwānál akadtak össze", "és 'Abdullāh ibn Abī Umayyah is elhagyta Mekkát, és al-Abwā'nál akadtak össze"),
    E("ENG", "7.5059", "and 'Abdullāh ibn Abi 'Umayyah left Makkah and encountered the Prophet (ﷺ) at Abwā.", "and 'Abdullāh ibn Abī Umayyah left Makkah and encountered the Prophet (ﷺ) at al-Abwā'."),
    E("HUN", "7.muzaynah", "Muzayyin", "Muzayn", count=2),
    E("ENG", "7.muzaynah", "Muzayyinah", "Muzaynah", count=2),
    E("HUN", "7.5139", "Sahl ibn 'Amr és Ṣafwān ibn Umayyah vezetésével.", "Suhayl ibn 'Amr és Ṣafwān ibn Umayyah vezetésével."),
    E("ENG", "7.5139", "Sahl ibn 'Amr and Ṣafwān ibn Umayyah.", "Suhayl ibn 'Amr and Ṣafwān ibn Umayyah."),
    E("HUN", "7.himas", "Ḥamās", "Ḥimās", count=2),
    E("ENG", "7.himas", "Ḥamās", "Ḥimās", count=2),
    E("HUN", "7.5145", "„Istenre, remélem, hogy egyiküket rabszolgáddá teszem.\"", "„Istenre, remélem, hogy egyiküket rabszolgáddá teszem.\" Majd így szólt:\n\n*„Ha ma előjönnek, nincs mentségem:*\n\n*itt a teljes fegyverzet, egy hosszú lándzsa,*\n\n*meg egy kétélű kard, amely gyorsan kirántható!\"*"),
    E("ENG", "7.5145", "\"By God, I hope to make one of them a slave for you.\"", "\"By God, I hope to make one of them a slave for you.\" Then he said:\n\n*\"If they come on today, I have no excuse:*\n\n*here is complete armour, and a long spear,*\n\n*and a two-edged sword, quick to draw!\"*"),
    E("HUN", "7.5151", "Ő mentegetőzve így szólt: „Ha láttad volna Khandamah napját, amikor Safwān megfutott, és 'Ikrimah is, és Abū Yazīd úgy állt, mint egy oszlop, és muszlim kardok fogadták őket, amelyek kart és koponyát hasítottak, s mögöttünk nem hallatszott más, csak nyögés, jajszavuk és hörgésük — egyetlen szemrehányó szót sem szóltál volna!\"",
      "Ő mentegetőzve így szólt:\n\n*„Ha láttad volna a Khandamah napját, amikor Ṣafwān elfutott, és elfutott 'Ikrimah is,*\n\n*Abū Yazīd [Suhayl ibn 'Amr] pedig úgy állt, mint az árváival magára maradt asszony — és kivont muszlim kardok fogadták őket,*\n\n*amelyek levágtak minden kart és koponyát, úgy csaptak, hogy nem hallatszott más, csak zűrzavaros moraj,*\n\n*mögöttünk pedig hörgésük és dörmögésük — a szemrehányásnak egyetlen szavát sem ejtetted volna ki!\"*"),
    E("ENG", "7.5151", "Excusing himself, he said: \"If you had seen the day of Khandaman, when Safwān fled, and also 'Ikrimah, and Abū Yazīd stood like a pillar, and they were met by Muslim swords cutting through every arm and skull, leaving only moans to be heard, behind us their cries and groans. Not a word of blame would you have uttered!\"",
      "Excusing himself, he said:\n\n*\"Had you witnessed the day of Khandamah, when Ṣafwān fled and 'Ikrimah fled too,*\n\n*and Abū Yazīd [Suhayl ibn 'Amr] stood like a woman left alone with her orphans — and drawn Muslim swords met them,*\n\n*cutting off every arm and skull, striking so that nothing could be heard but confused murmuring,*\n\n*and behind us their snorting and growling — you would not have uttered the least word of blame!\"*"),
    E("HUN", "7.5157", "és bálványokkal telve találta;", "és képekkel telve találta;"),
    E("ENG", "7.5157", "and saw it full of idols,", "and saw it full of pictures,"),
    E("HUN", "7.5167", "Az, meglátva őt, hívta, hogy üljön le és beszélgessenek. Ő azonban így felelt: „Nem. Allah (ﷻ) és az iszlám megtiltja nekem. Ha láttad volna Mohamedet (ﷺ) és törzsét a Hódítás napján, amikor a bálványok összezúzattak, láttad volna, amint Allah (ﷻ) vallása nyilvánvalóvá lesz, és a bálványimádás arca sötétségbe borul.\"",
      "Az, meglátva őt, hívta, hogy jöjjön beszélgetni. Ő erre így felelt:\n\n*„Azt mondta: »Gyere, beszélgessünk!« Én azt feleltem: »Nem! Allah (ﷻ) és az iszlám nem engedi.«*\n\n*Ha láttad volna Mohamedet (ﷺ) és seregét a hódítás napján, amikor a bálványok összezúzattak,*\n\n*láttad volna, amint Allah (ﷻ) vallása nyilvánvalóvá lett, a bálványimádás arcát pedig sötétség borította el.\"*"),
    E("ENG", "7.5167", "Fuḍalah had his weaknesses in jahilīyah, and as he was going home he came across a woman with whom he had had an affair. Upon seeing him she invited him to sit and chat. But he replied: \"No, Allāh (ﷻ) and Islām forbid it to me. If you had seen Muhammad (ﷺ) and his tribe on the day of the Conquest when the idols were smashed, you would have seen the religion of Allāh (ﷻ) becoming manifest and the face of idolatry being smothered in darkness.\"",
      "Fuḍālah had his weaknesses in jahilīyah, and as he was going home he came across a woman with whom he had had an affair. Upon seeing him she invited him to come and chat, and he answered:\n\n*\"She said: 'Come and talk!' I said: 'No! Allāh (ﷻ) and Islām forbid me.'*\n\n*Had you seen Muhammad (ﷺ) and his host on the day of the Conquest, when the idols were smashed,*\n\n*you would have seen the religion of Allāh (ﷻ) made manifest, and the face of idolatry covered in darkness.\"*"),
    E("HUN", "7.5177a", "Ezek az imák az elmélkedés pillanatai e világ értékéről;", "Ezek az imák az elmélkedés pillanatai a világ zajában;"),
    E("ENG", "7.5177a", "These prayers are the moments of contemplation about the worth of this world;", "These prayers are the moments of contemplation amid the noise of this world;"),
    E("HUN", "7.5177b", "— gőgös arckifejezésük dacára —", "— hiúságuk ellenére —"),
    E("ENG", "7.5177b", "inspite of their haughty airs,", "in spite of their vanity,"),
    E("HUN", "7.5185", "Van, aki a korai szakaszokat éli át, más pedig", "Van, akit már a küzdelem korai szakaszaiban elragad a halál, más pedig"),
    E("ENG", "7.5185", "Some may live through the early stages, whereas others", "Death may take some in its early stages, whereas others"),
    E("HUN", "7.5191", "és az egész hónapban ott maradt, imáit megrövidítve. Nem böjtölt tizenöt napnál tovább, noha böjtölve indult el Medinából.", "és a hónap hátralévő részében ott maradt; tizenkilenc napon át rövidítette imáit, és nem böjtölt, noha böjtölve indult el Medinából."),
    E("ENG", "7.5191", "and remained the whole month, shortening his prayers. He did not fast for more than fifteen days though he had left Madīna while fasting.", "and remained there for the rest of the month; for nineteen days he shortened his prayers and did not fast, though he had left Madīnah fasting."),
    E("HUN", "7.5193", "Öreg és fiatal, férfiak és nők jöttek, amikor tudtak.⁷⁶", "Jöttek öregek és fiatalok, asszonyok is, és a hűségeskü arra szólt, hogy hallgatnak Allahra (ﷻ) és Küldöttére (ﷺ), és engedelmeskednek nekik, amennyire csak képesek.⁷⁶"),
    E("ENG", "7.5193", "The old and the young, men and women came when they could.⁷⁶", "The old and the young came, and the women, and the pledge was to hear and obey Allāh (ﷻ) and His Messenger (ﷺ) as far as they were able.⁷⁶"),
    E("HUN", "7.5199", "Nem volt azonban mély gondolkodó, és ritkán kért másoktól tanácsot.", "Ítélőképessége azonban beteges, tanácsai rosszak voltak."),
    E("ENG", "7.5199", "However, he was not a deep thinker and seldom asked others for advice.", "However, his judgment was unsound and his counsel poor."),
]
