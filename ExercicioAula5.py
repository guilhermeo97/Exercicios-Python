# # 1. Adicione os números de 1 a 10 à lista "minha_lista" utilizando um loop, em seguida imprima esses valores na tela e por fim
# # mostre o tamanho dessa lista.
# minha_lista = []

# for num in range(1, 11):
#     minha_lista.append(num)

# print("Valores da lista:")
# for valor in minha_lista:
#     print(valor)

# tamanho_lista = len(minha_lista)
# print("\nTamanho da lista:", tamanho_lista)



# # 2. Crie uma lista com os números pares de 0 a 20 e em seguida atenda os seguintes comandos:
# # a) Inverta a ordem dos elementos da lista.
# # b) Inverta a ordem dos elementos da lista.
# # c) Remova os números múltimos de 5 da lista.

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# lista.sort(reverse=True)
# for item in lista:
#     if(item % 5 == 0):
#         lista.remove(item)
# print(lista)

# # 3. Crie uma lista chamada "lista_concatenada" que seja a concatenação das listas criadas na questão 1 e na questão 2.

# lista_concatenada = minha_lista + lista
# # 4. Remova todos os elementos da lista "lista_concatenada".

# lista_concatenada.clear()

# # 5. Crie uma lista chamada "lista_repetida" com 5 repetições da lista "lista_concatenada".
# lista_concatenada = [1, 2, 3, 4, 5, 6]

# lista_repetida = lista_concatenada * 5

# print(lista_repetida)


# # 6. Copie a lista "lista_concatenada" para uma nova lista chamada "copia_lista_concatenada" sem utilizar o operador de atribuição direta.
# copia_lista_concatenada = lista_concatenada.copy()

# print(copia_lista_concatenada)

# # 7. Faça um programa que leia nome e idade de 5 pessoas e coloque os nomes em uma lista e as idades em outra. 
# # Apresente as duas listas preenchidas.
# nomes = []
# idades = []

# for i in range(5):
#     nome = input("Digite o nome da pessoa: ")
#     idade = int(input("Digite a idade da pessoa: "))

#     nomes.append(nome)
#     idades.append(idade)


# # 8.Faça um script que leia números do usuário, enquanto ele não digitar 0. 
# # Armazene esses números em uma lista e ao final informe quantos números foram digitados, ignorando o 0, 
# # o valor máximo e o valor mínimo.
# numeros = []

# while True:
#     numero = int(input("Digite um número (digite 0 para encerrar): "))

#     if numero == 0:
#         break

#     numeros.append(numero)

# if len(numeros) > 0:
#     quantidade_numeros = len(numeros)
#     valor_maximo = max(numeros)
#     valor_minimo = min(numeros)

#     print("Quantidade de números digitados:", quantidade_numeros)
#     print("Valor máximo:", valor_maximo)
#     print("Valor mínimo:", valor_minimo)
# else:
#     print("Nenhum número foi digitado.")



# # 9.Faça um script que informe o fatorial de um número.
# # Utilize obrigatoriamente o comando for
# numero = int(input("Digite um número: "))

# fatorial = 1

# for i in range(1, numero + 1):
#     fatorial *= i

# print("O fatorial de", numero, "é:", fatorial)

# 10.Informe, de forma decrescente todos os pares entre N (número fornecido pelo usuário) e -N.
# Se N for par, ele também deve ser incluído no output (vide exemplo para N = 2)
# N = int(input("Digite um número: "))

# if N % 2 == 0:
#     numeros_pares = list(range(N, -N-1, -2))
# else:
#     numeros_pares = list(range(N-1, -N-1, -2))

# for num in numeros_pares:
#     print(num)



# 11. Faça um script que peça ao usuário para digitar um número n e some todos os números de 1 a n.
# n = int(input("Digite um número: "))

# soma = 0

# for i in range(1, n + 1):
#     soma += i

# print("A soma de todos os números de 1 a", n, "é:", soma)

# 12. Faça um programa que recebe um número inteiro do usuário e imprime na tela a quantidade 
# de divisores desse número e quais são eles.
# numero = int(input("Digite um número inteiro: "))

# divisores = []

# for i in range(1, numero + 1):
#     if numero % i == 0:
#         divisores.append(i)

# quantidade_divisores = len(divisores)

# print("Quantidade de divisores:", quantidade_divisores)
# print("Divisores:", divisores)
