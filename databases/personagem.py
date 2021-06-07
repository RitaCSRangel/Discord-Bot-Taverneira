genero = ["Feminino", "Masculino", "Outro"]

raca = [
    "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Orc",
    "Human", "Catfolk", "Dhampir", "Drow", "Goblin", "Hobgoblin", "Kitsune",
    "Kobold", "Oread", "Ratfolk", "Samsaran", "Tengu", "Sylph", "Undine",
    "Vanara", "Lizardfolk", "Ifrit", "Aasimar"
]

idade = [
    "20 anos ou menos (1 evento marcante).",
    "21 a 30 anos (2 eventos marcantes).",
    "31 a 40 anos (3 eventos marcantes).",
    "41 a 50 anos (4 eventos marcantes).",
    "51 a 60 anos (5 eventos marcantes).",
    "61 anos ou mais (5 eventos marcantes)."
]

pais = [
    "Você sabe quem seus pais são e onde eles estão.",
    "Você não sabe quem seus pais são e onde eles estão.",
    "Você sabe quem seus pais são mas não sabe onde estão."
]

mestico = [
    "Ambos os seus pais são humanos, você nasceu diferente do restante da sua família por algum motivo.",
    "Um dos seus paie é humano e o outro é um não humano.",
    "Ambos os seus pais são não humanos."
]

familia = [
    "Não possui nenhum familiar.",
    "Sua família é uma instituição, como um asilo.",
    "Os membros de um orfanato são sua família.",
    "Sua família são os membros de um templo.",
    "Você foi criado por parentes próximos, como tios, ou amigos da família.",
    "Você foi criado por um ou os dois avós.",
    "Você foi criado por uma família adotiva.",
    "Você foi criado pelo seu pai ou padrasto.",
    "Você foi criado por sua mãe ou madrasta.",
    "Você foi criado por ambos os seus pais."
]

pais_ausentes_causa = [
    "Seu pai (pais) morreram.",
    "Seu pai (pais) foi aprisionado, escravizado ou levado de alguma maneira.",
    "Seu pai (pais) te abandonaram.",
    "Seu pai (pais) desapareceram misteriosamente."
]

pais_mortos_causa = [
    "Desconhecida.", 
    "Assassinato.", 
    "Morte em batalha.",
    "Acidente de trabalho.", 
    "Acidente.", 
    "Causas naturais.", 
    "Suicídio.",
    "Vítima de um animal selvagem.", 
    "Vítima de um disastre natural.",
    "Executado por um crime.", 
    "Torturado até a morte.",
    "Evento bizarro, como ser atingido por um meteorito, abatido por um deus zangado etc."
]

local_nascimento = [
  "Você nasceu em casa.",
  "Você nasceu na casa de um amigo de família.",
  "Você nasceu na casa de um curandeiro ou parteira.",
  "Você nasceu em uma carroça/carruagem/vagão.",
  "Você nasceu em um celeiro ou galpão.",
  "Você nasceu em uma caverna.",
  "Você nasceu em um campo.",
  "Você nasceu em uma floresta.",
  "Você nasceu em um templo.",
  "Você nasceu em um campo de batalha.",
  "Você nasceu em uma rua/ruela.",
  "Você nasceu em um bordel, estalagem ou taverna.",
  "Você nasceu em um castelo, torre, forte ou palácio.",
  "Você nasceu nos esgotos.",
  "Você nasceu em entre membros de uma raça diferente da sua.",
  "Você nasceu em um barco.",
  "Você nasceu em uma prisão.",
  "Você nasceu em no quartel de uma organização secreta.",
  "Você nasceu em um laboratório.",
  "Você nasceu no plano das fadas.",
  "Você nasceu no plano das sombras.",
  "Você nasceu em um plano transitivo a sua escolha.",
  "Você nasceu em um plano externo a sua escolha."
]

