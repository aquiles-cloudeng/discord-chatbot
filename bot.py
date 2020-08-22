# bot.py
import os
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} se unió al mejor Discord de la vida!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hola {member.name}, bienvenido a barredoras!'
    )
    channel = client.get_channel(389520903899185154)
    await channel.send(f'Hola {member.name}, ME PREGUNTO QUE VIENES A BUSCAR (ojala a mi)')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mensajerino = [
        '@everyone vengan a jugar por favor amigos',
        '@everyone si no vienen a jugar me voy a calentar',
        '@everyone si no quieren perecer les pido que se presenten inmediatamente para jugar' 
    ]

    juguemos = [
        'lo que sea por favor no aguanto mas',
        'hoy en dia jugamos TTT, GMOD, fall guys, entre otros',
        'cualquier cosa menos factorio'
    ]

    factorio = [
        'basta con este juego por favor',
        'che hay otros juegos sabes?',
        'we todo el dia con ese juego toy cansado hermano'
    ]

    if 'que sale?' in message.content:
        response = random.choice(juguemos)
        await message.channel.send(response)
    if 'koloseñal' in message.content:
        response = random.choice(mensajerino)
        await message.channel.send(response)
    if 'factorio' in message.content:
        response = random.choice(factorio)
        await message.channel.send(response)

client.run(TOKEN)