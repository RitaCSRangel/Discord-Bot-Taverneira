import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
import random
from youtube_dl import YoutubeDL
from databases import urls

class Musica (commands.Cog):

  #Retornando um print para saber que o cog foi inicializado
  def __init__ (self, client):
    self.client = client
  
  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print("Cog Musica pronto para uso.")

#------------------- ENTRAR E SAIR NO CANAL DE VOZ -------------------------

#Nota: Os comandos relacionados ao voice channel precisam da biblioteca PyNaCl, use pip install -U discord.py[voice] no terminal para instalar o pacote
#Entra no canal de voz
@commands.command()
async def join(ctx):
  channel = ctx.author.voice.channel
  vc = await channel.connect()
  
#Sai no canal de voz
@commands.command()
async def leave(self, ctx):
  for vc in self.client.voice_clients:
    await vc.disconnect()

#------------------- COMANDOS DE MÚSICA -------------------------

#Faz tocar a música do url, precisa dar pip instal ffmpeg
#Faz tocar a música do url
@commands.command()
async def play(self, ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(self.client.voice_clients, guild=ctx.guild)
    with YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']
    voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    voice.is_playing()

#Para a música
@commands.command()
async def stop(self, ctx):
    voice = get(self.client.voice_clients, guild=ctx.guild)
    voice.stop()

#Pausa a música
@commands.command()
async def pause(self, ctx):
    voice = get(self.client.voice_clients, guild=ctx.guild)
    voice.pause()

#Continua a música
@commands.command()
async def resume(self, ctx):
    voice = get(self.client.voice_clients, guild=ctx.guild)
    voice.resume()

#Cria uma queue
@commands.command()
async def queue(self, ctx, url):
  global queue
  queue.append(url)
  await ctx.send ("Música adicionada ao queue.")

#Dá loop na música
@commands.command()
async def loop(self, ctx):
  await ctx.send ("Nem fiz ainda.")

#Envia um url randomizado para o play
@commands.command()
async def combatecomum(self, ctx):
  musica = random.choice(urls.combate_comum)
  #await join (ctx)
  await play(self, ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado para o play
@commands.command()
async def combatesombrio(self, ctx):
  musica = random.choice(urls.combate_sombrio)
  #await join (ctx)
  await play(self, ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@commands.command()
async def combateepico(self, ctx):
  musica = random.choice(urls.combate_epico)
  #await join (ctx)
  await play(self, ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@commands.command()
async def ambienteinfernal(self, ctx):
  musica = random.choice(urls.ambiente_infernal)
  #await join (ctx)
  await play(self, ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@commands.command()
async def ambientecalmo(self, ctx):
  musica = random.choice(urls.ambiente_calmo)
  #await join (ctx)
  await play(self, ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@commands.command()
async def ambienteepico(self, ctx):
  musica = random.choice(urls.ambiente_epico)
  #await join (ctx)
  await play(self, ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado para o play
@commands.command()
async def ambientefantasia(self, ctx):
  musica = random.choice(urls.ambiente_fantasia)
  #await join (ctx)
  await play(self, ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@commands.command()
async def ambientesombrio(self, ctx):
  musica = random.choice(urls.ambiente_sombrio)
  #await join (ctx)
  await play(ctx, musica)
  await ctx.send (f"Tocando: {musica}")

#Envia um url randomizado de para o play
@commands.command()
async def kasinao(self, ctx):
  musica = urls.kasinao
  #await join (ctx)
  await play(self, ctx, musica)
  await ctx.send (f"Tocando: {musica}")
#------------------ ADD MÚSICA ---------------------

@commands.command()
async def addmusica(self, ctx):
  await ctx.send("Um dia eu implemento isso aqui.")


#Adicionando o cog ao bot
def setup (client):
  client.add_cog(Musica(client))