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
          description= 'Hi I am **Gorkhali Bot**!\n\n**Gorkhali Blodd** can talk to you!\nIt greets new users.\n\n**Discord Support Server**__\nhttps://discord.gg/U9VcvHp')
                   

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
    await bot.change_presence(game=discord.Game(name="Gorkhali Server", type=3))

@bot.event
async def on_member_join(member):
    for channel in member.server.channels:
        if 'welcome' in channel.name:
            await bot.send_message(channel,'Hey ' + str(member.mention) + ', welcome to **' + str(member.server) + '**! :tada: :hugging: ')
    newUserMessage = 'Hey ' + str(member.mention) +', welcome to **' + str(member.server) + '**!  :tada:  :hugging: '
    print("Recognised that a member called " + member.name + " joined")
    await bot.send_message(member, newUserMessage)
    print("Sent message to " + member.name)
         
@bot.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if 'welcome' in channel.name:
            await bot.send_message(channel, '**' + member.mention + '** just left.')
    print("Recognized that " + member.name + " left")
    print("Sent message to #CHANNEL")
                    
@bot.command()
async def helpme():
    await bot.say("**Gorkhali Bot** can talk to you! It can send a message on user join or leave to a text channel which contains 'welcome'. It also sends a welcome Direct Message to the user. It also assigns the users with role 'Gorkhalis' if the role already exists.\n\n__**Discord Support Server**__\nhttps://discord.gg/U9VcvHp\n\n__**Commands:**__\n**`-greet <mentiom user>`**: Greets user\n**`-punch <mention user>`**: Punches a User\n**`-coinflip`**: does a coinflip \n**`-jiugare <mention user>`**: Gives Respect To the user (Nepali language)\n**`-kiss <mention user>`**: kisses a user\n**`-hug <member mention>`**: Hugs A User\n**`-slap <member mention>`**: Slaps A User\n**`-headpat <member mention>`**: Headpats A User\n**`-stare <member mention>`**: Stares At The User\n**`-love <member mention>`**: Says I love You\n**`-marry <mention user>`**: Get Married With A User\n**`-dumb <member mention>`**: Says Dumb To A User\n**`-ashirwad <member mention>`**: Get Ashirwad from user\n**`-qball <question>`**: Answers a Question Given By The User\n**`-pranam <member nebtion>`**: Gives Pranam To A User\n**`-insult <member mention>`**: Insults a User\n**`-praise <member mention>`**: Praises a User")

@bot.command(pass_context=True)
async def greet(ctx, member: discord.Member):
    """Greets someone."""
    await bot.say("{1} Hello, I Was Waiting For You {0}!, :hugging:".format(member.mention, ctx.message.author.mention)) 
          
@bot.command()
async def coinflip():
          choices = ["Heads", "Tails"]
          rancoin = random.choice(choices)
          await bot.say(rancoin)
          
@bot.command(pass_context=True)
async def jiugare(ctx, member: discord.Member):
    """Respects someone."""
    await bot.say("{1} did jiu to {0}!, Khoi Tw Ashirwad?".format(member.mention, ctx.message.author.mention))                                                                                                                                                                  

@bot.command(pass_context=True)
async def kiss(ctx, member: discord.Member):
    """Kisses someone."""
    await bot.say("{1} Kissed {0}! :kiss:".format(member.mention, ctx.message.author.mention))
 
@bot.command(pass_context=True)
async def punch(ctx, member: discord.Member):
    """Punches someone."""
    await bot.say("{1} Punched {0}! :punch: :dizzy_face:".format(member.mention, ctx.message.author.mention))
          
@bot.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    """Slaps someone."""
    await bot.say("{1} slaps {0}! :dizzy_face:".format(member.mention, ctx.message.author.mention))
          
@bot.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    """Hugs someone."""
    await bot.say("{1} Hugged {0}! :hugging:".format(member.mention, ctx.message.author.mention))

@bot.command(pass_context=True)
async def headpat(ctx, member: discord.Member):
    """Hugs someone."""
    await bot.say("{1} Headpatted {0}! :hugging: https://tenor.com/view/anime-pet-gif-9200932".format(member.mention, ctx.message.author.mention))

