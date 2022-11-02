# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

#CONTINUAÇÃO EXERCÍCIO DE MÉTODOS DE LISTAS E FUNÇÕES BUILT IN


'''
Exercício de fixação 1: crie um programa que solicite ao usuário seis números, calculando a média,
e mostre uma lista com os números iguais ou acima da média e uma lista com os números abaixo da média.
'''


numeros = []
numerosMaiores = []
numerosMenores = []
somatoria = 0

for indice in range(6):
    numeroUsuario = int(input(f"Digite o {indice + 1}º número:  "))
    numeros.append(numeroUsuario)
    somatoria += numeroUsuario
media = somatoria / 6

for numeroUsuario in numeros:
    if numeroUsuario >= media:
        numerosMaiores.append(numeroUsuario)
    else:
        numerosMenores.append(numeroUsuario)

print("▒"*30)
print("Os números digitados foram: {}".format(numeros))
print("A soma entre os números é: {}".format(somatoria))
print("A média dos números é: {}".format(media))
print("Os maiores números são: {}".format(numerosMaiores))
print("Os menores números são: {}".format(numerosMenores))
print("▒"*30)



'''
Exercício de fixação 2: Crie um programa que solicite ao usuário duas listas com cinco 
elementos cada e, como resultado, crie uma terceira lista que intercale os elementos das anteriores.

'''


lista01 = []
lista02 = []
merge = []

for indice in range(5):
    numeroUsuario01 = int(input(f"Digite o {indice + 1}º número: "))
    lista01.append(numeroUsuario01)
    #lista01.sort()
for jindice in range(5):
    numeroUsuario02 = int(input(f"Digite o {jindice + 1}º número: "))
    lista02.append(numeroUsuario02)
    #lista02.sort()

merge.extend(lista01 + lista02)
merge.sort()

print("▒"*30)
print("Essa é a primeira lista: {}\n".format(lista01), end=" ")
print("Essa é a segunda lista: {}\n".format(lista02), end=" ")
print("Essa é a junção das listas: {}\n".format(merge), end=" ")
print("▒"*30)



'''
Exercício de fixação 3: Crie um programa que leia as temperaturas médias de cada mês do ano e as armazene em uma lista;
use outro vetor para guardar e exibir, quando necessário, o nome dos meses do ano; calcule a média anual de temperatura
e informe quais meses ficaram acima da média anual.

'''


