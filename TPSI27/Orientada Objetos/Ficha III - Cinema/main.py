import evento

def menu():

    while True:
        print("***   CINEMAS CINEL  ****")
        print("1 - Criar Espetáculo")
        print("2 - Vender Bilhete")
        print("3 - Consultar Informações | Espetáculo")
        print("4 - Atualizar Informações | Espetáculo")
        print("5 - Listar Espetáculos")
        print("6 - Remover Espetáculo")
        print("0 - Fechar a Aplicação")
        opcao = input("Selecione a opção pretendida: ")


        match opcao:

            case "1":
                evento.CriarEspetaculo()
            case "2":
                evento.Venderbilhetes()
            case "3":
                evento.ConsultarEspetaculo()
            case "4":
                evento.AtualizarEspetaculo()
            case "5":
                evento.ListarEspetaculos()
            case "6":
                evento.RemoverEspetaculo()
            case "0":
                print("Até já")
                break

            case _:
                print("\n Opção inválida")

menu()