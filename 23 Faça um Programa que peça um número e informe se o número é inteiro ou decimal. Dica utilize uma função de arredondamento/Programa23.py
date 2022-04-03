#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica utilize uma função de arredondamento.

import math
numero = float(input('Digite um numero: '))

if numero != math.floor(numero):
    print(f'O número {numero} é decimal.')
else:
    print(f'O número {numero} é inteiro.')
