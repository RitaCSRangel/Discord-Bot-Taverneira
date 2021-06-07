import discord
from replit import db
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
    texto = "Ao completar missões seu personagem ganha moedas planares equivalentes a quantidade de níveis que conseguiu avançar naquela missão (mínimo 1). O mestre também ganha moedas equivalentes a quantidade de níveis que os jogadores avançaram na missão + 1. \n \n`Não esqueça de marcar suas moedas de maneira adequada em sua ficha e lembre-se de que uma missão pode fornecer, no máximo 3 níveis, ou seja, 3 moedas.` "
    await ctx.channel.send(texto)

  @commands.command()
  async def jogadorestp(self, ctx):
    keys = db.keys()
    k = str(keys)
  
    nomes = k.replace("{", "").replace ("'", "").replace("}","").replace(" ", "").replace(",", " ")
    nomes = nomes.split()
  
    jogadores = []
    for n in nomes:
      if "jogador_" in n:
        jogadores.append(n)
  
    jogadoresTP = str(jogadores).replace("jogador_", "").replace("[", "").replace("'", "").replace("]", "\n")

    texto = f"**Esses são os aventureiros da Taverna Planar:** \n {jogadoresTP}"
    await ctx.send(texto)

  @commands.command()
  async def saldostp(self, ctx):
    keys = db.keys()
    k = str(keys)
  
    nomes = k.replace("{", "").replace ("'", "").replace("}","").replace(" ", "").replace(",", " ")
    nomes = nomes.split()
  
    jogadores = []
    for n in nomes:
      if "jogador_" in n:
        jogadores.append(n)
  
    jogadoresTP = str(jogadores).replace("jogador_", "").replace("[", "").replace("'", "").replace("]", "")

    texto = f"**Esses são os aventureiros da Taverna Planar:** \n {jogadoresTP} \n Digite o nome do aventureiro que gostaria de verificar:"
    await ctx.send(texto)
    msgNome = await self.client.wait_for("message")
  
    if "!" in msgNome.content:
      return
  
    try:
      value = db[f"jogador_{msgNome.content}"]
      await ctx.send (f"Esse(a) aventureiro(a) tem um total de ** {value}** moedas planares")
    except:
      await ctx.send (f"Falha. Digite um dos nomes listados acima. Se o seu nome não estiver ali, use o comando **!entrartp** para se cadastrar nos comanos da Taverna Planar.")
      return

@commands.command()
async def bolsatp(self, ctx):
  keys = db.keys()
  k = str(keys)
  
  nomes = k.replace("{", "").replace ("'", "").replace("}","").replace(" ", "").replace(",", " ")
  nomes = nomes.split()
  
  jogadores = []
  for n in nomes:
    if "jogador_" in n:
      jogadores.append(n)
  
  jogadoresTP = str(jogadores).replace("jogador_", "").replace("[", "").replace("'", "").replace("]", "")

  texto = f"**Esses são os aventureiros da Taverna Planar:** \n {jogadoresTP} \n Digite o nome do aventureiro que gostaria de verificar:"
  await ctx.send(texto)
  msgNome = await self.client.wait_for("message")

  try:
    itens = db [f"bolsa_{msgNome.content}"]
    await ctx.send (f"Esse(a) aventureiro(a) tem os seguintes itens em sua bolsa: \n {itens}")
  except:
    await ctx.send (f"Falha. Sua bolsa pode estar vazia ou você não digitou um dos nomes listados acima. Se o seu nome não estiver ali, use o comando **!entrartp** para se cadastrar nos comanos da Taverna Planar.")
    return

@commands.command()
async def entrartp(self, ctx):
  texto = "Digite o seu nome:\n*Não utilize caracteres especiais e espaços. Acentos e números são permitidos.*"
  await ctx.send(texto)
  msgNome = await self.client.wait_for("message")
  
  if "!" in msgNome.content:
    return
  
  texto = "Digite quantas moedas planares você tem:"
  await ctx.send (texto)
  msgMoeda = await self.client.wait_for("message")
  
  valor = int (msgMoeda.content)
  
  if "!" in msgMoeda.content:
    return
  elif valor < 0:
    await ctx.send ("Insira uma quantidade válida de moedas (maior que 0):")
    msgMoeda = await self.client.wait_for("message")
    valor = int (msgMoeda.content)
  elif valor < 0:
    await ctx.send ("Falha. Valor inserido é inválido.")
    

  db[f"jogador_{msgNome.content}"] = msgMoeda.content
  await ctx.send ("Bem vindo(a)! Agora você pode consultar seu saldo com o comando **!saldostp**, comprar itens com o comando **!comprartp**, adicionar mais moedas com o comando **!addmoedas** ou remover seu cadastro aqui na Taverneira de Fibra com o comando **!sairtp**. Não deixe também de checar as regras sobre a Taverna Planar em **!regrastp** e ver a lista de itens em **!itenstp**.")

@commands.command()
async def sairtp(self, ctx):
  texto = "Digite o nome do aventureiro a ser removido:"
  await ctx.send(texto)
  msgNome = await self.client.wait_for("message")
  
  if "!" in msgNome.content:
    return
  
  try:
    del db [f"jogador_{msgNome.content}"]
    del db [f"bolsa_{msgNome.content}"]
    await ctx.send (f"{msgNome.content} foi removido(a) da lista de Aventureiros Planares.")
  except:
    await ctx.send ("Falha. Insira o nome de um jogador cadastrado nos comandos da Taverna Planar. Você pode se cadastrar em **!entrartp** ou checar quem são os jogadores em **!jogadorestp**")

