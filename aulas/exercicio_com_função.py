
# criando função que faz multiplicação com args.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    
multplicacao = multiplicar(10, 2, 3, 4, 5)    
print(multplicacao)


# criando função que diz se o numero é par ou impar

def par_impar(numero):
    return numero % 2 == 0

print (par_impar(2))
print (par_impar(3))
print (par_impar(15))
print (par_impar(16))


