import os
import discord
from discord.ext import commands
from database import Database

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = False

bot = commands.Bot(command_prefix="!", intents=intents)
bot.db = Database()

COGS = [
    "cogs.teams",
    "cogs.matches",
    "cogs.tournaments",
    "cogs.leaderboard",
    "cogs.admin"
]

@bot.event
async def on_ready():
    print(f"✅ {bot.user} aktif!")

    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"✔️ {cog} yüklendi")
        except Exception as e:
            print(f"❌ {cog} yüklenemedi: {e}")

    try:
        await bot.tree.sync()
        print("⚡ Slash komutlar sync edildi!")
    except Exception as e:
        print(f"⚠️ Slash komut sync hatası: {e}")

bot.run(TOKEN)
