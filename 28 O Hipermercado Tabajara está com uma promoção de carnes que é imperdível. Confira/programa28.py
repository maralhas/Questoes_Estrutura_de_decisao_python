#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

preco_kg_file_duplo = 4.90
preco_kg_alcatra = 5.90
preco_kg_picanha = 6.90
preco_5kg_file_duplo = 5.80
preco_5kg_alcatra = 6.80
preco_5kg_picanha = 7.80
tipo_de_pagamento = 'Dinheiro'
desconto = 0 

kg = float(input('Informe a quantidade desejada: '))
carne = int(input('''Informe a carne escolhida: 
ID      Carne
01      File Duplo
02      Alcatra
03      Picanha 
'''))
cartao = False
opcao = input('A compra será feita no cartão da loja: (S) sim (N) não')
opcao = opcao.upper()

if opcao == 'S':
    cartao = True

if carne == 1:
    if kg <= 5:
        compra = preco_kg_file_duplo * kg
    else:
        compra = preco_5kg_file_duplo * kg
    tipo_de_carne = 'File duplo'
elif carne == 2:
    if kg <= 5:
        compra = preco_kg_alcatra * kg
    else:
        compra = preco_5kg_alcatra * kg
    tipo_de_carne = 'Alcatra'
elif carne == 3:
    if kg <= 5:
        compra = preco_kg_picanha * kg
    else:
        compra = preco_5kg_picanha * kg
    tipo_de_carne = 'Picanha'

if cartao == True:
    desconto = compra * 0.05
    tipo_de_pagamento = 'Cartão da loja'

print(f'''Tipo de carde: {tipo_de_carne} quant.: {kg}Kg
Total: R$ {compra}
Tipo de pagamento {tipo_de_pagamento}
Desconto : R$ {desconto}
Total a pagar: {compra - desconto}
''')