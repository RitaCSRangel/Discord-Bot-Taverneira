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
  
  #Retorma infos sobre as mesas atuais
  @commands.command()
  async def mesas(self, ctx):
    await ctx.send("**Atualmente as mesas em andamento são:** \n\n **Wrath of the Righteous** \n *A Ira dos justos (Wrath of the Righteous) é uma campanha que se passa na quinta crusada mendeviana conta os demônios da Ferida do Mundo. Enquanto vigiados por uma divindade, os crusados devem se provar merecedores de receberem um poder inimaginável que poderá virar a mesa contra os exércitos de Sarkoris.* \n Vagas: Esgotadas. \n\n **Rise of the Runelords** \n *Mais informações em breve.* \n Vagas: Esgotadas. \n\n **Kingmaker** \n *Em Kingmaker os jogadores desbravam as terras saqueadas, uma imensidão selvagem abaixo de Brevoy, para formar um reino próprio. As terras saqueadas contudo não são fáceis de se domar, pois escondem muitos perigos e segredos, além de uma forte conexão com o Primeiro Mundo, ou como é também é conhecido, o Mundo das Fadas. \n Vagas: Esgotadas \n\n **Namíria** \n\n *Namíria é um cenário próprio construído também pelos jogadores que deixaram suas marcas ao longo das campanhas. Mais informações podem ser encontradas no canal cenário dentro da categoria Namíria.* \n Vagas: Hiato. \n\n **Age of Ashes** \n *Era das cinzas (Age of Ashes) conta a história de um grande mal que assombra toda a Golarion, um mal nunca antes visto desde a Era da Earthfall (uma era citada na cronologia do mundo de Golarion). O grupo acaba se envolvendo nessa história quando se apossam de um castelo antes pertencente aos cavaleiros helknight cheliaxianos que abandonaram o local.* \n Vagas: Hiato. \n\n **Corte de Espinhos e Rosas** \n *Mais informações em breve.* \n Vagas: Esgotadas. \n Sistema: Changeling \n\n **Um Velho Amigo** \n\n *Uma trama sobre um assassinato repentino e cruel de um senhor que muito falava sobre o sobrenatural que, de uns tempos para cá, tem cercado a vida dos personagens.* \n Vagas: Esgotadas. \n Sistema: Crônicas das Trevas. \n\n **Não encontrou nenhuma mesa disponível ou interessante?** \n Então experimente olhar na Taverna Planar, um local para aventureiros que desejam uma aventura rápida.")

#Adicionando o cog ao bot
def setup (client):
  client.add_cog(Utilitarios(client))