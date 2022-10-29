# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Terceiro Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# CONTINUAÇÃO - ESTRUTURAS DE REPETIÇÃO - for | while

import math

# Elabore um programa que solicite ao usuário seu nome e mostre as suas letras uma a uma com a estrutura for.


nomeUsuario = input("Digite o seu nome: ")

print("[ ", end=" ")
for i in nomeUsuario:
    print("{}".format(i), end=" ")
print(" ]", end=" ")



# Elabore um programa que solicite trÊs números, some-os e exiba o resultado para o usuário.



somatoria = 0

for indice in range(3):
    numeroDigitado = int(input(f"Digite o {indice+1} número: "))
    somatoria += numeroDigitado

print("A soma total é: {}".format(somatoria))



# Elabore um código que calcule o fatorial de um número, exibindo a informação d como é realizado o procedimento.



fator = 1
expre = ' '

numeroUsuario = int(input("Digite um Número: "))

for indice in range(numeroUsuario, 0, -1):
    fator *= indice
    expre += str(indice)

    if indice > 1:
        expre += " x "

print(" O valor do fatorial de {} é : {}".format(numeroUsuario, fator))
print("A expressão matemática funciona assim: [ {} = {} ]".format(expre, fator))



# Elabore um programa que solicite ao usuário 10 números e efetue a soma, exibindo o resultado. Portanto, caso
# digite [ 0 ] o laço deve ser interrompido com o comando Break, somando somente valores anteriores.


somatoria = 0

for indice in range(10):
    numeroUsuario = int(input(f"Digite o {indice+1} numero: "))
    if numeroUsuario == 0:
        break
    somatoria += numeroUsuario
print("A somatória dos números é: {}".format(somatoria))

print("Agora vamos multiplicar! ")



multiplicacao = 1

for indice in range(10):
    numeroUsuario = int(input(f"Digite o {indice+1} numero: "))
    if numeroUsuario == 0:
        continue
    multiplicacao *= numeroUsuario
print("A somatória dos números é: {}".format(multiplicacao))





'''
Elabore um código que solicite ao usuário que digite indefinidade números e efetue a soma dos mesmos
até que o usuário digite o [ 0 ] para assim interromper o programa.
'''


somatoria = 0
numeroUsuario = -1
print(" Digite seu núemro, para encerrar o programa digite [ 0 ] ")
while numeroUsuario != 0:
    numeroUsuario = int(input("Digite um Número: "))
    somatoria += numeroUsuario
print("A soma é: {}".format(somatoria))


print("Agora vamos multiplicar! ")

numeroUsuario02 = -1
multiplicacao = 1

while True:
    numeroUsuario02 = int(input("Digite um número: "))
    if numeroUsuario02 == 0:
        break
    multiplicacao *= numeroUsuario02
print("A multiplicação é: {}".format(multiplicacao))



# Crie um código que valide um número inteiro, fazendo correção de ERRO com o comando TRY.


while True:
    try:
        numeroUsuario = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("O número digitado, não é um número inteiro, tente novamente!")
print("Tudo certo no número {}, está validade corretamente.".format(numeroUsuario))



# Agora Crie um código que valide um número flutuante, fazendo correção de ERRO com o comando TRY.



while True:
    try:
        numeroUsuario = float(input("Digite um número decimal: "))
        break
    except ValueError:
        print("O número digitado, não é um número decimal, tente novamente!")
print("Tudo certo no número {}, está validade corretamente.".format(numeroUsuario))



##Agora Crie um código que valide um número inteiro entre 1 e 100, fazendo correção de ERRO com o comando TRY.


while True:
    try:
        numeroUsuario = int(input("Digite um número inteiro, entre 1 e 100: "))
        if numeroUsuario >= 1 and numeroUsuario <= 100:
            break
        else:
            print("O numero deve ser entre 1 e 100!")
    except ValueError:
        print("ERRO! Tente novamente! O número deve ser inteiro")
print("O número {}, foi validado com sucesso!".format(numeroUsuario))


# Crie um programa que solicite ao utilizador 10 números e mostre na saída quantos são pares e quantos são impáres.



