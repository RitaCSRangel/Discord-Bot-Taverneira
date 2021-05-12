import discord
from discord.ext import commands

class Utilitarios (commands.Cog):

  #Retornando um print para saber que o cog foi inicializado
  def __init__ (self, client):
    self.client = client
  
  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print("Cog utilitários pronto para uso.")
  
  #Commands
  #Retorma os comandos disponíveis do bot
  @commands.command()
  async def comandos(self, ctx):
    await ctx.send("**Os comandos disponíveis são: ** \n !mesas \n !gerarpersonagem \n !musicas")

#Adicionando o cog ao bot
def setup (client):
  client.add_cog(Utilitarios(client))