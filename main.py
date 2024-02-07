import discord
import os

bot = discord.Bot(intents=discord.Intents.all(),)

discord_token = os.environ.get('DISCORD_TOKEN')

@bot.event
async def on_ready():
	await bot.change_presence(
	    status=discord.Status.online,
	    activity=discord.Game(name="Now with slash commands (/)"))

# load cogs
extensions = [
    'cogs.probs',
    'cogs.ping',
    'cogs.multiGogeta',
    'cogs.multiBroly'
]

# import cogs from the folder
if __name__ == '__main__': 
    for extension in extensions:
        bot.load_extension(extension)
        
# bot token
bot.run(discord_token)  
