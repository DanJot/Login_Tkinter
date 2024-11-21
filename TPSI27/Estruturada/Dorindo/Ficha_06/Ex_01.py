# importação modulos
import os


# definição de Funções

def limpar_ecra():
    # Verifica o sistema operacional e usa o comando apropriado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')


def mostrar_menu():
    print("")
    print("--- MENU ---")
    print("1. Inserir Médico")
    print("2. Listar Médicos")
    print("3. Atualizar Médico")
    print("S. Sair")


def existe_medico(codigoMedico):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        codigos = [linha.strip().split(";")[0] for linha in linhas]
        if codigoMedico in codigos:
            return True
        else:
            return False
        

def inserir_medico(codigoMedico, nomeMedico, especialidadeMedico):

    if not existe_medico(codigoMedico):
        #Insere
        with open(nome_ficheiro, 'a', encoding="UTF-8") as ficheiro:
            novalinha = f"{codigoMedico};{nomeMedico};{especialidadeMedico}\n"
            ficheiro.write(novalinha)
        print("Registo inserido com sucesso!")
    else:
        print("Código já existe")


def listar_médicos():
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            dados = linha.strip().split(";")
            print(f"{dados[0]} - {dados[1]} - {dados[2]}")

        if not linhas:
            print("Não existem registos de Médicos")
            

def atualizar_medico(codigoMedico, nomeMedico, especialidadeMedico):
    if existe_medico(codigoMedico):
        #Atualiza
        with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
            linhas = ficheiro.readlines()
            for pos, linha in enumerate(linhas):
                dados = linha.strip().split(";")
                
                if codigoMedico == dados[0]:
                    linhas[pos] = f"{codigoMedico};{nomeMedico};{especialidadeMedico}\n"
                    break

    
        with open(nome_ficheiro, 'w', encoding="UTF-8") as ficheiro:
            ficheiro.writelines(linhas)

        print("Dados do Médico atualizados com sucesso!")

    else:
         print("Médico não encontrado.")




# main program
nome_ficheiro="medicos.txt"

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        limpar_ecra()
        codigo = input("Código: ")
        if not existe_medico(codigo):
            nome = input("Nome: ")
            especialidade = input("Especialidade: ")
            inserir_medico(codigo, nome, especialidade)
        else:
            print("Código já existe")

    elif opcao == "2":
        limpar_ecra()
        listar_médicos()
 
    elif opcao == "3":
        limpar_ecra()
        codigo = input("Código: ")
        if existe_medico(codigo):
            nome = input("Novo Nome: ")
            especialidade = input("Nova Especialidade: ")
            atualizar_medico(codigo, nome, especialidade)
        else:
            print("Médico não existe.")

    elif opcao.upper()=="S":
        limpar_ecra()
        print("Obrigado!")
        break #sai do ciclo while
    else:
        limpar_ecra()
        print("opção inválida.")

