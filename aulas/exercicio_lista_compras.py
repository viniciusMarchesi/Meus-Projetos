'''Faça uma lista de compras
o usuario deve ter a possibilidade de
inserir , apagar e listar valores da sua lista
não permita que o programa quebre com
erros de indices inexistentes na lista.
'''
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input ('[i]nserir [a]pagar [l]listar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input ('valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(' escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print(' Por Favor digite Número int.')
        except IndexError:
            print('Indice não existe na lista')
        except Exception :
            print('Erro Desconhecido')
    elif opcao == 'l' :
        os.system('cls')                   
    
        if len (lista) == 0:
         print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor) 
    else :
        print('por favor, escolha i, a ou l. ')        