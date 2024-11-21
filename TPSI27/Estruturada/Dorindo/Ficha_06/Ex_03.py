
# definicao de funcoes
def mostrar_menu():
    print("")
    print("--- MENU ---")
    print("a. Listar Formandos")
    print("b. Inserir Formando")
    print("c. Procurar Formando")
    print("d. Atualizar dados de um Formando")
    print("e. Eliminar Formando")
    print("f. Sair")


def listar_formandos():
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            colunas = linha.strip().split(";")
            print(f"{colunas[0]} - {colunas[1]} - {colunas[2]}")

        if not linhas:
            print("Não existem Formandos registados.")


def existe_formando(nomeFormando):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        nomes = [linha.strip().split(";")[0].lower() for linha in linhas]
        if nomeFormando.strip().lower() in nomes:
            return True
        else:
            return False
        
def procurar_formando(nomeFormando):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            colunas = linha.strip().split(";")
            if colunas[0].lower()==nomeFormando.lower():
                return (colunas[0], colunas[1], colunas[2])
        
    
    return None
        

def inserir_formando(nomeFormando, codigoFormando, cidadeFormando):

    if not existe_formando(nomeFormando):
        with open(nome_ficheiro, 'a', encoding="UTF-8") as ficheiro:
            novalinha = f"{nomeFormando};{codigoFormando};{cidadeFormando}\n"
            ficheiro.write(novalinha)
        print("Registo inserido com sucesso!")
    else:
        print("Formando já existe")



def atualizar_formando(nomeFormando, codigoFormando, cidadeFormando):
    if existe_formando:
        #Atualiza
        with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
            linhas = ficheiro.readlines()
            for pos, linha in enumerate(linhas):
                colunas = linha.strip().split(";")
                
                if nomeFormando.lower() == colunas[0].lower():
                    linhas[pos] = f"{nomeFormando};{codigoFormando};{cidadeFormando}\n"
                    break

    
        with open(nome_ficheiro, 'w', encoding="UTF-8") as ficheiro:
            ficheiro.writelines(linhas)

        print("Registo atualizado com sucesso!")
    else:
         print("Nome não existe")


def eliminar_formando(nomeFormando):
    if existe_formando:
        #Elimina
        with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
            linhas = ficheiro.readlines()
            for pos, linha in enumerate(linhas):
                colunas = linha.strip().split(";")
                
                if nomeFormando.lower() == colunas[0].lower():
                    linhas.pop(pos)
                    break

    
        with open(nome_ficheiro, 'w', encoding="UTF-8") as ficheiro:
            ficheiro.writelines(linhas)

        print("Registo eliminado com sucesso!")
    else:
         print("Nome não existe")


# main program
nome_ficheiro="CINEL.txt"

formandos = []

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao.lower() == "a":
        listar_formandos()

    elif opcao.lower() == "b":
        nome = input("Nome: ")
        existeFormando = existe_formando(nome)
        if not existeFormando:
            nome = input("Nome: ")
            codigo = input("Código: ")
            cidade = input("Cidade: ")
            inserir_formando(nome.strip(), codigo, cidade)
        else:
            print("Formando já existe")

    elif opcao.lower() == "c":
        nome = input("Insira o Nome a pesquisar: ")
        formando = procurar_formando(nome)
        if formando:
            print(f"Nome: {formando[0]} - Código: {formando[1]} - Cidade: {formando[2]}")
        else:
            print("Formando não existe.")

    elif opcao.lower() == "d":
        nome = input("Nome: ")
        existeFormando = existe_formando(nome)
        if existeFormando:
            codigo = input("Novo Código: ")
            cidade = input("Nova Cidade: ")
            atualizar_formando(nome, codigo, cidade)
        else:
            print("Código do Formando não existe.")


    elif opcao.lower() == "e":
        nome = input("Nome: ")
        existeFormando = existe_formando(nome)
        if existeFormando:
            eliminar_formando(nome)
        else:
            print("Código do Formando não existe.")


    elif opcao.lower()=="f":
        print("Obrigado!")
        break #sai do ciclo while
    
    else:
        print("opção inválida.")


