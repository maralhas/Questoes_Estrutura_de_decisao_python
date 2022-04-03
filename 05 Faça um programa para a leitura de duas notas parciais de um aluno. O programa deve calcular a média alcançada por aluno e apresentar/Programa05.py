#Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

if media == 10:
    print(f'A media é {media}: Aprovado com Distinção')
elif media >= 7:
    print(f'A media é {media}: Aprovado')
else:
    print(f'A media é {media}: Reprovado')