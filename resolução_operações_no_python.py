# Resolução dos exercícios do módulo que trata sobre as Operações no Python

# Questão 01

# numero = input("Informe um número:")

# numero = int(numero)

# numero_resto = numero % 2

# print("O número é par?", numero_resto == 0)
# print("O número é impar?" , numero_resto != 0)

#Questão 02

# A saída do primeiro print será True, pois o operador and(lóigico) está comparando se a sentença a<b é verdadeiro ou falso, como é verdadeiro(10>5) ele coloca true na saída. Já o segundo print tem uma NAND, que vai inverter o valor do print anterior por conta do not,logo a saída será false.

# a = 5
# b = 10
# x = True
# y = False
# print((x or y) and (a < b))
# print((x or y) and not (a < b))

#Questão 03

# resultado = 2 + 3 * 2 ** 2
# print(resultado)

#Para plotar o valor 14

# resultado = 2 + 3 * (2 ** 2) #A ordem matemática padrão já resulta em 14
# print(resultado)

#Para plotar o valor 38

# resultado = 2 + (3 * 2) ** 2 
# print(resultado)

#Para plotar o valor 100 

# resultado = ((2 + 3) * 2) ** 2
# print(resultado)

#Questão 04

# valor_de_compra = input("Informe o valor de compra: \n")
# valor_de_compra = float(valor_de_compra)
# valor_do_frete = input("Informe o valor do frete: \n")
# valor_do_frete = float(valor_do_frete)
# fidelidade = input("Cliente é cadastrado no programa de fidelidade? (S) ou (N)\n")

# cupom = (valor_de_compra + valor_do_frete >= 100) or (fidelidade == 'S')

# print("O cupom pode ser utilizado?\n",cupom)