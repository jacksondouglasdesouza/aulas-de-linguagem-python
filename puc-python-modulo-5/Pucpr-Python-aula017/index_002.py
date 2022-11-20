# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Sexto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# Continuação def() Funções em Python
import math


alunos = []

for indice in range(4):
    aluno = {}
    aluno['nome'] = input(f"Digite o nome do {indice+1} aluno: ")
    aluno['nota'] = float(input(f"Digite a nota do {indice+1} aluno: "))
    alunos.append(aluno)
    print("_"*30)

print("#"*15)
for indice in range(4):
    print(f"# Nota do {indice+1} Aluno: ")
    print("Nome: {}".format(alunos[indice]["nome"]))
    print("Nota: {}".format(alunos[indice]["nota"]))
print("#"*15)





#Função Cálculo do IMC
def imc(peso, altura):
    return (peso / (altura**2))

peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))

print("Seu IMC é: {:.2f}".format(imc(peso, altura)))





#Maior ou Menor Número

def maiorMenor(x, y):
    return x > y


numero01 = float(input("Digite o 1º Número: "))
numero02 = float(input("Digite o 2º Número: "))

if numero01 == numero02:
    print("Esses números são Iguais!")
elif maiorMenor(numero01, numero02):
    print("O Número {} é maior que o Número {}.".format(numero01, numero02))
else:
    print("O número {} é menor o número {}".format(numero01, numero02))

print("FIM")





#fatorial

def numeroFatoria(x):
    fatorial = 1
    for indice in range(1, x+1):
        fatorial = fatorial * indice
    return fatorial


numeroUsuario = int(input("Digite um núemro: "))
print("O fatórial de [{}!] = [1 x 2 x 3 ... x{}] = [ {} ]"
      "".format(numeroUsuario, numeroUsuario, numeroFatoria(numeroUsuario)))




#lista de Cores

def listaComCores(listaCores):
    for indice in listaCores:
        print([indice])


cores = []
coreslista = input("Digite suas cores: ")
cores.append(coreslista)

print(listaComCores(cores))




#somatoria de elementos de lista, sendo passado um vetor como argumento.

def somaVetor(listaNumero):
    somatoria = 0
    for indice in range(len(listaNumero)):
        somatoria += listaNumero[indice]
    return somatoria



lista = []
while True:
    numeroUsuario = int(input("Digite um número: "))
    lista.append(numeroUsuario)
    if input("Deseja adicionar outro número: ") == 'n':
        break
print("A soma dos números digitado é: {}".format(somaVetor(lista)))




#Crie uma função para receber cadastros telefonicos chamea de inserir.


def inserir(nome, telefone, agenda):
    agenda[nome] = telefone

agendaTelefonica = {}

while True:
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    inserir(nome, telefone, agendaTelefonica)
    if input("Deseja cadastrar outro contato? [s] ou [n] ") == 'n':
        break

print(agendaTelefonica)
print(agendaTelefonica.keys())
print(agendaTelefonica.items())




'''
Elabore um programa que cadastre contatos de uma agenda telefônica. A função de cadastro deve ser realizada dentro
de uma função chamada inserir, que recebe como parâmetros o nome e o telefone do contato, bem como a agenda de contatos.
A função deve verificar se o contato já existe e, em caso positivo, perguntar se o telefone deve ser
modificado, retornando true ou false, de acordo com a inclusão/modificação executada ou não na agenda.
'''


def inserirContato(nome, contato, nomeAgenda):
    if nome in nomeAgenda:
        if input("Contato Já cadastrato! Que alterar seu número? ") == 'n':
            return False
    nomeAgenda[nome] = contato
    return True

primeiraAgenda = {}

while True:
    nomeContato = input("Digite o nome do Usuário: ")
    telefoneContato = input("Digite o Número do Contato: ")

    if inserirContato(nomeContato, telefoneContato, primeiraAgenda):
        print("Contato Adicionado com Sucesso!")
    else:
        print("Falha ao cadastrar o usuário!")

    if input("Quer cadastrar outro contato? [s] ou [n] ") == 'n':
        break

print(primeiraAgenda)
print(" ")
print(primeiraAgenda.keys())
print(" ")
print(primeiraAgenda.items())
print(" ")
print(primeiraAgenda.values())


#função arbitraria

def somaAleatoria(*x):
    somatoria = 0
    for indice in range(len(x)):
        somatoria = somatoria + x[indice]
    return somatoria

numeros = somaAleatoria(2, 3, 4, 5, 8)
print("A somatória é: {}".format(numeros))




#Crie uma função que  retorne o maior e menor número de uma lista

def maiorMenor(*n):
    maiorNumero = -1000000000
    menorNumero = 1000000000
    for numeroUsuario in n:
        if numeroUsuario > maiorNumero:
            maiorNumero = numeroUsuario
        if numeroUsuario < menorNumero:
            menorNumero = numeroUsuario
    return maiorNumero, menorNumero
           #posição [0] #posição [1]


