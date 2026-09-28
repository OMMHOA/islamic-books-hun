# User decisions 2026-09-25 (answers to the Opus 5.5 [D] list) — content edits.
# Run BEFORE d2_mech.py (these strings still contain straight quotes / em dashes).
from apply import E

EDITS = [
    # 5. Allah, not "Isten", wherever the Arabic has الله (pagans too swore by Allah).
    #    Oaths «والله / أنشدك الله» — all 43 "Istenre" are oaths (checked).
    E("HUN", "D5.oaths", "Istenre", "Allahra (ﷻ)", count=43),
    E("HUN", "D5.fogadom", "„Fogadom Istennek, hogy iszom", "„Fogadom Allahnak (ﷻ), hogy iszom"),
    E("HUN", "D5.fogadtak", "és Istennek fogadták, hogy", "és Allahnak (ﷻ) fogadták, hogy"),
    # Zayd ibn 'Amr's story «غضب الله… لعنة الله… اللهم»
    E("HUN", "D5.harag", "Isten haragjának", "Allah (ﷻ) haragjának", count=3),
    E("HUN", "D5.atka", "Isten átkának rád eső részét", "Allah (ﷻ) átkának rád eső részét"),
    E("HUN", "D5.atkatol", "Isten átkától", "Allah (ﷻ) átkától"),
    E("HUN", "D5.ozayd", "„Ó Isten, tanúnak hívlak Téged", "„Ó, Allah (ﷻ), tanúnak hívlak Téged"),
    # «فأبى الله إلا أن يكون للدين»
    E("HUN", "D5.abalah", "de Isten úgy akarta", "de Allah (ﷻ) úgy akarta"),
    # «باسمك اللهم»
    E("HUN", "D5.bismika", "„A Te Nevedben, ó, Isten.\"", "„A Te Nevedben, ó, Allah.\""),
    # fn «ليس إلهًا ولا ندا لله»
    E("HUN", "D5.nidd", "nem istennek vagy Isten társának", "nem istennek, sem Allah társának"),
    # «يوشك أن يبعث الله نبيا»
    E("HUN", "D5.yabath", "„Isten hamarosan Prófétát küld", "„Allah (ﷻ) hamarosan Prófétát küld"),
    # «وقد نجاها الله»
    E("HUN", "D5.najjaha", "Isten immár megmentette őket", "Allah (ﷻ) immár megmentette őket"),
    # «واستئصاله أرضى لله»
    E("HUN", "D5.arda", "és megölése elnyeri számukra Isten tetszését", "és kiirtása kedvesebb Allahnak (ﷻ)"),
    # «لا بأس بأمر الله»
    E("HUN", "D5.amr", "Semmi kifogásom Isten rendelése ellen.", "Semmi kifogásom Allah (ﷻ) rendelése ellen."),
    # «بيت الله»
    E("HUN", "D5.bayt", "Elzárjuk Isten Házától", "Elzárjuk Allah (ﷻ) Házától"),
    # al-Muqawqis «أن يدعو على من خالفه» — no "God/curse of God" in the Arabic
    E("HUN", "D5.muqawqis", "hogy Isten átkát hívja le azokra, akik", "hogy átkot kérjen azokra, akik"),
    # «فض الله فاك»
    E("HUN", "D5.fadda", "Hasítsa fel Isten a szádat!", "Hasítsa fel Allah (ﷻ) a szádat!"),
    # Ghassān letter «ولم يجعلك الله»
    E("HUN", "D5.ghassan", "Isten azonban nem szánt téged", "Allah (ﷻ) azonban nem szánt téged"),
    # Najrān «كلمة الله»
    E("HUN", "D5.kalima", "hogy ő Isten Szava", "hogy ő Allah (ﷻ) Szava"),
    # «يدعوهم إلى توحيد الله»
    E("HUN", "D5.tawhid", "az Egy Igaz Isten imádatára", "Allah egyedüli imádatára"),
    # Epilogue «من لا يؤمن بإله» — generic god
    E("HUN", "D5.ilah", "semmilyen Istenben", "semmilyen istenben"),

    # 6. Zayd ibn 'Amr ibn Nufayl: honorifics removed — see d2_mech.py (line-range bound).

    # 7. No softening of the author's statements about the Jews («هذه خلال اليهود»; «فهم إلى اليوم دهاقين الربا… وهم قادة التبرج والعهر»)
    E("HUN", "D7.traits", "Ilyenek némely zsidók jellemvonásai.", "Ilyenek a zsidók jellemvonásai."),
    E("ENG", "D7.traits", "These are the character traits of some of the Jews.", "These are the character traits of the Jews."),
    E("HUN", "D7.usury", "Mind a mai napig ők e világ uzsorájának mesterei közé tartoznak, és némelyek a kicsapongás és a prostitúció vezéralakjai, asszonyaik egyetlen széptevő kezét sem utasítják el.",
      "Mind a mai napig ők e világ uzsorájának mesterei, és ők a kicsapongás és a prostitúció vezéralakjai; asszonyaik egyetlen széptevő kezét sem utasítják el."),
    E("ENG", "D7.usury", "To this day they are among the masters of usury in this world and some are the leaders of libertinism and prostitution, whose women do not reject the hand of any flirt.",
      "To this day they are the masters of usury in this world and they are the leaders of libertinism and prostitution, and their women do not reject the hand of any flirt."),

    # 8. No softening in general — Ḥamzah's taunt «يابن مقطعة البظور»
    E("HUN", "D8.bazr", "»Gyere csak ide, te lánykörülmetélő asszony fia!«", "»Gyere csak ide, te csiklómetsző asszony fia!«"),
    E("ENG", "D8.bazr", "'Come to me, you son of the woman who circumcises girls!'", "'Come to me, you son of the woman who cuts clitorises!'"),

    # 9. Utószó «الصليبية» (×2) — the author's polemical term, not neutral "Christianity"
    E("HUN", "D9.salib1", "és a kereszténységgel, amely a félsziget északán lesben állt", "és a keresztes hatalommal, amely a félsziget északán lesben állt"),
    E("HUN", "D9.salib2", "A kereszténység olyan, mint a kúszónövény az egyenlítőnél:", "A keresztes hatalom pedig olyan, mint a kúszónövény az egyenlítőnél:"),
    E("ENG", "D9.salib1", "and Christianity, which lay in wait in the north of the peninsula", "and the Crusading power, which lay in wait in the north of the peninsula"),
    E("ENG", "D9.salib2", "Christianity is like a creeping vine in the equator: it depends", "As for the Crusading power, it is like a creeping vine in the equator: it depends"),
    E("ENG", "D9.trinity", "the Trinty and vicarious sacrifice", "the Trinity and vicarious sacrifice"),

    # 10. Provenance + Qur'ān-quotation notes reworded
    E("HUN", "D10.prov", "*Magyar fordítás az angol kiadás alapján (International Islamic Federation of Student Organizations / IIFSO, terjeszti: International Islamic Publishing House, átdolgozott második kiadás, 1420 AH / 1999). A hadíszokat",
      "*Magyar fordítás az angol kiadás alapján (International Islamic Federation of Student Organizations / IIFSO, terjeszti: International Islamic Publishing House, átdolgozott második kiadás, 1420 AH / 1999), az arab eredetivel (فقه السيرة) egybevetve; ahol a kettő eltér, a fordítás az arab eredetit követi. A hadíszokat"),
    E("HUN", "D10.quran", "A magyar Korán-idézetek e kiadás angol szövegének fordításai.",
      "A magyar Korán-idézetek ennek az angol szövegnek a fordításai, az arab eredetivel egybevetve: a hivatkozásokat, a kihagyott versrészeket és a téves fordulatokat az eredeti szerint javítottuk."),

    # 11. Pokol capitalised (Jahannam), like Paradicsom
    E("HUN", "D11.a", "vagy örökké tartó pokol lesz.", "vagy örökké tartó Pokol lesz."),
    E("HUN", "D11.b", "[egészen] a pokolba?", "[egészen] a Pokolba?", count=2),
    E("HUN", "D11.c", "Mondd: a pokol tüze", "Mondd: a Pokol tüze"),
    E("HUN", "D11.d", "A pokol bizony körülveszi", "A Pokol bizony körülveszi"),
]
# second batch (Isten occurrences found after the first pass; each checked against the AR)
EDITS += [
    E("HUN", "D5.khadhala", "De akit Isten elhagy, az elhagyatott.", "De akit Allah (ﷻ) elhagy, az elhagyatott."),          # «من يخذل الله يُخذل»
    E("HUN", "D5.harag2", "„Csak Isten haragjától menekülök", "„Csak Allah (ﷻ) haragjától menekülök"),                  # «ما أفر إلا من غضب الله»
    E("HUN", "D5.hanif", "és Istenen kívül senkit sem imádott.", "és Allahon kívül senkit sem imádott.", count=2),     # «ولا يعبد إلا الله»
    E("HUN", "D5.hatib", "mi akadályozta meg abban, hogy Isten átkát hívja le rájuk?", "mi akadályozta meg abban, hogy Allahhoz (ﷻ) fohászkodjék ellenük, és Ő elpusztítsa őket?"),  # «أن يدعو الله عليهم فيهلكهم»
    E("HUN", "D5.ahabb", "a mi hitünk kedvesebb-e Istennek,", "a mi hitünk kedvesebb-e Allahnak (ﷻ),"),                # «أديننا أحب إلى الله»
    E("HUN", "D5.gift", "ha a pátriárka hisz Allahban (ﷻ), az egyetlen imádatra méltó Istenben.", "ha a pátriárka egyedül Allahban (ﷻ) hisz."),  # «الإيمان بالله وحده»
    E("HUN", "D5.jazak", "„Nem. Isten jutalmazzon meg érte,", "„Nem. Allah (ﷻ) jutalmazzon meg érte,"),                # «جزاك الله خيرا»
    E("HUN", "D5.lailah", "„Ma nincs Isten, Banū Bakr!", "„Ma nincs isten, Banū Bakr!"),                               # «لا إله اليوم» (ilāh)
]
