# Discord Moderation Threat Intelligence & Banlist

Curated blocklist of malicious Discord user IDs, scam bots, and raid accounts for cross-server security.

## Raw Endpoints

- **Plain text list (one ID per line):**
  ```text
  https://raw.githubusercontent.com/<YOUR_USERNAME>/<REPO_NAME>/main/banlist.txt
  ```
- **Structured JSON feed:**
  ```text
  https://raw.githubusercontent.com/<YOUR_USERNAME>/<REPO_NAME>/main/banlist.json
  ```

## Quick Bot Integration Examples

### Bash / cURL loop
```bash
curl -s https://raw.githubusercontent.com/<YOUR_USERNAME>/<REPO_NAME>/main/banlist.txt | while read -r id; do
  echo "Banning ID: $id"
  # e.g., trigger moderation bot ban endpoint
done
```

### Python (discord.py)
```python
import urllib.request

URL = "https://raw.githubusercontent.com/<YOUR_USERNAME>/<REPO_NAME>/main/banlist.txt"
with urllib.request.urlopen(URL) as response:
    banned_ids = {line.strip() for line in response.read().decode().splitlines() if line.strip()}

@bot.event
async def on_member_join(member):
    if str(member.id) in banned_ids:
        await member.ban(reason="Known malicious account on cross-server blocklist")
```

## Active Reported Accounts (64 IDs)

