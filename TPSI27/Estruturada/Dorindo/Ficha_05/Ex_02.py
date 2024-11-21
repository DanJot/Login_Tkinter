def mostrar_menu():
    print("")
    print("--- MENU ---")
    print("1. Verificar existência de especialidade")
    print("2. Listar Médicos")
    print("S. Sair")


def existe_especialidade(especialidade):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        especialidades = [linha.strip().split(";")[2] for linha in linhas]
        if especialidade in especialidades:
            return True
        else:
            return False


def existe_medico(codigoMedico):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        codigos = [linha.strip().split(";")[0] for linha in linhas]
        if codigoMedico in codigos:
            return True
        else:
            return False
        


def listar_médicos():
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            colunas = linha.strip().split(";")
            print(f"{colunas[0]} - {colunas[1]} - {colunas[2]}")




# main program
nome_ficheiro="medicos.txt"

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        especialidade = input("Especialidade: ")
        existeEspecialidade = existe_especialidade(especialidade)
        if existeEspecialidade:
            print(f"A especialidade {especialidade} existe.")
        else:
            print(f"A especialidade {especialidade} não existe.")

    elif opcao == "2":
       listar_médicos()
 

    elif opcao.upper()=="S":
        print("Obrigado!")
        break #sai do ciclo while
    else:
        print("opção inválida.")