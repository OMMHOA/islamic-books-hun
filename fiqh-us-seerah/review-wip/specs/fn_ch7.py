# Footnote restorations ch7 — AR pp.267(٢), 280(١), 283(٣) [+ fn56/57 one-slot misalignment], 292(٣), 292(٤), 301(١)
# (p.324(٣) author's book reference is inlined in the body — not dropped.)
import re

from fnins import INS


def _rep(s, a, b, done_marker):
    if done_marker in s:
        return s
    assert s.count(a) == 1, (a[:60], s.count(a))
    return s.replace(a, b)


def PRE(t):
    h, e = t["HUN"], t["ENG"]
    # fn56 text = AR p.284(١) (orphans ḥadīth), fn57 text = AR p.284(٢) («لا تختلفا»): each marker sits one anchor too early.
    if not re.search("ne vitatkozzék 'Amrral\\.[⁰-⁹]", h):
        h = _rep(h, "köztünk lennének.\"⁵⁶", "köztünk lennének.\"", "@@")
        h = _rep(h, "túlvilágon?«\"⁵⁷", "túlvilágon?«\"⁵⁶", "@@")
        h = _rep(h, "akinek meghagyta, hogy ne vitatkozzék 'Amrral.", "akinek meghagyta, hogy ne vitatkozzék 'Amrral.⁵⁷", "@@")
    if not re.search("disputes with 'Amr\\.[⁰-⁹]", e):
        e = _rep(e, "they would not be happy to be among us.\"⁵⁶", "they would not be happy to be among us.\"", "@@")
        e = _rep(e, "in this world and the next?\"⁵⁷", "in this world and the next?\"⁵⁶", "@@")
        e = _rep(e, "whom he advised not to have any disputes with 'Amr.", "whom he advised not to have any disputes with 'Amr.⁵⁷", "@@")
    # «وحسابهم على الله»; وادى القرى
    h = _rep(h, "Wādī al Qurā zsidói harcoltak", "Wādī al-Qurā zsidói harcoltak", "Wādī al-Qurā zsidói")
    h = _rep(h, "büntetésük pedig Allahra (ﷻ) marad.", "számadásuk pedig Allahra (ﷻ) tartozik.", "számadásuk pedig Allahra (ﷻ) tartozik.")
    e = _rep(e, "The Jews of Wadi al Qira fought", "The Jews of Wādī al-Qurā fought", "The Jews of Wādī al-Qurā")
    e = _rep(e, "and their punishment would be left to Allāh (ﷻ).", "and their reckoning would rest with Allāh (ﷻ).", "their reckoning would rest with Allāh")
    t["HUN"], t["ENG"] = h, e
    return t


RESTORE = [
    # p.267(٢) Wādī al-Qurā
    INS("HUN", 7, "számadásuk pedig Allahra (ﷻ) tartozik.", "Al-Wāqidī beszélte el lánc nélkül, ahogyan az Al-Bidāyában áll (4/218)."),
    INS("ENG", 7, "their reckoning would rest with Allāh (ﷻ).", "Narrated by Al-Wāqidī without a chain, as in Al-Bidāyah (4/218)."),
    # p.280(١) Mu'tah command «إن أصيب فجعفر…»
    INS("HUN", 7, "és ha Ja'far elesik, akkor 'Abdullāh ibn Rawāḥah.",
        "Hiteles (ṣaḥīḥ) hadísz: Bukhārī (7/412) és mások jegyezték le Ibn 'Umartól, Aḥmad (5/299, 300–301) pedig Abū Qatādahtól; lánca hiteles."),
    INS("ENG", 7, "and if Ja'far was killed then 'Abdullāh ibn Rawāḥah.",
        "A sound Ḥadīth transmitted by Bukhārī (7/412) and others from Ibn 'Umar, and by Aḥmad (5/299, 300–301) from Abū Qatādah; its chain is sound."),
    # p.283(٣) «ما يسرهم أنهم عندنا»
    INS("HUN", 7, "„Nem örülnének annak, ha köztünk lennének.\"",
        "Hiteles (ṣaḥīḥ) hadísz: Bukhārī jegyezte le (6/135) Anas fent említett hadíszaként, egyik változatában ezzel a szöveggel: „Nem örülnék — vagy azt mondta: nem örülnének…\", kétkedve."),
    INS("ENG", 7, "\"they would not be happy to be among us.\"",
        "A sound Ḥadīth transmitted by Bukhārī (6/135) as part of the Ḥadīth of Anas mentioned above, in one narration with the wording: \"I would not be happy — or he said: they would not be happy…\", with doubt."),
    # p.292(٣) «فدخل مكة من أعلاها»
    INS("HUN", 7, "A Próféta (ﷺ) Mekka felső része felől lépett be,", "Hiteles (ṣaḥīḥ): Bukhārī jegyezte le (8/14, 15) Ibn 'Umartól és 'Ā'ishahtól."),
    INS("ENG", 7, "The Prophet (ﷺ) entered Makkah from its upper side", "Ṣaḥīḥ: transmitted by Bukhārī (8/14, 15) from Ibn 'Umar and 'Ā'ishah."),
    # p.292(٤) «ألا يقاتلوا إلا من قاتلهم»
    INS("HUN", 7, "hogy ne harcoljanak, hacsak meg nem támadják őket.", "Ibn Hishām említi (3/383) Ibn Isḥāqtól, lánc nélkül."),
    INS("ENG", 7, "not to fight unless they were attacked.", "Mentioned by Ibn Hishām (3/383) from Ibn Isḥāq without a chain."),
    # p.301(١) al-'Abbās (report restored in ch7e)
    INS("HUN", 7, "élük egyre tompul, soraik pedig hátrálnak.\"", "Muszlim jegyezte le Al-'Abbāstól."),
    INS("ENG", 7, "their cause turn to retreat.\"", "Transmitted by Muslim from Al-'Abbās."),
]
