# Footnote restorations ch1 (AR p.24), ch3 (AR p.99), ch4 (AR pp.115, 126, 129) — see opus55-findings FOOTNOTE INVENTORY
from fnins import INS


def PRE(t):
    # ch4: the critique of Aḥmad's spider-web report (AR p.126 fn ٢) sits on the "two whose third is Allah"
    # ḥadīth; move that marker to "Aḥmad elbeszélte:" / "Aḥmad narrated:" (no marker lies in between).
    h, e = t["HUN"], t["ENG"]
    if "Aḥmad elbeszélte:¹" not in h:
        a = "akiknek Allah (ﷻ) a harmadik társuk?\"¹⁴"
        assert h.count(a) == 1
        h = h.replace(a, a[:-len("¹⁴")]).replace("lóra szálltak, hogy hazatérjenek. Aḥmad elbeszélte:", "lóra szálltak, hogy hazatérjenek. Aḥmad elbeszélte:¹⁴")
    if "Aḥmad narrated:¹" not in e:
        a = "\"Abū Bakr (رضي الله عنه), what is this thought of two. The third among us is Allāh (ﷻ).\"¹⁴"
        assert e.count(a) == 1
        e = e.replace(a, "\"Abū Bakr (رضي الله عنه), what do you think of two whose third is Allāh (ﷻ)?\"")
        e = e.replace("to return home. Aḥmad narrated:", "to return home. Aḥmad narrated:¹⁴")
    t["HUN"], t["ENG"] = h, e
    return t


RESTORE = [
    # ch1 p.24 «حديث صحيح أخرجه مسلم وابن ماجه»
    INS("HUN", 1, "míg száz párverset el nem mondtam.\"", "Hiteles (ṣaḥīḥ) hadísz: Muszlim és Ibn Mājah jegyezte le."),
    INS("ENG", 1, "until I had recited a hundred couplets.\"", "A sound Ḥadīth, transmitted by Muslim and Ibn Mājah."),
    # ch3 p.99 «ابن جرير (٢/ ٨٢ـ ٨٣) بدون سند كما تقدم فى تخريج الحديث السابق»
    INS("HUN", 3, "és beléptek abba, amit most tagadtok.\"", "Ibn Jarīr (2/82–83), lánc nélkül, ahogyan az előző hadísz forrásainál már említettük."),
    INS("ENG", 3, "before you enter into that which you are denying.\"", "Ibn Jarīr (2/82–83), without a chain, as mentioned in the sources of the previous Ḥadīth."),
    # ch4 p.115 «يقصد أهل يثرب جميعا من "أوس" و"خزرج"»
    INS("HUN", 4, "Azt mondta: „Ó, Khazraj gyülekezete!", "Yathrib egész népét érti ezen — az Awst és a Khazrajt egyaránt."),
    INS("ENG", 4, "He said: \"O assembly of the Khazraj", "He means all the people of Yathrib, both the Aws and the Khazraj."),
    # ch4 p.126 fn(١) at «ما ظنك باثنين الله ثالثهما»
    INS("HUN", 4, "akiknek Allah (ﷻ) a harmadik társuk?\"", "Hiteles (ṣaḥīḥ): Bukhārī (7/207), Muszlim (7/109) és mások jegyezték le Abū Bakr al-Ṣiddīq (رضي الله عنه) hadíszaként."),
    INS("ENG", 4, "what do you think of two whose third is Allāh (ﷻ)?\"", "Ṣaḥīḥ: transmitted by Bukhārī (7/207), Muslim (7/109) and others as a Ḥadīth of Abū Bakr al-Ṣiddīq (رضي الله عنه)."),
    # ch4 p.129 fn(١) «عزاه إليه ابن كثير (٣/ ١٨٧)… وهذا إسناد ضعيف معضل»
    INS("HUN", 4, "Abū Nu'aym elbeszéli,", "Ibn Kathīr (3/187) neki tulajdonítja, Muhammad ibn Isḥāq útján, aki azt mondta: „Úgy értesültem, hogy Allah Küldötte (ﷺ), amikor kivándorlóként elhagyta Mekkát, Allahhoz, Medina felé tartva, így szólt…\" — és elmondja a fohászt. Én azt mondom: ez gyenge, *mu'ḍal* lánc."),
    INS("ENG", 4, "Abū Nu'aym narrates", "Ibn Kathīr (3/187) attributes it to him by way of Muhammad ibn Isḥāq, who said: \"I have been told that when the Messenger of Allāh (ﷺ) left Makkah as an emigrant to Allāh, heading for Madīnah, he said…\" and he mentions the supplication. I say: this is a weak, *mu'ḍal* chain."),
]
