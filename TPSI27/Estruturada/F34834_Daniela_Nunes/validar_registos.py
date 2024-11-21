from datetime import datetime

def ValidarPassagem(numpassagem):
    while True:
        try:
            numpassagem = int(numpassagem)
            if numpassagem <= 0:
                raise ValueError("O numero de passagens devem ser um número maior que zero")
            return numpassagem
        except ValueError as e:
            print(f"Erro: {e}")
            numpassagem = input("Insira o numero de passagens no formato correto!\n")


def ValidarDataPassagem():
    while True:
        try:
            dataPassagem = input("Insira a data de partida no formato DD/MM/AAAA: ")
            data = datetime.strptime(dataPassagem, "%d/%m/%Y")
            return data
        except ValueError as e:
            print("Erro: A data tem que estar no formato DD/MM/AAAA")
            dataPassagem = input("Insira a data de partida no formato correto: ")

