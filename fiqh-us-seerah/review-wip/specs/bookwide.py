# Book-wide mechanical/name unifications (both files) — see opus55-findings.md "Book-wide mechanical" + per-chapter [C] items
from apply import E

EDITS = [
    E("HUN", "BW.salamahh", "Umm Salamahh", "Umm Salamah"),        # repair of a ch4a double-h artefact
    E("ENG", "BW.salmah", "Umm Salmah", "Umm Salamah", count=2),
    E("HUN", "BW.abusalamah", "Abū Salāmah", "Abū Salamah", count=3),
    E("ENG", "BW.abusalamah", "Abū Salāmah", "Abū Salamah", count=3),
    E("HUN", "BW.salit", "Umm Salit", "Umm Salīṭ"),
    E("ENG", "BW.salit", "Umm Salit", "Umm Salīṭ"),
]
EDITS += [
    E("HUN", "BW.madinai", "madīnaiak", "medinaiak"),
    E("HUN", "BW.madinai2", "madīnai", "medinai", count=9),
]
EDITS += [
    E("HUN", "BW.dblhon", "a Próféta (ﷺ) — béke legyen vele — megérkezett", "a Próféta (ﷺ) megérkezett"),
]
EDITS += [
    E("HUN", "BW.hubab", "Habbāb", "Ḥubāb", count=7),
    E("ENG", "BW.hubab", "Habbāb", "Ḥubāb", count=7),
]
EDITS += [
    E("HUN", "BW.quraydhah", "a Banu Qurayzah-ból,", "a Banū Quraydhahból,"),
    E("ENG", "BW.quraydhah1", "of the Banu Qurayzah as a", "of the Banū Quraydhah as a"),
    E("ENG", "BW.quraydhah2", "the Jews of the Qurayzah", "the Jews of the Quraydhah"),
]

