# Exercicios

# 1. Escreva uma função que retorne o maior número entre dois números.
# numero1 = float(input("Digite um número: "))
# numero2 = float(input("Digite outro número: "))

# def avaliar_numero(numero1, numero2):
#     if numero1 > numero2:
#         print("O maior número é", numero1)
#     elif numero2 > numero1:
#         print("O maior número é", numero2)
#     else:
#         print("Os número são iguais")

# avaliar_numero(numero1, numero2)

# 2. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
# numero = int(input("Digite um número: "))

# def inverter_numero(numero):
#     numero_invertido = int(str(numero)[::-1])
#     return numero_invertido

# print(inverter_numero(numero))


# 3. Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor x inteiro como parâmetro e imprima 
# uma linha com 1 até x. 
# Se x = 1 na função, imprime:
# 1
# Se x = 2 na função, imprime:
# 1   2
# E assim por diante.
# def imprimir_linhas(numero):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# n = int(input("Digite um número: "))

# for i in range(1, n + 1):
#     imprimir_linhas(i)

# 4. Faça uma função que verifique se um valor é perfeito ou não.
# Um valor é dito perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio.
# (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor booleano.



# 5.  Crie uma função e dê o nome pertinente para a mesma, essa função deve retornar um dicionário
# com os dados abaixo:
# Matricula - Nome      - Sexo - Departamento - TempoServiço - Salario
#     1     - Ana       -  F   -     TI       -      7       - 3200
#     2     - Beatriz   -  F   -     TI       -      4       - 3720
#     3     - Carla     -  F   -     TI       -      1       - 2100
#     4     - Daniela   -  F   -     RH       -      2       - 3920
#     5     - Emílio    -  M   -     RH       -      7       - 4235
#     6     - Fernando  -  M   -     RP       -      7       - 1200
#     7     - Gabriela  -  F   -     RP       -      8       - 7234.89
#     8     - Hernandes -  M   -     TI       -      6       - 4234.12

# 6. Com base no dicionário obtido na questão anterior, faça:
# a) Uma função que retorne o número de homens e mulheres cadastrados;
# b) Uma função que retorne um dicionário dos funcionários cujo tempo de serviço seja maior que 5 anos.
# c) Uma função que receba como argumento o sexo e retorne a média salarial dos funcionários daquele sexo.