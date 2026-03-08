
import discord
from discord.ext import commands
from discord import app_commands

class Leaderboard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="leaderboard", description="Show team rankings")
    async def leaderboard(self, interaction: discord.Interaction):

        teams = self.bot.db.all_teams()

        text = ""
        rank = 1

        for name, elo in teams:
            text += f"{rank}. {name} - {elo} ELO\n"
            rank += 1

        embed = discord.Embed(
            title="Team Leaderboard",
            description=text if text else "No teams yet.",
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Leaderboard(bot))
