
import discord
from discord.ext import commands
from discord import app_commands

class Teams(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="team_create", description="Create a team")
    async def team_create(self, interaction: discord.Interaction, name: str):

        if self.bot.db.get_team(interaction.user.id):
            await interaction.response.send_message("You already have a team.", ephemeral=True)
            return

        self.bot.db.create_team(interaction.user.id, name)

        role = await interaction.guild.create_role(name=name)
        await interaction.user.add_roles(role)

        embed = discord.Embed(
            title=f"{name} created",
            description="Team successfully created.",
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="team_delete", description="Delete your team")
    async def team_delete(self, interaction: discord.Interaction):

        team = self.bot.db.get_team(interaction.user.id)

        if not team:
            await interaction.response.send_message("No team found.", ephemeral=True)
            return

        self.bot.db.delete_team(interaction.user.id)

        await interaction.response.send_message("Team deleted.")

async def setup(bot):
    await bot.add_cog(Teams(bot))
