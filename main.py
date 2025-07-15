# sflow/main.py

from clientes import cadastrar_cliente, listar_clientes
from servicos import cadastrar_servico, listar_servicos


def exibir_menu():
    """
    Exibe o menu principal do sistema com as opções disponíveis.
    """
    print("\n✨ --- SFlow | Sistema para Studios de Beleza --- ✨")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Cadastrar serviço")
    print("4. Listar serviços")
    print("5. Marcar atendimento")
    print("6. Listar atendimentos")
    print("7. Sair")


def main():
    """
    Função principal que executa o menu e gerencia as escolhas do usuário.
    """
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            cadastrar_servico()
        elif opcao == "4":
            listar_servicos()
        elif opcao == "5":
            print("📌 Função de marcar atendimento ainda será implementada.")
        elif opcao == "6":
            print("📌 Função de listar atendimentos ainda será implementada.")
        elif opcao == "7":
            print("👋 Saindo do SFlow... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
