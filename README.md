# Bot Taverneira

# Introdução

A bot taverneira é um bot desenvolvido para o discord utilizando a linguagem Python e a biblioteca [discord.py](https://discordpy.readthedocs.io/en/stable/) em sua versão mais recente. A finalidade da taverneira é unir comandos que melhoram a experiência de uma mesa de RPG, adicionando coleções de músicas para ambientes e geradores de personagens para gerar esqueletos de histórias. 

# Desenvolvimento

Pacotes:

- [discord.py](https://pypi.org/project/discord.py/)

To get voice support you should also run the following command:
Linux -> python3 -m pip install -U "discord.py[voice]"
Windows -> py -3 -m pip install -U discord.py[voice]

- [dotenv](https://pypi.org/project/python-dotenv/)
- [ffmpeg](https://pypi.org/project/ffmpeg/)

# Comandos

## Utilitários

~~!comandos~~
*Status: Para remção.*

~~!mesas~~
*Status: Completo.*

### !help

Lista todos os comandos com uma descrição breve de cada um deles.
*Status: Completo.*

## Geradores

### !gerarpersonagem

O gerador de personagem randomiza características de personagem para criar um esqueleto interessante que fornece características, eventos de vida, objetivos, segredos, traços positivos e negativos de personalidade, maneirismos, familiares e mais. 

*Status: Incompleto.* 

### !nomef e !nomem

Gerador de nomes femininos e masculinos.

*Status: Em breve.* 

### !gerarquest

Gerador de quests para fornecer ideias de missões ou pequenos acontecimentos que possam vir a acontecer em sua aventura. Este esqueleto fornece 

*Status: Em breve.*

### !gerarcampanha

Gerador de campanhas para fornecer ideias centrais, vilões e acontecimentos que possam gerar uma trama. Este esqueleto fornece 

*Status: Em breve.*

## Músicas

### !join

Permite ao bot ingressar no canal de voz onde você se encontra. 
*Status: Completo.*

Nunca se esqueça de usar o !join antes de pedir por alguma música, seja das coleções abaixo ou de um link direto do youtube.

### !musicas

Retorna a lista de comandos para os tipos de música disponíveis. As músicas são separadas por contexto e, ao chamar um comando, a taverneira escolhe uma música aleatória dentro do contexto escolhido para tocar. 

!ambientefantasia
!ambientesombrio
!combatecomum
!combateepico
!combatesombrio  

*Status: Mais opções em breve.* 

### !play

O comando play deve estar acompanhado de uma url do youtube para que ele possa tocar uma música do youtube no canal de voz. Não se esqueça do comando !join para que ele entre no canal antes de usar o !play
*Status: Completo.*

### !leave

Quando você quiser que o bot saia do canal onde ele se encontra, basta usar esse comando e ele será desconectado.
*Status: Completo.*

## Load (Desenvolvimento)

### !load

Carregar um cog específico. Digite load e o nome do cog.
*Status: Completo.*

### !unload

Descarregar um cog específico. Digite load e o nome do cog. 
*Status: Completo.*

### !reload

Recarregar um cog espeífico. Digite load e o nome do cog.
*Status: Completo.*