| Discord ID | Reported By | Date Reported | Notes / Reason |
| :--- | :--- | :--- | :--- |
| `1023079001985663126` | tslayr82 | 10/04/2026 3:40 PM | 1023079001985663126 |
| `1068874695702761482` | jfromthebay | 10/08/2026 1:35 PM | 1068874695702761482 |
| `1110476666192535653` | edynn | 10/04/2026 9:21 PM | Not sure if any of you have issues with this user, but by his own admission, he keeps getting banned from PC hardware... |
| `1144325061654888649` | tslayr82 | 10/09/2026 7:00 PM | 1144325061654888649 1430353021946040410 1287854594482901005 1533229968656568393 |
| `1196850086953631755` | byokugen | 10/04/2026 2:45 PM | <1196850086953631755> (jonatan0576) and another mr beast crypto scam 🙂 |
| `1197253997543825521` | edynn | 10/04/2026 9:21 PM | Not sure if any of you have issues with this user, but by his own admission, he keeps getting banned from PC hardware... |
| `1226567367941689536` | jfromthebay | 08/23/2026 8:42 PM | 1226567367941689536 |
| `1242212409498927220` | mrroomba | 10/17/2026 2:06 PM | 1242212409498927220 |
| `1283321787341340744` | bilko | 10/04/2026 9:27 PM | agdagfda / 1505223386199232674 Account Deleted / 1383608829379346525 hell706 / 1283321787341340744 Those are the ones... |
| `1286838349335629906` | mrroomba | 10/02/2026 4:48 PM | 1286838349335629906 |
| `1287854594482901005` | tslayr82 | 10/09/2026 7:00 PM | 1144325061654888649 1430353021946040410 1287854594482901005 1533229968656568393 |
| `1287882355251478550` | mrroomba | 10/01/2026 7:21 AM | 1287882355251478550 |
| `1313451022491848764` | jfromthebay | 10/19/2026 3:05 PM | 1313451022491848764 |
| `1313958539773087845` | brutus.tech | 10/04/2026 11:57 PM | lenoirsx_ 1313958539773087845 |
| `1340331428738502787` | jfromthebay | 05/29/2026 12:00 PM | 1340331428738502787 |
| `1351938127530430536` | brutus.tech | 10/04/2026 11:56 PM | v3nk_i 1426974684834041971 matthewandre_x 1351938127530430536 |
| `1369678199201730602` | edynn | 10/04/2026 9:21 PM | Not sure if any of you have issues with this user, but by his own admission, he keeps getting banned from PC hardware... |
| `1373356582657589398` | mrroomba | 10/17/2026 1:49 AM | 1373356582657589398 |
| `1383608829379346525` | bilko | 10/04/2026 9:27 PM | agdagfda / 1505223386199232674 Account Deleted / 1383608829379346525 hell706 / 1283321787341340744 Those are the ones... |
| `1395449757371076628` | mrroomba | 09/03/2026 10:47 AM | 1395449757371076628 Ai firm scam bot account |
| `1400825354435821730` | byokugen | 10/04/2026 3:23 AM | <1400825354435821730> (vstromakias7) standard crypto scam |
| `1414752214051721348` | edynn | 10/04/2026 9:21 PM | Not sure if any of you have issues with this user, but by his own admission, he keeps getting banned from PC hardware... |
| `1426974684834041971` | edynn | 10/04/2026 11:59 PM | Here's another alt we have: 1426974684834041971 v3nk_i But realistically, trying to hunt down his alts is rather poin... |
| `1430353021946040410` | tslayr82 | 10/09/2026 7:00 PM | 1144325061654888649 1430353021946040410 1287854594482901005 1533229968656568393 |
| `1436422427142787243` | edynn | 10/04/2026 9:21 PM | Not sure if any of you have issues with this user, but by his own admission, he keeps getting banned from PC hardware... |
| `1456722209656803483` | bilko | 10/04/2026 9:06 PM | Underage (and quite racist) user: 1456722209656803483 |
| `1484769295232794674` | jfromthebay | 07/02/2026 10:20 PM | 1484769295232794674 |
| `1490501890109341919` | jfromthebay | 08/21/2026 10:34 PM | 1490501890109341919 |
| `1492875609372885052` | jfromthebay | 09/30/2026 1:30 PM | 1492875609372885052 |
| `1498951849493921943` | mrroomba | 06/04/2026 7:36 AM | User ID: @mike_heleket (1498951849493921943) |
| `1504087093528231996` | bilko | 09/01/2026 2:55 AM | 1504087093528231996 Underage user, joined our server and Intel <@306899600382492673> |
| `1505223386199232674` | bilko | 10/04/2026 9:27 PM | agdagfda / 1505223386199232674 Account Deleted / 1383608829379346525 hell706 / 1283321787341340744 Those are the ones... |
| `1507457811381096458` | tslayr82 | 10/07/2026 11:22 AM | 1507457811381096458 |
| `1519707665096507621` | d2ultima | 10/03/2026 11:06 AM | 1519707665096507621 name scam |
| `1523754110409637980` | jfromthebay | 10/08/2026 1:11 AM | 1523754110409637980 |
| `1533229968656568393` | tslayr82 | 10/09/2026 7:00 PM | 1144325061654888649 1430353021946040410 1287854594482901005 1533229968656568393 |
| `1537455244928221206` | mrroomba | 09/04/2026 11:31 AM | 1537455244928221206 |
| `1545981820649218090` | mrroomba | 09/11/2026 11:44 PM | 1545981820649218090 |
| `1546840214960607243` | mrroomba | 09/08/2026 4:24 PM | 1546840214960607243 Job listing bot |
| `1551464928248856607` | watermelonkirbs | 10/15/2026 1:33 PM | 1556010033479815328 1313451022491848764 1555629557510447115 1551464928248856607 Joined at the same time to advertise ... |
| `1555337843235102885` | jfromthebay | 10/01/2026 11:45 PM | 1555337843235102885 |
| `1555525351914999866` | jfromthebay | 10/04/2026 3:20 AM | 1555525351914999866 |
| `1555629557510447115` | watermelonkirbs | 10/15/2026 1:33 PM | 1556010033479815328 1313451022491848764 1555629557510447115 1551464928248856607 Joined at the same time to advertise ... |
| `1556010033479815328` | watermelonkirbs | 10/15/2026 1:33 PM | 1556010033479815328 1313451022491848764 1555629557510447115 1551464928248856607 Joined at the same time to advertise ... |
| `1561031456392876142` | jfromthebay | 10/18/2026 4:06 PM | 1561031456392876142 |
| `340714404314349570` | byokugen | 10/05/2026 2:51 PM | kyotorun50 <340714404314349570> Another crypto scam |
| `353807196087386113` | mzgszm | 05/15/2023 10:31 AM | Just gonna share this user id: 353807196087386113 They joined another server I moderate to post a gif of someone shoo... |
| `400896526924251136` | mrroomba | 10/03/2026 10:34 AM | 400896526924251136 |
| `406620720437788674` | jfromthebay | 09/29/2026 2:07 PM | 406620720437788674 |
| `484765847546626068` | mrroomba | 10/19/2026 1:30 PM | 484765847546626068 |
| `490188321226620928` | byokugen | 10/06/2026 12:51 PM | <490188321226620928> (danishgtr) And another crypto |
| `657811008550600705` | gaugeprower | 06/06/2023 9:05 PM | Heads up Mod teams, we have a user joining multiple large tech servers and getting high level nasty, un provoked. I u... |
| `687933479622934620` | byokugen | 10/06/2026 3:49 AM | <687933479622934620> (4m4y4s) and another one 🙂 |
| `696257474420015114` | mrroomba | 06/23/2026 11:42 PM | <@111798505042939904> 696257474420015114 Bot in your server |
| `704031430325436537` | mrroomba | 10/19/2026 1:31 PM | 704031430325436537 |
| `751903171198189618` | smokcat | 10/12/2026 2:43 PM | anyone know a <@751903171198189618> `751903171198189618`? they seem to have a psychotic break, troll, other mental is... |
| `797391110900285441` | jfromthebay | 08/23/2026 5:39 PM | 797391110900285441 |
| `855443094870687794` | awervekov | 10/04/2026 7:22 AM | Watch out for 855443094870687794 |
| `887491471828209684` | madben65 | 09/15/2021 2:35 PM | 887491471828209684 just joined watercooling |
| `936358065207390238` | mrroomba | 09/11/2026 11:49 AM | 936358065207390238 |
| `938710016289046608` | brutus.tech | 10/12/2026 3:36 PM | 938710016289046608 / `f0rgotte1n` - spam invites to sex-related discord server |
| `946841687253213214` | jfromthebay | 07/16/2026 8:43 PM | User ID: 946841687253213214 |
| `953748748280946730` | edynn | 10/04/2026 11:53 PM | Have not. For those curious, he's some unemployed vibe coder with endless time to yap about his world views, more or ... |
| `989603040237584426` | rohzino | 06/27/2022 3:33 PM | Newegg mods - got a scammy scam for you. 989603040237584426 - has “recruited” me for an online carding scheme. Seems ... |

## Contributing / Adding New Reports

1. Click on `banlist.txt` or `banlist.json` in GitHub.
2. Click the ✏️ **Edit this file** button in the top right.
3. Add the new Discord snowflake ID.
4. Commit changes with a descriptive message (e.g. `feat: add spam bot 12345...`).

## License

This work is dedicated to the public domain under the [Creative Commons CC0 1.0 Universal License](LICENSE). Anyone may freely use, copy, modify, and distribute this list without restriction.
