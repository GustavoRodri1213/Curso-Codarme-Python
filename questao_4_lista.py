# Suponha o seguinte programa:
#  Alunos e suas respectivas notas
# alunos = [
# ("Alice", 8),
# ("Bob", 7),
# ("Carlos", 9),
# ]
# Escreva uma programa que calcula a média das notas de todos os alunos.

alunos = [
    ("Alice",8),
    ("Bob",7),
    ("Carlos",9),
]

somatorio = 0
media = 0

for k,i in alunos:
    somatorio = i + somatorio
    print(i)

media = somatorio / len(alunos)

print("A média é:",media)

