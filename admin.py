
import discord
from discord.ext import commands
from discord import app_commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="set_elo", description="Admin: set team elo")
    @app_commands.checks.has_permissions(administrator=True)
    async def set_elo(self, interaction: discord.Interaction, owner_id: int, elo: int):

        self.bot.db.update_elo(owner_id, elo)
        await interaction.response.send_message("ELO updated.")

async def setup(bot):
    await bot.add_cog(Admin(bot))
