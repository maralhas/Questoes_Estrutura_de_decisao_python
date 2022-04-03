#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, 
# informando ao usuário nas seguintes situações:

#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau 
# e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math
valor_a = int(input('Informe o valor de a: '))
if valor_a != 0:
    valor_b = int(input('Informe o valor de b: '))
    valor_c = int(input('Informe o valor de c: '))
    
    delta = (valor_b ** 2) - (4 * valor_a * valor_c)
    if delta < 0:
        print('Delta menor que 0. Raíz imáginaria.')
    elif delta == 0:
        raiz = -valor_b / (2* valor_a)
        print('Delta igual a 0, a raiz é {raiz}')
    else:
        primeira_raiz = (-valor_b + math.sqrt(delta)) / (2 * valor_a)
        segunda_raiz = (-valor_b - math.sqrt(delta)) / (2 * valor_a)
        print(f''' O resultado da primeira raiz é {primeira_raiz}
        O resultado da segunda raiz é: {segunda_raiz}''')
else:
    print('A igual 0, não é uma equação do segundo grau.')