@bot.command(pass_context=True)
async def stare(ctx, member: discord.Member):
    """Hugs someone."""
    await bot.say("{1} Stared at {0}! :eyes:".format(member.mention, ctx.message.author.mention))    
          
@bot.command(pass_context=True)
async def love(ctx, member: discord.Member):
    """Says i love you to someone"""
    await bot.say("{1} Loves {0}! :heart:".format(member.mention, ctx.message.author.mention))
          
@bot.command(pass_context=True)
async def marry(ctx, member: discord.Member):
    """Get Married to Someone"""
    await bot.say("{1} Got Married With :ring: {0}! :heart:".format(member.mention, ctx.message.author.mention)) 
          
@bot.command(pass_context=True)
async def dumb(ctx, member: discord.Member):
    """Says Dumbass to A User"""
    await bot.say("{1} Said {0} is So Freaking Dumb! :joy:".format(member.mention, ctx.message.author.mention))
                
@bot.command(pass_context=True)
async def ashirwad(ctx, member: discord.Member):
    """Gets Ashirwad from A User"""
    await bot.say("{1} Gave Ashirwad to :raised_hand: {0}".format(member.mention, ctx.message.author.mention))
          
@bot.command(pass_context=True)
async def qball(ctx):
    """Answers an  Question"""
    await bot.say(random.choice(["It is certain :8ball:",
                                 "It is decidedly so :8ball:",
                                 "Without a doubt :8ball:",
                                 "Yes, definitely :8ball:",
                                 "You may rely on it :8ball:",
                                 "As I see it, yes :8ball:",
                                 "Most likely :8ball:",
                                 "Outlook good :8ball:",
                                 "Yes :8ball:",
                                 "Signs point to yes :8ball:",
                                 "Reply hazy try again :8ball:",
                                 "Ask again later :8ball:",
                                 "Better not tell you now :8ball:",
                                 "Cannot predict now :8ball:",
                                 "Concentrate and ask again :8ball:",
                                 "Don't count on it :8ball:",
                                 "My reply is no :8ball:",
                                 "My sources say no :8ball:",
                                 "Outlook not so good :8ball:",
                                  "Very doubtful :8ball:"]))
          
@bot.command(pass_context=True)
async def pranam(ctx, member: discord.Member):
    """Gets Ashirwad from A User"""
    await bot.say("{1} Le {0} Lai Pranam Garyo, Ashirwad Pilich!".format(member.mention, ctx.message.author.mention))
          
@bot.command(pass_context=True)
async def insult(ctx, member: discord.Member):
    """Insults a user"""
    await bot.say(random.choice(["You speak an infinite deal of nothing :8ball:",
                                 "Only dull people are brilliant at breakfast :8ball:",
                                 "You look lousy :8ball:",
                                 "You're awfully small to be so hugely irritating :8ball:",
                                 "No I mean it. You don't look good :8ball:",
                                 "As I see it, you are ugly boi :8ball:",
                                 "Most likely You're Dumb :8ball:",
                                 "The only time you seem honest is when you’re insulting someone! :8ball:",
                                 "You're hair is ridiculous :8ball:",
                                 "Signs point to yes :8ball:",
                                 "You ignorant little slug! :8ball:",
                                 "You spawny-eyed pig-faced wazzock :8ball:"]))
          
@bot.command(pass_context=True)
async def praise(ctx, member: discord.Member):
    """Praises a user"""
    await bot.say(random.choice(["You are more fun than anyone or anything I know, including bubble wrap :8ball:",
                                 "You are the most perfect you there is. :8ball:",
                                 "You are enough. :8ball:",
                                 "You are one of the strongest people I know. :8ball:",
                                 "No I mean it. You don't look good :8ball:",
                                 "You look great today. :8ball:",
                                 "You have the best smile. :8ball:",
                                 "Your outlook on life is amazing. :8ball:",
                                 "You just light up the room.:8ball:",
                                 "Everything seems brighter when you are around :8ball:",
                                 "You really seem to know who you are. I admire that. :8ball:",
                                 "I tell everyone how amazing you are. :8ball:"]))
          
bot.run(os.environ['BOT_TOKEN'])
