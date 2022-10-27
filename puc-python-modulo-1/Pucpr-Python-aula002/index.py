#ESTRUTURAS CONDICIONAIS
# IGUAL ==
igual = 2 == 2

#DIFERENTE !=
diferente = "A" != 3

#MAIOR-QUE > DADO
maior = 3 > 1

#MENOR-QUE < DADO
menor = 10 < 100

#MAIOR-QUE >= DADO
maiorOuIgual = 10 >= 10

#MENOR-QUE <= DADO

menorOuIgual = 90 <= 89


'''
Elabore um código que peça ao usuário seu ano de nascimento e calcule a sua idade,
e também pergunte se o mesmo já fez aniversário este ano e analise as informações.
'''


anoAtual = 2022
print("Olá bem vindo!")
anoNascimento = int(input("Me informe em qual ano você nasceu: "))
idade = anoAtual - anoNascimento
comparacao = input("Você já fez aniversário este ano: ")

if comparacao == "Não":
    idade -= 1
print("Sua idade é: {}".format(idade))


"""
Elabore um código que faça o calculo da média escolar de um aluno, peça 4 notas e faça a comparação da média, caso
media for maior ou igual a 7, informe que o aluno foi aprovado
"""


print("Digite aqui suas 4 notas: ")
nota001 = float(input())
nota002 = float(input())
nota003 = float(input())
nota004 = float(input())
media = (nota001 + nota002 + nota003 + nota004) / 4
print("Sua média geral foi: {}".format(media))

if media >= 7:
    print("Parabéns você foi Aprovado!")


#SELEÇAO COMPOSTA | IMPLEMENTAÇÃO DO IF COM O ELSE


'''
Elabore um código que faça o calculo da média escolar de um aluno, peça 4 notas e faça a comparação da média, caso
media for maior ou igual a 7, informe que o aluno foi aprovado, se for < que 7, informe ao aluno que ele foi reprovado
'''


print("Digite aqui suas 4 notas: ")
nota001 = float(input())
nota002 = float(input())
nota003 = float(input())
nota004 = float(input())
media = (nota001 + nota002 + nota003 + nota004) / 4
print("Sua média geral foi: {}".format(media))

if media >= 7:
    print("Parabéns você foi Aprovado!")
else:
    print("Infelismente, você está reprovado.")


#ENCADEAMENTO DE IFs - ELIF

'''
Elabore um código que solicite dois números ao usuário e informe qual é o menor número digitado.
'''




print("Digite três numeros, sendo eles diferentes: ")
number01 = float(input())
number02 = float(input())
number03 = float(input())

if number01 < number02:
    if number01 < number03:
        print("O primeiro Número é o menor!")
    else:
        print("O terceiro número é o menor!")

else:
    if number02 < number03:
        print("O segundo número é o menor!")
    else:
        print("O terceiro número é o menor!")



'''
Elabore um código que solicite dois números ao usuário e informe qual é o menor número digitado. Agora use a cláusula
elif do cpmando if
'''



print("Digite três números diferentes: ")
num001 = float(input())
num002 = float(input())
num003 = float(input())

if (num001 < num002) and (num001 < num003):
    print("O primeiro número é o menor!")
elif (num002 < num001) and (num002 < num003):
    print("O segundo número é o menor!")
else:
    print("O terceiro numero é o menor!")



#OPERADORES LÓGICOS

# AND | OUR | NOT
#and = Basta uma confição falsa para retornar falso
#or = basta uma conição verdadeira para retornar verdadeiro
#not = nega qualquer condição ou conjunto de condições



'''
Faça um código que peça a idade do usuário e caso ele seja maior ou igual a 18 anos, informe que
ele já pode tirar a sua habilitação.
'''


print("Bem vindo(a)")
idade = int(input("Qual é a sua idade: "))

if idade >= 18:
    print("Parabéns, você já pode tirar a sua carteira de habilitação!")


'''
Faça um código que peça para o usuário informar o seu nome, sendo que ele dever conter no máximo 
20 caracteres. Caso seja maior de 20, informe ao mesmo que ele dever abreviar seu nome para caber no formulário
'''



nomeUsuario = input("Digite o seu nome: ")
if len(nomeUsuario) > 20:
    print("Por favor, abrevie seu sobrenome. São permitido somente 20 caractreres!")


#Elabore um código que faça comparacão entre numeros e informe se o mesmo é par ou impar.


numero = int(input("Porfavor, digite um número para saber se ele é par ou impar: "))

if numero % 2 == 0:
    print("O seu número é par!")
else:
    print("O seu número é impar")


''' 
Elabore um código que peça para o usuário informar seu salário e que faça acrescimo de bônus salarial.
Se salário for > 5.000 abone em 10%, caso contrário abone em 15%
'''


salarioUsuario = float(input("Informe o seu salário: "))
salarioAbonado = 0
if salarioUsuario <= 5000:
    salarioAbonado = ((salarioUsuario / 100) * 15) + salarioUsuario
