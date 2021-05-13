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
from keep_alive import keep_alive

load_dotenv()
client = commands.Bot (command_prefix = "!")

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

#Faz tocar a música do url, precisa dar pip instal ffmpeg
@client.command()
async def play(ctx, url):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
    else:
        await ctx.send("Already playing song")
        return

#Envia um url randomizado para o play
@client.command()
async def ambientefantasia(ctx):
  musica = random.choice(urls.ambiente_fantasia)
  await play.callback(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado para o play
@client.command()
async def combatecomum(ctx):
  musica = random.choice(urls.combate_comum)
  await play.callback(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado para o play
@client.command()
async def combatesombrio(ctx):
  musica = random.choice(urls.combate_sombrio)
  await play.callback(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command()
async def combateepico(ctx):
  musica = random.choice(urls.combate_epico)
  await play.callback(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command()
async def ambientesombrio(ctx):
  musica = random.choice(urls.ambiente_sombrio)
  await play.callback(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Retornando um print para saber que o bot foi inicializado
@client.event
async def on_ready():
    print("Bot pronto para uso.")

#Faz o bot rodar usando o token dele
keep_alive()
client.run(os.environ['TOKEN'])
