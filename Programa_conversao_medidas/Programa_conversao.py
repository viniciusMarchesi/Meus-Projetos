#Faça um Programa que converta metros para centímetros.

# Pede ao usuário que digite a medida em metros.
medida = input('Digite a medida em metros: ')

# Converte a medida em um dado de ponto flutuante (float).
medida_float = float(medida)

# Pega a medida já em tipo de dado float, multiplica por 100 
# e guarda na variavel (medida_centimetros).
medida_centimetros = medida_float * 100

# Mostra ao usuario a medida já convertida em centímetros.
print('A medida convertida em centimetros é: ', medida_centimetros)