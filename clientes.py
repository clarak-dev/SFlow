import json
import os

ARQUIVO_CLIENTES = 'clientes.json'

def carregar_clientes():
    """Carrega a lista de clientes a partir de um arquivo JSON."""
    if os.path.exists(ARQUIVO_CLIENTES):
        with open(ARQUIVO_CLIENTES, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []

def salvar_clientes(clientes):
    """Salva a lista de clientes em um arquivo JSON."""
    with open(ARQUIVO_CLIENTES, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

def cadastrar_cliente():
    """Solicita dados do cliente e os salva no arquivo."""
    clientes = carregar_clientes()
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    cliente = {"nome": nome, "telefone": telefone}
    clientes.append(cliente)

    salvar_clientes(clientes)
    print(f"✅ Cliente {nome} cadastrado com sucesso!")

def listar_clientes():
    """Lista todos os clientes cadastrados."""
    clientes = carregar_clientes()
    if not clientes:
        print("⚠️ Nenhum cliente cadastrado.")
    else:
        print("\n📋 Lista de clientes:")
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. {cliente['nome']} - {cliente['telefone']}")

