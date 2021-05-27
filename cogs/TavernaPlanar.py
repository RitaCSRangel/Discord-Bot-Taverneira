import discord
from discord.ext import commands

class TavernaPlanar (commands.Cog):

  #Retornando um print para saber que o cog foi inicializado
  def __init__ (self, client):
    self.client = client
  
  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print("Cog Taverna Planar pronto para uso.")
  
  #Commands
  @commands.command()
  async def regrastp(self, ctx):
    texto = "Ao completar missões seu personagem ganha *moedas planares equivalentes a quantidade de níveis que conseguiu avançar naquela missão (mínimo 1)*. O mestre também ganha moedas equivalentes a quantidade de níveis que os jogadores avançaram na missão + 1. \n \n`Não esqueça de marcar suas moedas de maneira adequada em sua ficha e lembre-se de que uma missão pode fornecer, no máximo 3 níveis, ou seja, 3 moedas.` "
    await ctx.channel.send(texto)
  
  @commands.command()
  async def itenstp(self, ctx):
    texto = "**Nome:** Pergaminho de Ressureição \n**Preço:** 12 moedas planares. \n**Efeito:** Ressuscita o personagem independente de quanto tempo tenha se passado desde a sua morte e de como tenha morrido. O personagem mantém os itens e níveis que tinha ao morrer. \n \n*Mais itens em breve. Sugestões são bem vindas, mande-as no chat.*"
    await ctx.channel.send(texto)

#Adicionando o cog ao bot
def setup (client):
  client.add_cog(TavernaPlanar(client))