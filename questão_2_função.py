# Implemente uma função que recebe uma lista de números inteiros e retorna uma
# tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num
# é o valor desse número.

lista = [1, 7, 3, 4, 5, 6, 2] ##Deve retornar posição 1 e valor 7 *1,7) (pos,num)

def tupla(lista):
    maior = 0
    resultado = ()
    for numero in lista:
        if numero > maior:
            maior = numero
            posicao = lista.index(maior)
            resultado = (posicao,maior)
    return resultado

x = tupla(lista)
print(x)

