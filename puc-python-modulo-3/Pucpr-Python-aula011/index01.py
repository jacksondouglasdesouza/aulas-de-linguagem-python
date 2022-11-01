# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

#CONTINUAÇÃO LISTAS



listaIndice = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lenLista = len(listaIndice)
for indice in range(lenLista):
    print(f"Na posição {indice}:", "Valor: {}".format(listaIndice[indice]))




#concatenação de listas


listaA = ["A", "B", "C", "D", "E"]
listaB = [1, 2, 3, 4, 5]
listaC = listaA + listaB

print(listaC)

listaD = listaC + ["Óleo", "Feijão", "Macarrão", "frutas"]

print(listaD)




list = [6, 3, 2, 65, 89, 3, 1, 96, 100, -7]
print(len(list))
print(type(list))
print(list)
print(list.index(96))
print(min(list))

menor = min(list)
posicaoMenor = list.index(menor)

print("Na posição {}, está o menor número: {}".format(posicaoMenor, menor))

maior = max(list)
posicaoMenor = list.index(maior)

print("Na posição {}, está o maior número: {}".format(posicaoMenor, maior))

print("A soma da lista é: {}".format(sum(list)))
mediaLista = sum(list) / len(list)
print("A média da lista é de:  {}".format(mediaLista))


print("\n")


def meses(mes):
    nomeMeses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro",
                 "Outubro", "Novembro", "Dezembro"]
    return (nomeMeses[mes])

def diasMeses(mes):
    nomeMeses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return (nomeMeses[mes])

def semestreAno(mes):
    nomeMeses = ["Primeiro Semetre", "Segundo Semestre"]
    indice = ((mes - 1) // 6)
    return (nomeMeses[indice])

for indice in range(1, 13):
    print("{} = O Mês de {}, tem {} dias e é o {} do ano.".format(indice, meses(indice), diasMeses(indice),
    semestreAno(indice)))

