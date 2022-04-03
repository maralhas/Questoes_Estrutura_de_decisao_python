#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

first_score = float(input('Digite a primeira nota: '))
second_score = float(input('Digite a segunda nota: '))
third_score = float(input('Digite a terceira nota: '))
media = (first_score + second_score + third_score) / 3

if media == 10:
    print(f'Aprovado com Distinção, média alcançada: {media}')
elif media >= 7:
    print(f'Aprovado, média alcançada: {media}')
else:
    print(f'Reprovado, média alcançada: {media}')