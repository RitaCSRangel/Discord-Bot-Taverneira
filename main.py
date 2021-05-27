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
from databases import urls, jogadores
from keep_alive import keep_alive

load_dotenv()
client = commands.Bot (command_prefix = "!", help_command=None)

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

#----------- COMANDOS GERAIS ------------------
#Redefinição do comando de Help
@client.command()
async def help(ctx):
    await ctx.send("**Bem vindo a taverna, aventureiro**! \n Aqui estão os comandos disponíveis e suas descrições. \n \n **Comandos para controlar o bot de música:** \n join             *Entrar em um canal de voz.* \n leave            *Sair do canal de voz.* \n play            *Tocar a música do fornecido.* \n pause            *Pausar a música.* \n stop             *Parar a música.* \n resume           *Continua a música.* \n \n **Comandos para tocar músicas aleatórias baseadas em um tópico:** \n ambientecalmo    *Música aleatória de Ambiente Calmo.* \n ambienteepico    *Música aleatória de Ambiente Calmo.* \n ambientefantasia    *Música aleatória de Ambiente Fantasia.* \n ambienteinfernal    *Música aleatória de Ambiente Infernal.* \n ambientesombrio    *Música aleatória de Ambiente Sombrio.* \n combatecomum     *Música aleatória de Combate Comum.* \n combateepico     *Música aleatória de Combate Épico.* \n combatesombrio   *Música aleatória de Combate Sombrio.* \n kasinao          *Música do Kasinão.* \n \n **Comandos para utilizar a Loja Planar:** \n regraslp     *Ver as regras da Loja Planar.* \n itenslp     *Ver os itens disponíveis na Loja Planar.* \n saldoslp     *Ver o saldo dos jogadores na Loja Planar.* \n \n **Comandos para ajudar na criação de personagens e NPCs:** \n gerarpersonagem     *Gerar informações genéricas e divertidas.* \n\n **Comandos de developer para manipular cogs:** \n load     *Carregar uma cog.* \n reload     *Recarregar uma cog.* \n unload     *Descarregar cog.*")

@client.command()
async def saldostp(ctx):
  texto = f"Os jogadores disponíveis são: \n \n{jogadores.jogadoresTP}"
  await ctx.channel.send(texto)
  
  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and \
    msg.content in jogadores.jogadoresTP

  msg = await client.wait_for("message", check=check)

  if msg.content in jogadores.jogadoresTP:
    i = 0
    while msg.content != jogadores.jogadoresTP[i]:
      i = i + 1
    
    texto = f"{jogadores.jogadoresTP[i]} tem {3} moedas planares."
    await ctx.send (texto)
  else:
    await ctx.send("You said no!")

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
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()

#Pausa a música
@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.pause()

#Continua a música
@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.resume()

#Cria uma queue
@client.command()
async def queue(ctx, url):
  global queue
  queue.append(url)
  await ctx.send ("Música adicionada ao queue.")

#Dá loop na música
@client.command()
async def loop(ctx):
  await ctx.send ("Nem fiz ainda.")

#------------------- TIPOS DE MÚSICA -------------------------

#Envia um url randomizado para o play
@client.command()
async def combatecomum(ctx):
  musica = random.choice(urls.combate_comum)
  #await join (ctx)
  await play(ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado para o play
@client.command()
async def combatesombrio(ctx):
  musica = random.choice(urls.combate_sombrio)
  #await join (ctx)
  await play(ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command()
async def combateepico(ctx):
  musica = random.choice(urls.combate_epico)
  #await join (ctx)
  await play(ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command()
async def ambienteinfernal(ctx):
  musica = random.choice(urls.ambiente_infernal)
  #await join (ctx)
  await play(ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command()
async def ambientecalmo(ctx):
  musica = random.choice(urls.ambiente_calmo)
  #await join (ctx)
  await play(ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command()
async def ambienteepico(ctx):
  musica = random.choice(urls.ambiente_epico)
  #await join (ctx)
  await play(ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado para o play
@client.command()
async def ambientefantasia(ctx):
  musica = random.choice(urls.ambiente_fantasia)
  #await join (ctx)
  await play(ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command()
async def ambientesombrio(ctx):
  musica = random.choice(urls.ambiente_sombrio)
  #await join (ctx)
  await play(ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@client.command()
async def kasinao(ctx):
  musica = urls.kasinao
  #await join (ctx)
  await play(ctx, musica)
  await ctx.send (f"Tocando: {musica}")
#------------------ ADD MÚSICA ---------------------

@client.command()
async def addmusica(ctx):
  await ctx.send("Um dia eu implemento isso aqui.")

#------------------- RUN E DEBUG --------------------------

#Retornando um print para saber que o bot foi inicializado
@client.event
async def on_ready():
    print("Bot pronto para uso.")

#Faz o bot rodar usando o token dele
keep_alive()
client.run(os.environ['TOKEN'])
