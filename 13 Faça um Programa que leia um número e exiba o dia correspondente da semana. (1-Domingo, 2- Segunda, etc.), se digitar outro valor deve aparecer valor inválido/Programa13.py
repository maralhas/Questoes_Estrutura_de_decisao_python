#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia_da_semana = int(input('Digite um número: '))

if dia_da_semana == 1:
    print('1- Domingo')
elif dia_da_semana == 2:
    print('2- Segunda')
elif dia_da_semana == 3:
    print('3- Terça')
elif dia_da_semana == 4:
    print('4- Quarta')
elif dia_da_semana == 5:
    print('5- Quinta')
elif dia_da_semana == 6:
    print('6- Sexta')
elif dia_da_semana == 76:
    print('7- Sabado')
else:
    print('Valor inválido.')