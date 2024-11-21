def mostrar_menu():
    print("-------MENU-------")
    print("1 - Mostrar quantidade de determiado produto")
    print("2 - Consultar informação de determinado produto")
    print("3 - Consultar toda a informação")
    print("4 - Apresentar o preço de todos os produtos e somatorio dos mesmos")
    print("5 - Inserir novo produto")
    print("6 - Atualizar dados de um produto")


def opcao_1():
    with open("produtos.txt", "r", encoding="UTF-8") as ficheiro:
        codigo = input("Introduza o codigo do produto que pretende consultar\n")
        encontrou = False
        for linha in ficheiro:
            dados = linha.strip().split(';')
            if ( codigo == dados[0] ) and ( encontrou == False ):
                produto = (dados[0],dados[1],dados[3])
                encontrou = True
        if encontrou == True:
            print("O produto existe e tem os seguintes dados:")
            print(f"{'cod_prod':<5} {'qdd':<5} {'nome':<5}")
            print(produto)
        else:
            print("O produto nao existe")

def opcao_2():
    with open("produtos.txt", "r", encoding="UTF-8") as ficheiro:
        codigo = input("Introduza o codigo do produto que pretende consultar\n")
        encontrou = False
        for linha in ficheiro:
            dados = linha.strip().split(';')
            if ( codigo == dados[0] ) and ( encontrou == False ):
                produto = (dados[0],dados[1],dados[2],dados[3])
                encontrou = True
        if encontrou == True:
            print("O produto existe e tem os seguintes dados:")
            print(f"{'cod_prod':<5} {'qdd':<5} {'preço':<10} {'nome':<10}")
            print(produto)
        else:
            print("O produto nao existe")

def opcao_3():
    with open("produtos.txt", "r", encoding="UTF-8") as ficheiro:
        print(f"{'cod_prod':<10} {'qdd':<7} {'preço':<15} {'nome':<10}")
        for linha in ficheiro:
            dados = linha.strip().split(';')
            print(f"{dados[0]:<10} {dados[1]:<5} {dados[2]:<7} {dados[3]:<5}")



def opcao_4():
    with open("produtos.txt", "r", encoding="UTF-8") as ficheiro:
        print(f"{'preço':<5} {'nome':<5}")
        soma=0
        for linha in ficheiro:
            dados = linha.strip().split(';')
            soma += float(dados[2])
            print(f"{dados[2]:<5} {dados[3]:<5}")
        print(f"A soma de todos os preços é de: {soma}")

def opcao_5():
    cod= input("introduza o código do produto: ")
    qtd = float(input("introduza a quatidade do produto: "))
    preco = float(input("Introduza o preço do produto: "))
    nome = input("Introduza o nome do produto: ")
    dados = f"{cod};{str(qtd)};{str(preco)};{nome}\n"
    print("dados inseridos com sucesso")
    with open("produtos.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(dados)

def opcao_6():
    existe = False
    codProcurar = int(input("Indique o código do produto a procurar: "))
    with open("produtos.txt", "r", encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        #print(linhas)
        for i, linha in enumerate(linhas):
            dados = linha.strip().split(';')
            if codProcurar == int(dados[0]):
                #print("Estou aqui e estou na posição: " + str(i))
                novaQuantidade = float(input("Indique a nova quantidade do produto:"))
                novoPreco = float(input("Indique o novo preço do produto:"))
                novoNome = input("Indique o novo nome do produto produto:")
                existe = True
                linhas[i] = f"{str(codProcurar)};{str(novaQuantidade)};{str(novoPreco)};{novoNome}\n"
                with open("produtos.txt", "w", encoding="UTF-8") as ficheiro:
                    ficheiro.writelines(linhas)

    if not existe:
        print("Código do produto inválido!! ")


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
