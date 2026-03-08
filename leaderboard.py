import discord
from discord.ext import commands
from discord import app_commands

class Leaderboard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="leaderboard",
        description="Show team rankings based on ELO"
    )
    async def leaderboard(self, interaction: discord.Interaction):

        teams = self.bot.db.all_teams()

        if not teams:
            await interaction.response.send_message("Henüz takım yok.", ephemeral=True)
            return

        text = ""
        rank = 1

        for name, elo in teams:
            text += f"**{rank}. {name}** - {elo} ELO\n"
            rank += 1

        embed = discord.Embed(
            title="🏆 Team Leaderboard",
            description=text,
            color=discord.Color.blurple()
        )

        embed.set_footer(text="PRX | Prime Raiders")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Leaderboard(bot))
