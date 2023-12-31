def cadastrar_fornecedor(cadastro_fornecedores):
    codigo_fornecedor = str(len(cadastro_fornecedores) + 1)
    
    nome_fornecedor = None
    while not nome_fornecedor:
        nome_fornecedor = input("Digite o nome do fornecedor: ")
        if nome_fornecedor == None:    
            print("Nome não preenchido. Digite o nome do fornecedor.")
    
    telefone_fornecedor = None
<<<<<<< HEAD
    qtd_numero_telefone = 8
    while not telefone_fornecedor or len(telefone_fornecedor) >= qtd_numero_telefone or not telefone_fornecedor.isdigit():
        telefone_fornecedor = input("Digite o telefone do fornecedor (no mínimo", qtd_numero_telefone, "dígitos): ")
=======
    qtd_numero_telefone = 11
    while not telefone_fornecedor or len(telefone_fornecedor) != qtd_numero_telefone or not telefone_fornecedor.isdigit():
<<<<<<< HEAD
        telefone_fornecedor = input("Digite o telefone do fornecedor (11 dígitos): ")
        
=======
        telefone_fornecedor = input("Digite o telefone do fornecedor (até, qtd_numero_telefone, dígitos): ")
>>>>>>> 80643b7c2b0d65619d848f8a12626e4bb33dd901
>>>>>>> b9b791a4f6ec1e828616c31296e057da536404a6
        if len(telefone_fornecedor) != qtd_numero_telefone or not telefone_fornecedor.isdigit():
            print("Telefone inválido. Digite no mínimo", qtd_numero_telefone, "números.")
    
    email_fornecedor = None
    while not email_fornecedor or "@" not in email_fornecedor or "." not in email_fornecedor:
        email_fornecedor = input("Digite o e-mail do fornecedor: ")
        if "@" not in email_fornecedor or "." not in email_fornecedor:
            print("E-mail inválido. O e-mail deve conter o símbolo '@' e pelo menos um ponto '.'.")

    fornecedor = {
        'nome': nome_fornecedor,
        'telefone': telefone_fornecedor,
        'email': email_fornecedor
    }

    cadastro_fornecedores[codigo_fornecedor] = fornecedor
    print("Fornecedor cadastrado com sucesso!")

def exibir_fornecedor(cadastro_fornecedores):
    codigo_pesquisado = input("Digite o código do fornecedor a ser pesquisado: ")
    fornecedor = cadastro_fornecedores.get(codigo_pesquisado)

    if fornecedor:
        print(f"Código do fornecedor: {codigo_pesquisado}")
        print(f"Nome: {fornecedor['nome']}")
        print(f"Telefone: {fornecedor['telefone']}")
        print(f"E-mail: {fornecedor['email']}")
    else:
        print("Fornecedor não encontrado.")

def remover_fornecedor(cadastro_fornecedores):
    if not cadastro_fornecedores:
        print("Não existem fornecedores cadastrados.")
        return

    codigo_remover = input("Digite o código do fornecedor a ser removido: ")
    fornecedor = cadastro_fornecedores.pop(codigo_remover, None)

    if fornecedor:
        print("Fornecedor removido com sucesso!")
    else:
        print("Fornecedor não encontrado.")

def logar():
    print(""""\n---- Sistema de Cadastro de Fornecedores ----"
          Olá! Seja bem-vindo!")
    Para continar informe usuário e senha
    
    """)

    tentativa = 0
    usuario = input("Informe o usuário: ")
    senha = input("Informe a senha: ")
    while tentativa < 2:
        if usuario == "comprador" and senha == "12345":
            print("Você está logado!")
            tentativa = 1
        else:
            print("Senha ou usuário incorretos. Você ainda tem", 2 - tentativa, "tentativa(s)")
            usuario = input("Digite o usuário: ")
            senha = input("Digite a senha: ")
            
        tentativa = tentativa + 1

def menu():
    cadastro_fornecedores = {}
    while True:
        print("""---- Menu de opções ----
        1 - Cadastrar Fornecedor
        2 - Exibir Fornecedor
        3 - Remover Fornecedor
        4 - Sair""")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar_fornecedor(cadastro_fornecedores)
        elif opcao == "2":
            exibir_fornecedor(cadastro_fornecedores)
        elif opcao == "3":
            remover_fornecedor(cadastro_fornecedores)
        elif opcao == "4":
            print("Saindo do sistema de cadastro...")
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    if logar():
        menu()
