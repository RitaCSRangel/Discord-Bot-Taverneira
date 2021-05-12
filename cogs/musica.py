import discord
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
from youtube_dl import YoutubeDL

class Musica (commands.Cog):

  #Retornando um print para saber que o cog foi inicializado
  def __init__ (self, client):
    self.client = client
  
  #Events
  @commands.Cog.listener()
  async def on_ready (self):
    print("Cog música pronto para uso.")
  
  #Commands
  #Nota: Os comandos relacionados ao voice channel precisam da biblioteca PyNaCl, use pip install -U discord.py[voice] no terminal para instalar o pacote
  @commands.command()
  async def join(self, ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

#Adicionando o cog ao bot
def setup (client):
  client.add_cog(Musica(client))