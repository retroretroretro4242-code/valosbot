import os
import discord
from discord.ext import commands
from database import Database

TOKEN = os.getenv("TOKEN")  # Railway’den gelecek

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)
db = Database()

COGS = [
    "cogs.teams",
    "cogs.matches",
    "cogs.tournaments",
    "cogs.leaderboard",
    "cogs.admin"
]

@bot.event
async def on_ready():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"Loaded {cog}")
        except Exception as e:
            print(f"Failed to load {cog}: {e}")

    await bot.tree.sync()
    print(f"{bot.user} is online and ready!")

bot.db = db

bot.run(TOKEN)
