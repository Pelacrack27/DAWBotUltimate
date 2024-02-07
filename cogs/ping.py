import discord
from discord.commands import slash_command
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name='ping',description='Returns the latency of the bot')
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"pong! ({self.bot.latency*1000:.2f} ms)")

def setup(bot):
    bot.add_cog(ping(bot))