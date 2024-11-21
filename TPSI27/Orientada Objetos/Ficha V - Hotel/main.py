import manipularHotel

def menu():

    while True:
        print("CINEL RESORT E SPA")
        print("1 - Criar Quarto")
        print("2 - Listar Quartos Disponiveis")
        print("3 - Reservar Quarto | Simples - Luxo")
        print("4 - Alterar Status do Quarto")
        print("5 - Remover Quarto")
        print("6 - Listar Quartos Reservados")
        print("0 - Fechar a Aplicação ")

        opcao = input("Indique a sua opção: ")

        match opcao:

            case "0":
                print("Até à próxima!")
                break

            case "1":
                manipularHotel.CriarQuarto()

            case "2":
                manipularHotel.ListarQuatoDisponiveis()




            case _:
                print("Opção Inválida")



menu()