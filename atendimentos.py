import json
import os
import clientes
import servicos

ARQUIVO_ATENDIMENTOS = 'atendimentos.json'

def carregar_atendimentos():
    """Carrega a lista de atendimentos a partir de um arquivo JSON."""
    if os.path.exists(ARQUIVO_ATENDIMENTOS):
        with open(ARQUIVO_ATENDIMENTOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []

def salvar_atendimentos(atendimentos):
    """Salva a lista de atendimentos em um arquivo JSON."""
    with open(ARQUIVO_ATENDIMENTOS, 'w', encoding='utf-8') as f:
        json.dump(atendimentos, f, indent=4, ensure_ascii=False)

def marcar_atendimento():
    """Marca um atendimento associando cliente e serviço."""
    atendimentos = carregar_atendimentos()
    clientes_lista = clientes.carregar_clientes()
    servicos_lista = servicos.carregar_servicos()

    if not clientes_lista:
        print("⚠️ Nenhum cliente cadastrado. Cadastre um cliente antes.")
        return
    if not servicos_lista:
        print("⚠️ Nenhum serviço cadastrado. Cadastre um serviço antes.")
        return

    print("\nClientes cadastrados:")
    for i, cliente in enumerate(clientes_lista, start=1):
        print(f"{i}. {cliente['nome']} - {cliente['telefone']}")
    escolha_cliente = int(input("Escolha o cliente pelo número: "))
    cliente_escolhido = clientes_lista[escolha_cliente - 1]

    print("\nServiços disponíveis:")
    for i, servico in enumerate(servicos_lista, start=1):
        print(f"{i}. {servico['nome']} - R$ {servico['preco']}")
    escolha_servico = int(input("Escolha o serviço pelo número: "))
    servico_escolhido = servicos_lista[escolha_servico - 1]

    atendimento = {
        "cliente": cliente_escolhido,
        "servico": servico_escolhido
    }

    atendimentos.append(atendimento)
    salvar_atendimentos(atendimentos)
    print(f"✅ Atendimento marcado para {cliente_escolhido['nome']} - Serviço: {servico_escolhido['nome']}")

def listar_atendimentos():
    """Lista todos os atendimentos marcados."""
    atendimentos = carregar_atendimentos()
    if not atendimentos:
        print("⚠️ Nenhum atendimento marcado.")
    else:
        print("\n📋 Lista de atendimentos:")
        for i, atendimento in enumerate(atendimentos, start=1):
            cliente = atendimento['cliente']
            servico = atendimento['servico']
            print(f"{i}. Cliente: {cliente['nome']} - Serviço: {servico['nome']} - Preço: R$ {servico['preco']}")
