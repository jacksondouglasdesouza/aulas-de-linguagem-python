# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quarto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# CONTINUAÇÃO - ESTRUTURAS DE REPETIÇÃO - for | while

import math

print("▬"*20)
print(" 𝓑𝓔𝕸 𝓥𝓘𝓝𝓓𝓞 𝓗𝓤𝓜𝓐𝓝𝓞")
print(" 🅵🅰🅲🅰 🆂🆄🅰🆂 🅲🅾🅽🅿🆁🅰🆂")
print("▬"*20)

valordasCompras = 0
flag = True

while flag:
    while True:
        selecaoProduto = input("❱ 🅢🅔🅛🅔🅒🅘🅞🅝🅔 🅞 🅟🅡🅞🅓🅤🅣🅞 : ")
        if selecaoProduto != "":
            break
        else:
            print("Produto é inválido!")
    while True:
        try:
            valorProduto = float(input("❱ 🅠🅤🅐🅛 🅞 🅥🅐🅛🅞🅡: "))
            if valorProduto <= 0:
                print("Zero não é um valor válido!")
            else:
                break
        except ValueError:
            print("ERROR! O valor é inválido, tente novamente!")
    while True:
        try:
            quantidadeProduto = int(input("❱ 🅠🅤🅐🅛 🅐 🅠🅤🅐🅝🅣🅘🅓🅐🅓🅔: "))
            if quantidadeProduto <= 0:
                print("Quantidade não pode ser de 0")
            else:
                break
        except ValueError:
            print("ERROR! Quantidade de produto escolhihda inválida!")

    valordasCompras += quantidadeProduto * valorProduto
    respostaUsuario = input("❱ 🅟🅡🅞🅓🅤🅣🅞🅢 🅝🅐 🅢🅐🅒🅞🅛🅐, 🅓🅔🅢🅔🅙🅐 🅐🅛🅖🅞 🅜🅐🅘🅢 ☑ Sim ░ ☒ Não ")
    if respostaUsuario == "Não":
        flag = False
print(f"O valor total a pagar é: R${valordasCompras:.2f}")




