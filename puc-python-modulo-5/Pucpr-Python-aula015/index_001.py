# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quinto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

#CONTINUAÇÃO TUPLAS E DICIONÁRIOS | TIPOD DE DADOS COMPOSTOS
#LIST | TUPLE | SET | DICT
# list - listas de elementos
# tuple - tuplas.
# set - Conjuntos
# dict - Dicionários

'''
Elabore um programa que solicite ao usuário o cadastro de endereços para entregas de sua compra.
'''


enderecos = []
print("Bem vindo, Digite seu endereço de Entrega: ")
while True:
    rua = input("Rua: ")
    numero = int(input("Número: "))
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    novoEndereco = (rua, numero, bairro, cidade, estado)
    enderecos.append(novoEndereco)

    if input("Deseja cadastrar um endereço opcional para entrega? [sim] ou [não] ") == "não":
        break

print("seus endereços de entrega são: ")
for i in range(0, len(enderecos)):
    imprimirEndereco = enderecos[i]
    print(f"{i+1}º Endereço: {imprimirEndereco[0]}, {imprimirEndereco[1]}, {imprimirEndereco[2]}-{imprimirEndereco[3]}"
          f" | {imprimirEndereco[4]}")

print(imprimirEndereco)



'''
Elabore um programa que crie uma tupla contendo duas listas com dados, altere os dados da primeira lista
e verifique se haverá alteração de dados na Tupla!
'''


tuplalist = ([1, 2, 3], [4, 5, 6])
print(tuplalist)
print(id(tuplalist[0]))
tuplalist[0].append(9)
print(tuplalist)
print(id(tuplalist[0]))



#crie um programa para concatenar tuplas.

enderecos = ("Rua josé da Silva Chavier", 1552, "Lagoa da Conceição", "Florianópolis", "SC")
print(enderecos)
print(id(enderecos))
enderecos += ("Brasil", )
print(enderecos)
print(id(enderecos))



'''
Crie um programa que analise os typos de dados na tupla.
'''


tupla_a = ("Brasil")
#Só um dado entre parêntes não é considerado uma Tupla, só acrescentando uma virgula no final é possível.
tupla_b = ("Croácia", )

print(type(tupla_a))
print(type(tupla_b))






