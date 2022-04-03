#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica utilize o operador módulo (resto da divisão).

numero = int(input('Digite um número: '))

verificador = numero % 2

if verificador == 0:
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')