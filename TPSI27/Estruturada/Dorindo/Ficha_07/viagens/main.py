import validar
import manipulardados

# definicao de funcoes
def mostrar_menu():
    print("")
    print("--- CINEL | TRAVEL ---")
    print("1. Adicionar Viagem")
    print("2. Consultar Viagem - Nome")
    print("3. Atualizar Reserva")
    print("4. Listar Reservas")
    print("5. Listar Reservas - Nome")
    print("6. Listar Reservas - Destino")
    print("7. Remover Reserva")
    print("8. Fechar Aplicação")


#def inserir_viagem(nomeFormando, codigoFormando, cidadeFormando):

    # if not existe_formando(nomeFormando):
    #     with open(nome_ficheiro, 'a', encoding="UTF-8") as ficheiro:
    #         novalinha = f"{nomeFormando};{codigoFormando};{cidadeFormando}\n"
    #         ficheiro.write(novalinha)
    #     print("Registo inserido com sucesso!")
    # else:
    #     print("Formando já existe")

# main program


reservas = []

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        print("Escolheste a opção 1")

        nome = input("Nome: ")
        validar.validar_nome(nome)

        destino = input("Destino: ")
        while(not validar.validar_destino(destino)):
            destino = input("Insira o destino no formato correto. Destino: ")


        # while(True):
        #     numeroAcompanhantes =input("Número de acompanhantes: ")
        #     if not numeroAcompanhantes.isnumeric():
        #         numeroAcompanhantes = print("Insira o número de acompanhantes no formato correto.")
        #     else:
        #         break

        numeroAcompanhantes =input("Número de acompanhantes: ")        
        numeroAcompanhantes = validar.validar_numeroacompanhantes(numeroAcompanhantes)
        #print(numeroAcompanhantes)

        dataPartida =input("Data de Partida no formato DD/MM/AAAA: ")        
        dataPartida = validar.validar_datapartida(dataPartida)

        #print(type(dataPartida))

        dataChegada =input("Data de Chegada no formato DD/MM/AAAA: ")   
        dataChegada = validar.validar_datachegada(dataChegada, dataPartida)

        total = numeroAcompanhantes * 100


        # print(f"Nome: {nome}")
        # print(f"Destino: {destino}")
        # print(f"Número de acompanhantes: {numeroAcompanhantes}")
        # print(f"Data de Partida: {dataPartida.strftime("%d/%m/%Y")}")
        # print(f"Data de Chegada: {dataChegada.strftime("%d/%m/%Y")}")
        # print(f"Total: {total}")

        manipulardados.verificao_criterios(nome, dataPartida)

        manipulardados.adicionar_viagem(nome, destino, numeroAcompanhantes, dataPartida, dataChegada, total)

         




    # elif opcao == "2":
    #     nome = input("Nome: ")
    #     existeFormando = existe_formando(nome)
    #     if not existeFormando:
    #         nome = input("Nome: ")
    #         codigo = input("Código: ")
    #         cidade = input("Cidade: ")
    #         inserir_formando(nome.strip(), codigo, cidade)
    #     else:
    #         print("Formando já existe")

    # elif opcao == "3":
    #     nome = input("Insira o Nome a pesquisar: ")
    #     formando = procurar_formando(nome)
    #     if formando:
    #         print(f"Nome: {formando[0]} - Código: {formando[1]} - Cidade: {formando[2]}")
    #     else:
    #         print("Formando não existe.")

    # elif opcao == "4":
    #     nome = input("Nome: ")
    #     existeFormando = existe_formando(nome)
    #     if existeFormando:
    #         codigo = input("Novo Código: ")
    #         cidade = input("Nova Cidade: ")
    #         atualizar_formando(nome, codigo, cidade)
    #     else:
    #         print("Código do Formando não existe.")


    # elif opcao == "5":
    #     nome = input("Nome: ")
    #     existeFormando = existe_formando(nome)
    #     if existeFormando:
    #         eliminar_formando(nome)
    #     else:
    #         print("Código do Formando não existe.")


    elif opcao.lower()=="8":
        print("Obrigado!")
        break #sai do ciclo while
    
    else:
        print("opção inválida.")

