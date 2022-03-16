from ChatbotAPI.chatbasics import sendmsg, chatbotsetup  
import os
from dotenv import load_dotenv
load_dotenv()

key=os.environ['BRAINSHOP']
chatbotsetup(159615,key)  
 
import discord
import random
import asyncio
from discord.ext.commands import bot
from discord.utils import get
from discord.ext import commands, tasks

bot_channel=[
    953615954447843368
]

intents = discord.Intents.default() 
intents.members = True
intents = intents.all()

client=commands.Bot(command_prefix="`", intents=intents)
client.remove_command('help')
status=['Instagram','Facebook','Reddit',"twitter"]

@client.event
async def on_ready():
  change_status.start()
  print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.channel.id not in bot_channel:
       return
    text = message.content.lower().strip()
    if message.author == client.user:
        return
    data = sendmsg(text)
    await client.process_commands(message)  
    async with message.channel.typing():
        await asyncio.sleep(2)
    await message.reply(data) 
    

@tasks.loop(seconds=2)
async def change_status():
  await client.change_presence(activity=discord.Game(random.choice(status)))

client.run(os.environ['DISCORD_TOKEN'])