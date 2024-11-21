import datetime

nome_ficheiro = "viagens.txt"

def adicionar_viagem(nome, destino, numeroAcompanhantes, dataPartida, dataChegada, total):

    dataPartida = dataPartida.strftime("%d/%m/%Y")
    dataChegada = dataChegada.strftime("%d/%m/%Y")

#with open("viagens.txt", "w", encoding="UTF-8") as ficheiro:

#if not existe_medico(codigoMedico):
    with open(nome_ficheiro, "a", encoding="UTF-8") as ficheiro:
        novalinha = f"{nome};{destino};{numeroAcompanhantes};{dataPartida};{dataChegada};{total}\n"
        ficheiro.write(novalinha)
    print("Registo inserido com sucesso!")
#else:
    #print("Código já existe")



def verificao_criterios(nome, dataPartida):
    # nao pode ter uma viagem com dataPartida no mesmo dia

    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        
        viagens = [1 for linha in linhas if (nome == linha.strip().split(";")[0]) and (dataPartida.strftime("%d/%m/%Y") == linha.strip().split(";")[3]) ]

    
    print("Teste")


