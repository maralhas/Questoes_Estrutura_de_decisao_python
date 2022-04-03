#Faça um programa que pergunte o preço de três produtos e informe qual 
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto_um = float(input('Informe o valor do produto: '))
produto_dois = float(input('Informe o valor do produto: '))
produto_tres = float(input('Informe o valor do produto: '))

if produto_um < produto_dois and produto_um < produto_tres:
    print('Compre o produto 1')
elif produto_tres < produto_dois:
    print('Compre o produto 3')
else:
    print('Compre o produto 2')