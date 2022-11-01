# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

#EXERCÍCIO DE MÉTODOS DE LISTAS E FUNÇÕES BUILT IN

"""
Elabore um programa que, numa competição esportiva, pegue as 7 notas atribuidas pelos jurados aos competidores e
remova a maior e a menor nota, e some as demais, usando métos e funções built in.

"""

notasCompetidores = []

for _ in range(7):
    nota = float(input("Digite a nota do competidor: "))
    notasCompetidores.append(nota)
menorNota = min(notasCompetidores)

if notasCompetidores.count(menorNota) == 1:
    notasCompetidores.remove(menorNota)
else:
    indice = -1
    for i in range(len(notasCompetidores)):
        if notasCompetidores[i] == menorNota:
            indice = i
            break
    notasCompetidores.pop(indice)

maiorNota = max(notasCompetidores)

if notasCompetidores.count(maiorNota) == 1:
    notasCompetidores.remove(maiorNota)
else:
    indice = -1
    for i in range(len(notasCompetidores)):
        if notasCompetidores[i] == maiorNota:
            indice = i
            break
    notasCompetidores.pop(indice)

somatoriaNotas = sum(notasCompetidores)

print("A pontuação final do salto é de: {}".format(somatoriaNotas))