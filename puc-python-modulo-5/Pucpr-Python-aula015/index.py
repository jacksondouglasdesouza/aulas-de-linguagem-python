# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quinto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

#TUPLAS E DICIONÁRIOS | TIPOD DE DADOS COMPOSTOS
#LIST | TUPLE | SET | DICT
# list - listas de elementos
# tuple - tuplas.
# set - Conjuntos
# dict - Dicionários


listaMista = [12, 13, 14, 15, "ABACAXI", True, "Let's date"]
print("{}".format(listaMista))
print("{}".format(listaMista[0]))
print("{}".format(listaMista[1]))
print("{}".format(listaMista[2]))
print("{}".format(listaMista[3]))
print("{}".format(listaMista[4]))
print("{}".format(listaMista[5]))
print("{}".format(listaMista[6]))
listaMista.append(325)
print("{}".format(listaMista))
listaMista[2] = "Cachorro"
print("{}".format(listaMista))
print("{}".format(len(listaMista)))




tuplaMista = ("Casa", 25, 50, False, bool)
print("{}".format(tuplaMista))
tuplaB = 1, 2, 3, 4, "casaNova"
print("{}".format(type(tuplaMista)))
print("{}".format(tuplaMista))
print("{}".format(tuplaB))
print("{}".format(type(tuplaB)))



cojuntoNovo = {"casa", "apartamento, 2, 3"}

print("{}".format(cojuntoNovo))
cojuntoNovo.add("+ 256")
print("{}".format(cojuntoNovo))
elemento = cojuntoNovo.pop()
print(elemento)



dicionario = {"casa": "Mãe Joana", "beco": "Dos Petas", "numero": 258 }
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

del dicionario["numero"]
print(dicionario)

dicionario["casa"] = "Nova Casa"
print(dicionario)



raul_seixas = ["Eu prefiro ser", "Essa metamorfose ambulante"]
print(type(raul_seixas))
#Convertendo lista em tupla.

raul_seixas = tuple(raul_seixas)
print(type(raul_seixas))

#Convertendo para conjunto

raul_seixas = set(raul_seixas)
print(type(raul_seixas))

estadosCidade = [("Amazonas", "AM"), ("São Paulo", "SP")]
print(type(estadosCidade))

#Convertendo para Dicionário

estadosCidade = dict(estadosCidade)
print(type(estadosCidade))
print(estadosCidade)

