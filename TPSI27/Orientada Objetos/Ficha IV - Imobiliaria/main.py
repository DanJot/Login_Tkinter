import imo

def menu():

    while True:
        print("\n CINEL | IMOBILIÁRIO")
        print("1 - Venda de um Imóvel")
        print("2 - Imoveis Disponiveis")
        print("3 - Inserir Imóvel")
        print("4 - Editar Preço de Imóvel ")
        print("5 - Remover Imóvel")
        print("6 - Listar Imóveis Vendidos")
        print("0 - Fechar a Aplicação")

        opcao = input("Indique a sua opção: ")

        match opcao:
            case "1":
                imo.VenderImovel()
            case "2":
                imo.ListarImoveisDisponiveis()
            case "3":
                imo.InserirImovel()
            case "4":
                imo.EditarImovel()
            case "5":
                imo.RemoverImovel()
            case "6":
                imo.ListarImoveisVendidos()
            case "0":
                print("\n Até à próxima")
                break
            case _:
                print("\n Opção Inválida")

menu()