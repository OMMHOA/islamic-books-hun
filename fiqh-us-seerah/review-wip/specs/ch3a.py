# Ch3 part 1 (→ Tárgyalások) — see opus55-findings.md "Ch3 — part 1"
from apply import E

HUN_MAD = ("\n\nHa egy eszelős az utadba áll, és éles nyelvvel gyalázza becsületedet, hallod, amint valaki azt mondja neked: »Ez nem neked akar ártani, csak a vérében lakozó őrület késztetéseinek enged.« Így voltak azok a bálványimádók is. Durvaságuk és tagadásuk inkább természetük hitetlenségre hajló késztetéseiből fakadt, semmint abból, hogy le akarták volna becsülni azt a férfit, aki szólt hozzájuk, vagy jellemét akarták volna gyalázni:"
           "\n\n(…bár valójában nem téged [Mohamed] tagadnak, hanem a gonosztevők megvetik Allah Kinyilatkoztatásait.) (Korán 6: 33)")
ENG_MAD = ("\n\nIf a madman blocks your way and assails your honour with a sharp tongue, you hear someone say to you: 'He does not mean to attack you; he is only responding to the urges of madness in his blood.' So it was with those idolaters. Their harshness and denial sprang from the urges of disbelief in their nature rather than from any wish to belittle the man who was speaking to them or to impugn his character:"
           "\n\n(…though in truth they do not deny you [Muhammad], but evil-doers flout the Revelations of Allāh.) (Qur'ān 6: 33)")

