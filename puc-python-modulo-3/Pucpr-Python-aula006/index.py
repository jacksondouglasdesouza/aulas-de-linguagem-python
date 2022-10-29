#Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
#Terceiro Módulo - Python
#Aluno: Jackson Douglas de Souza
#Matéria: Raciocínio Computacional

#CONTINUAÇÃO - ESTRUTURAS DE REPETIÇÃO

import math


for i in range(9, 82, 9):
    print(i, end=" ")




for i in range(50, -50, -1):
    print(i, end=" ")


#faça uma calculadora com a estrutura de repetição For


numero = int(input("Digite um número: "))

print("+-------------+")

for i in range(1, 11):

    print("| {} x {:2} = {:2} |".format(numero, i, numero * i))

print("+-------------+")




lista = [9, 0, 5, 3, 4]
posicao = len(lista)

for i in range(posicao):
    print("Valor na Posição: {} = {}".format(i, lista[i]))
    



lista = [9, 0, 5, 3, 4]

print("[ ", end=" ")
for itens in lista:
    print("{}".format(itens), end=" ")
print(" ]")



lista = [9, 0, 5, 3, 4]

for i, items in enumerate(lista):
    print("Posição {} = {}".format(i, items))
    



nomes = 'JACKSON DOUGLAS DE SOUZA'

for i, nome in enumerate(nomes):
    print("Letra na Posição {:2} : {:2}".format(i, nome))

print("\n[ ", end=" ")
for letras in nomes:
    print("{}".format(letras), end=" ")
print(" ]", end=" ")




#cosntrua um código que identifique se o núymero é primo



numeroDigitado = int(input("Digite um número: "))

if numeroDigitado == 0 or numeroDigitado == 1:
    flag = False

else:
    flag = True
    limiteContagem = int(math.sqrt(numeroDigitado))
    for i in range(2, limiteContagem + 1):
        if numeroDigitado % i == 0:
            flag = False
            break

if flag == True:
    print("{} SIM, este é um número primo!".format(numeroDigitado))
else:
    print("{} NÃO, este número não é primo!".format(numeroDigitado))
    



soma = 0
indice = 2

print("[ ", end=" ")
while indice <= 20:
    print(" {}".format(indice), end=" ")
    soma = soma + indice
    indice = indice + 2

print(" ===> TOTAL {} ]".format(soma))



soma = 0
print("[ ", end=" ")
for indice in range(2, 21, 2):
    print("{}".format(indice), end=" ")
    soma = soma + indice

print(" ==> SOMA = {}".format(soma))