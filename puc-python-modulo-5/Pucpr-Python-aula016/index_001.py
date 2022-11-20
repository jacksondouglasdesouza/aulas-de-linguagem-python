# Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas - PUCPR
# Quinto Módulo — Python
# Aluno: Jackson Douglas de Souza
# Matéria: Raciocínio Computacional

# CONTINUAÇÃO namedtuples()

from collections import namedtuple


pessoa = namedtuple('pessoa', 'nome, profissao rua numero')

Douglas = pessoa('Douglas', 'Programador', 'Rua Acácia', 556)

print(Douglas)



figurinhaJogadores = namedtuple('jogador', 'Nome Time Camisa Numero')

jogador_01 = figurinhaJogadores('Neymar Jr', 'Brasil', 10, 12)
print(len(jogador_01))
print(jogador_01)
print(jogador_01[2])
print(jogador_01.Nome, jogador_01.Time, jogador_01.Camisa, jogador_01.Numero)
print(jogador_01.index(10))
print(jogador_01.index(12))




#Elabore um programa que faça uso de uma tupla chamada endereço, contendo os dados nomeados.

enderecoUsuario = namedtuple('endereco', 'rua numero bairro cidade estado')

endereco_01 = enderecoUsuario('Rua Cristovo Colombo', 369, 'Castelo Branco', 'Florianópolis', 'SC')
endereco_02 = enderecoUsuario('Rua da Luxação', 896, 'Castro de Alves', 'Rio de Janeiro', 'RJ')

print('O ENDEREÇO 01 É: ')
print('Rua: {}'.format(endereco_01.rua))
print('Numero: {}'.format(endereco_01.numero))
print('Bairro: {}'.format(endereco_01.bairro))
print('Cidade: {}'.format(endereco_01.cidade))
print('Estado: {}\n'.format(endereco_01.estado))

print('O ENDEREÇO 02 É: ')
print('Rua: {}'.format(endereco_02.rua))
print('Numero: {}'.format(endereco_02.numero))
print('Bairro: {}'.format(endereco_02.bairro))
print('Cidade: {}'.format(endereco_02.cidade))
print('Estado: {}'.format(endereco_02.estado))




#Elabore um Código que simule o cadastro de telefones com dicionário como uma agenda, mostrar o Dic na saida

agenda = {}

print(" 》》》 Cadastro de Telefones ☎")

while True:
    nome = input("》 Digite o nome do usuário: ")
    fone = input('》 Digite o Número de Telefone: ')
    agenda[nome] = fone
    if input('Deseja cadastrar outro Número [Sim] ou [Não]: ') == 'Não':
        break
print(agenda)




'''
Elabore um Código que simule o cadastro de telefones com dicionário como uma agenda, caso seja validado um contato
já existente, perguntar se o usuário deseja alterar o contato. Caso um telefone informado seja existente na agenda
mostrar mensagem que este número já existe na agenda!

'''


agenda = {}
print(" 》》》 Cadastro de Telefones ☎")

while True:
    nomeUsuario = input("Digite o nume do Usuário: ")
    contatoUsuario = input("Informe o telefone do Usuário: ")

    if nomeUsuario in agenda:
        if input(f"Usuário já cadastrado com o número: {agenda[nomeUsuario]}."
                 f"Deseja alterar? [S] ou [N]") == 'n' or 'N':
            break
    if contatoUsuario in agenda.values():
        print(f'Esse número {contatoUsuario} já está registrado em outro usuário.')
        continue
        agenda = [contatoUsuario]
        if input("Deseja cadastrar um novo contato? [S] ou [N]") == 'n' or 'N':
            break
print(agenda)


'''

Crie um programa que efetue o cadastro de pessoas com nome, RG e CPF por meio de tuplas, adicionando-as a uma
lista e imprimindo essa lista no fim do programa.

'''

pessoas = []
while True:
    nome = input('Digite o seu nome: ')
    rg = input('Digite seu RG: ')
    cpf = input('Digite seu CPF: ')
    pessoa = (nome, rg, cpf)
    pessoas.append(pessoa)
    if input('Gostaria de cadastrar outra pessoa? ') == 'n':
        break
print(pessoas)



'''
Crie um programa que cadastre os funcionários de uma empresa e seus dependentes. O funcionário deve ser cadastrado
com matrícula, nome e dependentes. Os dependentes devem ser inseridos dinamicamente em uma tupla. Use o operador
' += '

'''


