import discord
import os
import crazycommands
from platform import python_version

client = discord.Client()
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
    role = discord.utils.get(member.server.roles, id="619274812199534593")
    mention = member.mention
    await client.add_roles(member, role)
    await channel.send(f"{mention} joined the game")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(619268114357682247)
    mention = str(member)
    await channel.send(f"{mention} left the game")

@client.event
async def on_message(message):
    msg = message.content.lower()
    #if message.author == client.user:
        #return

    if msg.startswith(f"{p} vibecheck"):
        await crazycommands.vibecheck(message)
        
    if msg.startswith(f"{p} getsomefreemoney"):
        await crazycommands.getsomefreemoney(message)
    
client.run(os.environ["TOKEN"])