mesesdoAno = [
    "Janeiro", "Fevereiro", "Março", "Abril", "maio", "Junho",
    "julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
temperaturas = []
somaTemperatura = 0

for indice in mesesdoAno:
    dadosUsuario = float(input(f"Digite a temperatura de {indice}: "))
    temperaturas.append(dadosUsuario)
    somaTemperatura += dadosUsuario
mediaAnual = somaTemperatura / 12
print("\n")
print("▒"*50)
print("A média anual da temperatura é: {:.2f}ºCelsius\n".format(mediaAnual))
print("Os meses que passaram da média anual foram: \n")
for jindice in range(12):
    if temperaturas[jindice] > mediaAnual:
        print(f"{mesesdoAno[jindice]} com: {temperaturas[jindice]} ºCelsius")
print("▒"*50)




'''

Exercício de fixação 4: Crie um programa que efetue a soma de duas matrizes 3x3, sabendo que
a soma desse tipo de matriz é uma nova matriz 3x3, sendo cada elemento resultado da soma dos
elementos das matrizes na mesma posição.

'''


matriz_01 = []
matriz_02 = []
somatoriaMatriz = []

for indice in range(3):
    matriz_01.append([])
    for i in range(3):
        numero = int(input(f"Digite o {i+1}º número da primeira Matriz: "))
        matriz_01[indice].append(numero)
for indice in range(3):
    matriz_02.append([])
    for i in range(3):
        numero = int(input(f"Digite o {i+1}º número da segunda Matriz: "))
        matriz_02[indice].append(numero)
for indice in range(3):
    somatoriaMatriz.append([])
    for j in range(3):
        numero = matriz_01[indice][j] + matriz_02[indice][j]
        somatoriaMatriz[indice].append(numero)

print("\n")
print("▒"*50)
print("Primeira Matriz: {}".format(matriz_01))
print("Segunda Matriz: {}".format(matriz_02))
print("Soma dos Vetores: {}".format(somatoriaMatriz))
print("▒"*50)



'''
Exercício de fixação 5:

A matriz-identidade é uma matriz com a mesma quantidade de linhas e colunas, apresentando todos
os elementos da diagonal principal (de cima para baixo, da esquerda para a direita) iguais a 1
e os demais elementos iguais a 0. Crie um programa que solicite o tamanho da matriz desejada
gerando a matriz-identidade.

'''


matrizIdentidade = []

tamanhoMatriz = int(input("Qual o Tamanho que deseja: "))
print("▒"*(tamanhoMatriz*4))
for indice in range(tamanhoMatriz):
    matrizIdentidade.append([])
    for jindice in range(tamanhoMatriz):
        if indice == jindice:
            matrizIdentidade[indice].append(1)
        else:
            matrizIdentidade[indice].append(0)
for linhas in matrizIdentidade:
    print("▒▒ {} ▒▒".format(linhas))

print("▒"*(tamanhoMatriz*4))



'''
Exercício de fixação 6: Dado o vetor nums = [3, 7, 2, 9, 5, 6], crie um programa que, em uma linha,
calcule a média dos seus elementos.

'''


numeros = [3, 7, 2, 9, 5, 6]
mediaNumeros = sum(numeros) / len(numeros)
print(mediaNumeros)




'''
Exercício de fixação 7:Dado o vetor nums = [3, 11, 6, 32, 15, 22, 4, 10, 5], crie uma matriz 3x3 com os três maiores
elementos na primeira linha, os três elementos intermediários na segunda linha
e os elementos menores na terceira linha.

'''



numeros = [3, 11, 6, 32, 15, 22, 4, 10, 5]
vetor_01 = []
vetor_02 = []
matriz = []


for indice in range(3):
    vetor_01.append(numeros.pop(numeros.index(max(numeros))))
    vetor_01.sort()
for indice in range(3):
    vetor_02.append(numeros.pop(numeros.index(min(numeros))))
    vetor_02.sort()

numeros.sort()
matriz.append(vetor_01)
matriz.append(numeros)
matriz.append(vetor_02)


print("▒"*50)
print("Vetor 01, maiores: {}".format(vetor_01))
print("Vetor 02:, menores {}".format(vetor_02))
print("Numeros restantes: {}\n".format(numeros))
print("Matriz 3X3 {}: ".format(matriz))
print("▒"*50)




'''

Exercício de fixação 8: Crie um programa que solicite o nome de quatro times de futebol e simule partidas de forma que
cada time jogue uma vez com os outros três. Na partida, deve perguntar quantos gols fez cada time e somar as devidas
pontuações. Ao final, deve dizer quais times foram campeões, uma vez que pode haver empate em pontuação.
Observação: vitória vale 3 pontos para o vencedor, empate vale 1 ponto para cada time e derrota não soma pontos.

'''


equipes = []
pontuacao = [0, 0, 0, 0]

for indice in range(4):
    times = input(f"Digite o nome do {indice+1} time: ")
    equipes.append(times)
for i in range(3):
    for jindice in range(i+1, 4):
        print(f"Jogo {equipes[i]} X {equipes[jindice]}")
        gols_01 = int(input(f"Gols do {equipes[i]}: "))
        gols_02 = int(input(f"Gols do {equipes[jindice]}: "))
        if gols_01 > gols_02:
            pontuacao[i] += 3
        elif gols_01 < gols_02:
            pontuacao[jindice] += 3
        else:
            pontuacao[i] += 1
            pontuacao[jindice] += 1

print("\n▒▒▒▒▒ PONTUAÇÃO DAS EQUIPES ▒▒▒▒▒")

for i in range(4):
    print(f"{equipes[i]} : {pontuacao[i]}")
maior = max(pontuacao)

print("▒▒▒▒▒ EQUIPE CAMPEÃ ▒▒▒▒▒")

for i in range(4):
    if pontuacao[i] == maior:
        print(f"{equipes[i]}")

print("▒"*30)
