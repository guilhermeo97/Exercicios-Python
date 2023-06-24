# Lista 2
# 1. Faça um programa que escreva a contagem regressiva do lançamento de um foguete. O programa deve imprimir na tela a sequência regressiva de 10 até 0 e 'Fogo!'.
# x = 10
# while (x != -1):
#     print(x)
#     x = x - 1
# print("fogo")


# 2. Escreva um programa em que o usuário informará qual o último número a imprimir. E esse programa deverá mostrar apenas os números ímpares entre 1 e o número definido pelo usuário.
# x = float(input("Digite um número: "))
# y = 0

# while(y <= x):
#     if(y%3 == 0):
#         print(y)
#     y += 1

# 3. Imagine o sistema de um caixa eletrônico. Construa um programa que receba um senha e 
# que essa senha tenha que ser validada. Considere que a senha é **123456**. Existem as seguintes restrições:
# - Ao acertar a senha, a mensagem a ser exibida é: "Olá! Seja bem-vindo ao banco!"
# - Quando o usuário errar a senha pela primeira vez, mostrar a mensagem: "Senha incorreta! Você ainda tem 2 tentativas."
# - Se o usuário errar a senha pela segunda vez, mostrar: "Senha incorreta! Você ainda tem 1 tentativa."
# - Se o usuário errar a senha novamente, mostrar a mensagem "Sua senha foi bloquada! Por favor, dirija-se a agência".
# senha_digitada = input('Digite sua senha para acessar o banco:')
# senha_correta = '123456'
# tentativas = 3
# while tentativas != 0:
#     if (senha_digitada != senha_correta) and (tentativas == 3):
#         print('Senha incorreta! Você ainda tem 2 tentativas.')
#         tentativas -=1
#         senha_digitada = input('Digite sua senha:')
#     elif (senha_digitada != senha_correta) and (tentativas == 2):
#         print('Senha incorreta! Você ainda tem 1 tentativas.')
#         tentativas -=1
#         senha_digitada = input('Digite sua senha:')
#     elif (senha_digitada != senha_correta) and (tentativas == 1):
#         print('Sua senha foi bloqueada! Por favor, dirija-se a agência!')
#         tentativas = 0
#     else:
#         print('Olá, bem-vindo ao banco!')
#         tentativas = 0




# 4. Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. 
# Exiba os valores Mês a mês para os 24 primeiros meses. Imprima o total ganho com o juros no período.
# Obs.: A fórmula de cálculo de juros compostos e que se aplica ao caso da questão é:
# M = C*(1+i/100)*t
# No qual C é o valor inicial; i é a taxa de juros e t é o tempo em acordo com a taxa.
# deposito_inicial = float(input("Digite o valor do depósito inicial: "))
# taxa_juros = float(input("Digite a taxa de juros em porcentagem: "))

# total_ganho = 0
# saldo = deposito_inicial
# mes = 1

# while mes <= 24:
#     saldo = saldo * (1 + taxa_juros/100)
#     total_ganho += saldo - deposito_inicial
#     print(f"Mês {mes}: R$ {saldo:.2f}")
#     mes += 1

# print(f"\nTotal ganho com juros no período: R$ {total_ganho:.2f}")

# 5. Escreva um programa que pergunte o valor inicial de uma dívida, o juro mensal. 
# Pergunte também o valor mensal que será pago. 
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
# valor_divida = float(input("Digite o valor da divida inicial: "))
# taxa_juros = float(input("Digite a taxa de juros em decimal: "))
# valor_mensal = float(input("Digite o valor mensal que será pago: "))

# total_pago = 0
# total_juros = 0
# mes = 1

# while valor_divida > 0:
#     juros = valor_divida * (taxa_juros / 100)
#     valor_divida += juros
#     valor_divida -= valor_mensal
#     total_pago += valor_mensal
#     total_juros += juros
#     mes += 1

# print(f"\nNúmero de meses para pagar a dívida: {mes}")
# print(f"Total pago: R$ {total_pago:.2f}")
# print(f"Total de juros pago: R$ {total_juros:.2f}")