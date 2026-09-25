# Footnote restorations ch6 — 16 notes dropped by the English edition + fn43 misanchor
# (AR pp.167, 185, 186[anchor on p.185 at Q5:52], 197(٢), 201(٢), 206 ×3, 207 ×2, 208, 209, 210, 219(١), 220, 224)
from fnins import INS


def _rep(s, a, b, done_marker):
    """Replace a→b once unless done_marker is already present (self-guarding)."""
    if done_marker in s:
        return s
    assert s.count(a) == 1, (a[:60], s.count(a))
    return s.replace(a, b)


def PRE(t):
    h, e = t["HUN"], t["ENG"]
    # fn43 carries AR p.197 fn(٣) (Abū Ṭalḥah «نحرى دون نحرك») but sits on Sa'd's «ارم فداك أبى وأمى»: move it.
    h = _rep(h, "„Lőj! Apám és anyám legyen váltságod.\"⁴³", "„Lőj! Apám és anyám legyen váltságod.\"", "nyakam a te nyakad előtt!\"⁴")
    h = _rep(h, "nyakam a te nyakad előtt!\"", "nyakam a te nyakad előtt!\"⁴³", "nyakam a te nyakad előtt!\"⁴")
    e = _rep(e, "\"Shoot. My father and mother be your ransom.⁴³", "\"Shoot! May my father and mother be your ransom!\"", "my neck before your neck!\"⁴")
    e = _rep(e, "my neck before your neck!\"", "my neck before your neck!\"⁴³", "my neck before your neck!\"⁴")
    # «فما خلصت من لحمه حتى سقطت معها ثنيتاه» — Abū 'Ubaydah's OWN two front teeth came out with the rings
    h = _rep(h, "Ám alig távolította el őket, elülső fogai kihullottak, és a sebből bőségesen folyt a vér.",
             "Ám mire a szegecsek kiszabadultak a húsából, az ő két elülső foga is kiesett velük. A sebből bőségesen folyt a vér.",
             "az ő két elülső foga is kiesett velük.")
    e = _rep(e, "However, no sooner had they been removed than his front teeth fell out and blood flowed copiously from his wound.",
             "However, by the time they came free from the flesh, his own two front teeth had fallen out with them. Blood flowed copiously from the wound.",
             "his own two front teeth had fallen out with them.")
    # حمراء الأسد
    for x in ("HUN", "ENG"):
        s = h if x == "HUN" else e
        s = s.replace("Ḥamra Al-Asad", "Ḥamrā' al-Asad")
        if x == "HUN":
            h = s
        else:
            e = s
    # «فنادى منادى رسول الله» — the Prophet's crier; ENG missing closing quote
    h = _rep(h, "A Próféta (ﷺ) azonban kihirdette, hogy a vértanúkat", "A Próféta (ﷺ) kikiáltója azonban kihirdette, hogy a vértanúkat", "kikiáltója azonban kihirdette")
    e = _rep(e, "However, the Prophet's (ﷺ) announced that the martyred should all be returned to their places of martyrdom.",
             "However, the Prophet's (ﷺ) crier announced that the martyred should all be returned to their places of martyrdom.\"",
             "the Prophet's (ﷺ) crier announced")
    t["HUN"], t["ENG"] = h, e
    return t


