
def ValidarMatricula(matricula):
    while True:
        try:
            if len(matricula) < 6 or len(matricula) > 8:
                raise ValueError("A matricula deve conter 6 a 8 caracteres")
            if not matricula.isalnum():
                raise ValueError("A matricula só pode ser constituido por números e letras")
            return matricula
        except ValueError as e:
            print(f"Erro: {e}")
            matricula = input("Insira o código no formato correto\n")



def ValidarSaldo(saldo):
    while True:
        try:
            saldo = float(saldo)
            if saldo < 0:
                raise ValueError("O saldo deve ser um número positivo ou zero")
            return saldo
        except ValueError as e:
            print(f"Erro: {e}")
            saldo = input("Insira o saldo no formato correto!\n")
