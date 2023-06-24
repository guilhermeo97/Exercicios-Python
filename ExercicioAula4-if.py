# Lista 1 - Aula 4
# 1. Desenvolva um programa que leia dois números e informe o maior deles.
# n1 = float(input("Informe o primeiro número: "))
# n2 = float(input("Informe o primeiro número: "))

# if(n1 == n2):
#     print("valores são iguais")
# elif(n1 > n2):
#     print(n1, "é maior que", n2)
# else:
#     print(n2, "é maior que", n1)


# 2. Faça um código que leia um número informado pelo usuário e que ao final informe se o número é par ou ímpar.
# numero = float(input("Informe um número: "))

# if(numero%2 == 0):
#     print(numero, "é um número par")
# else:
#     print(numero, "é um número impar")

# 3. Partindo da solução da questão anterior. Crie um programa que calcule o quadrado de um número quando ele for par e que calcule o cubo do número caso ele seja ímpar.
# numero = float(input("Informe um número: "))

# if(numero%2 == 0):
#     quadrado = numero ** 2
#     print(numero, "é um número par, e o quadrado", quadrado)

# else:
#     cubo = numero ** 3
#     print(numero, "é um número impar, e o cubo é", cubo)

# 4. Faça um programa que receba 3 notas de prova de um aluno, calcule a média e diga se ele foi aprovado ou reprovado. A média para aprovação é de pelo menos 6 (aprovado se média maior ou igual a 6).
# prova1 = float(input("Informe a nota da prova 1: "))
# prova2 = float(input("Informe a nota da prova 2: "))
# prova3 = float(input("Informe a nota da prova 3: "))

# media = (prova1 + prova2 + prova3) / 3

# print("A nota é", media)


# 5. Escreva um program que leia dois números e que pergunte qual operação o usuário deseja realizar. 
# Esse programa deve aceitar como respostas a soma(+), a subtração(-), a multiplicação (*) e a divisão (/). 
# Ao final, o programa deve exibir o resultado da operação escolhida.
# num1 = float(input('Insira o primeiro número: '))
# num2 = float(input('Insira o segundo número: '))
# op = input('Insira o sinal da operação desejada: ')
# if (op == '+'):
#     soma = num1 + num2
#     print(soma)
# elif (op == '-'):
#     subt = num1 - num2
#     print(subt)
# elif (op == '*'):
#     mult = num1*num2
#     print(mult)
# elif (op == '/'):
#     div = num1/num2
#     print(div)

# 6. Escreva um programa que pergunte a distância que determinado passageiro deseja percorrer em km. A partir disso calcule o preço da passagem. É cobrado 0,50 centavos por km para viagens de até 300 km. E 0,45 centavos para viagens mais longas.
# km_percorrido = float(input("Informe a quantidade de KM percorridos"))
# if km_percorrido <= 0:
#     print("Informe um valor maior que 0")
# elif km_percorrido <= 300:
#     valor = km_percorrido * 0.5
#     print("Valor a ser pago R$", valor)
# else:
#     valor = km_percorrido * 0.45
#     print("Valor a ser pago R$", valor)

# 7. Suponha que determinado usuário possua 2 logins em uma rede corporativa.
# Login 1
# usuario: jardim
# senha: flores1206
# Login 2
# usuario: cordeiro
# senha la1506
# Escreva um programa que valide o acesso do usuário na rede. Caso o par usuário e senha estejam corretos, o programa deve imprimir a mensagem: "Seja bem vindo!". Caso contrário, "Usuário e senha não conferem".
# usuario = input("Informe seu usuário: ")
# senha = input("Informe seu usuário: ")

# if(usuario == "jardim" and senha == "flores1206") or (usuario == "cordeiro" and senha == "la1506"):
#     print("Seja bem vindo!")
# else:
#     print("Usuário e senha não conferem")


# 8. Uma empresa concederá aumento de salário aos seus funcionários de acordo com o cargo.
# Cargo - Aumento(%)
# Gerente Geral - 30
# Gerente de Relacionamento - 30
# Analista - 25
# Assistente de Atendimento - 20
# Crie um programa que solicite o salário e o cargo do funcionário. 
#O programa deve calcular e imprimir o novo salário. Caso o cargo informado não esteja na tabela, 
#o programa deve imprimir "Cargo inválido".
# print("Olá, informe um dos cargos abaixo")
# print()
# print("Gerente Geral")
# print("Gerente de Relacionamento")
# print("Analista")
# print("Assistente de Atendimento")
# print()

# cargo = input("Informe o seu cargo: ")
# salario = float(input("Agora informe o salário: "))

# if cargo == "Assistente de Atendimento":
#     novo_salario = salario * 1.2
#     print("O novo salário é R$", novo_salario)
# elif cargo == "Analista":
#     novo_salario = salario * 1.25
#     print("O novo salário é R$", novo_salario)
# elif cargo == "Gerente Geral" or cargo == "Gerente de Relacionamento":
#     novo_salario = salario * 1.3
#     print("O novo salário é R$", novo_salario)
# else:
#     print("Cargo inválido")