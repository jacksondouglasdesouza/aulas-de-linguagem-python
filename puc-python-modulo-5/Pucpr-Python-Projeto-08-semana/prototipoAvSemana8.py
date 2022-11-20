# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas — PUCPR
# PROJETO FINALIZADO — AV SEMANA 08
# Aluno: Jackson Douglas de Souza
#RA — 1112022209646
# Matéria: Raciocínio Computacional

import random

#➤➤➤➤➤➤ ESTILO - OK REVISADO
def quadros():
    '''
    Estilização do código.
    :return: quadrados na horizontal
    '''

    return print("▓▓▓▓▓" * 9)


def linhas():
    '''
    Estilização do código.
    :return: linhas na horizontal
    '''

    return print("—" * 45)

#➤➤➤➤➤➤ FACES DOS DADOS - OK REVISADO

verde = ["C", "P", "C", "T", "P", "C"]
amarelo = ["T", "P", "C", "T", "P", "C"]
vermelho = ["T", "P", "T", "C", "P", "T"]
dados = ["Verde", "Verde", "Verde", "Verde", "Verde", "Verde", "Amarelo", "Amarelo", "Amarelo", "Amarelo",
         "Vermelho", "Vermelho", "Vermelho"]

#➤➤➤➤➤➤ ROLAR OS DADOS - OK REVISADO

def RolarDados():

    escolha01 = random.choice(dados)
    escolha02 = random.choice(dados)
    escolha03 = random.choice(dados)
    print(escolha01)
    print(escolha02)
    print(escolha03)
    quadros()

    if escolha01 == "Verde":
        greenDice = random.choice(verde)
        print("🎲 O dado sorteado foi:🎲", greenDice)
        if greenDice == "C":
            quadros()
            print("Ponto")
            linhas()
        elif greenDice == "P":
            quadros()
            print("Dado Verde = Pegadas!")
            linhas()
        else:
            quadros()
            print("​😷​🤒​🤧​😫​")
            print("𝐕𝐎𝐂𝐄 𝐏𝐄𝐑𝐃𝐄𝐔 ０１ 𝐕𝐈𝐃𝐀!")
            linhas()
    elif escolha01 == "Amarelo":
        yellowDice = random.choice(amarelo)
        print("🎲 O dado sorteado foi:🎲", yellowDice)
        if yellowDice == "C":
            quadros()
            print("Ponto")
            linhas()
        elif yellowDice == "P":
            quadros()
            print("Dado Amarelo = Pegadas!")
            linhas()
        else:
            quadros()
            print("​😷​🤒​🤧​😫​")
            print("𝐕𝐎𝐂𝐄 𝐏𝐄𝐑𝐃𝐄𝐔 ０１ 𝐕𝐈𝐃𝐀!")
            linhas()
    else:
        redDice = random.choice(vermelho)
        print("Dado Vermelho : ", redDice)
        if redDice == "C":
            quadros()
            print("Ponto")
            linhas()
        elif redDice == "P":
            quadros()
            print("Dado Vermelho = Pegadas!")
            linhas()
        else:
            quadros()
            print("​😷​🤒​🤧​😫​")
            print("𝐕𝐎𝐂𝐄 𝐏𝐄𝐑𝐃𝐄𝐔 ０１ 𝐕𝐈𝐃𝐀!")
            linhas()

    if escolha02 == "Verde":
        greenDice = random.choice(verde)
        print("Dado Verde: ", greenDice)
        if greenDice == "C":
            quadros()
            print("Ponto")
            linhas()
        elif greenDice == "P":
            quadros()
            print("Dado Verde = Pegadas!")
            linhas()
        else:
            quadros()
            print("​😷​🤒​🤧​😫​")
            print("𝐕𝐎𝐂𝐄 𝐏𝐄𝐑𝐃𝐄𝐔 ０１ 𝐕𝐈𝐃𝐀!")
            linhas()
    elif escolha02 == "Amarelo":
        yellowDice = random.choice(amarelo)
        print("Dado Amarelo: ", yellowDice)
        if yellowDice == "C":
            quadros()
            print("Ponto")
            linhas()
        elif yellowDice == "P":
            quadros()
            print("Dado Amarelo = Pegadas!")
            linhas()
        else:
            quadros()
            print("​😷​🤒​🤧​😫​")
            print("𝐕𝐎𝐂𝐄 𝐏𝐄𝐑𝐃𝐄𝐔 ０１ 𝐕𝐈𝐃𝐀!")
            linhas()
    else:
        redDice = random.choice(vermelho)
        print("🎲 O dado sorteado foi:🎲", redDice)
        if redDice == "C":
            quadros()
            print("Ponto")
            linhas()
        elif redDice == "P":
            quadros()
            print("Dado Vermelho = Pegadas!")
            linhas()
        else:
            quadros()
            print("​😷​🤒​🤧​😫​")
            print("𝐕𝐎𝐂𝐄 𝐏𝐄𝐑𝐃𝐄𝐔 ０１ 𝐕𝐈𝐃𝐀!")
            linhas()

    if escolha03 == "Verde":
        greenDice = random.choice(verde)
        print("Dado Verde: ", greenDice)
        if greenDice == "C":
            quadros()
            print("Ponto")
            linhas()
        elif greenDice == "P":
            quadros()
            print("Dado Verde = Pegadas!")
            linhas()
        else:
            quadros()
            print("​😷​🤒​🤧​😫​")
            print("𝐕𝐎𝐂𝐄 𝐏𝐄𝐑𝐃𝐄𝐔 ０１ 𝐕𝐈𝐃𝐀!")
            linhas()
    elif escolha03 == "Amarelo":
        yellowDice = random.choice(amarelo)
        print("Dado Amarelo: ", yellowDice)
        if yellowDice == "C":
            quadros()
            print("Ponto")
            linhas()
        elif yellowDice == "P":
            quadros()
            print("Dado Amarelo = Pegadas!")
            linhas()
        else:
            quadros()
            print("​😷​🤒​🤧​😫​")
            print("𝐕𝐎𝐂𝐄 𝐏𝐄𝐑𝐃𝐄𝐔 ０１ 𝐕𝐈𝐃𝐀!")
            linhas()
    else:
        redDice = random.choice(vermelho)
        print("🎲 O dado sorteado foi:🎲", redDice)
        if redDice == "C":
            quadros()
            print("Ponto")
            linhas()
        elif redDice == "P":
            quadros()
            print("Dado Vermelho = Pegadas!")
            linhas()
        else:
            quadros()
            print("​😷​🤒​🤧​😫​")
            print("𝐕𝐎𝐂𝐄 𝐏𝐄𝐑𝐃𝐄𝐔 ０１ 𝐕𝐈𝐃𝐀!")
            linhas()