RESTORE = [
    # p.167 «روى أحمد(١)»
    INS("HUN", 6, "Aḥmad beszélte el 'Abdullāh ibn Mas'ūd (رضي الله عنه) tekintélyére hivatkozva, aki azt mondta:",
        "A Musnadban (3901. és 3665. sz.); lánca jó (ḥasan). Al-Ḥākim is lejegyezte (3/20), és azt mondta: „Muszlim feltételei szerint hiteles hadísz.\""),
    INS("ENG", 6, "Aḥmad narrated on the authority of 'Abdullāh ibn Mas'ūd (رضي الله عنه) who said:",
        "In the Musnad (nos. 3901, 3665); its chain is good (ḥasan). Al-Ḥākim also transmitted it (3/20) and said: \"A sound Ḥadīth according to the criteria of Muslim.\""),
    # p.185 «هم لك(١)»
    INS("HUN", 6, "Allah Küldötte (ﷺ) így felelt: „A tieid,",
        "Eddig Ibn Hishām (2/121) beszélte el Ibn Isḥāqtól: „'Āṣim ibn 'Umar ibn Qatādah beszélte el nekem\", mursalként. A többit egyelőre nem találtam meg."),
    INS("ENG", 6, "The Messenger of Allāh (ﷺ) replied: \"They are yours",
        "Up to here it was narrated by Ibn Hishām (2/121) from Ibn Isḥāq: \"'Āṣim ibn 'Umar ibn Qatādah told me,\" as *mursal*. The rest of it I have not come across for now."),
    # p.186 note, anchored at Q5:52
    INS("HUN", 6, "(Korán 5: 52)",
        "Ibn Isḥāq (2/121) beszélte el 'Ubādah ibn al-Walīd ibn 'Ubādah ibn al-Ṣāmittól, Ibn Jarīr pedig 'Aṭiyyah al-'Awfītól és Al-Zuhrītól; ezek mind mursal elbeszélések. Ibn Kathīr tafsīrjában (2/68) utalt rá, hogy gyenge az a hagyomány, amely szerint a vers Ibn Ubayyról nyilatkoztatott ki. Allah tudja jobban."),
    INS("ENG", 6, "(Qur'ān 5: 52)",
        "Narrated by Ibn Isḥāq (2/121) from 'Ubādah ibn al-Walīd ibn 'Ubādah ibn al-Ṣāmit, and by Ibn Jarīr from 'Aṭiyyah al-'Awfī and from Al-Zuhrī; all of them are *mursal*. Ibn Kathīr indicated in his Tafsīr (2/68) that the report of the verse's revelation concerning Ibn Ubayy is weak. And Allāh knows best."),
    # p.197(٢) «ارم فداك أبى وأمى»
    INS("HUN", 6, "„Lőj! Apám és anyám legyen váltságod.\"", "Bukhārī jegyezte le (7/287) Sa'd hadíszaként."),
    INS("ENG", 6, "\"Shoot! May my father and mother be your ransom!\"", "Transmitted by Bukhārī (7/287) as a Ḥadīth of Sa'd."),
    # p.201(٢) the rings / incisors
    INS("HUN", 6, "az ő két elülső foga is kiesett velük.",
        "Ibn Hishām említi (2/135–136) Isḥāq ibn Yaḥyā ibn Ṭalḥah útján, 'Īsā ibn Ṭalḥahtól, 'Ā'ishahtól, Abū Bakrtól. Al-Ṭayālisī összefüggő lánccal közölte (99/21): „Ibn al-Mubārak beszélte el nekünk Isḥāqtól…\", és ugyanígy Al-Ḥākim is (8/26–28) — láncában torzulás esett —, aki azt mondta: „Hiteles lánc.\" Al-Dhahabī azonban helyesbítette: „Én azt mondom: Isḥāq elhagyott (*matrūk*).\" Ugyanezt mondta Al-Haythamī is (16/112), miután Al-Bazzārnak tulajdonította."),
    INS("ENG", 6, "his own two front teeth had fallen out with them.",
        "Mentioned by Ibn Hishām (2/135–136) by way of Isḥāq ibn Yaḥyā ibn Ṭalḥah from 'Īsā ibn Ṭalḥah from 'Ā'ishah from Abū Bakr. Al-Ṭayālisī transmitted it with a connected chain (99/21): \"Ibn al-Mubārak told us from Isḥāq…\", and so did Al-Ḥākim (8/26–28) — a distortion has crept into his chain — who said: \"Its chain is sound.\" Al-Dhahabī, however, corrected him: \"I say: Isḥāq is abandoned (*matrūk*).\" Al-Haythamī (16/112) said the same, after attributing it to Al-Bazzār."),
    # p.206(١) «روى ابن إسحاق(١)» — Sa'd ibn al-Rabī'
    INS("HUN", 6, "Ibn Isḥāq elbeszélte, hogy a Próféta (ﷺ) így szólt:",
        "Muhammad ibn 'Abdullāh ibn 'Abd al-Raḥmān ibn Abī Ṣa'ṣa'ah al-Māzinī útján közölte, aki kifejezetten kijelentette, hogy tőle hallotta, ahogyan Ibn Hishām Szírájában áll (2/140–141); ez *mu'ḍal* lánc. Al-Ḥākim (3/201) Muhammad ibn Isḥāq útján közölte, hogy 'Abdullāh ibn Abī Ṣa'ṣa'ah az apjától [hallotta], hogy Allah Küldötte (ﷺ) mondta — és elmondja. Attól tartok, hogy a láncból kiesett „Muhammad\" ibn 'Abdullāh ibn 'Abd al-Raḥmān Ibn Isḥāq és 'Abdullāh ibn 'Abd al-Raḥmān között, mert Ibn Isḥāqot nem említik azok között, akik 'Abdullāh ibn 'Abd al-Raḥmāntól hagyományoztak; így a hadísz mursal, mert ez az 'Abdullāh követő (tābi'ī), apja, 'Abd al-Raḥmān ibn Abī Ṣa'ṣa'ah pedig társ (ṣaḥābī). Ha Al-Ḥākim lánca hiánytalan volna, a hadísz összefüggő volna, és Al-Dhahabī nem kifogásolta volna mursal volta miatt. Allah tudja jobban. A hadíszt Mālik is közölte a Muwaṭṭa'ban (2/21) Yaḥyā ibn Sa'īdtól, *mu'ḍal*ként. Al-Suyūṭī a *Tanwīr al-Ḥawālik*ban idézi Ibn 'Abd al-Barrt: „Ezt a hadíszt nem tudom fejből, és nem is ismerem, csak a szíra-írók körében, akiknél közismert.\" Én azt mondom: Al-Ḥākim Zayd ibn Thābit hadíszaként is közölte: „Allah Küldötte (ﷺ) Uḥud napján elküldött, hogy keressem meg Sa'd ibn al-Rabī'-t…\", és Al-Ḥākim azt mondta: „Hiteles lánc\", amiben Al-Dhahabī egyetértett vele. Láncában azonban ott van Abū Ṣāliḥ 'Abdullāh ibn Ṣāliḥ al-Ṭawīl, akinek életrajzát most nem találtam."),
    INS("ENG", 6, "Ibn Isḥāq narrated that the Prophet (ﷺ) said:",
        "He transmitted it by way of Muhammad ibn 'Abdullāh ibn 'Abd al-Raḥmān ibn Abī Ṣa'ṣa'ah al-Māzinī, stating explicitly that he heard it from him, as in Ibn Hishām's Sīrah (2/140–141); this is a *mu'ḍal* chain. Al-Ḥākim (3/201) transmitted it by way of Muhammad ibn Isḥāq, that 'Abdullāh ibn Abī Ṣa'ṣa'ah [heard] from his father that the Messenger of Allāh (ﷺ) said — and he mentions it. I fear that \"Muhammad\" ibn 'Abdullāh ibn 'Abd al-Raḥmān has dropped out of the chain between Ibn Isḥāq and 'Abdullāh ibn 'Abd al-Raḥmān, for Ibn Isḥāq is not listed among those who narrate from 'Abdullāh ibn 'Abd al-Raḥmān; accordingly the ḥadīth is *mursal*, since this 'Abdullāh is a Successor (*tābi'ī*), while his father 'Abd al-Raḥmān ibn Abī Ṣa'ṣa'ah was a Companion. Had Al-Ḥākim's chain been free of the omission, the ḥadīth would be connected, and Al-Dhahabī would not have faulted it as *mursal*. And Allāh knows best. Mālik also transmitted it in the Muwaṭṭa' (2/21) from Yaḥyā ibn Sa'īd as *mu'ḍal*. Al-Suyūṭī quotes Ibn 'Abd al-Barr in *Tanwīr al-Ḥawālik*: \"I do not know this ḥadīth by heart, nor do I know it except among the people of the sīrah, among whom it is well known.\" I say: Al-Ḥākim also transmitted it as a ḥadīth of Zayd ibn Thābit: \"The Messenger of Allāh (ﷺ) sent me on the day of Uḥud to look for Sa'd ibn al-Rabī'…\", and Al-Ḥākim said: \"Its chain is sound,\" and Al-Dhahabī agreed with him. In its chain, however, is Abū Ṣāliḥ 'Abdullāh ibn Ṣāliḥ al-Ṭawīl, whose biography I have not found for now."),
    # p.206(٢) «ردوا القتلى إلى مضاجعهم»
    INS("HUN", 6, "hogy a vértanúkat mind vissza kell vinni vértanúságuk helyére.\"",
        "Hiteles (ṣaḥīḥ) hadísz: Abū Dāwūd (2/63), Al-Nasā'ī (1/284), Ibn Mājah (1/264) és Aḥmad (3/297, 308, 397, 398) jegyezte le hiteles lánccal Jābirtól."),
    INS("ENG", 6, "should all be returned to their places of martyrdom.\"",
        "A sound Ḥadīth transmitted by Abū Dāwūd (2/63), Al-Nasā'ī (1/284), Ibn Mājah (1/264) and Aḥmad (3/297, 308, 397, 398) with a sound chain from Jābir."),
    # p.206(٣) burial with their blood, no prayer, no washing
    INS("HUN", 6, "sem meg nem mosdatta őket.",
        "Hiteles (ṣaḥīḥ) hadísz: Bukhārī (3/163–165, 169; 288/1), Al-Nasā'ī (7/300), Al-Tirmidhī (2/148), Ibn Mājah (1/460) és Aḥmad (5/431) jegyezte le, szintén Jābir hadíszaként."),
    INS("ENG", 6, "nor washed them.",
        "A sound Ḥadīth transmitted by Bukhārī (3/163–165, 169; 288/1), Al-Nasā'ī (7/300), Al-Tirmidhī (2/148), Ibn Mājah (1/460) and Aḥmad (5/431), also as a Ḥadīth of Jābir."),
    # p.207(١) blood colour / musk
    INS("HUN", 6, "illata pedig a pézsmáé.\"",
        "Hiteles (ṣaḥīḥ) hadísz: Aḥmad (5/431, 432) és Ibn Hishām (2/142) jegyezte le, mindketten Ibn Isḥāq útján: „Al-Zuhrī beszélte el nekem 'Abdullāh ibn Tha'labah ibn Ṣu'ayr al-'Udhrītól\", a Prófétáig felvezetve (*marfū'*). Ibn Ṣu'ayr fiatal társ volt, így ez egy társ mursalja, ami bizonyítékként elfogadható. Ugyanígy jegyezte le Al-Bayhaqī (4/11) Ibn 'Uyaynah útján Al-Zuhrītól, és egy másik úton is Al-Zuhrītól, 'Abd al-Raḥmān ibn Ka'b ibn Māliktól, az apjától. Ennek lánca szintén hiteles."),
    INS("ENG", 6, "the scent that of musk.\"",
        "A sound Ḥadīth transmitted by Aḥmad (5/431, 432) and Ibn Hishām (2/142), both by way of Ibn Isḥāq: \"Al-Zuhrī told me from 'Abdullāh ibn Tha'labah ibn Ṣu'ayr al-'Udhrī,\" traced back to the Prophet (*marfū'*). Ibn Ṣu'ayr was a young Companion, so it is a Companion's *mursal*, which is admissible as proof. Al-Bayhaqī (4/11) transmitted it likewise by way of Ibn 'Uyaynah from Al-Zuhrī, and also by another route from Al-Zuhrī from 'Abd al-Raḥmān ibn Ka'b ibn Mālik from his father. Its chain is sound as well."),
    # p.207(٢) «أحد جبل يحبنا ونحبه»
    INS("HUN", 6, "„Uḥud olyan hegy, amely szeret minket, és amelyet mi szeretünk.\"",
        "Hiteles (ṣaḥīḥ) hadísz: Bukhārī (7/302), Muszlim (4/124) és mások jegyezték le Anas és mások hadíszaként."),
    INS("ENG", 6, "\"Uḥud is a mountain which loves us and which we love.\"",
        "A sound Ḥadīth transmitted by Bukhārī (7/302), Muslim (4/124) and others as a Ḥadīth of Anas and others."),
    # p.208 Ḥamrā' al-Asad
    INS("HUN", 6, "míg Ḥamrā' al-Asadhoz nem értek, Abū Sufyān erőinek közelébe.",
        "Ibn Lahī'ah beszélte el Abū al-Aswadtól, 'Urwah ibn al-Zubayrtól, mursalként, ahogyan az Al-Bidāyában áll; Ibn Hishām pedig Ibn Isḥāqtól említi, lánc nélkül."),
    INS("ENG", 6, "until they reached Ḥamrā' al-Asad and approached Abū Sufyān's force.",
        "Narrated by Ibn Lahī'ah from Abū al-Aswad from 'Urwah ibn al-Zubayr as *mursal*, as in Al-Bidāyah; Ibn Hishām mentions it from Ibn Isḥāq without a chain."),
    # p.209 Abū Salamah's expedition
    INS("HUN", 6, "mielőtt bármilyen rajtaütést végrehajthatnának.",
        "Ezt a portyát Ibn Kathīr említi az Al-Bidāyában (4/61–62) Al-Wāqidī útján, *mu'ḍal* lánccal! Al-Wāqidī pedig elhagyott (*matrūk*)!"),
    INS("ENG", 6, "before they could carry out any raids.",
        "This expedition is mentioned by Ibn Kathīr in Al-Bidāyah (4/61–62) by way of Al-Wāqidī with a *mu'ḍal* chain! And Al-Wāqidī is abandoned (*matrūk*)!"),
    # p.210 'Abdullāh ibn Unays
    INS("HUN", 6, "amikor a beduin törzseket próbálta Medina ellen mozgósítani.",
        "Abū Dāwūd (2/196), Al-Bayhaqī (3/256) és Aḥmad (3/496) jegyezte le 'Abdullāh ibn Unays fiának útján, az apjától. Ibn Kathīr tafsīrjában (1/295) azt mondta: „Lánca jó (*jayyid*)\", Ibn Ḥajar pedig a *Fatḥ*ban (2/350): „Lánca jó (*ḥasan*).\" Én azt mondom: 'Abdullāh ibn Unays fia az ő elbeszélésükben „'Ubaydullāh\", ami alighanem a másoló vagy a nyomdász torzítása, mert Ibn Abī Ḥātim az „'Abdullāh\" nevűek között említi, és azt mondja: „Apjától hagyományozott, és Muhammad ibn Ibrāhīm al-Taymī hagyományozott tőle\" — sem megbízhatóságáról, sem gyengeségéről nem szól. Muhammad ibn Ja'far ibn al-Zubayr is hagyományozott tőle, és éppen ő az, aki ezt a hadíszt tőle elbeszélte. Allah tudja jobban."),
    INS("ENG", 6, "while still attempting to mobilize the bedouin tribes against Madīnah.",
        "Transmitted by Abū Dāwūd (2/196), Al-Bayhaqī (3/256) and Aḥmad (3/496) by way of the son of 'Abdullāh ibn Unays from his father. Ibn Kathīr said in his Tafsīr (1/295): \"Its chain is good (*jayyid*),\" and Ibn Ḥajar in Al-Fatḥ (2/350): \"Its chain is good (*ḥasan*).\" I say: in their narration the son of 'Abdullāh ibn Unays is named \"'Ubaydullāh\", which seems to be a distortion by the copyist or the printer, for Ibn Abī Ḥātim lists him among those named \"'Abdullāh\" and says: \"He narrated from his father, and Muhammad ibn Ibrāhīm al-Taymī narrated from him,\" mentioning neither criticism nor commendation of him. Muhammad ibn Ja'far ibn al-Zubayr also narrated from him, and it is he who narrated this ḥadīth from him. And Allāh knows best."),
    # p.219(١) Banū al-Muṣṭaliq outcome
    INS("HUN", 6, "Így az egész törzs mindenével együtt a muszlimok kezére került.",
        "Hasonlóan jegyezte le Ibn Jarīr Történetében (2/160–262) Ibn Isḥāq útján, láncával, mursalként; ugyanígy Ibn Hishām is a *Szírában* (2/216–218). Ez a lánc — gyengesége mellett — nem tartalmazza, hogy 'Umar felajánlotta volna az iszlámot. Al-Zurqānī az *Al-Mawāhib* kommentárjában (2/97) utalt e kiegészítés gyengeségére, és joggal, hiszen a Prófétától (ﷺ) hitelesen fennmaradt valami, ami gyengeségét maga után vonja: Ibn al-Qayyim a *Zād*ban, miután az itteninél hasonló harcot említ, azt mondja: „Így mondta 'Abd al-Raḥmān ibn Khalaf ibn Khalīfah a szírájában és mások is; ez azonban tévedés, mert nem volt köztük harc: a vízforrásnál ütött rajtuk, foglyul ejtette asszonyaikat és gyermekeiket, és elvette javaikat, ahogyan a *Ṣaḥīḥ*ban áll: »Allah Küldötte (ﷺ) rajtaütött a Banū al-Muṣṭaliqon, amikor azok gyanútlanok voltak« — és elmondja a hadíszt.\" Lásd a *Fatḥ al-Bārī*t (7/346)."),
    INS("ENG", 6, "Thus the whole tribe and all that they possessed fell into the hands of the Muslims.",
        "Transmitted in similar form by Ibn Jarīr in his History (2/160–262) by way of Ibn Isḥāq with his chain as *mursal*, and likewise by Ibn Hishām in the Sīrah (2/216–218). This chain, besides being weak, does not contain 'Umar's offering Islām to them. Al-Zurqānī pointed out the weakness of this addition in his commentary on Al-Mawāhib (2/97), and rightly so, for something authentic has come from the Prophet (ﷺ) that entails its weakness: Ibn al-Qayyim says in Al-Zād, after mentioning fighting like that described here: \"Thus said 'Abd al-Raḥmān ibn Khalaf ibn Khalīfah in his sīrah, and others; but it is a mistake, for there was no fighting between them: he raided them at the water, took their women and children captive and seized their property, as in the Ṣaḥīḥ: 'The Messenger of Allāh (ﷺ) raided the Banū al-Muṣṭaliq while they were unaware' — and he mentions the ḥadīth.\" See Fatḥ al-Bārī (7/346)."),
    # p.220 Q63:8
    INS("HUN", 6, "(Korán 63: 8)", "Ez Ibn Isḥāq fent említett mursal elbeszélésének a vége."),
    INS("ENG", 6, "(Qur'ān 63: 8)", "This is the end of Ibn Isḥāq's *mursal* report mentioned above."),
    # p.224 the Ifk story
    INS("HUN", 6, "(Korán 24: 11)",
        "Ezt a történetet ebben a formában Ibn Isḥāq beszélte el hiteles láncokkal 'Ā'ishahtól; az ő útján jegyezte le Ibn Hishām a *Szírában* (2/220–222). Bukhārī (7/447–35) és Muszlim (8/113–177) is lejegyezte, az itteninél hasonlóan."),
    INS("ENG", 6, "(Qur'ān 24: 11)",
        "This story was narrated in this form by Ibn Isḥāq with sound chains from 'Ā'ishah; by his route Ibn Hishām transmitted it in the Sīrah (2/220–222). It is also in Bukhārī (7/447–35) and Muslim (8/113–177) in similar form."),
]
