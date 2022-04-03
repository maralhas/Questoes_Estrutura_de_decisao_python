#Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero_um = int(input('Digite um número: '))
numero_dois = int(input('Digite outro número: '))
numero_tres = int(input('Digite mais um número: '))
aux = 0

if numero_um < numero_dois and numero_um < numero_tres:
    if numero_tres < numero_dois:
        aux = numero_dois
        numero_dois = numero_tres
        numero_tres = aux
    print(f'{numero_um, numero_dois, numero_tres}')

elif numero_tres < numero_dois:
    aux = numero_tres
    numero_tres = numero_um
    numero_um = aux 
    print(f'{numero_um, numero_dois, numero_tres}')

else:
    aux = numero_dois
    numero_dois = numero_um
    numero_um = aux
    print(f'{numero_um, numero_dois, numero_tres}')