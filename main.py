import os
import discord
from discord import message
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

#------------------- COMANDOS DE COGS -------------------------

#Carrega um arquivo cog
@client.command(brief='Load de uma cog', description='Faz o load de uma cog que estiver unloaded. Comando usado apenas para fins de desenvolvimento.')
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  await ctx.send ("Cog **carregado** com sucesso.")

#Descarrega um arquivo cog 
@client.command(brief='Unload de cog', description='Faz o unload de uma cog que estiver loaded. Comando usado apenas para fins de desenvolvimento.')
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  await ctx.send ("Cog **descarregado** com sucesso.")

#Recarrega um arquivo cog 
@client.command(brief='Recarregar cog', description='Faz o unpload e load de uma cog. Comando usado apenas para desenvolvimento.')
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
@client.command(brief='Entrar em um canal de voz.', description='Faz o bot entrar no canal de voz em que você estiver.')
async def join(ctx):
  channel = ctx.author.voice.channel
  vc = await channel.connect()
  
#Sai no canal de voz
@client.command(brief='Sair do canal de voz.', description='Faz o bot sair do canal no qual ele se encontra.')
async def leave(ctx):
  for vc in client.voice_clients:
    await vc.disconnect()

#------------------- COMANDOS DE MÚSICA -------------------------

#Faz tocar a música do url, precisa dar pip instal ffmpeg
#Faz tocar a música do url
@client.command(brief='Toca a música do link fornecido.', description='Pega o link do youtube fornecido junto ao comando e o toca caso esteja em um canal de voz.')
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
@client.command(brief='Para a música.', description='Encerra completamente a música que estiver tocano.')
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()

#Pausa a música
@client.command(brief='Pausa a música.', description='Pausa a música que estiver tocando. Ela pode voltar a tocar de onde parou com o comando resume.')
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.pause()

#Continua a música
@client.command(brief='Continua a música.', description='Volta a tocar a música pausada.')
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.resume()

#------------------- TIPOS DE MÚSICA -------------------------

#Envia um url randomizado para o play
@client.command(brief='Música aleatória de Ambiente Fantasia.', description='Pega uma música aleatória de Ambiente Fantasia e a toca.')
async def ambientefantasia(ctx):
  musica = random.choice(urls.ambiente_fantasia)
  await join (ctx)
  await play(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command(brief='Música aleatória de Ambiente Sombrio.', description='Pega uma música aleatória de Ambiente Sombrio e a toca.')
async def ambientesombrio(ctx):
  musica = random.choice(urls.ambiente_sombrio)
  await join (ctx)
  await play(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado para o play
@client.command(brief='Música aleatória de Combate Comum.', description='Pega uma música aleatória de Combate Comum e a toca.')
async def combatecomum(ctx):
  musica = random.choice(urls.combate_comum)
  await join (ctx)
  await play(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado para o play
@client.command(brief='Música aleatória de Combate Sombrio.', description='Pega uma música aleatória de Combate Sombrio e a toca.')
async def combatesombrio(ctx):
  musica = random.choice(urls.combate_sombrio)
  await join (ctx)
  await play(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command(brief='Música aleatória de Combate Épico.', description='Pega uma música aleatória de Combate Épico e a toca.')
async def combateepico(ctx):
  musica = random.choice(urls.combate_epico)
  await join (ctx)
  await play(ctx, musica)
  await ctx.channel.send (f"Tocando: {musica}")

#------------------ INFOS SOBRE MÚSICA E ADD MÚSICA -------------------------

#Lista de Playlists de música
@commands.command(brief='Lista de categoria de músicas.', description='Todas as categorias de música atuais. Use um desses comandos para pegar uma música aleatória do estilo escolhido e tocar.')
async def musicas(self, ctx):
  texto = "**Escolha o tipo de música que deseja tocar:** \n !AmbienteFantasia \n !AmbienteSombrio \n !AmbienteÉpico \n !CombateComum \n !CombateSombrio \n !CombateÉpico \n !Floresta \n !Dungeon \n !Taverna \n !Mercado \n !Deserto"
  await ctx.channel.send(texto)

@client.command(brief='Adicionar a sua música em uma categoria.', description='Coloque o seu link do youtube em uma das categorias e música para que ele possa ser tocado daqui em diante.')
async def addmusica(ctx):
  await ctx.channel.send("Um dia eu implemento isso aqui.")

#------------------- RUN E DEBUG --------------------------

#Retornando um print para saber que o bot foi inicializado
@client.event
async def on_ready():
    print("Bot pronto para uso.")

#Faz o bot rodar usando o token dele
keep_alive()
client.run(os.environ['TOKEN'])
