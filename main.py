import discord
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(f"Bot is online {bot.user.name}")
  try:
    synced = await bot.tree.sync()
    print(f"synced {len(synced)} commands")
  except Exception as e:
    print(f"{e}


bot.run("")
