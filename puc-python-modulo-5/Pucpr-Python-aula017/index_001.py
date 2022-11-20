# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Sexto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# def() Funções em Python
import math



def reversao(a, b):
    return (b, a)

def operacoes(x):
    return (x*2, x*3, x**2)

def chamaOperacoes(x):
    dobro, triplo, quadrado = operacoes(x)
    result =\
    print("Valor: {}".format(x))
    print("Dobro de {} é: {}".format(x, dobro))
    print("Triplo de {} é: {}".format(x, triplo))
    print("Quadrado de {} é: {}".format(x, quadrado))
    return result


chamaOperacoes(5)
a = 5
b = 3

print(reversao(a, b))





numero = float(input("Digite um Número: "))

for i in range(1, 11):
    print("| {} x {} = {} |".format(numero, i, numero * i))
print("#"*10)
for i in range(1, 11):
    print("| {} + {} = {} |".format(numero, i, numero + i))
print("#"*10)
for i in range(1, 11):
    print("| {} - {} = {} |".format(numero, i, numero - i))
print("#"*10)
for i in range(1, 11):
    print("| {} / {} = {} |".format(numero, i, numero / i))







def multiplicacao(n):
    for i in range(1, 11):
        print("{} * {} = {}".format(n, i, n * i))
def adicao(n):
    for i in range(1, 11):
        print("{} + {} = {}".format(n, i, n + i))
def subtracao(n):
    for i in range(1, 11):
        print("{} - {} = {}".format(n, i, n - i))
def divisao(n):
    for i in range(1, 11):
        print("{} / {} = {}".format(n, i, n / i))

# main

numero = int(input("Digite um Número:"))
print("{}".format(multiplicacao(numero)))
print("*"*15)
print("{}".format(adicao(numero)))
print("*"*15)
print("{}".format(subtracao(numero)))
print("*"*15)
print("{}".format(divisao(numero)))
print("*"*15)




def chamaoFor(start, stop, step=1):
    stop = stop+1 if (start <= stop) else stop-1
    for i in range(start, stop, step):
        print("{}".format(i), end=" ")
    print("")

#main

print(chamaoFor(1, 10, 1))
print(chamaoFor(1, 10))
print(chamaoFor(0, 18, 3))
print(chamaoFor(10, 1, -1))
print(chamaoFor(5, -1, -1))





def estilo(tipo=5, tamanho=20):
    for i in range(tamanho):
        print(tipo, end="")
    print()

estilo('x',10)
estilo('*',20)
estilo('#', 30)
estilo("$")
estilo("/")
estilo()





#Função numero primo

def numeroPrimo(x):
    if(x == 0) or (x == 1):
        return False
    else:
        final = int(math.sqrt(x))
        for i in range(2, final+1):
            if(x % i) == 0:
                return False
        return True

print(numeroPrimo(13))

for i in range(0, 50):
    if numeroPrimo(i):
        print("{}".format(i), end=" ")
        




