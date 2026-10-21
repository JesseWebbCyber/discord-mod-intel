# Discord Moderation Threat Intelligence & Banlist

Curated blocklist of malicious Discord user IDs, scam bots, and raid accounts for cross-server security.

## Raw Endpoints & Batch Formats

- **Newline separated (`banlist.txt`):**
  ```text
  https://raw.githubusercontent.com/JesseWebbCyber/discord-mod-intel/main/banlist.txt
  ```
- **Comma separated for batch copy/paste (`banlist-comma.txt`):**
  ```text
  https://raw.githubusercontent.com/JesseWebbCyber/discord-mod-intel/main/banlist-comma.txt
  ```
- **Structured JSON (`banlist.json`):**
  ```text
  https://raw.githubusercontent.com/JesseWebbCyber/discord-mod-intel/main/banlist.json
  ```

## Quick Bot Integration Examples

### Bash / cURL loop
```bash
curl -s https://raw.githubusercontent.com/JesseWebbCyber/discord-mod-intel/main/banlist.txt | while read -r id; do
  echo "Banning ID: $id"
  # e.g., trigger moderation bot ban endpoint
done
```

### Python (discord.py)
```python
import urllib.request

URL = "https://raw.githubusercontent.com/JesseWebbCyber/discord-mod-intel/main/banlist.txt"
with urllib.request.urlopen(URL) as response:
    banned_ids = {line.strip() for line in response.read().decode().splitlines() if line.strip()}

@bot.event
async def on_member_join(member):
    if str(member.id) in banned_ids:
        await member.ban(reason="Known malicious account on cross-server blocklist")
```

---

## Active Reported Accounts (2961 IDs)

Ordered from newest to oldest.

