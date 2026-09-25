# Ch7 part 3 (levelek vége → 'Umrat al-Qaḍā' → Mu'tah → Dhāt al-Salāsil) — see opus55-findings.md "Ch7 part 3"
from apply import E

HUN_FAREWELL = ("A muszlimok háromezer harcost tett ki. Medina népe kivonult, hogy elbúcsúztassa az induló sereget, és ezt mondták: „Allah (ﷻ) kísérjen benneteket épségben, óvjon meg titeket, és hozzon vissza hozzánk jó egészségben!\" 'Abdullāh ibn Rawāḥah e búcsúra így felelt:\n\n"
    "*„Én azonban a Könyörületestől bocsánatot kérek, és egy széles, habot vető kardcsapást;*\n\n"
    "*vagy egy szomjas [ellenség] kezéből jövő, halálos döfést, lándzsával, amely átjárja belsőmet és májamat;*\n\n"
    "*hogy ha elhaladnak sírom mellett, azt mondják: Ó, milyen jó útra vezérelte Allah (ﷻ) e harcost, és ő jó úton is járt!\"*\n\n"
    "A Próféta (ﷺ) elrendezte")
ENG_FAREWELL = ("for it comprised three thousand fighters. The people of Madīnah came out to bid farewell to the departing army, saying: \"May Allāh (ﷻ) accompany you in safety, protect you and bring you back to us in good health!\" 'Abdullāh ibn Rawāḥah answered this farewell:\n\n"
    "*\"But I ask the Compassionate for forgiveness, and a wide sword-blow that throws up foam;*\n\n"
    "*or a deadly thrust from the hands of a thirsting [foe], with a spear that pierces the bowels and the liver;*\n\n"
    "*so that when they pass by my grave they say: O how Allāh (ﷻ) guided this warrior aright, and he was rightly guided!\"*\n\n"
    "The Prophet (ﷺ) arranged")

