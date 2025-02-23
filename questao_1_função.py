# Escreva uma função que recebe um número inteiro positivo e retorna True caso ele
# seja primo e False , caso contrário.

# Sugestão:
# def e_primo(n):
# Sua implementação aqui
# print(e_primo(1))
# # False
# print(e_primo(2))
# # True
numero = int(input("Informe um número para análise: \n"))

def e_primo(numero):
    contador = 0
    i = 1
    while i <= numero:
        if numero % i == 0:
            contador = contador + 1
        i = i + 1
    if contador == 2:
        return True
    else:
        return False

x = e_primo(numero)

print("O número é primo?",x)

