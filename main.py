import os
import discord
from replit import db
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
client = commands.Bot (command_prefix = "!", help_command=None)

#Retornando um print para saber que o bot foi inicializado
@client.event
async def on_ready():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      client.load_extension (f'cogs.{filename[:-3]}')
      print("Bot pronto para uso.")

#Redefinição do comando de Help
@client.command()
async def help(ctx):
  await ctx.send("**Bem vindo a taverna, aventureiro**! \n Aqui estão os comandos disponíveis e suas descrições. \n \n **Comandos para controlar o bot de música:** \n!join             *Entrar em um canal de voz.* \n!leave            *Sair do canal de voz.* \n!play            *Tocar a música do fornecido.* \n!pause            *Pausar a música.* \n!stop             *Parar a música.* \n!resume           *Continua a música.* \n \n **Comandos para tocar músicas aleatórias baseadas em um tópico:** \n!ambientecalmo    *Música de Ambiente Calmo.* \n!ambienteepico    *Música de Ambiente Calmo.* \n!ambientefantasia    *Música de Ambiente Fantasia.* \n!ambienteinfernal    *Música de Ambiente Infernal.* \n!ambientesombrio    *Música de Ambiente Sombrio.* \n!combatecomum     *Música de Combate Comum.* \n!combateepico     *Música de Combate Épico.* \n!combatesombrio   *Música de Combate Sombrio.* \n!kasinao          *Música do Kasinão.* \n \n **Comandos para utilizar a Loja Planar:** \n!regrastp     *Regras da Loja Planar.* \n!jogadorestp     *Jogadores cadastrados na Loja Planar.*\n!itenstp     Itens disponíveis na Loja Planar.* \n!entrartp     *Se cadastrar na Loja Planar.*\n!sairtp     *Sair da Loja Planar.*\n!addmoedastp     *Adicionar moedas para um jogador.*\n!remoedastp     *Remover moedas de um jogador.* \n!saldoslp     *Saldo dos jogadores.* \n!comprartp     *Comprar um item da Loja Planar.*\n!bolsatp     *Quais itens o jogador comprou.*\n \n **Comandos para ajudar na criação de personagens e NPCs:** \n!gerarpersonagem     *Gerar informações genéricas e divertidas.* \n\n")

#Faz o bot rodar usando o token dele
keep_alive()
client.run(os.environ['TOKEN'])