EDITS = [
    E("HUN", "7.4855", "ahogyan Szaúd-Arábiában az asszonyok pulykákat nevelnek:", "ahogyan hazánkban az asszonyok pulykákat nevelnek:"),
    E("ENG", "7.4855", "just as the women in Saudi Arabia rear turkeys", "just as the women in our country rear turkeys"),
    E("HUN", "7.4869", "Az arabok nem tisztelik, és a kinyilatkoztatott tudás előtt sincs becsülete.", "Nincs benne sem az arabok nemeslelkűsége, sem a kinyilatkoztatott könyv tudása."),
    E("ENG", "7.4869", "The Arabs have no respect for it nor is there any respect for revealed knowledge.", "It has neither the nobility of the Arabs nor the knowledge of the revealed Book."),
    E("HUN", "7.4885", "Hasonlóképpen a Próféta úgy tekintett nemzetére, mint tudatlan emberekre, akiket tanítani kell;", "Hasonlóképpen a próféták az emberekben csak tudatlanokat látnak, akiket tanítani kell, és balgákat, akiket az igaz útra kell vezetni;"),
    E("ENG", "7.4885", "Similarly, the Prophet looked upon his nation as ignorant people who ought to be educated,", "Similarly, the prophets see in people only the ignorant who must be taught and the foolish who must be guided,"),
    E("HUN", "7.4887", "és a saruban meg a mezítláb járóknál ér véget;", "és elér addig, ameddig teve és ló patája eljuthat;"),
    E("ENG", "7.4887", "and will end at the clothed and the barefoot,", "and will reach as far as camel-hoof and horse-hoof can go,"),
    E("HUN", "7.4905", "és így énekelt: „Nyissatok utat neki, hitetlenek fiai! Nyissatok utat, mert az Ő küldötte csupa jóság! Uram! Bizony hiszek abban, amit mond. Elismerem Allah (ﷻ) jogát az ő elfogadásában!\"",
      "és így énekelt:\n\n*„Nyissatok utat neki, hitetlenek fiai! Nyissatok utat, mert minden jó az Ő Küldöttében van!*\n\n*Uram! Bizony hiszek szavában; elismerem Allah (ﷻ) jogát az ő elfogadásában!\"*"),
    E("ENG", "7.4905", "and chanting: \"Give way to him, sons of unbelievers. Give way, for His messenger is all good. Lord! Verily I believe in what he says. I recognize Allāh's (ﷻ) right in accepting him!\"",
      "and chanting:\n\n*\"Give way to him, sons of unbelievers! Give way, for all good is in His Messenger!*\n\n*Lord! Verily I believe in his word; I recognize Allāh's (ﷻ) right in accepting him!\"*"),
    E("HUN", "7.4911", "Al 'Abbās, a Próféta (ﷺ) nagybátyja ajánlotta neki házasságra Maymūnah bint al-Ḥāritht.", "Al 'Abbās, a Próféta (ﷺ) nagybátyja ajánlotta neki házasságra Maymūnah bint al-Ḥāritht, 'Abdullāh ibn 'Abbās anyai nagynénjét."),
    E("ENG", "7.4911", "had offered Maymūnah bint al-Ḥārith to him in marriage.", "had offered Maymūnah bint al-Ḥārith, the maternal aunt of 'Abdullāh ibn 'Abbās, to him in marriage."),
    E("HUN", "7.4921", "A muszlimok háromezer harcost tett ki. A Próféta (ﷺ) elrendezte", HUN_FAREWELL) if False else E("HUN", "7.4921", "mert háromezer harcost tett ki. A Próféta (ﷺ) elrendezte", "mert háromezer harcost tett ki. Medina népe kivonult, hogy elbúcsúztassa az induló sereget, és ezt mondták: „Allah (ﷻ) kísérjen benneteket épségben, óvjon meg titeket, és hozzon vissza hozzánk jó egészségben!\" 'Abdullāh ibn Rawāḥah e búcsúra így felelt:\n\n*„Én azonban a Könyörületestől bocsánatot kérek, és egy széles, habot vető kardcsapást;*\n\n*vagy egy szomjas [ellenség] kezéből jövő, halálos döfést, lándzsával, amely átjárja belsőmet és májamat;*\n\n*hogy ha elhaladnak sírom mellett, azt mondják: Ó, milyen jó útra vezérelte Allah (ﷻ) e harcost, és ő jó úton is járt!\"*\n\nA Próféta (ﷺ) elrendezte"),
    E("ENG", "7.4921", "for it comprised three thousand fighters. The Prophet (ﷺ) arranged", ENG_FAREWELL),
    E("HUN", "7.4929", "annyi fegyvert, juhot, brokátot, selymet és aranyat láttunk,", "annyi fegyvert, lovat, brokátot, selymet és aranyat láttunk,"),
    E("ENG", "7.4929", "such large amounts of weapons, sheep, brocade, silk and gold", "such large amounts of weapons, horses, brocade, silk and gold"),
    E("HUN", "7.4935", "amint leugrott pej lováról és megbénította azt.", "amint leugrott sárga (sorrel) kancájáról és megbénította azt."),
    E("ENG", "7.4935", "when he jumped off his chestnut horse and hamstring it.", "when he jumped off his sorrel mare and hamstrung it."),
    E("HUN", "7.4937", "*Üdvöz légy, Paradicsom, közelségeddel! Mily jó vagy, mily hűs italod!*\n\n*A rómaiak — rómaiak, akiknek betelt a végzete; hitetlenek, akiknek származása korántsem tiszta — még ha csapásaikat el is szenvedem.\"*",
      "*Mily szép a Paradicsom és közelsége — mily jó, mily hűs az itala!*\n\n*A rómaiak rómaiak, közel már büntetésük — hitetlenek, tőlünk távoli származásúak!*\n\n*Rajtam a sor, ha összecsapok velük: sújtani őket!\"*"),
    E("ENG", "7.4937", "*Welcome to Paradise and its approach! How good it is, how cool its drink!*\n\n*The Romans are Romans whose doom has arrived; unbelievers whose lineage is far from pure even though I receive their blows.\"*",
      "*How lovely is Paradise and its nearness — how good, how cool its drink!*\n\n*The Romans are Romans whose punishment draws near — unbelievers, remote from us in lineage!*\n\n*It is upon me, if I meet them, to strike them!\"*"),
    E("HUN", "7.4945", "*„Ó, lelkem, ha meg nem ölnek is, meghalsz.*\n\n*Íme a halál szerelme, amelynek kitétettél.*\n\n*Amit kívántál, megadatott neked. Ha úgy teszel, ahogyan ők [ketten] tettek, helyes vezetést nyertél.\"*",
      "*„Ó, lelkem, ha meg nem ölnek is, meghalsz — íme a halál végzete, amelybe beléptél!*\n\n*Amit kívántál, megadatott neked; ha úgy teszel, ahogyan ők [ketten] tettek, helyes vezetést nyertél!\"*"),
    E("ENG", "7.4945", "*\"O soul of mine, if you are not killed you will die.*\n\n*Here is the love of death to whom you are exposed.*\n\n*What you wished for, you are given it. If you do as they (both) did, you will be rightly guided.\"*",
      "*\"O soul of mine, if you are not killed you will die — this is death's fated hour that you have entered!*\n\n*What you wished for, you have been given; if you do as they (both) did, you will be rightly guided!\"*"),
    E("HUN", "7.4957", "„Mu'ta napján kilenc kard tört el a kezemben.\"", "„Mu'ta napján kilenc kard tört el a kezemben, és csak egy jemeni széles penge maradt meg a kezemben.\" Az éjszaka ráborult a harcoló felekre, és ez ideiglenes fegyverszünetet hozott. Amikor megvirradt, Khālid már újjászervezte csekély erejét: az elővédet utóvéddé, a jobbszárnyat balszárnnyá tette."),
    E("ENG", "7.4957", "\"On the day of Mu'ta, nine swords broke in my hand.\"", "\"On the day of Mu'tah, nine swords broke in my hand, and nothing held in my hand but a broad Yemeni blade.\" Night fell on the combatants and brought a temporary truce. When morning came, Khālid had reorganized his small force, making the vanguard the rearguard and the right wing the left."),
    E("HUN", "7.4965", "olyan szintet ért el, amilyet egyetlen modern nemzet sem látott.", "olyan szintet ért el, amilyet egyetlen akkori nemzet sem ismert."),
    E("ENG", "7.4965", "had reached a level no modern nation has seen.", "had reached a level no contemporary nation had known."),
    E("HUN", "7.4967", "és hogyan tanították őket anyáik?", "és hogyan dédelgették őket anyáik?"),
    E("ENG", "7.4967", "and how did their mothers train them?", "and how did their mothers cherish them?"),
    E("HUN", "7.4973", "»Mohamed hasonlít nagybátyánkra, Abū Ṭālibra,", "»Muhammad hasonlít nagybátyánkra, Abū Ṭālibra,"),
    E("ENG", "7.4973", "\"Muhammad (ﷺ) is like our uncle Abū Ṭālib", "\"Muhammad is like our uncle Abū Ṭālib"),
    E("HUN", "7.4981", "## Dhāt al Salāsil", "## Dhāt al-Salāsil"),
    E("HUN", "7.4991", "'Amr üldözni kezdte a rómaiakkal szövetséges törzseket. Számos vidékre behatolt,", "'Amr üldözni kezdte a rómaiakkal szövetséges törzseket, és behatolt a Balī, az 'Udhrah, a Balqayn és a Ṭayyi' földjére;"),
    E("ENG", "7.4991", "'Amr began to pursue the tribes which were allied to the Romans. He entered a number of countries,", "'Amr began to pursue the tribes which were allied to the Romans, and penetrated the lands of Balī, 'Udhrah, Balqayn and Ṭayyi';"),
    E("HUN", "7.4867", "A levelet Al 'Alā ibn al-Ḥaḍramī vitte,⁴⁸ aki kitűnt az iszlám bemutatásában. Többek között ezt mondta:", "A levelet Al-'Alā' ibn al-Ḥaḍramī vitte el hozzá.⁴⁸ Al-Mundhir ibn Sāwā, Bahrein emírje értelmes és szerencsés ember volt: örömmel fogadta a hívást, és szíve megnyílt az elfogadására. Al-'Alā' pedig mindent megtett, hogy megnyerje, és feltárja előtte az iszlám szépségeit. Többek között ezt mondta:"),
    E("ENG", "7.4867", "The letter was taken by Al 'Ala ibn al-Hadrami,⁴⁸ who excelled in his presentation of Islām. Among the things he said was:", "The letter was taken to him by Al-'Alā' ibn al-Ḥaḍramī.⁴⁸ Al-Mundhir ibn Sāwā, the emir of Bahrain, was a sensible and fortunate man: he welcomed the call and his heart opened to accept it. Al-'Alā' did his utmost to win him over and to show him the merits of Islām. Among the things he said was:"),
]