numerosPar = 0
numerosImpares = 0

for indice in range(10):
    try:
        numeroUsuario = int(input("Digite 10 números inteiros: "))
        if numeroUsuario % 2 == 0:
            numerosPar += 1
        else:
            numerosImpares += 1
    except ValueError:
        print("Esse não é um Valor inteiro!")

print("{} São números pares e {} São números ímpares".format(numerosPar, numerosImpares))



# Crie um código que peça 5 números ao usuário e informe para ela qual é o menor e qual é o maior número.



menor = 10000000000000
maior = -1000000000000

for indice in range(5):
    try:
        numeroUsuario = int(input("Digite 5 numeros inteiros: "))

        if numeroUsuario < menor:
            menor = numeroUsuario
        elif numeroUsuario > maior:
            maior = numeroUsuario
    except ValueError:
        print('Esse não é um número interiro! Tente novamente!!!')

print("Esse é o menor número {}".format(menor))
print("Esse é o maior número: {}".format(maior))



# Crie um programa que receba um texte digitado pelo usuário e imprima a sua saída apenas com consoantes.



textoUsuario = input("Digite sua frase: ")
consoantes = " "

for letras in textoUsuario:
    if letras.lower() not in "aeiou":
        consoantes = consoantes + letras

print("Essas são as consoantes: {}".format(consoantes))



#Faça a tuabuada de um número inteiro até 10


numeroUsuario = int(input("Digite um número inteiro: "))

print("A tabuada do número {}: ".format(numeroUsuario))

for indice in range(1, 11):
    multiplicacao = indice * numeroUsuario
    print(" {} X {} = {}".format(numeroUsuario, indice, numeroUsuario * indice))
    




#crie um programa que peça dois números ao usuário e que mostre a saída do programa o resultado de primeiro
#elevado ao segundo sem ultilizar formula de pontencialização


numerador = int(input("Digite um número inteiro para ser o numerador: "))
expoente = int(input("Digite um número inteiro para ser expoente: "))
resultado = 1
for indice in range(expoente):
    resultado *= numerador

print("{} elevado ao {} é: {}".format(numerador, expoente, resultado))





#Elebore umcódigo que peça a senha e logim do usuário, caso ambas sejam iguais, retornar erro!


while True:
    login = input("Seu Login: ")
    senha = input("Sua senha: ")

    if login == senha:
        print("Dados inválidos, tente novamente!")
    else:
        break
print("Tudo certo, bem vindo ao programa!")




#Crie um código que armazene vários números e imprima a média dos mesmos após usuário digitar [ 0 ]



contagem = 0
somatoria = 0

print("Digite [ 0 ] para finalizar!")
while True:
    numerosUsuario = int(input("Digite seu número:  "))
    if numerosUsuario == 0:
        break
    else:
        contagem += 1
        somatoria += numerosUsuario

    if contagem == 0:
        print("Não existe números sulficiente!")
    else:
        media = somatoria / contagem

print("A média geral é: {}".format(media))




'''
crie um programa que sere a série de fibonacci enquanto o valor for menor que um valor informado pelo
usuário.0,1,1,2,3,5,8,13,21,34,55...... ao infinito
'''



valor = 0
numero = int(input("Digite o valor máximo: "))
numero01 = 0
numero02 = 1
seriacao = "0, 1"
while valor < numero:
    valor = numero01 + numero02
    if valor < numero:
        numero01 = numero02
        numero02 = valor
        seriacao += str(f", {valor}")
print("Fibonacci: {}".format(seriacao))





'''
PROJETO - 01 - Na proxima aula entregar o proejto do carrinho de compras!
Crie um programa que simule um carrinho de compras, solicitando o nome do produto (não pode ser vazio), 
seu valor (valor decimal, positivo) e quantidade a ser comprada (valor inteiro, positivo). Ao incluir um produto, 
deve perguntar se o usuário deseja fechar o pedido ou incluir mais produtos. Todos os dados devem ser validados.
Ao final da compra, deve ser informado o valor total do pedido.
'''