memorias_infancia = [
    "Ainda sou assombrado pela minha infância, quando fui maltratado.",
    "Passei a maior parte da minha infância sozinho e sem amigos.",
    "Os outros me viam como estranho ou diferente, então eu tinha pouquíssimos colegas.",
    "Eu tinha alguns amigos próximos e vivi uma infância comum.",
    "Eu tive vários amigos e me lembro de ter uma infância feliz.",
    "Eu sempre tive facilidade em fazer amigos e tive uma infância rodeada de pessoas.",
    "Todos sabiam quem eu era e eu tinha amigos por todos os cantos."
]

estilo_de_vida = [
    "Faminto.", "Miserável.", "Pobre.", "Modesto.", "Confortável.", "Nobre."
]

objetivos = [
    "Ter uma boa noite de sono.", 
    "Mentorar uma criança.",
    "Provar suas origens nobres.", 
    "Visitar a póxima vila.",
    "Resolver um mistério sobre o qual ninguém mais se importa.",
    "Adquirir dinheiro o suficiente para se aposentar.",
    "Escalar uma grande montanha.",
    "Obter uma reputação melhor (ou diferente) da que tem agora.",
    "Fazer amizade com alguém ou um grupo específico.",
    "Apagar as falhas do passado com um único ato dramático.",
    "Sair da casa dos pais.", 
    "Melhorar a condição física e aprender a lutar.",
    "Ver o mar.",
    "Ver um texto bíblico em especial, uma construção específica ou um Afresco.",
    "Encontrar um novo lar para um animal maltratado.",
    "Ler os livros históricos.", 
    "Voltar ao lar apesar dos obstáculos.",
    "Superar um terrível vício pessoal.",
    "Conseguir provas de que a vida após a morte existe.", 
    "Viajar.",
    "Se casar.", 
    "Humilhar um rival.", 
    "Encontrar uma criança perdida.",
    "Aprender a arte da aposta.", 
    "Carregar a tradição da família.",
    "Partir em uma peregrinação.", 
    "Se casar com o seu amor de infância.",
    "Gravar um texto sagrado na memória.",
    "Completar uma espécie de trabalho artistico (pintura, estátua, etc).",
    "Encontrar um trabalho melhor.", 
    "Evitar a falência.",
    "Impressionar os pais que te desaprovaram.",
    "Impressionar um interesse amoroso.", 
    "Atingir um nível social mais alto.",
    "Começar o seu próprio negócio.", 
    "Se tornar o recipiente de um milagre.",
    "Ajudar uma criança a ter uma nova vida.", 
    "Redimir o nome da família.",
    "Caçar e matar um monstro.", 
    "Resolver um assassinato.",
    "Proteger a sua terra natal.", 
    "Liderar um país.",
    "Se casar com um príncipe/princesa.", 
    "Se tornar um herói.",
    "Se tornar um monstro.", 
    "Se curar de uma doença ou outra efermidade.",
    "Assassinar alguém.", 
    "Ver um anjo.", 
    "Descobrir o significado da vida.",
    "Atravessar os mares.", 
    "Descobrir algo importante.", 
    "Obter vingança.",
    "Se redimir por um erro do passado.", 
    "Remover uma maldição.",
    "Vingar a própria mãe.",
    "Descobrir o que aconteceu com o seu/sua mentor (a)."
]

