import discord
import asyncio
 
client = discord.Client()
 
@client.event
async def on_ready():
    print('BOT ONLINE!')
    print(client.user.name)
 
 
@client.event
async def on_message(message):
    if message.content.lower().startswith('?oi'):
        await client.send_message(message.channel, 'Olá!')
    elif message.content.lower().startswith('?test'):
        await client.send_message(message.channel, 'Ok!')

client.run('')


