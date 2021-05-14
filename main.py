import os
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord.utils import get
from dotenv import load_dotenv
import random
from youtube_dl import YoutubeDL
from databases import urls
from cogs import musica

load_dotenv()
client = commands.Bot (command_prefix = "!")

#------------------- COMANDOS DE COGS -------------------------

#Carrega um arquivo cog
@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  await ctx.send ("Cog **carregado** com sucesso.")

#Descarrega um arquivo cog 
@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  await ctx.send ("Cog **descarregado** com sucesso.")

#Recarrega um arquivo cog 
@client.command()
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')
  await ctx.send ("Cog **recarregado** com sucesso.")

#Ao iniciar o bot dá load em seus cogs
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension (f'cogs.{filename[:-3]}')

#------------------- ENTRAR E SAIR NO CANAL DE VOZ -------------------------

#Nota: Os comandos relacionados ao voice channel precisam da biblioteca PyNaCl, use pip install -U discord.py[voice] no terminal para instalar o pacote
#Entra no canal de voz
@client.command()
async def join(ctx):
  channel = ctx.author.voice.channel
  vc = await channel.connect()
  
#Sai no canal de voz
@client.command()
async def leave(ctx):
  for vc in client.voice_clients:
    await vc.disconnect()

#------------------- COMANDOS DE MÚSICA -------------------------

#Faz tocar a música do url, precisa dar pip instal ffmpeg
#Faz tocar a música do url
@client.command()
async def play(ctx, url):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)
    with YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']
    voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    voice.is_playing()

#Para a música
@client.command()
async def stop(ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    voice.stop()

#Pausa a música
@client.command()
async def pause(ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    voice.pause()

#Continua a música
@client.command()
async def resume(ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    voice.resume()

#------------------- TIPOS DE MÚSICA -------------------------

#Envia um url randomizado para o play
@client.command()
async def ambientefantasia(ctx):
  musica = random.choice(urls.ambiente_fantasia)
  await join (ctx)
  await play(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado para o play
@client.command()
async def combatecomum(ctx):
  musica = random.choice(urls.combate_comum)
  await join (ctx)
  await play(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado para o play
@client.command()
async def combatesombrio(ctx):
  musica = random.choice(urls.combate_sombrio)
  await join (ctx)
  await play(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command()
async def combateepico(ctx):
  musica = random.choice(urls.combate_epico)
  await join (ctx)
  await play(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command()
async def ambientesombrio(ctx):
  musica = random.choice(urls.ambiente_sombrio)
  await join (ctx)
  await play(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#------------------- RUN E DEBUG --------------------------

#Retornando um print para saber que o bot foi inicializado
@client.event
async def on_ready():
    print("Bot pronto para uso.")

#Faz o bot rodar usando o token dele
client.run(os.environ['TOKEN'])
