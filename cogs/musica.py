import discord
from discord.ext import commands

class Musica (commands.Cog):

  #Retornando um print para saber que o cog foi inicializado
  def __init__ (self, client):
    self.client = client
  
  #Events
  @commands.Cog.listener()
  async def on_ready (self):
    print("Cog música pronto para uso.")
  
  #Músicas
  @commands.command()
  async def musicas(self, ctx):
    texto = "**Escolha o tipo de música que deseja tocar:** \n !AmbienteFantasia \n !AmbienteSombrio \n !AmbienteÉpico \n !CombateComum \n !CombateSombrio \n !CombateÉpico \n !Floresta \n !Dungeon \n !Taverna \n !Mercado \n !Deserto"
    await ctx.channel.send(texto)

#Adicionando o cog ao bot
def setup (client):
  client.add_cog(Musica(client))