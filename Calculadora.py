<<<<<<< HEAD
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

client.run('NDg3NjI4NDc5MDIyNDk3ODE2.DnQm6Q.jbALvHH79kUnhQyO8b-81wu9t2c')



=======
import discord
import asyncio
 
client = discord.Client()
 
@client.event
async def on_ready():
    print('BOT ONLINE!')
    print(client.user.name)
    print(client.user.id)
 
 
@client.event
async def on_message(message):
    if message.content.lower().startswith('?oi'):
        await client.send_message(message.channel, 'Olá!')
    elif message.content.lower().startswith('?birl'):
        await client.send_message(message.channel, 'BIIIRLLLLL!')
	elif message.content.lower().startswith('?game'):
		await client.send_message(message.channel, ':)')
        
        
 
 
client.run('NDg3NjI4NDc5MDIyNDk3ODE2.DnQm6Q.jbALvHH79kUnhQyO8b-81wu9t2c')



>>>>>>> 544f2e504581ffd3df3d7438524b2793591e1cc7
