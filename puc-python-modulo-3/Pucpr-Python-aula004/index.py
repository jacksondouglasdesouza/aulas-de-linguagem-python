#Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
#segundo Módulo - Python
#Aluno: Jackson Douglas de Souza
#Matéria: Raciocínio Computacional

import math



algo = input("Digite algo: ")
print("O tipo primitivo deste valor é: {}".format(type(algo))) #methods
print("Só tem espaços: {}".format(algo.isspace())) #methods
print("O digitado é um número? {}".format(algo.isnumeric())) #methods
print("O digitado é alfabético? {}".format(algo.isalpha())) #methods
print("O digitado é alfanumérico? {}".format(algo.isalnum())) #methods
print("O digitado é letra maiúsculas? {}".format(algo.isupper())) #methods
print("O digitado é letra minúsculas? {}".format(algo.islower())) #methods
print("O digitado é letra maiúsculas? {}".format(algo.istitle())) #methods





'''
Crie um programa que leia um número inteiro e mostre o seu sucessor e o seu antecessor.
'''


numeroInterio = int(input("Digite aqui um número inteiro: "))
print("O número inteiro é : {}".format(numeroInterio))
print("O antecessor do número inteiro é : {}".format(numeroInterio - 1))
print("O sucessor do número inteiro é : {}".format(numeroInterio + 1))





'''
crie um programa que leia um número e mostre o dobro, triplo e a raiz quadrada.
'''



numeroDois = int(input("Digite um número aqui: "))
print("O número digitado é: {}".format(numeroDois))
print("O dobro deste número é: {}".format(numeroDois * 2))
print("O triplo deste número é : {}".format(numeroDois * 3))
print("A raiz quadra deste número é: {:.2f}".format(math.sqrt(numeroDois)))




'''
Desenvolva um programa que leia duas notas e calcule a media do aluno
'''


print("Digite suas duas notas: ")
nota01 = int(input())
nota02 = int(input())
media = (nota01 + nota02) / 2

print("A sua média é {}".format(media))




'''
Escreva um programa que leia um valor em metros e exiba o valorconvertido em centímetros e milímetrs

'''


valorRecebido = float(input("Digite seu valor em metros: "))
valorCentimetros = valorRecebido * 100
valorMilimetros = valorRecebido * 1000

print("Valor em metros é: {}".format(valorRecebido))
print("O valor convertido em cetímetros é: {}".format(valorCentimetros))
print("O valor convertido em milimetros é: {}".format(valorMilimetros))






'''
Faça um programa que leia um número inteiro e mostre na tela a sua tabuada
'''



#ADIÇÃO

numeroParaCalcular = int(input("Digite um número inteiro: "))

mais1 = numeroParaCalcular + 1
mais2 = numeroParaCalcular + 2
mais3 = numeroParaCalcular + 3
mais4 = numeroParaCalcular + 4
mais5 = numeroParaCalcular + 5
mais6 = numeroParaCalcular + 6
mais7 = numeroParaCalcular + 7
mais8 = numeroParaCalcular + 8
mais9 = numeroParaCalcular + 9
mais10 = numeroParaCalcular + 10

print(" {} + 1 = {}" .format(numeroParaCalcular, mais1))
print(" {} + 2 = {}" .format(numeroParaCalcular, mais2))
print(" {} + 3 = {}" .format(numeroParaCalcular, mais3))
print(" {} + 4 = {}" .format(numeroParaCalcular, mais4))
print(" {} + 5 = {}" .format(numeroParaCalcular, mais5))
print(" {} + 6 = {}" .format(numeroParaCalcular, mais6))
print(" {} + 7 = {}" .format(numeroParaCalcular, mais7))
print(" {} + 8 = {}" .format(numeroParaCalcular, mais8))
print(" {} + 9 = {}" .format(numeroParaCalcular, mais9))
print(" {} + 10 = {}" .format(numeroParaCalcular, mais10))

#SUBTRAÇÃO

sub1 = numeroParaCalcular - 1
sub2 = numeroParaCalcular - 2
sub3 = numeroParaCalcular - 3
sub4 = numeroParaCalcular - 4
sub5 = numeroParaCalcular - 5
sub6 = numeroParaCalcular - 6
sub7 = numeroParaCalcular - 7
sub8 = numeroParaCalcular - 8
sub9 = numeroParaCalcular - 9
sub10 = numeroParaCalcular - 10

print("\n {} - 1 = {}" .format(numeroParaCalcular, sub1))
print(" {} - 2 = {}" .format(numeroParaCalcular, sub2))
print(" {} - 3 = {}" .format(numeroParaCalcular, sub3))
print(" {} - 4 = {}" .format(numeroParaCalcular, sub4))
print(" {} - 5 = {}" .format(numeroParaCalcular, sub5))
print(" {} - 6 = {}" .format(numeroParaCalcular, sub6))
print(" {} - 7 = {}" .format(numeroParaCalcular, sub7))
print(" {} - 8 = {}" .format(numeroParaCalcular, sub8))
print(" {} - 9 = {}" .format(numeroParaCalcular, sub9))
print(" {} - 10 = {}" .format(numeroParaCalcular, sub10))


