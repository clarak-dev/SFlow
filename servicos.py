# sflow/servicos.py

servicos = []  # Lista para armazenar os serviços


def cadastrar_servico():
    """
    Solicita ao usuário o nome e valor e cadastra um novo serviço.
    """
    print("\n--- Cadastrar Serviço ---")
    nome = input("Nome do serviço: ")
    valor = float(input("Valor do serviço (R$): "))

    servico = {"nome": nome, "valor": valor}
    servicos.append(servico)
    print(f"✅ Serviço '{nome}' cadastrado com sucesso!")


def listar_servicos():
    """
    Lista todos os serviços cadastrados.
    """
    print("\n--- Lista de Serviços ---")
    if not servicos:
        print("⚠️ Nenhum serviço cadastrado.")
    else:
        for i, servico in enumerate(servicos, start=1):
            print(f"{i}. {servico['nome']} - R${servico['valor']:.2f}")
