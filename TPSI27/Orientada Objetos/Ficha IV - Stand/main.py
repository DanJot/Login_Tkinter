import stand

def menu():

    while True:
        print("\n CINEL | Boa Viagem")
        print("1 - Venda de um Carro")
        print("2 - Carros Disponiveis")
        print("3 - Inserir Carro")
        print("4 - Editar Carro")
        print("5 - Remover Carro")
        print("6 - Listar Carros Vendidos")
        print("0 - Fechar a Aplicação")

        opcao = input("Indique a sua opção: ")

        match opcao:
            case "1":
                stand.VenderCarro()
            case "2":
                stand.ListarCarrosDisponiveis()
            case "3":
                stand.InserirCarro()
            case "4":
                stand.EditarCarro()
            case "5":
                stand.RemoverCarro()
            case "6":
                stand.ListarCarrosVendidos()
            case "0":
                print("\n Até à próxima")
                break
            case _:
                print("\n Opção Inválida")

menu()