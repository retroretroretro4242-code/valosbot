
import discord
from discord.ext import commands
from discord import app_commands

class Tournaments(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.participants = []

    @app_commands.command(name="tournament_create", description="Create a tournament")
    async def tournament_create(self, interaction: discord.Interaction, name: str):

        self.participants.clear()

        embed = discord.Embed(
            title="Tournament Created",
            description=f"{name} tournament started. Join with /tournament_join",
            color=discord.Color.gold()
        )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="tournament_join", description="Join tournament")
    async def tournament_join(self, interaction: discord.Interaction):

        if interaction.user.id not in self.participants:
            self.participants.append(interaction.user.id)

        await interaction.response.send_message("Joined tournament.")

async def setup(bot):
    await bot.add_cog(Tournaments(bot))
