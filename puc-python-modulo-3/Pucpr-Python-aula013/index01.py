# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

#METODOS EM LISTAS E FUNÇÕES

'''
print() | apped() | extend() | insert() | remove() | pop() | clear() | index() | count() | sort() | reverse() | copy() |
len() |
'''

numerosLista = [550, 365, 256, 98, 256, 324, 356, 32, 65, 69, 32, 23, 25, 36, 96, 35, 23, 36, 36, 98, 365, 32,
                125, -5, -96, 36, 35, 36, 45, 46, 46, 31, 1, 523]
numerosLista02 = ["A", "B", "C", True, False, 48, 630]


print(numerosLista) #imprime
print(len(numerosLista)) #retorna a quantidade de intens

numerosLista.append(489) #adiciona um elemento ao final da lista
print(numerosLista)
print(len(numerosLista))

numerosLista.extend(numerosLista02) #Faz um merge entre a lista 01 e lista 02
print(numerosLista)
print(len(numerosLista))

numerosLista.insert(6, 3456) #insere o elemento na posição definida ( posição , elemento )
print(numerosLista)

numerosLista.remove(3456) #remove o elemento definido na função
print(numerosLista)

print(numerosLista.pop(13)) #remove o elemento definido emostra em qual posição se encontrava na lista
print(numerosLista)

numerosCopy = numerosLista.copy() #a função vai fazer uma copia da lista 01 e vai aplicala a lista Copy.
print(numerosCopy)
print("\n")

numerosLista02.clear() #função vai limpar a lista selecionada por completo
print(numerosLista)
print("Lista 02 Vazia")
print(numerosLista02)
print(numerosCopy)

print(numerosLista.count(36)) #função va contar quantos números 36 tem na lista

numerosLista.sort() #   Vai organizar a lista na ordem crescente < para >
print(numerosLista)


numerosLista.reverse() #Vai organizar a lista na ordem decrescente > para <
print(numerosLista)























