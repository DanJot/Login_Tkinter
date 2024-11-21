import funcoes

def menu():

    while True:
        print("****   CINEL DEELICIAS GASTRO  ****")
        print("1 - Adicionar Reserva")
        print("2 - Consultar Informações | Reserva")
        print("3 - Atualizar Informações | Reserva")
        print("4 - Listar Reservas - Por cliente")
        print("5 - Listar Reservas - Por Data")
        print("6 - Listar todas as Reservas")
        print("7 - Remover Reserva")
        print("0 - Fechar a Aplicação")
        opcao = input("Selecione a opção pretendida: ")


        match opcao:

            case "1":
                funcoes.CriarReserva()
            case "2":
                funcoes.ConsultarReserva()
            case "3":
                funcoes.AtualizarReserva()
            case "4":
                funcoes.ConsultarReservaCliente()
            case "5":
                funcoes.ConsultarReservaData()
            case "6":
                funcoes.ListarReservas()
            case "7":
                funcoes.RemoverReserva()
            case "0":
                print("Até já")
                break

            case _:
                print("\n Opção inválida")

menu()