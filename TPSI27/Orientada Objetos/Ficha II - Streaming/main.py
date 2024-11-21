import streaming

def menu():
    while True:
        print(" ***** CINEL FLIX ******")
        print("1 - Inserir Vídeo")
        print("2 - Listar Videos")
        print("3 - Listar Videos 5*")
        print("4 - Eliminar Video")
        print("0 - Fechar Aplicação")

        opcao = input("Escolha uma opção: ")

        match opcao:

            case "1":
                streaming.InserirVideo()
            case "2":
                streaming.ListarVideos()
            case "3":
                streaming.ListarVideos5()
            case "4":
                streaming.RemoverVideos()
            case "0":
                print("\n Até já!!")
                break
            case _:
                print("\nOpção inválida")

menu()