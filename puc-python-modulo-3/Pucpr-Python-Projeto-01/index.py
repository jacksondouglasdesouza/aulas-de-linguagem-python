# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Terceiro Módulo — PROJETO - 01 - Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional


'''
PROJETO — 01 — carrinho de compras!
Crie um programa que simule um carrinho de compras, solicitando o nome do produto (não pode ser vazio),
o seu valor (valor decimal, positivo) e quantidade a ser comprada (valor inteiro, positivo). Ao incluir um produto,
deve perguntar se o usuário deseja fechar o pedido ou incluir mais produtos. Todos os dados devem ser validados.
Ao final da compra, deve ser informado o valor total do pedido.
'''



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
            print("ERROR! O valor é inválido, Não tente me enganar tente novamente!")
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

