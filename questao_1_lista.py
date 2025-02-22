# Escreva um programa que lê números inteiros positivos do usuário, um após o
# outro, e monta uma lista a partir desses números e depois imprime a lista montada.
# O programa deve continuar solicitando por números até que o elemento digitado
# seja um número negativo (que não deve ser inserido na lista).

lista = []
i = 0
while True:
    numero = int(input("Informe um número: \n"))
    lista.append(numero)
    if lista[i] < 0:
        lista.pop()
        break
    i = i + 1

print(lista)

    