resultadoAleatorio = maiorMenor(7, 15, 3, 22, 1, 8)

print(f"O maior é: {resultadoAleatorio[0]} e o menor é: {resultadoAleatorio[1]}")



#Elabore um programa que, aplicando a fórmula de Bhaskara por funções, encontre as raízes de um
#polinômio do segundo grau, a saber:


def delta(a, b, c):
    return b * b - 4 * a * c


def bhaskara(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print("As raízes são imaginárias")
        return 0, 0, False
    else:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        return x1, x2, True


result1 = bhaskara(1, 3, 1)
if result1[2]:
    print(f"As raízes são {result1[0]} e {result1[1]}")

result2 = bhaskara(1, 2, 1)
if result2[2]:
    print(f"As raízes são {result2[0]} e {result2[1]}")

result3 = bhaskara(1, 1, 1)
if result3[2]:
    print(f"As raízes são {result3[0]} e {result3[1]}")





"""
# DOCUMENTAÇÃO DA FUNÇÃO!
"""

def maiorMenor(*n):
    """
    Essa função recebe uma lista aleatória de números e calcula o maior e o menor números recebidos.

    :param n: variável que armazenarar a lista de números.
    :return: Retorna o maior e menor número da lista n.
    """
    maiorNumero = -1000000000
    menorNumero = 1000000000
    for numeroUsuario in n:
        if numeroUsuario > maiorNumero:
            maiorNumero = numeroUsuario
        if numeroUsuario < menorNumero:
            menorNumero = numeroUsuario
    return maiorNumero, menorNumero
           #posição [0] #posição [1]


#Crie um programa que calcule, a partir de uma função, o fatorial de um número.
# Exemplo: Fatorial de 5 => 5! = 5.4.3.2.1. Observação: por propriedade, 0! = 1.


def fatorial(numero):
    # segundo as propriedades de fatorial
    if numero == 0:
        return 1

    fat = 1
    for i in range(numero, 0, -1):
        fat *= i
    return fat


numero = int(input("Digite um número inteiro para calcular seu fatorial: "))
fat = fatorial(numero)
print(f"O fatorial de {numero} é {fat}")




# Crie um programa que calcule o fatorial de um número, mas de forma recursiva, ou seja,
# chamando a função fatorial de dentro dela mesma.


def fatorial(numero):
    # segundo as propriedades de fatorial
    if numero == 0:
        return 1

    return numero * fatorial(numero - 1)


numero = int(input("Digite um número inteiro para calcular seu fatorial: "))
fat = fatorial(numero)
print(f"O fatorial de {numero} é {fat}")



#Crie um programa que receba uma lista de números e retorne a média.


def media(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)


resultado = media(2, 5, 9, 4, 11)
print(f"O valor da média é {resultado}")



#Documente a função fatorial() desenvolvida no exercício de fixação 1 desta unidade


def fatorial(numero: int):
    """
    Calcula o fatorial de um número
   
    :param numero: número-base para o cálculo do fatorial
    :return: resultado do cálculo do fatorial
    """
    # segundo as propriedades de fatorial
    if numero == 0:
        return 1
 
    fat = 1
    for i in range(numero, 0, -1):
        fat *= i
    return fat
    


# Documente a função media() desenvolvida no exercício de fixação 3 desta unidade.


def media(*numeros):
    """
    Calcula a média dos números passados para a função
   
    :param numeros: lista de números
    :return: valor da média calculada
    """
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)
    


#Crie um programa que, fazendo uso de funções, cadastre contatos em uma agenda
# telefônica, podendo exclui-los. Deve ser exibido um menu com as opções: inserir, remover e sair.

def receber_dados_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    return nome, telefone


def inserir(agenda):
    contato = receber_dados_contato()
    if contato[0] in agenda:
        if input("Contato já cadastrado. Deseja alterar o telefone? (s/n) ") == "n":
            return False
    agenda[contato[0]] = contato[1]
    return True


def remover(nome, agenda):
    if nome in agenda:
        del agenda[nome]
        return True
    else:
        return False


def menu():
    print("*** Agenda Telefônica ***")
    print("1. Inserir contato")
    print("2. Remover contato")
    print("3. Sair")
    return int(input("Escolha uma das opções: "))


agenda = {}
while True:
    op = menu()
    if op == 1:
        if inserir(agenda):
            print("Contato cadastrado com sucesso")
            print(agenda)
        else:
            print("Operação não realizada")
    elif op == 2:
        nome = input("Digite o nome do contato a ser removido: ")
        if remover(nome, agenda):
            print("Contato removido com sucesso")
            print(agenda)
        else:
            print("Operação não realizada")
    else:
        break

