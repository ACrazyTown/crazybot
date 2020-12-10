import discord
import os
import crazycommands
from platform import python_version

intents = discord.Intents.all()
client = discord.Client(intents=intents)
botpfp = "https://cdn.discordapp.com/avatars/679783761247731729/e985affe9ddb2090a1465c11a765c6b9.jpg"
p = "crazy"
py_ver = python_version()
v = "1.0_dev"

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="me screaming"))
    print("=" * 25)
    print(f"I am {client.user}, and my prefix is {p}")
    print(f"I am running Python {py_ver} and my version is {v}")
    print("=" * 25)

@client.event
async def on_member_join(member):
    channel = client.get_channel(619268114357682247)
    role = discord.utils.get(member.guild.roles, name="Citizens")
    mention = member.mention
    await member.add_roles(role)
    await channel.send(f":arrow_right: **{mention}** welcome to The Crazy Town.")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(619268114357682247)
    mention = str(member)
    await channel.send(f":arrow_left: **{mention}** has escaped Brazi- I mean has left The Crazy Town. ")

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

    if msg.startswith(f"{p} yomama") or msg.startswith(f"{p} yomomma") or msg.startswith(f"{p} yourmother") or msg.startswith(f"{p} yourfemaleparent"):
        await crazycommands.yomama(message, botpfp)

    if msg.startswith(f"{p} debug info"):
        await crazycommands.dbg_info(message, py_ver, p, v, client.user, botpfp)
    
client.run(os.environ["TOKEN"])
