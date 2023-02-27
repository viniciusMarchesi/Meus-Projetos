#Faça um Programa que pergunte quanto você ganha por hora 
# e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

# Pede ao usuário o ganho por hora e quantas horas foram trabalhadas.
ganho_hora = input('Quanto você ganha por hora?: ')
horas_trabalhadas = input('Quantas horas você trabalhou?: ')

# Converte tipo de dado (str) string em float.
ganho_hora_float = float (ganho_hora)
horas_trabalhadas_float = float (horas_trabalhadas)

# faz o cálculo do sálario do mês e guarda na variável (total_salario).
total_salario = ganho_hora_float * horas_trabalhadas_float

# imprime na tela o sálario.
print('O Total de seu sálario é: ', total_salario)