# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# Minha solução
#def duplicar (x): 
#    return x * 2

'''def triplicar (x): 
    return x * 3

def quadruplicar (x): 
    return x * 4

print(duplicar(2)) # 4
print(triplicar(3)) # 6
print(quadruplicar(4)) # 8'''

#sulução mais inteligente e dinâmica

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))

