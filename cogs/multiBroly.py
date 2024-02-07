import discord
import random
from discord.ext import commands
from discord.commands import slash_command

summon_animations = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_broly = [
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1028020_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1028220_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1027200_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1025710_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1024810_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1022360_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1019970_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1018600_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1018630_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1015990_thumb.png"
]

random_ssr_broly = [
    "<:SSR_eclair:971672682712141844>"
]

sr_broly = [
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1002470_thumb.png",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

class multiBroly(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


  #Comandos del bot
  @slash_command(name="multibroly", description="Multisummon 9th Anniversary event (Broly) [Dokkan festival]")
  async def multiBroly(self, ctx: discord.ApplicationContext):
    await ctx.respond("**Starting multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 points")
    await ctx.send("<:SSR_eclair:971672682712141844> Not featured - 2 points")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 point")
    await ctx.send(random.choice(summon_animations))
    points = 0
    for i in range(0, 9):
            number = random.randint(1, 10000)
            if number >= 9300:
                random2 = random.choice(featured_ssr_broly)
                await ctx.send(random2)
                points = points + 3
            elif number >= 9000:
                await ctx.send(random.choice(random_ssr_broly))
                points = points + 2
            elif number >= 3000:
                await ctx.send(random.choice(sr_broly))
                points = points + 1
            else:
                await ctx.send("<:R_eclair:971673105024045056> Random")  
    await ctx.send(random.choice(featured_ssr_broly))
    points = points + 3
    await ctx.send(f"Total points: {points}")
    await ctx.send("**Multisummon finished**")


def setup(bot):
	bot.add_cog(multiBroly(bot))