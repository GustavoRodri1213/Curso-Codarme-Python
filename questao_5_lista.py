# Suponha o seguinte programa:

#  Alunos e suas notas representados através de dicionários
# alunos = [
# {
# "nome": "Alice",
# "nota": 8,
# },
# {
# "nome": "Bob",
# "nota": 7,
# },
# {
# "nome": "Carlos",
# "nota": 9,
# }
# ]
# Escreva uma programa que calcula a média das notas de todos os alunos.
alunos = [
 {
 "nome": "Alice",
 "nota": 8,
 },
 {
 "nome": "Bob",
 "nota": 7,
 },
 {
 "nome": "Carlos",
 "nota": 9,
 }
 ]

mediador = []

for value in alunos:
    print(value)
    mediador.append(value["nota"])

somatorio = 0
media = 0

for i in mediador:
    somatorio = i + somatorio
     
media = somatorio / len(mediador) 
print(media)   

