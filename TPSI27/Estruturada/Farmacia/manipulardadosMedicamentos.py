import validarMedicamentos

def AdicionarMedicamento(codMedicamento, quantidadeMedicamento, precoMedicamento, nomeMedicamento):

    encontrado = False
    with open("medicamentos.txt", "r", encoding="UTF-8") as ficheiro:

        for linha in ficheiro:

            dados = linha.strip().split(';')
            if dados[0] == codMedicamento:
                encontrado = True
                print("\nEsse código já está registado\n !")
                break

        if not encontrado:
            linhas = (f"{codMedicamento};{quantidadeMedicamento};{precoMedicamento};{nomeMedicamento}\n")
            with open("medicamentos.txt", "a", encoding="UTF-8") as ficheiro:
                ficheiro.write(linhas)
            print("\nMedicamento registado com sucesso!\n\n")

def VerificarDisponibilidade(codMedicamento):
    encontrado = False
    with open("medicamentos.txt", "r", encoding="UTF-8") as ficheiro:

            for linha in ficheiro:

                dados = linha.strip().split(';')
                if dados[0] == codMedicamento:
                    encontrado = True
                    print("\nProduto encontrado!\n")
                    print("Código: " + dados[0] + "\n Quantidade: " + dados[1] + "\n")
                    break

            if not encontrado:
                print("\nEsse código não existe!\n\n")

def AtualizarMedicamento(codMedicamento):

    encontrado = False
    with open("medicamentos.txt", "r", encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        if not linhas:
            print("\n Não existem medicamento para atualizar!\n")
        else:

            for i,linha in enumerate(linhas):
                dados = linha.strip().split(';')
                if dados[0] == codMedicamento:
                    encontrado = True
                    print("\nProduto encontrado!\n")
                    novoPreco = input("Indique o novo preço: ")
                    novoPreco = validarMedicamentos.ValidarPreco(novoPreco)

                    novaQuantidade = input("Indique a nova quantidade: ")
                    novaQuantidade = validarMedicamentos.ValidarQuantidade(novaQuantidade)

                    linhas[i] = (f"{codMedicamento};{novaQuantidade};{novoPreco};{dados[3]}\n")
                    break

            if not encontrado:
                print("\nEsse código não existe!\n\n")
            else:

                with open("medicamentos.txt", "w", encoding="UTF-8") as ficheiro:
                    ficheiro.writelines(linhas)
                print("\nDados atualizados com sucesso!\n\n")
                
def AtualizarMedicamentoVenda(codMedicamento, quantidadeMedicamento):
    
    encontrado = False
    with open("medicamentos.txt", "r", encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        if not linhas:
            print("\n Não existem medicamento para atualizar!\n")
        else:

            for i,linha in enumerate(linhas):
                dados = linha.strip().split(';')
                if dados[0] == codMedicamento:
                    encontrado = True
                    
                    novaQuantidade = int(dados[1]) - int(quantidadeMedicamento)
                   

                    linhas[i] = (f"{codMedicamento};{novaQuantidade};{dados[2]};{dados[3]}\n")
                    break

            if not encontrado:
                print("\nEsse código não existe!\n\n")
            else:

                with open("medicamentos.txt", "w", encoding="UTF-8") as ficheiro:
                    ficheiro.writelines(linhas)
              

def RemoverMedicamento(codMedicamento):
    encontrado = False
    with open("medicamentos.txt", "r", encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for i,linha in enumerate(linhas):
            dados = linha.strip().split(';')
            if dados[0] == codMedicamento:
                encontrado = True
                linhas.pop(i)
                print("\nProduto removido!\n")
                break

        if not encontrado:
            print("\nEsse código não existe!\n\n")
        else:

            with open("medicamentos.txt", "w", encoding="UTF-8") as ficheiro:
                ficheiro.writelines(linhas)
            print("\nDados atualizados com sucesso!\n\n")

def ListagemMedicamentosNomeCodigo():

    with open("medicamentos.txt", "r", encoding="UTF-8") as ficheiro:
        print("\nListagem do ficheiro medicamento\n")
        for linha in ficheiro:
            dados = linha.strip().split(';')
            print(f"{dados[0]} {dados[1]} {dados[2]} {dados[3]}")
        print("----\n")
