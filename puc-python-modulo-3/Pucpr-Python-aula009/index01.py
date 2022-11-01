# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# LISTAS

#Elabore um código que solicite ao usuário 5 numeros, armazene-os em uma lista.

listaNumeros = []
for indice in range(5):
    numeroUsuario = int(input(f"Digite o {indice+1} número: "))
    listaNumeros.append(numeroUsuario)
print("Os números armazenados são: {}".format(listaNumeros))

