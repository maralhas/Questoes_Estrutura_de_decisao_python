#Faça um Programa que leia três números e mostre o maior e o menor deles.

numero_um = int(input('Digite um número: '))
numero_dois = int(input('Digite outro número: '))
numero_tres = int(input('Digite mais um número: '))

maior = 0
menor = 0

if numero_um > numero_dois and numero_um > numero_tres:
    maior = numero_um
    if numero_dois > numero_tres:
        menor = numero_tres
    print(f'{maior} é o maior')
    print(f'{menor} é o menor')

elif numero_tres > numero_dois:
    maior = numero_tres
    if numero_um > numero_dois:
        menor = numero_dois
    else:
        menor = numero_um
    print(f'{maior} é o maior')
    print(f'{menor} é o menor')

else:
    maior = numero_dois
    if numero_um > numero_tres:
        menor = numero_tres
    else:
        menor = numero_um
    print(f'{maior} é o maior')
    print(f'{menor} é o menor')
