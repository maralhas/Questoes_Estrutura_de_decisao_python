#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessconoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 
# "Suspeita", entre 3 e 4 
# como "Cúmplice" e 
# 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

print('''Responta as perguntas abaixo com: 
((S) para SIM e (N) para NÃO''')

counter = 0
question_1 = input('Telefonou para a vítima?')
question_1 = question_1.upper()
if question_1 == 'S':
    counter += 1

question_2 = input('Esteve no local do crime?')
question_2 = question_2.upper()
if question_2 == 'S':
    counter += 1

question_3 = input('Mora perto da vítima?')
question_3 = question_3.upper()
if question_3 == 'S':
    counter += 1

question_4 = input('Devia para a vítima?')
question_4 = question_4.upper()
if question_4 == 'S':
    counter += 1

question_5 = input('Já trabalhou com a vítima?')
question_5 = question_5.upper()
if question_5 == 'S':
    counter += 1

if counter == 5:
    print('Assassino')
elif counter >= 3:
    print('Cumprice')
elif counter == 2:
    print('Suspeito')
else:
    print('Inocente')