#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

from re import A


letra = input('Digite uma letra: ')
letra = letra.upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('É vogal')
elif letra != 'A' or letra != 'E' or letra != 'I' or letra != 'O' or letra != 'U':
    print('É consoante') 