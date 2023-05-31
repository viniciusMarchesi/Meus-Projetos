import random

def gerar_jogo_mega_sena(numeros_mais_provaveis, numeros_menos_sorteados, num_pares, num_impares):
    todos_numeros = list(range(1, 61))
    numeros_pares = [num for num in numeros_mais_provaveis + numeros_menos_sorteados + todos_numeros if num % 2 == 0]
    numeros_impares = [num for num in numeros_mais_provaveis + numeros_menos_sorteados + todos_numeros if num % 2 != 0]
    numeros = []
    while len(numeros) < num_pares:
        numero = random.choice(numeros_pares)
        if numero not in numeros:
            numeros.append(numero)
    while len(numeros) < num_pares + num_impares:
        numero = random.choice(numeros_impares)
        if numero not in numeros:
            numeros.append(numero)
    return sorted(numeros)

numeros_mais_provaveis = [10, 53, 5, 37, 33, 23, 4, 30, 41, 42]
numeros_menos_sorteados = [26, 21, 55, 15, 22, 48, 31, 7, 3]

print(gerar_jogo_mega_sena(numeros_mais_provaveis, numeros_menos_sorteados, 4, 2))
print(gerar_jogo_mega_sena(numeros_mais_provaveis, numeros_menos_sorteados, 3, 3))
print(gerar_jogo_mega_sena(numeros_mais_provaveis, numeros_menos_sorteados, 5, 1))
