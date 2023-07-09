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

# 4. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos 
# de mercado e seus respectivos preços e os mostre na tela.

# 5. Escreva um programa que conta a quantidade de vogais em um 
# texto e armazena tal quantidade em um dicionário, onde a 
# chave é a vogal considerada.

# 6. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo
#  como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).