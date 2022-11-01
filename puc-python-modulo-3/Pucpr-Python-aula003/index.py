#Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
#segundo Módulo - Python
#Aluno: Jackson Douglas de Souza
#Matéria: Raciocínio Computacional


'''
Elabore um Código quesimule um caixa eletrônico. O código deverá perguntar ao usuário o valor
do saque e depois informar a quantidade de notas de cada valor que serão fornecidas ao mesmo.
Nostas disponíveis: 1,5,10,50,100.
Valor mínimo de saque é de 10.
Valor máximo de saque é de 600.
'''


print("Bem vindo ao Banco 24 horas da PUCPR!")
valor = int(input("Quanto queseja sacar: "))
modulo = valor
notas01 = 0
notas05 = 0
notas10 = 0
notas50 = 0
notas100 = 0
moedasRestante = 0

if valor < 10 or valor > 600:
    print("Saque não permitido. Valor mínimo para saque é R$10,00 e valor Máximo de R$600,00")

else:
    if modulo >= 100:
        moedasRestantes = modulo % 100
        notas100 = int((modulo - moedasRestantes) / 100)
        modulo = moedasRestantes
    if modulo >= 50:
        moedasRestantes = modulo % 50
        notas50 = int((modulo - moedasRestantes) / 50)
        modulo = moedasRestantes
    if modulo >= 10:
        moedasRestantes = modulo % 10
        notas10 = int((modulo - moedasRestantes) / 10)
        modulo = moedasRestantes
    if modulo >= 5:
        moedasRestantes = modulo % 5
        notas05 = int((modulo - moedasRestantes) / 5)
        modulo = moedasRestantes
    notas01 = modulo

    print("Notas de 100: {}".format(notas100))
    print("Notas de 50: {}".format(notas50))
    print("Notas de 10: {}".format(notas10))
    print("Notas de 05: {}".format(notas05))
    print("Notas de 01: {}".format(notas01))
    print("Obirgado por ser cliente Banco da PUCPR")




#GERADOR DE NÚMEROS ALEATÓRIOS


import math
import random
import string

print(math.sqrt(81))

numero = random.randint(1, 100)
print(numero)
numero001 = random.randint(-100, 100)
print(numero001)

numero002 = random.randrange(0, 10)
print(numero002)

numero003 = random.randrange(-10, 10)
print(numero003)

numero004 = random.randrange(15)
print(numero004)

numero005 = random.randrange(0, 100, 2)
print(numero005) #saída somente de números pares

numero006 = random.randrange(1, 100, 2)
print(numero006) #saída somente de números ímpares

numero007 = random.random()
print(numero007) #saída somente números entre 0 e 1 - numeração decimal

numero008 = random.uniform(-5.0, 5.0)
print(numero008) #saída somente números entre -5.0 e 5.0 - sorteio de numeração decimal

letraSorteada = random.choice("ABACAXI")
print(letraSorteada) #saída somente alguma letra específica


tabelaAscii = random.choice(string.ascii_uppercase)
print(tabelaAscii) #saída somente alguma letra ta tabela ascii





