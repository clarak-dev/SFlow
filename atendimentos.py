# sflow/atendimentos.py

from clientes import clientes
from servicos import servicos

atendimentos = []  # Lista para armazenar os atendimentos


def marcar_atendimento():
    """
    Permite ao usuário marcar um atendimento no sistema.

    O usuário escolhe um cliente da lista de clientes cadastrados,
    escolhe um serviço da lista de serviços cadastrados,
    e informa a data e a hora do atendimento.

    Se não houver clientes ou serviços cadastrados, a função exibe uma mensagem de aviso
    e não permite marcar o atendimento.

    Ao final, o atendimento é armazenado na lista 'atendimentos'.
    """
    print("\n--- Marcar Atendimento ---")

    if not clientes:
        print("⚠️ Nenhum cliente cadastrado.")
        return

    if not servicos:
        print("⚠️ Nenhum serviço cadastrado.")
        return

    # Escolher cliente
    print("\nClientes:")
    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. {cliente['nome']} - {cliente['telefone']}")
    cliente_index = int(input("Escolha o cliente (número): ")) - 1
    cliente_escolhido = clientes[cliente_index]

    # Escolher serviço
    print("\nServiços:")
    for i, servico in enumerate(servicos, start=1):
        print(f"{i}. {servico['nome']} - R${servico['valor']:.2f}")
    servico_index = int(input("Escolha o serviço (número): ")) - 1
    servico_escolhido = servicos[servico_index]

    # Data e hora
    data = input("Data do atendimento (dd/mm/aaaa): ")
    hora = input("Hora do atendimento (hh:mm): ")

    # Criar o atendimento
    atendimento = {
        "cliente": cliente_escolhido,
        "servico": servico_escolhido,
        "data": data,
        "hora": hora
    }
    atendimentos.append(atendimento)
    print(f"✅ Atendimento marcado para {cliente_escolhido['nome']} em {data} às {hora}.")


def listar_atendimentos():
    """
    Exibe todos os atendimentos marcados.

    Se não houver atendimentos, exibe mensagem informando que a lista está vazia.

    Para cada atendimento, exibe:
    - Nome do cliente
    - Serviço escolhido
    - Data e hora do atendimento
    """
    print("\n--- Lista de Atendimentos ---")
    if not atendimentos:
        print("⚠️ Nenhum atendimento marcado.")
    else:
        for i, atendimento in enumerate(atendimentos, start=1):
            cliente = atendimento["cliente"]["nome"]
            servico = atendimento["servico"]["nome"]
            data = atendimento["data"]
            hora = atendimento["hora"]
            print(f"{i}. {cliente} - {servico} em {data} às {hora}")
