import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

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

@client.event
async def setup_hook():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        await client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded Cog: {filename[:-3]}")
    else:
        print("Unable to load pycache folder.")
        
# bot token
client.run(discord_token)  