segredo = [
    "Sabe onde um item mágico está enterrado.",
    "Conhece o melhor local de pesca.", 
    "Está tendo um caso.",
    "Rouba de seus vizinhos.",
    "Sabe cozinhar com segurança um peixe venenoso.",
    "Sabe por que ninguém mais nada no lago do moinho.",
    "Está fazendo bebidas alcoólicas ilegalmente.", 
    "Sabe quem é o assassino.",
    "Perdeu a posição de paladino devido à covardia.",
    "É um paladino trabalhando disfarçado.", 
    "Bebe muito.",
    "Está sendo chantageado.", "Sabe o que aconteceu com todos os ratos.",
    "Está secretamente relacionado a outro NPC.", 
    "É um mentiroso habitual.",
    "Ouve vozes no cemitério.", 
    "É um espião.",
    "Conhece o lanche favorito de um determinado monstro.",
    "Sabe a localização de um esconderijo de bandidos.", 
    "É religioso.",
    "É um colecionador (a) obsessivo.",
    "Conhece a maneira correta de ler um mapa do tesouro.",
    "É espancado pelo cônjuge.", 
    "Tem um estoque secreto de fundos.",
    "Conhece a palavra de comando para um item mágico.",
    "Envolve-se em algum comportamento desviante.",
    "Sabe como fazer o oráculo responder com sinceridade.",
    "Sabe porque mais come carne na aldeia.", 
    "Tem uma doença secreta.",
    "É um assassino.", "Sabe onde é possível entrar em contato com as fadas.",
    "Sabe quem realmente comanda a região.", 
    "Faz doações secretas.",
    "Assassinou alguém.", 
    "É procurado por um crime.",
    "É membro de um culto local secreto.",
    "Sabe como aplacar um fantasma zangado.",
    "Era uma criatura muito diferente antes da reencarnação.",
    "Tem uma identidade secreta.", 
    "Conhece algum segredo local.",
    "Adora uma divindade maligna.",
    "Deve fundos substanciais ao agiota local.",
    "Sabe que alguém não é o que parece ser.", 
    "Sabe onde o meteoro caiu.",
    "Tem sangue de troll na família.", 
    "Tem sangue orc na família.",
    "Tem medo de um determinado tipo de monstro.",
    "Sabe quando o herdeiro (a) do trono foge para visitar um (a)camponês (a) atraente.",
    "É o filho bastardo de um nobre."
]

background = [
    "Veterano militar.",
    "Criminoso reformado.",
    "Vem de uma longa linhagem de artesãos.",
    "Refugiado de terras invadidas pelo mal.",
    "Ex-prostituta.",
    "Lutou do lado perdedor em uma guerra civil/revolução.",
    "Nobre desonrado.",
    "Ex-assistente de um laboratório.",
    "Já teve uma pousada que foi queimada por bandidos.",
    "Falsamente condenado que depois fugiu da prisão.",
    "Escravo fugitivo.",
    "Matou alguém em legítima defesa.",
    "Companheiro de infância de alguém importante.",
    "Viciado que atualmente está em recuperação.",
    "Órfão.",
    "Criminoso que se aposentou após trair o resto da gangue.",
    "Deixado no altar.",
    "Fugiu de uma dívida.",
    "Piedoso membro de uma família notória.",
    "Perdeu um item mágico poderoso.",
    "Morreu, mas voltou por meio de magia.",
    "Praticou magia antes de um acidente traumatizante.",
    "Enganado por um monstro poderoso.",
    "Passou em um teste de guilda, mas ficou muito desiludido para entrar nela.",
    "Comerciante falido.",
    "Padre falido.",
    "Ex-criança doente que se curou milagrosamente como um adulto.",
    "Cônjuge e filhos abandonados.",
    "Fugiu jovem e entrou para um circo.",
    "Ex-servo contratado.",
    "Procurado por um crime grave.",
    "Prometeu guardar um segredo enorme.",
    "Ex-caçador de bruxas.",
    "Criado por membros de uma raça diferente.",
    "Ex-artista sofrendo de um bloqueio criativo.",
    "Costumava ter que implorar por comida.",
    "Perdeu um cônjuge ou filho.",
    "Inadvertidamente salvou a vida/planos de um vilão.",
    "Candidatou-se a um cargo público e sofreu uma derrota humilhante.",
    "Monstro reencarnado como humano.",
    "Oprimido por raça, sexualidade, religião, etc.",
    "Fugiu do próprio passado e hoje vive como se fosse otra pessoa.",
]

