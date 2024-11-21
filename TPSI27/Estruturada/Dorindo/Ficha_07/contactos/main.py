# importação modulos
import validardados
import manipulardados
import os

# definição de Funções

def limpar_ecra():
    # Verifica o sistema operacional e usa o comando apropriado
    if os.name == 'nt':
        # Para Windows  
        os.system('cls')
    else:
        # Para Linux e macOS  
        os.system('clear')


def mostrar_menu():
    print("")
    print("--- AGENDA DIGITAL ---")
    print("1. Adicionar Contacto")
    print("2. Consultar informação de Contacto")
    print("3. Atualizar Contacto")
    print("4. Listar Contactos por ordem inserção")
    print("5. Listar Contactos por ordem alfabética")
    print("6. Remover Contacto")
    print("S. Sair")



# main program
# contacto -> nome, telefone, email

manipulardados.criar_ficheiro_se_nao_existe()

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        limpar_ecra()
        print("*** Inserir Contacto ***")
        telefone = input("Telefone: ")
        telefone = validardados.validar_telefone(telefone)
        if not manipulardados.existe_contacto(telefone) :
            nome = input("Nome: ")
            nome = validardados.validar_nome(nome)
            email = input("Email: ")
            email = validardados.validar_email(email)
            manipulardados.inserir_contacto(nome, telefone, email)
        else:
            print("Contacto já existe.")

        input("\nPressione qualquer tecla para continuar...")


    elif opcao == "2":
        limpar_ecra()
        print("*** Informação do Contacto ***")
        telefone = input("Telefone: ")
        telefone = validardados.validar_telefone(telefone)
        contacto = manipulardados.procurar_contacto(telefone)
        if contacto:
            print(f"{contacto[0]} - {contacto[1]} - {contacto[2]}")
        else:
            print("Contacto não encontrado.")

        input("\nPressione a tecla ENTER para continuar...")
    

    elif opcao == "3":
        limpar_ecra()
        print("*** Atualização de Contacto ***")
        telefone = input("Telefone: ")
        telefone = validardados.validar_telefone(telefone)
        contacto = manipulardados.procurar_contacto(telefone)
        if contacto:
            print(f"Nome (atual): {contacto[0]} - Telefone (atual) {contacto[1]} - Email (atual): {contacto[2]}")
            nome = input("Nome (novo): ")
            nome = validardados.validar_nome(nome)
            email = input("Email (novo): ")
            email = validardados.validar_email(email)
            manipulardados.atualizar_contacto(nome, telefone, email)
        else:
            print("Contacto não encontrado.")

        input("\nPressione a tecla ENTER para continuar...")


    elif opcao == "4":
        limpar_ecra()
        print("*** Lista de Contactos ***")
        manipulardados.listar_contactos()
        input("\nPressione a tecla ENTER para continuar...")


    elif opcao == "5":
        limpar_ecra()
        print("*** Lista de Contactos (ordem alfabética) ***")
        manipulardados.listar_contactos_ordNome_asc()
        input("\nPressione a tecla ENTER para continuar...")


    elif opcao == "6":
        limpar_ecra()
        print("*** Remover Contacto ***")
        telefone = input("Telefone: ")
        telefone = validardados.validar_telefone(telefone)
        contacto = manipulardados.procurar_contacto(telefone)
        if contacto:
            print(f"Nome: {contacto[0]} - Telefone: {contacto[1]} - Email: {contacto[2]}")
            confirmacao = input("Pretende prosseguir com a remoção do Contacto? [S-Sim; Outra tecla - Cancelar]: ")
            if confirmacao.lower() == "s":
                manipulardados.apagar_contacto(telefone)
            else:
                print("Operação de remoção cancelada.")
        else:
            print("Contacto não encontrado.")

        input("\nPressione a tecla ENTER para continuar...")


    elif opcao.upper()=="S":
        limpar_ecra()
        print("Obrigado!")
        break #sai do ciclo while


    else:
        limpar_ecra()
        print("Opção inválida.")
        input("\nPressione a tecla ENTER para continuar...")