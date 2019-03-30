import discord
import asyncio
import random
import aiohttp
import time
import datetime
import json
import urllib.request
import os
import sys
from discord.ext import commands
from discord import Game
from discord.voice_client import VoiceClient
from discord.ext.commands import Bot
from random import randint
from discord import Permissions

Client = discord.Client()
bot = commands.Bot(command_prefix=('gblood ', '-'),
          description= 'Hi I am **Gorkhali Blood**!\n\n**Gorkhali Blodd** can talk to you!\nIt greets new users.\n\n**Discord Support Server**__\nhttps://discord.gg/U9VcvHp')
                   

start_time = time.time()
starttime2 = time.ctime(int(time.time()))

def user_is_me(ctx):
    return ctx.message.author.id == "552034006187769865"

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    await bot.process_commands(message)
    author = message.author
    if message.author == bot.user:
        return
    if message.author.bot:
        return

    if message.content.startswith("-repeat"):
        await bot.delete_message(message)
    if 'how are you' in message.content.lower():
        msg = 'I am fine, What about you? {0.author.mention}?'.format(message)
        await bot.send_message(message.channel, msg)

    if 'who are you' in message.content.lower():
        msg = 'I am Gorkhali Blood Bot.'.format(message)
        await bot.send_message(message.channel, msg)
    
    if 'good afternoon' in message.content.lower():
        msg = 'Good afternoon {0.author.mention}. Hope you are experiencing a nice day! :hugging: '.format(message)
        await bot.send_message(message.channel, msg)
        
    if 'good evening' in message.content.lower():
        msg = 'Good evening {0.author.mention}. How did your day go? :hugging: '.format(message)
        await bot.send_message(message.channel, msg)
        
    if 'good morning' in message.content.lower():
        msg = 'Good morning {0.author.mention}. Hope you have an awesome day! :hugging: '.format(message)
        await bot.send_message(message.channel, msg)
        
    if 'good night' in message.content.lower():
        msg = 'Good night, Sweet Dreams {0.author.mention}. Sleep Well! :hugging: '.format(message)
        await bot.send_message(message.channel, msg)
    
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'hi' in message.content.lower():
            msg = 'Hello {0.author.mention}'.format(message)
            await bot.send_message(message.channel, msg)
        
        if 'hello' in message.content.lower():
            msg = 'Hello {0.author.mention}'.format(message)
            await bot.send_message(message.channel, msg)
        
        if 'spam' in message.content.lower():
            msg_to_send = 10
            while msg_to_send > 0:
                msg_to_send = msg_to_send - 1
                msg = '''I am Gorkhali Blood Bot.'''.format(message)
                await bot.send_message(message.channel, msg)
                await asyncio.sleep(1)
            return
        if 'bye' in message.content.lower():
            msg = 'Bye Bye , See You Soon :wave::skin-tone-1: {0.author.mention}. :hugging: '.format(message)
            await bot.send_message(message.channel, msg)
        if 'gm' in message.content.lower():
            msg = 'Good morning {0.author.mention}. Hope you have an awesome day! :hugging: '.format(message)
            await bot.send_message(message.channel, msg)
        if 'gn' in message.content.lower():
            msg = 'Good night, Sweet Dreams {0.author.mention}. Sleep Well! :hugging: '.format(message)
            await bot.send_message(message.channel, msg)
        if 'help' in message.content.lower():
            msg = 'Send **`-help`** to see the available commands.'
            await bot.send_message(message.channel, msg)
        
        if 'khaja' in message.content.lower():
            msg = 'Sorry {0.author.mention}, I do not eat. '.format(message)
            await bot.send_message(message.channel, msg)
        if 'khana' in message.content.lower():
            msg = 'Sorry {0.author.mention}, I do not eat. '.format(message)
            await bot.send_message(message.channel, msg)
        if 'love' in message.content.lower():
            msg = '{0.author.mention}, I will love you until you are in **EchoZONE**. :heart_eyes: :hugging: '.format(message)
            await bot.send_message(message.channel, msg)
        if 'playlist' in message.content.lower():
            msg = '**Global Top 50:** https://www.youtube.com/playlist?list=PL8cV2deJEZLGsrT9z5wq101gnXXvwrSwe\n**Spanish:** https://www.youtube.com/playlist?list=PL8cV2deJEZLH3MqOgKunS4IqHtjgORutm'.format(message)
            await bot.send_message(message.channel, msg)
        if 'gender' in message.content.lower():
            msg = 'Sorry {0.author.mention}, I am a bot. '.format(message)
            await bot.send_message(message.channel, msg)
        if 'k cha' in message.content.lower():
            msg = 'thik xa {0.author.mention}, tmro k xa? '.format(message)
            await bot.send_message(message.channel, msg)
        if 'k 6' in message.content.lower():
            msg = 'thik xa {0.author.mention}, tmro k xa? '.format(message)
            await bot.send_message(message.channel, msg)
        if 'k chha' in message.content.lower():
            msg = 'thik xa {0.author.mention}, tmro k xa? '.format(message)
            await bot.send_message(message.channel, msg)
        if 'k xa' in message.content.lower():
            msg = 'thik xa {0.author.mention}, tmro k xa? '.format(message)
            await bot.send_message(message.channel, msg)
        if 'sanchai' in message.content.lower():
            msg = 'sanchai xu {0.author.mention} :smile: '.format(message)
            await bot.send_message(message.channel, msg)
        if 'k gardai' in message.content.lower():
            msg = '{0.author.mention}, ma yetikai basiraxu, tmi? :smile: '.format(message)
            await bot.send_message(message.channel, msg)
        if 'hate' in message.content.lower():
            msg = 'No, I love you, {0.author.mention} :cry: :hugging: '.format(message)
            await bot.send_message(message.channel, msg)
               

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="Gorkhali Blood server", type=3))

