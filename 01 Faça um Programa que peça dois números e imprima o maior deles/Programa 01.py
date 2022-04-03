#Faça um Programa que peça dois números e imprima o maior deles.

primeiro_numero = int(input('Informe o primeiro número: '))
segundo_numero = int(input('Informe o segundo número: '))

if primeiro_numero > segundo_numero:
    print(f'O mair número é: {primeiro_numero}')
else:
    print(f'O mair número é: {segundo_numero}')