#➤➤➤➤➤➤ DADOS - OK REVISADO

dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"

playGame = False

caixadeDados = []
listPlayers = []

def adicionarDados():
    '''
    Essa função adcionar os dados na lista caixa de dados.
    :return: Dados
    '''

    for i in range(0, 6):
        caixadeDados.append(dadoVerde)
    for i in range(0, 4):
        caixadeDados.append(dadoAmarelo)
    for i in range(0, 3):
        caixadeDados.append(dadoVermelho)

dadosJogador = []

def jogarDados():
    '''
    Essa função joga os dodos.
    :return:  Dados sorteados.
    '''

    dadosJogador.clear()
    for i in range(0, 3):
        dadosJogador.append(random.choice(caixadeDados))

def mostrarPacar():
    '''
    Essa função exibe o placar para o párticipante.
    :return: Placar do jogo
    '''

    print(" ")
    quadros()
    print(" 🅿🅻🅰🅲🅰🆁  🅳🅰  🆁🅾🅳🅰🅳🅰 ")
    print(f"{listPlayers}\n")

opção = 0

#➤➤➤➤ ABERTURA DAS JOGADAS - OK REVISADO

while opção != 4:
    quadros()
    print("▓▓▓▓▓ 𝓑ᴇ𝓜 𝓥𝓘𝓝𝓓𝓞 𝓐𝓞 𝓙𝓞𝓖𝓞 𝓩𝓞𝓜𝓑𝓘𝓔 𝓓𝓘𝓒𝓔 ▓▓▓▓▓")
    linhas()
    print("▁▂▃▄▅▆▇█ １ 𝐈𝐍𝐈𝐂𝐈𝐀𝐑 𝐍𝐎𝐕𝐎 𝐉𝐎𝐆𝐎 █▇▆▅▄▃▂▁\n"
          "▁▂▃▄▅▆▇█ ２ 𝐏𝐎𝐍𝐓𝐔𝐀𝐂𝐀𝐎        █▇▆▅▄▃▂▁\n"
          "▁▂▃▄▅▆▇█ ３ 𝐓𝐈𝐑𝐀𝐑 𝐉𝐎𝐆𝐀𝐃𝐎𝐑    █▇▆▅▄▃▂▁\n"
          "▁▂▃▄▅▆▇█ ４ 𝐒𝐀𝐈𝐑              █▇▆▅▄▃▂▁\n")
    quadros()
    opção = int(input("➤➤ Escolha uma Opção! 🧟‍♂​🧠​🧟‍♀\n"))

    if opção == 1:
        quadros()
        quadros()
        print("▓▓▓▓▓▓▓▓▓▓▓▓ 🆅🅰🅼🅾🆂 🅽🅴🆂🆂🅰 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓‍")
        quadros()
        linhas()
        print("▁▂▃▄▅▆▇█ １ 𝐈𝐍𝐈𝐂𝐈𝐀𝐑 𝐍𝐎𝐕𝐎 𝐉𝐎𝐆𝐎 █▇▆▅▄▃▂▁\n"
              "▁▂▃▄▅▆▇█ ２ 𝐕𝐎𝐋𝐓𝐀𝐑           █▇▆▅▄▃▂▁")
        quadros()
        opcaoInicio = int(input("➤➤ Escolha uma Opção! 🧟‍♂​🧠​🧟‍♀\n"))
        if opcaoInicio == 1:
            numJog = int(input("➤➤ Insira o Número de Jogadores: \n"))
            if numJog >= 2:
                ind = 1
                for ind in range(1, numJog + 1):
                    nome = input(f"➤➤ Insira o Nome do jogador N° {ind}: ")
                    pessoas = dict({'Player N°': ind, "Nome": nome, 'Pontos': 0, 'Tiros': 0})
                    listPlayers.append(pessoas)
                    ind += 1
                playGame = True

                #➤➤➤➤➤➤ NOVA JOGADA - OK REVISADO

                while playGame == True:
                    adicionarDados()
                    rodada = False
                    i = 1

                    #➤➤➤➤➤➤ SELECIONAR JOGADOR - OK REVISADO

                    try:
                        jogador = int(input("➤➤ 𝐐𝐔𝐀𝐋 𝐉𝐎𝐆𝐀𝐃𝐎𝐑 𝐕𝐀𝐈 𝐈𝐍𝐈𝐂𝐈𝐀𝐑 ☚ ０１𝐎𝐔 ０２"))
                        jogadorVez = jogador - 1
                    except:
                        print("➤➤ Insira um Valor Válido!")

                    if jogador != 0:
                        playGame = True
                        rodada = True
                        cerebrosTurno = 0
                        tirosTurno = 0

                    #➤➤ INICIO DA RODADA
                    while rodada == True:

                        try:
                            quadros()
                            jogar = int(input("🎲 - ０１ - 𝐉𝐎𝐆𝐀𝐑 𝐃𝐀𝐃𝐎𝐒 \n"
                                              "🎲  - ０２ - 𝐏𝐀𝐒𝐒𝐀𝐑 𝐀 𝐕𝐄𝐙 \n"))

                        except:
                            print("➤➤ Digite um valor Válido!")
                        if jogar == 1:
                            jogarDados()
                            dados = []
                            for i in range(0, 3):
                                dadoSorteado = random.choice(dadosJogador)
                                corDado = dadoSorteado
                                faceDado = random.randint(0, 5)

                                # ➤➤➤➤➤➤ FACES SORTEADA DOS DADOS - OK REVISADO

                                try:
                                    if dadoSorteado == "CPCTPC":
                                        corDado = "Verde"
                                    elif dadoSorteado == "TPCTPC":
                                        corDado = "Amarelo"
                                    else:
                                        corDado = "Vermelho"
                                    if dadoSorteado[faceDado] == "C":
                                        if listPlayers[jogadorVez]['Pontos'] >= 13 or cerebrosTurno >= 13:
                                            listPlayers[jogadorVez]['Pontos'] += cerebrosTurno
                                            quadros()
                                            print(" ◍◍◍ 🆅🅸🆃🅾🆁🅸🅰 ◍◍◍ ")
                                            quadros()
                                            print(listPlayers[jogadorVez])
                                            rodada = False
                                            playGame = False
                                            break
                                        else:
                                            quadros()
                                            print(f"🎲 O dado {corDado}"
                                                  f" ▁▂▃▄▅▆▇█ LETRA {dadoSorteado[faceDado]} █▇▆▅▄▃▂▁")
                                            print(f"🧟🧠 Você acaba de comer um Cérebro. 🧠🧟")
                                            quadros()
                                            cerebrosTurno = cerebrosTurno + 1
                                            dadosJogador.remove(dadoSorteado)

                                    elif dadoSorteado[faceDado] == "T":
                                        if tirosTurno == 3:
                                            quadros()
                                            print("🚨🚨🚨🚨🚨😬🚨🚨🚨🚨🚨\n"
                                                  "𝐕𝐎𝐂𝐄 𝐄𝐒𝐓𝐀 𝐒𝐄𝐌 𝐕𝐈𝐃𝐀𝐒"
                                                  "😬 𝐒𝐄𝐔𝐒 𝐂𝐄𝐑𝐄𝐁𝐑𝐎𝐒 𝐅𝐎𝐑𝐀𝐌 𝐙𝐄𝐑𝐀𝐃𝐎𝐒😬 ")
                                            quadros()
                                            rodada = False
                                        else:
                                            quadros()
                                            print(f"🎲 O dado {corDado}"
                                                  f" ▁▂▃▄▅▆▇█ LETRA {dadoSorteado[faceDado]} █▇▆▅▄▃▂▁")
                                            print(f"🚨😬🔫 Você acaba de levar um Tiro.🚨😬🔫")
                                            quadros()
                                            tirosTurno = tirosTurno + 1
                                            dadosJogador.remove(dadoSorteado)
                                    else:
                                        quadros()
                                        print(f"🎲 O dado {corDado}:"
                                              f" ▁▂▃▄▅▆▇█ LETRA {dadoSorteado[faceDado]} █▇▆▅▄▃▂▁")
                                        print(f"✘💨 Você acaba de perder uma vítima.💨✘")
                                        quadros()
                                except:
                                    print("Erro")

                            #➤➤ RESET DOS DADOS - OK REVISADO

                            if len(caixadeDados) == 0:
                                quadros()
                                print("🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲\n"
                                      "𝐒𝐄𝐔𝐒 𝐃𝐀𝐃𝐎𝐒 𝐄𝐒𝐓𝐀𝐎 𝐑𝐄𝐒𝐄𝐓𝐀𝐃𝐎𝐒!")
                                linhas()
                            elif playGame == False:
                                adicionarDados()
                            elif len(dadosJogador) < 3:
                                jogarDados()


                        #➤➤FECHAMENTO DA RODADA - OK REVISADO

                        elif jogar == 2:
                            quadros()
                            print("​⚒​😫​🛠️​"
                                  "𝐄𝐒𝐒𝐄 𝐄 𝐎 𝐅𝐈𝐍𝐀𝐋 𝐃𝐄 𝐒𝐔𝐀 𝐑𝐎𝐃𝐀𝐃𝐀!\n"
                                  "➤➤➤➤➤ PRÓXIMO JOGADOR!\n")
                            quadros()
                            rodada = False
                            listPlayers[jogadorVez]['Pontos'] += cerebrosTurno
                            cerebrosTurno = 0
                            listPlayers[jogadorVez]['Tiros'] += tirosTurno
                            tirosTurno = 0
                            quadros()
                            print(" 𝐄𝐒𝐒𝐄 𝐄 𝐎 𝐏𝐋𝐀𝐂𝐀𝐑 𝐃𝐀 𝐑𝐎𝐃𝐀𝐃𝐀 ")
                            print(f"{listPlayers}\n")
                            linhas()
                        else:
                            linhas()
                            print("🤷 - ERROR! ➤➤ Digite um Valor Válido!")
                            quadros()
                        try:
                            linhas()
                            continuar = int(input("☛ Deseja Continuar o Jogo?\n"
                                                  " ☛ ０１ - 𝐒𝐈𝐌\n"
                                                  " ☛ ０２ - 𝐍𝐀𝐎\n"))
                            quadros()
                            if continuar == 1:
                                if tirosTurno == 3:
                                    quadros()
                                    print("🚨🚨🚨🚨🚨😬🚨🚨🚨🚨🚨\n")
                                    print("𝐈𝐌𝐏𝐎𝐒𝐒𝐈𝐕𝐄𝐋 𝐂𝐎𝐍𝐓𝐈𝐍𝐔𝐀𝐑\n")
                                    print("🚨😬🔫 Você levou muitos Tiros.🚨😬🔫\n"
                                          "É Fim de sua rodada!\n")
                                    print("🚨🚨🚨🚨🚨😬🚨🚨🚨🚨🚨\n")
                                    linhas()
                                    quadros()
                                    cerebrosTurno = 0
                                    listPlayers[jogadorVez]['Tiros'] += tirosTurno
                                    tirosTurno = 0
                                    rodada = False
                                    break
                                else:
                                    continue

                            # ➤➤CHECK OUT DA RODADA - OK REVISADO

                            elif continuar == 2:
                                quadros()
                                sair = int(input("☛ Deseja sair do Jogo?\n"
                                                  " ☛ ０１ - 𝐒𝐈𝐌\n"
                                                  " ☛ ０２ - 𝐍𝐀𝐎\n"))
                                if sair == 1:
                                    listPlayers[jogadorVez]['Pontos'] += cerebrosTurno
                                    cerebrosTurno = 0
                                    listPlayers[jogadorVez]['Tiros'] += tirosTurno
                                    tirosTurno = 0
                                    quadros()
                                    print("▓▓▓▓▓▓ ☻ 𝐎 𝐉𝐎𝐆𝐎 𝐀𝐂𝐀𝐁𝐎𝐔 ☻ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
                                    quadros()
                                    mostrarPacar()
                                    rodada = False
                                    playGame = False
                                    break
                                elif sair == 2:
                                    continue
                                else:
                                    quadros()
                                    print("🤷‍ ERROR! ☛ Digite um Valor Válido!")
                                    quadros()
                            else:
                                quadros()
                                print("🤷‍ ERROR! ☛ Digite um Valor Válido!")
                                quadros()
                        except:
                            quadros()
                            print("🤷‍ ERROR! ☛ Digite um Valor Válido!")
                            quadros()
                    else:
                        rodada = False

            # ➤➤➤➤➤➤ MENSSAGEM DE JOGADORES INSULFICIENTES - OK REVISADO
            elif numJog < 2:
                quadros()
                quadros()
                print("🤷 Lamento, mais você precisa de no mínimo 2 jogadores 🤷‍\n")
                quadros()
                quadros()
        elif opcaoInicio == 2:
            continue
        else:
            quadros()
            print("➤➤ 🤷 ERROR! Insira um Valor Válido!🤷\n")
            quadros()


# ➤➤➤➤➤➤ IMPRIMIR LISTA DE JOGADORES - OK REVISADO
    elif opção == 2:
        if len(listPlayers) == 0:
            quadros()
            print("➤➤ 𝐀 𝐋𝐈𝐒𝐓𝐀 𝐃𝐄 𝐉𝐎𝐆𝐀𝐃𝐎𝐑𝐄𝐒 𝐄𝐒𝐓𝐀 𝐕𝐀𝐙𝐈𝐀!\n")
            quadros()
        else:
            quadros()
            mostrarPacar()
            quadros()

# ➤➤➤➤➤➤ EXCLUIR JOGADOR DA LISTA - OK REVISADO
    elif opção == 3:
        if len(listPlayers) == 0:
            quadros()
            print("​🎶​🇫🇷​😩​😂​")
            print("𝐀 𝐋𝐈𝐒𝐓𝐀 𝐃𝐄 𝐉𝐎𝐆𝐀𝐃𝐎𝐑𝐄𝐒 𝐄𝐒𝐓𝐀 𝐕𝐀𝐙𝐈𝐀! ​🎶​🇫🇷​😩​😂​")
            print("​🎶​🇫🇷​😩​😂​\n")
        elif len(listPlayers) == 2:
            quadros()
            print("➤➤ 😩 ERRO! Operação Inválida!😩")
            print("➤➤ 😩 Ao excluir este jogador, seu número de jogadores será insuficiente para Continuar!😩\n")
        else:
            quadros()
            delJogador = int(input("➤➤ 😩 Digite o Número do Jogador que Deseja Excluir: 😩"))
            delJogador = delJogador - 1
            listPlayers.pop(delJogador)


# ➤➤➤➤➤➤ SAIR DO JOGO - OK REVISADO
    elif opção == 4:
        print("\n")
        quadros()
        print("▓▓▓▓▓▓ ☻ 𝐎 𝐉𝐎𝐆𝐎 𝐀𝐂𝐀𝐁𝐎𝐔 ☻ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
        quadros()
        print("Copyright © Jackson Douglas de Souza")
        print("www.linkedin.com/in/jacksondouglasdesouza")
        break
    else:
        print("😩 ERROR! ESTE VALOR É INVÁLIDO😩 ")
    linhas()
    print(" ")
input()
