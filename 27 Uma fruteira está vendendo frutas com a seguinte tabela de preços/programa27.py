#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e 
# escreva o valor a ser pago pelo cliente.

preco_kg_morango = 2.50
preco_morango_maior_5kg =2.20
preco_kg_maca = 1.80
preco_maca_maior_5kg = 1.5

kg_morango = float(input('Informe o peso dos Morangos: '))
kg_maca = float(input('Informe o peso dos Maçã: '))

if kg_morango <= 5 and kg_maca <= 5 or kg_morango > 5 and kg_maca > 5:
    if kg_morango <= 5:
        preco_morango = (kg_morango * preco_kg_morango)
        preco_maca = (kg_maca * preco_kg_maca)
    else:
        preco_morango = (kg_morango * preco_morango_maior_5kg)
        preco_maca = (kg_maca * preco_maca_maior_5kg)
elif kg_morango <= 5 and kg_maca > 5:
    preco_morango = (kg_morango * preco_kg_morango)
    preco_maca = (kg_maca * preco_maca_maior_5kg)
elif kg_morango > 5 and kg_maca <= 5:
    preco_morango = (kg_morango * preco_morango_maior_5kg)
    preco_maca = (kg_maca * preco_kg_maca)
print(preco_maca, preco_morango)

if (kg_morango + kg_maca > 8) or (preco_maca + preco_morango > 25):
    desconto = (preco_maca + preco_morango) * 0.10
    preco_final = (preco_maca + preco_morango) - desconto
    print( f'O valor pago pelo criente é de: {preco_final}')
else:
    preco_final = (preco_maca + preco_morango)
    print( f'O valor pago pelo criente é de: {preco_final}')