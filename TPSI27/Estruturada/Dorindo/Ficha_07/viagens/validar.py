import datetime

def validar_nome(nome:str):
    # O nome do viajante deve ter no máximo 10 caracteres
    while True:
        try:
            if(len(nome) == 0 or len(nome) >10):
                raise ValueError("O nome deve ter entre 1 e 10 carateres")
            

            #if not nome.isalpha():
            if not nome.replace(" ", "").isalpha():
                raise ValueError("O nome só pode ser constituído por letras.")
            
            break

        except ValueError as e:
            print(f"Erro: {e}")
            nome = input("Insira o nome no formato correto. Nome: ")

    

def validar_destino(destino:str):
    
    # O nome do viajante deve ter no máximo 10 caracteres
    #while True:
    error = False
    try:
        if(len(destino) == 0 or len(destino) >15):
            raise ValueError("O destino deve ter entre 1 e 15 carateres")
        
        #if not destino.isalpha():
        if not destino.replace(" ", "").isalpha():
            raise ValueError("O destino só pode ser constituído por letras.")
        
        return True
        
        #break

    except ValueError as e:
        print(f"Erro: {e}") 
        #destino = input("Insira o destino no formato correto\n")
        return False
    

def validar_numeroacompanhantes(numeroAcompanhantes:str):  
    while True:

        try:
            numero = int(numeroAcompanhantes)
            if numero <= 0:
                #raise ValueError("O número de acompanhantes deve ser um número inteiro e maior do que zero.")
                raise ValueError()
            
            break

        except ValueError as e:
            #print(f"Erro: {e}")
            print("O número de acompanhantes deve ser um número inteiro e maior do que zero.")
            numeroAcompanhantes = input("Insira o número de acompanhantes no formato correto. Nº Acompanhantes: ")


    return numero       


def validar_datapartida(dataPartida):
    while True:
        try:
            dataPartida = datetime.datetime.strptime(dataPartida,"%d/%m/%Y")
            return dataPartida
    
        except ValueError as e:
            #print(f"Erro: {e}")
            print("A data tem que estar no formato DD/MM/AA.")
            dataPartida = input("Insira o número de acompanhantes no formato correto. Data de Partida: ")
            

def validar_datachegada(dataChegada, dataPartida):
    while True:
        try:
            dataChegada = datetime.datetime.strptime(dataChegada,"%d/%m/%Y")
            if dataChegada < dataPartida:
                raise ValueError()
            
            return dataChegada
    
        except ValueError as e:
            #print(f"Erro: {e}")
            print("A Data de Chegada tem que estar no formato DD/MM/AA e ser superior à Data de partida.")
            dataChegada = input("Insira a Data de Chegada no formato correto. Data de Chegada: ")
