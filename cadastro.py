import json

# Carregar clientes do arquivo
try:
    with open("clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)
except:
    clientes = []


def salvar():
    with open("clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)


def menu():
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Editar cliente")
    print("5 - Excluir cliente")
    print("6 - Sair")


while True:
    menu()
    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")

        cliente = {
            "nome": nome,
            "idade": idade,
            "email": email,
            "telefone": telefone
        }

        clientes.append(cliente)
        salvar()

        print("\nCliente cadastrado com sucesso!")


    elif opcao == "2":
        if len(clientes) == 0:
            print("\nNenhum cliente cadastrado.")

        else:
            print("\n===== CLIENTES CADASTRADOS =====")

            for cliente in clientes:
                print(f"Nome: {cliente['nome']}")
                print(f"Idade: {cliente['idade']}")
                print(f"E-mail: {cliente['email']}")
                print(f"Telefone: {cliente['telefone']}")
                print("-" * 30)


    elif opcao == "3":
        nome_busca = input("Digite o nome do cliente: ")

        encontrado = False

        for cliente in clientes:
            if cliente["nome"].lower() == nome_busca.lower():

                print("\nCliente encontrado!")
                print(cliente)

                encontrado = True
                break

        if not encontrado:
            print("Cliente não encontrado.")


    elif opcao == "4":
        nome_busca = input("Digite o nome do cliente que deseja editar: ")

        encontrado = False

        for cliente in clientes:
            if cliente["nome"].lower() == nome_busca.lower():

                cliente["nome"] = input("Novo nome: ")
                cliente["idade"] = input("Nova idade: ")
                cliente["email"] = input("Novo email: ")
                cliente["telefone"] = input("Novo telefone: ")

                salvar()

                print("\nCliente atualizado com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("Cliente não encontrado.")


    elif opcao == "5":
        nome_busca = input("Digite o nome que deseja excluir: ")

        encontrado = False

        for cliente in clientes:
            if cliente["nome"].lower() == nome_busca.lower():

                clientes.remove(cliente)
                salvar()

                print("\nCliente excluído com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("Cliente não encontrado.")


    elif opcao == "6":
        print("Programa encerrado!")
        break


    else:
        print("Opção inválida!")
