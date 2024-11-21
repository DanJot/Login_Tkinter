import apoio as aux
def menu():
    print("--------MENU------")
    print("1 - Listar todos os formandos")
    print("2 - Inserir formando")
    print("3 - Procurar formando")
    print("4 - Atualizar dados de um formando")
    print("5 - Eliminar um aluno")
    print("6 - Sair")


def opcao_3(): #Procurar formando
    procurarnome= input("Qual o nome do aluno que pretende encontrar: ")
    aux.procurar_formando(procurarnome)



while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        def listar_formandos():
    elif opcao == "2":
        def inserir_aluno():
    elif opcao == "3":
        opcao_3()
    elif opcao == "4":
        def atualizar_aluno():
    elif opcao == "5":
        opcao_5()
    elif opcao == "6":
        print("Obrigado!")
        break

