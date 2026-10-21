# Discord Bot Automation & Mass Ban Guide

This guide walks you through creating a lightweight, private Discord bot to automatically apply the ban list from `banlist.txt` to your server using the included [`ban_all.py`](ban_all.py) script.

---

## Why Use an Automation Script?

Standard public bots (like Carl-bot or Dyno) require you to manually paste IDs into Discord chat messages, which are capped at **2,000 characters (~90 IDs per message)**. 

The included [`ban_all.py`](ban_all.py) script:
* Reads `banlist.txt` directly from disk.
* Automatically checks existing server bans so it **does not waste time re-banning accounts**.
* Preemptively bans users using raw Discord snowflake IDs (targets do not need to be in your server).
* Built-in rate-limit throttling to keep your bot safely within Discord API limits.
* Displays live progress in your terminal.

---

## Prerequisites

* Python 3.8 or higher installed on your system.
* The `discord.py` library:
  ```bash
  pip install discord.py
  ```

---

## Step 1: Create a Bot on the Discord Developer Portal

1. Log in to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application** in the top right.
3. Give your bot a name (e.g., `Server Sentinel` or `Moderation Guard`) and accept the terms.
4. Navigate to the **Bot** tab in the left sidebar:
   * Click **Reset Token** (and enter your 2FA code if prompted).
   * **Copy the Bot Token** and store it somewhere private. *(Never share this token or commit it to GitHub).*

---

## Step 2: Invite the Bot to Your Server

1. Navigate to **OAuth2** -> **URL Generator** in the left sidebar.
2. Under **SCOPES**, check:
   * `bot`
3. Under **BOT PERMISSIONS** (appears below scopes), check:
   * `Ban Members`
4. Copy the **Generated URL** at the bottom of the page.
5. Paste the URL into your browser, select your Discord server, and click **Authorize**.

> [!IMPORTANT]
> **Role Hierarchy Check:** In your Discord server, go to **Server Settings** -> **Roles**. Ensure your bot's role is positioned **higher** in the role list than standard member roles. Discord prevents bots from banning anyone whose highest role is equal to or above the bot's highest role.

---

## Step 3: Get Your Discord Server ID

1. In Discord, go to **User Settings** -> **Advanced**.
2. Toggle on **Developer Mode**.
3. Right-click your server icon in the left server list and select **Copy Server ID**.

---

## Step 4: Configure and Run the Script

### Option A: Interactive Terminal Prompts (Fastest)
Run the script directly; it will securely prompt you for your Bot Token and Server ID:

```bash
python ban_all.py
```

### Option B: Local `.env` Configuration (Recommended for Repeat Runs)
1. Copy the template `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and fill in your values:
   ```env
   DISCORD_BOT_TOKEN=your_bot_token_here
   GUILD_ID=your_server_id_here
   BAN_REASON=Malicious account flagged on threat intelligence blocklist
   ```
   *(The repository `.gitignore` automatically prevents `.env` from ever being tracked or committed to Git).*
3. Run the script:
   ```bash
   python ban_all.py
   ```

---

## Step 5: Understanding Status Outputs & Error Codes

During execution, the script streams status updates for each account:

| Status Code | Meaning | Action Required |
| :--- | :--- | :--- |
| `BANNED` | Account was successfully banned from the server. | None. Target is blocked. |
| `ID_NOT_FOUND` *(HTTP 404)* | Account does not exist in Discord's global database. | **Safe to ignore.** Occurs when an account was permanently purged by Discord Trust & Safety, or when a human typo occurred in the original report. No user can log into or join with this ID. |
| `HTTP_ERR_400` *(Bad Request)* | Discord rejected the ID as an invalid user object. | **Safe to ignore.** Occurs when an account was terminated/nuked platform-wide by Discord. |
| `HTTP_ERR_503` *(Service Unavailable)* | Discord's backend moderation service or Cloudflare proxy is temporarily congested. | **Temporary server-side hiccup.** Discord was momentarily overloaded writing audit logs. Rerunning the script will catch any IDs that encountered a 503. |
| `HTTP_ERR_429` *(Rate Limited)* | Discord requested the bot pause briefly. | **Handled automatically.** `discord.py` pauses for the requested cooldown and automatically resumes. |
| `Permission Error` *(HTTP 403)* | The bot lacks permission to execute bans. | Verify the bot has the `Ban Members` permission and its role is high enough in the server role hierarchy. |

---

## Updating & Rerunning

When new IDs are added to `banlist.txt`:
1. Pull the latest repository updates:
   ```bash
   git pull origin main
   ```
2. Re-run `python ban_all.py`.
3. The script will automatically skip all previously banned accounts and only process the new additions.
