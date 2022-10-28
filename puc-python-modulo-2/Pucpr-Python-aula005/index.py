#Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
#segundo Módulo - Python
#Aluno: Jackson Douglas de Souza
#Matéria: Raciocínio Computacional


#ESTRUTURAS DE REPETIÇÃO

for i in range(10):
   print(i)



for i in range(10):
    print(i)



for i in range(10):
    print(i)
    if i == 5:
        break




i = 0
while i < 10:
    print(i)
    i = i + 1



i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i = i + 1



for i in range(10):
    if i == 5:
        continue
    print(i)




i = 0
while i < 10:
    i = i + 1
    if i == 5:
        continue
    print(i)



i = 0
while i < 10:
    i = i + 1

    if i == 5:
        pass
    else:
        print(i)




i = 1
while i <= 10:
    print(i)
    i = i + 1



i = 3
while i <= 18:
    print(i, end=" ")
    i = i + 3 #vai pular de três em trÊs
    



i = 1.50
while i <= 3.0:
    print("R${:.2f}".format(i), end=" || ")
    i = i + 0.25


#DECRESCENTE


i = 10
while i >= 1:
    print(" Nº{}".format(i), end="  ||  ")
    i = i - 1



'''
Elabore um código que, analise a seguinte situação: 
Cliente faz aplicação financeira de 100,00 com rendimentos mensais de 5% ao mês.
Quantos meses serão necessários para o capital investido ultrapasse a 200,00. 
'''



capitalInicial = float(input("Insira o valor inicial da aplicação: "))
mes = 0

while capitalInicial <= 200:
    capitalInicial = capitalInicial + (capitalInicial * (5 / 100))
    mes = mes + 1
    print("No {}º mês renderá = R${:.2f} ".format(mes, capitalInicial))

print("\nEsse será o valor da aplicação R${:.2f} em {} meses.".format(capitalInicial, mes))


