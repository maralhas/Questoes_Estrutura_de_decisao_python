#Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00


valor_hora_trabalhada = float(input('Informe o valor da hora trabalhada: '))
quantidade_de_horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))
salario_bruto = valor_hora_trabalhada * quantidade_de_horas_trabalhadas
sindicato = salario_bruto * 0.03

ir = 0
if salario_bruto <= 900:
    ir = 0
elif salario_bruto < 1500:
    ir = 0.05
elif salario_bruto < 2500:
    ir = 0.10
else:
    ir = 0.20

ir_descontado = salario_bruto * ir
fgts = 0.11
fundo_de_garantia = salario_bruto * fgts
inss = 0.10
inss_descontado = salario_bruto * inss
descontos =  ir_descontado + inss_descontado
salario_liquido = salario_bruto - descontos

print(f''' Salário Bruto: ({quantidade_de_horas_trabalhadas} * {valor_hora_trabalhada})        : R$ {salario_bruto}
(-) IR ({ir * 100})                     : R$   {ir_descontado}  
(-) INSS (10%)                 : R$  {inss_descontado}
FGTS (11%)                      : R$  {fundo_de_garantia}
Total de descontos              : R$  {descontos}
Salário Liquido                 : R$  {salario_liquido}''')