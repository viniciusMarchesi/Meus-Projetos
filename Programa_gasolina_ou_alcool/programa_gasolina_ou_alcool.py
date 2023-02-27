# Pede ao usuário o preço da gasolina e do alcool.
preco_gasolina = input('Qual é o preço da Gasolina? : ')
preco_etanol = input ('Qual é o preço do Etanol?: ')

# Converte em tipo de dado float.
preco_gasolina_float = float(preco_gasolina)
preco_etanol_float = float(preco_etanol)

# Faz o cálculo e guarda na váriavel (resultado_calculo).
resultado_calculo = preco_etanol_float / preco_gasolina_float

# imprime na tela qual combustivel é mais vantajoso.
if resultado_calculo <= 0.70:
    print('Compensa abastecer com Alcool')
else:
    print('Compensa abastecer com Gasolina')    
