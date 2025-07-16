from clientes import cadastrar_cliente, listar_clientes
from servicos import cadastrar_servico, listar_servicos
from atendimentos import marcar_atendimento, listar_atendimentos


def exibir_menu():
    print("\n--- Menu SFlow ---")
    print("1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Cadastrar Serviço")
    print("4. Listar Serviços")
    print("5. Marcar Atendimento")
    print("6. Listar Atendimentos")
    print("7. Sair")


def main():
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
            marcar_atendimento()
        elif opcao == "6":
            listar_atendimentos()
        elif opcao == "7":
            print("👋 Saindo do SFlow... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
