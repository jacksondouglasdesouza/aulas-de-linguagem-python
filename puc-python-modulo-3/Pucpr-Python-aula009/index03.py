# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# LISTAS

#Dada a lista a seguir [13, 33, 23, 11, 8, 15, 9, 102, -2, 305, 850], elabore um código que
# identifique o maior e menor número da lista e mostre-los na saída.

lista = [13, 33, 23, 11, 8, 15, 9, 102, -2, 305, 850]
maior = lista[0]
menor = lista[0]
for indice in lista:
    if indice > maior:
        maior = indice
    elif indice < menor:
        menor = indice

print("O maior número da lista é : {}".format(maior))
print("O menor número da lista é : {}".format(menor))
