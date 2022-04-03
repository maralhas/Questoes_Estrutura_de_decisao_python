#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#a. par ou ímpar;
#b. positivo ou negativo;
#c. inteiro ou decimal.

first_number = int(input('Digite um número: '))
second_number = int(input('Digite outro número: '))

option = input('''Escolha uma das opção abaixo:
a. par ou ímpar
b. positivo ou negativo
c. inteiro ou decimal: ''')
option = option.lower()

if option == 'a':
    if (first_number % 2) == 0 and (second_number % 2) == 0:
        print( f'Os dois numeros são pares.')
    elif(first_number % 2) == 0 and (second_number % 2) == 1 or (first_number % 2) == 1 and (second_number % 2) == 0:
        if (first_number % 2) == 0:
            print( f'O primeiro número {first_number} é par e o segundo número {second_number} é impar.')
        else:
            print( f'O primeiro número {first_number} é ímpar e o segundo número {second_number} é par.')
    else:
        print( f'Os dois numeros são ímpares.')
