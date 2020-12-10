import discord
import random
import asyncio

ids = {
    "anthony": 309279430738444288,
    "jan": 252145305825443840,
    "bot": 679783761247731729,
    "admin": 678277218186690599
    }

accent_color = 0x0b8a7c

async def vibecheck(message):
    
    vibecheck_message = ["*You have failed the vibe check.*", "*You have passed the vibe check.*"]
    
    if len(message.mentions) >= 2:
        embed = discord.Embed(title="Vibecheck", description="I can't vibe check all of you...", color=accent_color)
        await message.channel.send(embed=embed)
    elif "yourself" in message.content or 679783761247731729 in [user.id for user in message.mentions]:
        embed = discord.Embed(title="Vibecheck", description="Fool, my vibe is too powerful to be checked.", color=accent_color)
        await message.channel.send(embed=embed)
    elif len(message.mentions) == 1:
        mention = message.mentions[0]
        vb_message_mention = [f"*{mention} has failed the vibe check.*", f"*{mention} has passed the vibe check.*"]
        vibecheck_embed = discord.Embed(title="Vibecheck", description=random.choice(vb_message_mention), color=accent_color)
        vibecheck_embed.set_image(url="https://cdn.discordapp.com/attachments/619275354049347605/770039014094405642/vibecheck.png")
        await message.channel.send(embed=vibecheck_embed)
    else:
        await asyncio.sleep(1.5)
        vibecheck_embed = discord.Embed(title="Vibecheck", description=random.choice(vibecheck_message), color=accent_color)
        vibecheck_embed.set_image(url="https://cdn.discordapp.com/attachments/619275354049347605/770039014094405642/vibecheck.png")
        await message.channel.send(embed=vibecheck_embed)
        
async def getfreemoney(message):
    # Not actually a scam, just a rickroll.
     
    embed = discord.Embed(title="Get some free money!", description=":wave:Hey!:wave: You are qualified to reedeem :money_mouth:thousands:money_mouth: of :moneybag:dollars:moneybag:. Just click this link and get your :moneybag:money:moneybag:!:point_right: <https://bit.ly/getsumfreemoneys>", color=accent_color)
    await message.channel.send(embed=embed)
