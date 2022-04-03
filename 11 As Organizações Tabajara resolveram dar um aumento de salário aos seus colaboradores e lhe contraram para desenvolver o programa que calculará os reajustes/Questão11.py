#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa 
# que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

from ast import NodeVisitor


salario_atual = float(input('Informe o valor do salário: '))

if salario_atual <= 280:
    percentual_de_aumento = 0.20
    valor_do_aumento = salario_atual * 0.20
    novo_salario = salario_atual + valor_do_aumento

elif salario_atual < 700:
    percentual_de_aumento = 0.15
    valor_do_aumento = salario_atual * 0.15
    novo_salario = salario_atual + valor_do_aumento

elif salario_atual < 1500:
    percentual_de_aumento = 0.10
    valor_do_aumento = salario_atual * 0.10
    novo_salario = salario_atual + valor_do_aumento
else:
    percentual_de_aumento = 0.05
    valor_do_aumento = salario_atual * 0.05
    novo_salario = salario_atual + valor_do_aumento
    
print(f'''Salário Atual: R$ {salario_atual}
Percentual de aumento aplicado: {percentual_de_aumento * 100} %
Valor do aumento R$ {valor_do_aumento}
Novo Salário R$ {novo_salario}''')


