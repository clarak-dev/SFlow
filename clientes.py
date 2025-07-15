# sflow/clientes.py

clientes = []  # Lista para armazenar os clientes


def cadastrar_cliente():
    """
    Solicita ao usuário o nome e telefone e cadastra um novo cliente.
    """
    print("\n--- Cadastrar Cliente ---")
    nome = input("Nome do cliente: ")
    telefone = input("Telefone do cliente: ")

    cliente = {"nome": nome, "telefone": telefone}
    clientes.append(cliente)
    print(f"✅ Cliente '{nome}' cadastrado com sucesso!")


def listar_clientes():
    """
    Lista todos os clientes cadastrados.
    """
    print("\n--- Lista de Clientes ---")
    if not clientes:
        print("⚠️ Nenhum cliente cadastrado.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. {cliente['nome']} - Telefone: {cliente['telefone']}")
