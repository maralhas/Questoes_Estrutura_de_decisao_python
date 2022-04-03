#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo
#Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

from re import S


primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
media = (primeira_nota + segunda_nota) / 2
conceito = ''
status = ''

if media >= 9 and media <= 10:
    conceito = 'A'
    status = 'APROVADO'
elif media >= 7.5:
    conceito = 'B'
    status = 'APROVADO'
elif media >= 6:
    conceito = 'C'
    status = 'APROVADO'
elif media >= 4:
    conceito = 'D'
    status = 'REPROVADO'
else:
    conceito = 'E'
    status = 'Reprovado'

print(f''' Primeira nota: {primeira_nota}
Segunda nota: {segunda_nota}
Media: {media} Conceito: {conceito}
status : {status}
''')