# Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto uma
# tupla quanto um dicionário. Dica: método type pode te ajudar.

tipo_de_entrada = input("Quer armazenar os dados em: Dicionario 'D' ou Tupla 'T' ?\n")

if tipo_de_entrada == "T":
    nome = input("Informe seu nome:\n")
    idade = int(input("Informe a sua idade: \n"))
    pessoa = (nome,idade)
elif tipo_de_entrada == "D":
    nome = input("Informe seu nome:\n")
    idade = int(input("Informe a sua idade: \n"))
    pessoa = {"nome":nome , "idade":idade}
else:
    print("Entrada inválida!")
    pessoa = None

def maior_de_idade(pessoa):
    if type(pessoa) == tuple:
        nome, idade = pessoa
    elif type(pessoa) == dict:
        nome = pessoa.get('nome')
        idade = pessoa.get('idade')
    else:
        print("Tipo de entrada inválido!")
        return
    
    if idade >=18:
        print(f"{nome} é maior de idade!")
    else:
        print(f"{nome} é menor de idade!")

if pessoa:
    maior_de_idade(pessoa)
