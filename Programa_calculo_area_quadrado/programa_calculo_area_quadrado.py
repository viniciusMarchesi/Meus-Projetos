# Faça um Programa que calcule a área de um quadrado, 
#em seguida mostre o dobro desta área para o usuário.

# Pede ao usuário altura e base do quadrado.
altura = input('Digite a altura do quadrado: ')
base = input('Digite a base do quadrado: ')

# Transforma altura e base em inteiros (int).
altura_int = int(altura)
base_int = int(base)

# Faz o cálculo da área e guarda na variável (area_quadrado).
# Faz o cálculo do dobro da área e guarda na variável (dobro_area).
area_quadrado = base_int * altura_int
dobro_area = area_quadrado * 2

# Imprime na tela a área do quadrado e o dobro da mesma.
print(' A área do quadrado é: ', area_quadrado)
print(' O dobro da área do quadrado é: ', dobro_area)