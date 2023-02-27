#Faça um Programa que peça a temperatura em graus Fahrenheit, 
#transforme e mostre a temperatura em graus Celsius.

# Pede ao usuário a temperatura em graus fahrenheit.
temperatura_Fahrenheit = input('Qual a temperatura em Fahrenheit?: ')

# Tranforma temperatura fahrenheit de (int) para (float).
temperatura_Fahrenheit_float = int(temperatura_Fahrenheit)

# Faz o cálculo já transformando em graus celsius e guardando na váriavel.
temperatura_celsius = (temperatura_Fahrenheit_float - 32) * 5 / 9

# Imprime na tela a temperatura em graus Celsius.
print('A temperatura em Graus Celsius é: ', temperatura_celsius)