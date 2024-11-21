# 29. A Biblioteca do CINEL precisa da sua ajuda para organizar os Livros existentes na 
# mesma. Nesse sentido, é necessário criar um programa que permita guardar o nome, 
# o autor e o código ISBN de cada Livro. A aplicação uma lista e permitir realizar as 
# seguintes opções:

# a. Inserir um Livro
# b. Consultar Livro, dado o seu ISBN
# c. Consultar Livros, dado o seu autor
# d. Listar todos os livros
# e. Corrigir os dados de um livro
# f. Apagar dados de um livro
# g. Fechar Aplicação


# Nota: os livros são guardados numa lista de tuple(isbn, titulo, autor)

# definicao de funções
def mostrar_menu():
    print("")
    print("--- MENU ---")
    print("1. Inserir Livro")
    print("2. Consultar Livro por ISBN")
    print("3. Consultar Livro por Autor")
    print("4. Listar todos os Livros")
    print("5. Atualizar dados de um Livro")
    print("6. Apagar um Livro")
    print("7. Sair")


def inserir_livro(dadosLivro):
        livros.append(dadosLivro)


def existe_livro(isbnLivro):
    for livro in livros:
        if isbnLivro == livro[0]:
            return True

    return False


def pesquisa_livro_isbn(isbnLivro):
    for livro in livros:
        if isbnLivro == livro[0]:
            return (livro[0], livro[1], livro[2])
    
    return None


def pesquisa_livro_autor(autorLivro):
    
    listaLivrosAutor = [livro for livro in livros if livro[2] == autorLivro]
    return listaLivrosAutor
    

def atualizar_livro(dadosLivro):
    # obtenho a posição do livro a atualizar
    posicao = [ pos for pos, livro in enumerate(livros) if livro[0] == dadosLivro[0]] [0]
    livros[posicao] = (dadosLivro)
    print("Livro atualizado com sucesso.")


def apagar_livro(isbnLivro):
    # obtenho a posição do livro a atualizar
    posicao = [ pos for pos, livro in enumerate(livros) if livro[0] == isbnLivro] [0]
    livros.pop(posicao)
    print("Livro apagado com sucesso.")


def listar_livros():
    if livros:
        for livro in livros:        
            print(f"Título: {livro[1]} - Autor: {livro[2]} - ISBN: {livro[0]}")
    else:
        print("Sem Livros registados.")


# main program

livros = []

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        print("Escolheste Inserir Livro")
        isbn = input("ISBN: ")
        if not existe_livro(isbn):
            titulo = input("Título: ")
            autor = input("Autor: ")   
            livro = (isbn, titulo, autor)
            inserir_livro(livro)
        else:
            print("Já existe um Livro com o ISBN introduzido!")


    elif opcao == "2":
        print("Escolheste Consultar Livro por ISBN")
        isbn = input("ISBN: ")   
        livro = pesquisa_livro_isbn(isbn)
        if livro:
            print(f"Título: {livro[1]} - Autor: {livro[2]} - ISBN: {livro[0]}")
        else:
            print("Não encontrei o Livro com o ISBN introduzido!")


    elif opcao == "3":
        print("Escolheste Consultar Livro por Autor")
        autor = input("Autor: ")
        livrosPesquisa = pesquisa_livro_autor(autor)
        if livrosPesquisa:
            for livro in livrosPesquisa:
                print(f"Título: {livro[1]} - Autor: {livro[2]} - ISBN: {livro[0]}")
        else:
            print("Não encontrei Livros para o Autor introduzido!")


    elif opcao == "4":
        print("Escolheste Listar todos os Livros")
        listar_livros()

    elif opcao == "5":
        print("Escolheste Atualizar dados de um Livro")
        isbn = input("ISBN do Livro a atualizar: ")   
        livro = pesquisa_livro_isbn(isbn)
        if livro:
            titulo = input("Novo Título do Livro: ")
            autor = input("Novo Autor do Livro: ")
            novolivro = (isbn, titulo, autor)
            atualizar_livro(novolivro)
        else:
            print("Não encontrei o Livro com o ISBN introduzido!")


    elif opcao == "6":
        print("Escolheste Apagar um Livro")
        isbn = input("ISBN do Livro a apagar: ")   
        livro = pesquisa_livro_isbn(isbn)
        if livro:
            apagar_livro(isbn)
        else:
            print("Não encontrei o Livro com o ISBN introduzido!")


    elif opcao=="7":
        print("Obrigado!")
        break #sai do ciclo while
    else:
        print("opção inválida.")

