import discord
import Birdies
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import time
from keep_alive import keep_alive
NEW_NICKNAME = Birdies.generate_bird_name()
print(NEW_NICKNAME)

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

keep_alive()

handler = logging.FileHandler(filename='bird.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def givebird(ctx):
    await ctx.send(f"Tweet Tweet! A {Birdies.generate_bird_name()} flew by!")

@bot.event
async def on_member_join(member):
    NEW_NICKNAME=Birdies.generate_bird_name()
    try:
            await member.edit(nick={NEW_NICKNAME})
            print(f"Renamed {member.name} to {NEW_NICKNAME}")
    except discord.Forbidden:
            print(f"Missing permissions to change nickname for {member.name}")
    except discord.HTTPException as e:
            print(f"Failed to rename user: {e}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)


while True:
    keep_alive()
    time.sleep(5)
