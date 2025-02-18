#Questão 01 Condicionais if/else/elif

# numero = int(input("Informe o valor do número: \n"))

# if (numero % 3 == 0) and (numero % 5 == 0):
#     print("FizzBuzz")
# elif (numero % 5 == 0):
#     print("Buzz")
# elif (numero % 3 == 0):
#     print("Fizz")
# else:
#     print("O número não é múltiplo de 3 nem de 5!")

#Questão 02 Condicionais if/else/elif

# a = float(input("Informe o valor do operando A: \n"))
# b = float(input("Informe o valor do operando B : \n"))
# op = input("Qual operação você deseja fazer? (+),(-),(*),(/)\n")
# valor = 0
# if (op == "+"):
#     print("A soma é:",a+b)
# elif (op == "-"):
#     print("A subtração é:",a-b) 
# elif (op == "*"):
#     print("A multiplicação é:",a*b) 
# elif (op == "/") and (b == 0):
#     print("Não é possível realizar divisão por zero!")
# elif (op == "/"):
#     print("A divisão é:",a/b)
# else:
#     print("Valor de entrada indefinido!")

#Questão 03 Condicionais if/else/elif 

# usuario = "admin" 
# senha = "123123"  

# nome_usuario = input("Informe o nome do usuário: \n")
# senha_usuario = input("Informe a senha do usuário: \n")

# if (nome_usuario == usuario) and (senha_usuario == senha):
#     print("Autenticação foi bem-sucedida!")
# elif (nome_usuario != usuario) and (senha_usuario == senha):
#     print("Nome do usuário não existe!")
# elif (nome_usuario == usuario)  and (senha_usuario != senha) :
#     print("A senha está incorreta!")
# else:
#     print("Tanto o usuário quanto a senha estão incorretos!")

#Questão 01 Repetição(while)

# num = int(input("Informe um número inteiro: \n"))
# total = 0;
# i = 0;
# while True:
#     i = i + 1;
#     total = total + i;
#     if (i == num) :
#         break  
# print("A soma de todos os números é de: ",total)

#Questão 02 Repetição(while)

# num = int(input("Informe um número: \n"))
# i = 0;
# while num != i:
#     i = i +1;
#     if (i % 2 == 0):
#         print(i)

#Questão 03 Repetição(while)

# num = int(input("Informe um número: \n"))
# i = 1;
# total = 0
# while i<=num:
#     if num % i == 0:
#         total = total + 1
#     i = i + 1   
# if total == 2:
#     print("Esse número é primo!")
# else:
#     if total > 2:
#         print("Esse número não é primo!")

#Questão 04 Repetição(while) 

# num = 15
# i = 1

# while i <= 3:
#     teste = int(input("Tente descobrir o número: \n"))

#     if num == teste:
#         print("Parabéns, você acertou!")
#         break
#     elif teste > num:
#         print("O número que você informou é maior que o disposto!")
#     elif teste < num:
#         print("O número que você informou é menor que o disposto!")
#     i = i+1
# if i > 3:
#     print("Número de tentativas excedidas, você perdeu!")