@bot.event
async def on_member_join(member):
    for channel in member.server.channels:
        if 'welcome' in channel.name:
            await bot.send_message(channel,'Hey ' + str(member.mention) + ', welcome to **' + str(member.server) + '**! :tada: :hugging: ')
    newUserMessage = 'Hey ' + str(member.mention) +', welcome to **' + str(member.server) + '**!  :tada:  :hugging: '
    print("Recognised that a member called " + member.name + " joined")
    await bot.send_message(member, newUserMessage)
    print("Sent message to " + member.name)
         
    if member.server == '559935882858070027':
          role = discord.utils.get(member.server.roles, name="Gorkhalis")
          await bot.add_roles(member, role)
          print("Added role '" + role.name + "' to " + member.name)

@bot.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if 'welcome' in channel.name:
            await bot.send_message(channel, '**' + member.mention + '** just left.')
    print("Recognized that " + member.name + " left")
    print("Sent message to #CHANNEL")
                    
@bot.command()
async def helpme():
    await bot.say("**Gorkhali Blood** can talk to you! It can send a message on user join or leave to a text channel which contains 'welcome'. It also sends a welcome Direct Message to the user. It also assigns the users with role 'Gorkhalis' if the role already exists.\n\n__**Discord Support Server**__\nhttps://discord.gg/U9VcvHp\n\n__**Commands:**__\n**`-greet <mentiom user>`**: Greets user\n**`-punch <mention user>`**: Punches a User\n**`-coinflip`**: does a coinflip \n**`-jiugare <mention user>`**: Gives Respect To the user (Neplai language)\n**`-kiss <mention user>`**: kisses a user")

@bot.command()
async def greet(user):
        """Greets mentioned user"""
        await bot.say("Hello, I Was Waiting For You "+ user + " :love_letter:  :hugging: ")
          
@bot.command()
async def coinflip():
          choices = ["Heads", "Tails"]
          rancoin = random.choice(choices)
          await bot.say(rancoin)
          
@bot.command()
async def jiugare(user):
        """It Gives Respect to mentioned user"""
        await bot.say("Jiu Gare Hai!, La Khai Ashirwad Pani Dinu "+ user + " :heart: ")                                                                                                                                                                     

@bot.command()
async def kiss(user):
          """It Gives A Kiss to mentioned user"""
          await bot.say(" What did i just see! " " :see_no_evil:" )
 
@bot.command()
async def punch(user):
          """ It Punches A User"""
          await bot.say(" You Got Punched In Face! "+ user + " :punch: :dizzy_face:  ")
                                              
bot.run(os.environ['BOT_TOKEN'])
