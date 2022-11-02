# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

#CONTINUAÇÃO EXERCÍCIO DE MÉTODOS DE LISTAS E FUNÇÕES BUILT IN



import math


numeroUsuario = int(input("Digite seu número: "))
print("O quadrado do número {} é: {}".format(numeroUsuario, pow(numeroUsuario, 2)))
print("A raiz quadrada de {} é: {:.2f}".format(numeroUsuario, math.sqrt(numeroUsuario)))



numero = int(input("Digite o número: "))
print("O cubo do número {} é: {}".format(numero, pow(numero, 3)))


#Calcule a área do círculo dado por PI * r²


pi = 3.14159265359
raio = float(input("Digite o valor do raio: "))
print("A área do círculo de raio {}, é de: {:.3f}".format(raio, (pi * pow(raio, 2))))



pessoas = 10
somatoria = 0
for indice in range(pessoas):
    altura = float(input(f"Digite a altura da {indice+1}: "))
    somatoria += altura
mediaPessoas = somatoria / pessoas
print("A média aritimética das pessoas é de: {}".format(mediaPessoas))




alunos = 10
soma = 0
media = 0
aprovados = 0
reprovados = 0
notasTotais = []

for indice in range(alunos):
    nota = float(input(f"Digite a nota do {indice + 1} aluno: "))
    notasTotais.append(nota)

    if notasTotais[indice] >= 7:
        aprovados += 1
    else:
        reprovados += 1
for indice in range(alunos):
    soma += notasTotais[indice]
media = soma / alunos
print("\n")
print("▒"*40)
print("Essa é a quantidade de alunos aprovados: {}".format(aprovados))
print("Essa é a quantidade de alunos reprovados: {}".format(reprovados))
print("Esta é a média artimética da turma: {:.2f}".format(media))
print("▒"*40)




linhas = 2
colunas = 3
matriz = [[4, 2, 3], [5, 1, 0]]
maior = [0][0]

for indiceLinhas in range(linhas):
    for indiceColunas in range(colunas):
        if matriz[indiceLinhas][indiceColunas] > maior:
            maior = matriz[indiceLinhas][indiceColunas]

print("O maior número da matriz é: {}".format(maior))



numeros_positivos_pares = []
numeros_negativos_impares = []

for i, numero in enumerate(range(-10, 11)):
    if numero < 0:
        if numero % 2 == 1:
            numeros_negativos_impares.append([i, numero])
    else:
        if numero % 2 == 0:
            numeros_positivos_pares.append([i, numero])

print("Numeros negativos Ímpares: ")
for i in numeros_negativos_impares:
    print(f"{i}")
print("Numeros positivos Pares: ")
for i in numeros_positivos_pares:
    print(f"{i}")



