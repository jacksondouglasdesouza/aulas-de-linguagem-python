# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# LISTAS

#Elabore um código que solicite ao usuário 510numeros, armazene-os numa lista com pares e ímpares.


numerosPares = []
numerosImpares = []
print("*** Digite 10 números aleatorios ***")
for indice in range(10):
    numeroUsuario = int(input(f"Digite o {indice+1} número:: "))
    if numeroUsuario % 2 == 0:
        numerosPares.append(numeroUsuario)
    else:
        numerosImpares.append(numeroUsuario)
print("Lista com pares: {}".format(numerosPares))
print("Lista com ímpares: {}".format(numerosImpares))



#Agora acesse todos os números da lista criada a seguir. [10,20,30,40,50,60,70,80,90,100]

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("ESSA É A LISTA!")
for indice in range(len(lista)):
    print("{}".format(lista[indice]), end=" ")