drawback = [
  "Apegado (Objeto): Você está apegado a um bem precioso com imenso valor sentimental e significado. Sem ele, você não é mais você mesmo e está sujeito a sofrer de depressão, mau humor ou comportamento agressivo.",
  "Apegado (Pessoa): Você está apegado a uma determinada pessoa - um amigo, membro da família ou ente querido - que significa mais do que qualquer coisa ou qualquer pessoa no mundo. Seus pensamentos sempre voltam para essa pessoa.",
  "Família: Sua família significa tudo para você e não há nada que você não faria por eles. Talvez seus laços se estendam a todo o seu clã ou linhagem, ou talvez haja um membro específico de sua família que você mantenha mais próximo do que qualquer outro.",
  "Justiça: Injustiças são intoleráveis. Sempre que você os testemunha, você se sente compelido a agir ou falar. Quando você é pessoalmente injustiçado, você precisa de apaziguamento - ou vingança.",
  "Amor: Seu amor por alguém te motiva. Quando essa pessoa está em perigo, você tende a se sentir fraco, impotente ou com raiva.",
  "Lealdade: Você valoriza a lealdade acima de todas as coisas. Você valoriza os amigos, associados e amantes que conquistou ao longo dos anos e, quando alguém quebra sua confiança ou o trai de alguma forma, você fica totalmente desequilibrado.",
  "Riqueza material: Você tem um fraco por coisas materiais - dinheiro, jóias finas, alimentos requintados, itens caros ou raros e assim por diante. Quando essas riquezas estão ao seu alcance, você é levado a possuí-las e as reivindica como um colecionador honesto ou um ladrão astuto.",
  "Prazer: Você anseia por luxo, entretenimento e prazer. Você pode se entregar a todas as fantasias passageiras ou resistir a uma tentação que constantemente o devora.",
  "Poder: Você anseia pela capacidade de influenciar o mundo ao seu redor, seja ele tão pequeno quanto uma aldeia ou tão grande quanto um plano de realidade.",
  "Orgulho: Você apresenta uma imagem para o mundo que não pode ser manchada. Quando alguém questiona seus motivos, critica suas ações ou insulta sua honra ou orgulho, você questiona sua amizade ou o considera um de seus inimigos até que ele faça as pazes.",
  "Raça: Você se sente realmente confortável apenas perto de outros de sua raça e tem dificuldade em depositar fé ou confiança naqueles de raças diferentes da sua.",
  "Religião: Suas crenças são fundamentais importância em sua vida, quer você pertença a um templo, siga um culto ou pratique uma filosofia religiosa de forma independente. Quando outros questionam ou atacam as crenças, princípios, relíquias ou estruturas de sua fé, você responde com fúria.",
  "Reputação ou Fama: Você trabalhou muito para estabelecer sua identidade e reputação, e alguém que calunia ou insulta você deve responder por isso. Você se esforça para promover sua identidade a ponto de todos conhecerem sua reputação.",
  "Proteção ou segurança: Você é cauteloso e protegido - desconfie de outras pessoas que possam prejudicá-lo, roubá-lo ou trair sua confiança. Como tal, você dorme leve, sempre suspeitando que alguém ou algo se esgueirou sobre você no escuro. Até quando se relaciona com pessoas que confiam em você, sempre há o medo de que elas abriguem agendas ocultas ou mudem e se voltem contra você.",
  "Dúvida pessoal: Não importa o que você faça, nunca é bom o suficiente. Você não pode deixar de ver em suas vitórias muitas pequenas derrotas e fracassos. Se você fosse mais forte, mais inteligente, mais rápido ou mais poderoso, talvez pudesse ser melhor. No entanto, preso no corpo e na mente que você tem, você sente que está destinado ao fracasso.",
  "Aceitação Social: Você quer que os outros o aceitem, que acreditem que você é especial e digno de mérito. Você está autoconsciente sobre suas falhas sociais e violações de etiqueta. A rejeição está entre seus maiores medos. Você pode ir a extremos para ser aceito ou buscar o favor de seus colegas.",
  "O Futuro: Suas preocupações não estão com o presente, mas com a preparação para o futuro. Você pode ser um planejador ávido e organizado, ou talvez veja os sinais de uma era das trevas que se aproxima ou de tempos difíceis. Você se comporta de maneira cautelosa, conservadora e metódica ao planejar eventos que podem ocorrer um dia.",
  "O Passado: Você deseja que o mundo volte a uma era passada. Você adotou as maneiras e o estilo desta época e está fascinado por seus costumes, relíquias e artefatos, e pelas figuras históricas da época. Talvez você viva tanto nesta era passada que sua conexão com o presente seja tênue. Ou sua pretensão irrita os outros.",
  "Visão de mundo: em seus olhos, sua moral filosofia - o seu alinhamento - é o único maneira correta e verdadeira do mundo. Talvez você gentilmente tenha pena, discuta ou brigue com aquelas almas desorientadas que não vêem o mundo do seu jeito ou pela luz da razão.",
  "Juventude: Você reflete sobre sua juventude como uma época de ouro, uma época sempre presente em sua mente e que se recusa a desaparecer no segundo plano. Todos os dias, você se sente ficando mais velho e mais perto do seu fim inevitável. Você busca maneiras de fazer você parece e se sente jovem na tentativa de reacender aquele fogo de sua adolescência, mas apesar de suas tentativas, você percebe que seu tempo ainda se aproxima cada vez mais."
]

