"""
Discord Mass Ban Automation Script
Reads banlist.txt and preemptively bans all listed IDs from your Discord server.
"""

import os
import sys
import asyncio
import discord

# Path to banlist.txt in the same directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BANLIST_PATH = os.path.join(SCRIPT_DIR, "banlist.txt")

# Auto-load .env if present
env_path = os.path.join(SCRIPT_DIR, ".env")
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

# --- Configuration ---
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "").strip()
GUILD_ID_INPUT = os.getenv("GUILD_ID", "").strip()
BAN_REASON = os.getenv("BAN_REASON", "Malicious account flagged on threat intelligence blocklist")


async def main():
    token = BOT_TOKEN
    guild_id_str = GUILD_ID_INPUT

    if not token:
        token = input("Enter your Discord Bot Token: ").strip()
    if not guild_id_str:
        guild_id_str = input("Enter your Server (Guild) ID: ").strip()

    try:
        guild_id = int(guild_id_str)
    except ValueError:
        print("[!] Error: Server ID must be a number.")
        return

    if not os.path.exists(BANLIST_PATH):
        print(f"[!] Error: Could not find banlist at {BANLIST_PATH}")
        return

    with open(BANLIST_PATH, "r", encoding="utf-8") as f:
        target_ids = [int(line.strip()) for line in f if line.strip() and line.strip().isdigit()]

    print(f"[*] Loaded {len(target_ids)} target IDs from banlist.txt")

    intents = discord.Intents.default()
    # Note: bans intent requires default intents; member list not required for banning by ID
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"\n[+] Connected as: {client.user} (ID: {client.user.id})")
        guild = client.get_guild(guild_id)
        if not guild:
            print(f"[!] Error: Bot is not in a server with ID {guild_id}.")
            print("    Please invite the bot to the server first!")
            await client.close()
            return

        print(f"[+] Target Server: {guild.name}")
        
        # Check permissions
        me = guild.me
        if not me.guild_permissions.ban_members:
            print("[!] Error: Bot does not have 'Ban Members' permission in this server.")
            print("    Please grant the bot a role with 'Ban Members' permission and try again.")
            await client.close()
            return

        print("[*] Fetching existing server bans to avoid redundant requests...")
        existing_bans = set()
        try:
            async for ban_entry in guild.bans(limit=None):
                existing_bans.add(ban_entry.user.id)
            print(f"[+] Found {len(existing_bans)} existing bans in {guild.name}")
        except Exception as e:
            print(f"[-] Could not pre-fetch bans ({e}). Proceeding to ban directly...")

        to_ban = [uid for uid in target_ids if uid not in existing_bans]
        already_banned_count = len(target_ids) - len(to_ban)
        print(f"[*] Accounts to process: {len(to_ban)} ({already_banned_count} already banned)")
        
        if not to_ban:
            print("[+] All accounts in banlist.txt are already banned! Nothing to do.")
            await client.close()
            return

        confirm = input(f"\nAre you sure you want to ban {len(to_ban)} accounts from '{guild.name}'? (y/n): ").strip().lower()
        if confirm != 'y':
            print("[-] Cancelled by user.")
            await client.close()
            return

        print("\n[*] Starting mass ban. Press Ctrl+C at any time to pause/stop...\n")
        
        success_count = 0
        error_count = 0
        total = len(to_ban)

        for idx, user_id in enumerate(to_ban, 1):
            try:
                # discord.Object allows banning any ID preemptively without fetching the user
                await guild.ban(discord.Object(id=user_id), reason=BAN_REASON)
                success_count += 1
                status = "BANNED"
            except discord.NotFound:
                status = "ID_NOT_FOUND"
                error_count += 1
            except discord.Forbidden:
                print(f"\n[!] Permission Error: Bot role hierarchy is too low or permissions were revoked.")
                break
            except discord.HTTPException as e:
                status = f"HTTP_ERR_{e.status}"
                error_count += 1

            # Progress indicator
            percent = (idx / total) * 100
            print(f"[{idx:4d}/{total}] {percent:5.1f}% | ID: {user_id} -> {status}")

            # Sleep to pace requests comfortably within Discord rate limits
            await asyncio.sleep(0.4)

        print(f"\n[+] Finished! Successfully banned: {success_count} | Errors/Skipped: {error_count}")
        await client.close()

    try:
        await client.start(token)
    except discord.LoginFailure:
        print("[!] Login failed: Invalid Bot Token provided.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[-] Stopped by user.")
