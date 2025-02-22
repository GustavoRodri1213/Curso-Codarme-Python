# DESAFIO. Escreva um programa que declara uma lista com elementos de
# diferentes tipos e imprime na tela essa lista invertida. Não é permitido utilizar
# métodos como reverse ou sort .

# def inverte_lista(lista):
# ...
# lista = ["a", 5, {1}]
# lista_invertida = inverte_lista(lista)
# print(lista_invertida)
# # [{1}, 5, "a"]

lista = ["a",5,{1}]
tamanho_lista = len(lista)
lista_invertida = []
for i in range(tamanho_lista-1,-1,-1):  # range(start,stop,step) 
    lista_invertida.append(lista[i])

print(lista_invertida)