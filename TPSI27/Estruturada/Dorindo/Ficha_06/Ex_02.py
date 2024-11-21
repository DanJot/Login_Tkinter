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
    print("1. Listar Produtos")
    print("2. Inserir Produto")
    print("3. Ver informação de Produto")
    print("4. Atualizar informação de Produto")
    print("S. Sair")


# definiçao de funções

def listar_produtos():
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            produto = linha.strip().split(";")
            print(f"Código: {produto[0]} - Tipo: {produto[3]} - Quantidade: {produto[1]} - Preço: {produto[2]} ")


def existe_produto(codigoPoduto):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        codigos = [linha.strip().split(";")[0] for linha in linhas]
        if codigoPoduto in codigos:
            return True
        else:
            return False
        

def inserir_produto(codigoProduto, quantidadeProduto, precoProduto, tipoProduto):

    if not existe_produto(codigoProduto):
        #Insere
        with open(nome_ficheiro, 'a', encoding="UTF-8") as ficheiro:
            novalinha = f"{codigoProduto};{quantidadeProduto};{precoProduto};{tipoProduto}\n"
            ficheiro.write(novalinha)
        print("Registo inserido com sucesso!")
    else:
        print("Código já existe")


def procurar_produto(codigoProduto):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            produto = linha.strip().split(";")
            if codigoProduto == produto[0]:
                return (produto[0], produto[1], produto[2], produto[3])
           
    return None


def atualizar_produto(codigoProduto, quantidadeProduto, precoProduto, tipoProduto):
    if existe_produto(codigoProduto):
        #Atualiza
        with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
            linhas = ficheiro.readlines()
            for pos, linha in enumerate(linhas):
                produto = linha.strip().split(";")
                
                if codigoProduto == produto[0]:
                    linhas[pos] = f"{codigoProduto};{quantidadeProduto};{precoProduto};{tipoProduto}\n"
                    break

    
        with open(nome_ficheiro, 'w', encoding="UTF-8") as ficheiro:
            ficheiro.writelines(linhas)

        print("Dados do Produto atualizados com sucesso!")

    else:
         print("Produto não encontrado.")
        


def valor_total_produtos():
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        produtos = [linha.strip().split(";") for linha in ficheiro.readlines()]
    
    total_tipo = [ int(produto[1]) * float(produto[2])  for produto in produtos]
    return(sum(total_tipo))



# main program
nome_ficheiro="produtos.txt"

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        limpar_ecra()
        listar_produtos()


    elif opcao == "2":
        limpar_ecra()
        codigo = input("Código: ")
        if not existe_produto(codigo):
            quantidade = input("Quantidade: ")
            preco = input("Preço: ")
            tipo = input("Tipo: ")
            inserir_produto(codigo, quantidade, preco, tipo)
        else:
            print("Código já existe")


    elif opcao == "3":
        codigo = input("Insira o Código do produto a pesquisar: ")
        produto = procurar_produto(codigo)
        if produto:
            print(f"Código: {produto[0]} - Tipo: {produto[3]} - Quantidade: {produto[1]} - Preço: {produto[2]}")
        else:
            print("Produto não existe.")


    elif opcao == "4":       
        limpar_ecra()
        codigo = input("Código: ")
        if existe_produto(codigo):
            quantidade = input("Quantidade: ")
            preco = input("Preço: ")
            tipo = input("Tipo: ")
            atualizar_produto(codigo, quantidade, preco, tipo)
        else:
            print("Produto não existe.")
 

    elif opcao.upper()=="S":
        limpar_ecra()
        print("Obrigado!")
        break #sai do ciclo while
    
    else:
        limpar_ecra()
        print("Opção inválida.")