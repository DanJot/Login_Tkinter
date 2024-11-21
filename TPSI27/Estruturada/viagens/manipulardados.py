import validar
def AdicionarViagem(nome, destino,dataPartida, dataChegada,numeroAcompanhantes,total):

    encontrado = False
    with open("viagens.txt", "r", encoding="UTF-8") as ficheiro:

        for linha in ficheiro:

            dados = linha.strip().split(';')
            if dados[0] in nome:
                encontrado = True
                print("O Cliente já existe !")
                break

        if not encontrado:
            linhas = (f"{nome};{destino};{dataPartida};{dataChegada};{numeroAcompanhantes};{total}\n")
            with open("viagens.txt", "a", encoding="UTF-8") as ficheiro:
                ficheiro.write(linhas)
            print("\nDados da viagem guardados com sucesso!\n")

def ConsultarViagemCliente():

    nome = input("Indique o nome do cliente que pretende consultar: ")

    nome = validar.ValidarNome(nome)

    encontrado = False

    with open("viagens.txt", "r", encoding="UTF-8") as ficheiro:

        for linha in ficheiro:
            dados = linha.strip().split(';')
            if nome == dados[0]:
                print(f"{dados[0]} {dados[1]} {dados[2]} {dados[3]} {dados[4]} {dados[5]}")
                encontrado = True


        if not encontrado:
            print("\nO Cliente que procura não existe ! \n")


def ConsultarViagemDestino():

    destino = input("Indique o destino que pretende consultar")

    destino = validar.ValidarDestino(destino)

    encontrado = False

    with open("viagens.txt", "r", encoding="UTF-8") as ficheiro:

        for linha in ficheiro:
            dados = linha.strip().split(';')
            if destino == dados[1]:
                print(f"{dados[0]} {dados[1]} {dados[2]} {dados[3]} {dados[4]} {dados[5]}")
                encontrado = True

        if not encontrado:
            print("\nO Destino que procura não existe ! \n")


def RemoverReserva():

    with open("viagens.txt", "r", encoding="UTF-8") as ficheiro:

        linhas = ficheiro.readlines()

        for i, linha in enumerate(linhas):
            dados = linha.strip().split(';')
            print(f"{i+1} {dados[0]} {dados[1]} {dados[2]} {dados[3]} {dados[4]} {dados[5]}")

    numeroReserva = input("\n\n\n\nIndique a reserva que pretende remover: ")

    numeroReserva =  validar.ValidarReserva(numeroReserva)

    print(numeroReserva)