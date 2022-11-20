# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Sexto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# CONTINUAÇÃO def() Funções em Python
import math

def consultar(contatos):
    f = open('dados.txt', 'r')
    linhas = f.readlines()
    for linha in linhas:
        linha = linha.replace("\n", "")
        nome, fone = linha.split(",")
        if contatos == nome:
            print(nome, fone)
    f.close()

def inserirContatos(nome, fone):
    f = open('dados.txt', 'a')
    linha = nome+","+fone+"\n"
    f.writelines(linha)
    f.close()

def deletarContato(contatos):
    f = open('dados.txt', 'r')
    linhas = f.readlines()
    linhas02 = []

    for linha in linhas:
        ax = linha
        linha = linha.replace("\n", "")
        nome, fone = linha.split(",")
        if contatos == nome:
            pass
        else:
            linhas02.append(ax)
    f.close()
    f = open('dados.txt', 'w')
    f.writelines(linhas02)
    f.close()


def atualizarContatos(contatos, fone02):
    f = open('dados.txt', 'r')
    linhas = f.readlines()
    lista02 = []

    for linha in linhas:
        ax = linha
        linha = linha.replace("\n", "")
        nome, fone = linha.split(",")
        if contatos == nome:
            lista02.append(nome+" "+fone02+"\n")
        else:
            lista02.append(ax)
    f.close()
    f = open('dados.txt', 'w')
    f.writelines(lista02)
    f.close()

#consultar("Maria")
#inserirContatos("Jackson Doulas", "(48) 99166-8449")
#deletarContato("Maria")

atualizarContatos("Jackson Doulas", " 021 3236 4525")
