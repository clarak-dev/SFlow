import json
import os

ARQUIVO_SERVICOS = 'servicos.json'

def carregar_servicos():
    """Carrega a lista de serviços a partir de um arquivo JSON."""
    if os.path.exists(ARQUIVO_SERVICOS):
        with open(ARQUIVO_SERVICOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []

def salvar_servicos(servicos):
    """Salva a lista de serviços em um arquivo JSON."""
    with open(ARQUIVO_SERVICOS, 'w', encoding='utf-8') as f:
        json.dump(servicos, f, indent=4, ensure_ascii=False)

def cadastrar_servico():
    """Solicita dados do serviço e os salva no arquivo."""
    servicos = carregar_servicos()
    nome = input("Digite o nome do serviço: ")
    preco = input("Digite o preço do serviço: ")

    servico = {"nome": nome, "preco": preco}
    servicos.append(servico)

    salvar_servicos(servicos)
    print(f"✅ Serviço {nome} cadastrado com sucesso!")

def listar_servicos():
    """Lista todos os serviços cadastrados."""
    servicos = carregar_servicos()
    if not servicos:
        print("⚠️ Nenhum serviço cadastrado.")
    else:
        print("\n📋 Lista de serviços:")
        for i, servico in enumerate(servicos, start=1):
            print(f"{i}. {servico['nome']} - R$ {servico['preco']}")

