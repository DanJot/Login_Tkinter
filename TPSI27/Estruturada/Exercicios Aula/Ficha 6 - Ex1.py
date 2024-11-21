def mostrar_menu():
    print("-------MENU-------")
    print("1 - Adicionar informação ao ficheiro")
    print("2 - Consultar toda a informação do ficheiro")
    print("3 - Atualizar dados de um médico")
    print("4 - Fechar a aplicação")

def opcao_1():
    cod = input("introduza o código do colaborador: ")
    nome = input("Introduza o nome do médico: ")
    esp = input("Introduza a especialidade do médico: ")
    dados = f"{cod};{str(nome)};{str(esp)}\n"
    print("dados inseridos com sucesso")
    with open("medicos.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(dados)

def opcao_2():
    with open("medicos.txt", "r", encoding="UTF-8") as ficheiro:
        print(f"{'Cod':<5} {'Nome':<9} {'Especialidade':<15}")
        for linha in ficheiro:
            dados = linha.strip().split(';')
            print(f"{dados[0]:<5} {dados[1]:<9} {dados[2]:<7}")
def opcao_3():
    existe = False
    codProcurar = int(input("Indique o código do colaborador a procurar: "))
    with open("medicos.txt", "r", encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for i, linha in enumerate(linhas):
            dados = linha.strip().split(';')
            if codProcurar == int(dados[0]):
                novoNome = input("Indique o novo nome do médico:")
                novaEsp = input("Indique a especialidade do médico:")
                existe = True
                linhas[i] = f"{str(codProcurar)};{str(novoNome)};{str(novaEsp)}\n"
                with open("medicos.txt", "w", encoding="UTF-8") as ficheiro:
                    ficheiro.writelines(linhas)

    if not existe:
        print("Código do colaborador inválido!! ")


def opcao_4():
    Exit()

while True:
    mostrar_menu()
    opcao = input("Selecione a opção desejada\n")

    if opcao == "1":
        opcao_1()
    elif opcao == "2":
        opcao_2()
    elif opcao == "3":
        opcao_3()
    elif opcao == "4":
        opcao_4()
    else:
        print("Opção invalida")
