# Implemente uma função maior_idade(pessoa) que receba uma tupla representando
# uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou
# não.

nome = input("Informe o nome da pessoa:\n")
idade = int(input("Informe a idade da pessoa:\n"))

pessoa = (nome,idade)

def maior_idade(pessoa):
    nome,idade = pessoa
    if idade >= 18:
        print(f"{nome} é maior de idade!")
    else:
        print(f"{nome} não é maior de idade!")

maior_idade(pessoa)