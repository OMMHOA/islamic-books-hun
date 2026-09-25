# Ch3 part 2 (Abesszínia → A szomorúság éve) — see opus55-findings.md "Ch3 part 2"
from apply import E

HUN_Q53 = "(És a felforgatott [városokat] Ő döntötte romba, és beborította őket az, ami beborította. Urad mely jótéteményeiről vitatkozol hát? Ez egy intő a régi intők közül. Közeledik a közelgő [Óra]; senki más, csak Allah fedheti fel. Csodálkoztok-e hát ezen a beszéden, és nevettek, és nem sírtok, miközben hanyagul mulatoztok?) (Korán 53: 53–61)"
ENG_Q53 = "(And the Overthrown Cities He destroyed, So that there covered them that which did cover. Concerning which then, of the bounties of your Lord, can you dispute? This is a warner of the warners of old. The threatened Hour is nigh. None beside Allāh can disclose it. Marvel you then at this statement, And laugh and not weep, While you amuse yourselves?) (Qur'ān 53: 53-61)"

EDITS = [
    E("HUN", "3.gt", "\n>\n", "\n\n", count=3),
    E("HUN", "3.1431", "Ha a tudósok teljesen tudatában lettek volna hamis voltának, egyáltalán nem lett volna szabad feljegyezni.", "Bár hamissága és romlottsága egyetlen tudós előtt sem volt rejtve, soha nem lett volna szabad feljegyezni."),
    E("ENG", "3.1431", "Had the scholars been fully aware of its spuriousness it never should have been recorded at all.", "Although its spuriousness and corruption were hidden from no scholar, it never should have been recorded at all."),
    E("HUN", "3.1433", "abból egy vadkan meg egy patkány esett ki, s azok az ürülékhez rohantak és felfalták.", "abból egy hím és egy nőstény disznó esett ki; majd megsimogatta a disznót, és abból a patkány esett ki. A disznók az ürülékhez rohantak és felfalták."),
    E("ENG", "3.1433", "a boar and a rat fell from it and they rushed to the droppings and devoured them.", "a male and a female pig fell from it; then he stroked the pig, and the rat fell from it. The pigs rushed to the droppings and devoured them."),
    E("HUN", "3.1437a", "Így amikor a Próféta (ﷺ) zengő hangja a szúra végéhez ért, az igazság félelmetes ereje összezúzta", "Amikor a Próféta (ﷺ) dörgő intelmeitől zengő hangja eljutott Allah e szavaihoz:\n\n" + HUN_Q53 + "\n\n— az igazság félelmetes ereje összezúzta"),
    E("ENG", "3.1437a", "So when the Prophet's (ﷺ) resounding voice reached the end of the Sūrah, the awesomeness of the truth had crushed", "When the Prophet's (ﷺ) voice, thundering with its warnings, reached the words of Allāh:\n\n" + ENG_Q53 + "\n\n— the awesomeness of the truth crushed"),
    E("ENG", "3.1437b", "they felt ashamed of themselves and wanted to make an excuse for what they did. They felt ashamed of themselves and wanted to make an excuse for what they did.", "they felt ashamed of themselves and wanted to make an excuse for what they did."),
    E("HUN", "3.1437c", "„Ma bizony az égből szóltál, Mohamed (ﷺ).\"", "„Ma az égből szóltak-e hozzád, Mohamed (ﷺ)?\""),
    E("ENG", "3.1437c", "\"Today you have indeed spoken from heaven, Muhammad (ﷺ).\"", "\"Were you spoken to from heaven today, Muhammad (ﷺ)?\""),
    E("HUN", "3.1443", "'Amr ibn ul 'Ās", "'Amr ibn al-'Āṣ"),
    E("ENG", "3.1443", "'Amr ibn ul 'Ās", "'Amr ibn al-'Āṣ"),
    E("HUN", "3.1449", "Megparancsolta az ima megtartását és a böjtöt.", "Megparancsolta az ima megtartását, a böjtöt és a zakātot."),
    E("ENG", "3.1449", "He ordered us to establish prayer and fast.", "He ordered us to establish prayer, to fast and to pay zakāh."),
    E("HUN", "3.1457a", "„Menjetek békében.", "„Menjetek, biztonságban vagytok."),
    E("ENG", "3.1457a", "\"Go in peace.", "\"Go, you are safe."),
    E("HUN", "3.1457b", "és az emberek nem vetették alá magukat nekem, hogy Vele szemben engedelmeskedjem nekik.\"", "és Ő sem engedett az embereknek az én ügyemben, hogy én engedjek nekik az Ő ügyében.\""),
    E("ENG", "3.1457b", "and the people did not submit to me so that I might obey them concerning Him.\"", "nor did He obey the people concerning me, that I should obey them concerning Him.\""),
    E("HUN", "3.1467", "„Ó, Abū 'Amarah!", "„Ó, Abū 'Umārah!"),
    E("ENG", "3.1467", "\"O Abū 'Amarah!", "\"O Abū 'Umārah!"),
    E("HUN", "3.1513", "Azért siettek, mert könnyű győzelemre számítottak, és mert nem hittek a halál utáni feltámadásban, sem jutalomban és büntetésben.", "Azért siettek, mert nevettek rajta, hiszen nem hittek a halál utáni feltámadásban, sem jutalomban és büntetésben."),
    E("ENG", "3.1513", "They were in a hurry because they thought it was an easy victory, and because they did not believe in a resurrection after death or a reward and punishment.", "They were in a hurry because they laughed at it, having no belief in a resurrection after death or in reward and punishment."),
    E("HUN", "3.1525a", "'Athikah bint 'Abdul Muṭṭalib", "'Ātikah bint 'Abdul Muṭṭalib"),
    E("ENG", "3.1525a", "'Athikah bint 'Abdul Muṭṭalib", "'Ātikah bint 'Abdul Muṭṭalib"),
    E("HUN", "3.1525b", "Abū Hakam (azaz Abū Jahl)", "Abū al-Ḥakam (azaz Abū Jahl)"),
    E("ENG", "3.1525b", "Abū Hakam (That is, Abū Jahl)", "Abū al-Ḥakam (that is, Abū Jahl)"),
    E("HUN", "3.1573", "Khatm al Hajumra", "Khaṭm al-Ḥajūnra"),
    E("ENG", "3.1573", "Khatm al Hajum", "Khaṭm al-Ḥajūn"),
    E("HUN", "3.1595", "Khadījah ezzel szemben az asszonyok igaza volt.", "Khadījah pedig az asszonyok közt az igazmondó (ṣiddīqah) volt."),
    E("HUN", "3.1597", "„A Quraish nem tudott rávenni semmire, amit nem szerettem, Abū Ṭālib haláláig.\"", "„A Quraish semmi olyat nem tett velem, ami bántott volna, míg Abū Ṭālib meg nem halt.\""),
    E("ENG", "3.1597", "\"The Quraish were unable to make me do anything which I disliked until the death of Abū Ṭālib.\"", "\"The Quraish did not inflict on me anything I disliked until Abū Ṭālib died.\""),
    E("HUN", "3.1605", "holtan Badr napján, az árokba vetve (amelyet a csata után ástak a halottaknak).\"", "holtan Badr napján; aztán a kútba, Badr kútjába vonszolták őket.\""),
    E("ENG", "3.1605", "killed on the day of Badr and thrown into the trench (which was dug for the dead after the battle).\"", "killed on the day of Badr; then they were dragged to the well, the well of Badr.\""),
]
