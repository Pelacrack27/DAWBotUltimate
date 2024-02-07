import discord
from discord.commands import slash_command
from discord.ext import commands

class probs(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  #Comandos del bot
  @slash_command(name='probs',description='Probabilities of the current multisummons')
  async def probs(self, ctx: discord.ApplicationContext):
    embed=discord.Embed(title="Probabilidades",  description="A continuación se muestran las probabilidades de los banner de SDBH", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,  icon_url=ctx.author.avatar)
    embed.add_field(name="SSR featured:", value="5% <:SSR_eclair:971672682712141844> Featured | 95% <:SSR_eclair:971672682712141844> not featured", inline=False)
    embed.add_field(name="SSR not featured:", value="5% <:SSR_eclair:971672682712141844> Featured | 5% <:SSR_eclair:971672682712141844> not featured | 60% <:SR_eclair:971673046496731166> Random | 30% <:R_eclair:971673105024045056> Random", inline=False)
    embed.set_footer(text="Thank you for using the bot!")
    await ctx.respond(embed=embed)

def setup(bot):
	bot.add_cog(probs(bot))