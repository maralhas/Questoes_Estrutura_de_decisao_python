#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

valor = int(input('Informe o primeiro número: '))

if valor >= 0:
    print(f'O número {valor} é POSITIVO')
else:
    print(f'O número {valor} é NEGATIVO')