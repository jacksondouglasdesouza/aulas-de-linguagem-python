# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas — PUCPR
# QUARTO MÓDULO — PROTÓTIPO DO PROJETO — AV SEMANA 04
# Aluno: Jackson Douglas de Souza
#RA — 1112022209646
# Matéria: Raciocínio Computacional
#Protótipo do projeto Zombie Dice


'''

Nesta semana fará a entrega do protótipo inicial do jogo realizado durante as semanas anteriores.
Este protótipo deve apresentar:
Manipulação de variáveis e constante
Uso de estruturas condicionais (if, elif e else) na implementação em Python
Uso de operadores lógicos e relacionais
Uso de estruturas de repetição (for e while)

'''
import random

print("▓▓▓▓▓" * 9)
print("▓▓▓▓▓ 𝓑ᴇ𝓜 𝓥𝓘𝓝𝓓𝓞 𝓐𝓞 𝓙𝓞𝓖𝓞 𝓩𝓞𝓜𝓑𝓘𝓔 𝓓𝓘𝓒𝓔 ▓▓▓▓▓")
print("—" * 45)

#➤➤➤➤➤➤ Secção — 001 — Receber Quantidade de Jogadores.
quantidadeJogadores = 0
while True:
    try:
        quantidadeJogadores = int(input("➤➤ Digite a quantidade de jogadores: "))
        if quantidadeJogadores < 2:
            print("▓▓▓▓▓" * 9)
            print("🤷 Lamento, mais você precisa de no mínimo 2 jogadores 🤷‍")
            print("➤➤➤➤➤➤➤➤ Tente novamente!")
        elif quantidadeJogadores >= 2:
            print("▓▓▓▓▓" * 9)
            print("▓▓▓▓▓▓▓▓▓▓▓▓ 🆅🅰🅼🅾🆂 🅽🅴🆂🆂🅰 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓‍")
            print("▓▓▓▓▓" * 9)
            break
    except ValueError:
        print("㋡ Só é aceito numero Inteiro!")
        print("➤➤➤➤➤➤➤➤ Tente novamente!")

#➤➤➤➤➤➤ Secção — 002 — Receber nome dos Jogadores

listadejogadores = []

for indice in range(quantidadeJogadores):
    print("—" * 45)
    nomeJogador = input(f"➤➤ Escreva o nome do {indice+1}º jogador: ")
    listadejogadores.append(nomeJogador)

dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"

listaDeDados = [
    dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
    dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
    dadoVermelho, dadoVermelho, dadoVermelho
]

print("\n")
print("▓▓▓▓▓" * 9)
print("▓▓▓🧟❒ 𝐈𝐍𝐈𝐂𝐈𝐀𝐍𝐃𝐎 𝐎 𝐉𝐎𝐆𝐎 ≋ 𝐁𝐎𝐀 𝐒𝐎𝐑𝐓𝐄 ❒‍🧟 ▓▓▓")
print("▓▓▓▓▓" * 9)

jogadorAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0

# ➤➤➤➤➤➤ Secção — 003 — Lógica do Jogo.

while True:
    print("—" * 45)
    print(f"☻ 𝐎 𝐉𝐎𝐆𝐀𝐃𝐎𝐑 {listadejogadores[jogadorAtual]} 𝐉𝐀 𝐏𝐎𝐃𝐄 𝐈𝐍𝐈𝐂𝐈𝐀𝐑\n")
    for indice in range(0, 2):
        numeroSorteado = random.randint(0, 12)
        dadoSorteado = listaDeDados[numeroSorteado]
        if dadoSorteado == "CPCTPC":
            corDado = dadoVerde
        elif dadoSorteado == "TPCTPC":
            corDado = dadoAmarelo
        else:
            corDado = dadoVermelho
    print("▓▓▓▓▓" * 9)
    print("▩▩▩" * 11)
    print(f"🎲 O dado sorteado foi:🎲 {corDado}")
    dadosSorteados.append(dadoSorteado)
    print("—" * 45)


    for dadoSorteado in dadosSorteados:
        numeroFaceDado = random.randint(0, 5)
        if dadoSorteado[numeroFaceDado] == "C":
            print("▁▂▃▄▅▆▇█ LETRA {} █▇▆▅▄▃▂▁".format(dadoSorteado[numeroFaceDado]))
            print(f"🧟🧠 Você acaba de comer um Cérebro. 🧠🧟")
            cerebros += 1
        elif dadoSorteado[numeroFaceDado] == "T":
            print("▁▂▃▄▅▆▇█ LETRA {} █▇▆▅▄▃▂▁".format(dadoSorteado[numeroFaceDado]))
            print(f"🚨😬🔫 Você acaba de levar um Tiro.🚨😬🔫")
            tiros += 1
        else:
            print("▁▂▃▄▅▆▇█ LETRA {} █▇▆▅▄▃▂▁".format(dadoSorteado[numeroFaceDado]))
            print(f"✘💨 Você acaba de perder uma vítima.💨✘")
            passos += 1
    print("\n")
    print("▓▓▓▓▓" * 9)
    print("ESTA É A SUA PONTUAÇÃO ATUAL!")
    print("Você comeu {} Cérebros".format(cerebros))
    print("Você levou {} Tiros".format(tiros))
    print("VocÊ perdeu {} Vítimas".format(passos))
    print("▩▩▩" * 11)

    print("Escolha [S] - Para Continuar Jogando\nEscolha [N] - Para Passar a Vez\nEscolha [F] - Para Finalizar o Jogo")
    continuarJogando = input("☞ 𝐕𝐎𝐂𝐄 𝐃𝐄𝐒𝐄𝐉𝐀 𝐂𝐎𝐍𝐓𝐈𝐍𝐔𝐀𝐑 𝐉𝐎𝐆𝐀𝐍𝐃𝐎?")
    if continuarJogando == ("n" or "N"):
        jogadorAtual = jogadorAtual + 1
        dadosSorteados = []
        tiros = 0
        cerebros = 0
        passos = 0
    elif continuarJogando == ("s" or "S"):
        print("\n")
        print("▓▓▓▓▓" * 9)
        print("▓▓▓▓▓▓ ☻ 𝐂𝐎𝐍𝐓𝐈𝐍𝐔𝐄 𝐉𝐎𝐆𝐀𝐍𝐃𝐎 ☻ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
        print("▓▓▓▓▓" * 9)
        dadosSorteados = []
    else:
        print("\n")
        print("▓▓▓▓▓" * 9)
        print("▓▓▓▓▓▓ ☻ 𝐎 𝐉𝐎𝐆𝐎 𝐀𝐂𝐀𝐁𝐎𝐔 ☻ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
        print("▓▓▓▓▓" * 9)
        print("Copyright © Jackson Douglas de Souza")
        print("www.linkedin.com/in/jacksondouglasdesouza")
        break
