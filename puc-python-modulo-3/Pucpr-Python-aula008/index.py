# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# CONTINUAÇÃO - ESTRUTURAS DE REPETIÇÃO - for | while


import math

#Faça a sequencia de Fibonacci


print("-"*30)
print("SEQUÊNCIA DE FIBONACCI")
print("-"*30)

numeroDigitado = int(input("Digite um número: "))
numeroAnterior = 0
proximoNumero =1
somatoria = 1

for indice in range(numeroDigitado):
    print(" ⇢ {}".format(numeroAnterior), end=" ")
    somatoria = proximoNumero + numeroAnterior
    numeroAnterior = proximoNumero
    proximoNumero = somatoria

print("⇢ FIM")



#------------


print("-"*30)
print("SEQUÊNCIA DE FIBONACCI")
print("-"*30)
numeroUsuario = int(input("Quantos termos que mostrar: "))
numero01 = 0
numero02 = 1
print("{} ⇢ {}".format(numero01, numero02), end=" ")
indice = 3
while indice <= numeroUsuario:
    numero03 = numero01 + numero02
    print(" ⇢ {} ".format(numero03), end=" ")
    numero01 = numero02
    numero02 = numero03
    indice += 1
print("⇢ FIM")



