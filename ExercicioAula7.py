# Exercicios

# 1. Construa um programa no qual o usuário informe o nome, a estatura e o peso de vários alunos
# de uma turma. Após o cadastro, o programa deve imprimir o nome e o IMC de cada aluno ordenados
# pelo nome do aluno. Sabe-se que IMC = peso/altura**2
# print("Calculando o IMC dos alunos")

# turma = []

# opcao = "s"

# while opcao == "s":
#     aluno_nome = input("Insira o nome do aluno: ")
#     aluno_altura = float(input("Insira a altura do aluno: "))
#     aluno_peso = float(input("Insira o peso do aluno: "))
#     aluno_imc = (aluno_peso / aluno_altura ** 2) 
#     aluno_imc *= 10000
#     aluno_imc = "{:.2f}".format(aluno_imc)
#     turma.append({"nome": aluno_nome, "altura": aluno_altura, "peso": aluno_peso, "imc": aluno_imc})
#     opcao = input("Deseja adicionar mais um aluno? Digite [s] ou [n]: ")
    

# alunos_ordenados = sorted(turma, key=lambda x: x["nome"])

# for aluno in alunos_ordenados:
#     nome = aluno["nome"]
#     peso = aluno["peso"]
#     altura = aluno["altura"]
#     imc = aluno["imc"]

# print(f"Nome: {nome} | IMC: {imc}")


# 2. Faça um script que receba os valores do nome, idade e e-mail de uma pessoa
# e guarde-os em um dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. 
# Exiba as informações desse dicionário
# nome = input("Informe seu nome: ")
# idade = int(input("Informe sua idade: "))
# email = input("Informe o seu email: ")

# dicionario = {
#     "nome" : [],
#     "idade": [],
#     "email": []
# }

# dicionario['nome'].append(nome)
# dicionario['idade'].append(idade)
# dicionario['email'].append(email)

# print(dicionario)

# 3. Faça um programa que leia 10 números do usuário e os coloque corretamente no dicionário D abaixo.
# D = {'pares': [], 'impares':[]}
# x = 0
# dicionario = {
#     'pares': [], 
#     'impares':[]
# }

# while x <= 10:
#     numero = int(input("Digite um número: "))
#     if numero % 2 == 0:
#         dicionario['pares'].append(numero)
#     else :
#         dicionario['impares'].append(numero)
#     x = x + 1

# print(dicionario)


# 4. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos 
# de mercado e seus respectivos preços e os mostre na tela.
# x = 0
# dicionario = {
#     'nome': [],
#     'preco': []
# }

# while x < 3:
#     produto_nome = input("Digite o nome do produto: ")
#     dicionario['nome'].append(produto_nome)
#     produto_preco = float(input("Digite o preço: "))
#     dicionario['preco'].append(produto_preco)
#     x = x + 1

# print("Produtos e preços inseridos:")
# for i in range(len(dicionario['nome'])):
#     nome = dicionario['nome'][i]
#     preco = dicionario['preco'][i]
#     print(f"Produto: {nome} | Preço: R${preco:.2f}")

# 5. Escreva um programa que conta a quantidade de vogais em um 
# texto e armazena tal quantidade em um dicionário, onde a 
# chave é a vogal considerada.
# texto = input("Digite um texto: ")

# vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# for letra in texto:
#     if letra.lower() in vogais:
#         vogais[letra.lower()] += 1

# print("Quantidade de vogais:")
# for vogal, quantidade in vogais.items():
#     print(f"{vogal}: {quantidade}")



# 6. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo
#  como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).
# semana = {
#     'segunda': ['Python'],
#     'terca': ['Métodos ágeis'],
#     'quarta': ['Python'],
#     'quinta': ['Python'],
#     'sexta': [],
#     'sabado': [],
#     'domingo': []
# }

# print(semana)
