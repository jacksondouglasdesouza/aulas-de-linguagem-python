# Variáveis

#TIPO INTEIRO
idade = 300

#TIPO REAL
PI = 3.14159265359

#TIPO BOOLEANO | LÓGICO
verdade = True
mentira = False

#TIPO TEXTO | CARACTERES
nomeCliente = "Jackson Douglas de Souza"

#OPERADORES ARITMÉTICOS

numero001 = 1 + 1
subtracao = - 1 - 2
multiplicacao = 1 * 2
divisao = 10 / 3
modulo = 10 % 2 #resulta no resto da operação matemática

print(numero001)
print(subtracao)
print(multiplicacao)
print(divisao)
print(modulo)


#Solicite o nome do usuário e mostre uma mensagem de boas vindas

nome = input("Digite aqui o seu nome: ")
print("Olá {},".format(nome), "seja muito bem vindo ao programa")


primeiroNome = input("Digite aqui o seu primeiro nome: ")
segundoNome = input("Agora digite aqui o seu sobrenome")

print("O seu nome completo é {} {}".format(primeiroNome, segundoNome))
print("O seu nome completo é : " + primeiroNome + " " + segundoNome + "!!! \n\n")



#CONVESÃO DE TIPOS | DADOS


number_01 = int(input("Digite aqui o primeiro número: "))
number_02 = int(input("Digite aqui o segundo número: "))
totalSoma = number_01 + number_02

print(" A soma de {} + {} = {}".format(number_01, number_02, totalSoma))



#OUTRAS CONVERSÕES
# int() flot() complex() str()

'''
Solicite ao usuário dois produtos, com suas respectivas quantidades e preços, e
mostre os dados formatados como tabelas
'''


nome_produto01 = input("Digite o nome do primeiro produto: ")
quantidade_produto01 = int(input("Qual a quantidade do primeiro produto: "))
valor_produto01 = float(input("Qual é o valor do primeiro produto: "))

nome_produto02 = input("Digite o nome do segundo produto: ")
quantidade_produto02 = int(input("Qual a quantidade do segundo produto: "))
valor_produto02 = float(input("Qual é o valor do segundo produto: "))
#print(f'{"PRODUTO":20} | {"QUANTIDADE":^12"} | {"VALOR" :> 10}')
print(f'{nome_produto01:20} | {quantidade_produto01:^12} | {valor_produto01:>10.2f}')
print(f'{nome_produto02:20} | {quantidade_produto02:^12} | {valor_produto02:>10.2f}')














