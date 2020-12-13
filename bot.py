import discord
import os
import sys
import crazycommands
import json
from platform import python_version
from discord.ext import tasks

with open("data.json", "r") as f:
    token = json.load(f)["TOKEN"]
intents = discord.Intents.all()
client = discord.Client(intents=intents)
botpfp = "https://cdn.discordapp.com/avatars/679783761247731729/fa6d206ad4ee083ef87a487062876570.jpg"
p = "crazy"
py_ver = python_version()
v = "1.0-gittest_1"

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="me screaming"))
    print("=" * 25)
    print(f"I am {client.user}, and my prefix is {p}")
    print(f"I am running Python {py_ver} and my version is {v}")
    print("=" * 25)

@tasks.loop(hours=24)
async def update_24h():
    bot_channel = client.get_channel(619275354049347605)
    await bot_channel.send("I am currently doing my scheduled reboot and will be unavailable for a moment \nPlease check back soon!")
    exit(3)

@client.event
async def on_member_join(member):
    channel = client.get_channel(619268114357682247)
    role = discord.utils.get(member.guild.roles, name="Citizens")
    mention = member.mention
    await member.add_roles(role)
    await channel.send(f":arrow_right: **{mention}** welcome to **The Crazy Town™**.")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(619268114357682247)
    mention = str(member)
    await channel.send(f":arrow_left: **{mention}** has escaped Brazi- I mean has left **The Crazy Town™**. ")

@client.event
async def on_message(message):
    msg = message.content.lower()
    # Check if the message author is the bot.
    if message.author == client.user: 
        return

    if msg.startswith(f"{p} vibecheck"):
        await crazycommands.vibecheck(message, botpfp)
        
    if msg.startswith(f"{p} getsomefreemoney"):
        await crazycommands.getfreemoney(message, botpfp)

    if msg.startswith(f"{p} dadjoke"):
        await crazycommands.dadjoke(message, botpfp)

    if msg.startswith(f"{p} yomama") or msg.startswith(f"{p} yomomma") or msg.startswith(f"{p} yourmother") or msg.startswith(f"{p} yourmom") or msg.startswith(f"{p} yourmomther") or msg.startswith(f"{p} yourfemaleparent"):
        await crazycommands.yomama(message, botpfp)

    if msg.startswith(f"{p} debug info"):
        if len(sys.argv) >= 2:
            overseer = True
        else:
            overseer = False

        await crazycommands.dbg_info(message, py_ver, p, v, client.user, botpfp, overseer)

    if msg.startswith(f"{p} update"):
        # Check if Overseer is active
        if len(sys.argv) >= 2:
            overseer = True
        else:
            overseer = False

        await crazycommands.update(message, botpfp, overseer)

    
client.run(token)