funcionarios = []

while True:
    nomeFuncionario = input('Digite seu nome: ')
    idFuncionario = input('Digite sua matricula: ')
    dependentesFuncionario = tuple()
    while True:
        dependentes = input('Tem outro dependente para cadastrar? ')
        if dependentes == 'não':
            break
        dependentesFuncionario += (dependentes, )
    colaborador = (nomeFuncionario, idFuncionario, dependentesFuncionario)
    funcionarios.append(colaborador)
    if input('Gostaria de cadastrar outro funcionário? ') == 'n':
        break
print(funcionarios)




'''
Crie um programa que cadastre locais históricos do mundo com suas coordenadas geográficas, fanzendo o uso de tuplas
cp, parâmetrôs  nomeados. Use a função namedtuple().

'''

'''
Crie um programa que cadastre produtos e preços. Caso o produto inserido já exista na lista,
informa ao usuário sobre e perguntar se ele deseja atualizar o preço.
'''

estoque = {}
print('》》》》》》》》》》》》》》》》》》》》》》》》')
while True:
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    if produto in estoque:
        if input("Esse produto já consta nop estoque. Deseja atualizar o valor? ") == 'n':
            continue
    estoque[produto] = valor
    if input("Deseja cadastrar outro produto ao estoque? [sim] ou [não]: ") == 'n':
        break
for produtoRecebido in estoque:
    print(f'》》》 {produtoRecebido} R${estoque[produtoRecebido]:.2f}')

print('》》》》》》》》》》》》》》》》》》》》》》》》')



'''
Crie um programa que solicite o valor de vendas e o mês em que a venda ocorrêu.
Independentimente da repetição de meses, o código deve totalizar por mês todas as vendas cadastradas.
Deve imprimir no final o valor com todas as vendas do ano.

'''


cadastroVendas = {}

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']

while True:
    mes = input("Informe o mês: ")
    valor = float(input("Informe o valor do faturamento: "))

    if not mes in meses:
        print('Insira um mês válido. Tente novamente!')
        continue
    if mes in cadastroVendas:
        cadastroVendas[mes] += valor
    else:
        cadastroVendas[mes] = valor

    if input("Deseja Continuar? [s] ou [n]") == 'n':
        break

for mes in meses:
    if mes in cadastroVendas:
        print(f"Mês {mes} - R${cadastroVendas[mes]:.2f}")
    else:
        print(f"Mês {mes} - R$ 00,00")
        


frutas = {'cod01': "Laranja", 'cod02': "Mamão", 'cod03': "Jaca", "cod04": "Melância", 'cod05': "Uva", 'cod06': "Goiaba"}
frutas["cod07"] = "Graviola"
print(frutas)

del frutas["cod07"]
print(frutas)

for i in frutas.values():
    print(i)
print("\n")
for i in frutas.keys():
    print(i)

print("\n")
print(frutas.items())
print("\n")
for i in frutas.items():
    print(i)
print("\n")

frutas['cod008'] = ["Queijo", "Ovos", "Molho Pimenta"]

print(frutas)

for key, item in frutas.items():
    print("Id: {} - Produto: {}".format(key, item))





listaFrutas = {}
indice = 0
while indice < 5:
    indice += 1
    nomeFruta = input("Digite o nome da fruta: ")
    unidadeMedida = input("A fruta é vendida por Unidade [U] ou Kilo [K]: ")
    tipoUnidadeMedida = ''
    if unidadeMedida == 'u':
        tipoUnidadeMedida = 'Unidade'
    else:
        tipoUnidadeMedida = 'Kg'
    preco = float(input("Digite o preço: "))
    listadeDados = []
    listadeDados.append(nomeFruta)
    listadeDados.append(tipoUnidadeMedida)
    listadeDados.append(preco)
    codigo = "Id-0" + str(indice)
    listaFrutas[codigo] = listadeDados


print('》》》》》》》》》》》》》》》》》》》》》》》》')
print("Frutas Unidades: ")

for key, listaFrutasrecebe in listaFrutas.items():
    if listaFrutasrecebe[1] == 'Unidade':
        print(key, listaFrutasrecebe)

print('\n》》》》》》》》》》》》》》》》》》》》》》》》')
print("Frutas Quilogramas: ")
for key, listaFrutasrecebe in listaFrutas.items():
    if listaFrutasrecebe[1] == 'Kg':
        print(key, listaFrutasrecebe)


