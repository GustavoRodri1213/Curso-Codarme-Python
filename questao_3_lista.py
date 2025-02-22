# Data uma lista de números inteiros, escreva um programa que calcula a média dos
# números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3
# deve imprimir apenas 12 .
# Se preferir, pode utilizar a lista abaixo como exemplo:
# lista = [1, 10, 20, 35, 22, 12]
#  Resultado deve ser 16

lista = [1, 10, 20, 35, 22, 12]
somatorio = 0
media = 0

for x in lista:
    somatorio = x + somatorio

media = somatorio // len(lista)
print(media)