# ---- 2026-09-25: remaining book-wide items (after ch7/ch8 specs) ----
EDITS += [
    # al-Jannah → Paradicsom (2026-07-25 convention; the sweep missed Dzsanna/Jannah)
    E("HUN", "BW.jannah1", "Ha a Dzsannában van,", "Ha a Paradicsomban van,"),
    E("HUN", "BW.jannah2", "Dzsannába", "Paradicsomba", count=4),
    E("HUN", "BW.jannah3", "*Ḥūr*: Húrik, Allah teremtményei a Jannah lakói számára.", "*Ḥūr*: Húrik, Allah teremtményei a Paradicsom lakói számára."),
    # names / suffixes
    E("HUN", "BW.muzaynah", "Mi közöm nekem Muzaynához", "Mi közöm nekem Muzaynahhoz"),
    E("HUN", "BW.quraishbol", "a Quraishből", "a Quraishból"),
    E("HUN", "BW.aws", "z Aus", "z Aws", count=7),
    E("ENG", "BW.aws1", "was under the Aus and Khazr", "was under the Aws and Khazr"),
    E("ENG", "BW.aws2", "salvation. The Aus and the K", "salvation. The Aws and the K"),
    E("ENG", "BW.aws3", "between the Aus and the K", "between the Aws and the K"),
    E("ENG", "BW.aws4", "favoured the Aus. Both par", "favoured the Aws. Both par"),
    E("ENG", "BW.aws5", "three from the Aus.⁵", "three from the Aws.⁵"),
    E("ENG", "BW.aws6", "chief of the Aus, who were", "chief of the Aws, who were"),
    E("ENG", "BW.aws7", "benefit them. The Aus themselve", "benefit them. The Aws themselve"),
    E("HUN", "BW.juwayriyah", "Juwayrīyah Al-Ḥārithnak", "Juwayriyah Al-Ḥārithnak"),
    E("ENG", "BW.juwayriyah", "Juwayrīyah was the daughter", "Juwayriyah was the daughter"),
    E("HUN", "BW.uhud", "Uhud napján", "Uḥud napján", count=4),
    E("HUN", "BW.uhudi", "az uhudi ", "az uḥudi ", count=2),
    E("HUN", "BW.signature", "**Muhammad Al Ghazālī**", "**Muhammad Al-Ghazali**"),
    # quote-mark repairs (state-tracking scan 2026-09-25)
    E("HUN", "BW.q1605", "ahol előző nap tevét vágtak.\"\n\nAbū Jahl azt mondta: „Melyikőtök fogja ennek-és-ennek a tevéjének a gyomrát, és dobja Mohamed (ﷺ) lapockái közé (a hátára), amikor leborul?\"",
      "ahol előző nap tevét vágtak.\n\nAbū Jahl azt mondta: »Melyikőtök fogja ennek-és-ennek a tevéjének a gyomrát, és dobja Mohamed (ﷺ) lapockái közé (a hátára), amikor leborul?«"),
    E("HUN", "BW.q1609a", "Háromszor mondta: „Ó, Allah (ﷻ), ragadd meg a Quraisht.\" Amikor", "Háromszor mondta: »Ó, Allah (ﷻ), ragadd meg a Quraisht.« Amikor"),
    E("HUN", "BW.q1609b", "Majd így szólt: „Ó, Allah (ﷻ), ragadd meg Abū Jahl ibn Hishāmot, 'Utbah ibn Rabi'át, Shaybah ibn Rabi'át, Al Walīd ibn 'Utbát, Umayyah ibn Khalafot, 'Uqbah ibn Abi Mu'iṭot\" — és",
      "Majd így szólt: »Ó, Allah (ﷻ), ragadd meg Abū Jahl ibn Hishāmot, 'Utbah ibn Rabi'át, Shaybah ibn Rabi'át, Al Walīd ibn 'Utbát, Umayyah ibn Khalafot, 'Uqbah ibn Abi Mu'iṭot« — és"),
    E("HUN", "BW.q1934", "„Ha ezt teljesítitek, a Paradicsom jár nektek.", "»Ha ezt teljesítitek, a Paradicsom jár nektek."),
    E("HUN", "BW.q1934b", "ha akarja, megbüntet (ﷻ), különben megbocsát nektek.\"³", "ha akarja, megbüntet (ﷻ), különben megbocsát nektek.«\"³"),
    E("HUN", "BW.q2549", "*Lā ilāha illa-llāh.«*", "*Lā ilāha illa-llāh.«\"*"),
    E("HUN", "BW.q2747", "jótettet viszonzott vele.\"²¹", "jótettet viszonzott vele.²¹"),
    E("HUN", "BW.q2933", "mert az üldözés rosszabb az ölésnél.) (Korán 2: 217)", "mert az üldözés rosszabb az ölésnél.\") (Korán 2: 217)"),
    E("HUN", "BW.q2961", "idegenkedett [tőle]; „Vitáznak veled az igazságról", "idegenkedett [tőle]; vitáznak veled az igazságról"),
    E("HUN", "BW.q3257", "Hozzá hívok, és Hozzá térek vissza.) (Korán 13: 36)", "Hozzá hívok, és Hozzá térek vissza.\") (Korán 13: 36)"),
    E("HUN", "BW.q3589", "\n\nÓ, Allah (ﷻ), Tiéd minden dicséret.", "\n\n„Ó, Allah (ﷻ), Tiéd minden dicséret."),
    E("HUN", "BW.q3915", "ha bajt akarnak, ellenállunk.«*⁶⁵", "ha bajt akarnak, ellenállunk.«\"*⁶⁵"),
    E("HUN", "BW.q6241", "(Korán 9: 37) — „…és megtiltják azt, amit Allah (ﷻ) megengedett.\"", "(Korán 9: 37) — …és megtiltják azt, amit Allah (ﷻ) megengedett.\""),
    # inner quotes '…' → »…« (second level)
    E("HUN", "BW.i953", "Azt felelte: 'A Szentséges Mecset' (vagyis Al Masjid Al Ḥarām). Aztán megkérdeztem: 'és mi következett?' Azt mondta: 'a Legtávolabbi Mecset' (vagyis Al Masjid Al Aqṣā). Megkérdeztem: 'Mennyi idő telt el a kettő között?' Azt mondta: 'Negyven év, és ráadásul a föld mecset a számodra. Tehát bárhol ér az imádság ideje, végezd el azt, mert erény van benne.'\"¹⁸",
      "Azt felelte: »A Szentséges Mecset« (vagyis Al Masjid Al Ḥarām). Aztán megkérdeztem: »És mi következett?« Azt mondta: »A Legtávolabbi Mecset« (vagyis Al Masjid Al Aqṣā). Megkérdeztem: »Mennyi idő telt el a kettő között?« Azt mondta: »Negyven év, és ráadásul a föld mecset a számodra. Tehát bárhol ér az imádság ideje, végezd el azt, mert erény van benne.«\"¹⁸"),
    E("HUN", "BW.i961", "azt mondta a Prófétának (ﷺ): 'Emeld az izárodat (ágyékkendődet) a vállad fölé, és megvéd a kövektől.'", "azt mondta a Prófétának (ﷺ): »Emeld az izárodat (ágyékkendődet) a vállad fölé, és megvéd a kövektől.«"),
    E("HUN", "BW.i961b", "és azt mondta: 'Az izárom! Az izárom!'", "és azt mondta: »Az izárom! Az izárom!«"),
    E("HUN", "BW.i1005", "és ezt mondta: 'Ó, Quraish népe, Istenre, senki közületek nem követi Ibrāhīm (عليه السلام) vallását, csak én.' Szokta volt megmenteni az elevenen eltemetett kislányokat, és azt mondani apáiknak, amikor meg akarták ölni kislányaikat: „Gondját viselem én.\" Elvette a lányt, és amikor elég nagy lett, azt mondta apjának: 'Ha akarod, visszaadom neked; ha nem, én folytatom gondozását.'\"²⁴",
      "és ezt mondta: »Ó, Quraish népe, Istenre, senki közületek nem követi Ibrāhīm (عليه السلام) vallását, csak én.« Szokta volt megmenteni az elevenen eltemetett kislányokat, és azt mondani apáiknak, amikor meg akarták ölni kislányaikat: »Gondját viselem én.« Elvette a lányt, és amikor elég nagy lett, azt mondta apjának: »Ha akarod, visszaadom neked; ha nem, én folytatom gondozását.«\"²⁴"),
    E("HUN", "BW.i1133", "és azt mondta: 'Ó, Allah Küldötte (ﷺ), íme, Khadījah jön", "és azt mondta: »Ó, Allah Küldötte (ﷺ), íme, Khadījah jön"),
    E("HUN", "BW.i1133b", "sem lárma, sem fáradtság nem lesz.'\"", "sem lárma, sem fáradtság nem lesz.«\""),
    E("HUN", "BW.i1340", "Azt mondtuk: 'Nem kéred Allah segítségét számunkra? Nem imádkozol értünk?'", "Azt mondtuk: »Nem kéred Allah segítségét számunkra? Nem imádkozol értünk?«"),
    E("HUN", "BW.i1342", "Ő azt felelte: 'A ti időtök előtt", "Ő azt felelte: »A ti időtök előtt"),
    E("HUN", "BW.i1344", "Ti azonban túl türelmetlenek vagytok.'\"", "Ti azonban túl türelmetlenek vagytok.«\""),
    E("HUN", "BW.i2857", "így szólt: ‘Aki megtanul lőni,", "így szólt: 'Aki megtanul lőni,"),
]
EDITS += [
    E("HUN", "BW.q3301", "„Ezek helyesebben vezéreltetnek, mint azok, akik hisznek?) (Korán 4: 51)", "„Ezek helyesebben vezéreltetnek, mint azok, akik hisznek?\") (Korán 4: 51)"),
]
