
import discord
from discord.ext import commands
from discord import app_commands

class Matches(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="report_match", description="Report a match result")
    async def report_match(self, interaction: discord.Interaction, winner_id: int):

        team = self.bot.db.get_team(interaction.user.id)

        if not team:
            await interaction.response.send_message("You don't own a team.", ephemeral=True)
            return

        current_elo = team[2]
        new_elo = current_elo + 25

        self.bot.db.update_elo(interaction.user.id, new_elo)

        embed = discord.Embed(
            title="Match Result",
            description=f"ELO increased to {new_elo}",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Matches(bot))
