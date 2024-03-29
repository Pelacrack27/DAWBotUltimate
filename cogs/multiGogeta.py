import discord
import random
from discord.ext import commands
from discord.commands import slash_command

summon_animations = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_gogeta = [
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1027960_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1027270_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1026110_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1024910_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1026800_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1020020_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1019800_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1018980_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1019030_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1016070_thumb.png"
]

random_ssr_gogeta = [
    "<:SSR_eclair:971672682712141844> Random"
]

random_sr_gogeta = [
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1012940_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000030_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000090_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000110_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000850_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000870_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000890_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1001620_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1002130_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1003750_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1004460_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_2000760_thumb.png",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

class multiGogeta(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


  #Comandos del bot
  @slash_command(name="multigogeta", description="Multisummon 9th Anniversary event (Gogeta) [Carnival]")
  async def multiGogeta(self, ctx: discord.ApplicationContext):
    await ctx.respond("**Starting multisummon:**")
    await ctx.respond("<:SSR_eclair:971672682712141844> Featured - 3 points")
    await ctx.respond("<:SSR_eclair:971672682712141844> Not featured - 2 points")
    await ctx.respond("<:SR_eclair:971673046496731166>  - 1 point")
    await ctx.respond(random.choice(summon_animations))
    points = 0
    for i in range(0, 9):
            number = random.randint(1, 10000)
            if number >= 9300:
                random2 = random.choice(featured_ssr_gogeta)
                await ctx.respond(random2)
                points = points + 3
            elif number >= 9000:
                await ctx.respond(random.choice(random_ssr_gogeta))
                points = points + 2
            elif number >= 3000:
                await ctx.respond(random.choice(random_sr_gogeta))
                points = points + 1
            else:
                await ctx.respond("<:R_eclair:971673105024045056> Personaje kk")  
    await ctx.respond(random.choice(featured_ssr_gogeta))
    points = points + 3
    await ctx.respond(f"Total points: {points}")
    await ctx.respond("**Multisummon finished**")


async def setup(client):
    await client.add_cog(multiGogeta(client))
