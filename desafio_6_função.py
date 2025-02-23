# DESAFIO. Uma função fatorial calcula o valor da multiplicação de um certo número
# inteiro não-negativo por todos os números positivos menores que ele. A exceção é
# o fatorial de zero que é igual a 1. Por exemplo:

#     fatorial(3) = 3 * 2 * 1 = 6
#     fatorial(1) = 1
#     fatorial(0) = 1

# Ou seja, podemos definir a função fatorial como:
#     fatorial(n) = n * n-1 * n-2 * ... * 1
# Implemente a função fatorial(n) de modo que ela retorne o valor do fatorial de n.

n = int(input("Informe o valor do número:\n"))

def fatorial(n):
    contador = 1
    total = 1
    while contador <= n:
        total = total * contador
        contador = contador + 1

    return total

x = fatorial(n)
print(f"O fatorial de {n} é {x}")