evento_maior = [
  "Treinamento da Academia - Você frequentou uma academia particular onde estudou uma série de habilidades e obteve treinamento em sua profissão atual. Quer você tenha sido um aluno brilhante ou um desistente, o ambiente universitário foi sua casa durante boa parte de seus anos de formação.",
  "Traição - Um amigo ou membro da família em quem você confiava mais do que qualquer outra pessoa o traiu. Você nunca confiou totalmente em ninguém desde então e prefere confiar em suas próprias habilidades em vez de confiar nos outros.",
  "Intimidado - No início da sua vida, você foi uma vítima - presa fácil para aqueles mais fortes ou mais espertos do que você. Eles batiam em você quando podiam, usando você como esporte. Este abuso alimentou uma poderosa chama de vingança.",
  "Campeão da competição - Você se destacou desde muito cedo quando venceu uma competição. Isso pode ter sido uma competição marcial de armas, uma exibição de magos aprendizes, apostas altas ou algo mundano como um campeonato de comer.",
  "Morte na Família - Você foi profundamente afetado pela morte do parente mais próximo a você - um pai, avô, irmão favorito, tia, tio ou primo. Essa morte o afetou profundamente e você nunca foi capaz de abandoná-la.",
  "Morreu - você morreu ou chegou tão perto da morte que percorreu a fronteira entre os reinos dos vivos e dos mortos. Tendo passado do domínio da vida uma vez, você tem uma perspectiva única da vida, talvez até uma apreciação maior por ela - ou talvez sua experiência o tenha feito rejeitar todas as coisas triviais, focando apenas em questões de verdadeira importância.",
  "Queda de uma potência importante - Em seus primeiros anos, uma antiga potência com influência de longo alcance entrou em declínio. Pode ter sido um império, uma grande organização ou gangue, ou uma pessoa como um rei benevolente ou um ditador maligno. Suas primeiras memórias foram fundadas em um mundo onde este grande poder afetou sua região para o bem ou para o mal.",
  "Caiu com uma multidão má - Em sua juventude, você correu com uma multidão brutal, malvada ou sádica. Você pode ter pertencido a uma gangue, associação de ladrões ou alguma outra organização nefasta. Foi fácil ceder à pressão e fazer o que quer que eles mandassem, e sua visão é colorida pela ambigüidade moral. Você ganha acesso ao traço social Child of the Streets.",
  "Primeira morte - você tem sangue nas mãos desde a juventude, quando tirou a vida de outra criatura pela primeira vez. Se esse ato o repeliu ou lhe deu prazer, foi uma experiência formativa.",
]

evento_menor = [
  "Em breve."
]

tracos_negativos = [
  "Em breve."
]

tracos_positivos = [
  "Em breve."
]

maneirismo = [
  "Em breve."
]

circunstancia_crime = [
  "Você não cometeu o crime e foi exonerado depois de ser acusado.",
  "Você cometeu o crime ou ajudou a fazê-lo, mas no entanto, as autoridades o consideraram inocente.",
  "Você quase foi pego em flagrante. Você teve que fugir e agora é um procurado na comunidade onde o crime ocorreu.",
  "Você foi pego e condenado. Você passou um tempo cadeia, acorrentado a um remo ou realizando trabalho duro. Você cumpriu uma sentença dealguns anos ou conseguiu escapar depois de muito tempo."
]