@commands.command()
async def addmoedastp(self, ctx):
  texto = "Digite o seu nome:"
  await ctx.send(texto)
  msgNome = await self.client.wait_for("message")
  
  if "!" in msgNome.content:
    return

  texto = "Digite quantas moedas planares quer adicionar:"
  await ctx.send (texto)
  msgMoeda = await self.client.wait_for("message")
  
  valor = int (msgMoeda.content)
  
  if "!" in msgMoeda.content:
    return
  
  if valor < 0:
    await ctx.send ("Insira uma quantidade válida de moedas (maior que 0):")
    msgMoeda = await self.client.wait_for("message")
    valor = int (msgMoeda.content)
  elif valor < 0:
    await ctx.send ("Falha. Valor inserido é inválido.")
    return
  
  moedasAtuais = int(db[f"jogador_{msgNome.content}"])
  moedasTotais = moedasAtuais + valor
  db[f"jogador_{msgNome.content}"] = str ( moedasTotais)
  await ctx.send ("Valor inserido com sucesso.")

@commands.command()
async def remoedastp(self, ctx):
  texto = "Digite o seu nome:"
  await ctx.send(texto)
  msgNome = await self.client.wait_for("message")
  
  if "!" in msgNome.content:
    return

  texto = "Digite quantas moedas planares quer remover:"
  await ctx.send (texto)
  msgMoeda = await self.client.wait_for("message")
  
  valor = int (msgMoeda.content)
  
  if "!" in msgMoeda.content:
    return
  
  if valor < 0:
    await ctx.send ("Insira uma quantidade válida de moedas (maior que 0):")
    msgMoeda = await self.client.wait_for("message")
    valor = int (msgMoeda.content)
  elif valor < 0:
    await ctx.send ("Falha. Valor inserido é inválido.")
    return
  
  moedasAtuais = int(db[f"jogador_{msgNome.content}"])
  moedasTotais = moedasAtuais - valor
  db[f"jogador_{msgNome.content}"] = str ( moedasTotais)
  await ctx.send ("Valor removido com sucesso.")

@commands.command()
async def comprartp(self, ctx):
  texto = "Esses são os itens disponíveis para a compra: \n\n**Nome:** Pergaminho de Ressurreição \n**Preço:** 12 moedas planares.\n**Efeito:** Ressuscita o personagem independente de quanto tempo tenha se passado desde a sua morte e de como tenha morrido. O personagem mantém os itens e níveis que tinha ao morrer. \n\n**Nome:** Hero Point\n**Preço:** 1 moeda planar.\n**Efeito:** Só pesquisar o que faz. Sujeito a alterações do mestre da mesa.\n\n**Nome:** Tomo de Aprimoramento\n**Preço:** 8 moedas planares.\n**Efeito:** Concede ao jogador +1 de atributo, esse bônus é do tipo inherent e pode aumentar um atributo em no máximo +5.\n\n**Nome:** Treinamento Especial\n**Preço:** 2 moedas planares.\n**Efeito:** Permite que o jogador considere uma perícia como perícia de classe. \n\n `Mais itens em breve. Sugestões são bem vindas, mande-as no chat.`\n\nDigite o nome do item que você gostaria de comprar:"
  await ctx.send(texto)
  msgItem = await self.client.wait_for("message")
  
  if "!" in msgItem.content:
    return
  
  itemNome = msgItem.content
  itemNome.replace("item_", "")
  
  try:
    valorItem = db [f"item_{msgItem.content}"]
  except:
    await ctx.send ("Falha. Digite um nome de item cadastrado nos comandos da Taverna Planar.")
    return
  
  texto = "Digite o nome do jogador que irá comprar o item:"
  await ctx.send (texto)
  msgNome = await self.client.wait_for("message")
  
  if "!" in msgNome.content:
    return
  
  jogadorNome = msgNome.content
  jogadorNome.replace("jogador_", "")
  
  try:
    moedas = db [f"jogador_{msgNome.content}"]
  except:
    await ctx.send ("Falha. Digite um nome de jogador cadastrado nos comandos da Taverna Planar.")
    return
  
  texto = f"Deseja confirmar a compra de **{itemNome}** para **{jogadorNome}** pelo preço listado de {valorItem} moedas planares? Digite **s** para sim ou **n** para não:"
  await ctx.send(texto)
  msgResposta = await self.client.wait_for("message")
  
  if msgResposta.content == "s" or msgResposta.content == "S":
    v = int(valorItem)
    m = int (moedas)
    moedasRestantes = m - v
  
    if moedasRestantes < 0:
      await ctx.send (f"Falha. O jogador possui **{moedas}** moedas planares.")
      return
    
    db [f"jogador_{msgNome.content}"] = str(moedasRestantes)
    itensAnteriores = db [f"bolsa_{msgNome.content}"]
    db [f"bolsa_{msgNome.content}"] = itensAnteriores + msgItem.content
    await ctx.send (f"Compra realizada com sucesso. Restam {moedasRestantes} moedas planares.")


#Adicionando o cog ao bot
def setup (client):
  client.add_cog(TavernaPlanar(client))