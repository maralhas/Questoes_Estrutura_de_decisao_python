#Faça um Programa que leia três números e mostre o maior deles.

numero_um = int(input('Digite um número: '))
numero_dois = int(input('Digite outro número: '))
numero_tres = int(input('Digite mais um número: '))

if numero_um > numero_dois and numero_um > numero_tres:
    print(f'{numero_um} é o maior')
elif numero_tres > numero_dois:
    print(f'{numero_tres} é o maior')
else:
    print(f'{numero_dois} é o maior')