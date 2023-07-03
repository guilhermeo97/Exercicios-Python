# Exercicios

# 1.Faça um programa que pede para o usuário digitar uma palavra e imprima cada letra em uma linha.
# palavra = input("Digite uma palavra ")

# lista = list(palavra)
# for item in lista:
#     print(item)

# 2.Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, 
# porém com espaço entre cada letra, depois imprima a nova string: Exemplo: se o usuário digitar "python" 
# o programa deve imprimir "p y t h o n "
# palavra = input("Digite uma palavra ")
# palavra_tratada = " ".join(palavra)
# print(palavra_tratada)

# 3.Faça um programa que receba uma string e retorne uma nova string substituindo: 'a' por '4' 'e' por '3' 'I' por '1' 't' por '7'
# def substituir_caracteres(string):
#     string = string.replace('a', '4')
#     string = string.replace('e', '3')
#     string = string.replace('I', '1')
#     string = string.replace('t', '7')
#     return string

# palavra = input("Digite uma string: ")
# nova_string = substituir_caracteres(palavra)
# print("Nova string:", nova_string)


# 4.Faça um programa que recebe uma string e retorna ela ao contrário. Exemplo: Recebe "teste" e retorna "etset".
# palavra = input("Digite uma string: ")
# palavra_lista = list(palavra)
# palavra_lista = palavra_lista[::-1]
# palavra = "".join(palavra_lista)
# print(palavra)

# 5. Escreva um programa que lê duas strings e gere uma terceira na qual os caracteres da segunda foram retirados da primeira.
# def remover_caracteres(string1, string2):
#     for char in string2:
#         string1 = string1.replace(char, '')
#     return string1

# string1 = input("Digite a primeira string: ")
# string2 = input("Digite a segunda string: ")

# nova_string = remover_caracteres(string1, string2)

# print("Nova string:", nova_string)


# 6. Escreva um programa que receba um texto e uma palavra, então verifique se a palavra está no texto.
# texto = input("Digite uma string: ")
# palavra = input("Digite uma string: ")
# palavra_contem = texto.find(palavra)

# if palavra_contem >= 0:
#     print("Palavra está na string")
# else:
#     print("Palavra não está na string")
