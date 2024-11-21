import validar_veiculos


def AdicionarVeiculo(matricula, classe, saldo):

    encontrado = False
    with open("veiculos.txt", "r", encoding="UTF-8") as ficheiro:

        for linha in ficheiro:
            dados = linha.strip().split(';')
            if dados[0] == matricula:
                encontrado = True
                print("Essa matricula já está registada!")
                break

        if not encontrado:
            linhas = (f"{matricula};{classe};{saldo}\n")
            with open("veiculos.txt", "a", encoding="UTF-8") as ficheiro:
                ficheiro.write(linhas)
            print("\nVeiculo registado com sucesso!\n\n")


def RemoverVeiculo(matricula):
    encontrado = False
    with open("veiculos.txt", "r", encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for i, linha in enumerate(linhas):
            dados = linha.strip().split(';')
            if dados[0] == matricula:
                encontrado = True
                linhas.pop(i)
                print("\nVeiculo removido!\n")
                break

        if not encontrado:
            print("\nEssa matricula não existe!\n\n")
        else:

            with open("veiculos.txt", "w", encoding="UTF-8") as ficheiro:
                ficheiro.writelines(linhas)
            print("\nDados atualizados com sucesso!\n\n")


def ListarVeiculos():

    matricula = input("Indique a matricula do veiculo que pretende consultar: ")

    matricula = validar_veiculos.ValidarMatricula(matricula)

    encontrado = False

    with open("veiculos.txt", "r", encoding="UTF-8") as ficheiro:

        for linha in ficheiro:
            dados = linha.strip().split(';')
            if matricula == dados[0]:
                print(f"{dados[0]} {dados[1]} {dados[2]}")
                encontrado = True


        if not encontrado:
            print("\nA matricula que procura não existe ! \n")


def RecarregarSaldo(matricula):
    encontrado = False
    with open("veiculos.txt", "r", encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        if not linhas:
            print("\n Não existem veiculos para recarregar saldo!\n")
        else:
            for i, linha in enumerate(linhas):
                dados = linha.strip().split(';')
                if dados[0] == matricula:
                    encontrado = True
                    print("\nVeiculo encontrado!\n")
                    novosaldo = input("Indique o valor do novo saldo: ")
                    novosaldo = validar_veiculos.ValidarSaldo(novosaldo)

                    linhas[i] = (f"{matricula};{dados[1]};{novosaldo}")
                    break

            if not encontrado:
                print("\nEssa matricula não existe\n\n")
            else:

                with open("veiculos.txt", "w", encoding="UTF-8") as ficheiro:
                    ficheiro.writelines(linhas)
                print("\nDados atualizados com sucesso!\n\n")








