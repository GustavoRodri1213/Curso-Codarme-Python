# DESAFIO. Escreva um programa que dado uma lista de números inteiros, imprime
# o maior número dessa lista.
# lista = [1, 3, 2, 5]

#  Deve imprimir 5
lista = [1, 3, 2, 5]
maior = 0

for i in lista:
    if i > maior:
        maior = i
print(maior)