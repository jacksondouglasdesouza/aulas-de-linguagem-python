# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

#CONTINUAÇÃO LISTAS


x = [2, 3, 4, 5, 70, 90, 80]
print(type(x))
print(len(x))
print(x)

y = [indice for indice in range(10)]
print(type(y))
print(len(y))
print(y)

z = [indice for indice in range(0, 19, 3)]
print(type(z))
print(len(z))
print(z)

a = [2] * 10
print(type(a))
print(len(a))
print(a)


b = [int(input("Digite número: "))]
print(type(b))
print(len(b))
print(b)

c = 20 * b
print(type(c))
print(len(c))
print(c)




frutas = ["banana", "maça", "goiaba", "mamão", "melão"]
print(type(frutas))
print(len(frutas))
print(frutas)

print(frutas[0])


misto = ["banana", 5000, 352.85, True]
print(type(misto))
print(len(misto))
print(misto)

print(misto[0])
print(type(misto[0]))
print(misto[1])
print(type(misto[1]))
print(misto[2])
print(type(misto[2]))
print(misto[3])
print(type(misto[3]))

matriz = [["linha 01", 1, 2, 3], ["linha 02", 4, 5, 6], ["linha 03", 7, 8, 9]]
print(matriz)
print(matriz[1][3])
print(type(matriz[1]))






