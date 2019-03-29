import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if 'hello' in message.content.lower():
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if 'how are you' in message.content.lower():
        msg = 'I am fine. What about you, {0.author.mention}?'.format(message)
        await client.send_message(message.channel, msg)

    if 'who are you' in message.content.lower():
        msg = 'I am Echo Bot.'.format(message)
        await client.send_message(message.channel, msg)

    if 'where are you' in message.content.lower():
        msg = 'I am in discord servers. Add me to a server you manage: https://discordapp.com/api/oauth2/authorize?client_id=532762575524593674&permissions=8&scope=bot .'.format(message)
        await client.send_message(message.channel, msg)
    
    if 'good afternoon' in message.content.lower():
        msg = 'Good afternoon {0.author.mention}. Hope you are having a nice day! :hugging: '.format(message)
        await client.send_message(message.channel, msg)
        
    if 'good evening' in message.content.lower():
        msg = 'Good evening {0.author.mention}. How was your day? :hugging: '.format(message)
        await client.send_message(message.channel, msg)
        
    if 'good morning' in message.content.lower():
        msg = 'Good morning {0.author.mention}. Have a nice day! :hugging: '.format(message)
        await client.send_message(message.channel, msg)
        
    if 'good night' in message.content.lower():
        msg = 'Good night {0.author.mention}. Sweet dreams! :hugging: '.format(message)
        await client.send_message(message.channel, msg)
    
    if client.user.mentioned_in(message) and message.mention_everyone is False:
        if 'hi' in message.content.lower():
            msg = 'Hello {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)
        
        if 'spam' in message.content.lower():
            msg_to_send = 10
            while msg_to_send > 0:
                msg_to_send = msg_to_send - 1
                msg = '''I am Echo Bot.'''.format(message)
                await client.send_message(discord.Object(id='533652594145361929'), msg)
                await asyncio.sleep(1)
            return
        if 'bye' in message.content.lower():
            msg = 'Bye :wave::skin-tone-1: {0.author.mention}. :hugging: '.format(message)
            await client.send_message(message.channel, msg)
        if 'gm' in message.content.lower():
            msg = 'Good morning {0.author.mention}. Have a nice day! :hugging: '.format(message)
            await client.send_message(message.channel, msg)
        if 'gn' in message.content.lower():
            msg = 'Good night {0.author.mention}. Sweet dreams! :hugging: '.format(message)
            await client.send_message(message.channel, msg)
        if 'help' in message.content.lower():
            msg = 'Send **`$help`** to see the available commands.'
            await client.send_message(message.channel, msg)
        
        if 'khaja' in message.content.lower():
            msg = 'Sorry {0.author.mention}, I do not eat. '.format(message)
            await client.send_message(message.channel, msg)
        if 'khana' in message.content.lower():
            msg = 'Sorry {0.author.mention}, I do not eat. '.format(message)
            await client.send_message(message.channel, msg)
        if 'love' in message.content.lower():
            msg = '{0.author.mention}, I will love you until you are in **EchoZONE**. :heart_eyes: :hugging: '.format(message)
            await client.send_message(message.channel, msg)
        if 'playlist' in message.content.lower():
            msg = '**Global Top 50:** https://www.youtube.com/playlist?list=PL8cV2deJEZLGsrT9z5wq101gnXXvwrSwe\n**Spanish:** https://www.youtube.com/playlist?list=PL8cV2deJEZLH3MqOgKunS4IqHtjgORutm'.format(message)
            await client.send_message(message.channel, msg)
        if 'gender' in message.content.lower():
            msg = 'Sorry {0.author.mention}, I am a bot. '.format(message)
            await client.send_message(message.channel, msg)
            
    if message.content.startswith('$greet'):
        channel = message.channel
        await client.send_message(channel,'Say **`hello`**!')
    if message.content.startswith('$help'):
        msg = '__**Discord Link**__\nhttps://discord.gg/SfEVnnn\n\n__**Commands:**__\n**`$greet`**: Greetings!\n**`good morning`**: Wishes Good Morning!\n**`good night`**: Wishes Good night!\n**`who are you`**: Identifies itself.\n**`how are you`**: are you fine?\n**`where are you`**: Gives information on how to add ***Echo Bot*** to your server.'.format(message)
        await client.send_message(message.channel, msg)
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name=str(len(client.servers))+"1 servers", type=3))

newUserMessage = """Hey there, welcome to EchoZONE :tada: :hugging: ! Enjoy your stay. """

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message(discord.Object(id='514791436953321472'), 'Hey ' + member.mention + ', welcome to EchoZONE :tada: :hugging: !')
    await client.send_message(discord.Object(id='524545409109196800'), 'Hey ' + member.mention + ', send `$help` and know commands to talk to me! :wink: ')
    await client.send_message(member, newUserMessage)
    print("Sent message to " + member.name)

    # give member the steam role here
    ## to do this the bot must have 'Manage Roles' permission on server, and role to add must be lower than bot's top role
    role = discord.utils.get(member.server.roles, name="Echo Echo")
    await client.add_roles(member, role)
    print("Added role '" + role.name + "' to " + member.name)

@client.event
async def on_member_remove(member):
    print("Recognized that " + member.name + " left")
    await client.send_message(discord.Object(id='514791436953321472'), '**' + member.mention + '** just left.')
    print("Sent message to #CHANNEL")

client.run(os.environ['BOT_TOKEN'])
