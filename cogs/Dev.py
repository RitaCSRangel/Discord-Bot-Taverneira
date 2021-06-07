import os
import discord
from replit import db
from discord.ext import commands
import random
from databases import personagem

class Dev (commands.Cog):

  #Retornando um print para saber que o cog foi inicializado
  def __init__ (self, client):
    self.client = client
  
  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print("Cog Dev pronto para uso.")
  
  #Recarrega um arquivo cog 
  @commands.command()
  async def devcogreload(self, ctx, extension):
    self.client.unload_extension(f'cogs.{extension}')
    self.client.load_extension(f'cogs.{extension}')
    await ctx.send ("Cog **recarregado** com sucesso.")
  
  #Carrega um arquivo cog
  @commands.command()
  async def devcogload(self, ctx, extension):
    self.client.load_extension(f'cogs.{extension}')
    await ctx.send ("Cog **carregado** com sucesso.")

  #Descarrega um arquivo cog 
  @commands.command()
  async def devcogunload(self, ctx, extension):
    self.client.unload_extension(f'cogs.{extension}')
    await ctx.send ("Cog **descarregado** com sucesso.")

  #Adiciona um item na loja planar
  @commands.command()
  async def devadditemtp(self, ctx):
    texto = "Insira o nome do item:"
    await ctx.send (texto)
    msgNome = await self.client.wait_for("message")
    texto = "Insira o valor do item:"
    await ctx.send (texto)
    msgValor = await self.client.wait_for("message")
  
    db[f"item_{msgNome.content}"] = msgValor.content

    await ctx.send ("Item cadastrado com sucesso no banco Replit.")

  #Remove um item da loja planar
  @commands.command()
  async def devremitemtp(self, ctx):
    texto = "Insira o nome do item:"
    await ctx.send (texto)
    msgNome = await self.client.wait_for("message")
  
    del db[f"item_{msgNome.content}"]

    await ctx.send ("Item removido com sucesso no banco Replit.")
  
  #Altera um item da loja planar
  @commands.command()
  async def devaltitemtp(self, ctx):
    texto = "Insira o nome do item:"
    await ctx.send (texto)
    msgNome = await self.client.wait_for("message")
    texto = "Insira o novo valor do item:"
    await ctx.send (texto)
    msgValor = await self.client.wait_for("message")
  
    del db[f"item_{msgNome.content}"]
    db [f"item_{msgNome.content}"] = msgValor.content

    await ctx.send ("Item removido com sucesso no banco Replit.")
  
  @commands.command()
  async def devlistaitenstp(self, ctx):
    keys = db.keys()
    k = str(keys)
  
    nomes = k.replace("{", "").replace ("'", "").replace("}","").replace(" ", "").replace(",", " ")
    nomes = nomes.split()
  
    itens = []
    for n in nomes:
      if "item" in n:
        itens.append(n)
  
    itensTP = str(itens).replace("item_", "").replace("[", "").replace("'", "").replace("]", "\n")

    texto = f"**Esses são os itens cadastrados na Taverna Planar:** \n{itensTP}"
    await ctx.send(texto)

#Adicionando o cog ao bot
def setup (client):
  client.add_cog(Dev(client))