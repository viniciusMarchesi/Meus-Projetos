'''Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% 
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
 faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.'''

# Pergunta ao usuário horas trabalhadas e ganho por hora.
ganho_hora = input('Quanto você ganha por hora?: ')
horas_trabalhadas = input('Quantas horas você trabalhou?: ')

# Converte em dado float.
ganho_hora_float = float (ganho_hora)
horas_trabalhadas_float = float (horas_trabalhadas)

# Faz o cálculo salário bruto.
salario_bruto = ganho_hora_float * horas_trabalhadas_float

# Faz o cálculo do desconto de imposto de renda.
desconto_imposto_renda = 11 * salario_bruto / 100
desconto_imposto_renda_total = salario_bruto - desconto_imposto_renda

# Faz o cálculo do desconto do INSS.
desconto_inss = 8 * salario_bruto / 100
desconto_inss_total = salario_bruto - desconto_inss

# Faz o cálculo do desconto do sindicato.
desconto_sindicato = 5 * salario_bruto / 100
desconto_sindicato_total = salario_bruto - desconto_sindicato

# Faz o cálculo do sálario liquido já com todos os descontos.
salario_liquido = salario_bruto - desconto_imposto_renda - desconto_inss - desconto_sindicato 

# Imprime na tela o sálario com todas as informações e descontos.
print('O Total de seu sálario Bruto: ', salario_bruto)
print('Desconto IR (11%): ',            desconto_imposto_renda)
print('Desconto INSS: (8%): ',          desconto_inss)
print('Desconto SINDICATO (5%): ',      desconto_sindicato)
print('Salário LÍQUIDO:  ',             salario_liquido)