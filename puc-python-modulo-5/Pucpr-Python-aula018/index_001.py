# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Sexto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# CONTINUAÇÃO def() Funções em Python
import math

#Crie um módulo de endereços vinculados a cada cliente, selecionando-o na hora da venda.

"""
Módulo de Cadastro de Endereços
"""


def inserir_endereco(cliente, enderecos):
    endereco = input("Digite o endereço: ")
    if cliente in enderecos:
        enderecos[cliente].append(endereco)
    else:
        enderecos[cliente] = [endereco]


def listar_enderecos(cliente, enderecos):
    if cliente in enderecos:
        return enderecos[cliente]
    else:
        return []


def menu():
    print("*** ENDEREÇOS ***")
    print("1. Inserir endereço")
    print("2. Listar endereços")
    print("3. Remover endereço")
    print("4. Sair")
    op = int(input("Selecione uma das opções: "))
    if 1 <= op <= 4:
        return op
    else:
        print("Opção inválida.")


def remover_endereco(cliente, enderecos):
    lista = listar_enderecos(cliente, enderecos)
    if len(lista) == 0:
        print("Não há endereços cadastrados para o cliente!")
    else:
        for i in range(len(lista)):
            endereco = lista[i]
            print(f"{i + 1:>3}: {endereco}")
        print(f"{len(lista) + 1:>3}: Cancelar")
        item = int(input("Qual endereço deseja remover? "))
        if 1 <= item <= len(lista):
            enderecos[cliente].remove(lista[item - 1])
        elif item == len(lista) + 1:
            return
        else:
            print("Opção inválida")


def inicio_enderecos(cliente, enderecos: dict):
    while True:
        op = menu()
        if 1 <= op <= 4:
            if op == 1:
                inserir_endereco(cliente, enderecos)
            elif op == 2:
                for endereco in listar_enderecos(cliente, enderecos):
                    print(endereco)
            elif op == 3:
                remover_endereco(cliente, enderecos)
            else:
                break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    enderecos = {}
    nome = input("Digite o nome do cliente: ")
    inicio_enderecos(nome, enderecos)
    

"""
Módulo de cadastro de clientes
"""

import enderecos


def editar_cliente(nome, clientes):
    pesquisa = pesquisar_cliente(nome, clientes)
    if pesquisa[1]:
        cpf = input(f"Digite o novo CPF de {nome}: ")
        clientes[nome] = cpf
        return True
    else:
        return False


def inserir_cliente(clientes):
    cliente = solicitar_dados_cliente()
    pesquisa = pesquisar_cliente(cliente[0], clientes)
    if pesquisa[1]:
        if cliente[1] == pesquisa[0]:
            return False
    clientes[cliente[0]] = cliente[1]
    return True


def listar_clientes(clientes):
    print("*** Lista de Clientes ***")
    for cliente in clientes:
        print(f"{clientes[cliente]:>12}: {cliente}")
    print("*** Fim da Listagem ***")


def menu():
    print("*** CLIENTES ***")
    print("1. Inserir cliente")
    print("2. Editar cliente")
    print("3. Listar clientes")
    print("4. Pesquisar cliente")
    print("5. Gerenciar endereços")
    print("6. Sair")
    op = int(input("Escolha uma das opções: "))
    if 1 <= op <= 6:
        return op
    else:
        print("Opção inválida.")


def pesquisar_cliente(nome, clientes):
    if nome in clientes:
        return clientes[nome], True
    else:
        return "", False


def solicitar_dados_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    return nome, cpf


def inicio_clientes(clientes):
    while True:
        op = menu()
        if op == 1:
            if inserir_cliente(clientes["clientes"]):
                print("Cliente cadastrado com sucesso")
            else:
                print("Operação falhou")
        elif op == 2:
            nome = input("Digite o nome do cliente a ser editado: ")
            if editar_cliente(nome, clientes["clientes"]):
                print("Cliente editado com sucesso")
            else:
                print("Operação falhou")
        elif op == 3:
            listar_clientes(clientes["clientes"])
        elif op == 4:
            nome = input("Digite o nome do cliente a ser editado: ")
            pesquisa = pesquisar_cliente(nome, clientes["clientes"])
            if pesquisa[1]:
                print("*** Dados do Cliente Pesquisado ***")
                print(f"{pesquisa[0]:>12}: {nome}")
            else:
                print("Operação falhou")
        elif op == 5:
            nome = input("Digite o nome do cliente: ")
            pesquisa = pesquisar_cliente(nome, clientes["clientes"])
            if pesquisa[1]:
                Enderecos.inicio_enderecos(nome, clientes["enderecos"])
            else:
                print("Operação falhou")
        else:
            break


if __name__ == '__main__':
    clientes_local = {}
    clientes_local["clientes"] = {}
    clientes_local["enderecos"] = {}
    inicio_clientes(clientes_local)

"""
Módulo de vendas
"""

import clientes
import enderecos
from collections import namedtuple

Venda = namedtuple("Venda", ["valor", "cliente", "endereco"])


def listar_vendas(vendas, clientes):
    clientes_dict = clientes["clientes"]
    enderecos_dict = clientes["enderecos"]
    print("*** Lista de Vendas ***")
    print("  código      vendas        cliente")
    for venda in vendas:
        print(
            f"{venda:^10} R${vendas[venda].valor:^14.2f} {vendas[venda].cliente} ({clientes_dict[vendas[venda].cliente]})")
        print(f"Local de entrega: {vendas[venda].endereco}")
    print("*** Fim da Listagem ***")


def menu():
    print("*** SISTEMA ***")
    print("1. Registrar uma venda")
    print("2. Listar vendas")
    print("3. Gerenciar clientes")
    print("4. Sair")
    op = int(input("Escolha uma das opções: "))
    if 1 <= op <= 3:
        return op
    else:
        print("Opção inválida.")


def registrar_venda(vendas, clientes):
    codigo = int(input("Digite o número do pedido: "))
    nome = input("Digite o nome do cliente: ")
    valor = float(input("Digite o valor da venda: "))
    pesquisa = clientes.pesquisar_cliente(nome, clientes["clientes"])
    if pesquisa[1]:
        print("Selecione um endereço: ")
        enderecos = enderecos.listar_enderecos(nome, clientes["enderecos"])
        for i in range(len(enderecos)):
            endereco = enderecos[i]
            print(f"{i + 1:>3}: {endereco}")
        print(f"{len(enderecos) + 1:>3}: Cancelar")
        item = int(input("Qual endereço deseja selecionar? "))
        if 1 <= item <= len(enderecos):
            venda = Venda(valor=valor, cliente=nome, endereco=enderecos[item - 1])
            vendas = venda 
            return True
        else:
            return False
    else:
        return False


def inicio_vendas(vendas: dict):
    while True:
        op = menu()
        if op == 1:
            if registrar_venda(vendas["vendas"], vendas["clientes"]):
                print("Venda registrada com sucesso!")
            else:
                print("Operação falhou")
        elif op == 2:
            listar_vendas(vendas["vendas"], vendas["clientes"])
        elif op == 3:
            clientes.inicio_clientes(vendas["clientes"])
        else:
            break


if __name__ == '__main__':
    vendas_local = {}
    vendas_local["vendas"] = {}
    vendas_local["clientes"] = {}
    vendas_local["clientes"]["clientes"] = {}
    vendas_local["clientes"]["enderecos"] = {}
    inicio_vendas(vendas_local)