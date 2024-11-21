def mostrar_menu():
    print("--------MENU------")
    print(" 1 - Listar Formandos ")
    print(" 2 - Inserir Formando ")
    print(" 3 - Procurar Formando ")
    print(" 4 - Atualizar dados de um Formando ")
    print(" 5 - Eliminar Formando ")
    print(" 6 - Sair da Aplicação ")


def opcao_1():
    with open("CINEL.txt", "r", encoding="UTF-8") as ficheiro:
        print(f"{'Nome':<10} {'Cod Interno':<15} {'Cidade':<5}")
        for linha in ficheiro:
            dados = linha.strip().split(';')
            print(f"{dados[0]:<14} {dados[1]:<11} {dados[2]:5}")

def opcao_2():
    nome = input("Introduza o nome do Formando: ")
    cod = input("Introduza o código interno do Aluno: ")
    cid = input("Introduza a cidade que o Formando pertence: ")
    dados = f"{str(nome)};{str(cod)};{str(cid)}\n"
    print("Dados inseridos com sucesso")
    with open("CINEL.txt", "a", encoding="UTF-8") as ficheiro:
        ficheiro.write(dados)

def opcao_3():
    with open("CINEL.txt", "r", encoding="UTF-8") as ficheiro:
        codigo = input("Qual o código interno do formando a procurar? \n")
        encontrou = False
        for linha in ficheiro:
            dados = linha.strip().split(";")
            if codigo == dados[1] and encontrou == False:
                formando = (dados[0],dados[1],dados[2])
                encontrou = True

        if encontrou == True:
            print("O Formando foi encontrado e tem os seguintes dados: ")
            print(f"{'Nome': <7} {'Cod Interno': <7} {'Cidade': <5}")
            print(formando)
        else:
            print("Formando não existe")



def opcao_4():

    existe = False
    codProcurar = int(input("Indique o código do formando a procurar: "))
    with open("CINEL.txt", "r", encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for i, linha in enumerate(linhas):
            dados = linha.strip().split(';')
            if codProcurar == int(dados[1]):
                novoNome = input("Indique o novo nome do Formando: ")
                novoCod = input("Indique o novo código interno do formando: ")
                novaCid = input("Indique a nova cidade do aluno: ")
                existe = True
                linhas[i] = f"{str(novoNome)};{str(novoCod)};{str(novaCid)}"
                with open("CINEL.txt", "w", encoding="UTF-8") as ficheiro:
                    ficheiro.writelines(linhas)

def opcao_5():
    with open("CINEL.txt", "r", encoding="UTF-8") as ficheiro:
        print("Qual o codigo do formando que pretende eliminar? ")

def opcao_6():
    exit()

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
    elif opcao == "5":
        opcao_5()
    elif opcao == "6":
        opcao_6()
    else:
        print("Opção invalida")