EDITS = [
    E("HUN", "3.1148", "figyelmeztetést és felmentést követelt.", "figyelmeztetést és kellő intést követelt."),
    E("ENG", "3.1148", "warning and acquittal.", "warning and due notice."),
    E("HUN", "3.1156", "legyetek mértékletesek a keresésben. Nem kevésbé valószínű-e ez, hogy rémületet és kimerültséget okozzon?\"⁶", "legyetek mértékletesek a keresésben…\"⁶ Nem állt volna-e ez távolabb attól, ami rémületet és kimerültséget okoz?"),
    E("ENG", "3.1156", "and be restrained in seeking.⁶ Is this not less likely to cause fright and exhaustion?\"", "and be restrained in seeking…\"⁶ Would that not have been further removed from what causes fright and exhaustion?"),
    E("HUN", "3.1188", "Aktam ibn Ṣayfī azt mondta", "Aktham ibn Ṣayfī azt mondta"),
    E("ENG", "3.1188", "Aktam ibn Sayfī said", "Aktham ibn Ṣayfī said"),
    E("HUN", "3.1204", "Bár csak egy materialista gondolat, életüket annak terjesztésére fordítja, és arra ösztönzi őket, hogy a szenvedés legrosszabb fajtáit viseljék el az érdekében.", "Bár csak egy materialista gondolat, életüket annak terjesztésére fordítják, és a szenvedés legrosszabb fajtáit is elviselik érte."),
    E("HUN", "3.1206", "Mennyivel hatékonyabb lett volna, ha a hit, amely abban az időben megjelent, az Allahba (ﷻ), minden világok Urába vetett hit volt,", "Mennyivel inkább így volt ez, amikor az iszlám hajnalán megjelent hit az Allahba (ﷻ), minden világok Urába vetett hit volt,"),
    E("ENG", "3.1206", "How much more effective it would have been if the faith which appeared at that time was faith in Allāh (ﷻ), Lord of all the worlds,", "How much more so, then, when the faith which appeared at the dawn of Islām was faith in Allāh (ﷻ), Lord of all the worlds,"),
    E("HUN", "3.1208a", "felszabadított rabszolgája, Zayd ibn Ḥārithah is,", "felszabadított rabszolgája, Zayd ibn Ḥārithah [az arab eredeti „Zayd ibn Thābit\"-et ír — a ford.] is,"),
    E("ENG", "3.1208a", "his slave freed, Zayd ibn Ḥārithah,", "his freed slave, Zayd ibn Ḥārithah [the Arabic original has 'Zayd ibn Thābit' — translator's note],"),
    E("HUN", "3.1208b", "'Umar ibn 'Anbasa és Sa'īd ibn al-'Āṣ felvette az iszlámot,", "'Umar ibn 'Anbasa [így az arab eredetiben; a korai hívő neve helyesen 'Amr ibn 'Abasah — a ford.] és Sa'īd ibn al-'Āṣ [így az arab eredetiben; a korai hívő helyesen Khālid ibn Sa'īd ibn al-'Āṣ — a ford.] felvette az iszlámot,"),
    E("ENG", "3.1208b", "Umar ibn 'Anbasa and Sa'īd ibn al 'As accepted Islām,", "'Umar ibn 'Anbasa [thus in the Arabic original; the early convert's name is 'Amr ibn 'Abasah — translator's note] and Sa'īd ibn al-'Āṣ [thus in the Arabic original; the early convert was Khālid ibn Sa'īd ibn al-'Āṣ — translator's note] accepted Islām,"),
    E("HUN", "3.1210", "egyike azoknak a vallási fanatikusoknak, akik az Istenségről és annak jogairól beszélnek, ahogy Umayyah ibn al-Ṣalt szokta tenni, vagy a keresztény tudós, Ibn Sa'īdah,", "egyike azoknak a vallásos embereknek, akik az Istenségről és annak jogairól beszélnek, ahogy Umayyah ibn al-Ṣalt szokta tenni, vagy Quss ibn Sā'idah,"),
    E("ENG", "3.1210", "one of those religious fanatics who would speak of Divinity and its rights as Umayyah ibn Al Ṣalt used to do, or the Christian scholar Ibn Sa'idah", "one of those religious-minded men who would speak of Divinity and its rights as Umayyah ibn Al Ṣalt used to do, or Quss ibn Sā'idah"),
    E("HUN", "3.1228", "ó, Ṣafiyyah, Allah Küldöttének (ﷺ) nagynénje, semmiképp nem leszek hasznodra Allah (ﷻ) előtt.\"¹⁰", "ó, Ṣafiyyah, Allah Küldöttének (ﷺ) nagynénje, semmiképp nem leszek hasznodra Allah (ﷻ) előtt; ó, Fāṭimah, Allah Küldöttének (ﷺ) leánya, kérj tőlem vagyonomból, amit csak akarsz, de semmiképp nem leszek hasznodra Allah (ﷻ) előtt.\"¹⁰"),
    E("ENG", "3.1228", "O Ṣafiyyah, aunt of Allāh's Messenger (ﷺ), I will not avail you in any way before Allāh (ﷻ).\"¹⁰", "O Ṣafiyyah, aunt of Allāh's Messenger (ﷺ), I will not avail you in any way before Allāh (ﷻ); O Fāṭimah, daughter of Allāh's Messenger (ﷺ), ask me for whatever you wish of my wealth, but I will not avail you in any way before Allāh (ﷻ).\"¹⁰"),
    E("HUN", "3.1230", "A Próféta (ﷺ) megszakította a kapcsolatot népével hívása miatt.", "A Próféta (ﷺ) hívását tette meg a népéhez fűződő viszonya mércéjévé."),
    E("ENG", "3.1230", "The Prophet (ﷺ) severed relations with his people on account of his call.", "The Prophet (ﷺ) made his call the criterion of his relations with his people."),
    E("HUN", "3.1232", "Nem volt tehát az ő dolga, hogy éjjel nyugalmat találjon, miközben Mekka megrendült a megdöbbenéstől és az elítéléstől, és arra készült, hogy véget vessen ennek a forradalomnak, amely hirtelen leszállt rá, és arra készült, hogy elsöpörje szokásait és örökölt hagyományait.",
      "Nem bánta hát, hogy e figyelmeztetés után úgy tér nyugovóra, hogy Mekka háborog a megdöbbenéstől és a felháborodástól, és arra készül, hogy leszámoljon ezzel a hirtelen kirobbant forradalommal, amelytől azt féltette, hogy elsöpri szokásait és örökölt hagyományait."),
    E("ENG", "3.1232", "It was not for him, therefore, to find rest at night while Makkah was shaking with astonishment and condemnation, and was preparing to put an end to this revolution which had suddenly descended upon it and was about to sweep away its custom and inherited traditions.",
      "It did not trouble him, therefore, to spend the night after this warning while Makkah surged with astonishment and condemnation and prepared to put an end to this revolution which had suddenly broken out and which it feared would sweep away its customs and inherited traditions."),
    E("HUN", "3.1242", "beszélj hát, és ne viselkedj gyerekesen,", "beszélj hát, de hagyd a hitehagyottakat (ṣubāt),"),
    E("ENG", "3.1242", "so speak and do not act childishly,", "so speak, but leave the apostates (ṣubāt) alone,"),
    E("HUN", "3.1280", "egyetlen értelmes ember sem tehetett volna jobban náluk.", "egyetlen értelmes ember sem hibáztathatta volna őket ezért."),
    E("ENG", "3.1280", "no intelligent person could have done better than they.", "no sensible person would have blamed them for it."),
    E("HUN", "3.1284", "megvetik Allah Kinyilatkoztatásait.) (Korán 6: 33)\n\nÍgy Mohamednek (ﷺ) tovább kellett", "megvetik Allah Kinyilatkoztatásait.) (Korán 6: 33)" + HUN_MAD + "\n\nÍgy Mohamednek (ﷺ) tovább kellett"),
    E("ENG", "3.1284", "flout the Revelations of Allāh.) (Qur'ān 6: 33)\n\nThus Muhammad (ﷺ) had to continue", "flout the Revelations of Allāh.) (Qur'ān 6: 33)" + ENG_MAD + "\n\nThus Muhammad (ﷺ) had to continue"),
    E("HUN", "3.1290", "Évekig így maradt,", "Tíz évig így maradt,"),
    E("ENG", "3.1290", "For years it remained like that,", "For ten years it remained like that,"),
    E("HUN", "3.1292", "Hasonló stratégia ez ahhoz, amelyet az újságok alkalmaznak, amikor szatirikus beszámolókat tesznek közzé riválisaikról, és mulatságos képeket, hogy csökkentsék a köztük belé vetett bizalmat.", "Hasonló stratégia ez ahhoz, amelyet az ellenzéki sajtó alkalmaz, amikor csípős élceket és nevetséges képeket közöl ellenfeleiről, hogy lejárassa őket a tömegek előtt."),
    E("ENG", "3.1292", "It is a similar strategy to that used by the newspapers when they publish satirical reports about their rivals", "It is a similar strategy to that used by the opposition press when it publishes satirical reports about its rivals"),
    E("HUN", "3.1300", "Ez elterjedt, és ellenséges pillantásokkal és a düh érzéseivel találkozott:", "Falánk, gyűlölködő pillantások és felkorbácsolt, háborgó indulatok kísérték és fogadták:"),
    E("ENG", "3.1300", "This spreads and he is met with hostile stares and feelings of rage:", "He was seen off and received with devouring, resentful stares and agitated, raging feelings:"),
    E("HUN", "3.1348a", "(És azok, akik nem hisznek, azt mondják: Cselekedjetek erőtök szerint.", "(És mondd azoknak, akik nem hisznek: Cselekedjetek erőtök szerint."),
    E("HUN", "3.1348b", "Imádjátok hát Őt, és Belé helyezzétek bizodalmatokat.", "Imádd hát Őt, és Belé helyezd bizodalmadat."),
    E("ENG", "3.1348", "(And say those who do not believe: Act according to your power.", "(And say unto those who do not believe: Act according to your power."),
    E("HUN", "3.1354", "Az egyik azt mondja: 'költő', a másik azt mondja: 'egy dzsinn szállta meg'.", "Az egyik azt mondja: 'varázsló', a másik: 'jós', a harmadik: 'költő', a negyedik: 'egy dzsinn szállta meg'."),
    E("ENG", "3.1354", "One will say 'a poet', and another will say 'possessed by a Jinn'", "One will say 'a sorcerer', another 'a soothsayer', another 'a poet', and another 'possessed by a Jinn'."),
]