crime = [
  "Assassinato",
  "Roubo",
  "Agressão",
  "Contrabando",
  "Sequestro",
  "Extorção",
  "Falsificar"
]

aventura = [
  "Você quase morreu. Você tem cicatrizes desagradáveis no seu corpo e alguns pedaços faltando.",
  "Você sofreu uma lesão grave. Embora a ferida tenha sido curada, ainda te machuca de vez em quando.",
  "Você contraiu uma doença enquanto explorava. Você se recuperou da doença, mas uma tosse persistente, marcas na pele ou cabelos prematuramente grisalhos ficaram como marca.",
  "Você foi envenenado por uma armadilha ou um monstro. Você se recuperou, mas você se tornou paranóico com isso e sempre compra antídotos.",
  "Você perdeu algo de valor sentimental para você durante a sua aventura e sempre se lembra dela.",
  "Você ficou terrivelmente assustado com algo que encontrou e fugiu, abandonando seus companheiros ao destino deles.",
  "Você aprendeu muito durante sua aventura e se tornou um explorador experiente.",
  "Você encontrou um item adormecido e carrega esse item com você desde então, esperando descobrir do que se trata."
]

condicao_nascimento = [
  "Nascimento de classe baixa - Você nasceu entre camponeses ou habitantes de favelas. Você cresceu trabalhando na terra em torno de uma vila ou mansão, praticando um comércio rudimentar ou implorando por um acordo.",
  "Nascimento da classe média - Você nasceu na classe média, que inclui comerciantes, artesãos e comerciantes. Você provavelmente cresceu em um assentamento de bom tamanho, e um de seus pais provavelmente está associado a uma guilda ou outra organização comercial. Como pessoa livre, você não experimenta a escravidão da servidão ou do campesinato, mas também não tem o privilégio da nobreza.",
  "Nascimento nobre - Você nasceu para privilegiar a nobreza. A menos que um de seus pais seja o regente, sua família serve um nobre mais alto, mas nobres menores servem sua família.",
  "Adotado fora da sua raça - Você não foi criado por sua família biológica e cresceu em uma família de raça diferente da sua.",
  "Adotado - Você não foi criado por sua família biológica, mas acolhido por outra família de sua raça ou cultura.",
  "Nascido bastardo - Seus pais tiveram um encontro que resultou em seu nascimento fora do casamento. Você conhece um de seus pais, mas o outro permanece desconhecido ou uma presença distante na melhor das hipóteses.",
  "Nascimento Abençoado - Quando você nasceu, você foram abençoados por um ser de grande poder como um anjo, azata ou gênio. Essa bênção o protegeu de certos perigos ou o marcou como especial para alguma divindade.",
  "Nascido da violência - Seu nascimento foi causado por meios violentos e sem vontade. Você tem um pai e o outro provavelmente permanece desconhecido.",
  "Nascido fora do tempo - Você nasceu em uma era diferente, seja no passado distante ou no futuro distante. Algum evento o desalojou do seu tempo, e os costumes e costumes do presente lhe parecem estranhos e estranhos.",
  "Nascido em Bondage - Você nasceu em escravidão ou servidão. Seus pais provavelmente são escravos ou criados, ou você foi vendido como escravo quando criança.",
  "Nascimento Amaldiçoado - Quando você nasceu, uma poderosa entidade diabólica contaminou seu sangue de alguma forma e o amaldiçoou como um agente da profecia sombria.",
  "Família Desonrada - Você nasceu em uma família que já foi homenageada em sua sociedade, mas que caiu em desgraça. Agora seu nome de família é odiado e difamado por aqueles que conheça, colocando você em guarda.",
  "Herdeiro de um legado - Você é o herdeiro de uma família com um nome antigo e um passado distinto. Sua família pode ser rica ou de classe média, mas seu próprio nome vale o dobro de sua fortuna.",
  "Deixado para morrer - Quando você nasceu, você foi deixado para morrer, mas por alguma reviravolta das circunstâncias, você sobreviveu.",
  "Marcado pelos deuses - Uma divindade marcou você. Essa marca pode estar em seu corpo ou em sua alma.",
  "Energia Infundida - Durante o seu nascimento, você foi exposto a uma potente fonte de energia divina.",
  "Progênie do Poder - Você nasceu durante uma conjunção particularmente poderosa ou em algum outro período de poder.",
  "Profetizado - Seu nascimento foi predito, tão recentemente quanto na última geração, já em milhares de anos atrás.",
  "Reencarnado - Você renasceu em muitos ciclos e pode renascer em muitos outros até que você realize a tarefa final para a qual está destinado.",
  "O presságio - os sábios, sacerdotes ou bruxos de sua sociedade decretaram seu nascimento como um presságio de uma era ou evento que se aproxima - talvez você seja um presságio de promessa, talvez um dos tempos sombrios pela frente."
]

