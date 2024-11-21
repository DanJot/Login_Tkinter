import validar
import manipulardados

def menu():
    print(" CINEL | TRAVEL")
    print("1 - Adicionar Viagem")
    print("2 - Consultar Viagem - Nome")
    print("3 - Atualizar Reserva")
    print("4 - Listar Reservas")
    print("6 - Listar Reservas - Destino")
    print("7 - Remover Reserva")
    print("8 - Fechar Aplicação\n")

while True:

    menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        #print("Escolheste a opção 1")
        nome = input("Escreva o nome do cliente: ")
        #chamo o metodo que recebe como parâmetro o nome do cliente
        nome = validar.ValidarNome(nome)

        destino = input("\nEscreva o destino do cliente: ")
        destino = validar.ValidarDestino(destino)

        dataPartida = validar.ValidarDataPartida()

        dataChegada = validar.ValidarDataChegada(dataPartida)

        numeroAcompanhantes = input("\nIndique o número de acompanhantes: ")
        numeroAcompanhantes = validar.ValidarAcompanhantes(numeroAcompanhantes)

        total = int(numeroAcompanhantes) * 100
        #tenho os dados validados
        manipulardados.AdicionarViagem(nome, destino,dataPartida.strftime('%d/%m/%Y'), dataChegada.strftime('%d/%m/%Y'),numeroAcompanhantes,total)

        """
        print("Dados\n")
        print("Nome: " + nome)
        print("\nDestino: " + destino)
        print("\nDataPartida: " + dataPartida.strftime('%d/%m/%Y'))
        print("\nDataChegada: " + dataChegada.strftime('%d/%m/%Y'))
        print("\nNAcompanhantes: " + numeroAcompanhantes)
        print(f"\nTotal: {total}")
        """
    elif opcao == "2":
        manipulardados.ConsultarViagemCliente()
    elif opcao == "4":
        print("Escolheste a opção 4")
    elif opcao == "6":
        manipulardados.ConsultarViagemDestino()
    elif opcao == "7":
        manipulardados.RemoverReserva()
    elif opcao == "8":
        print("\nObrigado pela sua colaboração !!\n")
        break
    else:
        print("\nOpção Inválida\n")
