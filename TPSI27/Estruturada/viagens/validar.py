from datetime import datetime

def ValidarNome(nome):
    while True:
        try:
            if len(nome) == 0 or len(nome) > 10:
                raise ValueError("O nome deve ter entre 1 e 10 caracteres")
            if not nome.isalpha():
                raise ValueError("O nome só pode ser constítuido por letras")
            return nome
        except ValueError as e:
            print(f"Erro: {e}")
            nome = input("Insira o nome no formato correto\n")

def ValidarDestino(destino):
    while True:
        try:
            if len(destino) == 0 or len(destino) > 15:
                raise ValueError("O destino deve ter entre 1 e 15 caracteres")
            if not destino.isalpha():
                raise ValueError("O destino só pode ser constítuido por letras")
            return destino
        except ValueError as e:
            print(f"Erro: {e}")
            destino = input("Insira destino no formato correto\n")

def ValidarDataPartida():
    while True:
        try:
            dataPartida = input("Insira a data de partida no formato DD/MM/AAAA: ")
            data = datetime.strptime(dataPartida, "%d/%m/%Y")
            return data
        except ValueError as e:
            print("Erro: A data tem que estar no formato DD/MM/AAAA")
            dataPartida = input("Insira a data de partida no formato correto: ")

def ValidarDataChegada(dataPartida):
    while True:
        try:
            dataChegada = input("Insira a data de chegada no formato DD/MM/AAAA: ")
            data = datetime.strptime(dataChegada, '%d/%m/%Y')

            if data < dataPartida:
                raise ValueError("A data de chegada não pode ser posterior à data de partida!")
            return data
        except ValueError as e:
            print(f"Erro: {e}")
            dataChegada = input("Insira a data de chegada no formato correto: ")

def ValidarAcompanhantes(numeroAcompanhantes):
    while True:
        try:
           # if numeroAcompanhantes.is_integer():
                #raise ValueError("O número de acompanhantes deve ser um número inteiro e maior que zero")
            if int(numeroAcompanhantes) <= 0:
                raise ValueError("")
            return numeroAcompanhantes
        except ValueError as e:
            print(f"Erro: O número de acompanhantes deve ser um número inteiro e maior que zero")
            numeroAcompanhantes = int(input("Insira o número de acompanhantes no formato correto\n"))

def ValidarReserva(numeroReserva):

    try:

    except ValueError as e:
