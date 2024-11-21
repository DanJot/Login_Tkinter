import funcoes

def menu():
    while True:
        print(" ***** AVALIAÇÕES ******")
        print("1 - Inserir Novo Estudante")#
        print("2 - Consultar as informações de um estudante específico")#
        print("3 - Atualizar informações de um estudante")
        print("4 - Listar todos os estudantes")#
        print("5 - Listar todos os estudantes - Aprovados")#
        print("6 - Remover um estudante do sistema")#
        print("0 - Fechar Aplicação")

        opcao = input("Escolha uma opção: ")

        match opcao:

            case "1":
                funcoes.InserirEstudante()
            case "2":
                funcoes.ListarEstudanteEsp()
            case "3":
                funcoes.AtualizarEstudante()
            case "4":
                funcoes.ListarEstudantes()
            case "5":
                funcoes.ListarEstudanteAprovados()
            case "6":
                funcoes.RemoverEstudante()
            case "0":
                print("\n Até uma próxima!!")
                break
            case _:
                print("\nOpção inválida")

menu()