else:
    salarioAbonado = ((salarioUsuario / 100) * 10) + salarioUsuario

print("O seu salário com o bônus é de: {}".format(salarioAbonado))


'''
peça ao usuario que informe o turno que opera na empresa, e mostre na saída, bom dia, tarde ou noite, conforme a sua
resposta, e informe código inválido, caso não se enquadre no padrão estabelecido.
'''



turnoColaborador = str(input("Qual o seu turno de Trabalho: "))
m = "Bom dia"
t = "Boa tarde"
n = "Boa noite"
if turnoColaborador == "m":
    print("Bom dia Colaborador!")
elif turnoColaborador == "t":
    print("Boa tarde Colaborador!")
elif turnoColaborador == "n":
    print("Boa noite Colaborador!")
else:
    print("Informação inserida inválida!")


'''
Elabore um código que solicite ao usuário dois números e a opração que o mesmo deseja operar,
mostre o resultado para o mesmo.
'''



print("Olá vamos calcular? Informe os números abaixo!")
numeroDaOperacao001 = float(input("Digite primeiro número: "))
numeroDaOperacao002 = float(input("Digite o segundo número: "))
operacaoEscolhida = str(input("Escolha a Operação: [ + , -, x ou / ]"))
resultadoSaida = 0
if operacaoEscolhida == "+":
    resultadoSaida = numeroDaOperacao001 + numeroDaOperacao002
    print("O resultado é: {}".format(resultadoSaida))
elif operacaoEscolhida == "-":
    resultadoSaida = numeroDaOperacao001 - numeroDaOperacao002
    print("O resultado é: {}".format(resultadoSaida))
elif operacaoEscolhida == "x":
    resultadoSaida = numeroDaOperacao001 * numeroDaOperacao002
    print("O resultado é: {}".format(resultadoSaida))
elif operacaoEscolhida == "/":
    resultadoSaida = numeroDaOperacao001 / numeroDaOperacao002
    print("O resultado é: {}".format(resultadoSaida))
else:
    print("Operação inválida!")



'''

Elabore um código que peça ao usuário para informar as dimensões dos lados do triângulo e informe ao mesmo
qual é o tipo de triângulo pertinente aos dados informado.
'''



print("VAMOS DESCOBRIR QUAL É O SEU TRIÂNGULO!")
ladoTriangulo001 = int(input("Digite a dimensão do lado A: "))
ladoTriangulo002 = int(input("Digite a dimensão do lado B: "))
ladoTriangulo003 = int(input("Digite a dimensão do lado C: "))

if ladoTriangulo001 == "0" or ladoTriangulo002 == 0 or ladoTriangulo003 == 0:
    print("Não existe a medida 0 para triângulo")
else:
    if (ladoTriangulo001 + ladoTriangulo002 < ladoTriangulo003) or (
            ladoTriangulo003 + ladoTriangulo002 < ladoTriangulo001) or (
            ladoTriangulo003 + ladoTriangulo001 < ladoTriangulo002):
        print("Isso não é um triângulo")
    else:
        if ladoTriangulo001 == ladoTriangulo002 and ladoTriangulo003 == ladoTriangulo001:
            print("O seu triângulo é equilátero")
        elif (ladoTriangulo001 == ladoTriangulo002) or (ladoTriangulo001 == ladoTriangulo003) or (
                ladoTriangulo002 == ladoTriangulo003):
            print("O seu triângulo é isósceles")
        else:
            print("O seu triângulo é escaleno")

'''
Crie um código que solicite ao usuário as quatro notas bimestrais de uma matéria e o número de faltas. Informe se
o aluno foi aprovado ou não, média 7, 40 aulas, 75% frequencia.
'''


print("Digite suas 4 notas bimestrais: ")
nota0001 = float(input())
nota0002 = float(input())
nota0003 = float(input())
nota0004 = float(input())
faltas = float(input("Agora digite quantas faltas: "))
mediaNota = (nota0001 + nota0002 + nota0003 + nota0004) / 4
totalAulas = 40
mediaFaltaAprovacao = 100 - (faltas * 100) / totalAulas

if (mediaNota >= 7) and (mediaFaltaAprovacao >= 75):
    print("Você está aprovado com a nota {}.".format(mediaNota))
    print("Sua média de presença é de {}%".format(mediaFaltaAprovacao))
elif(mediaNota >= 7) and (faltas < 75):
    print("Você está reprovado por faltas!")
    print("Sua média de nota foi de nota {}".format(mediaNota))
    print("Sua média de presença é de {}%".format(mediaFaltaAprovacao))
elif (mediaNota < 7) and (mediaFaltaAprovacao >=75):
    print("Você foi reprovado por nota")
    print("Sua média de presença é de {}%".format(mediaFaltaAprovacao))
    print("A sua média de nota foi de {}.".format(mediaNota))

else:
    print("Você foi reprovado por nota e por falta!")
    print("Sua média de presença é de {}%".format(mediaFaltaAprovacao))
    print("A sua média de nota foi de {}.".format(mediaNota))



