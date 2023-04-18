import json
import pandas as pd

# Sample JSON data
data = [

  {
    "caption": "Neuvěřitelný týden!! 🚂🚂Nejlepší softbal v celé Evropě a skončili jsme na 4. místě (nejlépe z celé české republiky). Jediný v top 4 bez neevropského pickupu🔥Hráli jsme opravdu skvělý softbal, ukázali jsme naši sílu a vytrvalost po celou dobu turnaje a nikomu jsme nebyli snadným soupeřem💪Dávejte si bacha MY JSME LOCOS a další rok si jdeme pro vás 😤\n\nWhat a incredible week!! 🚂🚂The best softball in all of Europe and we finished in 4th place (the best of the whole Czech Republic). The only one in the top 4 without a non-European pick-up🔥We played really great softball, we showed our strength and tenacity throughout the tournament and we were no easy opponent to anyone💪Watch out WE ARE LOCOS and next year we are coming for you 😤\n\n#locos #parasiempreloco #incredible #softball #softballlife #best #friends #family #oneteam #onegoal",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/Chz6fROK3iT/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 178,
    "timestamp": "2022-08-28T17:13:49.000Z"
  },
  {
    "caption": "After a long season we achieved 3rd place and a dream spot on the Supercup 🥉🚂🔥\n\nPo dlouhé sezóně vybojované 3.místo a vysněné místo na Supercupu. 🥉🚂🔥\n\n#locos#vamos#jedentymjedencil#stepbysteptothetop#DONE",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CVLkqnyqC1Y/",
    "commentsCount": 7,
    "firstComment": "Congratulations Locos,  well done",
    "likesCount": 205,
    "timestamp": "2021-10-18T18:56:47.000Z"
  },
  {
    "caption": "🔥 WE ARE STARTING TOMORROW 🔥\n\n- FOR THE TITLE OF THE WORLD CHAMPION\n- FIVE GUYS FROM @breclavsoftball IN CZECH U23  NATIONAL SOFTBALL TEAM @czechsoftball 🇨🇿\n\n#czechsoftball #softballeurope #europeansoftball #mensfastpitch #worldchsmpionship #worldcup #softballworldcup #u23softballwc #parasiempreloco",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CrBubY1AGr7/",
    "commentsCount": 2,
    "firstComment": "👏❤️",
    "likesCount": 84,
    "timestamp": "2023-04-14T18:47:16.000Z"
  },
  {
    "caption": "🇨🇿Turnaj na Kanárských ostrovech, kde jsme celkově obsadili druhé místo \n\n🇬🇧Tournament in Canary Islands where we took second place overall 💪\n.\n.\n.\n.\n.\n\n#locos#softball#czechsoftball#europeansoftball#fun#funtime#sport#moravia#southmoravia#extraleagueteam#onegoal",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CpuUDc2K19U/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 156,
    "timestamp": "2023-03-13T09:12:56.000Z"
  },
  {
    "caption": "Od čtvrka 2.2. do soboty 4.2. se mix děvčat žákyň a kadetek Locos Břeclav zúčastnilo mini soustředění ve Starém Hrozenkově. \nCílem soustředění bylo především stmelení kolektivu, včetně \"taktické\"  přípravy na zápasy. \nV sobotu se přímo ze soustředění přesunuli na turnaj Moravské ligy kadetek do nedalekého Starého Města, kde absolvovali čtyři kvalitní zápasy ze soupeři @snailskunovice @skseverbrno @trnava.panthers.softball @softball_cats_brno. Nešlo především z naší strany ani tak o samotné výsledky, jak o to, aby si děvčata na samotnou kadetskou soutěž a následné jarní mistrovské soutěže zvykla a jak se říká \"osahala\". 🥎\nNa celém programu soustředění a koučování turnaje se značnou měrou podílela naše začínající mládežnická trenérka a zároveň současná hráčka Severu Brno Lucka Kociánová, za což jí patří velké poděkování. 🚂\n.\n.\n.\n.\n\n#locos#softball#czechsoftball#europeansoftball#fun#funtime#sport#moravia#southmoravia#extraleagueteam#onegoal",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CoXO4QPKqsn/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 94,
    "timestamp": "2023-02-07T13:33:47.000Z"
  },
  {
    "caption": "Last training session before U23 world Cup! 🇦🇷",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CqpojfUqCWg/",
    "commentsCount": 2,
    "firstComment": "Brno",
    "likesCount": 320,
    "timestamp": "2023-04-05T10:13:13.000Z"
  },
  {
    "caption": "Dva naši borci se vypravili sbírat cenné zkušenosti s národním týmem do Japonska🇯🇵Let´s go Locos 👏",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/Cjz915vqGWa/",
    "commentsCount": 4,
    "firstComment": "🔥🔥 easel",
    "likesCount": 233,
    "timestamp": "2022-10-17T10:45:55.000Z"
  },
  {
    "caption": "Po dlouhém víkendu si odnášíme 2 výhry (4:3,4:1) nad @spectrumpraha a vedeme tak v semifinálové sérii 2:0. Děkujeme všem fanouškům za podporu 🤙\n\nAfter a long weekend, we take home 2 wins (4:3,4:1) over @spectrumpraha and lead the semifinal series 2:0. Thanks to all the fans for their support 🤙",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CiqMIr6KfAF/",
    "commentsCount": 1,
    "firstComment": "👏",
    "likesCount": 138,
    "timestamp": "2022-09-18T19:07:01.000Z"
  },
  {
    "caption": "Už v sobotu začíná naše semifinále proti @spectrumpraha 🚂 Přijďte podpořit naše borce v cestě za titulem 🔥začínáme v 13:45 na hřišti Casa de Locos \n\nOur semifinal against @spectrumpraha starts on Saturday 🚂 Come and support our players on their way to the title 🔥starting at 13:45 at Casa de Locos",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CidVL35q872/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 115,
    "timestamp": "2022-09-13T19:15:58.000Z"
  },
  {
    "caption": "Ukázka naší Locos obrany🔥která play vám přijde nejlepší ? \n\nA couple of plays from our Locos defense🔥which play looks the best to you ? \n\n1) @antonsbrown ——> @ludekoplustil caught steal 🤙\n\n2) @martin.magula ——> @tobiasholmelund close out from bunt to 3th base 🔥\n\n3) @ma_name_george laser throw to 3th base 💥\n\n4) @vbuchner_ ——> @tobiasholmelund close out from bunt to 1st base 🌪\n\n5) @tobiasholmelund overhead catch 💪",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/Ch5F5skKPek/",
    "commentsCount": 5,
    "firstComment": "🔥🔥",
    "likesCount": 156,
    "timestamp": "2022-08-30T17:29:45.000Z"
  },
  {
    "caption": "Úžasný výkon našeho hráče @maik.48 na přípravném předsezóním turnaji na Floridě💪 Maik zde nadhazoval za tým @hilluchiefs jež je historicky jedním z nejúspěšnějších týmu na světě. Jen tak dále 😤\n\n#beast \n\nAmazing performance of our player @maik.48 at the pre-season tournament in Florida💪 Maik pitched for @hilluchiefs which is historically one of the most successful teams in the world. Keep it up 😤",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/Cn_5p_oqTx7/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 125,
    "timestamp": "2023-01-29T12:05:48.000Z"
  },
  {
    "caption": "Včera se nám dařilo jak v obraně tak v útoku a vyrovnáváme sérii na 1:1. Pokračujeme další sobotu v mostě 🧨🚂\n\nYesterday, we did well both defensively and offensively to even the series at 1-1. We continue next Saturday in Most 🧨🚂\n\n#softball #czechsoftball #europeansoftball #extraleague #friends #fun #funtime #homeruns #homerunsports #power #win #victory",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CjQLZG_KcyZ/",
    "commentsCount": 1,
    "firstComment": "👏",
    "likesCount": 187,
    "timestamp": "2022-10-03T13:11:40.000Z"
  },
  {
    "caption": "Vysněné finále je tady !! V sobotu 1.10.2022  v 13:45 začíná naše zápasová série o titul na hřišti Casa de Locos🚂 doveďte přátele a rodinu, vemte pivko a přijďte podpořit naše borce v cestě za prvním extraligovým titulem. \n\n#parasiempreloco \n\nThe dream final is here !! On Saturday 1.10.2022 at 13:45 our game series for the title starts on Casa de Locos field 🚂 bring your friends and family, grab a beer and come and support our players in their quest for the first extraleague title. \n\n#parasiempreloco",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CjA9xF0Kbjy/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 106,
    "timestamp": "2022-09-27T15:24:00.000Z"
  },
  {
    "caption": "Letos na SuperCup přicházíme se třemi posilami. První dvě jsou borci z Dánska @tobiasholmelund a @antonsbrown kteří také hrají za dánský nároďák 🤙třetí posilou je také reprezentant @vbuchner_ který již jednou v historii naše barvy hájil při postupu do extraligy💪Všichni tři hráči nám budou významnými oporami během klubového mistrovství Evropy, které začíná už v pondělí 🚂 \n\nThis year we are bringing three pick-ups to the SuperCup. The first two are the Danish players @tobiasholmelund and @antonsbrown who also play for the Danish national team 🤙The third pick-up is also the national team player @vbuchner_ who has already defended our colours once in the history of the league💪All three players will be important supports for us during the European Club Championship, which starts on Monday 🚂\n\n#locos#softball#czechsoftball#europeansoftball#fun#funtime#sport#moravia#southmoravia#extraleagueteam#onegoal #parasiempre #vamos",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/ChbI_t4DcZD/",
    "commentsCount": 2,
    "firstComment": "👏",
    "likesCount": 137,
    "timestamp": "2022-08-19T02:19:34.000Z"
  },
  {
    "caption": "V sobotu se konalo poslední kolo nadstavby a my v ní čelili Chomutovu. Zápasy jsme oba dva vyhráli o bod (4:3, 7:6) i přes chybějící 4 klíčové hráče👏na druhou stranu @beaverschomutov také postrádal 2 klíčové hráče. Za celý víkend mohlo vyniknout spoustu mladých hráčů, kteří  získávali extraligové zkušenosti🔥play-off pro nás začíná třetí týden v září. Momentálně se všichni soustředíme na SuperCup, kde nás už posílí naši hráči z Ameriky💪\n\nOn Saturday was the last round of the playoffs and we faced Chomutov. We won both games by a point (4:3, 7:6) despite missing 4 key players👏on the other hand @beaverschomutov was also missing 2 key players. Lots of young players could stand out over the weekend gaining extra league experience🔥play-offs start 3rd week of September for us. At the moment we are all focused on the SuperCup, where we are already reinforced by our players from America who are currently participating in the ISC tournament💪\n\n#locos #parasiempreloco #softball #czechsoftball #extraleague #playoff #supercup #season #friends #fun #funtime",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/ChU0ndpOF29/",
    "commentsCount": 1,
    "firstComment": "😮👏❤️",
    "likesCount": 101,
    "timestamp": "2022-08-16T15:26:03.000Z"
  },
  {
    "caption": "Naše poslední zápasy základní části nám zaručili 1. místo po základní skupině. 💪🏼\n.\nOur last games placed us on top of the league, after first part of the season. \n.\n.\n.\n.\n#softball #locos #softbal #baseball #game #sport #hitting #fielding #czechsoftball",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/Cf9lnmuKmSH/",
    "commentsCount": 1,
    "firstComment": "👏😍",
    "likesCount": 51,
    "timestamp": "2022-07-13T18:21:05.000Z"
  },
  {
    "caption": "O víkendu se konal turnaj na Lokomotivě, kterého se účastnili i naši žáci. 🥎 Celý turnaj byla skvělá atmosféra a přispěl k celkové zimní přípravě na následující sezónu 💪 jen tak dále 🚂 \n\nAt the weekend there was a tournament at Lokomotiva Area, which was also attended by our pupils. 🥎 The whole tournament was a great atmosphere and contributed to the overall winter preparation for the next season 💪 keep it up 🚂 \n.\n.\n.\n.\n#softball #czechsoftball #youngguns #tournament #friends \n#fun #funtime",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CoU_cLmqC6-/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 77,
    "timestamp": "2023-02-06T16:40:24.000Z"
  },
  {
    "caption": "First two games of the season and 4 homers💣",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CpQIURCKJ45/",
    "commentsCount": 5,
    "firstComment": "🔥🔥🔥👍👍",
    "likesCount": 164,
    "timestamp": "2023-03-01T15:55:09.000Z"
  },
  {
    "caption": "První zapas jsme vyhráli 20:2 proti Německu🔥pokračujeme zítra proti @horsholmhurricanes !!\nZápasy najdete na @wbsc_europe \n\nWe won first game 20:2 agains German national team 💪 tomorrow we play against @horsholmhurricanes. Watch the stream on @wbsc_europe 🤙",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/ChnLul7Kl6l/",
    "commentsCount": 1,
    "firstComment": "📸 @gregavalancic",
    "likesCount": 151,
    "timestamp": "2022-08-23T18:34:20.000Z"
  },
  {
    "caption": "Dnes v dresu AWP Lumberjacks hrál i náš hráč @maik.48 kdy v sedmé směně porazili úřadující šampiony @hilluchiefs walk-off homerunem @gojeda34 🔥🔥Maik odházel polovinu zápasu společně s @nikkidickydo a udrželi Hill United pouze na pěti bodech a postupují tak mezi TOP6 týmů. Skvěle vidět našeho nadhazovače mezi světovou špičkou🤙\n\nOur player @maik.48 played today in the AWP Lumberjacks jersey when they beat the reigning champions @hilluchiefs with a walk-off home run in the seventh inning by @goyeda34 🔥🔥Maik threw half the game along with @nikkidickydo and held Hill United to only five runs and advanced to the Top 6 teams. Great to see our pitching among the world's top🤙\n\n#locos#softball#czechsoftball#europeansoftball#fun#funtime#sport#moravia#southmoravia#extraleagueteam#onegoal #bigmaik",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/ChdUuztvtoI/",
    "commentsCount": 2,
    "firstComment": "👏😮",
    "likesCount": 176,
    "timestamp": "2022-08-19T22:40:36.000Z"
  },
  {
    "caption": "O víkendu nás čeká další kolo nadstavby. Začínáme v sobotu proti @beaverschomutov v 12:45. Neseďte doma a přijďte podpořit naše borce 🚂\n\nNext weekend we have another round of the extraleague. We start on Saturday against @beaverschomutov at 12:45. Don't sit at home and come and support our guys 🚂",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/ChHxpS6Oe0A/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 98,
    "timestamp": "2022-08-11T13:49:58.000Z"
  },
  {
    "caption": "Po kratší posezónní pauze se 5 našich borců vypravilo reprezentovat Českou republiku 🇨🇿na mistrovství světa, které se koná Novém Zélandu 🇳🇿🥎 Všichni naši hráči jsou výraznými oporami týmu a předvádí skvělé výkony 💪Zápasy se vždy vysílají na Maori+ a WBSC livestream. \n\n📸 @paulopics.nz \n\nAfter a short post-season break, 5 of our players went to represent the Czech Republic 🇨🇿at the World Championship in New Zealand 🇳🇿🥎 All of our players are strong pillars of the team and are performing well 💪The matches are always broadcast on Maori+ and WBSC livestream. \n\n📸 @paulopics.nz",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/ClkVRNQvxvG/",
    "commentsCount": 3,
    "firstComment": "Looking good boys! Nice diving catch George 👌🏻 \nKeep enjoying softball, play like there is no tomorrow and succes will happen 👏👏",
    "likesCount": 151,
    "timestamp": "2022-11-30T02:05:34.000Z"
  },
  {
    "caption": "🥇2022 CHAMPIONS 🥇\n\n#nowordsneeded",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/Cji43BOKJA_/",
    "commentsCount": 5,
    "firstComment": "Check dm",
    "likesCount": 170,
    "timestamp": "2022-10-10T19:35:17.000Z"
  },
  {
    "caption": "Už v neděli vypukne v Břeclavi velké finále, kde se rozlouskne, kdo se stane vítězem chlapské extraligy. Přijďte s kamarády a rodinou podpořit naše borce a udělat pořádný kotel🧨Začínáme ve 11:45 na Hřišti Casa de Locos 🚂🔥\n\nOn Sunday, the grand final will take place in Breclav, where the winner of the men's extraliga will be decided. Come with your friends and family to support our players and make noise🧨Starting at 11:45 am at the Casa de Locos field 🚂🔥",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CjcaiYTKvDH/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 147,
    "timestamp": "2022-10-08T07:14:53.000Z"
  },
  {
    "caption": "Včerejší zapas jsme vyhráli a postoupili ze skupiny na druhém místě. Dneska jsme vyhráli první zápas play-off (7:0) 🔥zítra pokračujeme v 12 hodin v Eagles parku. Sledujte naše borce na WBSC Europe🤙\n\nWe won yesterday's match and advanced from the group in second place. Today we won the first match of the playoffs (7:0) 🔥 Tomorrow we continue at 12 am at Eagles Park. Follow our players on WBSC Europe🤙",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/ChsXQwKq82Y/",
    "commentsCount": 2,
    "firstComment": "some home run",
    "likesCount": 147,
    "timestamp": "2022-08-25T18:51:19.000Z"
  },
  {
    "caption": "Třetí semifinálový zápas jsme včera zvládli a vyhráli 11:1. Postupujeme tak přímo do finále 🚂\n\nWe managed the third semifinal game yesterday and won 11:1. So we are going straight to the finals 🚂\n\n#unstoppable",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/Ci7QRB4q2At/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 146,
    "timestamp": "2022-09-25T10:10:12.000Z"
  },
  {
    "caption": "Rovnou pět našich borců se dostalo do nominace na MS U23 v Argentině, kde budou klíčovými hráči na cestě za medailí 💪 velká gratulace \n\nFive of our guys were nominated for the U23 World Championships in Argentina, where they will be key players on the way to the medal 💪 big congratulations \n.\n.\n.\n.\n.\n.\n\n#locos#softball#czechsoftball#europeansoftball#fun#funtime#sport#moravia#southmoravia#extraleagueteam#onegoal",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CoXVhr7Kcpt/",
    "commentsCount": 3,
    "firstComment": "😮😮",
    "likesCount": 152,
    "timestamp": "2023-02-07T14:31:52.000Z"
  },
  {
    "caption": "Souhrn jedněch z mála opravdu tvrdých hitů💥\n\nCouple of really hard hits from Supercup 💥 \n\n1) Clutch homerun by @ma_name_george 💣\n\n2) @ludekoplustil hit the fence with RBI double 💥\n\n3) Missile to top of the fence by @tobiasholmelund 🔥\n\n4) Moon shot 2 run homerun by @adam_lunak ☄️ \n\n5) Nuke to the fence by @martin.magula 🧨\n\n#homeruns #hits #nukes #missiles #dingers #moonshots #rockets #watchout #onfire🔥 #offense #hugelineup #locos #letsgo #friends #family #supercup \n\n📸 @gregavalancic \n\n@softball_europe @softballclassics @czechsoftball",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/Ch6nS55qzDi/",
    "commentsCount": 4,
    "firstComment": "👏👏👏",
    "likesCount": 173,
    "timestamp": "2022-08-31T07:40:48.000Z"
  },
  {
    "caption": "O víkendu se naše děvčata zúčastnila turnaje v areálu Sk Joudrs Praha🔥🥎 Atmosféra na turnaji byla výborná a turnaj hodně přispěl k celkové zimní přípravě na další sezónu💪. \n\nAt the weekend our girls took part in a tournament in the area of Sk Joudrs Praha🔥🥎 Atmosphere at the tournament was excellent and the tournament contributed a lot to the overall winter preparation for the next season💪",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/CnmXOxYqPrf/",
    "commentsCount": 1,
    "firstComment": "👏",
    "likesCount": 115,
    "timestamp": "2023-01-19T14:03:59.000Z"
  },
  {
    "caption": "Tři úžasné týdny, plné potu krve a slz prožilo hned pět našich hráčů na MS na Novém Zélandu a ukončilo tím jejich dlouhou sezónu. 🚂Všichni naši borci byli oporami národního týmu a předvedli na MS skvělé výkony 💪💪💪 \n\n@maik.48 ERA: 2,42 SO: 31\n\n@kuba.osicka ERA: 2,49 SO: 49\n\n@martin.magula AVG: 0,412 OBP: 0,517 \n\n@vojtech_forman RBI: 10 HR: 2\n\n@ma_name_george  AVG: 0,381 HR: 2\n\nPro 4/5 našich hráčů to bylo první mužské MS a rozhodně ne poslední 😤\n\nThree amazing weeks, full of blood sweat and tears, were experienced by five of our players at the World Championships in New Zealand, ending their long season. 🚂All of our players were mainstays of the national team and delivered great performances at the World Championships 💪💪💪 \n\n@maik.48 ERA: 2.42 SO: 31\n\n@kuba.osicka ERA: 2.49 SO: 49\n\n@martin.magula AVG: 0.412 OBP: 0.517 \n\n@vojtech_forman RBI: 10 HR: 2\n\n@ma_name_george AVG: 0.381 HR: 2\n\nFor 4/5 of our players it was the first men's WC and definitely not the last 😤\n\n#locos#softball#czechsoftball#europeansoftball#fun#funtime#sport#moravia#southmoravia#extraleagueteam#onegoal",
    "ownerFullName": "Locos Břeclav",
    "ownerUsername": "breclavsoftball",
    "url": "https://www.instagram.com/p/ClvKFgvP2k5/",
    "commentsCount": 3,
    "firstComment": "Send Pic @NEW_ZEALAND_TIMES 🌐",
    "likesCount": 148,
    "timestamp": "2022-12-04T06:59:29.000Z"
  },
  {
    "caption": "Nemusíte vždy k nám na hřiště, aby se vaše děti dozvěděly o softballu. Jezdíme také po školách, kde žáčkům ukazujeme, kolik legrace si hrou můžou užít!💪\n#painbustersmost #♥️🐍🖤 \n\n📸 @lenka_bakuus",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CqiLjuhteyM/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 69,
    "timestamp": "2023-04-02T12:39:12.000Z"
  },
  {
    "caption": "Mezi nejlepšími sportovci města Mostu jsme se umístili i my - a nejen jednou! Více info v biu💪\n#painbustersmost #czechsoftball #❤️🐍🖤",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CoP9pWctRCb/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 85,
    "timestamp": "2023-02-04T17:48:31.000Z"
  },
  {
    "caption": "Sezóna už je za rohem a my trénujeme na plné obrátky!\n#painbustersmost #❤️🐍🖤",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CpuO1Evglj7/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 75,
    "timestamp": "2023-03-13T08:27:16.000Z"
  },
  {
    "caption": "Vánoce jsou za dveřmi! Skočte si také do našeho nového výběru a potěšte svého oblíbeného hráče, nebo fanouška💪",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CmIqtjvtafP/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 59,
    "timestamp": "2022-12-14T04:45:36.000Z"
  },
  {
    "caption": "Děkujeme všem, kteří s námi sdíleli radost ze softballu a už se těšíme na další rok! ❤️🐍🖤",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/Cmjb99NtVNG/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 83,
    "timestamp": "2022-12-24T14:16:15.000Z"
  },
  {
    "caption": "Už v sobotu začne český reprezentační tým MS mužů zápasem proti Novému Zélandu💪\n#painbustersmost #menssoftballworldcup #czechsoftball \n\nPhoto by @kouba_vladimir",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/ClVmhKfgr0y/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 129,
    "timestamp": "2022-11-24T08:47:41.000Z"
  },
  {
    "caption": "První finálovou účast v nejvyšší soutěži mužů loni zažili mostečtí softballisté a díky stříbrné medaili 🥈 se letos představí také na evropském poháru Super Cup. Jaké cíle mají Painbusters Most do letošní sezóny a na co se klub v rámci areálu nyní soustředí? Preview s Adamem Šuchou 🗣️\n\n#czechsoftball #season2023",
    "ownerFullName": "Czech Softball",
    "ownerUsername": "czechsoftball",
    "url": "https://www.instagram.com/p/Cq5Jrk-LJ2-/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 163,
    "timestamp": "2023-04-11T10:46:39.000Z"
  },
  {
    "caption": "A tak jsme zahájili zimní přípravu! Během dvou úspěšných akcích, nově v prostorách @pontestudio3 , byl rozdám nespočet ocenění ze strany klubu jeho hráčům. Děkujeme všem za účast💪",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/Cks8dVctcDi/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 65,
    "timestamp": "2022-11-08T13:50:32.000Z"
  },
  {
    "caption": "Klub má posezónní pauzu, soft si ovšem dopřáváme i mimo domácí pole. Na Open poháru v Chomutově jste tento víkend mohli vidět @jstroleny a @krivanekadam v dresech @pikespraha, @vitoralek zase po dlouhé době oblékl dres Tunnellers💪\n#openpohar #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/Cj4ksImMIKX/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 100,
    "timestamp": "2022-10-19T05:42:20.000Z"
  },
  {
    "caption": "Česká repre se odstěhovala na týden do Japonska! \nNa soustředění juniorů už mají hráči za sebou pár zápasů s domácími týmy. Čekáme, jaké novinky přivezou tyhle tři borci zpět💪\n#reprezentacecru18 #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/Cj0y7w9NKHr/",
    "commentsCount": 11,
    "firstComment": "Co je to za děti?",
    "likesCount": 193,
    "timestamp": "2022-10-17T18:29:50.000Z"
  },
  {
    "caption": "Mistrovství ČR v žákovské lize se rozjede zítra na Hippos Stadium💪\n#painbustersmost #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjYqotJsIiv/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 34,
    "timestamp": "2022-10-06T20:18:36.000Z"
  },
  {
    "caption": "“Druhé místo získává tým Painbusters Most!”🥈\nJe to tak. Po mnohých eskapádách, zvratech a nekonečném napětí si náš extraligový tým odváži z břeclavi stříbrnou medaili! \nDíky, chlapi❤️🐍🖤\n \nDěkujeme také @breclavsoftball za to, jakým skvělým oponentem ve finále byli a gratulujeme k vítězství. Samozřejmě díky patří i všem, kteří nás podporovali při celý týhle šílený cestě. \n\nTím ELM pro rok 2022 končí a my pokračujeme za dalšími úspěchy💪\n#painbustersmost #extraliga #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjhN7mVqR87/",
    "commentsCount": 3,
    "firstComment": "Supeer",
    "likesCount": 125,
    "timestamp": "2022-10-10T04:00:56.000Z"
  },
  {
    "caption": "Za zmínku rozhodně také stojí úsilí našich kadetů na finálovém turnaji. Ačkoliv se neumístil, rozhodně si s sebou do další sezóny berou spoustu nových dovedností💪\n📷 @stanislavstys & @e.stysova \n#painbustersmost #czechsoftball #❤️🐍🖤",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjVZ-_aMtcQ/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 88,
    "timestamp": "2022-10-05T13:55:22.000Z"
  },
  {
    "caption": "Už je nás tu 500🤩\nZa letošní sezónu se k nám přidalo nespočet lidí a za to vám všem moc děkujeme. Pojďme dělat dál to co nás baví a ukažme ostatním, jak super to je💪\n#❤️🐍🖤 #500followers",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CkQYcXvMkFs/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 54,
    "timestamp": "2022-10-28T11:37:06.000Z"
  },
  {
    "caption": "Recap finálové série ELM💪\n#painbustersmost #extraliga #czechsoftball #❤️🐍🖤",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/Cj-b3XGsqOR/",
    "commentsCount": 2,
    "firstComment": "👏",
    "likesCount": 93,
    "timestamp": "2022-10-21T12:20:40.000Z"
  },
  {
    "caption": "Hřiště je zahalené pod mlhou, tribuny pod plachtou a šatny zejí prázdnotou. Hřiště je připravené na zimu. Nám s počátkem listopadu začíná makačka💪\n#painbustersmost #❤️🐍🖤",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CkYfVS4tbJh/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 71,
    "timestamp": "2022-10-31T15:11:13.000Z"
  },
  {
    "caption": "Náš nový homerunový plot se plní banery sponzorů! Pokud máte zájem o propagaci na našem hřišti, neváhejte nás kontaktovat💪",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjrlKGLjznV/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 65,
    "timestamp": "2022-10-14T04:47:22.000Z"
  },
  {
    "caption": "Prodloužený víkend ve znamení honu za vůní medaile podstoupí tentokrát kadetský tým. Teď mohou ukázat co v nich je💪\n#painbustersmost #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjGpAJFspRK/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 53,
    "timestamp": "2022-09-29T20:17:59.000Z"
  },
  {
    "caption": "Blyští se i umístění coachballu! Na finále mistrovství ČR se děti do 11 let umístily třetí💪\n#painbustersmost #coachball #czechsoftball #❤️🐍🖤",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/Ci-hL11M9h0/",
    "commentsCount": 4,
    "firstComment": "Gratulace, jste proste frajeri 🔥😍❤️",
    "likesCount": 90,
    "timestamp": "2022-09-26T16:35:45.000Z"
  },
  {
    "caption": "Bude boj o zlato! Převratným víkendem jsme rozválcovali našeho semifinálového soupeře. Teď nás teprve čeká challenge💪\n#painbustersmost #extraliga #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjAX7YUgdIk/",
    "commentsCount": 2,
    "firstComment": "Gratulace!!! O to větší motivace pro celý tým, protože my víme, jak moc jsou skvělí!! Bojujte, kluci, mate na to! A bez ohledu na výsledek - pro nás budete borci a vždycky těmi nejlepšími. Painbusters jsou jedna velká rodina ❤️🔥❤️ Přesně ta rodina, co drží vždycky při sobě ❤️❤️❤️",
    "likesCount": 135,
    "timestamp": "2022-09-27T09:53:21.000Z"
  },
  {
    "caption": "Rookie finalizuje v Eagles parku 💪\n#painbustersmost #rookieball #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjHnBZ7NfBd/",
    "commentsCount": 1,
    "firstComment": "Držíme palce ❤️",
    "likesCount": 42,
    "timestamp": "2022-09-30T05:19:56.000Z"
  },
  {
    "caption": "Jste připravení? Poslední tři zápasy chlapské nejvyšší soutěže ČR jsou tu! Stav je 1:1 a napětí dosahuje nevídaných hodnot. Kdo ukáže, že kraluje této hře? 👑\nChceme vás vidět v sobotu v Mostě a v neděli v Břeclavi💪\n#painbustersmost #extraliga #finale #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjXEwXQsXh3/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 84,
    "timestamp": "2022-10-06T05:28:21.000Z"
  },
  {
    "caption": "Čekají nás napínavé časy!\nOba týmy si vybraly jeden den, kdy předvedly co dokážou a nyní je stav finálové série 1:1💪\n#painbustersmost #extraliga #finale #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjPXIVoscTH/",
    "commentsCount": 1,
    "firstComment": "❤️👏",
    "likesCount": 118,
    "timestamp": "2022-10-03T05:34:59.000Z"
  },
  {
    "caption": "🥇už čeká! \nSérie zápasů začíná už tento víkend. V sobotu v Břeclavi, v neděli na Ovčíně💪\n#painbustersmost #extraliga #finale #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjFUIUxAlCk/",
    "commentsCount": 6,
    "firstComment": "😮",
    "likesCount": 82,
    "timestamp": "2022-09-29T07:56:22.000Z"
  },
  {
    "caption": "Další úspěšný ples je za námi. Děkujeme všem zúčastněným a jsme rádi, že se si s námi užíváte zábavu💪\n#painbustersmost #❤️🐍🖤",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/Co7gWsMNjyp/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 86,
    "timestamp": "2023-02-21T15:39:09.000Z"
  },
  {
    "caption": "Už zbývá jen pár dní do každoročního softballového plesu Painbusters! Lístků zbývá už jen pár - rychle si o ně napište svým trenérům, ať nepřijdete o šanci se zúčastnit💪",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CoUq1Lwt6Yg/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 31,
    "timestamp": "2023-02-06T13:40:19.000Z"
  },
  {
    "caption": "Chyboval ten, který si nechal ujít sobotní školení. Pod vedením Vojty Albrechta jsme získali nový pohled na pálení a v odpoledním programu nás Matěj Bíža obohatil o možnosti trénování pole. Děkujeme 💪\n#painbustersmost #czechsoftball #❤️🐍🖤\n\nPhoto by @stanislavstys",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/Cnv8cT4N4-X/",
    "commentsCount": 1,
    "firstComment": "👍👍",
    "likesCount": 115,
    "timestamp": "2023-01-23T07:22:18.000Z"
  },
  {
    "caption": "Rookieballové úsměvy z finálového turnaje ❤️🐍🖤\n#painbustersmost #coachball #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CjvZTSktKsI/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 71,
    "timestamp": "2022-10-15T16:09:39.000Z"
  },
  {
    "caption": "Jak se připravit na sezónu lépe, než dvoudenním velikonočním turnajem na @tempofastpitch? My už jsme na cestě!\n#painbustersmost #czechsofball #❤️🐍🖤",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/CqueEevtFWs/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 52,
    "timestamp": "2023-04-07T07:11:51.000Z"
  },
  {
    "caption": "Antuka na nás do jara počká💪\n#painbustersmost #czechsoftball",
    "ownerFullName": "Painbusters Most",
    "ownerUsername": "painbusters_most",
    "url": "https://www.instagram.com/p/ClNkPVWNYT9/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 42,
    "timestamp": "2022-11-21T05:53:51.000Z"
  },
  {
    "caption": "Junioři Spectra mají za sebou premiéru v Extralize. \nStřetem s realitou pro ně byly dvě porážky rozdílem od Hrochů z Havlíčkova Brodu. Slovy jejich trenéra Matyáše Horvátha: ,,Víme, na čem je potřeba zapracovat a rozhodně nevěšíme hlavu.''",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CrG13yqsay3/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 55,
    "timestamp": "2023-04-16T18:21:36.000Z"
  },
  {
    "caption": "Už za 12 dní začíná extraliga juniorek a mužů na našem domácím hřišti, tak je přijďte podpořit. Oba týmy se určitě nemohou dočkat a co vy? Jak se na začátek sezóny těšíte? 🤔 Napište nám to do komentářů.\n\n#spectrumpraha #czechsoftball #openingday",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CrIWNmgA9De/",
    "commentsCount": 7,
    "firstComment": "4",
    "likesCount": 62,
    "timestamp": "2023-04-17T08:23:26.000Z"
  },
  {
    "caption": "Naše mužské Áčko se již tradičně zúčastnilo turnaje Velikonoční pomlázka. Tento turnaj pořádá pražský oddíl Tempo. Muži poměřili síly s kvalitními soupeři a připravili se tak na nadcházející sezónu. Na Spectrum si z turnaje odvážejí krásné 3. místo.🥉🥎👏",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CqyYcPVNzlO/",
    "commentsCount": 1,
    "firstComment": "Dope",
    "likesCount": 91,
    "timestamp": "2023-04-08T19:39:37.000Z"
  },
  {
    "caption": "Happy birthday!🥳 Přejeme všechno nejlepší k dnešním narozeninám rovnou dvěma oslavencům @davidmertl4 slaví čtyřicítku a @kubat_lukas slaví čtyřiadvacet. Přejeme zdraví, štěstí a hodně úspěchů v nové sezóně. \n\n#spectrumpraha #czechsoftball #birthday",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/Cq03_XTNZvd/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 70,
    "timestamp": "2023-04-09T18:53:47.000Z"
  },
  {
    "caption": "Už dnes začíná historicky první mistrovství světa mužů do 23 let. Turnaje se samozřejmě účastní i česká reprezentace. Barvy národního týmu budou hájit i naši kluci Lukáš Kubát a Matěj Ryšavý. První zápas začíná v 15:30 středoevropského času. Naše reprezentace se utká s hráči Jihoafrické republiky. Klukům i celému národnímu týmu přejeme hodně štěstí.",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CrDNoOGgGI8/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 81,
    "timestamp": "2023-04-15T08:32:14.000Z"
  },
  {
    "caption": "Dnes jsme se věnovali rozvíjení dovedností našeho trenérského týmu. Zastoupeni byli trenéři všech kategorií od žákyň po extraligu mužů. Vzhledem k rozdílným časům přednášek se nás na fotku dostavilo jenom pět. Tímto zdravíme Edu, Říďu a Michala. #JaroSeBlíží, #TěšímeSeVen #NaHřištiJeNejlíp",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CpYR4LctUbp/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 68,
    "timestamp": "2023-03-04T19:50:37.000Z"
  },
  {
    "caption": "Žáci tento víkend úspěšně vstoupili do superligy. Díky skvělému výkonu porazili všechny své soupeře a v tabulce tak obsazují průběžné první místo. Gratulujeme!",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CrGWNmgMEBT/",
    "commentsCount": 1,
    "firstComment": "👏",
    "likesCount": 55,
    "timestamp": "2023-04-16T13:44:57.000Z"
  },
  {
    "caption": "Reprezentace U12 na mistrovství světa na Tchajwanu získala stříbrnou medaili. Gratulujeme celému týmu, ale nejvíc chceme poblahopřát Alfredu Steinerovi a Pavlovi Moravcovi, kteří tak úspěšně reprezentovali Spectrum.\n\n#spectrumpraha #czechsoftball #silvermedal",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CmE_nRJNrXb/",
    "commentsCount": 1,
    "firstComment": "👏",
    "likesCount": 61,
    "timestamp": "2022-12-12T18:31:16.000Z"
  },
  {
    "caption": "Všem hráčům, trenérům, fanouškům a přátelům našeho úžasného sportu děkujeme za uplynulý rok, za všechny krásné momenty ve hře a za všechny vzpomínky, které jsme si na hřišti vytvořili. \nDo nového roku přejeme všem jen to nejlepší a doufáme, že se se všemi uvidíme v nové sezóně na hřišti.",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CmhGp6pOfZx/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 69,
    "timestamp": "2022-12-23T16:31:32.000Z"
  },
  {
    "caption": "Přes Givt jste nám přispěli už přes 6 500 korun! Vás tato podpora nic nestojí a nám pomůže. Proto na nás nezapomeňte při svém dalším online nákupu a část útraty věnujte Sportovnímu klubu Spectrum Praha. Nejjednodušší je to s pomocníkem. Přidejte si jej z odkazu https://givt.cz/aplikace/sportovni-klub-spectrum-praha-z-s do 26. 2. 2023 a my za to dostaneme bonus 30 Kč. Děkujeme za Vaši podporu!\n\n #spectrumpraha #givt",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/Co4mTx_A1eL/",
    "commentsCount": 1,
    "firstComment": "Stonks",
    "likesCount": 20,
    "timestamp": "2023-02-20T12:33:28.000Z"
  },
  {
    "caption": "Gratulujeme všem našim mladým zástupcům, kteří se dostali do reprezentací a výběrů STM.\n \n\n#czechsoftball #spectrum #reprezentace #nextgeneration",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/Ck_VloxjrMm/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 100,
    "timestamp": "2022-11-15T17:16:27.000Z"
  },
  {
    "caption": "O víkendu se na Vypichu odehrálo tradiční DSL a tento rok mělo Spectrum největší zastoupení v SO Clubu. Naši mladiství zakončili sezónu nejlépe, jak mohli. Všechny zápasy vyhráli a získali první místo. Teď už jenom najít místo na poličce pro pohár.🤩🏆",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/Ckp9B0jgiKc/",
    "commentsCount": 2,
    "firstComment": "DSL champs @czechsofotobol @tempofastpitch",
    "likesCount": 87,
    "timestamp": "2022-11-07T09:57:48.000Z"
  },
  {
    "caption": "Již v tento pátek startuje MČR juniorů a naši kluci na něm hrají, a dokonce budou hrát na domácím. Přijďte je podpořit na jejich posledním turnaji sezony v boji o titul mistrů republiky!!!",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CjVK3XbM5Q7/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 49,
    "timestamp": "2022-10-05T11:43:15.000Z"
  },
  {
    "caption": "Áčko je bronzové!!!😍 Muži vyhráli sérii 2:0 na zápasy a berou si na konci sezóny bronzovou placku. V sobotu hráli v pražských Bohnicích kde vyhráli 6:5. Zápas byl napínavý až do konce, kdy @joudrsofficial začali dotahovat a v 7. směně si doběhli pro 5 bodů. V neděli bylo konečné skóre ještě o něco hezčí a chlapi vyhráli 9:4. Supi z Černého mostu si tak mohli užít vítězství a dosažení třetího místa na domácím hřišti. K úspěchu celého družstva se velkým dílem zasadili hlavně @matejrysavy_ , který poslal balón za plot hned třikrát a nadhazovači @dominik.bank86 a Aleš Jetmar, kteří si rozdělili celý víkend mezi sebe.\n\n#czechsoftball #spectrumpraha #bronzemedal",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CjTkAZesxwY/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 81,
    "timestamp": "2022-10-04T20:44:28.000Z"
  },
  {
    "caption": "V létě si zopakujeme s SK Joudrs Praha spolupořadatelství mistrovství Evropy hráček do 18-ti let. \n\nPřihlášeno je 22 evropských týmů, takže bude na co koukat. Česká reprezentace navíc obhajuje titul evropských mistryň.🥇\n\nPřijďte nás od 30.července do 5.srpna navštívit v softball parku Copacabana🥎",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CpI01_LNben/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 39,
    "timestamp": "2023-02-26T19:48:18.000Z"
  },
  {
    "caption": "Dnes ráno začalo na Novém Zélandu 17. mistrovství světa mužů. Za český národní tým také nastupují @tomasklein19 @kubat_lukas a @matejrysavy_ .\n\nNárodní tým v úvodním zápase podlehnul Novému Zélandu 1:3. Další zápas česká reprezentace hraje od 23:00 proti Kubě. Přejeme klukům hodně štěstí. 🤙🤙",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/ClbAYRfNPKJ/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 86,
    "timestamp": "2022-11-26T11:09:52.000Z"
  },
  {
    "caption": "V pátek proběhla akce Gala Softball, kde byli oceněni nejlepší hráči, trenéři i kolektivy uplynulé sezóny. Jedna cena putuje taky k nám na Spectrum. David Mertl obhájil titul nejvíce odpálených homerunů v extralize. Gratulujeme👏🎉",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CoAW0vsMBgi/",
    "commentsCount": 1,
    "firstComment": "🔥💪🏼",
    "likesCount": 68,
    "timestamp": "2023-01-29T16:20:41.000Z"
  },
  {
    "caption": "Mužské áčko za sebou má celou semifinálovou sérii proti Locos Břeclav. Bohužel končí se stavem 0-3 na zápasy a do finále se nepodívají. O bronz budou hrát s poraženým série Painbusters most x Joudrs Praha.",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/Ci5T2fKMJTM/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 51,
    "timestamp": "2022-09-24T16:03:03.000Z"
  },
  {
    "caption": "Junioři se před finálovým turnajem potvrdili svoji formu. V 6. kole 2. ligy na turnaji v Pardubicích junioři vyhráli, co mohli a získali první místo. Snadné to ale neměli. Finále vyhráli proti @pasospardubice , se kterými hráli v této sezóně poprvé, až v tie-breaku 13:12. Klukům gratulujeme a doufáme, že stejně dobré zprávy uslyšíme i po finálovém turnaji, kde budou bojovat o postup do extraligy a který se bude konat 24.-25.9. na domácím hřišti u nás na Spectru.",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/Ciclnvzs7v0/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 57,
    "timestamp": "2022-09-13T12:20:21.000Z"
  },
  {
    "caption": "Naše juniorky vybojovaly na konci sezóny 4. místo. 🤩 V boji o bronz prohrály s @tempo_praha 2:10 a 2:9. I když se jim tento rok nepodařilo dosáhnout na medaili, nasbíral omlazený tým mnoho zkušeností, které budou důležité do dalších sezón.\nBohužel se tímto loučíme s jedničkou na nadhozu @_eviickaa_ , pro kterou to byl poslední zápas v juniorské kategorii.\nJak Evičce, tak celému týmu a trenérům přejeme zasloužený odpočinek, než začne zimní příprava a těšíme se na úspěchy příští sezónu.🥎",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CicZ-mNs32a/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 95,
    "timestamp": "2022-09-13T10:38:36.000Z"
  },
  {
    "caption": "Našim juniorkám se nepovedlo postoupit do finále, ale již zítra mají možnost na opravu a budou hrát proti @tempo_praha o třetí místo. Přijďte je podpořit a pomoct jim v jejich boji na domácím hřišti na Spectru v 17:00!!\n\n#spectrumpraha #czechsoftball",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CiQYolUMFjs/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 83,
    "timestamp": "2022-09-08T18:35:58.000Z"
  },
  {
    "caption": "OPRAVA: Muži pátý zápas v sérii vyhráli 4:2, omlouváme se za chybu\n\nČtvrtfinále v extralize mužů máme za sebou a můžeme si oddechnout. Chlapi porazili @beaverschomutov a tím postoupili do semifinále, kde se potkají s @breclavsoftball . Gratulujeme a přejeme hodně štěstí v semifinále!🤩\n\n#czechsoftball #spectrumpraha #quarterfinals",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CiMvz0WA4gC/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 76,
    "timestamp": "2022-09-07T08:41:31.000Z"
  },
  {
    "caption": "V uplynulém týdnu se na Novém Zélandu konalo mistrovství světa mužů, kde česká reprezentace nakonec obsadila krásné 9. místo. Na turnaji nás mimo jiné také zastupovali @tomasklein19 @kubat_lukas a @matejrysavy_ . 🤩🤩🤩\n\n#czechsoftball #softballeurope  #wbsc",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/ClvwIdLtAfg/",
    "commentsCount": 1,
    "firstComment": "😮",
    "likesCount": 106,
    "timestamp": "2022-12-04T12:31:57.000Z"
  },
  {
    "caption": "Tým juniorů získal bronz! 🥉 Na MČR U18 vybojoval 3. místo a zakončil tak úspěšnou sezónu.",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CjixOVjsRIw/",
    "commentsCount": 1,
    "firstComment": "🙌 a hodně štěstí do další sezóny 👏",
    "likesCount": 89,
    "timestamp": "2022-10-10T18:28:34.000Z"
  },
  {
    "caption": "Sportovcem roku Prahy 14 se už podruhé stal Tomáš Klein. Kapitán našeho A týmu mužů a jejich dlouholetá opora. Gratulujeme a přejeme mnoho dalších úspěchů. 🥎👏",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CqLoSEDN5NK/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 54,
    "timestamp": "2023-03-24T18:27:40.000Z"
  },
  {
    "caption": "O víkendu proběhla na Copacabaně odzimovací brigáda. Přestože nám hlavně v sobotu počasí nepřálo, podařilo se splnit všechno naplánované a to především díky pilné práci všech zúčastněných. Za to bychom vám chtěli poděkovat.💪👏🥎 #TahnemeZaJadenProvaz \n#SnihNasNezastavi\n#NaSezonuPripraveni\n#ZitraKonecneVen",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CpspDNItOWD/",
    "commentsCount": 1,
    "firstComment": "A",
    "likesCount": 86,
    "timestamp": "2023-03-12T17:37:55.000Z"
  },
  {
    "caption": "Chlapi mají brooooonz!!!🥎🥉🎉",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/CjNc6g9Dxal/",
    "commentsCount": 2,
    "firstComment": "@vitto_svejda 💪🏾💪🏾",
    "likesCount": 136,
    "timestamp": "2022-10-02T11:49:09.000Z"
  },
  {
    "caption": "Už za hodinu chlapům startuje jejich semifinálová tour. Dnes hrají v Břeclavi, ale zítra v neděli 18.9. a příští sobotu 24.9. je můžete přijít podpořit doma na Spectru. Tak přijďte a nebo držte palce doma na dálku!!!\n\n#czechsoftball #spectrumpraha #semifinals",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/Cimw85zATBA/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 68,
    "timestamp": "2022-09-17T11:11:45.000Z"
  },
  {
    "caption": "Naši chlapi mají za sebou první víkend semifinále, bohužel se špatným startem. Chlapi oba dva zápasy prohráli. Příští víkend hrají znovu, v sobotu hrají jeden zápas na domácím hřišti, tak je přijďte od 16:00 na Spectrum podpořit. \n\n#czechsoftball #spectrumpraha #semifinals",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/Cir27xtsv2_/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 46,
    "timestamp": "2022-09-19T10:40:14.000Z"
  },
  {
    "caption": "Gratulace!!!🥎 Junioři vyhráli finálový turnaj a postupují do extraligy. Do finále celého turnaje nastoupili proti Joudrs praha, proti kterým předešlý den prohráli. Junioři ale nic nevzdali a finále vyhráli 5:2. \n\n#spectrumpraha #czechsoftball #extraleague",
    "ownerFullName": "Spectrum Praha",
    "ownerUsername": "spectrumpraha",
    "url": "https://www.instagram.com/p/Ci9eduyg4uD/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 109,
    "timestamp": "2022-09-26T06:52:45.000Z"
  },
  {
    "caption": "🇨🇿x🇿🇦 Marek Malý- dvoubodový homerun\n.\nTouto ranou za plot Marek připsal první body českého týmu v zápase proti Jihoafrické republice a poslal tým do vedení 2:0!☄️\n.\n #BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame #czechnationalteam #homerun",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/Clpbx3eKxNz/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 148,
    "timestamp": "2022-12-02T01:41:47.000Z"
  },
  {
    "caption": "Softbalový večer je tu! Dnes večer proběhne další ročník naší společenské události, kdy proběhne zhodnocení sezóny, úspěchy i neúspěchy a také prostor na zábavu v dobré náladě.\n.\nV 19:15 otevíráme dveře pro vstup a ve 20:00 je oficiální začátek programu!\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CpC3KmPNyJu/",
    "commentsCount": 1,
    "firstComment": "👏",
    "likesCount": 88,
    "timestamp": "2023-02-24T12:13:09.000Z"
  },
  {
    "caption": "1/2 V rámci Gala @czechsoftball obdrželi ocenění i naši zástupci. \n.\nMezi oceněnou patří nadhazovačka Kateřina Kindermannová, která vyhrála ocenění juniorky roku 2022. Gratulujeme!\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CoDD76qtY2I/",
    "commentsCount": 1,
    "firstComment": "❤️ úžasné! Gratulujeme! 🥰👏🥂🥳",
    "likesCount": 91,
    "timestamp": "2023-01-30T17:33:21.000Z"
  },
  {
    "caption": "2/2 V rámci Gala @czechsoftball obdrželi ocenění i naši zástupci. \n.\nDruhým oceněným je opora mužského A-týmu Marek Malý, který letos získává ocenění pro nejlepšího pálkaře extraligy. Gratulujeme!\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CoF0TDgtM7G/",
    "commentsCount": 1,
    "firstComment": "👏😮",
    "likesCount": 72,
    "timestamp": "2023-01-31T19:14:25.000Z"
  },
  {
    "caption": "🦫 Beavers Chomutov by se rádi dle slov Jana Malého po hořké loňské sezóně vrátili do bojů o medaile. Svoji formu mohou ukázat již o nadcházejícím víkendu, kdy se představí na předsezónním turnaji Velikonoční Pomlázka v Praze.\n\n#czechsoftball #season2023",
    "ownerFullName": "Czech Softball",
    "ownerUsername": "czechsoftball",
    "url": "https://www.instagram.com/p/CqnUv3njVJS/",
    "commentsCount": 1,
    "firstComment": "Impressive\n image, we  would certainly  like to  deal with you for\n a lot more info message our main account in my\n biography",
    "likesCount": 150,
    "timestamp": "2023-04-04T12:36:43.000Z"
  },
  {
    "caption": "Softbalový večer. 🥎💃🏻🕺🏻\nMenší připomínka ze včerejší společenské softbalové události. Děkujeme všem zúčastněným a těšíme se na další ročník!\n.\nFotografie z večera již jsou na našem flickru. Dostanete se na něj na odkaz v profilu nebo v příběhu.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CpFyCV0PJE1/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 87,
    "timestamp": "2023-02-25T15:26:21.000Z"
  },
  {
    "caption": "U7. Tuto neděli se naše nejmladší skupinka bobrů zúčastnila svého prvního letošního turnaje a to Teeballové ligy U8 v pražském Eagles parku. Byl to vůbec první turnaj našich nejmladších a i když se nepodařilo připsat si výhru, tak jsme dokázali soupeřům nadělit 23 bodů a hned při první rozehře zahrát out! Turnaj si bobříci užili a nasbírali cenné množství zkušeností do dalších událostí v sezóně. Nutno vyzdvihnout, že důležitou oporou našich hráčů a trenéra Vládi byli rodiče, kteří fandili a tým doprovázeli. Novinkou je také náš nový malý maskot bobříka.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CrJ1w98tYvU/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 35,
    "timestamp": "2023-04-17T22:18:23.000Z"
  },
  {
    "caption": "SPOLEČENSKÝ SOFTBALOVÝ VEČER.\nJe to tedy oficiální, dovolte nám Vás pozvat na již 5. Společenský softbalový večer v Chomutově. \nTento večer není určen pouze pro hráče a trenéry, ale hlavně i pro rodiče a přátele klubu, kdy v přátelské atmosféře a dobré náladě proběhne shrnutí všech důležitých milníků sezóny 2022, ale také směřování klubu a další události do sezóny 2023. \nBudeme rádi, když přijdete sdílet s námi tento příjemný večer.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CoMlL8ngl3f/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 76,
    "timestamp": "2023-02-03T10:17:04.000Z"
  },
  {
    "caption": "MUŽI. Na Pomlázce končíme letos na prvním místě. Kulichy, mnoho vrstev oblečení a staré pálky, to vše nás doprovázelo první herní turnaj v této sezóně. Sezóna již startuje a příští herní víkend startuje extraliga juniorů.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CqyDLwlNdbE/",
    "commentsCount": 1,
    "firstComment": "⚾️👍",
    "likesCount": 112,
    "timestamp": "2023-04-08T16:33:52.000Z"
  },
  {
    "caption": "REPREZENTACE. Velký úspěch českých mladíků na MS U12-Mix, kteří získali stříbrné medaile. Velký podíl na tom měli i chomutovští zástupci. Hráči Kryštof Roll, Ondřej Kos a trenér Bohuslav \"Čabi\" Roll.\n.\n\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame #czechnationalteam",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CmByYtCs6Ir/",
    "commentsCount": 2,
    "firstComment": "Check your inbox 📥 plz",
    "likesCount": 104,
    "timestamp": "2022-12-11T12:37:58.000Z"
  },
  {
    "caption": "🇳🇿 HOMERUN Marka Malého.\n.\nTakto otevřel Marek skóre v zápasu proti reprezentaci Nového Zélandu. Celý zápas také nadhazoval a pomohl k výhře národního týmu 🇨🇿3:2🇳🇿 se 14 strikeouty.\n.\n #BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame #czechnationalteam #homerun",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/ClLXhQmAoLA/",
    "commentsCount": 2,
    "firstComment": "!!!",
    "likesCount": 115,
    "timestamp": "2022-11-20T09:28:47.000Z"
  },
  {
    "caption": "MUŽI B. Béčko nenavázalo na sobotní výhru a v Ledenicích prohrává 7:6 a 6:5. Finálová série nabídla kvalitní zápasy a přinesla další zkušenosti pro mladý tým se staršími oporami. Letos tedy bereme stříbro a vyhlížíme příští sezónu.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CjOCE6MssZN/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 91,
    "timestamp": "2022-10-02T17:11:47.000Z"
  },
  {
    "caption": "U11. U malých bobrů patří zima hlavně k všeobecné sportovní přípravě. Přesto bobři neodmítli pozvání 28.1. na přátelský turnaj kategorie U11 do Berouna, ve které budou příští rok nováčci. Nejstarším našim hráčkám a hráčům je deset a tak se setkali i se zkušenějšími soupeři z @minerskladno , @piranhasberoun , @tempofastpitch a @eaglespraha . Cílem bylo nasbírat nové zkušenosti, vyvézt našeho nového maskota a to se povedlo. Odměnou pro hráče byly čokoládové medaile a ani nevadilo, že byly za páté místo. \n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CoZg9Krteua/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 77,
    "timestamp": "2023-02-08T10:50:13.000Z"
  },
  {
    "caption": "Muži B. Blíží se finále druhé ligy a Chomutov tam bude mít zástupce. Béčko se utká s B-týmem Žraloci Ledenice. Začíná se v sobotu na severu Čech.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CjGl1O9sk2z/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 59,
    "timestamp": "2022-09-29T19:50:17.000Z"
  },
  {
    "caption": "REPREZENTACE. Juniorský výběr odletěl před víkendem do Japonska, kde po deset dnů  bude hrát  proti tamnímu týmu Kochi a středoškolským a vysokoškolským výběrům. Součástí české expedice do země vycházejícího slunce je i Adam Buňata.\n.\nAdam v zápase proti týmu Kochi University odpálil také grand slam!☄️\n.\nNa druhé fotce vidíme našeho zástupce s mosteckým @jan__pazdera a druhometařem japonského národního týmu @8tarooo 🥎\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame #czechnationalteam",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/Cj7gFaPAr2A/",
    "commentsCount": 4,
    "firstComment": "Úžasné! Držíme palce😘",
    "likesCount": 157,
    "timestamp": "2022-10-20T08:59:49.000Z"
  },
  {
    "caption": "ZLATÍ ŽÁCI. Naši mladici slaví titul v kategorii U13. Mistrovství republiky hostil Havlíčkův Brod. Ze 6 týmů které se potkávaly během celé sezóny a odehrály spolu spoustu vyrovnaných utkání se mělo rozhodnout o mistrovi České republiky. Po pěti odehraných vyrovnaných zápasech se naši dostali do finále, kde je čekal silný soupeř @joudrsofficial .\n.\nSkvělý výkon našeho nadhazovače Matěje Prontekera, který získal i individuální cenu za nejlepšího nadhazovače turnaje, podpořený opravdu týmovým výkonem všech kluků nás dostal tam, kam jsme směřovali celou sezónu.\n.\nMistři ČR v kategorii U13 pro sezónu 2022 BEAVERS CHOMUTOV. Gratulujeme. \n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CjkY6RVM3Ef/",
    "commentsCount": 2,
    "firstComment": "❤️",
    "likesCount": 93,
    "timestamp": "2022-10-11T09:34:36.000Z"
  },
  {
    "caption": "REPREZENTACE. Muži mají za sebou světový šampionát na Novém Zélandu.  S historickou bilancí 4 výher a 4 proher skončili na 9. místě. V českých barvách se představili i dva naši zástupci Marek Malý a Milan Šulc.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame #czechnationalteam #homerun",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/Cl75LkFNBzj/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 112,
    "timestamp": "2022-12-09T05:41:54.000Z"
  },
  {
    "caption": "MUŽI B. Béčku se podařil vstup do finále a vedou sérii 1:0. Ve vyrovnaném utkání se podařilo v dohrávce 7. směny stáhnout poslední vítězný bod.  K vítězství také pomohl homerun Davida Jalušky. Série se rozhodne zítra v Ledenicích, začínáme ve 12:00.\n.\n📸: Radim Beck\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CjLuZQYskme/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 51,
    "timestamp": "2022-10-01T19:41:19.000Z"
  },
  {
    "caption": "MUŽI B. Naše béčko pokračuje jasnými výkony v play-off druhé ligy. I ve třetím zápase proti @joudrsofficial se ukázali především oba naši nadhazovači David Jaluška a Tomáš Toka. Ve finále se utkáme s B-týmem @zraloci_ledenice .\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/Ci70QhasxpN/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 51,
    "timestamp": "2022-09-25T15:24:42.000Z"
  },
  {
    "caption": "MUŽI&JUNIOŘI. Dnes se muži a junioři zúčastnili tradičního jarního turnaje- Velikonoční Pomlázky na Tempu, kde dnes si odnášíme 3 výhry. Prvními homeruny této sezóny se blýskli Petr Šesták a David Jaluška. 💥 Zítra pokračujeme, tak nám držte palce.\n.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/Cqvp6QRMVGX/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 167,
    "timestamp": "2023-04-07T18:15:36.000Z"
  },
  {
    "caption": "U9&U11.\nKategorie U9 a U11 v zimní přípravě nepolevuje a tak se vydala na druhý a zároveň poslední přátelsky turnaj před sezónou do areálu @joudrsofficial .\nSoupeři nám byli dva týmy @joudrsofficial , @tempofastpitch a @tempo_praha .\nV této kategorii jsme se rozhodně neztratili a odjíždíme s třemi výhrami a jednou remízou.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CqYet2IN56I/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 58,
    "timestamp": "2023-03-29T18:14:12.000Z"
  },
  {
    "caption": "REPREZENTACE. 🇨🇿\n.\nMuži odehráli přípravný turnaj a nyní se přesouvají do Aucklandu, samotného dějiště mistrovství světa. 🇳🇿\n.\nProhlédněte si pár snímků našich chomutovských reprezentantů Milana a Marka.🥎\n.\n📸: @paulopics.nz \n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame #czechnationalteam",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/ClN_uHugO0x/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 109,
    "timestamp": "2022-11-21T09:53:59.000Z"
  },
  {
    "caption": "Reprezentace U12 na MS má za sebou již první zápas zakončený výhrou 10:0 nad Hongkongem. Do zápasu nastoupili oba naši chomutovští reprezentanti Ondřej Kos a Kryštof Roll.\n.\nKryštof dnes přispěl 2 úspěšnými odpaly, včetně 2 doběhů pro český tým. Jen tak dále!💪🏻🥎\n.\n\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame #czechnationalteam",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/Cl4tM7VNpyU/",
    "commentsCount": 3,
    "firstComment": "👏👏😍",
    "likesCount": 92,
    "timestamp": "2022-12-07T23:59:30.000Z"
  },
  {
    "caption": "INTERPOHÁR. O víkendu se na chomutovských hřištích odehrál i tradiční interpohár. K vidění byly týmy namixované z různých kategoriích. Jeden z chomutovských mančaftů obsadil na našlapaném klání první místo, druhý skončil na čtvrtém. Ve finále náš mladý tým porazil Tuneláře z Radotínu 11:4. Děkujeme všem zúčastněným a těšíme se třeba příští rok na další ročník.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/Cj0tiSoN2vC/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 121,
    "timestamp": "2022-10-17T17:42:40.000Z"
  },
  {
    "caption": "ROOKIEBALL. O uplynulém víkendu hrála i naše kategorie U9, představila se na hřišti Praotců ve Vědomicích. Počasí jim celý den přálo a sluníčko se na všechny usmívalo. První zápas s Painbusters začali mladíci útočně a podařila se výhra. Po obědě začali s Pasos s rozvahou , ale stačilo to už jen na remízu. S domácími Praotci vybojovali také remízu a poslední zápas s Lobkovicema se podařila opět výhra. Po dvou výhrách a dvou remízách  se umístili v tabulce jako druzí. Bobříci si to užili jak na hřišti, tak mimo hřiště.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CifiAugMcjF/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 55,
    "timestamp": "2022-09-14T15:46:31.000Z"
  },
  {
    "caption": "MUŽI B. Seniorskému áčku sice sezóna už skončila, o špičkový mužský softball ale v Chomutově nepřicházíme. Naše Béčko totiž stále bojuje o skvělý výsledek ve 2. lize. V semifinále se utká proti B-týmu SK Joudrs Praha. Přijďte je podpořit. Tým nadějných mladíků i zkušených borců může dosáhnout na cenné kovy.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CikFM4dAJS9/",
    "commentsCount": 1,
    "firstComment": "Play ball!! Great work!! Follow @fit4lyfe24 for ⚾️ fitness and training tips!",
    "likesCount": 38,
    "timestamp": "2022-09-16T10:10:59.000Z"
  },
  {
    "caption": "MUŽI B. Seniorskému béčku se vydařil vstup do semifinále. Joudrs v prvním zápase nedali šanci. Pomohly homeruny Adama Buňaty a Davida Jalušky. Druhý jmenovaný taky zápas ovládl na prkně, když za celý mač povolil pouze jednu jedinou metu a žádný hit. Pokračujeme v neděli od 16:00 v pražském Svoboda parku.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/Cinj1gXsf0c/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 56,
    "timestamp": "2022-09-17T18:36:23.000Z"
  },
  {
    "caption": "JUNIOŘI. Sezónu za sebou mají i naši junioři. I ti sice bojovali o medaile, nakonec z toho ale bylo čtvrté místo. I tak jde ale o hezký výkon po loňském postupu do nejvyšší soutěže a příslib do budoucna. Děkujeme.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CicAp6KgDBL/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 85,
    "timestamp": "2022-09-13T06:57:20.000Z"
  },
  {
    "caption": "MUŽI B. Po dvou zápasech vedeme semifinále 2:0. Dnes se předvedli především Jaroslav Mikulec, který dal homerun, a Tomáš Toka, který na prkně nedovolil bod. O postupu do finále druhé ligy se rozhodne příští víkend.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #menssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CiruCCXgVTH/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 64,
    "timestamp": "2022-09-19T09:22:27.000Z"
  },
  {
    "caption": "ZLATÉ JUNIORKY. I letos sbíráme v našem klubu medaile. A hned ty nejcennější! Juniorky vyhrály extraligový titul, když si s @joudrsofficial poradili 2:1 na zápasy. Kateřina Kindermanová během tří zápasů hodila skvělých 35 strike-outů. Jen tak dál holky. Gratulujeme a děkujeme.\n.\n#BVRS #beaverschomutov #WinDiesel\n.\n#softball #czechsoftball #gameday #fastpitch #fastpitchsoftball #playball #sport #chomutov #chomutovsport #ballgame #womenssoftball #softballgame",
    "ownerFullName": "Beavers Chomutov",
    "ownerUsername": "beaverschomutov",
    "url": "https://www.instagram.com/p/CiYRlRvgT1L/",
    "commentsCount": 1,
    "firstComment": "borky největší🧡🖤",
    "likesCount": 215,
    "timestamp": "2022-09-11T20:08:17.000Z"
  },
    {
    "caption": "First tournament of the season in Sharks Bay  #kids #sunny #letthegrassgrow #zralociledenice #czechsoftball #season2018 #sharksbayledenice",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BhTOPeHH2JN/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 66,
    "timestamp": "2018-04-08T07:02:16.000Z"
  },
  {
    "caption": "This weekend in Sharks Bay #zralociledenice #czechsoftball #sharksbay #comeandhavefun #gogirls",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BimZFfZDsfj/",
    "commentsCount": 1,
    "firstComment": "👋🦈",
    "likesCount": 43,
    "timestamp": "2018-05-10T14:13:59.000Z"
  },
  {
    "caption": "Poslední víkend Žraloků, ženy soustředění v Horní Stropnici, kadeti turnaj na Joudrs #zralociledenice #joudrspraha #u16tournament #hornistropnice #soustredeni #wintercamp",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BeP-X3lDOvV/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 57,
    "timestamp": "2018-01-22T11:11:42.000Z"
  },
  {
    "caption": "Žraloci ocenění na celostátním galavečeru softballu #czechsoftball #zralociledenice #galavecer #congratulation",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/Bbw-_poD3iZ/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 45,
    "timestamp": "2017-11-21T17:17:53.000Z"
  },
  {
    "caption": "Všude modrá, vzpomínka na finále dospělých extralig, zlatá a stříbrná #goldandsilver #zralociledenice #sharksbayledenice #season2017 #seasontoremember",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/Bbg0QuGj0B7/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 65,
    "timestamp": "2017-11-15T10:36:15.000Z"
  },
  {
    "caption": "Yobu přinesl ledenickým extraligovým mužům výborný víkend, 2 výhry v Pardubicích a 2 výhry v Havlíčkově Brodě #zralociledenice #czechsoftball #yobulifestyle #dontstealyobusrum #sharkswinagain #seasonopening #4wins",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/Bh4jsa2Dyh8/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 66,
    "timestamp": "2018-04-22T19:01:37.000Z"
  },
  {
    "caption": "#zralociledenice",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BXXPDFkAi_-/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 23,
    "timestamp": "2017-08-04T07:12:20.000Z"
  },
  {
    "caption": "Club president interview for ČT #hanakorcakova #interview #sharksbay #ceskatelevize",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BUBzTnYAw5J/",
    "commentsCount": 2,
    "firstComment": "@martasvybiralos někdy po 4.6.",
    "likesCount": 32,
    "timestamp": "2017-05-13T09:51:41.000Z"
  },
  {
    "caption": "Bloody busy day in Sharks Bay #busyday #SSC #tournament",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BUBy_PUgvRC/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 21,
    "timestamp": "2017-05-13T09:48:55.000Z"
  },
  {
    "caption": "Žraločí focení #zralociledenice #photoshooting #fotkybudou #softballbude #noneedforphotoshop",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BE0eX3kvrQJ/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 23,
    "timestamp": "2016-04-30T09:47:44.000Z"
  },
  {
    "caption": "Poslední večeře zimní přípravy #lastsupper #sharksspringtraining #holland #eastertournament #spijkenisse #zralociledenice",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BDgmlq3PrUx/",
    "commentsCount": 1,
    "firstComment": ":)))",
    "likesCount": 15,
    "timestamp": "2016-03-28T20:03:19.000Z"
  },
  {
    "caption": "#pitchingcamp #nadhoz #nadhazovacisoustredeni #zralociledenice #czechsoftball",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BCFdopbvrVt/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 11,
    "timestamp": "2016-02-22T10:34:11.000Z"
  },
  {
    "caption": "Prezidentka klubu Hana Korčáková má dnes narozeniny. Celý klub Žraloci Ledenice jí tímto přeje vše nejlepší, mnoho úspěchů a alespoň ještě jedno půlstoletí. #zralociledenice #czechsoftball #happybirthday #hanakorcakova",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/1iHximvrf8/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 16,
    "timestamp": "2015-04-16T10:53:01.000Z"
  },
  {
    "caption": "Žraloci Ledenice jsou na instagramu! Sledujte! A současně i žraločí hashtag #zralociledenice",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/0GK-oqPrRA/",
    "commentsCount": 1,
    "firstComment": "A vy nezapomínejte hashtag #czechsoftball ! :-)",
    "likesCount": 11,
    "timestamp": "2015-03-11T17:50:53.000Z"
  },
  {
    "caption": "Již brzy! #sbc #sharksbayclub #zralociledenice",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BCZwlf_PrX_/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 16,
    "timestamp": "2016-03-01T07:44:36.000Z"
  },
  {
    "caption": "O prázdninách v Sharks Bay znovu týdenní kemp s reprezentanty. Přihlášku na webu na: www.zralociledenice.cz/informace/ke-stazeni/\n#zralociledenice #czechsoftball #sharksbay #summercamp #july #nationalteamplayers",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BhtmnOGDrgU/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 27,
    "timestamp": "2018-04-18T12:55:29.000Z"
  },
  {
    "caption": "Žraločí školení na iScore! #zralociledenice #czechsoftball #iscore",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/0NsYXNvrRE/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 13,
    "timestamp": "2015-03-14T15:57:27.000Z"
  },
  {
    "caption": "Trenérská schůzka v sobotní podvečer. #progres #zralociledenice",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BBvAH1oPrbr/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 5,
    "timestamp": "2016-02-13T17:13:01.000Z"
  },
  {
    "caption": "PF 2018 #zralociledenice #softball #czechsoftball #championyear #pf2018",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BdcOyoajEYk/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 61,
    "timestamp": "2018-01-02T08:54:39.000Z"
  },
  {
    "caption": "První vítěz Superhrdinské challenge kadetů je Honza Křešnička, Batman výzva. #batmanchallenge #workout #zralociledenice @kresnaa_24",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BCk7d-lPrbm/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 17,
    "timestamp": "2016-03-05T15:51:20.000Z"
  },
  {
    "caption": "Včera se na domácí zápasy Žen A přišel podívat první softballový přírůstek! #zralociledenice #czechsoftball #littleborax #nofilter",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BGAF-p_vrTz/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 23,
    "timestamp": "2016-05-29T18:36:51.000Z"
  },
  {
    "caption": "New player has arrived #nz #howicksoftball",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BUOZnPiABcG/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 47,
    "timestamp": "2017-05-18T07:17:18.000Z"
  },
  {
    "caption": "První návštěvníci dětského koutku v clubhouse v Sharks Bay #zralociledenice #clubhouse #sharksbayledenice #detskykoutek #hracky #newsome",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/Bhyz2IfD6kc/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 38,
    "timestamp": "2018-04-20T13:27:19.000Z"
  },
  {
    "caption": "#zralociledenice #europeanchampions #sharksbay #mensnationalteam #goldmedal #czechsoftball @petrfrejlach @kopecnypatrik @jkorcak8 @czechsoftball",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BIKgYj4AqoV/",
    "commentsCount": 2,
    "firstComment": "@ultimatesports_cz děkujeme 🇨🇿",
    "likesCount": 28,
    "timestamp": "2016-07-22T12:42:47.000Z"
  },
  {
    "caption": "Tak co, obhájíme i letos? Cesta za zlatým hattrickem začìná v sobotu ve 12:00. #obhajoba #playoff #czechsoftball⚾️ #sharks #vs #kunovice #sharksbay",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/B27J_dAAqct/",
    "commentsCount": 1,
    "firstComment": "Moc blahopřejeme 👏",
    "likesCount": 95,
    "timestamp": "2019-09-27T18:14:02.000Z"
  },
  {
    "caption": "4 Žraloci na NZ #zralociledenice #czechsoftball #howicksoftballclub #meadowlandsreserve",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BQBulPFjE0j/",
    "commentsCount": 1,
    "firstComment": "1, 2, 3, Tiburones!",
    "likesCount": 45,
    "timestamp": "2017-02-02T23:04:50.000Z"
  },
  {
    "caption": "It's almost Christmas, so everybody gets ready for all the cookies #getyourabsready #zralociledenice #workout #beforechristmastrainings",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/Bcux-42j5Pt/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 44,
    "timestamp": "2017-12-15T17:17:06.000Z"
  },
  {
    "caption": "Žraločí muži B jsou na turnaji v Belgii. Vyhráli 2 ze 3 zápasů a zítra budou hrát Top 4. Homeruny odpálili Jakub Hajný, Tomáš Gabriška a i David Vašíček, kterému je dnes 18 let. Gratulujeme #zralociledenice #softball #belgium #springtournament #easterntournament",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/Bg_1USsjSsP/",
    "commentsCount": 1,
    "firstComment": "Hoši je to boží",
    "likesCount": 108,
    "timestamp": "2018-03-31T18:18:54.000Z"
  },
  {
    "caption": "Nové dresy mužů! #newjersey #zralociledenice #ledenice #czechsoftball",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/0vFrVGPreZ/",
    "commentsCount": 1,
    "firstComment": "What kind off brand are those jerseys??? @zraloci_ledenice 👕👕👢",
    "likesCount": 20,
    "timestamp": "2015-03-27T15:13:26.000Z"
  },
  {
    "caption": "Kadeti mají za sebou další dvoutýdenní challenge a další soustředění. Vítězem Flash výzvy se stal Jan Křešnička, druhé místo patří Vášovi Burešovi a ma třetím se umístil Matěj Vlk! #flashchallenge #workout #zralociledenice #soustredeni",
    "ownerFullName": "Žraloci Ledenice",
    "ownerUsername": "zraloci_ledenice",
    "url": "https://www.instagram.com/p/BDWlFmPPrQ2/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 14,
    "timestamp": "2016-03-24T22:37:48.000Z"
  },

  {
    "caption": "Mužské Áčko vyrazilo směrem na západ do softballového městečka Haarlem.Tam odehráli 6 zápasů před startem extraligy 2k23. #softball #softballlife #joudrsacko #joudrs #czechboy #amsterdam #haarlem #instalike #like",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CqXSjGtg2u6/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 167,
    "timestamp": "2023-03-29T07:17:56.000Z"
  },
  {
    "caption": "BOURÁNÍ HALY | BRIGÁDA 💪⛏🪛🔧🔨🧹\n\nProsíme dobrovolníky, aby nám přišli v neděli 26. 3. 2023 pomoc s BOURÁNÍM HALY. Sraz v 8:00 před Clubhousem.\nVenkovní sezóna už je za dveřmi!",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/Cp-K12VNaPx/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 34,
    "timestamp": "2023-03-19T13:00:17.000Z"
  },
  {
    "caption": "JOUDRS INDOOR CUP U10 | POSLEDNÍ HALOVÝ TURNAJ \n\nV sobotu 25. 3. jsme uzavřeli zimní část přípravy turnajem jedné z nejmladších kategorií, a to Coachballu U10.\n \nPoslední den, kdy stála hala, se všechny týmy rozhodly využít na maximum. Oproti prosincovému turnaji byl znát posun na pálce, ale především v poli. Delší a přesnější příhozy a lepší orientace ve hře přinesly krásné situace, dokonce i pár double outů. Nehrálo se o umístění, přesto byla motivace hráček a hráčů obrovská a nasazení neskutečné. Velká část bojů byla vyrovnaná, zaznamenali\njsme remízu i těsný obrat skore v poslední směně.\nVypadá to, že kategorie Coachball má našlápnuto na zajímavou sezonu.\n \nDěkujeme všem týmům, které za námi dorazily rozloučit se s letošními halovými turnaji:\nBeavers Chomutov\nTJ Tempo Praha - fastpitch softball\nTempo Praha\nSK Joudrs Praha Joudrs Grey a Joudrs Orange\n#softball #joudrs",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CqVmd2HtX_6/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 95,
    "timestamp": "2023-03-28T15:24:12.000Z"
  },
  {
    "caption": "MISTROVSTVÍ SVĚTA U12 MIX | STŘÍBRO🥈🏆💪🥎🇨🇿\n\nVeliká gratulace národnímu týmu U12 mix, kteří vybojovali na MS v Tchaiwanu stříbrné madaile. \n\nV národním dresu reprezentovali i zástupci Joudrs a to Markéta Švecová, Ádám Karel Sládek a Ondřej Vestfál v roli trenéra. \nVeliká gratulace všem🫶🏻🥎🇨🇿\n@czechsoftball",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CmBgFmqA_TO/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 222,
    "timestamp": "2022-12-11T09:58:04.000Z"
  },
  {
    "caption": "PF 2023\n\n#joudrs #pf #softball #lovesoftball #czechsoftball",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CmcbHUKtWdy/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 76,
    "timestamp": "2022-12-21T20:54:07.000Z"
  },
  {
    "caption": "DĚKUJEME VŠEM, CO SE PODÍLELI NA BOURANÍ HALY  A POMOHLI S OKOLNÍMI PRACEMI 💪🫶🏻\n\nLETNÍ SEZÓNA MUŽE ZAČÍT 🥎💪\n￼\nJoudrs olé!",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CqQkLQpAomi/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 107,
    "timestamp": "2023-03-26T16:28:31.000Z"
  },
  {
    "caption": "VÁNOČNÍ JOUDRS CUP mix U13\n\nPosledním turnajem v roce 2022 byl Vánoční Joudrs Cup dětí do 13 let. \nLetos se zúčastnilo 50 dětí, ze kterých bylo vytvořeno 5 týmu a odehrálo se 15 napínavých zápasů. Vítězství si vybojoval tým RED pod kapitánským vedením Matyáše Koudelky a Emy Horákové. \n\nCelkové pořadí: \n🥇 Red\n🥈 White\n🥉 Yellow\n 4. Green\n 5. Blue\n\nCeny za nejužitečnější hráče získali Dariia Kozhusko a Jakub “Lojza” Průšek.\n \nTurnaj doprovázel biatlonový závod, kterého se zúčastnili všichni děti. \nVítězem biatlonového klání v jednotlivých kategoriích:\nKluci - Matyáš Koudelka\nDívky - Anna Klementová\nŠtafety - tým Blue\nRekord trati - Jakub Mráz (1:08)\n\nGratulujeme všem zúčastněným a vítězům!\n\nDěkujeme našemu partnerovi PLAY-BALL.CZ za ceny do turnaje a všem, kteří se na turnaji podíleli!",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/Cm01-TMtRj2/",
    "commentsCount": 1,
    "firstComment": "@maty_softball 👏",
    "likesCount": 116,
    "timestamp": "2022-12-31T08:30:35.000Z"
  },
  {
    "caption": "SEZÓNA 2023 PŘICHÁZÍ \n\n#jsmetymjsmejoudrs #joudrs #softball #czechsobtball #lovesoftball #joudrsole #sezonaprichazi",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/Cpovx2ltimv/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 45,
    "timestamp": "2023-03-11T05:19:45.000Z"
  },
  {
    "caption": "🥈Mastenbroek 2023 | ŽENY A \n\nMinulý víkend proběhl připravný turnaj v holandském Enschede, kterého se zúčastnilo naše ženské ačko.\nŽeny se přes nepříznivé počasí probojovaly až do samotného finále, ve kterém nakonec podlehly týmu @olympiasoftball a odvezly si z turnaje 2. místo.\n\n#mastenbroek",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/Cq31CwBtKkw/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 103,
    "timestamp": "2023-04-10T22:25:45.000Z"
  },
  {
    "caption": "JUNIORKY A \n\nJuniorky si z chorvatského Záhřebu vezou druhé místo z turnaje Forever Fastpitch 2023\n\n#softball #joudrs# @joudrsjuniorky #joudrsole",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CqihOiVNwwh/",
    "commentsCount": 1,
    "firstComment": "Thank you for coming! It was great having you. Another great result at ForEVER 💪🏼",
    "likesCount": 169,
    "timestamp": "2023-04-02T15:48:33.000Z"
  },
  {
    "caption": "JOUDRS MASTERS +40 \n\nPrvní sraz ženského týmu Joudrs Masters 40+ zahájil přípravu na podzimní evropský turnaj pořádaný v Barceloně. Účast byla téměř stoprocentní a nálada výborná. Každý dostal rozpis tréninků, turnajů,  individuální softbalovou i kondiční přípravu. Kontakty na fyzioterapeuty, maséry, rehabilitační pracovníky, výživové poradce, nemocniční zařízení, atd. Jedním bodem programu bylo i materiálové zabezpečení a pro některé překvapení, že už se nehraje bílými míči. \nDěkujeme všem, co si vzali za úkol zajištění ubytování a dopravy. Už se těšíme na první společný trénink.\n#joudrs #softball #joudrsole #masters #fastpitch #lovesoftball #jsmetymjsmejoudrs",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CqaGBS6Apbb/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 99,
    "timestamp": "2023-03-30T09:16:53.000Z"
  },
  {
    "caption": "Krásných 25 let! \nSlavilo se, povídalo se, vzpomínalo se… popřáli jsem si do dalších 500 let💪🥎🥂. Joudrs olé!\n#25let #slavime #joudrs #softball #anniversary",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/ClrjYZ-NrYh/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 156,
    "timestamp": "2022-12-02T21:23:34.000Z"
  },
  {
    "caption": "JOUDRS CUP U16 MIX | KONEC SEZÓNY 2022\n\nPoslední turnj pro Joudrs děti do 16 let ukončil sezónu 2022 🏅🥎🔥\n\nTurnaje se účastnilo 54 děti, počasí nejprve v sobotu dopoledne nepřálo🌧️, ale pak 🌞… \nDěkujeme všem za účast, věříme, že si to všichni užili a dobře se bavili. \nSobotní setkání u grilu s rodiči, hráči i trenéry stálo za to💪🥩🍗🥗🥓.\nDěkujeme za přípravu a organizaci Jitce Ch. a Zdeňkovi M. 🙏\n\nJsme tým, jsme Joudrs!\nJoudrs olé!",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CkD6a8NsKFl/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 147,
    "timestamp": "2022-10-23T15:23:52.000Z"
  },
  {
    "caption": "JE TO DOMA!🥇🏆 | ŽENY A \n\nJoudrs potřetí v řadě ovládly ženskou extraligu a získaly titul Mistra ČR🤩\n\n📸 @jplatno \n#jsmetym #jsmejoudrs #jsmetri #hattrick",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/Cjq5EXtNmws/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 159,
    "timestamp": "2022-10-13T22:11:02.000Z"
  },
  {
    "caption": "🏆🥈 NA STŘÍBRNÉ VLNĚ SE NESLO JOUDRS NA MČR JUNIORŮ U18 - MČR KADETEK U16 - MČR ŽÁKŮ U13\n\nIndividualni ocenění si jako nejlepší pálkaři odnáší všichni zástupci klubu Joudrs 💪🎖️\nOndřej Tvrdek - MČR juniorů U18\nAmálie Kalčevová - MČR KADETEK U16\nKryštof Kučera - MČR žáků U13\n\nGratulujeme!\n\n@czechsoftball",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/Cjin5Z6spJJ/",
    "commentsCount": 2,
    "firstComment": "👏👏👏👏",
    "likesCount": 159,
    "timestamp": "2022-10-10T17:07:04.000Z"
  },
  {
    "caption": "HATTRICK | ŽENY A \n\n22 • 21 • 20\n\n📸 @jplatno & @benyphoto_czech \n#jsmetym #jsmejoudrs #jsmetri #hattrick",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/Cjq8haytFz1/",
    "commentsCount": 1,
    "firstComment": "LETS GOOOOO! 🔥💪🏼",
    "likesCount": 118,
    "timestamp": "2022-10-13T22:41:13.000Z"
  },
  {
    "caption": "MČR JUNIOREK U18 | OSTRAVA\nMistryně 🥇🏆💪🥎\n\nSvou sezónu dnes uzavřely naše juniorky na MČR v Ostravě, odkud si odváží zlatou medaili 🏆🥇💪\nHned prvním zápasem nastoupily na vítěznou vlnu, kterou neopustily.\n\nGratulujeme!\n\n@czechsoftball @joudrsjuniorky",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CjyBc-QNlzK/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 156,
    "timestamp": "2022-10-16T16:38:59.000Z"
  },
  {
    "caption": "REPREZENTACE | HERNÍ SOUSTŘEDĚNÍ V USA 💪🥎🇨🇿\n\nV brzkých ranních hodinách odletělo 10 hraček Joudrs, v čele s Tomášem Kusým s českou reprezentací juniorek do americkeho Los Angeles, na turnaj Early Thanksgiving Showcase, kde odehrají 11 zápasů. \nV týmu se z SK Joudrs Praha objeví: Karolína Beránková, Karolína Frýbová, Anna Haincová, Kristýna Horáčková, Amálie Chaloupková, Amálie Kalčevová, Karolína Nosková, Aneta Rambousková, Markéta Vlčková a Rebeka Wenclová. Hodně štěstí 🥎🥎🥎 \n@czechsoftball",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/Ck-jhVlgDUR/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 149,
    "timestamp": "2022-11-15T09:58:57.000Z"
  },
  {
    "caption": "Jdeme si pro HATTRICK!! 🏆🏆🏆| ŽENY A\n\nDnes v 15:00 vypukne na Tempu zápas, ve kterém mohou naše ženy ukončit finálovou sérii a získat poprvé v historii klubu zlatý hattrick.🥇\n\nPřijďte je podpořit na tribuny hostujiciho areálu.\n\n#joudrsacko #zenyA #extraliga #czechsoftball #jsmetri #hattrick\n📸 @simunkovaphoto",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CjfbI57AE7S/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 94,
    "timestamp": "2022-10-09T11:17:52.000Z"
  },
  {
    "caption": "JOUDRS OLÉ 🥎💪🔥\n\nŽÁKYNĚ vybojovaly zlaté medaile na MČR žákyně U13🥇🏆\n\nKADETI A na domácím hřišti na MČR kadetů U16 vybojovali stříbrné medaile 🥈🏆\n\nŽENY A jdou do finále 🔥💪\n\nMUŽI A ukončili letošní extraligovou sezónu s medailí bramborovou. \n\nROOKIE BALL na MČR U9 skončili na 5 místě a v projektu Clash of Skills byli na 3. místě. \n\nVšem gratulujeme a našim hráčům a trenérům děkujme za reprezentaci klubu.",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CjQ5AERslw2/",
    "commentsCount": 1,
    "firstComment": "Holky, gratulace 👏",
    "likesCount": 130,
    "timestamp": "2022-10-03T19:50:12.000Z"
  },
  {
    "caption": "Tak už jdeme do finále!🏅 | ŽENY A\n\nŽeny ovládly semifinálovou sérii proti @eagles_zeny a postupují do finále, kde se utkají s @tempo_praha. \n\nNa první zápas finále se můžete těšit ve čtvrtek 6.10. v 18:00, který se odehraje ve Svoboda parku. \nPřijďte naše áčko podpořit v cestě k hattricku!!🤩\n\n#joudrsacko #zenyA #extraliga #czechsoftball #jsmetri #jdemprohattrick",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CjOBxmbtYhX/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 157,
    "timestamp": "2022-10-02T17:09:09.000Z"
  },
  {
    "caption": "MUŽI A | EXTRALIGA A BOJ O 3. MÍSTO 🔥💪\n\nEXTRALIGA mužů vrcholí …\nDnes v 16 hod začne ve Svoboda parku utkají @joudrsacko proti @spectrumpraha o 3. místo!\nPřijďte podpořit chlapecké Áčko na tribuny🥎💪🔥\n@czechsoftball #extraliga #softball #fastpitch #muzia #play-off",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CjKpD_XgG7w/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 42,
    "timestamp": "2022-10-01T09:35:29.000Z"
  },
  {
    "caption": "ROOKIE BALL U9 | Finálový turnaj \n\nI naši nejmenší na hřišti v Eagles parku přejeme krásnou hru💪🥎😉\n@czechsoftball",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CjKfoFlA7Bi/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 25,
    "timestamp": "2022-10-01T08:13:02.000Z"
  },
  {
    "caption": "MČR ŽÁKYŇ | NA KOTLÁŘCE\n\nTento víkend se také koná Mistrovství ČR v kategorii žákyň do 13 let. I zde má náš klub zastoupení a našim holkám držíme palce!!! Přejeme krásnou hru💪🥎\n\n@czechsoftball",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CjKeWMwgO_w/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 24,
    "timestamp": "2022-10-01T08:01:51.000Z"
  },
  {
    "caption": "SLAVNOSTNÍ ZAHÁJENÍ 25. SEZÓNY \n\nV úterý slavnostním nadhozem zahájil softballovou sezónu Joudrs Praha pan starosta MČ Praha 8 Ondřej Gros a místostarosta pan Jiří Vítek.\nPodvečer jsme si náramně užili. Přivítali jsme nováčky v klubu, z rukou starosty, místostarosty a předsedy bylo předáno ocenění hračkám ženského Áčka za získaný Zlatý Hattrick, kapitáni týmů složili slib, proběhl slavnostní nadhoz. Poté byl zahájen otevírací zapas našich juniorů a kadetů A, ktery skončil 1:3 pro Kadety A.\nNásledovala autogramiáda a malé občerstvení pro všechny. \nCelým ceromonialem nás provázel Daniel Tobola.\n\nJsme tým, jsme Joudrs!\n\nVíce fotografii na https://www.flickr.com/gp/skjoudrs/Sv5z20161Q\na https://www.flickr.com/gp/skjoudrs/L0GNZH91p8\n\nDěkujeme fotografům 📸 Beny Photo a Martina Macháčková Softball Photos",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CqxqhrGNUuL/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 186,
    "timestamp": "2023-04-08T12:58:25.000Z"
  },
  {
    "caption": "MUŽI A | EXTRALIGA PLAY-OFF\n\nMužské áčko zakončilo sezónu na 4. místě. Naše třetí sezóna v extralize nás vynesla na čtvrté místo. Dokázali jsme vyhrát nadstavbu A a odnést si tak Pohár Aleše Hraběte a dokázali jsme porazit všechny týmy v extralize 💪🔥. Věříme, že v další sezóně už to cinkne a my pro to uděláme maximum. \n@czechsoftball @joudrsacko #extraliga #softball #fastpitch #play-off #muzua",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CjaLzY0gnhC/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 50,
    "timestamp": "2022-10-07T10:27:39.000Z"
  },
  {
    "caption": "Finále v televizi 📺 | ŽENY A\n\nVe čtvrtek 6.10. v 18:00 vypukne první utkání finálové série proti @tempo_praha.\n\nPřijďte do Svoboda parku nebo nalaďte ČT Sport.\n\n#joudrsacko #zenyA #extraliga #jsmetymjsmejoudrs #jsmetri",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CjS85XWjREe/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 52,
    "timestamp": "2022-10-04T15:02:43.000Z"
  },
  {
    "caption": "REPREZENTACE JUNIORŮ U18 | SOUSTŘEDĚNÍ V JAPONSKU 🇨🇿 🇯🇵\n\nJuniorští hráči jsou na cestě odlétají směr Japonsko, kde je po dobu deseti dnů čeká 14 zápasů proti místnímu týmu Kochi a středoškolským a vysokoškolským výběrům.\n\nOndřej Stroner jako hlavní kauč reprezentace do 18 let a Andrej Sokol budou reprezentovat náš klub. \n\nPřejeme šťastný let a krásnou hru 🥎💪 \n\nVíce v článku na @czechsoftball",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/Cjr5cT8gkXQ/",
    "commentsCount": 3,
    "firstComment": "@_an.d.rej_ frajer",
    "likesCount": 135,
    "timestamp": "2022-10-14T07:33:33.000Z"
  },
  {
    "caption": "MILNÍKY EXTRALIGY | PLAY-OFF\n\nBěhem říjnových play-off zápasů bylo pokořeno několik extraligových milníků \nGratulujeme 💪🥎👏\nJana Furková (SK Joudrs Praha) - 200 odpalů\nJan Janoušek (SK Joudrs Praha) - 100 stažených bodů\n@czechsoftball",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CkIS8IFACfh/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 89,
    "timestamp": "2022-10-25T08:15:05.000Z"
  },
  {
    "caption": "ŽÁKYNĚ UKONČILY SEZÓNU V ITÁLII | 🇨🇿 🇮🇹 🏆🥉🥎\n\nParádní jízda na italském turnaji v  Saronno Softball, kterého se účastnilo 8 týmu včetně zastoupení Joudrs žákyň. \nA dařilo se, nejen, že holky posbíraly  cenné zkušenosti, skvěle zážitky, ale ještě jim na krku cinká bronzová medaile 🥉🏆💪🥎 \nJedinou porážku okusily od mistra Itálie Bollate softball 4:0, pozdějšího vítěze turnaje. \nIndividuální cenu MVP získala Emma Horáková 💪\nGratulujeme!",
    "ownerFullName": "SK Joudrs Praha",
    "ownerUsername": "joudrsofficial",
    "url": "https://www.instagram.com/p/CkGGUT-suQh/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 143,
    "timestamp": "2022-10-24T11:46:18.000Z"
  },
    {
    "caption": "Dnes v 15:30 rozehrajeme čtvrtfinálovou sérii se Žraloci Ledenice. Přijďte nás podpořit do závěrečných play-off utkání.🥎",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CUg9VpAslZD/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 68,
    "timestamp": "2021-10-02T05:45:02.000Z"
  },
  {
    "caption": "📸 @benyphoto_czech",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CGXdpBKAQrN/",
    "commentsCount": 1,
    "firstComment": "Please check my dm",
    "likesCount": 170,
    "timestamp": "2020-10-15T13:55:22.000Z"
  },
  {
    "caption": "📸 @benyphoto_czech",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CGXdDnbAigS/",
    "commentsCount": 2,
    "firstComment": "Champions 🔥🔥🔥🔥",
    "likesCount": 195,
    "timestamp": "2020-10-15T13:50:16.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CC6G3BzAXE9/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 125,
    "timestamp": "2020-07-21T14:44:09.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CC6GnKOAWx1/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 151,
    "timestamp": "2020-07-21T14:41:59.000Z"
  },
  {
    "caption": "🌧",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CBquN-_AcSD/",
    "commentsCount": 1,
    "firstComment": "To jsem nefotil já.... ani jsem tam nebyl 😮",
    "likesCount": 123,
    "timestamp": "2020-06-20T18:48:50.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CC6GbygghG_/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 102,
    "timestamp": "2020-07-21T14:40:26.000Z"
  },
  {
    "caption": "📷 @marek_rosenkranz",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CBquk38g6Q9/",
    "commentsCount": 1,
    "firstComment": "😍😍😍",
    "likesCount": 230,
    "timestamp": "2020-06-20T18:51:57.000Z"
  },
  {
    "caption": "#czechsoftball 📷 @marek_rosenkranz",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CBqtjA3A0Pm/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 177,
    "timestamp": "2020-06-20T18:42:58.000Z"
  },
  {
    "caption": "The real season starts right now! Let’s do it again! ⚾️ #playoffs2018 #hippos #havlickuvbrod #softball #czechsoftball #weplayforoctober",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/Bnk9xh1jT-a/",
    "commentsCount": 2,
    "firstComment": "Great stuff hippos_softball nice post",
    "likesCount": 126,
    "timestamp": "2018-09-11T07:33:04.000Z"
  },
  {
    "caption": "Hippos pitcher Michal Holobradek helped his Bear Bottom Lodge team from Pennsylvania at the ISC World tournament in Canada to amazing 7th place. Michal won the individual award “Newcomer of the year” and got to the second all world all star team.\nThat’s absolutely awesome!!! We’re proud of you kid!!! #hippos #havlickuvbrod #softball #bearbottomlodge #czechsoftball #isctheshow",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/BmsWOFzDo_i/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 102,
    "timestamp": "2018-08-20T07:49:58.000Z"
  },
  {
    "caption": "📸 @benyphoto_czech",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CGXdPQGA2tV/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 124,
    "timestamp": "2020-10-15T13:51:51.000Z"
  },
  {
    "caption": "Our brothers Michal and Jakub play this winter in Auckland, New Zealand. In their very first weekend they helped Howick team to beat Marist 2:0. Big pitching matchup Holobradek x Shannon won our kid (complete game with 16 K’s). Well done Hippos 👍🏼 #hippos #havlickuvbrod #czechsoftball #aucklandsoftball",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/BbeGM64jrdA/",
    "commentsCount": 1,
    "firstComment": "Mike is absolutely the BEST 👍",
    "likesCount": 75,
    "timestamp": "2017-11-14T09:15:18.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CTM6JPVsDNG/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 122,
    "timestamp": "2021-08-30T14:20:55.000Z"
  },
  {
    "caption": "There are some trophies to defend next year 🏆🏆🏆🏆 U16, U19, U22 and men’s team, they all are 2017 champs!\n#hippos #havlickuvbrod #softball #czechsoftball #champs",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/BcJ-ENbjkj9/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 67,
    "timestamp": "2017-12-01T10:10:47.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/Cq0Ijhys9B8/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 82,
    "timestamp": "2023-04-09T11:59:17.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CTj3BhnsoDZ/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 81,
    "timestamp": "2021-09-08T12:16:11.000Z"
  },
  {
    "caption": "7 years in a row Hippos made a semifinal serie!!!\n#alwaysoctober #hippos #havlickuvbrod #softball #czechsoftball #playoffs #defendingchampions",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/BZLhmL7FFjC/",
    "commentsCount": 1,
    "firstComment": "Wish I was there",
    "likesCount": 49,
    "timestamp": "2017-09-18T11:06:19.000Z"
  },
  {
    "caption": "Season is over. After 2 champs years Hippos finished second in 2018. Still not bad.\nBig thanks to all our fans and club members.\nNext year we will be back stronger and bring the trophy back home again 🏆  #hippos #havlickuvbrod #softball #czechsoftball",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/BpWwQMqnzSC/",
    "commentsCount": 2,
    "firstComment": "Champions 😍😍💪",
    "likesCount": 136,
    "timestamp": "2018-10-25T12:08:20.000Z"
  },
  {
    "caption": "Po druhém finálovém zápase vedeme ve finálové sérii 2:0🥎\n#gohippos\n\n📸 @benyphoto_czech",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CF_7-MkgJYp/",
    "commentsCount": 2,
    "firstComment": "Hey Guys,how are you all? Its Tysons Mum and Dad here..",
    "likesCount": 200,
    "timestamp": "2020-10-06T10:38:38.000Z"
  },
  {
    "caption": "..and the best team in the country are Hippos again!!! 🏆🏆 #hippos #havlickuvbrod #2017champs #backtobackchamps #czechsoftball",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/BaUnXoolcTZ/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 79,
    "timestamp": "2017-10-16T20:21:19.000Z"
  },
  {
    "caption": "That smell of the freshly mowed grass before game day ☀️ Winter is over, softball is back! ⚾️ #newseason #hippos #havlickuvbrod #softball #czechsoftball #hipposarena",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/BhzjvRpjZAH/",
    "commentsCount": 1,
    "firstComment": "Ha Ha,Winter is coming here..Have a great season Hippos,from Tysons mum,Aussie Aussie Aussie",
    "likesCount": 81,
    "timestamp": "2018-04-20T20:25:48.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CTM6NV7slH_/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 120,
    "timestamp": "2021-08-30T14:21:29.000Z"
  },
  {
    "caption": "První cenné vítězství z finálové série nad @beaverschomutov 🥎",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CF_7SLag_Y5/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 167,
    "timestamp": "2020-10-06T10:32:38.000Z"
  },
  {
    "caption": "Tento pátek extraliga mužů u nás v hippos aréně 🥎!",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CTNOkPpsejN/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 92,
    "timestamp": "2021-08-30T17:19:22.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CguPLoeM_F6/",
    "commentsCount": 2,
    "firstComment": "Acaso es el mismo pitcher que salió campeón Panamericano de Softbol U23🇦🇷💙🤍 @tuttee_",
    "likesCount": 109,
    "timestamp": "2022-08-01T15:47:48.000Z"
  },
  {
    "caption": "HAPPY NEW YEAR AND HAVE FUN IN 2019!!! ⭐️🥎⭐️",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/BsDG8kFAQ8V/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 106,
    "timestamp": "2018-12-31T10:36:00.000Z"
  },
  {
    "caption": "The second best team in Europe in 2017 is Hippos Havlickuv Brod!\n#hippos #havlickuvbrod #softball #supercup2017 #silvermedal #czechsoftball #fearhb",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/BYpaMs6jho1/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 73,
    "timestamp": "2017-09-05T05:07:29.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/CTM6EUhM-tk/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 93,
    "timestamp": "2021-08-30T14:20:15.000Z"
  },
  {
    "caption": "Hippos under 22 boys are back to back league champs! 🏆🏆 Good job kids! #hippos #havlickuvbrod #czechsoftball #2017champs #fearhb",
    "ownerFullName": "Hippos Havlíčkův Brod 🥎",
    "ownerUsername": "hippos_softball",
    "url": "https://www.instagram.com/p/BY37AAZFW4o/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 55,
    "timestamp": "2017-09-10T20:23:29.000Z"
  },
    {
    "caption": "Tak se to podařilo! 🏆🥇Muži se stali nejlepším sportovním kolektivem okresu Uh. Hradiště! 👍💪Děkujeme všem za hlasy🙏♥️🥎🐌",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Cq45-W9NJGv/",
    "commentsCount": 1,
    "firstComment": "👏❤️",
    "likesCount": 58,
    "timestamp": "2023-04-11T08:28:05.000Z"
  },
  {
    "caption": "Přijďte o víkendu fandit našim kadetkám🙏🥎🐌 Jsou to borky☝️💪👍",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Cq8ad8QNOxB/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 55,
    "timestamp": "2023-04-12T17:09:44.000Z"
  },
  {
    "caption": "V pátek, případně v sobotu se naše juniorky utkají v kvalifikačním turnaji o dvě postupová místa do druhé ligy juniorek. Přijďte je podpořit👍🥎🐌💪 Začínáme v 9:30☝️",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CqnDye7AAGc/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 75,
    "timestamp": "2023-04-04T10:07:31.000Z"
  },
  {
    "caption": "Další kolo školské ligy v T-ball snad naposledy v hale. Příště už na hřišti☀️🙏👍💪🥎",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Cqmv3-9AX9O/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 82,
    "timestamp": "2023-04-04T07:13:30.000Z"
  },
  {
    "caption": "V sobotu se na Mlatevni představí extraliga juniorů💪🐌🥎 Bude se na co dívat☝️ Přijďte🙏👍",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Cq8ao_dN1ZB/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 62,
    "timestamp": "2023-04-12T17:11:15.000Z"
  },
  {
    "caption": "Kadetky ovládly první kolo Ligy kadetek! ❤️\nZa slunečného počasí přivedly poslední zápas do tie-breaku a otáčí zápas na 7:6! Výhra v kapse, jedeme dál! 🤩",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CrGaUsZNWQk/",
    "commentsCount": 1,
    "firstComment": "❤️❤️👏👏🔥🔥",
    "likesCount": 106,
    "timestamp": "2023-04-16T14:20:53.000Z"
  },
  {
    "caption": "‼️POZOR ZMĚNA‼️ Turnaj se odehraje kvůli nepřízni počasí JEN V NEDĚLI‼️ (Zkrácenou variantou.)",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CrBBjTWN_jL/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 48,
    "timestamp": "2023-04-14T12:08:13.000Z"
  },
  {
    "caption": "Na Velký pátek odehráli kadeti na domácí Mlatevni, v nepříznivém zimním počasí, další kolo Moravské ligy🥎",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CqvxKhSNxNT/",
    "commentsCount": 2,
    "firstComment": "🥎💪",
    "likesCount": 96,
    "timestamp": "2023-04-07T19:17:56.000Z"
  },
  {
    "caption": "Juniorky dnes, po včerejší bilanci 1:1 na zápasy, rozhodující zápas prohrály. A tak se z postupu do druhé ligy radovaly hráčky Joudrs B Praha. Gratulujeme soupeřkám👏👍",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Cqyfay8NR61/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 102,
    "timestamp": "2023-04-08T20:40:35.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Cq8aQ2SNQS4/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 39,
    "timestamp": "2023-04-12T17:07:57.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CqsHejjgbpK/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 35,
    "timestamp": "2023-04-06T09:15:57.000Z"
  },
  {
    "caption": "Také kadeti se představí v mrazivém počasí v pátek na Mlatevni💪👍🐌🥎",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Cqr6CXQt_5w/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 68,
    "timestamp": "2023-04-06T07:18:30.000Z"
  },
  {
    "caption": "Ženy B si poradily s muži B a berou vítězství☝️💪 Krev a pot! Souboj titánů💪😂",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CqdxD0UNvmZ/",
    "commentsCount": 1,
    "firstComment": "❤️🔥👏",
    "likesCount": 103,
    "timestamp": "2023-03-31T19:30:41.000Z"
  },
  {
    "caption": "Zástupci Snails vezou z turnaje Sammy Japan Masters Cup 2023 medaile💪🥎🐌 Muži se svým International Men’s týmem získali zlato🥇a ženy s týmem Sammy’s 35+ vybojovaly bronzové medaile🥉💪",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Cpv09OXv2Kw/",
    "commentsCount": 2,
    "firstComment": "🙌🙌🙌",
    "likesCount": 146,
    "timestamp": "2023-03-13T23:19:41.000Z"
  },
  {
    "caption": "Nová sezóna v Kunovicích začne už tento pátek přátelským zápasem našich B týmů. Přijďte na Mlatevňu oba týmy podpořit🥎",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CqR-cFFNHnA/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 71,
    "timestamp": "2023-03-27T05:36:43.000Z"
  },
  {
    "caption": "Kadetky dnes v Otrokovicích obsadily první místo na posledním turnaji Moravské ligy kadetek 🤩\nTak příště už venku ! 🥎 #kadetkyy",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CpX4k68tyJ_/",
    "commentsCount": 1,
    "firstComment": "❤️",
    "likesCount": 76,
    "timestamp": "2023-03-04T16:09:32.000Z"
  },
  {
    "caption": "Další kolo školské ligy B-Ball v plném proudu. 🥎🐌",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CqC7ICJgM9C/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 92,
    "timestamp": "2023-03-21T09:19:09.000Z"
  },
  {
    "caption": "Gratulujeme na Kanáry! 💪👍😀🥇\nMatyáš Zelinka byl pozván na mezinárodní turnaj na Kanárské ostrovy, který odehrál za domácí tým společně s kluky z Ledenic. Finále vyhráli až v prodloužení. \n\nParádní práce👏👏👏\n\n#clubcapitalinos #GranCanariaInternacionalCupSoftballFastpitchMens",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CpZotYTMz5z/",
    "commentsCount": 1,
    "firstComment": "❤️🔥👏",
    "likesCount": 141,
    "timestamp": "2023-03-05T08:29:22.000Z"
  },
  {
    "caption": "Softball spojuje lidi na celém světě💪🥎🪢\nDůkazem je turnaj Sammy Japan Masters Cup v Japonsku, kam byli letos pozváni i hráči a trenéři Snails🐌🥎🙏💪",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CpkGzj0StB4/",
    "commentsCount": 1,
    "firstComment": "❤️🔥👏",
    "likesCount": 160,
    "timestamp": "2023-03-09T10:04:45.000Z"
  },
  {
    "caption": "Juniorky si z Moravské ligy žen v Trnavě odvážejí prvenství🥇💪🐌🥎 Byl to po všech stránkách povedený turnaj😉",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CqNzsumNrfd/",
    "commentsCount": 2,
    "firstComment": "Šikulky.❤️",
    "likesCount": 104,
    "timestamp": "2023-03-25T14:45:54.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CpPgrtON6Xw/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 45,
    "timestamp": "2023-03-01T10:06:49.000Z"
  },
  {
    "caption": "Ženy se účastnily nedělního turnaje Slovnaft Apollo cup v Bratislavě. Probojovaly se do finále, které jim o kousek uteklo, když zápas skončil výsledkem 3:0. #snailszeny",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Cokj7CptzLF/",
    "commentsCount": 2,
    "firstComment": "❤️🔥👏",
    "likesCount": 96,
    "timestamp": "2023-02-12T17:47:47.000Z"
  },
  {
    "caption": "Juniorky dnes v Otrokovicích odehrály 2. turnaj Moravské ligy žen a juniorek. Ve třech odehraných zápasech nedaly soupeřům šanci a vše vyhrály.\n#snailsjuniorky",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CoiHNrgt_hN/",
    "commentsCount": 2,
    "firstComment": "Gratuluji👏",
    "likesCount": 115,
    "timestamp": "2023-02-11T18:58:27.000Z"
  },
  {
    "caption": "Kadetky se dnes představily na domácím turnaji druhého kola Moravské ligy kadetek! \nPo celý den předváděly slušnou hru jak v obraně, tak v útoku! 🐌 #Kadetkyy",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CoQKjGCN6Sp/",
    "commentsCount": 1,
    "firstComment": "❤️",
    "likesCount": 118,
    "timestamp": "2023-02-04T19:41:15.000Z"
  },
  {
    "caption": "",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CpPgn0rNMqX/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 55,
    "timestamp": "2023-03-01T10:06:18.000Z"
  },
  {
    "caption": "Dnešní neděli strávili malí šneci na druhém kole Moravské ligy T-Ballu, které se konalo v Břeclavi. Domů vezmeme druhé a čtvrté místo. Šnečci předvedli skvělou hru a napínavé finále, kde jim první místo uteklo jen o vlásek. Děkujeme všem hráčům, hráčkám a fanouškům! ❤️🐌",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Co2QH3at-eR/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 71,
    "timestamp": "2023-02-19T14:41:06.000Z"
  },
  {
    "caption": "Fandime 👍👏#baseballczech ♥️",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Cpt9i1Uy_G4/",
    "commentsCount": 4,
    "firstComment": "👏",
    "likesCount": 167,
    "timestamp": "2023-03-13T05:56:14.000Z"
  },
  {
    "caption": "Hlasujte pro sportovce města Kunovice za rok 2022👍 V kategorii nad 15. let byl nominován DAVID VÍCHA💪🥎🐌\nHlasovat můžete prostřednictvím hlas.lístku otištěného v místním Kunovjanu📝🗞️",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/Co9J7FKN1Q9/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 94,
    "timestamp": "2023-02-22T07:01:37.000Z"
  },
  {
    "caption": "Softball, pohyb, hra, zábava a radost - takové bylo dnešní kolo školské ligy v B-Ballu 🥎🐌",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CpNDzjSNP-A/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 74,
    "timestamp": "2023-02-28T11:16:01.000Z"
  },
  {
    "caption": "Kadeti v neděli ve Starém Městě odehráli 3. turnaj Moravské ligy. První zápas proti Severu Brno těsně prohráli 4:5, ve druhém zápase proti Locos Břeclav zvítězili 7:0. Kadety v zápasech doplnili tři hráči z žákovské kategorie U13, Lukáš Hubík, Adam Nemrava a Ondřej Zelinka💪🥎🐌",
    "ownerFullName": "Snails Kunovice",
    "ownerUsername": "snailskunovice",
    "url": "https://www.instagram.com/p/CpaQCsgtECB/",
    "commentsCount": 2,
    "firstComment": "👏🔥👏",
    "likesCount": 83,
    "timestamp": "2023-03-05T14:13:04.000Z"
  },
    {
    "caption": "⚾️ VÍKEND | Deště ustály a jdeme na to! \n🏰 V neděli proti @baseball.trebic na Tempu!\n#tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CrFvhh1MYml/",
    "commentsCount": 2,
    "firstComment": "Třetí zápas bude hostit Třebíč v PONDĚLÍ od 19:00.",
    "likesCount": 117,
    "timestamp": "2023-04-16T08:06:53.000Z"
  },
  {
    "caption": "❌✅ MUŽI A | Nedělní double nerozhodl o vítězi celé série. Jedno vítězství bralo Tempo a jedno @baseball.trebic .\n📅 Třetí zápas série je na programu v pondělí od 19:00 v Třebíči.\n#tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CrITZL_r4ka/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 69,
    "timestamp": "2023-04-17T07:58:48.000Z"
  },
  {
    "caption": "✅ MUŽI A | Stejně jako před týdnem jsme uhájili domácí tvrz a sérii o Prahu zakončujeme vítězstvím!\n📅 Příštím soupeřem Tempa bude o nadcházejícím víkendu Třebíč Nuclears!\n#tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/Cq1GmoYrEsj/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 87,
    "timestamp": "2023-04-09T21:01:28.000Z"
  },
  {
    "caption": "📷 DERBY | První zápas sice připadl soupeři, ale nový den přináší i novou příležitost uspět! \n💪🏼 V sobotu od 13:00 v Eagles Parku! \n#tempovsrdci #czech #baseball",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CqxNy2pLa9i/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 163,
    "timestamp": "2023-04-08T08:47:21.000Z"
  },
  {
    "caption": "❌ MUŽI A | Ani druhá bitva o Prahu nepřinesla vítězství.\n📅 Trojlístek zápasů mezi Tempem a Eagles uzavře nedělí měření sil na Tempu od 13:00.\n#tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CqzreItMUny/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 89,
    "timestamp": "2023-04-09T07:45:09.000Z"
  },
  {
    "caption": "❌ MUŽI A | Úvodní derby připadlo po bodové nadílce zelenému týmu.\n📅 Série pokračuje v SOBOTU od 13:00 opět v Eagles Parku.\n#tempovsrdci #czech #baseball",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CqxIlKcr6nI/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 85,
    "timestamp": "2023-04-08T08:01:47.000Z"
  },
  {
    "caption": "❌ PROHRA | Páni zahájili novou sezonou porážkou na půdě @dracibrno .\n🏰 Série se nyní přesouvá do Prahy. V neděli se na Tempu bude hrát od 13:00.\n🏟 Doražte na baseball! \n\n#tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CqfxzgHMS19/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 79,
    "timestamp": "2023-04-01T14:15:41.000Z"
  },
  {
    "caption": "✅ WIN | Doma to je hnedka jiná. \n💪🏼 @dracibrno jsme oplatili sobotu a z neúplného prvního víkendu odcházíme s bilancí 1-1.\n⚔️ Příští víkend je na řadě derby proti @eagles_muzi ! \n📷: @benyphoto_czech \n\nNeváhejte a přijďte na baseball! #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CqixcCuLY4u/",
    "commentsCount": 1,
    "firstComment": "👏👏👏👏",
    "likesCount": 142,
    "timestamp": "2023-04-02T18:10:12.000Z"
  },
  {
    "caption": "🤷🏻‍♂️ | Přišel, viděl, odpálil HR! \n🔥 Vítej po letech zpátky na Tempu @martincervenka28 !\n📷: @benyphoto_czech \n#tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/Cqm2N61rqE5/",
    "commentsCount": 1,
    "firstComment": "He’s got that dawg in him🔥",
    "likesCount": 240,
    "timestamp": "2023-04-04T08:08:55.000Z"
  },
  {
    "caption": "⚔️ PROTI DRAKŮM | Tempo zahajuje extraligovou sezónu v Brně proti @dracibrno !\n📅 V sobotu v Brně a v neděli se týmy představí v Praze! \n💙 Dorazíte na Tempo? \n\n#tempovsrdci #czech #baseball",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CqfRt5-rklD/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 94,
    "timestamp": "2023-04-01T09:35:18.000Z"
  },
  {
    "caption": "⚔️ DERBY | Víkend bude patřit soubojům o Prahu proti @eagles_muzi !\n📅 V pátek a v sobotu u zelených a v neděli pak uzavřeme sérii na Tempu! \n\n#tempovsrdci #czech #baseball",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CqpgiVmrqxC/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 86,
    "timestamp": "2023-04-05T08:57:12.000Z"
  },
  {
    "caption": "⚾ EXTRALIGA 2023 | Muži se o víkendu vrací na extraligová kolbiště @baseballczech !\n📅 Známe již kompletní rozpis letošního ročníku, takže pište do kalendářů a plňte diáře zápasy Tempa!\n\n#tempovsrdci #tempopower #czech #baseball",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CqcdmiQrPpR/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 116,
    "timestamp": "2023-03-31T07:21:26.000Z"
  },
  {
    "caption": "📋 POSILA | Druhou sezónu zahájí v dresu Tempa 🇻🇪Venezuelan @keibertpetit !\n⚾️ Muž mnoha rolí - silový pálkař, šikovný catcher a vnější polař bude součástí týmu pro sezónu 23!\n💙 Vítej zpátky, Keiberte! #tempovsrdci #czech #baseball",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CoIXMApLiWs/",
    "commentsCount": 9,
    "firstComment": "🔥 mine client win @tempo_praha",
    "likesCount": 174,
    "timestamp": "2023-02-01T18:57:47.000Z"
  },
  {
    "caption": "🏆 ŽENY A | Softbalistky Tempa v zimě nelenoší a porovnávají se se zahraniční konkurencí!\n🥇 Sílu Tempa naposledy pocítily soupeřky v německém Bonnu, kde dámy kralovaly a odvezly si turnajové prvenství! #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CphkuC1Ms5Q/",
    "commentsCount": 1,
    "firstComment": "Congrats, Ladies 👏👏👏🔥❤️",
    "likesCount": 146,
    "timestamp": "2023-03-08T10:28:26.000Z"
  },
  {
    "caption": "🏅 OCENĚNÍ | Přišel, viděl a od té chvíle je k nezastavení! Trenér Milan Humaj šéfuje ženským týmům na Tempu a společně s kolegy pomáhají v růstu množství hráček pro celý @czechsoftball !\n😎 Dámy a pánové, je nám ctí Vám představit trenéra sezóny v ženských kategoriích, trenér Milan Humaj! \n💙 Trenére, známe Vás a víme, že nezapomínáte. Proto ocenění patří nejen trenéru Humajovi, ale celému realizačnímu týmu včetně @petradiblikova a @vodickova.monika ! Gratulujeme! #tempovsrdci #tempofamily #czech #softball",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CoDXm4grcUE/",
    "commentsCount": 2,
    "firstComment": "🙌",
    "likesCount": 143,
    "timestamp": "2023-01-30T20:25:15.000Z"
  },
  {
    "caption": "🍾🎉 SILVESTR | Poslední den roku 22 je tady! \n😎 Jak bude vypadat vaše čekání na půlnoc? Divočina jako @ala.nepomucky nebo poklidné posezení ve stylu @marekminarikk ? #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/Cm1N7BDLsOV/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 112,
    "timestamp": "2022-12-31T11:59:51.000Z"
  },
  {
    "caption": "🌏 WBC | Převeliká gratulace do Tokia! Národní tým pohádkově zvládl první utkání a porazil Čínu! Dobrá práce @baseballczech ! \n🇨🇿 Atmosféru Tokyo Dome okusila přímo na hřišti i trojice hráčů Tempa - @filipsmola s @martincervenka28 nastoupili v základní sestavě a @marekminarikk uzavřel zápas na kopci! \n📷: @baseballczech \n\n#tempovsrdci #czech #baseball #czechin",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/Cpm2nMqLkO_/",
    "commentsCount": 1,
    "firstComment": "Great game and win that the beautiful of baseball nothing is write until the last out, congratulations",
    "likesCount": 268,
    "timestamp": "2023-03-10T11:40:59.000Z"
  },
  {
    "caption": "👶 U10/U11 | Mládežníci v novém roce nelení a již objíždějí turnaje. \n✅ Ovládnout se jim podařilo hnedka ten první na Joudrs!\n💙 Gratulace týme a držíme palce! #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CnCu2tbr-5t/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 86,
    "timestamp": "2023-01-05T17:57:45.000Z"
  },
  {
    "caption": "⚔️ DERBY | Velikonoční derby proti @eaglespraha před námi!\n🤔 Poznáte dva hráče, kteří doplnili tým na poslední chvíli? #tempovsrdci #baseball #czech",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/Cqut794LKay/",
    "commentsCount": 2,
    "firstComment": "Siiiiiiii @keibertpetit 🔥🔥🔥🔥😍",
    "likesCount": 248,
    "timestamp": "2023-04-07T09:30:29.000Z"
  },
  {
    "caption": "🇺🇸 SMĚR USA | Za oceán míří další “tempák”! Ondřej Vank bude v sezóně 2023 studovat v USA a zároveň oblékat dres @combinebase !\n💙 Držíme ti palce a drž se, @vankondrej ! #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/Cm6XrU1LArP/",
    "commentsCount": 5,
    "firstComment": "Well deserved 🫡 @vankondrej",
    "likesCount": 309,
    "timestamp": "2023-01-02T12:01:17.000Z"
  },
  {
    "caption": "🔥 POSILA | V dresu Tempa poprvé naskočil do EXL, uteklo 15 let, prošel svět a je zpátky - vítej @martincervenka28 !\n📋 Martin Červenka je první posilou Tempa pro sezónu 23, kterou s národním týmem @baseballczech zahájí na @wbcbaseball ! \n💙 Ať se ti na Tempu i v nároďáku daří, Martine! #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CnoX_c5LjWA/",
    "commentsCount": 2,
    "firstComment": "Ať se daří v novém dresu 🔥⚾️",
    "likesCount": 282,
    "timestamp": "2023-01-20T08:49:06.000Z"
  },
  {
    "caption": "🏅 OCENĚNÍ | Celou sezónu házela jako ďas, dováděla pálkařky k šílenství a do toho uměla vykouzlit úsměv od ucha k ucha! \n😎🔥 Představujeme vám nejlepší nadhazovačku sezony a MVP play-off extraligy @czechsoftball Martinu Bláhovou! \n💙 Obrovská gratulace @mimousek ! #tempovsrdci #tempopower #czech #softball",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CoDHXeALcVX/",
    "commentsCount": 2,
    "firstComment": "❤️",
    "likesCount": 231,
    "timestamp": "2023-01-30T18:03:20.000Z"
  },
  {
    "caption": "🇨🇿 WBC | Tempo v Tokio Dome! \n😍 A že jim to sekne, uznejte?! 📸: @baseballczech \n\n#czech #baseball #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CpxUZznsqsO/",
    "commentsCount": 1,
    "firstComment": "Určitě, děkujeme borci za skvělou reprezentaci a super zápasy, byli jste úžasní ⚾️🇨🇿👏🔝❤",
    "likesCount": 272,
    "timestamp": "2023-03-14T13:13:42.000Z"
  },
  {
    "caption": "🆕 POSILY | Nadhazovačská baterie Tempa hlásí dva nováčky pro sezonu 23!\n💪🇻🇪 Keibert Petit nebude v týmu jediným Venezuelanem, protože mu přibydou dva pravorucí parťaci - Jhonny Durán a Adonai Goyo!\n💙 Pánové, vítejte na Tempu! Bienvenidos! #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CoXwvLkrH4m/",
    "commentsCount": 9,
    "firstComment": "Pura 🔥 háblale",
    "likesCount": 172,
    "timestamp": "2023-02-07T18:29:38.000Z"
  },
  {
    "caption": "🍾 | Doufáme, že jste po silvestrovských večírcích všichni v pořádku! \n🥴 Jak jste slavili? Odpočíváte nebo už/ještě skotačíte #tempofamily ? #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/Cm3vtyGL_kz/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 154,
    "timestamp": "2023-01-01T11:33:37.000Z"
  },
  {
    "caption": "🏆 U11 | KRÁLOVÉ KAHANU\nJedenáctky kralovaly na téměř již tradičním zimním turnaji Kladenský kahan!\n🥇 Ve finále si Tempo poradilo s domácími @minerskladno a odváží si nejcennější medaile!\n👏 Skvělou týmovou práci podpořila ještě spolupráce K+K Kryštofů Kotoučka a Babůrka. Spolupráce nadhazovače a catchera jak se sluší a patří!\n💙 Gratulace, týme! #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CoZSUDLrzOq/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 73,
    "timestamp": "2023-02-08T08:42:16.000Z"
  },
  {
    "caption": "👶 NOVÉ TVÁŘE | Přijďte na Tempo vyzkoušet baseball! Hledáme nové tempáky narozené v letech 2013 až 2016!\n😍 Těšíme se na Vás! #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CoJ5VJ2rZKn/",
    "commentsCount": 1,
    "firstComment": "👶😍",
    "likesCount": 49,
    "timestamp": "2023-02-02T09:15:22.000Z"
  },
  {
    "caption": "😎 PONDĚLÍ | Všichni tvrdí, že pondělí za moc nestojí…Akorát ty víš, že je to další den, kdy se můžeš 💪🏼 zlepšit - tak makej ať jsi lepší než minulé pondělí! #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CnwvzSSszY2/",
    "commentsCount": 1,
    "firstComment": "💪⚾️",
    "likesCount": 100,
    "timestamp": "2023-01-23T14:51:05.000Z"
  },
  {
    "caption": "🌏 WBC | Baseballový svět je na nohou, protože začíná @wbcbaseball !\n🇨🇿 Historické vystoupení si připíše i @baseballczech včetně zástupců Tempa!\n💪🏼 V nominaci figurují @martincervenka28 & @marekminarikk & @filipsmola !\n💙 Držíme Vám palce, týme! \n\n📷: @baseballczech \n#tempovsrdci #czechin",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CphuMYMsFDy/",
    "commentsCount": 0,
    "firstComment": "",
    "likesCount": 119,
    "timestamp": "2023-03-08T11:51:13.000Z"
  },
  {
    "caption": "🏠 ZPÁTKY DOMA | Je to nezvyk v jiném dresu, ale pořád je to ten stejný @jrab42 ! \n💙 Osm sezon v tom nejkrásnějším dresu se nezapomíná! #tempovsrdci",
    "ownerFullName": "Tempo Praha",
    "ownerUsername": "tempo_praha",
    "url": "https://www.instagram.com/p/CrIff7jrgPk/",
    "commentsCount": 3,
    "firstComment": "🔥🔥🔥",
    "likesCount": 174,
    "timestamp": "2023-04-17T09:44:35.000Z"
  }
]

# Convert JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Export DataFrame to an Excel file
df.to_excel("softball_posts.xlsx", index=False)