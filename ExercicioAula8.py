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
# def verificar_perfeito(numero):
#     soma_divisores = 0

#     for i in range(1, numero):
#         if numero % i == 0:
#             soma_divisores += i

#     if soma_divisores == numero:
#         return True
#     else:
#         return False

# num = int(input("Digite um número: "))

# if verificar_perfeito(num):
#     print(f"O número {num} é perfeito.")
# else:
#     print(f"O número {num} não é perfeito.")



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

# def criar_dicionario_funcionarios():
#     funcionarios = {
#         1: {
#             "Matricula": 1,
#             "Nome": "Ana",
#             "Sexo": "F",
#             "Departamento": "TI",
#             "TempoServiço": 7,
#             "Salario": 3200
#         },
#         2: {
#             "Matricula": 2,
#             "Nome": "Beatriz",
#             "Sexo": "F",
#             "Departamento": "TI",
#             "TempoServiço": 4,
#             "Salario": 3720
#         },
#         3: {
#             "Matricula": 3,
#             "Nome": "Carla",
#             "Sexo": "F",
#             "Departamento": "TI",
#             "TempoServiço": 1,
#             "Salario": 2100
#         },
#         4: {
#             "Matricula": 4,
#             "Nome": "Daniela",
#             "Sexo": "F",
#             "Departamento": "RH",
#             "TempoServiço": 2,
#             "Salario": 3920
#         },
#         5: {
#             "Matricula": 5,
#             "Nome": "Emílio",
#             "Sexo": "M",
#             "Departamento": "RH",
#             "TempoServiço": 7,
#             "Salario": 4235
#         },
#         6: {
#             "Matricula": 6,
#             "Nome": "Fernando",
#             "Sexo": "M",
#             "Departamento": "RP",
#             "TempoServiço": 7,
#             "Salario": 1200
#         },
#         7: {
#             "Matricula": 7,
#             "Nome": "Gabriela",
#             "Sexo": "F",
#             "Departamento": "RP",
#             "TempoServiço": 8,
#             "Salario": 7234.89
#         },
#         8: {
#             "Matricula": 8,
#             "Nome": "Hernandes",
#             "Sexo": "M",
#             "Departamento": "TI",
#             "TempoServiço": 6,
#             "Salario": 4234.12
#         }
#     }
#     return funcionarios

# # Teste da função
# dados_funcionarios = criar_dicionario_funcionarios()
# print(dados_funcionarios)


# 6. Com base no dicionário obtido na questão anterior, faça:
# a) Uma função que retorne o número de homens e mulheres cadastrados;
# def contar_generos(funcionarios):
#     num_homens = 0
#     num_mulheres = 0

#     for funcionario in funcionarios.values():
#         if funcionario["Sexo"] == "M":
#             num_homens += 1
#         elif funcionario["Sexo"] == "F":
#             num_mulheres += 1

#     return num_homens, num_mulheres

# # Teste da função
# dados_funcionarios = criar_dicionario_funcionarios()
# homens, mulheres = contar_generos(dados_funcionarios)
# print(f"Número de homens: {homens}")
# print(f"Número de mulheres: {mulheres}")

# # b) Uma função que retorne um dicionário dos funcionários cujo tempo de serviço seja maior que 5 anos.
# def funcionarios_tempo_servico_maior_5(funcionarios):
#     funcionarios_maior_5_anos = {}

#     for funcionario in funcionarios.values():
#         if funcionario["TempoServiço"] > 5:
#             funcionarios_maior_5_anos[funcionario["Matricula"]] = funcionario

#     return funcionarios_maior_5_anos

# # Teste da função
# dados_funcionarios = criar_dicionario_funcionarios()
# funcionarios_maior_5_anos = funcionarios_tempo_servico_maior_5(dados_funcionarios)
# print(funcionarios_maior_5_anos)

# # c) Uma função que receba como argumento o sexo e retorne a média salarial dos funcionários daquele sexo.
# def media_salarial_por_sexo(funcionarios, sexo):
#     soma_salarios = 0
#     num_funcionarios = 0

#     for funcionario in funcionarios.values():
#         if funcionario["Sexo"] == sexo:
#             soma_salarios += funcionario["Salario"]
#             num_funcionarios += 1

#     if num_funcionarios == 0:
#         return 0
#     else:
#         media_salarial = soma_salarios / num_funcionarios
#         return media_salarial

# # Teste da função
# dados_funcionarios = criar_dicionario_funcionarios()
# sexo_desejado = "F"  # Pode ser "M" ou "F"
# media_salarial = media_salarial_por_sexo(dados_funcionarios, sexo_desejado)
# print(f"Média salarial dos funcionários do sexo {sexo_desejado}: R${media_salarial:.2f}")
