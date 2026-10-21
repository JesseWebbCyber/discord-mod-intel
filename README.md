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

## Active Reported Accounts (64 IDs)

Ordered from newest to oldest.

| Discord ID | Date Reported | Ban Reason |
| :--- | :--- | :--- |
| `1313451022491848764` | 10/19/2026 | Coordinated advertising raid account using fake member hype to promote third-party events. |
| `704031430325436537` | 10/19/2026 | Harassment raid participant engaging in coordinated server trolling. |
| `484765847546626068` | 10/19/2026 | Harassment raid participant engaging in severe trolling and channel disruption. |
| `1561031456392876142` | 10/18/2026 | Ban evasion alt account used to re-enter servers after prior moderation removal. |
| `1242212409498927220` | 10/17/2026 | Automated bot account sending unsolicited recruitment scams in member direct messages. |
| `1373356582657589398` | 10/17/2026 | Automated bot sending unsolicited spam links into member direct messages. |
| `1556010033479815328` | 10/15/2026 | Coordinated advertising raid account using fake member hype to promote third-party events. |
| `1555629557510447115` | 10/15/2026 | Coordinated advertising raid account using fake member hype to promote third-party events. |
| `1551464928248856607` | 10/15/2026 | Coordinated advertising raid account using fake member hype to promote third-party events. |
| `938710016289046608` | 10/12/2026 | Account ('f0rgotte1n') mass-spamming unauthorized NSFW server invites. |
| `751903171198189618` | 10/12/2026 | Disruptive troll account flagged for severe behavioral misconduct and harassment. |
| `1533229968656568393` | 10/09/2026 | Compromised account participating in coordinated malicious spam raids. |
| `1430353021946040410` | 10/09/2026 | Compromised account participating in coordinated malicious spam raids. |
| `1287854594482901005` | 10/09/2026 | Compromised account participating in coordinated malicious spam raids. |
| `1144325061654888649` | 10/09/2026 | Compromised account participating in coordinated malicious spam raids. |
| `1068874695702761482` | 10/08/2026 | Unsolicited DM spammer targeting server members with phishing links. |
| `1523754110409637980` | 10/08/2026 | Social engineering scammer attempting to trick members with fraudulent claims. |
| `1507457811381096458` | 10/07/2026 | Unsolicited DM spammer targeting members without shared mutual servers. |
| `490188321226620928` | 10/06/2026 | Account ('danishgtr') distributing fraudulent cryptocurrency scam links. |
| `687933479622934620` | 10/06/2026 | Account ('4m4y4s') distributing cryptocurrency phishing messages across servers. |
| `340714404314349570` | 10/05/2026 | Account ('kyotorun50') promoting deceptive cryptocurrency investment scams. |
| `1426974684834041971` | 10/04/2026 | Confirmed ban evasion alt ('v3nk_i') used for silent lurking and evasion. |
| `1313958539773087845` | 10/04/2026 | Primary account ('lenoirsx_') of a persistent troll spreading hate speech and Discord ToS violations. |
| `1351938127530430536` | 10/04/2026 | Confirmed alt account ('matthewandre_x') used for ban evasion and harassment. |
| `953748748280946730` | 10/04/2026 | Persistent troll account ('lenoired') violating Discord ToS with hate speech and harassment. |
| `1456722209656803483` | 10/04/2026 | Underage user engaging in hate speech and repeated racial slurs. |
| `1505223386199232674` | 10/04/2026 | Confirmed ban evasion alt ('sophus359353' / 'agdagfda') belonging to a serial harasser. |
| `1383608829379346525` | 10/04/2026 | Deleted alt account identified in cross-server ban evasion network. |
| `1283321787341340744` | 10/04/2026 | Confirmed ban evasion alt ('hell706') belonging to a serial harasser. |
| `1436422427142787243` | 10/04/2026 | Confirmed ban evasion alt ('yassingamer0317') belonging to a serial harasser. |
| `1414752214051721348` | 10/04/2026 | Confirmed ban evasion alt ('ah23421') belonging to a serial harasser. |
| `1369678199201730602` | 10/04/2026 | Confirmed ban evasion alt ('ratchet0549') belonging to a serial harasser. |
| `1197253997543825521` | 10/04/2026 | Confirmed ban evasion alt ('steavengameryt') belonging to a serial harasser. |
| `1110476666192535653` | 10/04/2026 | Confirmed ban evasion alt ('linux706') belonging to a serial harasser. |
| `1023079001985663126` | 10/04/2026 | Impersonated community staff members to target unsuspecting users in direct messages. |
| `1196850086953631755` | 10/04/2026 | Promoted fraudulent 'MrBeast' cryptocurrency giveaway scams in chat. |
| `855443094870687794` | 10/04/2026 | Account flagged across moderation teams for suspicious targeting of minors. |
| `1400825354435821730` | 10/04/2026 | Account ('vstromakias7') promoting fraudulent cryptocurrency scams. |
| `1555525351914999866` | 10/04/2026 | Malicious account reported for unsolicited advertising and deceptive links. |
| `1519707665096507621` | 10/03/2026 | Scammer engaging in name-spoofing and deceptive identity theft. |
| `400896526924251136` | 10/03/2026 | Compromised user account distributing phishing and account-stealing links. |
| `1286838349335629906` | 10/02/2026 | Automated adult-content / OnlyFans spam bot targeting server members. |
| `1555337843235102885` | 10/01/2026 | Scammer advertising fraudulent high-income / 'earn 100k' financial schemes. |
| `1287882355251478550` | 10/01/2026 | Compromised account distributing malicious links across tech servers. |
| `1492875609372885052` | 09/30/2026 | Malicious spam bot reported to Discord Trust & Safety for account compromise. |
| `406620720437788674` | 09/29/2026 | Deceptive account sharing server space to run targeted member phishing attacks. |
| `1545981820649218090` | 09/11/2026 | Automated scam bot targeting member direct messages with malicious links. |
| `936358065207390238` | 09/11/2026 | Automated scam bot targeting community channels with malicious links. |
| `1546840214960607243` | 09/08/2026 | Automated bot account scraping member lists and spamming fake job listings. |
| `1537455244928221206` | 09/04/2026 | Automated job listing spam bot posting fake employment opportunities. |
| `1395449757371076628` | 09/03/2026 | Automated scam bot masquerading as an AI firm to harvest user credentials. |
| `1504087093528231996` | 09/01/2026 | Underage user raiding community voice and text channels. |
| `1226567367941689536` | 08/23/2026 | Malicious bot account distributing unauthorized links and spam. |
| `797391110900285441` | 08/23/2026 | Compromised account flagged for cross-server spam and phishing outreach. |
| `1490501890109341919` | 08/21/2026 | Compromised account spreading fraudulent 'MrBeast' giveaway scams. |
| `946841687253213214` | 07/16/2026 | Flagged account reported across community mod teams for unauthorized solicitation. |
| `1484769295232794674` | 07/02/2026 | Automated bot account spamming fraudulent gambling service promotions. |
| `696257474420015114` | 06/23/2026 | Rogue or unauthorized bot account operating maliciously in shared community servers. |
| `1498951849493921943` | 06/04/2026 | Scam account ('@mike_heleket') conducting unauthorized outreach in direct messages. |
| `1340331428738502787` | 05/29/2026 | Compromised account flagged for persistent spam distribution. |
| `657811008550600705` | 06/06/2023 | Cross-server harasser removed from multiple communities for severe unprovoked abuse. |
| `353807196087386113` | 05/15/2023 | Severe raid account posting explicit violence and shock media into public channels. |
| `989603040237584426` | 06/27/2022 | Scam account conducting direct outreach to recruit members into financial carding fraud. |
| `887491471828209684` | 09/15/2021 | Compromised account immediately distributing spam upon entering server channels. |

---

## License

This work is dedicated to the public domain under the [Creative Commons CC0 1.0 Universal License](LICENSE). Anyone may freely use, copy, modify, and distribute this list without restriction.
