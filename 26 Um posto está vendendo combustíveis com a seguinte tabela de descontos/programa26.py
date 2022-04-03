#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litro_alcool = 1.90
litro_gasolina = 2.50
litros = int(input('Informe quantos litros: '))
tipo_de_combustivel = input('(A) Álcool | (G) Gasolina:')
tipo_de_combustivel = tipo_de_combustivel.upper()

if tipo_de_combustivel == 'A':
    if litros <= 20:
        preco = (litros * litro_alcool)
        descoto = preco * 0.03
        preco_com_desconto = preco - descoto
    else:
        preco = (litros * litro_alcool)
        descoto = preco * 0.05
        preco_com_desconto = preco - descoto
    print(f'O valor a ser pago para {litros} de álcool é de: {preco_com_desconto}')

if tipo_de_combustivel == 'G':
    if litros <= 20:
        preco = (litros * litro_gasolina)
        descoto = preco * 0.04
        preco_com_desconto = preco - descoto
    else:
        preco = (litros * litro_gasolina)
        descoto = preco * 0.06
        preco_com_desconto = preco - descoto
    print(f'O valor a ser pago para {litros} de gasolina é de: {preco_com_desconto}')