conhecido = [
  "O Caçador - Essa pessoa era um lobo solitário que, no entanto, permitiu que você se tornasse um membro de sua matilha solitária. Ela o ensinou a prosperar sozinho, apesar dos muitos perigos e perigos naturais de seu ambiente nativo.",
  "O Pária - Você conheceu um exilado em desgraça e encontrou em suas palavras e atitudes algo que falou com você. O que antes parecia verdadeiro em sua religião, sociedade ou família começou a parecer falso quanto mais tempo você passava com essa pessoa, e você rapidamente aprendeu a não confiar em todos que encontra - especialmente entre aqueles que afirmam ser mais merecedores disso.",
  "O Confidante - Havia uma pessoa em sua vida a quem você poderia contar qualquer coisa. Ela conhece seus segredos mais profundos e suas fraquezas e vulnerabilidades emocionais, assim como você conhece as dela. Esta pessoa pode ser um amigo valioso e um inimigo assustador, por isso certifique-se de nunca divulgar seus segredos ou dar-lhe um razão para fazer isso com o seu.",
  "O Mentor - Você teve um mentor que lhe ensinou tudo que vale a pena saber sobre a vida. Esta poderia ter sido a pessoa que lhe ensinou o heróico habilidades que você possui, ou simplesmente uma alma gêmea que ajudou a formar sua visão de mundo",
  "O Mercenário - Com essa pessoa, sempre havia um custo. Nenhuma ação foi feita em troca de algo de valor igual ou superior. Quer as ações desse indivíduo tendam ao bem, ao mal ou ao equilíbrio puro, ele sempre foi justo em seus tratos.",
  "O Amante - Você teve uma conexão romântica na adolescência e essa pessoa influenciou profundamente sua personalidade. Talvez este tenha sido um primeiro amor, um parceiro casual de quem você se aproximou ou aquele que fugiu. A experiência reforçou sua confiança nas interações românticas, embora você frequentemente descubra que seus pensamentos ainda estão se voltando para aquela pessoa especial de muito tempo atrás.",
  "O Louco - Um de seus amigos mais próximos era um palhaço que zombava de decoro e costume, em vez de se envolver em ações selvagens e um tanto aleatórias de vez em quando. Depois de um tempo, você aprendeu que havia sabedoria simples nessa tolice - uma visão de mundo descuidada que o ensinou a abandonar a preocupação.",
  "O Lorde Soberano - Você se tornou próximo de alguém a quem deveria servir, seja um senhor ou senhora menor, mestre (no caso de um escravo), príncipe ou princesa, rei ou rainha. Embora essa pessoa tivesse poder sobre você, ela o mantinha mais perto do que um súdito ou servo. Como resultado, você está acostumado a lidar e estar perto do poder, e seu nome é conhecido entre os privilegiados.",
  "O Parente - Há um parente de quem você era especialmente próximo. Para você, essa pessoa era o significado de família. Ele ajudou a conduzi-lo até a idade adulta, ensinando-lhe tudo o que você sabe sobre o mundo. Você está ligado a essa pessoa ou à sua memória e se esforça para cumprir uma promessa, voto ou juramento que fez a ela.",
  "O Chefe - Uma vez você conseguiu emprego sob um indivíduo organizado e poderoso com ampla influência. Quando o chefe estava presente, todos ouviam. Isso poderia ter sido um militar comandante, chefe tribal, líder de guilda ou líder de gangue. Com o chefe, você aprendeu como fazer as pessoas ouvirem, fazer com que vejam a razão e mantê-las na linha.",
  "A Acadêmica - Uma de suas associadas tinha tal desejo por conhecimento que ela nunca se satisfaria com respostas simples ou soluções óbvias. Este desejo de conhecimento freqüentemente excedeu sua necessidade de companhia, mas você era a única exceção. Por meio dessa associação, você desenvolveu um grande apreço por números, geometria, lógica, estudo árduo e solução de problemas.",
  "O Criminoso - Um de seus associados cometeu crimes regularmente. Ele o regalou com muitas histórias de ousados ​​roubos e arrombamentos - e talvez até assassinatos. Você aprendeu a maior parte do que você conhece o elemento criminoso dele, e ele confiou em você como um amigo.",
  "O Vidente - Você estava perto de uma pessoa que afirmava ver o futuro - talvez um oráculo, vidente, profeta ou simplesmente algum charlatão de festival. Quer sejam verdadeiras ou um truque, você já teve visões de lugares distantes e de tempos que podem chegar a passar. A influência do vidente tornou você um otimista com um impulso para mudar o futuro ou um fatalista resignado em aceitá-lo.",
  "O Místico - Você era especialmente próximo de uma pessoa sagrada em sua comunidade que mudou fundamentalmente sua vida ao abrir seus olhos para os incríveis poderes que existem além do natural mundo. Independentemente de você seguir uma fé, certos artefatos, rituais e textos religiosos desempenharam um grande papel em fazer de você a pessoa que você é.",
  "O Morto - Uma de suas maiores influências foi uma criatura morta-viva sensível, como um fantasma, lich, cavaleiro da sepultura, espectro ou vampiro. Você o encontrou em várias ocasiões e sobreviveu ... principalmente ileso. Por meio desse estranho relacionamento, você aprendeu sobre sua vida mortal, dando-lhe uma perspectiva sobre sua própria vida.",
  "O Demônio - Na sua adolescência, você tratou ou foi possuído por um demônio que lhe emprestou poder bruto em um momento de grande necessidade. Essa experiência contaminou seu corpo e sua mente e mudou sua vida. Alguma parte do demônio permanece dentro de você como um velho amigo, influenciando você para fins destrutivos.",
  "O Viajante - Você conheceu alguém que viajou de um lugar para outro com a mudança do vento, como um menestrel, presidiário, comerciante, proscrito, soldado ou marinheiro. Esta pessoa trouxe lembranças maravilhosas e falou de todos os lugares ele viajou e as pessoas que viviam lá, inspirando um desejo de viajar dentro de você.",
  "O campeão - você era próximo de alguém que se destacava em empreendimentos atléticos e testes de força ou habilidade. Por meio de sua amizade ou rivalidade, você desenvolveu o espírito competitivo que continua a conduzi-lo em tudo o que você faz.",
  "O Artesão - uma de suas principais influências acarinhava a perfeição em todas as formas de arte. Essa pessoa pode ter seguido qualquer caminho na vida, do artesão ao artista e ao assassino. Com essa pessoa, você desenvolveu uma mente disciplinada, um foco solitário e a capacidade de criar algo útil e belo.",
  "Amigo bem conectado - em seu círculo de associados díspares, havia alguém que todos conheciam. Esta pessoa colecionava amigos como troféus, e ela tinha contatos em todas as áreas sociais ou profissionais círculo. Por meio dessa conexão, você continua a se encontrar e a se associar com uma ampla variedade de pessoas em todas as áreas da vida."
]

trabalho = [
  "Academico que recebe financiamento para seus estudos.",
  "Aventureiro que sobrevivia de seus ganhos nas aventuras.",
  "Aristocrata que trabalhava como escriba.",
  "Artesão.",
  "Performance.",
  "Mercenário.",
  "Fazendeiro que vivia de sua produção.",
  "Caçador.",
  "Mercador.",
  "Marinheiro.",
  "Soldado."
]