#MULTIPLICAÇÃO

vez1 = numeroParaCalcular * 1
vez2 = numeroParaCalcular * 2
vez3 = numeroParaCalcular * 3
vez4 = numeroParaCalcular * 4
vez5 = numeroParaCalcular * 5
vez6 = numeroParaCalcular * 6
vez7 = numeroParaCalcular * 7
vez8 = numeroParaCalcular * 8
vez9 = numeroParaCalcular * 9
vez10 = numeroParaCalcular * 10

print("\n {} x 1 = {}" .format(numeroParaCalcular, vez1))
print(" {} x 2 = {}" .format(numeroParaCalcular, vez2))
print(" {} x 3 = {}" .format(numeroParaCalcular, vez3))
print(" {} x 4 = {}" .format(numeroParaCalcular, vez4))
print(" {} x 5 = {}" .format(numeroParaCalcular, vez5))
print(" {} x 6 = {}" .format(numeroParaCalcular, vez6))
print(" {} x 7 = {}" .format(numeroParaCalcular, vez7))
print(" {} x 8 = {}" .format(numeroParaCalcular, vez8))
print(" {} x 9 = {}" .format(numeroParaCalcular, vez9))
print(" {} x 10 = {}" .format(numeroParaCalcular, vez10))


#DIVISÃO


#MULTIPLICAÇÃO

divi1 = numeroParaCalcular / 1
divi2 = numeroParaCalcular / 2
divi3 = numeroParaCalcular / 3
divi4 = numeroParaCalcular / 4
divi5 = numeroParaCalcular / 5
divi6 = numeroParaCalcular / 6
divi7 = numeroParaCalcular / 7
divi8 = numeroParaCalcular / 8
divi9 = numeroParaCalcular / 9
divi10 = numeroParaCalcular / 10

print("\n {} / 1 = {}" .format(numeroParaCalcular, divi1))
print(" {} / 2 = {}" .format(numeroParaCalcular, divi2))
print(" {} / 3 = {}" .format(numeroParaCalcular, divi3))
print(" {} / 4 = {}" .format(numeroParaCalcular, divi4))
print(" {} / 5 = {}" .format(numeroParaCalcular, divi5))
print(" {} / 6 = {}" .format(numeroParaCalcular, divi6))
print(" {} / 7 = {}" .format(numeroParaCalcular, divi7))
print(" {} / 8 = {}" .format(numeroParaCalcular, divi8))
print(" {} / 9 = {}" .format(numeroParaCalcular, divi9))
print(" {} / 10 = {}" .format(numeroParaCalcular, divi10))




'''
Crie um programa que leia quantos dinheiro uma pessoa tem na carteira e mostre quantos Dólares
ela pode comprar
considerando: 1 dolar >>> 3,25
'''



dinheiroCarteira = float(input("Quanto dinheiro você tem em sua carteira digital: "))
conversaoDolar = dinheiroCarteira / 3.25

print("Você podera compra {} Dollar." .format(conversaoDolar))



'''
Faça um programa que leia a largura e altura de uma parede em metros e calcule
a sua área e a quantidade de tinta necessária para piná-la.
Considerando que, cada litro de tinta pinta uma área de 2m².
'''



largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
areaQuadrada = largura * altura
tinta = ((areaQuadrada * 1000) / 2) / 1000

print("Sua metragem ao quadrado é: {}".format(areaQuadrada))
print("A quantidade de tinta necessária é de {:.2f} litros" .format(tinta))



'''
Faça um programa que leia o preço de um produto e mostre seu novo valor com 5% de desconto.
'''


produto = float(input("Digite o preço do produto : "))
desconto = (produto / 100) * 5
novoPreco = produto - desconto

print("O valor do produto é R${} com o desconte de 5% fica R${}." .format(produto, novoPreco))



'''
Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário com
abono de 15%.
'''


salario = int(input("Digite o seu salário: "))

abono = (salario / 100) * 15
novoSalario = abono + salario

print("Seu salário e de: R${}, agora com a bonificação fica R${:.2f} ".format(salario, novoSalario))


'''
Escreva um programa que converta uma temperatura digitada em C e converta para F
'''



celcius = float(input("Digite a temperatura: "))
fahrenheit = (celcius * 9/5) + 32

print("A conversão é: {} Fahrenheit".format(fahrenheit))



#Calcule o preço a pagar pelo carro alugado. Sendo a diária 60,00 e a kilometragem 0,15 cent.


diarias = int(input("Quantas diárias: "))
km = float(input("Quantos Km: "))
pagamento = (diarias * 60) + (km * 0.15)

print("O valor a ser pago é de: {}".format(pagamento))
