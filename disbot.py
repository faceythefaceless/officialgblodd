import discord
from discord.ext import commands
import asyncio
import random


#id = 559935882858070027

TOKEN = 'NTU5OTM3MjMxOTc3MTg1MzAz.D3sqbw.7_SY7UgyoycIWss-s8Z8Tinynh0'
client = commands.Bot(command_prefix="-")
client.remove_command("help")

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(f"Hey, {member.mention} Welcome to the Server  :tada::hugging: !")
    roles = discord.utils.get(member.guild.roles, name="Gorkhalis")
    await member.add_roles(roles)


@client.event
async def on_message(message):
    id = client.get_guild(559935882858070027)
    channels = ["gorkhali-commands"]

    if str(message.channel) in channels:
        if message.content.find("-origin") != -1:
            await message.channel.send(f"""A Gorkhali Bot , A New Bot , Made By @Facey 一般 (Faceless)#5423!! , Jai Nepal! 🇳🇵✔ """)
        elif message.content == "-8ball":
            await message.channel.send(f"""This Command is Being Developed By @Facey 一般 (Faceless)#5423 !!""")
        elif message.content == "-developer":
            await message.channel.send(f"""This Bot was developed by @Facey 一般 (Faceless)#5423""")
        elif message.content == "-help":
            await message.channel.send(f"""Gorkhali Blood has 5 commands. :ballot_box_with_check: 
- help
- origin
- prefix
- 8ball
- developer
- info
- alex""")
        elif message.content == "prefix":
            await message.channel.send(f"""The Prefix of @Gorkhali Blood; 🇳🇵✔#0053 is : ( - )""")
        elif message.content == "-info":
            await message.channel.send(f"""Gorkhali Blood is a discord bot made by @Facey 一般 (Faceless)#5423 in Python! It can be used to greet new users and chat when the owner is not available.

It can be used to have fun using - developer and - 8ball commands.

Discord Link https://discord.gg/Uew29B

Visit @Facey 一般 (Faceless)#5423 Discord : https://discord.gg/Uew29B

Commands: - developer: Tells about developer : prefix ( Tells User What the Prefix is ) , - info ( Shares info of the Bot with the user! )

Other commands: - origin , - 8ball ( Still Developing )

I Am Still Learning Coding! :D""")

@client.command()
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

client.run(TOKEN)
