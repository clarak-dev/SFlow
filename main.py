import clientes
import servicos
import atendimentos

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
            clientes.cadastrar_cliente()
        elif opcao == "2":
            clientes.listar_clientes()
        elif opcao == "3":
            servicos.cadastrar_servico()
        elif opcao == "4":
            servicos.listar_servicos()
        elif opcao == "5":
            atendimentos.marcar_atendimento()
        elif opcao == "6":
            atendimentos.listar_atendimentos()
        elif opcao == "7":
            print("👋 Saindo do SFlow... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