| Discord ID | Date Reported | Ban Reason |
| :--- | :--- | :--- |
| `704031430325436537` | 10/19/2026 | Harassment raid participant engaging in coordinated server trolling. |
| `484765847546626068` | 10/19/2026 | Harassment raid participant engaging in severe trolling and channel disruption. |
| `1313451022491848764` | 10/19/2026 | Coordinated advertising raid account using fake member hype to promote third-party events. |
| `1561031456392876142` | 10/18/2026 | Ban evasion alt account used to re-enter servers after prior moderation removal. |
| `1373356582657589398` | 10/17/2026 | Automated bot sending unsolicited spam links into member direct messages. |
| `1242212409498927220` | 10/17/2026 | Automated bot account sending unsolicited recruitment scams in member direct messages. |
| `1556010033479815328` | 10/15/2026 | Coordinated advertising raid account using fake member hype to promote third-party events. |
| `1555629557510447115` | 10/15/2026 | Coordinated advertising raid account using fake member hype to promote third-party events. |
| `1551464928248856607` | 10/15/2026 | Coordinated advertising raid account using fake member hype to promote third-party events. |
| `938710016289046608` | 10/12/2026 | Account ('f0rgotte1n') mass-spamming unauthorized NSFW server invites. |
| `751903171198189618` | 10/12/2026 | Disruptive troll account flagged for severe behavioral misconduct and harassment. |
| `1533229968656568393` | 10/09/2026 | Compromised account participating in coordinated malicious spam raids. |
| `1430353021946040410` | 10/09/2026 | Compromised account participating in coordinated malicious spam raids. |
| `1287854594482901005` | 10/09/2026 | Compromised account participating in coordinated malicious spam raids. |
| `1144325061654888649` | 10/09/2026 | Compromised account participating in coordinated malicious spam raids. |
| `1523754110409637980` | 10/08/2026 | Social engineering scammer attempting to trick members with fraudulent claims. |
| `1068874695702761482` | 10/08/2026 | Unsolicited DM spammer targeting server members with phishing links. |
| `1507457811381096458` | 10/07/2026 | Unsolicited DM spammer targeting members without shared mutual servers. |
| `687933479622934620` | 10/06/2026 | Account ('4m4y4s') distributing cryptocurrency phishing messages across servers. |
| `490188321226620928` | 10/06/2026 | Account ('danishgtr') distributing fraudulent cryptocurrency scam links. |
| `340714404314349570` | 10/05/2026 | Account ('kyotorun50') promoting deceptive cryptocurrency investment scams. |
| `953748748280946730` | 10/04/2026 | Persistent troll account ('lenoired') violating Discord ToS with hate speech and harassment. |
| `855443094870687794` | 10/04/2026 | Account flagged across moderation teams for suspicious targeting of minors. |
| `1555525351914999866` | 10/04/2026 | Malicious account reported for unsolicited advertising and deceptive links. |
| `1505223386199232674` | 10/04/2026 | Confirmed ban evasion alt ('sophus359353' / 'agdagfda') belonging to a serial harasser. |
| `1456722209656803483` | 10/04/2026 | Underage user engaging in hate speech and repeated racial slurs. |
| `1436422427142787243` | 10/04/2026 | Confirmed ban evasion alt ('yassingamer0317') belonging to a serial harasser. |
| `1426974684834041971` | 10/04/2026 | Confirmed ban evasion alt ('v3nk_i') used for silent lurking and evasion. |
| `1414752214051721348` | 10/04/2026 | Confirmed ban evasion alt ('ah23421') belonging to a serial harasser. |
| `1400825354435821730` | 10/04/2026 | Account ('vstromakias7') promoting fraudulent cryptocurrency scams. |
| `1383608829379346525` | 10/04/2026 | Deleted alt account identified in cross-server ban evasion network. |
| `1369678199201730602` | 10/04/2026 | Confirmed ban evasion alt ('ratchet0549') belonging to a serial harasser. |
| `1351938127530430536` | 10/04/2026 | Confirmed alt account ('matthewandre_x') used for ban evasion and harassment. |
| `1313958539773087845` | 10/04/2026 | Primary account ('lenoirsx_') of a persistent troll spreading hate speech and Discord ToS violations. |
| `1283321787341340744` | 10/04/2026 | Confirmed ban evasion alt ('hell706') belonging to a serial harasser. |
| `1197253997543825521` | 10/04/2026 | Confirmed ban evasion alt ('steavengameryt') belonging to a serial harasser. |
| `1196850086953631755` | 10/04/2026 | Promoted fraudulent 'MrBeast' cryptocurrency giveaway scams in chat. |
| `1110476666192535653` | 10/04/2026 | Confirmed ban evasion alt ('linux706') belonging to a serial harasser. |
| `1023079001985663126` | 10/04/2026 | Impersonated community staff members to target unsuspecting users in direct messages. |
| `400896526924251136` | 10/03/2026 | Compromised user account distributing phishing and account-stealing links. |
| `1519707665096507621` | 10/03/2026 | Scammer engaging in name-spoofing and deceptive identity theft. |
| `1286838349335629906` | 10/02/2026 | Automated adult-content / OnlyFans spam bot targeting server members. |
| `1555337843235102885` | 10/01/2026 | Scammer advertising fraudulent high-income / 'earn 100k' financial schemes. |
| `1287882355251478550` | 10/01/2026 | Compromised account distributing malicious links across tech servers. |
| `1492875609372885052` | 09/30/2026 | Malicious spam bot reported to Discord Trust & Safety for account compromise. |
| `406620720437788674` | 09/29/2026 | Deceptive account sharing server space to run targeted member phishing attacks. |
| `936358065207390238` | 09/11/2026 | Automated scam bot targeting community channels with malicious links. |
| `1545981820649218090` | 09/11/2026 | Automated scam bot targeting member direct messages with malicious links. |
| `1546840214960607243` | 09/08/2026 | Automated bot account scraping member lists and spamming fake job listings. |
| `1537455244928221206` | 09/04/2026 | Automated job listing spam bot posting fake employment opportunities. |
| `1395449757371076628` | 09/03/2026 | Automated scam bot masquerading as an AI firm to harvest user credentials. |
| `1504087093528231996` | 09/01/2026 | Underage user raiding community voice and text channels. |
| `797391110900285441` | 08/23/2026 | Compromised account flagged for cross-server spam and phishing outreach. |
| `1226567367941689536` | 08/23/2026 | Malicious bot account distributing unauthorized links and spam. |
| `1490501890109341919` | 08/21/2026 | Compromised account spreading fraudulent 'MrBeast' giveaway scams. |
| `946841687253213214` | 07/16/2026 | Flagged account reported across community mod teams for unauthorized solicitation. |
| `1484769295232794674` | 07/02/2026 | Automated bot account spamming fraudulent gambling service promotions. |
| `696257474420015114` | 06/23/2026 | Rogue or unauthorized bot account operating maliciously in shared community servers. |
| `1498951849493921943` | 06/04/2026 | Scam account ('@mike_heleket') conducting unauthorized outreach in direct messages. |
| `1340331428738502787` | 05/29/2026 | Compromised account flagged for persistent spam distribution. |
| `657811008550600705` | 06/06/2023 | Cross-server harasser removed from multiple communities for severe unprovoked abuse. |
| `353807196087386113` | 05/15/2023 | Severe raid account posting explicit violence and shock media into public channels. |
| `989603040237584426` | 06/27/2022 | Scam account conducting direct outreach to recruit members into financial carding fraud. |
| `520662535385382935` | 01/13/2022 | Phishing bot ('ShadowMW#6345') distributing deceptive credential-harvesting link 'steelseriesgifts.com'. |
| `406872051689848833` | 01/12/2022 | Phishing bot ('Labino#7065') distributing deceptive credential-harvesting link 'discrode.gift'. |
| `520916884434976768` | 01/12/2022 | Phishing bot ('Yasof#6850') distributing deceptive credential-harvesting link 'dilscord.gift'. |
| `872112674199187467` | 01/12/2022 | Phishing bot ('Wrapper#5955') distributing deceptive credential-harvesting link 'dlscord-newyear.com'. |
| `735469865858498672` | 01/12/2022 | Phishing bot ('0$Broke#1719') distributing deceptive credential-harvesting link 'discorl.gift'. |
| `669964169700966488` | 01/12/2022 | Phishing bot ('StabiloFueller#3838') distributing deceptive credential-harvesting link 'discord-me.com'. |
| `742997389039894579` | 01/11/2022 | Phishing bot ('Noman#0538') distributing deceptive credential-harvesting link 'discqrde.com'. |
| `468170807315660800` | 01/10/2022 | Phishing bot ('ELI#4653') distributing deceptive credential-harvesting link 'discord-go.com'. |
| `599503113568649225` | 01/10/2022 | Phishing bot ('lio PingPong#8476') distributing deceptive credential-harvesting link 'discqrdapp.com'. |
| `900987611617828925` | 01/10/2022 | Phishing bot ('pizzaeater#0158') distributing deceptive credential-harvesting link 'dicsord-giftes.ru'. |
| `785299035228733461` | 01/07/2022 | Phishing bot ('ad$m#8888') distributing deceptive credential-harvesting link 'discyrd.com'. |
| `880289489178734673` | 01/06/2022 | Phishing bot ('Roshan Balaji#9755') distributing deceptive credential-harvesting link 'web-discord.com'. |
| `532300289072693248` | 01/06/2022 | Phishing bot ('EL-3OMDA#9901') distributing deceptive credential-harvesting link 'dlscold.com'. |
| `514801721042534415` | 01/05/2022 | Phishing bot ('Raiden#8476') distributing deceptive credential-harvesting link 'discordnitros.com'. |
| `751749868615106620` | 01/05/2022 | Phishing bot ('Decker#9115') distributing deceptive credential-harvesting link 'discovd.com'. |
| `737504269196066877` | 01/05/2022 | Phishing bot ('๖ۣۜŁᎥgh͢͢͢𝖙F𝓡#3792') distributing deceptive credential-harvesting link 'discojd.com'. |
| `228972790303293440` | 01/05/2022 | Phishing bot ('Iceskill#0398') distributing deceptive credential-harvesting link 'gifs-discord.com'. |
| `235245065130344459` | 01/04/2022 | Phishing bot ('Iso#7104') distributing deceptive credential-harvesting link 'disdornitro.com'. |
| `767705735475363870` | 01/04/2022 | Phishing bot ('Mr.Franta#3495') distributing deceptive credential-harvesting link 'discord-to.com'. |
| `745202710495625226` | 01/04/2022 | Phishing bot ('Gaurang Dipnaik#7926') distributing deceptive credential-harvesting link 'disdorsnitro.com'. |
| `554722604850610177` | 01/03/2022 | Phishing bot ('Haven#0759') distributing deceptive credential-harvesting link 'discobd.com'. |
| `887404543929905214` | 01/03/2022 | Phishing bot ('Ryft#7872') distributing deceptive credential-harvesting link 'discoord-app.com'. |
| `734781277273849987` | 01/03/2022 | Phishing bot ('WizForLife#2718') distributing deceptive credential-harvesting link 'dicsord-given.ru'. |
| `226698518876782592` | 01/02/2022 | Phishing bot ('LowkeyZA777#4198') distributing deceptive credential-harvesting link 'discoord-app.com'. |
| `590795545841238026` | 01/02/2022 | Phishing bot ('Holycrusader#9018') distributing deceptive credential-harvesting link 'dlsordnltros.com'. |
| `808615656991358996` | 01/02/2022 | Phishing bot ('Div#3480') distributing deceptive credential-harvesting link 'discgrd.com'. |
| `730734145994752090` | 01/02/2022 | Phishing bot ('ADITYA RJ#5064') distributing deceptive credential-harvesting link 'discoord-app.com'. |
| `835923277644955679` | 01/02/2022 | Phishing bot ('ZenCircles#9257') distributing deceptive credential-harvesting link 'discords-to.com'. |
| `315511711199264768` | 01/02/2022 | Phishing bot ('Golden-Slayer#2162') distributing deceptive credential-harvesting link 'discoord-gift.com'. |
| `927177984631250955` | 01/02/2022 | Malicious scam account flagged and reported by community moderation. |
| `926490863260008458` | 01/01/2022 | Malicious account distributing cryptocurrency phishing scams. |
| `469550418955993090` | 01/01/2022 | Phishing bot ('𝐏𝐚𝐛𝐥𝐨#0001') distributing deceptive credential-harvesting link 'discord-to.com'. |
| `574336196587552778` | 01/01/2022 | Phishing bot ('Yunngphatty_#3219') distributing deceptive credential-harvesting link 'dlsordnltros.gifts'. |
| `752943162980434011` | 12/31/2021 | Phishing bot ('Khion#0430') distributing deceptive credential-harvesting link 'discordnitro.me'. |
| `926371055407349790` | 12/31/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `592949086299095050` | 12/31/2021 | Phishing bot ('BBBtidss#0704') distributing deceptive credential-harvesting link 'dlsordnltros.gifts'. |
| `488644588182044673` | 12/31/2021 | Phishing bot ('Warrior_14nation#3725') distributing deceptive credential-harvesting link 'discomd.com'. |
| `925870977798270987` | 12/30/2021 | Malicious scam account flagged and reported by community moderation. |
| `735244796679159868` | 12/30/2021 | Phishing bot ('Zombijcraft#5237') distributing deceptive credential-harvesting link 'disordsnltros.gifts'. |
| `751070095815475302` | 12/30/2021 | Phishing bot ('king azan#5246') distributing deceptive credential-harvesting link 'discoqd.com'. |
| `741922613282078722` | 12/30/2021 | Phishing bot ('DiscordUser#5393') distributing deceptive credential-harvesting link 'discoqd.com'. |
| `886345503594397738` | 12/30/2021 | Phishing bot ('Levii#4167') distributing deceptive credential-harvesting link 'dlscordfreegift.com'. |
| `925822177553563699` | 12/30/2021 | Malicious scam account flagged and reported by community moderation. |
| `551564786966724624` | 12/30/2021 | Phishing bot ('michaelscott#5346') distributing deceptive credential-harvesting link 'dicsords-gifts.ru'. |
| `904334448462528513` | 12/29/2021 | Phishing bot ('Hexonically#7877') distributing deceptive credential-harvesting link 'disccord-appss.ru'. |
| `667086763474419742` | 12/29/2021 | Phishing bot ('anxiety#4112') distributing deceptive credential-harvesting link 'discoqd.com'. |
| `925474354152755200` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925473938224578620` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925473709945401384` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925473588516093974` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925473528952795146` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925473269463797800` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925473094703939594` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925473086801838180` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925473080766234645` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925473077863784538` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925472793699696650` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925472774015819776` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925430171207606303` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925411320222867526` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925410897621565480` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925410606868222042` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925410487099850824` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925410459891404811` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925410051248763101` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925410041513791519` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925410025084710973` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925410020307374110` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925406791624458260` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925406756530700320` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925406402225258517` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925406232670535751` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925405896153104397` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925405811755335710` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925405516883173396` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925405488793919508` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925405416018567228` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925405200951431219` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925405137546133525` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925404840371318794` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925404832288895049` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925404790039650364` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925404722121293875` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925404512947142676` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925404499198238740` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925402638441381918` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925401986675900426` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925401962642571274` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925401604121853962` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925401552104095765` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925401483741118504` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925401178051850240` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925401134900867072` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400829161275412` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400815663992842` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400786308046968` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400758361407538` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400710030450719` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400473119359057` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400424914251796` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400355485917215` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400212623736842` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400165425250325` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400164703821885` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400090418483250` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925400052564918363` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925399946822303827` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925399880254509116` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925399826793918505` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925399680307822594` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925399542311047168` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925399508832116796` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925399209065189386` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925398911835856936` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925398894458859591` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925398873592168468` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925397003968581744` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925396551621292043` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925395969690980372` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925392955328573501` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925392074902224988` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925391665898864671` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925391293234946079` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925391124384874527` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925391113450311701` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925391108148699200` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925391087617605653` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925390627376603166` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925390554399932416` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925390550214017095` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925390549534527499` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925390542110609410` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925390541884117133` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925388062404526140` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925388027965079612` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925387510253760542` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925387508576055326` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925387508303409172` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925387498966896750` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925383522947051562` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925383521328070656` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925381628744831036` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925381574390874233` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925381097251029002` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925381010739318794` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925379547384406087` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925374367301517352` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925373655859494963` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925372920023380038` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925372656260374539` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925372314651074591` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925370400110702613` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925369231703416862` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925368854287384626` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925366456936464405` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925365755434901504` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925365592012259369` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925364816372187196` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925362021384486972` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925357582598701136` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925355307113250896` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925348542669807637` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925333489409212527` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925329500923920384` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925319840770699294` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925311721969705004` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925311235027779584` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925311049656332288` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925309903256551444` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925309819861233705` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925309648247074836` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925309173384757278` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925308872124690432` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925308364026679346` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925308161160794113` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925308111420534805` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925308022375477288` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307906876928001` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307626642878495` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307581436682300` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307459931865088` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307404063768606` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307355174936606` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307354109603902` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307320320294932` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307290591064184` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307109883645983` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307039280930826` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925307020054245427` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925306852676337694` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925306717321969696` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925306486257774602` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925306385896448001` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925306361854693429` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925306153766903808` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925306040038350879` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925306015833030667` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925305819011117117` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925305738216239144` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925305692615753730` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925305510431957072` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925305491364655164` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925305426256465920` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925305192717643846` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925305155044393010` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925305006066900993` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925304947917062175` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925304899871326268` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925304603812175882` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925304008380416031` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925303884556173333` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925303856588542022` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925303841891680277` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925303839668703242` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925303829090684928` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925303826116935760` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925296580125425665` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925292069310836746` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925291583337795625` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925290763225559081` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925290104057102376` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925274042674601995` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925273091599376415` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925271063103959050` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925261975657799710` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925260573002838056` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925259496085925898` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925258584386859059` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925257001066446849` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925255841400094753` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925254359355379762` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925252795077115905` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925249765069951016` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925249180207812680` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925242208704135189` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925241306475790376` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925240974156894299` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925240103570407534` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `925239488089849856` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `279367235099951105` | 12/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `710927718719422485` | 12/28/2021 | Phishing bot ('Gamer999M#9928') distributing deceptive credential-harvesting link 'discocd.com'. |
| `923193284074045473` | 12/28/2021 | Malicious scam account flagged and reported by community moderation. |
| `925292191260241931` | 12/28/2021 | Malicious scam account flagged and reported by community moderation. |
| `738817575701708850` | 12/28/2021 | Phishing bot ('Ahmad15s#1819') distributing deceptive credential-harvesting link 'discocd.ru'. |
| `740640308940767333` | 12/27/2021 | Phishing bot ('ℍ 𝕠 𝕧 𝕖 𝕣 ℂ 𝕒 𝕥#6740') distributing deceptive credential-harvesting link 'discocd.com'. |
| `882615947733631036` | 12/27/2021 | Phishing bot ('BONK LE BONK#3003') distributing deceptive credential-harvesting link 'discordsteamj.com'. |
| `489426823055278080` | 12/27/2021 | Phishing bot ('Nagito#6210') distributing deceptive credential-harvesting link 'dicsords-gift.ru'. |
| `924895460035010591` | 12/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `924081309222047765` | 12/26/2021 | Malicious scam account flagged and reported by community moderation. |
| `924792784379068477` | 12/26/2021 | Identified ban evasion alt account linked to previously banned user. |
| `918687467530493952` | 12/26/2021 | Malicious account distributing cryptocurrency phishing scams. |
| `500768988905865216` | 12/26/2021 | Phishing bot ('💀💀#4352') distributing deceptive credential-harvesting link 'discordevents.xyz'. |
| `763035973222662144` | 12/26/2021 | Phishing bot ('foxika04#7992') distributing deceptive credential-harvesting link 'diiscord-nitro.com'. |
| `750835145556230206` | 12/26/2021 | Phishing bot ('Tristin#6297') distributing deceptive credential-harvesting link 'discord.gift'. |
| `836047492012965948` | 12/25/2021 | Phishing bot ('._.#0008') distributing deceptive credential-harvesting link 'diiscord-nitro.com'. |
| `693122829906083870` | 12/25/2021 | Phishing bot ('MaxGamerRealm#7825') distributing deceptive credential-harvesting link 'steamdiscorda.com'. |
| `512502285864140810` | 12/25/2021 | Phishing bot ('JuJu#6001') distributing deceptive credential-harvesting link 'dfscord.com'. |
| `525679583882903557` | 12/25/2021 | Phishing bot ('scythe47#5104') distributing deceptive credential-harvesting link 'steam-nitro.xyz'. |
| `291828754429509632` | 12/24/2021 | Phishing bot ('Jiggly_Panda#0120') distributing deceptive credential-harvesting link 'diiscord-nitro.com'. |
| `899420566082175036` | 12/24/2021 | Scam account distributing deceptive Oculus promotional links. |
| `771087200904544286` | 12/24/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `686899707959836703` | 12/24/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `723166099058720810` | 12/24/2021 | Phishing bot ('Evanz#0371') distributing deceptive credential-harvesting link 'discrode-app.com'. |
| `729603292295987230` | 12/24/2021 | Phishing bot ('yi#8175') distributing deceptive credential-harvesting link 'diiscord-nitro.com'. |
| `553643049373138945` | 12/24/2021 | Phishing bot ('MARS#7995') distributing deceptive credential-harvesting link 'disordnltros.gifts'. |
| `826830345441640529` | 12/24/2021 | Phishing bot ('LUXURY_KIMO#7259') distributing deceptive credential-harvesting link 'dlisocrd.com'. |
| `692660105417588766` | 12/24/2021 | Phishing bot ('KARMELbtw#5412') distributing deceptive credential-harvesting link 'steam-nitro.xyz'. |
| `749599825099751426` | 12/23/2021 | Phishing bot ('Noob_Troller#6574') distributing deceptive credential-harvesting link 'discrode-gifte.club'. |
| `650416903751204915` | 12/23/2021 | Phishing bot ('xarindell#9057') distributing deceptive credential-harvesting link 'discrode-gifte.club'. |
| `529372729779159054` | 12/23/2021 | Phishing bot ('bid#0470') distributing deceptive credential-harvesting link 'discrode-gifte.club'. |
| `768093026685157397` | 12/22/2021 | Phishing bot ('Windows 11#1856') distributing deceptive credential-harvesting link 'nitro-one.xyz'. |
| `325152323800268800` | 12/22/2021 | Phishing bot ('znacky#6023') distributing deceptive credential-harvesting link 'dlscord-app.su'. |
| `204073474040266752` | 12/22/2021 | Phishing bot ('Sonred#7571') distributing deceptive credential-harvesting link 'dlscord-app.su'. |
| `521022094503444485` | 12/22/2021 | Phishing bot ('RudRed/Racronr15#6407') distributing deceptive credential-harvesting link 'discrode-gift.com'. |
| `858035529946103898` | 12/21/2021 | Phishing bot ('jayy#0890') distributing deceptive credential-harvesting link 'discrode-gift.com'. |
| `683287984040312840` | 12/21/2021 | Phishing bot ('M22#3428') distributing deceptive credential-harvesting link 'discrode-gift.com'. |
| `778039857091706880` | 12/20/2021 | Phishing bot ('BOBTHEFATCOUCH#0317') distributing deceptive credential-harvesting link 'disordnltro.xyz'. |
| `560934136093868034` | 12/20/2021 | Phishing bot ('マスタードージ#0007') distributing deceptive credential-harvesting link 'disordnltro.xyz'. |
| `912291130668908544` | 12/20/2021 | Phishing bot ('Revenge#2848') distributing deceptive credential-harvesting link 'steamsdiscordl.com'. |
| `470079342672740372` | 12/20/2021 | Phishing bot ('Jaybird101#4666') distributing deceptive credential-harvesting link 'discrode-gift.com'. |
| `543502420236435458` | 12/20/2021 | Phishing bot ('Shogunael#1660') distributing deceptive credential-harvesting link 'discrode-gift.com'. |
| `692584899403710474` | 12/19/2021 | Phishing bot ('ESKRA88#6760') distributing deceptive credential-harvesting link 'discord-gifft.com'. |
| `589547088996597783` | 12/19/2021 | Phishing bot ('deutsche#4904') distributing deceptive credential-harvesting link 'discord-gifft.com'. |
| `146415542885023745` | 12/18/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `295963440797974539` | 12/18/2021 | Phishing bot ('AyoWtf#6945') distributing deceptive credential-harvesting link 'steamdiscordf.com'. |
| `287475070362714112` | 12/16/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `68831600363700224` | 12/13/2021 | Phishing bot ('Rob (Rolling_Go)#0216') distributing deceptive credential-harvesting link 'segabits.com'. |
| `658367660030951440` | 12/04/2021 | Phishing bot ('§icy#0001') distributing deceptive credential-harvesting link 'discorde-gift.com'. |
| `492921239711776769` | 12/04/2021 | Phishing bot ('PÅŃÇÃKĘ#9394') distributing deceptive credential-harvesting link 'discorde-gift.com'. |
| `765846484729593856` | 12/03/2021 | Phishing bot ('Stone Owl#8875') distributing deceptive credential-harvesting link 'discorde-gift.com'. |
| `702553361752391763` | 11/26/2021 | Phishing bot ('D.Trump#7453') distributing deceptive credential-harvesting link 'discorcd-apps.com'. |
| `425570536307949568` | 11/17/2021 | Phishing bot ('oTazzz#9356') distributing deceptive credential-harvesting link 'discord.glfte.com'. |
| `833382059669716994` | 11/17/2021 | Phishing bot ('nobodys#4841') distributing deceptive credential-harvesting link 'discorcd-app.com'. |
| `824922788262969347` | 11/14/2021 | Phishing bot ('Purple#5231') distributing deceptive credential-harvesting link 'steamcommunityx.com'. |
| `900567543985623040` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900567458207895562` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900567321146429462` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900566663739613234` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900565924971700296` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900565422431145984` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900565414671679519` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900565062815739905` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900564854925041785` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900564672057577483` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900564020099162122` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900563717077471243` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900586263105634364` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900586209561157663` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900586106494529587` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900585752549814293` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900583376954720306` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900582819422679060` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900581114614263878` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900580937199399012` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900580128407560262` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900579976309530665` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900579765591887872` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900579214162554920` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900578980720177172` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900578972767756288` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900578780588937267` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900577520661962803` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900576248483434556` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900576223753810010` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900575846870441985` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900574864451174491` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900574168997838899` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900574008351797259` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900573792638750730` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900573174050201691` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900573039392096256` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900572889282138123` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900572627754692648` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900572504890957944` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900571592449486858` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900571334625607760` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900571031750738010` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900570670579204186` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900570658537361438` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900569819433279529` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900569805470461993` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900568818118721636` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900568734299721748` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900568733574127636` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900568640066322502` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900568483018989568` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900568442816577546` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900568404967161967` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900567723807997984` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900567498380943430` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900567419364446268` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900567399496044555` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900566407736082472` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900566307064393738` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900564043755061288` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900560162379661342` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900546879241220177` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900546857674080257` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900546335017697360` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900546077642592307` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900545948940386374` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900545317538254869` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900545289054715934` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900545273401589811` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900545237817114714` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900544794877632543` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900544745200308274` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900543728438116474` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900543727947374672` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900543725355274280` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900543695789654098` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900543652932223047` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900543422451044382` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900543186420772944` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900542657384837120` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900542642276937739` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900542087597027369` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900541801214128138` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900541636218605568` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900541495336120330` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900540671105056778` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900540418347921548` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900540349792018472` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900540030378991667` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900539890058526760` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900539409559085056` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900535419769335860` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900535281718030376` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900534206524956672` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900532479885205508` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900532411660644385` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900532388134780998` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900532328340803625` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900531904980348999` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900531845509292042` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900531738961412157` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900531697920131083` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900531522329772115` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900531454583390249` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900531452008099880` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900530840499527691` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900530832782020648` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900530674015010816` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900530008144085032` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900529896412053515` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900529598486437918` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900529581734375504` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900529258303197214` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900529067881816125` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900529003541192756` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900528812020863028` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900528751778091020` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900528684249788416` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900528402547765331` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900528216387751937` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900528048112271371` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900527972497375293` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900527840670396467` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900527762366926868` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900527708688252968` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900527613708206131` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900513279921754123` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900512795261554698` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900511257197686844` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900511191200317470` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900565005647364178` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900564776906801182` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900564551542657025` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900564249418547210` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900563101777276979` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900563076825366539` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900563060492759050` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900563044676030584` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900562924345647124` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900562265869258786` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900561988881620992` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900561834355097660` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900561819893108809` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900561036988534834` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900560927106170910` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900560925931749396` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900560918377799700` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900560891462971392` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900560720901591050` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900560710931714120` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900560147519270962` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900559595943133205` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900557490691928094` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900557457242349620` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900557340842012722` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900554367365681204` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900553682146455632` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900553402784813116` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900553335483027467` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900552456625328159` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900552446290558979` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900552181864869980` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900552154077593640` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900551859167723600` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900551831221059646` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900551426944679967` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900551175097683978` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900551079517884486` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900550723304054885` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900550585454039071` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900549968576794634` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900549554158583930` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900549476652036097` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900549132857532436` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900549117909016597` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900549088544694302` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900549077912145920` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900549014599110676` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900548776597524501` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900548495142969375` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900548307212984450` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900547953041743872` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900547185920323604` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900547013119201360` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900546923507904523` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900546923075866674` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900546887847923802` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900545852643348480` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900527845149929552` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900527649796001823` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900527578534785074` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900527120533573692` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900527009493549128` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900526519162638367` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900526399914393641` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900526292695416833` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900526273053458442` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900526068702793749` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900526015384789044` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900526010284531794` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900525971009077348` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900525839182090260` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900525751122673734` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900525444821045268` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900525433894879302` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900525379708674119` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900524865713500210` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900524669373919272` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900524345640747050` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900524063968071750` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900523789425717340` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900523312965369876` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900523245986512916` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900523226638200895` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900523126008451092` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900522835456438342` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900522739130064956` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900522537518247986` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900522309373280316` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900522094327103518` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900521915456823357` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900521863321649163` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900521611961172008` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900521568881496065` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900521434043007026` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900521285522694165` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900521175954915369` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900520749540970579` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900520651729829978` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900520550458327071` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900520475317370910` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900520204302434365` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900520146383274026` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900520145083047966` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900520007719596052` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900519989457608715` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900519663044292618` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900518877073645598` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900518538220011523` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900518377032917032` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900518179791585320` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900518162586533969` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900518087923761232` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900518052054053016` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900518007573446656` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900517861292900413` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900517680145113090` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900517656308903956` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900517084621078579` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900516821168447491` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `900515766338727986` | 10/31/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `744588224709525596` | 10/27/2021 | Phishing bot ('mar#6000') distributing deceptive credential-harvesting link 'dliscord.com'. |
| `673776952578146315` | 10/26/2021 | Phishing bot ('! SSKATE ✅#0801') distributing deceptive credential-harvesting link 'dliscord.com'. |
| `541000922948698123` | 10/26/2021 | Phishing bot ('Mikey_#1000') distributing deceptive credential-harvesting link 'dliscord.com'. |
| `734200179108085780` | 10/26/2021 | Phishing bot ('nguyenhai#2732') distributing deceptive credential-harvesting link 'dliscord.com'. |
| `680518638180106323` | 10/26/2021 | Phishing bot ('th#4077') distributing deceptive credential-harvesting link 'dissord.gift'. |
| `618432602902102050` | 10/26/2021 | Phishing bot ('Secre#0715') distributing deceptive credential-harvesting link 'dissord.gift'. |
| `396915319521673216` | 10/26/2021 | Phishing bot ('LT#7047') distributing deceptive credential-harvesting link 'discordj.gift'. |
| `604328440946098218` | 10/25/2021 | Phishing bot ('koushxk hehe#5241') distributing deceptive credential-harvesting link 'discordn.gift'. |
| `778686992736583711` | 10/25/2021 | Phishing bot ('Folofx#3323') distributing deceptive credential-harvesting link 'discocrd.gifts'. |
| `901381564582199327` | 10/24/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `697715742983847936` | 10/24/2021 | Phishing bot ('Раб-Сасори#4387') distributing deceptive credential-harvesting link 'discordhalloween.co.uk'. |
| `685599175735378140` | 10/21/2021 | Phishing bot ('im just a cow#3222') distributing deceptive credential-harvesting link 'discordi.gift'. |
| `735468372359249941` | 10/21/2021 | Phishing bot ('Razee#5299') distributing deceptive credential-harvesting link 'discordi.gift'. |
| `812046985090957324` | 10/19/2021 | Phishing bot ('gfx_joey#0906') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `649521226552836116` | 10/19/2021 | Phishing bot ('Adn#1593') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `581536983038296065` | 10/19/2021 | Phishing bot ('xx𝙻𝚞-𝙹𝚊𝚑xx#4455') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `788617971757088800` | 10/19/2021 | Phishing bot ('Shashak#8242') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `752871474834178150` | 10/19/2021 | Phishing bot ('ruhankabir9#1867') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `633670149022679060` | 10/18/2021 | Phishing bot ('ŞⓀɎツ#9557') distributing deceptive credential-harvesting link 'dlscord-app.net'. |
| `755943795857686559` | 10/18/2021 | Phishing bot ('BIG VOXI#3870') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `704445173484093491` | 10/18/2021 | Phishing bot ('Mikotsuki#3715') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `292998437820039169` | 10/18/2021 | Phishing bot ('ToxicDream#5958') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `583283547041693696` | 10/18/2021 | Phishing bot ('Mishter_PoPo#4223') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `714476327582826538` | 10/17/2021 | Phishing bot ('Jimp!x#5960') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `744088151634608249` | 10/17/2021 | Phishing bot ('HetchZeee#3060') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `700060753574494278` | 10/17/2021 | Phishing bot ('Claps#4646') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `404940397068943360` | 10/17/2021 | Phishing bot ('ninjascotsman#8427') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `546156744645017604` | 10/17/2021 | Phishing bot ('I_Am_A_Frog#3207') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `666291321853706252` | 10/17/2021 | Phishing bot ('ES ERAM ✓#9643') distributing deceptive credential-harvesting link 'stearncornminuty.com'. |
| `715254634377248829` | 10/16/2021 | Phishing bot ('zip#7655') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `722434874341851158` | 10/16/2021 | Phishing bot ('!-N o a h#0339') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `412111340904382485` | 10/16/2021 | Phishing bot ('V A  L I A N T#6671') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `531194895856041986` | 10/16/2021 | Phishing bot ('ALLØY#6807') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `731558262033612940` | 10/16/2021 | Phishing bot ('ChiklisZhathZ#5229') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `377124585394536448` | 10/16/2021 | Phishing bot ('Asura#6399') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `531934467917479967` | 10/16/2021 | Phishing bot ('nOpeOn#8974') distributing deceptive credential-harvesting link 'discordc.gift'. |
| `673783240355610634` | 10/14/2021 | Phishing bot ('ara~ara~~#3802') distributing deceptive credential-harvesting link 'discordrgift.com'. |
| `777929167932096533` | 10/13/2021 | Phishing bot ('Zayed#0804') distributing deceptive credential-harvesting link 'dlscord.net'. |
| `775210426123943946` | 10/13/2021 | Phishing bot ('THΞSCΛRLΞTX#0184') distributing deceptive credential-harvesting link 'discordrgift.com'. |
| `526357544868904961` | 10/13/2021 | Phishing bot ('elprofeso#9152') distributing deceptive credential-harvesting link 'discordsgift.com'. |
| `561219765331427328` | 10/13/2021 | Phishing bot ('Kammmh#6666') distributing deceptive credential-harvesting link 'dlscord.net'. |
| `662218980085334034` | 10/13/2021 | Phishing bot ('ㄒ卄乂ﾌ卂几#0742') distributing deceptive credential-harvesting link 'discordrgift.com'. |
| `771055869609639967` | 10/13/2021 | Phishing bot ('ohad 102#0954') distributing deceptive credential-harvesting link 'discordsgift.com'. |
| `193755122235473920` | 10/12/2021 | Phishing bot ('Skry#4055') distributing deceptive credential-harvesting link 'discordrgift.com'. |
| `350445427939606528` | 10/12/2021 | Phishing bot ('Not Monika#5911') distributing deceptive credential-harvesting link 'dlscord.net'. |
| `675978452322746399` | 10/11/2021 | Phishing bot ('S_harach#8035') distributing deceptive credential-harvesting link 'dlscord.net'. |
| `656794931502776320` | 10/10/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `722463352726749235` | 10/10/2021 | Phishing bot ('ачап#2159') distributing deceptive credential-harvesting link 'discordsgift.com'. |
| `513592852232667137` | 10/10/2021 | Phishing bot ('rexsaint#9080') distributing deceptive credential-harvesting link 'discordsgift.com'. |
| `359040840225652736` | 10/10/2021 | Phishing bot ('XapXeb#8297') distributing deceptive credential-harvesting link 'dlscord.net'. |
| `761966706364383242` | 10/10/2021 | Phishing bot ('NXoob#2674') distributing deceptive credential-harvesting link 'dlscord.net'. |
| `450686979399614464` | 10/10/2021 | Phishing bot ('Chamdutsu#2652') distributing deceptive credential-harvesting link 'dlscord.net'. |
| `743167282565611581` | 10/09/2021 | Phishing bot ('trix for kids#3204') distributing deceptive credential-harvesting link 'dlscord.net'. |
| `728004869977538653` | 10/09/2021 | Phishing bot ('WALED ZAYED#9502') distributing deceptive credential-harvesting link 'dlscord.app'. |
| `660824329637855242` | 10/07/2021 | Phishing bot ('Lado direito do pescoço#6790') distributing deceptive credential-harvesting link 'dlscord.org'. |
| `728495055194685541` | 10/07/2021 | Phishing bot ('Franklin Clinton#1835') distributing deceptive credential-harvesting link 'dlscord.org'. |
| `682984813036306512` | 10/06/2021 | Phishing bot ('𝙈𝙀 \| PotatoXD ♪#9073') distributing deceptive credential-harvesting link 'dlscord.org'. |
| `756806522473807902` | 10/06/2021 | Phishing bot ('Hecker#2845') distributing deceptive credential-harvesting link 'discorcl-app.com'. |
| `747693489373839380` | 10/05/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `810541875362136094` | 10/05/2021 | Phishing bot ('nathan1x#8224') distributing deceptive credential-harvesting link 'discordglfts.com'. |
| `545311419781087272` | 10/05/2021 | Phishing bot ('NOT_Dudelord#6885') distributing deceptive credential-harvesting link 'discords-gift.com'. |
| `592506469212225566` | 10/05/2021 | Phishing bot ('🎃 TheRealF3AR 🎃#0001') distributing deceptive credential-harvesting link 'discordsteams.com'. |
| `776592499485311006` | 10/05/2021 | Phishing bot ('Yousef, anarchyson#7729') distributing deceptive credential-harvesting link 'dlscord.org'. |
| `663153679184166932` | 10/04/2021 | Phishing bot ('elo#0002') distributing deceptive credential-harvesting link 'dlscord.org'. |
| `751367218771787786` | 10/04/2021 | Phishing bot ('[Blubloxbeam]#7739') distributing deceptive credential-harvesting link 'dlscord.org'. |
| `876735916033601586` | 10/04/2021 | Phishing bot ('🎃 Spookura (さくら) 🎃#9112') distributing deceptive credential-harvesting link 'dlscord.org'. |
| `845294061720043581` | 10/04/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `638752729530892318` | 10/04/2021 | Phishing bot ('! 彡Ⱬ!ƝӾ彡◥⏦◤#2125') distributing deceptive credential-harvesting link 'dlscord-app.info'. |
| `471145904234299402` | 10/04/2021 | Phishing bot ('Shirou#7152') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `850126392053465139` | 10/04/2021 | Phishing bot ('CloneLocker#4583') distributing deceptive credential-harvesting link 'dlscord-app.info'. |
| `840867137571782656` | 10/04/2021 | Phishing bot ('DazedRhino9462#0819') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `820361106002149386` | 10/04/2021 | Phishing bot ('FlyTech9019#1495') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `599135121567776778` | 10/03/2021 | Phishing bot ('LinusTHD#0001') distributing deceptive credential-harvesting link 'dlscord.org'. |
| `647738765909032960` | 10/03/2021 | Phishing bot ('blazer4272#9408') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `694523208405090365` | 10/03/2021 | Phishing bot ('Ðᗩℝ₭_𝙎฿.₳#5512') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `519238161956601856` | 10/03/2021 | Phishing bot ('marti500#2930') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `309387367431536641` | 10/03/2021 | Phishing bot ('Jiro#7609') distributing deceptive credential-harvesting link 'dlscord.org'. |
| `371702534244532225` | 10/02/2021 | Phishing bot ('Hercules#7222') distributing deceptive credential-harvesting link 'discord-cpp.com'. |
| `760532125719593030` | 10/01/2021 | Phishing bot ('ϟPhⱥnτo𝓶Niͥnjͣaͫᴳᵒᵈツϟ \| 夜#3797') distributing deceptive credential-harvesting link 'discords-gift.com'. |
| `536685529580961794` | 10/01/2021 | Phishing bot ('Thomas57#1600') distributing deceptive credential-harvesting link 'dlscord.org'. |
| `479938202698776595` | 09/29/2021 | Phishing bot ('☭RTX Arthur aka Heisenberg☭#0799') distributing deceptive credential-harvesting link 'discocrd.gift'. |
| `892453199481540618` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892452751349522482` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892452633460215858` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892451562574733343` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892450058082091048` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892449483730849843` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892448443048542278` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892448129624977428` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892446668568530955` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892445722329354240` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892445559577772123` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892444191869771826` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892444145606610955` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892441460388032572` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892440050023944254` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892431242337853480` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892332990548566037` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892330670964240405` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `892327875989102602` | 09/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `423531605626322945` | 09/25/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `523031939859480582` | 09/25/2021 | Phishing bot ('S_oneGaming#0284') distributing deceptive credential-harvesting link 'discord-app.net'. |
| `612602866603130900` | 09/25/2021 | Phishing bot ('MrFrostOp#6098') distributing deceptive credential-harvesting link 'discord-give.com'. |
| `225369823310249984` | 09/25/2021 | Phishing bot ('EchoZoMbiie#4212') distributing deceptive credential-harvesting link 'discord-give.com'. |
| `858044276521041930` | 09/25/2021 | Phishing bot ('xalzezap#4848') distributing deceptive credential-harvesting link 'discord-app.net'. |
| `447360424334196748` | 09/23/2021 | Phishing bot ('Nhan#8823') distributing deceptive credential-harvesting link 'discord-give.com'. |
| `755545481630843011` | 09/23/2021 | Phishing bot ('leonsx#4830') distributing deceptive credential-harvesting link 'discord-give.com'. |
| `719921549217366046` | 09/23/2021 | Phishing bot ('Tzuao#4919') distributing deceptive credential-harvesting link 'discord-app.net'. |
| `888183428967710732` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888155446739873793` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888155199192064030` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888154287421677668` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888153873020231710` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888150556751839253` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888148410119630910` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888148317949800509` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888147954190401639` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888145909119066173` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888143070351212575` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888140209353527326` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888132841353904129` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888132292877369344` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888132172739911692` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888131608606035968` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888129613618905108` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888121838910197801` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888121062670336040` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888118780557950999` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888117405182742639` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888116723352489985` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888115636004327465` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888111514421182526` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888109975442952203` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888106755756818482` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888104843544236072` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888086676717584425` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888086376573202432` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888082761846497392` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888078942668468255` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888078690641129483` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888076232271470694` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888075791592738877` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888075547886895114` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888075358946074694` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888074699995770971` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888072092279533658` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888069265947766785` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888068535497134161` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888064395035422730` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888062935853838347` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888062833995165706` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888062429962051695` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888061561346863125` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888060822813823006` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `888057482990194688` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885692685443268619` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885691925695430706` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885689195929169970` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885688157658546187` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885688133633572904` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885687740086227005` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885686617350766652` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885563418197758042` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885563163108593684` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885562893586817034` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885561028711174215` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885560703220600893` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885560414849597550` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885560395807485952` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885559650509008906` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885558947015192637` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885558711127527424` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885558588913897512` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885558550301147186` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885558189767135242` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885557251300012093` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885556848193835089` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885556311054487662` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885555675600670760` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885554559894822923` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885554099368656957` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885554099129581579` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885552999689228368` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885552720050790432` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885540633509494845` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885539736272371722` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885537128807821404` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885526852343562240` | 09/22/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `540163885819363328` | 09/21/2021 | Phishing bot ('sakaminto#0582') distributing deceptive credential-harvesting link 'steam-discords.com'. |
| `879195277607702598` | 09/21/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `467534121347055617` | 09/20/2021 | Phishing bot ('jewls#9945') distributing deceptive credential-harvesting link 'discord-give.com'. |
| `887901402540687412` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887901300501671967` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887900984184012880` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887900686799470593` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887900618402955296` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887900374432903239` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887900315502915584` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887900191225684040` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887899821762027581` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887899623627309136` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887899525690318898` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887899293321666560` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887899108944261202` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887899103877546035` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887898536979628044` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887898500950548590` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887898418452791387` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887898380007800884` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887898253159440384` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887898207626092614` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887898180295983125` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887898017208889385` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887897976696098840` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887897946509672468` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887897786392125520` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887897712492683314` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887897444615069717` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887897439984562217` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887897238741852170` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887897159259787294` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887897007883190302` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887896903902171167` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887896842812153916` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887896810239184936` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887896690479235124` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887896570283061318` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887896398002020353` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887896344029704232` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887895852935426098` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887895813563510815` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887895697100267521` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887895628573704224` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887895585225576528` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887895342127931392` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887895231666733088` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887895207868243979` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887895149538062357` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887894611060736010` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887894556216008735` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887894488574459904` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887894458652327988` | 09/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `770645725011902474` | 09/18/2021 | Phishing bot ('Mizuki#4522') distributing deceptive credential-harvesting link 'steamdiscord.com'. |
| `763743239148011570` | 09/17/2021 | Phishing bot ('DeathTheGrim#2636') distributing deceptive credential-harvesting link 'discord-app.net'. |
| `728507245612105791` | 09/17/2021 | Phishing bot ('BlaZe#2459') distributing deceptive credential-harvesting link 'discord-give.com'. |
| `885986578609094677` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885986537198727178` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885986254448107640` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885986185816727563` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885986092707360809` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885985557954560072` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885985399938363432` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885984940385267733` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885984856994099250` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885984544258420736` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885984461378945045` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885984255145033829` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885984194495410218` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885983755276263475` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885983578733826050` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885982472196747334` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885981763917209600` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885973120589127730` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885972353820024894` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885972348229009408` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885972113201188864` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885972015981412374` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885971246997725205` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885970903605841980` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885970653717610507` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885970153664290866` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885970104930680903` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885970076577202226` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885970071678251048` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885969787652554803` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885969547918704640` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885969150617464873` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885968976054730752` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885968683556556881` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885968225811173448` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885968118562820126` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885966772895887391` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885966728276893756` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885966709620617226` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885966649231048726` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885966596563144785` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885966306464120954` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885965921225695312` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885965603783987202` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885965583315763201` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885965307477393440` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885965192368910356` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885964922427695114` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885964814847995944` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885964166446350418` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885964086762934303` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885963966839418980` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885963815706062889` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885963713193062421` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885963682620772422` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885962915348381756` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885962891180789850` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885962719075921940` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885962599513088060` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885962575890743296` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885962467509927937` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885962282008449096` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885962096498573315` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885962094749560864` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885961790444408892` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885961631891329034` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885960524632821761` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885960435851984906` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885959142529974282` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885958967606526002` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885958785087209534` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885958464478785637` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885958010617360474` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885957937498062910` | 09/17/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `676874994378342400` | 09/16/2021 | Phishing bot ('!            Sριȥҽʅ#2665') distributing deceptive credential-harvesting link 'stemcoominuty-alirdrop.xyz'. |
| `885998954070831125` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885998945954857011` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885998939021647923` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885998848856715304` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885998722981437451` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885998644749283370` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885998420999958589` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885997851937747024` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885997608387092550` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885997549218062336` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885997224717344829` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885997030298755114` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885996914070413414` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885996733115551786` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885996579826335794` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885996545747603467` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885996519927476234` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885995607666331719` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885995563726798899` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885995437662830672` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885995417395953665` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885995212671963216` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885995123459100683` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885994925076918272` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885994678275694663` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885994671472541756` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885994600878207006` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885994498071592962` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885994423329103922` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885994300851245098` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885993777796382740` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885993567464599634` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885993545343860797` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885993477828149268` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885992901576896542` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885992858409115668` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885992688808247306` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885992671724830760` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885992369214857288` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885992147059355728` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885991958181449788` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885991653142327327` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885991572657831946` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885991333263724555` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885990998314991626` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885990970225737728` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885990583699660800` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885990475025231942` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885990421195538493` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885989791546613802` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885989272174354553` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885989245267902494` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885989128058044517` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885988789015695381` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885988135706722335` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885987883499020359` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885987727332507708` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885987681732026398` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885987651382018098` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885987357151612929` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885987286817333279` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885934036151849082` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885933316136632320` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885933120824680448` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885932780897308723` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885932184169484288` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885931991034388480` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885931592747466782` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885931526628458537` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885931349855305728` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885931261951082546` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885931134238748803` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885931083181481994` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885930846861815849` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885930504275259453` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885930322330550372` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885930193997422602` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885930029060587541` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885929980352143470` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885929873623900220` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885929116543623248` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885929021106450452` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885928917146415115` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885928772195471360` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885928485741281310` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885928367206039563` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885928271928238140` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885928008987328542` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885928005287940156` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885927896466731008` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885927798173220905` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885927660440670289` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885927413433892904` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885927253505110078` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885927166464917525` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885926887975694396` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885926454171435018` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885926426249924638` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885926146464686100` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885926049811144744` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885926023017951242` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885925841417158657` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885925727126564864` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885925332933296148` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885924940937838643` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885924717905723402` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885924613668892682` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885924456546054255` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885924279038918656` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885924215918829630` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885924174047100999` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885923980601589802` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885923834295881768` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885923680952135721` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885923652145676288` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885923342870253612` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885923150502719499` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885922999344189501` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885922639946850384` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885921319928082443` | 09/16/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885994710521495632` | 09/16/2021 | Malicious scam account flagged and reported by community moderation. |
| `552524626639585280` | 09/16/2021 | Phishing bot ('Jason Miller#1657') distributing deceptive credential-harvesting link 'discord-app.net'. |
| `886974365890134077` | 09/16/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `747316102064898058` | 09/16/2021 | Phishing bot ('UwU Chan#1848') distributing deceptive credential-harvesting link 'discord-app.net'. |
| `843167807210258512` | 09/15/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `402047970733719552` | 09/15/2021 | Phishing bot ('Mundo#7809') distributing deceptive credential-harvesting link 'steamdlscord.com'. |
| `887003769567580160` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887003727691677759` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887003727037333514` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887003721148555304` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887003720892702784` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887003701972177058` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887003691507408946` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887003688093253722` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887003684263841812` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887003673895514122` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887003664324116541` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210962217107478` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210885985652757` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210853928574976` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210786408685588` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210750631276585` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210733107478588` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210730729275392` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210708457541652` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210700979081226` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210696734462002` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210670159335424` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210648860684298` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210648244117514` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210610348584990` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210599271424012` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210595332952104` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210564836179998` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210529570455562` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210518640107530` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886210496800358420` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886202131965693952` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886202063313313802` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886202041251270686` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886202023358382091` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886202013086531604` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886202007076110347` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886202004265918485` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886201970036195348` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886201898787569684` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `886201879271460924` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885822280574308362` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `885821898603257866` | 09/15/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `887491471828209684` | 09/15/2021 | Compromised account immediately distributing spam upon entering server channels. |
| `555632220660957215` | 09/14/2021 | Phishing bot ('HowUDoin#9144') distributing deceptive credential-harvesting link 'discord-app.net'. |
| `746961118827774003` | 09/14/2021 | Phishing bot ('x_idris_z_x#4265') distributing deceptive credential-harvesting link 'discord-app.net'. |
| `571414844834578433` | 09/13/2021 | Malicious scam account flagged and reported by community moderation. |
| `515444118143500291` | 09/11/2021 | Malicious scam account flagged and reported by community moderation. |
| `488391020384485411` | 09/11/2021 | Phishing bot ('TeleWorldTV#0104') distributing deceptive credential-harvesting link 'discordapp.click'. |
| `885673434204487680` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885672900957454336` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885672817260118056` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885672439978291200` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885672171697999903` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885672126613442570` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885671083691356261` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885670959795798026` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885670567087329310` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885670566248456252` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885670367438454795` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885670264967421963` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885669718747381770` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885668705168654376` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885668698441019472` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885668044939075664` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885555775920021514` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885554966083797012` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885552334330019840` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885546079620308994` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `885536015127830538` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `162977038481752064` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `407633511009484800` | 09/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `692718087769817099` | 09/09/2021 | Phishing bot ('𝔸𝕝𝕡𝕙𝕒_𝟘𝟙#1924') distributing deceptive credential-harvesting link 'dlscord-nitro.click'. |
| `676171622578913353` | 09/08/2021 | Phishing bot ('xedow#7777') distributing deceptive credential-harvesting link 'dlscord-app.com'. |
| `324676185395298307` | 09/07/2021 | Phishing bot ('shadowg#6915') distributing deceptive credential-harvesting link 'dlscord-app.com'. |
| `760434619140538409` | 09/06/2021 | Phishing bot ('Leacy José#1202') distributing deceptive credential-harvesting link 'dlscord-nitro.click'. |
| `596618326634004492` | 09/06/2021 | Phishing bot ('Jihan#0685') distributing deceptive credential-harvesting link 'dlscord-nitro.click'. |
| `755640728587206727` | 09/06/2021 | Phishing bot ('Myko卍#0013') distributing deceptive credential-harvesting link 'dlscord-nitro.click'. |
| `112576636737634304` | 09/06/2021 | Malicious scam account flagged and reported by community moderation. |
| `884263112952401940` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884260460986265642` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884257265857728514` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884255755778293832` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884255353250922536` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884255210040606780` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884254280440221696` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884254204175200256` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884252657466888243` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884251856124133396` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884251104781688862` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884250519684665455` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884249422190493716` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884249149569110137` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884247723459625021` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `884245880255942697` | 09/06/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `518386245978816513` | 09/06/2021 | Malicious scam account flagged and reported by community moderation. |
| `547192520480915456` | 09/05/2021 | Phishing bot ('CC#1111') distributing deceptive credential-harvesting link 'dlscord-nitro.link'. |
| `603836353460830219` | 09/05/2021 | Malicious scam account flagged and reported by community moderation. |
| `523601958674759814` | 09/04/2021 | Phishing bot ('Sanjay4512#9083') distributing deceptive credential-harvesting link 'discord-claim.com'. |
| `783663724850184232` | 09/04/2021 | Phishing bot ('Javierr#0001') distributing deceptive credential-harvesting link 'discord-claim.com'. |
| `567122168975196170` | 09/04/2021 | Phishing bot ('BearPawMEMES#4536') distributing deceptive credential-harvesting link 'discord-airdrop.com'. |
| `717427483900903476` | 09/03/2021 | Phishing bot ('!tom#0013') distributing deceptive credential-harvesting link 'dlscord-nitro.link'. |
| `587071782180093974` | 09/03/2021 | Phishing bot ('Runichi#1013') distributing deceptive credential-harvesting link 'dlscord-nitro.link'. |
| `882486757487153203` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `882485814842503188` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `882332806422863972` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `882148582352912404` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `881779005328601088` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `881597495443079219` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `881581200450400336` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `880983942235299901` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `880879187680968765` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `880444133863456828` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `879859103462223914` | 09/01/2021 | Identified ban evasion alt account linked to previously banned user. |
| `251114779828158474` | 08/31/2021 | Phishing bot ('Mob#4021') distributing deceptive credential-harvesting link 'steamcomminuty.com'. |
| `624565220790108170` | 08/31/2021 | Phishing bot ('yosshipaopao#8080') distributing deceptive credential-harvesting link 'steamcomminuty.com'. |
| `640617336008736828` | 08/31/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `627002920063336470` | 08/31/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `607274977670070293` | 08/31/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `881156295326068806` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881156240095465494` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881155961274916934` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881155232430694431` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881155139170353203` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881154866129547265` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881154846475034685` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881154600634318858` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881154594271531128` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881154580531003413` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881154351794647051` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881152712526401616` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881152466886987788` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881151257216155698` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881151065096073236` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881151025736716289` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881150891930042388` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881150874385281024` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `881150358511054858` | 08/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `352763995415117824` | 08/29/2021 | Malicious scam account flagged and reported by community moderation. |
| `710115630103396362` | 08/29/2021 | Phishing bot ('藤原#4058') distributing deceptive credential-harvesting link 'gave-nitro.com'. |
| `860518867964264448` | 08/29/2021 | Malicious scam account flagged and reported by community moderation. |
| `653933892847534090` | 08/29/2021 | Phishing bot ('melody#0100') distributing deceptive credential-harvesting link 'discord-nltro.com'. |
| `722555032389681251` | 08/26/2021 | Phishing bot ('SmL#1234') distributing deceptive credential-harvesting link 'discorcl.click'. |
| `531775499958222848` | 08/26/2021 | Phishing bot ('Micki mouse🤡#8825') distributing deceptive credential-harvesting link 'discorcl.click'. |
| `235121485826490370` | 08/25/2021 | Phishing bot ('_Adrian_#2676') distributing deceptive credential-harvesting link 'discorcl.click'. |
| `628617020266512403` | 08/24/2021 | Malicious scam account flagged and reported by community moderation. |
| `879235003119185940` | 08/23/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `879232564265623554` | 08/23/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `749894357343141949` | 08/21/2021 | Malicious scam account flagged and reported by community moderation. |
| `497094505439166465` | 08/21/2021 | Malicious scam account flagged and reported by community moderation. |
| `758665683256737832` | 08/19/2021 | Phishing bot ('Parzival#5199') distributing deceptive credential-harvesting link 'steancommunity.link'. |
| `532925932537905152` | 08/17/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `637956592750428195` | 08/17/2021 | Malicious scam account flagged and reported by community moderation. |
| `657347382693986334` | 08/17/2021 | Phishing bot ('PravVFX#4334') distributing deceptive credential-harvesting link 'steancommunity.link'. |
| `289901443060596737` | 08/17/2021 | Phishing bot ('tours#3944') distributing deceptive credential-harvesting link 'steancommunity.link'. |
| `231445754844020736` | 08/14/2021 | Malicious scam account flagged and reported by community moderation. |
| `785198049420771360` | 08/13/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `819806534644269058` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `763070786868477983` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `744599693580828863` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `696524752923394109` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `694996612375904326` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `652719385223626765` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `634941051454619650` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `617612514418753558` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `613061115575926800` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `594161342018093066` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `583259951343075348` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `534379848148320258` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `524965497444368384` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `516588567674355733` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `497204328117960715` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `474003259447705600` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `442066890714775553` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `435541252264689685` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `432249626553221124` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `424399386513244160` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `422195426733850646` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `409186275304931339` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `400777910560096269` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `395035833414975508` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `392111432948252673` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `390828590649835522` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `388883401396060170` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `377823765410611210` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `349693677142016012` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `343100982730817536` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `306242395048116224` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `303336563830685697` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `264485125939527680` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `247378198445162496` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `178687735312154635` | 08/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `874952940236988456` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874952149069602817` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874951383512662036` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874950706644279306` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874950473289981963` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874950468701405194` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874950344604532757` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874950084041797642` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874949846958743604` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874948019752157204` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874947966824226836` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874947536052445205` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874945510744686612` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874945386916229150` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874945173606522921` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874945143877271612` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874945093168168980` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874943956599832606` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874943870457237504` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874943697010196510` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874943605641453589` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874943498124681226` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874935651898908702` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874934999051288606` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874934903647666186` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874934743584628766` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874934575011332106` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874934471474962463` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `874933537436999680` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `720018198719758366` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `610239809587511306` | 08/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `875324882429313026` | 08/12/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `806803892825882656` | 08/10/2021 | Malicious scam account flagged and reported by community moderation. |
| `204315622237143049` | 08/10/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `855340842189062174` | 08/09/2021 | Phishing bot ('chalupo#2222') distributing deceptive credential-harvesting link 'discorcl.link'. |
| `466228788121042947` | 08/09/2021 | Phishing bot ('Dowiny#8467') distributing deceptive credential-harvesting link 'discorcl.link'. |
| `633615596579323904` | 08/09/2021 | Phishing bot ('Aldo#2865') distributing deceptive credential-harvesting link 'giftsdiscord.ru'. |
| `366275019984076802` | 08/08/2021 | Malicious scam account flagged and reported by community moderation. |
| `505295914030596096` | 08/08/2021 | Malicious scam account flagged and reported by community moderation. |
| `337483349289467904` | 08/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `723177589572763721` | 08/07/2021 | Phishing bot ('WINDOWS SAM.X70#8306') distributing deceptive credential-harvesting link 'giftsdiscord.ru'. |
| `536943150590197771` | 08/06/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `792363423484215327` | 08/06/2021 | Malicious scam account flagged and reported by community moderation. |
| `440509219175923733` | 08/06/2021 | Malicious scam account flagged and reported by community moderation. |
| `485717624827805707` | 08/05/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `790358425749684224` | 08/04/2021 | Malicious scam account flagged and reported by community moderation. |
| `531386755836936193` | 08/03/2021 | Phishing bot ('CazyFPS#0001') distributing deceptive credential-harvesting link 'steamcommunyty.com'. |
| `279515527351631872` | 08/03/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `871132131567468544` | 08/03/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `747696621487259709` | 08/02/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `480898037842182161` | 08/01/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `857564046160953344` | 07/31/2021 | Phishing bot ('party#6506') distributing deceptive credential-harvesting link 'steancomnunytu.ru'. |
| `870249649523539968` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869981973123309588` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869976138896785429` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869970570714955807` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869954414310477865` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869947614509039646` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869935960694067330` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869931520796790826` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869927596635328582` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869921273248092190` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869920102919860224` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869918042975514654` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869906158431928320` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869894519657738280` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869884356045443102` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869844012465549353` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869840651620085822` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869839997858111509` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869835477149167646` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869817491445133332` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869807853240733727` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869684630616432731` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869684356929683506` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869683528877629471` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869678638763749426` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869664229064581121` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869648408376393758` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869613378761555989` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869596803400597534` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869582738137702411` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `869577963874701362` | 07/29/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `454896210877218816` | 07/28/2021 | Phishing bot ('Tiara#0485') distributing deceptive credential-harvesting link 'steamcomminutiu.ru'. |
| `865645902580547585` | 07/28/2021 | Malicious account distributing cryptocurrency phishing scams. |
| `593157813799485452` | 07/27/2021 | Phishing bot ('SH1FT-EL1TE#5374') distributing deceptive credential-harvesting link 'steamcomminutiy.ru'. |
| `801314359732469772` | 07/26/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `459010152054390784` | 07/26/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `868263927488839771` | 07/26/2021 | Malicious account distributing cryptocurrency phishing scams. |
| `753288033935294474` | 07/24/2021 | Phishing bot ('marcopandolfi#4142') distributing deceptive credential-harvesting link 'steamcomminytiu.ru'. |
| `483000642487713793` | 07/22/2021 | Phishing bot ('Nerds#1929') distributing deceptive credential-harvesting link 'steancommunytiu.ru'. |
| `685252130650456067` | 07/22/2021 | Phishing bot ('guata#9434') distributing deceptive credential-harvesting link 'steancommunytiu.ru'. |
| `336619891077545985` | 07/22/2021 | Phishing bot ('Alex UwU#8423') distributing deceptive credential-harvesting link 'stearncommunytiy.ru'. |
| `187648739974971392` | 07/22/2021 | Phishing bot ('KingFuze#6319') distributing deceptive credential-harvesting link 'steamcomminytiu.ru'. |
| `524523180371607552` | 07/21/2021 | Phishing bot ('Im_Mart1m#2398') distributing deceptive credential-harvesting link 'steancommunytiu.ru'. |
| `507558902808707084` | 07/21/2021 | Phishing bot ('☭phil7927☭#0001') distributing deceptive credential-harvesting link 'stearncommunytiy.ru'. |
| `665193392518725652` | 07/21/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `855074567797604383` | 07/18/2021 | Malicious scam account flagged and reported by community moderation. |
| `809465248754040882` | 07/18/2021 | Malicious scam account flagged and reported by community moderation. |
| `766688668165210113` | 07/18/2021 | Phishing bot ('Parham#1441') distributing deceptive credential-harvesting link 'steamcomminytiu.com'. |
| `282071609723060225` | 07/17/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `512221357736591361` | 07/16/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `657028768233291807` | 07/16/2021 | Malicious scam account flagged and reported by community moderation. |
| `864944168605319195` | 07/15/2021 | Malicious account distributing cryptocurrency phishing scams. |
| `596672587371905034` | 07/15/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `724268795463729182` | 07/14/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `723548687711862795` | 07/14/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `428925301867937794` | 07/14/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `426331679838175233` | 07/14/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `399334419305070592` | 07/14/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `341507804630220810` | 07/14/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `558679309213237278` | 07/14/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `864580164859723787` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864579981673889873` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864579796289847316` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864579746922889238` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864579725958316073` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864579719830962196` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864579228528017459` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864579145400057857` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864579053351600158` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864578905359646731` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864578695603290122` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864578643623542784` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864578397938122764` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864578026149642240` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864577966150647868` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864577723489189948` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864577653503557712` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864577146579058708` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864577111099441182` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864577035497504778` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864576302053195796` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864576257387790377` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864576153971589120` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864576016386228244` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864575895833804832` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864575589923160144` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864575569533075476` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864575530292346880` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864575527615463455` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864575035577597952` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864574599937261604` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864574477803454494` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864574169747423232` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864574032442556448` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864573951702990868` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864573943088021534` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864573812652769291` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864573750410346526` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864573738145677374` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864573473775288320` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864573447983333417` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864573399820795924` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864573368878891018` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864573264445440060` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864572743865729075` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864572725262417931` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864572670204313681` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864572531751387177` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864572064844873748` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864571800776474625` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864571777924333668` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864567647147130890` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864567483112882196` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864567454742609941` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864567242648846356` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864567174517882901` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566897836294154` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566886117408778` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566878578671676` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566785200881669` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566608415555615` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566427931639818` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566342107791370` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566229188608060` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566228760789023` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566193042096149` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566184308113469` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566090167222362` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566043791196220` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864566020454219806` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565867274305576` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565830495109120` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565801936093194` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565707814600735` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565555822723072` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565427627622410` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565355032739843` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565323029938237` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565283476733952` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565249012269076` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565152171294731` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864565047975870485` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864545789552623646` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864624741104222208` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864624498028445717` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864624468043366422` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864624317437181993` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864624257812529152` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864624181113913355` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864623785059549196` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864623715361751050` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864623576048730142` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864623488122617876` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864623419743535134` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864623414308241418` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864623136305184779` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864623116918718475` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864623037189718017` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622932688109660` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622609852399648` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622520644927509` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622469037293569` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622458689683486` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622365681647616` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622345486467092` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622284856623125` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622245120704522` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622177915895858` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864622025985228860` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864621468851241001` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864621458286182411` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864621304313413703` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864620930268659732` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864620880810082324` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864620666631618590` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864620631722819641` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864620621966475284` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864620363601281094` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864620315312390154` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864620235679072268` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864620054083010561` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864619960433246298` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864619951703982130` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864619751060668446` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864619744614678528` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864619311749529601` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864619294457462795` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864619237381111818` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864618978584035339` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864618902909878293` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864618854130253834` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864618798904639499` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864618770417188895` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864618624379387946` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864618548104790036` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864618359383392257` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864618296082300968` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864617864958836776` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864617586829164584` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864617562201522187` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864617419540660256` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864616959483838464` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864616756110163968` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864616511754600458` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864616255034097695` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864616249933692949` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864616116303429662` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864615900187197510` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864615748776624149` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864615612043231273` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864615422560043009` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864615337177776140` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864615050802233351` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864614979839590420` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864614773139963945` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864614506855792700` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606763704385566` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606746294485002` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606729282256897` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606583249829888` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606579902644265` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606524226666506` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606484066598952` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606362700349440` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606311048019969` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606273395752991` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606133712060417` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864606113511899256` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605991072825404` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605852530769920` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605843940311080` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605758908530730` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605748679933962` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605703205552159` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605631934365736` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605621734211645` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605450031988736` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605397888663572` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605324887326720` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864605176324685844` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864604996397826089` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864604934532235284` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864604795401404456` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864604789496741925` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864604385774534686` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864604327725498398` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864604256661536799` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864604219843805196` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864602873500532821` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864602801400971265` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864602713080987648` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864602695981072394` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864602447066824735` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864602252747866182` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864602168592695316` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864602120850374666` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864601974413721600` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864601969653317642` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864601565612474368` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864601457659740191` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864601392361897984` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864601041923342379` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864601029316051006` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864600978305187861` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864600944220831744` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864600936529788939` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864600869789499423` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864600056589189130` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864599769938657320` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864599697192255518` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864599497107701780` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864599430975193108` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864599375942385685` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864599366417252442` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864599138654093313` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864599067442282517` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864598648397365288` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864598455132487682` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864598166703570955` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864598154556080128` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864597875043074098` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864597720517312542` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864597543530921994` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864597310193270854` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864597144748818435` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864596708680138822` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864596371273154660` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864596297885286410` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864596089206472734` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864595966296195092` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864595934998691881` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864595879658651679` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864595876739285013` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864576505395806209` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864380867618930688` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864662812730589204` | 07/13/2021 | Malicious scam account flagged and reported by community moderation. |
| `864429153104429056` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864429097974497280` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428977917919242` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428922464501780` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428885861203978` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428792793661450` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428662932635668` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428661927444510` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428660714766337` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428618784571392` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428594133860373` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428579394813982` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428541910450206` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428494901477417` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428289812987904` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428269608632330` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864428144240230401` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427984961929237` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427948433473567` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427903885115433` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427874786344971` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427870859296769` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427868109275147` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427776298713088` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427664042622996` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427620430905344` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427511408885810` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427472732422154` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427424447856640` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427398715670558` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427396958519307` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427342918844416` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427137906114581` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427132850929666` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427080728444948` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864427048658796554` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864426810779631637` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864426786183446530` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864426775643815966` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864426746530627595` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864426724023468092` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864426715799486494` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864426711125721089` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864425456726835211` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864425420451217448` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864425342105288736` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864425331960184853` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864425122071576576` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864425002585292832` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424932921311273` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424918912073760` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424821370388510` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424719382347786` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424669724540938` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424644085940244` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424617513713685` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424574048010251` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424539764424714` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424406428286987` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424327336427520` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424171844534284` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424057613451264` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424041141895168` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424039917027348` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864424006663929877` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423981703233537` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423967418351666` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423863755472947` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423815844200458` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423683744464917` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423523295821844` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423522860269579` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423466488430602` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423354604978178` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423350558654464` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423350187982858` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423339202969611` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423280948412426` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423071850561566` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423007333515314` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864423007324995594` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864422968540397578` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864422802798280735` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864422783772786688` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864422695814955068` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864422694506201088` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864422576846929931` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864422445033193502` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864422352740548648` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863719105382055947` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863719100186361916` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718991448899634` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718980804149278` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718968408932352` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718957771915266` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718934669557780` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718934624731147` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718924951879701` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718896661168138` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718865409933312` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718847038750730` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718836938473482` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718831007989760` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718790427574322` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718789958467595` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718783579455508` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718783523880960` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718767385509898` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718758836469771` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718727114424331` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718711357603865` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718706986221568` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718706169118720` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718701568360448` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718693979553815` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718674891145226` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718642114232320` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718605493239829` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718454849568768` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718442283958293` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718409694216223` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718408171683880` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718373153046549` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718244250157067` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718231813128203` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718227232948234` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718212578836501` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718203749564436` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718202181812245` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718200651022412` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718195583778826` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718189082083328` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718183029833748` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716522403823616` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716504607653888` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716495857942529` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716488825012225` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716483712286750` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716412111847465` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `730255089847107624` | 07/13/2021 | Phishing bot ('Veroxx#4123') distributing deceptive credential-harvesting link 'stearncommunytiy.ru'. |
| `864569984234815509` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864542779789803532` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864542768382345246` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864542726070337547` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864542703890071552` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864542697758523472` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864539855249211432` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864539821103906836` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864538684816752671` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863764665938477076` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `118109437989748740` | 07/13/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `409423094734913536` | 07/13/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `519326232089853967` | 07/13/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `863195697948262442` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863189714147475456` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863181985328529458` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863178736547528704` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863134254333820968` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863112266446274570` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863098457685622834` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863098432759791626` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863098419538296833` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863097794737864734` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863097712470917140` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863085834105258014` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861518069117485067` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861518025316761620` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861515253783461949` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861515219976847371` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861066339170385940` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `426417273000165386` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `687274691161096250` | 07/12/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `862002649766952971` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `862002563334668293` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861669282030813214` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861668755041681428` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861667404403966003` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861666885657427968` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861666060397576233` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861665541068816425` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861664903197360158` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861664123616100392` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861663107595632700` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861662953354035210` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861662614370517022` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861662530577498162` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861662208207093802` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861662094953021460` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861661654981541901` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861661542951682069` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861661134662402089` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861661069072531476` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861661024109068308` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861660665134710796` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861660659611598848` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861660650786258984` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861660638480826401` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861660598981623809` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861660198645137438` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861660196735418420` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861660169116057630` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861660165249957906` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861601533317611540` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861600088123899934` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861599748959633428` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861599405567377408` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861599305629433856` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861598930659835904` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861598916424630292` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861598489535971379` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861598473290776576` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861598443235311656` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861598104259526658` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861597780358856704` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861597775712354344` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861595751015645184` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861595611701575740` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861595167495421954` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861594762040573963` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861594716088827904` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861594704823189504` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861594320053993472` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861594172150906910` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861593766070321183` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861593696612515881` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861593680372039721` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861593568832389130` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861593242146963457` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861593166972583966` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861592864719110166` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861592828953755648` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861592674901295134` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861592357420924928` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861591940381147137` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861591887600418816` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861591733212151828` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861591724639256596` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861591505876811786` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861591490953609257` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861591322577207327` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861591067182497803` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861591063776854027` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861590052114530324` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861588873216524339` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861588451081584640` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861588156942909460` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861237840028499999` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861237587960004629` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861237516857114636` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861237322677878814` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861237202066341908` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861237170886017035` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861237001712828427` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861236759550230538` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861236533352595487` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861236503316660225` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861236413922803712` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861236380595257396` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861235998532042772` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861235989304705034` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861235988642005043` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861235982354350141` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861235979720982538` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `860940807477526549` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `860939848583872554` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `860939313713512520` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `860937334547021826` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `860937267862568981` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `860936869540528148` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `860936865880080414` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `860936862885085184` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `860932975704408094` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863719136245186560` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863719087293464586` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863719043089563689` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863719004673277992` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718961145184276` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718954031120384` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718898712444938` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718830089961472` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718826033545236` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718794631315457` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718758450593793` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718703681503232` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718642780471336` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718629227888640` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718627990306816` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718603642765322` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718560232898571` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718499914743848` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718496012337182` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718465701806081` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718429278470156` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718404597743626` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718403763994624` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718403667525662` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718331345010698` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718262243590154` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718243935584256` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718233072861184` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718220476186675` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718215317979146` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718206694096926` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718189581598732` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863718183423574036` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716638959861760` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716624954294273` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716565979365378` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716548288315413` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716465038327858` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716457544286238` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716442298253324` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716417278050325` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716407170039808` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716365512736780` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863716353478623272` | 07/12/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `864179951446917150` | 07/12/2021 | Malicious scam account flagged and reported by community moderation. |
| `855377725929553932` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `853101155475128340` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `848418638619738123` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `846729260981944341` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `846384760259608607` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `809642848576208896` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `809622565114085406` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `807974601158164491` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `749532991516311613` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `703065786180173844` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `668625024768540725` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `579121035547246592` | 07/11/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `862048494587740172` | 07/11/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `633012827547893782` | 07/11/2021 | Malicious scam account flagged and reported by community moderation. |
| `499737127374815242` | 07/11/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `863127969132052481` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863127471368831017` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863127156904951868` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863090715679653899` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863090572746817536` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863077664637190155` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863069893195857962` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863069770353475644` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863068224363167784` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `863063014411206666` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `862979892826996767` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `862979593774563369` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `843787194719272990` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `843746262998319116` | 07/10/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `786082003425558538` | 07/10/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `861445447624949790` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861444881875599371` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861444284048474133` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861444003379806218` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861443994335969290` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861443801603768330` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861443612112846889` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861443401400451072` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861443398581223445` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861443251385663498` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861442855968702476` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861442586022903818` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861442495447826452` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861442325612068894` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861442306356150323` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861442128826990594` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861441876983939073` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861441852002795521` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861441824543473664` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861441810761383946` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861441712197861389` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861441707123277834` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861441632917913620` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861441063297613825` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861440970221813780` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861440918564503573` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861440773803212811` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861440653278707763` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861440402065326151` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861440256518520862` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861439803639595009` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861439036634955806` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861438955051155476` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861438849502937088` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861438747865645098` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861438514452758538` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861438382076329995` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861438241290321940` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861438174898421770` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861438159991996467` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861438142153228299` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861437707812077599` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861437457064001537` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861437444414767134` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861437312494993418` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861436943136587787` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861436788127301682` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861436673098252288` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861436467921027093` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861436339097698325` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861436202766303262` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861436171808538624` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861436009996615720` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861435932137881602` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861435758463549451` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861435742295425074` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861435646655856640` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861435625692332053` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861435406846656513` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861435327837896704` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861435035562672149` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861434637427671070` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861434059804770314` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861433787313553428` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861433681683677206` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861433655632592896` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861433649648107520` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861433475017080843` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861433277309779990` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861432921928105994` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861432585926082610` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861432212397621299` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861432164339941376` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861431863661821982` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861431855517794314` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861431841567277058` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861431585735704596` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861431521079590912` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861431420832710657` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861431017599795230` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861430987346673664` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861430754285715456` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861430708164755477` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861430691447570452` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861430584521392159` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861430555287748608` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861429882566344724` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861429819787182120` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861429766946160701` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861429462193405982` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861429460196917248` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861429439689654303` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861429063859568641` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861429015357554709` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861428494763950131` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861428088046616606` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861428038285000754` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861427413023850506` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861427352168955977` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861427140758863922` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861426998262104064` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845279653404082187` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845279312642965515` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845279267411853342` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845279121189109790` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278987668291624` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278889391554630` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278884563648543` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278847271960607` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278842851295253` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278834978193488` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278683384119316` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278478965800990` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278445209780264` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278345310896178` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278299667824641` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278233065816095` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278217182380093` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278212262854677` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278149058232330` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278136714526760` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278075297595432` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845278066045747221` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845277818568835122` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845277702462373918` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845277419484086314` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845277403927543888` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845277350240452638` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845277177359892490` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845277159621656577` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845277150706008084` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276938179182603` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276892029386792` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276849005395990` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276847544860753` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276836128882738` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276825772097586` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276598185885707` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276550471090187` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276521937764402` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276510352179201` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276451909795880` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276443512143883` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276329745055824` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276328718499871` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276210170298418` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276177606246420` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276175978594356` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276061272375296` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845276014048968745` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845275782053101578` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845275724843843584` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845275224240816148` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845275217411702815` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845275013095751700` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274842965606411` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274842714210324` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274824967192596` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274807045718026` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274789127782443` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274748472131625` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274666070310924` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274557026795521` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274524843769856` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274480330801152` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274402144124948` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274363770830860` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274324462207026` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274296225628192` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274295072587806` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274269528752180` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274155342626857` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274134304522241` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274117867569194` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274088716369961` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274024326070284` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274022640222249` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845274022338232331` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272786691031070` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272785005838346` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272750800240694` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272741736480788` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272730705985536` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272593853448264` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272462300151808` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272284256010281` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272204626886666` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272199124615178` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272134729465867` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272120867291146` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272084699283456` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272016721674281` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845272007398522900` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271999391465504` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271941744820255` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271817584902176` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271784391180308` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271767497048064` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271740640133130` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271715542335518` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271656410251274` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271625900883998` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271624458043413` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271588169318400` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271510028910592` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271491301736508` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271441486250024` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271429636292638` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271423177719888` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271422120230952` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271414617145394` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271399130988595` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271375186231296` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271360623738920` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271357302112298` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271332899520522` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271327799246880` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271285084323850` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271277962264607` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271253962457129` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271205800050728` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271110672056320` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845271094118318121` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845270983165083648` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845270980577984553` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845270925297451038` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845270845252960277` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845270626548973617` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845270393752518656` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845270269304373278` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845270179869229058` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845270157546487858` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845270069617491998` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845269636492689431` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845269332971356220` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845269205853929503` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845268840153481216` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845268391547502676` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845268352691601409` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845268296479277076` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845268071345815552` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845268026679885844` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845267990278832128` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845267394049605653` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845267261035511818` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845264826409418753` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845263524807704658` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `845262271575621663` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `862767046337363978` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862765933948698624` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862764341560082492` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862763353017417730` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862762702291861514` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862761440146620446` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862760810589323314` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862759949583384656` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862759121727520789` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862758152353480764` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862757456287236126` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862756601174032434` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862755884589776936` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862755215123677225` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862754551442178088` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862753591218929685` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862752933779472394` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862751995143913523` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862750605385400370` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862749677752811520` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862747858683428885` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862740325391138876` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862739675408236574` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `862738219916984351` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `860892997909872662` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `860887736793694219` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `859536589674905641` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `859535898596081674` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `859535232528547900` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `859531518962565130` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `794938003906232330` | 07/09/2021 | Compromised account mass-spamming fraudulent Discord Nitro links. |
| `861413880957894677` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861413735171096576` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861413636241096705` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861412853872853011` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861412668728016899` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861411848833859645` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861411757414285312` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861410896941154355` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861410317347323944` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861410280017494047` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861409696556122112` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861409604911104000` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861407288166055958` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861407093055684638` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861405118745411584` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861404887421026344` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861404284775694336` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861404003551281204` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861403069710467112` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861403039105417269` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861402479098331136` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861402435619913750` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861401539566501908` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861400714245177374` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861399608412733450` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861399475363905578` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861398992817225748` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861397834381262858` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861397667792158750` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861396739441688596` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861396511484280853` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861396422691520543` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861395736766971955` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861395731520684042` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861395526704169002` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861394817182072853` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861394800136683560` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861394283298291732` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861393752991858720` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861393722909524009` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861393578475257898` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861393083106328576` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861392860850946069` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861392132828954674` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861390812273573888` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861390358118006784` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861390044828139531` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861389818885963786` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861389438546477067` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861389243049967667` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861388750189101057` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861388489467494400` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861388235578146846` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861387701457256498` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861387134903255080` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861386944155746304` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861386454914826261` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861386381103202365` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861386025862561792` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861385837253230602` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861385820317679616` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861385329021419521` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861385260952191006` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861384699637137428` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861384609212399657` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861384569769033760` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861383796975730708` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861383179796742174` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861382545605132339` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861382374197166161` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861381906377080853` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861381759915655168` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861381703129759755` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861380953830457424` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861380375192666132` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861379644522889216` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861379614743199774` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861379532497354782` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861378877422436372` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861377396313423923` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861377338268581950` | 07/09/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `861067927062315078` | 07/09/2021 | Malicious scam account flagged and reported by community moderation. |
| `857375773597237259` | 07/09/2021 | Phishing bot ('lxpm#7667') distributing deceptive credential-harvesting link 'stearncommunity.ru'. |
| `468945556379664385` | 07/08/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `862259487820873769` | 07/07/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `861523959220404224` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `861523809546403891` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `861522115840442399` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `861521720245878784` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `861519692095422464` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `861507726215479297` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `861507687397195796` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `861521448408449045` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `247752240398336000` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `861521312329367582` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `425122179710189569` | 07/07/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `862387918597128192` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `861677676514902084` | 07/07/2021 | Malicious scam account flagged and reported by community moderation. |
| `862178035389825085` | 07/07/2021 | Identified ban evasion alt account linked to previously banned user. |
| `846454394916569178` | 07/06/2021 | Identified ban evasion alt account linked to previously banned user. |
| `585232694007562242` | 07/05/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `537792482495430658` | 07/04/2021 | Phishing bot ('Anti-Spiral#0002') distributing deceptive credential-harvesting link 'steamcommunytu.ru'. |
| `704492218957824111` | 07/04/2021 | Phishing bot ('Hirotø#7336') distributing deceptive credential-harvesting link 'stearncomminuty.ru'. |
| `510387455656984588` | 07/04/2021 | Phishing bot ('MAR#9696') distributing deceptive credential-harvesting link 'stearncomminuty.ru'. |
| `549991152108044289` | 07/04/2021 | Malicious scam account flagged and reported by community moderation. |
| `828661296547233832` | 07/04/2021 | Malicious scam account flagged and reported by community moderation. |
| `331070130819694592` | 07/04/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `697599941417369653` | 07/04/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `685465489786273843` | 07/04/2021 | Phishing bot ('ƬТҞ_𒋑#5137') distributing deceptive credential-harvesting link 'steamcommunytu.ru'. |
| `859860886227124245` | 07/04/2021 | Malicious scam account flagged and reported by community moderation. |
| `845300381394927696` | 07/03/2021 | Malicious scam account flagged and reported by community moderation. |
| `859132694406234122` | 07/03/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `696434850563096656` | 07/03/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `479025116030697472` | 07/03/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `547060442107871329` | 07/03/2021 | Phishing bot ('Alonso.2080#1159') distributing deceptive credential-harvesting link 'steamcommunytu.ru'. |
| `859867317738274916` | 07/03/2021 | Malicious scam account flagged and reported by community moderation. |
| `801838049994211379` | 07/02/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `763422338687434772` | 07/02/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `696330852031922236` | 07/02/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `341594390524985344` | 07/02/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `450295859209306122` | 07/02/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `768665946004652103` | 07/02/2021 | Phishing bot ('Shin#2768') distributing deceptive credential-harvesting link 'stearncomminuty.ru'. |
| `360584843748442123` | 07/02/2021 | Phishing bot ('rckt_cris#7175') distributing deceptive credential-harvesting link 'stearncomminuty.ru'. |
| `601676804109107202` | 07/02/2021 | Phishing bot ('Cyrus MEXICAN DREAM#0001') distributing deceptive credential-harvesting link 'steamcommunytu.ru'. |
| `447756574388125716` | 07/01/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `554924157612195841` | 07/01/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `723560984005967922` | 07/01/2021 | Phishing bot ('DavisXD#1626') distributing deceptive credential-harvesting link 'stearncomminuty.ru'. |
| `859644307538182156` | 07/01/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `663054085175509012` | 07/01/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `658038890086531073` | 07/01/2021 | Phishing bot ('Renatowww_br#2437') distributing deceptive credential-harvesting link 'stearncomminuty.ru'. |
| `859957322012295199` | 06/30/2021 | Malicious scam account flagged and reported by community moderation. |
| `859938898657411092` | 06/30/2021 | Malicious scam account flagged and reported by community moderation. |
| `536593087229853697` | 06/30/2021 | Phishing bot ('jmxry_#0912') distributing deceptive credential-harvesting link 'stearncomminuty.ru'. |
| `859878044638117888` | 06/30/2021 | Malicious scam account flagged and reported by community moderation. |
| `859631620222877746` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859631395525886004` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859631028599128074` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859630709126463498` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859630673564663818` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859630653912907786` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859630499450454036` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859630435667673098` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859630247905722409` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859630121463185419` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859630108430958592` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859630064308060201` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859629975749001237` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859629895628881921` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859629807909994527` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859629188490330112` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859629084174581770` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859628921816612896` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859628849142824970` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859628692874199051` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859628546590900234` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859628527467626569` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859628358340706314` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859628178506121249` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859627991399137280` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859627947907743764` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859627887095578664` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859627662301069333` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859627504116301854` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859627442364219422` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859627398491406337` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859627385812287490` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859627299749888051` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859627256619204650` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859626893816102912` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859626828360187919` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859626753675493436` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859626741622505512` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859626705757143041` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859626631730954271` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859626187969527809` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859626092938395649` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859625799673839636` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859625668077682689` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859625645205618718` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859625569972912128` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859624173253165068` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859623123732791308` | 06/30/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `329641485664387072` | 06/30/2021 | Malicious scam account flagged and reported by community moderation. |
| `468877784668700683` | 06/30/2021 | Malicious scam account flagged and reported by community moderation. |
| `484621980906291211` | 06/30/2021 | Malicious scam account flagged and reported by community moderation. |
| `485836674484535307` | 06/30/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `859641298012471296` | 06/29/2021 | Malicious scam account flagged and reported by community moderation. |
| `859600303304474634` | 06/29/2021 | Malicious scam account flagged and reported by community moderation. |
| `859607179546591272` | 06/29/2021 | Malicious scam account flagged and reported by community moderation. |
| `859591752049492018` | 06/29/2021 | Malicious scam account flagged and reported by community moderation. |
| `859592501617491989` | 06/29/2021 | Malicious scam account flagged and reported by community moderation. |
| `859586775059791874` | 06/29/2021 | Malicious scam account flagged and reported by community moderation. |
| `859582454855499806` | 06/29/2021 | Malicious scam account flagged and reported by community moderation. |
| `859576608486850602` | 06/29/2021 | Malicious scam account flagged and reported by community moderation. |
| `859518985958850560` | 06/29/2021 | Malicious account distributing cryptocurrency phishing scams. |
| `858721809385652294` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721798031278110` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721626958200833` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721601791983646` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721596108963840` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721514233004033` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721506620473395` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721491751141427` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721483009949726` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721465947258892` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721387161976843` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721350527746089` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721292797345803` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721202142969906` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721167207825487` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721137357357086` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721121331445800` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858721081614270474` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720990493409300` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720981652733972` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720907018108948` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720870742753351` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720863728959499` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720836630347776` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720782850719765` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720752358391828` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720712389951508` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720655938420767` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720618627465216` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720599105994752` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720551073218590` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720540428730368` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720455204929556` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720446563745793` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720436724826142` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720392047099934` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720388816044055` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720245824880651` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720239126708256` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720230112755723` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720225075527760` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720138493034516` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720037048418324` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720012951879710` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858720008237350932` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719907058942003` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719886507114506` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719858458886165` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719808505905192` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719802004471850` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719745516109865` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719724321767424` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719719917617212` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719706973077504` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719543551852564` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719509435514881` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719490896035890` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719465202122763` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719430841466890` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719430838321172` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719420277063710` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719263522291733` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858719225102598155` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858579874226110476` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858579728595943434` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858579607119724564` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858579438195179520` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858578986627366943` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858578215298400306` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858578125499400252` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858578083358310414` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858577711843901452` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858575486321819649` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858575134284578826` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858575045890932746` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858574933537062942` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858573909586870292` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858573892183523328` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858573670696222740` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858573582941683713` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858573005499924511` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858570714591002624` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858567691265376257` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858560046514700308` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858559367107575830` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858556464350887957` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858553696786055208` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858551455069765652` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858550845897572352` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858550430040326194` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829030269453336626` | 06/28/2021 | Malicious scam account flagged and reported by community moderation. |
| `858763199641681960` | 06/28/2021 | Malicious scam account flagged and reported by community moderation. |
| `858719604791705610` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858570677527248896` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858564653751861279` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858560217209372692` | 06/28/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `859023072131284993` | 06/28/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `858735149805207582` | 06/28/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `856560732140470284` | 06/28/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `371653060092624907` | 06/28/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `858510092811239434` | 06/28/2021 | Scam account ('ConnorWyatt#5273') banned for: hi I have a 2060. |
| `857521308295364618` | 06/28/2021 | Scam account ('DarrenWillis#1239') banned for: I have a 2060. |
| `857320265289826304` | 06/28/2021 | Scam account ('ToddAlquist#3701') banned for: hi 2060 -d. |
| `856231997386784768` | 06/28/2021 | Scam account ('JakeSmith#8082') banned for: hi 2060. |
| `846440550390693899` | 06/28/2021 | Scam account ('HarryWillis#6258') banned for: I have a 2060. |
| `853028134134874122` | 06/28/2021 | Malicious scam account flagged and reported by community moderation. |
| `856926218024779797` | 06/28/2021 | Malicious scam account flagged and reported by community moderation. |
| `854037521071996928` | 06/28/2021 | Malicious scam account flagged and reported by community moderation. |
| `813448486699401277` | 06/28/2021 | Malicious scam account flagged and reported by community moderation. |
| `235765961163145216` | 06/28/2021 | Malicious scam account flagged and reported by community moderation. |
| `856204099304030228` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `843887955470712835` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `842052877166182482` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `838569657304743946` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `837645015710040125` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `828784178635997215` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `839743763958333450` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `845448105163489281` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `844730113887305759` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `844256610305703966` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `836028747701551114` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `807977708029083708` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `842054468635852830` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `839557365446475816` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `837645409546928139` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `828667590221627392` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `813633245769760768` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `812334658825486336` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `846803148630261792` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `837863852887769098` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `854062579608584192` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `854039703741399090` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `584886757489770517` | 06/27/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `361239934390108160` | 06/27/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `857628219246903298` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `857627810810298378` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `857627054941929493` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `857095188517486633` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `857091365250269214` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `856668795334688788` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `667598529031700490` | 06/27/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `292328399886614528` | 06/27/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `158583038341677056` | 06/27/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `558847347803815936` | 06/27/2021 | Malicious scam account flagged and reported by community moderation. |
| `858571156327497768` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858570896842555414` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858570852559749171` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858570632077508628` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858570493007233095` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858570323610959872` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858569542107398184` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858569333772779591` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858569316890837012` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858569022722408478` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858567516770271253` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858566496795885579` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858566183128530944` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858565856845758474` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858565385803268126` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858565122007891979` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858565064792211476` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858564751591079996` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858563550469554197` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858563336908439573` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858563261891739728` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858563229561913425` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858563064005525524` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858562956111511563` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858562868306509834` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858562721180418048` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858562099978698792` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858562045677928468` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858562012563636235` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858561981611245609` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858561963087626250` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `858560451055058994` | 06/27/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `263702083008593931` | 06/26/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `505446290822397962` | 06/26/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `830075939026108466` | 06/26/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `759641918886903819` | 06/26/2021 | Malicious scam account flagged and reported by community moderation. |
| `857641745839685652` | 06/26/2021 | Malicious scam account flagged and reported by community moderation. |
| `857641944766873671` | 06/26/2021 | Malicious scam account flagged and reported by community moderation. |
| `857641525202911232` | 06/26/2021 | Malicious scam account flagged and reported by community moderation. |
| `857641833152249857` | 06/26/2021 | Malicious scam account flagged and reported by community moderation. |
| `857641768157708298` | 06/26/2021 | Malicious scam account flagged and reported by community moderation. |
| `857641224643018803` | 06/26/2021 | Malicious scam account flagged and reported by community moderation. |
| `857519124530987009` | 06/25/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `577111882356490252` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `856599414864347196` | 06/25/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `857933784195399680` | 06/25/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `753703147595235328` | 06/25/2021 | Malicious scam account flagged and reported by community moderation. |
| `857244910808596511` | 06/25/2021 | Scam account distributing fraudulent Nvidia promotional links. |
| `772528936847933450` | 06/25/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `352953892033527808` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `644205291356815361` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `717967013557043220` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `711767787063738369` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `687690366505189529` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `661617535141150750` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `567777892793057311` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `767725783066083328` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `604459683734093825` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `837640211323158558` | 06/25/2021 | Malicious raid or scam account flagged by community moderation. |
| `521259056422322176` | 06/25/2021 | Malicious raid or scam account flagged by community moderation. |
| `812630831083421708` | 06/25/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `857365686492856330` | 06/24/2021 | Malicious raid or scam account flagged by community moderation. |
| `707638757087641610` | 06/24/2021 | Malicious scam account flagged and reported by community moderation. |
| `359000158567923722` | 06/24/2021 | Malicious raid or scam account flagged by community moderation. |
| `857096969721085992` | 06/24/2021 | Malicious raid or scam account flagged by community moderation. |
| `857537581104365578` | 06/24/2021 | Malicious raid or scam account flagged by community moderation. |
| `627889304173150249` | 06/24/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `435592130434695179` | 06/24/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `335859184153133056` | 06/24/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `857470349180665877` | 06/24/2021 | Malicious raid or scam account flagged by community moderation. |
| `575892327881768960` | 06/23/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `467621205789376512` | 06/23/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `857257355434262538` | 06/23/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `715494759963295745` | 06/23/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `689176827281145915` | 06/23/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `857201599524765737` | 06/23/2021 | Malicious raid or scam account flagged by community moderation. |
| `857292445238951956` | 06/23/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `854405766273695784` | 06/23/2021 | Malicious raid or scam account flagged by community moderation. |
| `857024598273294367` | 06/23/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `685900112022470657` | 06/22/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `652181277864230931` | 06/22/2021 | Malicious raid or scam account flagged by community moderation. |
| `855939360180535348` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855939122811633694` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855939015349239899` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855938956705005598` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855938626793504778` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855942521141198848` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855942376651489293` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855942233475907585` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855942110578081852` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855942091111399474` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855942071646158889` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855941926695600158` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855941509249630208` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855938628676354078` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855938514684477451` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855938433533214752` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855938394164035614` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855938116463231017` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855938096118235206` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855935218429853736` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855934339191144498` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855934295230775297` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855934083384082432` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855935034934034432` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855934841396527115` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855934625602994196` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855934431193858049` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855934275014492181` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `281138079853707276` | 06/21/2021 | Malicious raid or scam account flagged by community moderation. |
| `558295709791682561` | 06/21/2021 | Malicious raid or scam account flagged by community moderation. |
| `829271661563084831` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829270215338622998` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829270082877915207` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829163167535857674` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829163058931957761` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829163052619268121` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829163048127168552` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162769190223944` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162762847911958` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162720317276190` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162640692478044` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162606325006417` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162596975247380` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162453484699679` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162446618492968` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162446169833492` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162329022660678` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162327932796958` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162160533143563` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162101897429044` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162099733037127` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162063586394132` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162055634124841` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162046343741441` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829162023718748192` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829161955217506324` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829161904525672499` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829161850418626610` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829161652368441345` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829161585191813150` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829161545820667936` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829161395273859163` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829161391264366602` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829161349695143967` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `829161222905266187` | 06/21/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `856567250630606868` | 06/21/2021 | Malicious raid or scam account flagged by community moderation. |
| `831086868850278410` | 06/21/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `743206843043807394` | 06/21/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `460171368411955201` | 06/21/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `287646365583015938` | 06/20/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `597124711549370381` | 06/20/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `490996559115452417` | 06/20/2021 | Malicious scam account flagged and reported by community moderation. |
| `507331836356067343` | 06/20/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `433430689090764806` | 06/20/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `854980204995805204` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854979828964786176` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854973037685506079` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854965327358853140` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854964719885877268` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854929849381814277` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854928426041737237` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854911183467315230` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854895322903740447` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854893128968568842` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854891564156977164` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854885659125612594` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854877900524486676` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854866107777024000` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `854859950291025921` | 06/20/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `302497483249025025` | 06/20/2021 | Malicious raid or scam account flagged by community moderation. |
| `639849851231666196` | 06/20/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `492097632416563211` | 06/20/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `388131666889146378` | 06/20/2021 | Malicious raid or scam account flagged by community moderation. |
| `399610992201433099` | 06/20/2021 | Malicious raid or scam account flagged by community moderation. |
| `555092277400174592` | 06/20/2021 | Malicious raid or scam account flagged by community moderation. |
| `557838968469585941` | 06/20/2021 | Malicious scam account flagged and reported by community moderation. |
| `854983804368584704` | 06/20/2021 | Malicious raid or scam account flagged by community moderation. |
| `562666362195935252` | 06/20/2021 | Malicious raid or scam account flagged by community moderation. |
| `454769254991003648` | 06/20/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `855618063470952449` | 06/19/2021 | Malicious raid or scam account flagged by community moderation. |
| `203204317652582400` | 06/19/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `810318431676268544` | 06/19/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `538461726971133952` | 06/19/2021 | Phishing account distributing fraudulent Steam trade or report scams. |
| `851872205091373056` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851859610603356200` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851851508692811796` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851849544828584058` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851849348077977681` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851849114459177041` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851848241980637184` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851847573576482856` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851846997761196132` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851846373502746645` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851846247044350013` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851845902788329532` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851842266728235038` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851841030977224754` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851841003437948938` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131675030847529` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131649848246312` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131631737372703` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131611621883985` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131586442166293` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131502636826665` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131499099979847` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131440921444374` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131424252755969` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131419581087754` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131408108879883` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131355625685022` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131287691329558` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131269919801394` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131191419732079` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131154144952350` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131153183145984` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131139102867476` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131120035561473` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131056493166653` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131054612807700` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131040290308097` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851131037672669285` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130990298398721` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130987366711336` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130973168992287` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130971420229694` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130959172861992` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130833364582401` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130829546848256` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130773611741224` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130768515792957` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130705361895454` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130704322363393` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130700911607868` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130700575932487` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130687179718687` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130679138975785` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130666254467142` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130530551955476` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130480875143198` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130361369985024` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130347814649908` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130322727993344` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130316428673044` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130311877066764` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130307011674173` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130304391675935` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `851130189207437352` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849702683236630598` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849698494716313600` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849698104676319255` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849696715425841222` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849687791570911253` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849687767273046056` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849687764119453716` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849687489438023691` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849687359934562306` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849686695984627783` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849686548323893268` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849686451587383346` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849686250630021150` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849685980163866675` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849685911645585438` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849685753234718801` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849685652902903868` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849685521294163999` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849685109572763689` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849684965574836265` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849684349670129714` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849682786477539359` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849682087790903296` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849681518279917578` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849681472063537162` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849680098993897506` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849373752243519531` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849373494398681159` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849372855345872930` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849371817167945738` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849371537198022716` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849371112861204561` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849371075493756999` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849370712199135273` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849370485061845036` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849370461204906064` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849370365105143839` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849370101412921384` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849369763637624852` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849369558337978420` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849369093705564172` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849369024836010064` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849368946779750420` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849368415607980043` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849368391953023088` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849368184812208140` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849367959989649468` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849367959628677162` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849367884371066920` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849367854611693578` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849367509726920714` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849333467949957120` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849333104165388348` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849333092313595934` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849333031923351553` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849331774379130906` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849293816141971477` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849293748198309910` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849291966248386580` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849291915878334513` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849291610393935902` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849291312934158386` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849290743763435532` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849289277891805215` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849289182139383839` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849288731550548018` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849288699703328768` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849287557886771230` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849272888934400060` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849245583968829470` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849243447515938877` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849242192505339964` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849241580715507733` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849236836513611807` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849233952190627840` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849231564726468628` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849230878571888660` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849230684090400778` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849148639611584553` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849148383523373119` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849147516415115264` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849146906731085854` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849146347436507157` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849048091360755722` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849033991339245588` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849032086747873321` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849031172217765899` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849030889807544381` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849030838632448030` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849027525455249438` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `849026001795285013` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `846230979165421599` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `842247185105289216` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `727623998938021889` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `604105909328936960` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `345370262398828553` | 06/19/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `759226976837435402` | 06/19/2021 | Malicious raid or scam account flagged by community moderation. |
| `333098785762836480` | 06/19/2021 | Account participating in automated CS:GO trade and phishing scams. |
| `855212101345345567` | 06/18/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855211522804678677` | 06/18/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855211400213561414` | 06/18/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855211276068978689` | 06/18/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855211051209326602` | 06/18/2021 | Coordinated raid account participating in mass malicious server disruption. |
| `855210960360308756` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `762393629880090625` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `817516962808463383` | 06/18/2021 | Malicious scam account flagged and reported by community moderation. |
| `854723580021571605` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723549171679312` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723527618199552` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723488065650708` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854725060573003817` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724944210558997` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724911405465600` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724899149709322` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724892305653822` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724868671406082` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724863456444436` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724844632932422` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724832091439135` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724553095512107` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723517983096862` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724835073982474` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724796062498816` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724751544549386` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724737305542686` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724718367080469` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724713355018250` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724591658074202` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724525907640350` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724248496373780` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724234500767765` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723897281740870` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854725195192598538` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724788915011595` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724761287655484` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724285443604520` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854724101917769728` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723936654852167` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723930148306985` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723857428119590` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723741594550274` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723617445904404` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723544540512276` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854725711151759420` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723968052887582` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723959097262130` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723907319365663` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723824709009418` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854723507618709534` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `854382235079933972` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `563023114146152468` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `417745501446733845` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |
| `650307626021814276` | 06/18/2021 | Malicious raid or scam account flagged by community moderation. |

---

## License

This work is dedicated to the public domain under the [Creative Commons CC0 1.0 Universal License](LICENSE). Anyone may freely use, copy, modify, and distribute this list without restriction.
