#Ficha 3 - Ex. 29
livros = [] #criação de uma lista vazia
def mostrar_menu(): #Definir a função
    print("")
    print("--- MENU ---")
    print("1. Inserir Livro")
    print("2. Consultar Livro por ISBN")
    print("3. Consultar Livro por Autor")
    print("4. Listar todos os Livros")
    print("5. Atualizar dados de um Livro")
    print("6. Apagar um Livro")
    print("7. Sair")
    print("8. Listar por ISBN")

def opcao1():
    codigoISBN = int(input("Indique o código do Livro:"))
    procurar = False
    for livro in livros:
        if codigoISBN == livro[0]:
            print("O código já existe")
            procurar = True

    if not procurar: # a condiçáo é igual if procurar == False:
        nome = input("Indique o nome do livro: ")
        autor = input("Indique o autor do livro: ")
        livros.append((codigoISBN, nome, autor))
        print("Livro guardado com sucesso!")

def opcao2(procurarISBN):
    for livro in livros:
        if procurarISBN == livro[0]:
            print("O livro existe e tem a seguinte informação:")
            print("ISBN:", livro[0], "Nome:", livro[1], "Autor:", livro[2])
            return
    print("O livro não existe!")

def opcao3():
    if not livros: #Verifica se a lista está vazia
        print("Ainda ão foram inseridos livros !")
        return
    procurarAutor = input("Indique o nome do autor do livro a pesquisar:")
    procurar = False
    for livro in livros:
        if procurarAutor == livro[2]:
            print("ISBN:", livro[0], "Nome:", livro[1], "Autor:", livro[2])
            procurar = True
    if not procurar:
        print("Não existem livros do autor guardados !")


def opcao4():
    print(f" {'ISBN': <5} {'Nome': <5} {'Autor'}") #<5 é o espaçamento
    for codigoISBN, nome, autor in livros:
        print(f" {codigoISBN:<5} {nome:<5} {autor}")


def opcao5():
    if not livros:
        print("Não foram inseridos livros!")
        return
    atualizarLivroISBN = int(input("Indique o código do livro que pretende atualizar: "))
    for posicao, livro in enumerate(livros):  # a função enumerate devolve a posição e conteudo da Linha
        if atualizarLivroISBN == livro[0]:
            novoNome = input("Diga o novo nome do livro: ")
            novoAutor = input("Diga o novo autor do livro: ")
            #na posição encontrada vamos inserir a nova informação
            livros[posicao] = (livro[0], novoNome, novoAutor)
            print("Os dados do livro foram atualizados com sucesso!")
            return
    print("Livro não encontrado!")

def opcao6():
    if not livros:
        print("Não forma inseridos livros!")
        return
    removerLivroISBN = int(input("Indique o código do livro que pretende remover:"))
    for posicao, livro in enumerate(livros): # a função enumerate devolve a posição e conteudo da Linha
        if removerLivroISBN == livro[0]:
            livros.pop(posicao) #permite remover a linha de dados encontrada
            print("O livro foi removido com sucesso!")
            return
        print("Livro não encontrado!")

def opcao8():
    listaOrdenaISBN = sorted(livros, key=lambda x: x[0])  #Garantir que a ordem da lista inicial de mantém inalterada, é criada uma lista diferente
    print(f" {'ISBN': <5} {'Nome': <5} {'Autor'}")  # <5 é o espaçamento
    for codigoISBN, nome, autor in listaOrdenaISBN:
        print(f" {codigoISBN:<5} {nome:<5} {autor}")


while True:
    mostrar_menu()
    opcao = input("indique a sua opção: ")

    if opcao == "1":
        opcao1()
    elif opcao == "2":
        procurarISBN = int(input("Indique o código do livro a pesquisar:"))
        opcao2(procurarISBN) #Função que serve como parametro a procurar ISBN
    elif opcao == "3":
        opcao3()
    elif opcao == "4":
        opcao4()
    elif opcao == "5":
        opcao5()
    elif opcao == "6":
        opcao6()
    elif opcao == "8":
        opcao8()
    elif opcao =="7":
        print("Obrigado !")
        break # vai tornar a condição satisfeita e terminar o While
    else:
        print("Opção inválida")






