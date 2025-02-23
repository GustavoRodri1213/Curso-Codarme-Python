# Implemente uma função que recebe dois argumentos, uma lista e um elemento , e
# retorna True caso elemento seja encontrado na lista , e False caso contrário. Não
# é permitido utilizar o método in .

lista = [1 ,2 ,3 ,4 ,5 ,6]
valor = 5

def verificacao(lista,valor):
    i = 0
    contador = 0
    while i < len(lista):
        if lista[i] == valor:
            contador = contador + 1
            break
        else:
            contador = contador
            i = i + 1


    if contador >= 1:
        return True
    else:
        return False

x = verificacao(lista,valor)
print(x)
