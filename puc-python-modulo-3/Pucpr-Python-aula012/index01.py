# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

#CONTINUAÇÃO LISTAS

'''
animais = [
    ["Beija Flor", "Aguia"],# Valor [ 0 ] Aves
    ["Cobra", "Jacaré"]# Valor [ 1 ] Repteis
]
'''

'''
numeros = [12, 36, 89, 67, 333, 65, 15, 36, 359, 63, 50, 65, 67, 66, 32, 39, 37, 25, 26]
print(min(numeros))
print(max(numeros))
numeros.sort()
print(len(numeros))
print(numeros)

'''

#Solicite que o usuário insira as condenadas x e y, armazenando-as em uma matriz bidimensional.


"""
cordenadasUsuario = []
for indice in range(3):
    x = int(input("Digite a coordenada de X: "))
    y = int(input("Digite a coordenada de y: "))
    cordenadasUsuario.append([x, y])

print(cordenadasUsuario)

"""

#crie um programa que armazena em uma entrada de dados, com nome e sobrenome em uma lista. No formato
#sobrenome, nome.


'''
nomes = []

while True:
    nome = input("Digite o seu nome: ")
    if nome == "exit":
        break
    sobrenome = input("Digite o Sobrenome")
    nomeCompleto = [nome, sobrenome]
    nomes.append(nomeCompleto)

for nome in nomes:
    print("{}, {}".format(nome[1], nome[0]))

'''


#some todos os resultados da matriz bidimencional. Matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

'''
somatoriaMatriz = 0
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for indice in range(3):
    for jindice in range(3):
        somatoriaMatriz += matriz[indice][jindice]

print("A somatoria das matrizes é: {}".format(somatoriaMatriz))

'''




