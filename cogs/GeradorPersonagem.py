import discord
from discord.ext import commands
import random
from databases import personagem

class GeradorPersonagem (commands.Cog):

  #Retornando um print para saber que o cog foi inicializado
  def __init__ (self, client):
    self.client = client
  
  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print("Cog Gerador Personagem pronto para uso.")
  
  #Commands
  #Retorma um personagem randomizado
  @commands.command()
  async def gerarpersonagem(self, ctx):
    chance = random.randint(0,125)
    if chance <= 50:
      genero = personagem.genero[0]
    if chance <= 100:
      genero = personagem.genero[1]
    if chance <= 25:
      genero = personagem.genero[2]

    raca = random.choice(personagem.raca)
    idade = random.choice(personagem.idade)
    pais = random.choice(personagem.pais)
    familia = random.choice(personagem.familia)
    pais_ausentes = random.choice(personagem.pais_ausentes_causa)
    pais_mortos = random.choice(personagem.pais_mortos_causa)
    memorias_infancia = random.choice(personagem.memorias_infancia)
    objetivo = random.choice(personagem.objetivos)
    estilo_de_vida = random.choice(personagem.estilo_de_vida)
    segredo = random.choice(personagem.segredo)
    background = random.choice(personagem.background)
    drawback = random.choice(personagem.drawback)
    evento_maior = random.choice(personagem.evento_maior)
    evento_menor = random.choice(personagem.evento_menor)
    tracos_negativos1 = random.choice(personagem.tracos_negativos)
    tracos_negativos2 = random.choice(personagem.tracos_negativos)
    tracos_positivos1 = random.choice(personagem.tracos_positivos)
    tracos_positivos2 = random.choice(personagem.tracos_positivos)
    maneirismo = random.choice(personagem.maneirismo)
    texto = "*Aqui está o seu personagem, use apenas o que achar interessante!* \n\n **--------- Informações Gerais ---------** \n\n **Gênero:** %s \n **Raça:** %s \n **Idade:** %s \n\n **--------- Informações sobre o seu Background ---------** \n\n **Sobre seus pais:** %s \n **Sua família consiste em:** %s \n **Se ambos os seus pais forem ausentes, o motivo foi que:** %s \n **Se os seus pais morreram, a causa foi:** %s \n **Suas memórias de infância são:** %s \n **Seu objetivo principal é:** %s \n **Seu estilo de vida é:** %s \n **Se você possuir um segredo, ele será que você:** %s \n **Em geral, seu background pode ser resumido em:** %s \n **Você tem um grande defeito, que é:** %s \n **O evento mais marcante da sua vida foi:** %s \n **Os demais eventos da sua vida (determinados pela sua idade) podem ser:** %s \n\n **--------- Informações sobre a sua Personalidade ---------** \n\n **Seus traços negativos são:** \n - %s \n - %s \n\n **Seus traços positivos são:** \n - %s \n - %s \n\n **Seu maneirismo é:** %s \n  " % (genero, raca, idade, pais, familia, pais_ausentes, pais_mortos, memorias_infancia, objetivo, estilo_de_vida, segredo, background, drawback, evento_maior, evento_menor, tracos_negativos1, tracos_negativos2, tracos_positivos1, tracos_positivos2, maneirismo)
    await ctx.channel.send(texto)

#Adicionando o cog ao bot
def setup (client):
  client.add_cog(GeradorPersonagem(client))