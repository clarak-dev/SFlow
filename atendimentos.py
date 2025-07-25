import json
import os
from clientes import clientes
from servicos import servicos

ARQUIVO_ATENDIMENTOS = 'atendimentos.json'

def carregar_atendimentos():
    """Carrega a lista de atendimentos do arquivo JSON."""
    if os.path.exists(ARQUIVO_ATENDIMENTOS):
        with open(ARQUIVO_ATENDIMENTOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []

atendimentos = carregar_atendimentos()  # variável global para atendimentos

def salvar_atendimentos():
    """Salva a lista de atendimentos no arquivo JSON."""
    with open(ARQUIVO_ATENDIMENTOS, 'w', encoding='utf-8') as f:
        json.dump(atendimentos, f, indent=4, ensure_ascii=False)

def marcar_atendimento():
    """Agenda um atendimento para cliente e serviço cadastrados, incluindo data e horário."""
    if not clientes:
        print("⚠️ Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return

    if not servicos:
        print("⚠️ Nenhum serviço cadastrado. Cadastre um serviço primeiro.")
        return

    # Lista clientes
    print("\n📋 Lista de clientes:")
    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. {cliente['nome']}")

    try:
        escolha_cliente = int(input("Escolha o número do cliente para o atendimento: "))
        if escolha_cliente < 1 or escolha_cliente > len(clientes):
            print("❌ Número inválido de cliente.")
            return
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")
        return

    cliente_escolhido = clientes[escolha_cliente - 1]

    # Lista serviços
    print("\n📋 Lista de serviços:")
    for i, servico in enumerate(servicos, start=1):
        print(f"{i}. {servico['nome']} - R$ {servico['preco']:.2f}")

    try:
        escolha_servico = int(input("Escolha o número do serviço: "))
        if escolha_servico < 1 or escolha_servico > len(servicos):
            print("❌ Número inválido de serviço.")
            return
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")
        return

    servico_escolhido = servicos[escolha_servico - 1]

    data = input("Digite a data do atendimento (dd/mm/aaaa): ")
    horario = input("Digite o horário do atendimento (ex: 14:30): ")

    atendimento = {
        "cliente": cliente_escolhido["nome"],
        "servico": servico_escolhido["nome"],
        "preco": servico_escolhido["preco"],
        "data": data,
        "horario": horario
    }

    atendimentos.append(atendimento)
    salvar_atendimentos()

    print(f"✅ Atendimento para {cliente_escolhido['nome']} agendado com sucesso em {data} às {horario}!")

def listar_atendimentos():
    """Exibe todos os atendimentos agendados."""
    if not atendimentos:
        print("⚠️ Nenhum atendimento agendado.")
    else:
        print("\n📅 Atendimentos agendados:")
        for i, atendimento in enumerate(atendimentos, start=1):
            print(f"{i}. {atendimento['cliente']} - {atendimento['servico']} - R$ {atendimento['preco']:.2f} em {atendimento['data']} às {atendimento['horario']}")
