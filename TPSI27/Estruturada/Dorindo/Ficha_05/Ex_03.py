def mostrar_menu():
    print("")
    print("--- MENU ---")
    print("1. Quantidade do Produto (stock)")
    print("2. Ver informação do Produto")
    print("3. Listar Produtos")
    print("4. Valor Total dos Produtos em stock")
    print("S. Sair")


# definiçao de funções

def procurar_produto(codigoProduto):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            produto = linha.strip().split(";")
            if codigoProduto == produto[0]:
                return (produto[0], produto[1], produto[2], produto[3])
           
    return None
        


def listar_produtos():
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            produto = linha.strip().split(";")
            print(f"{produto[0]} - {produto[1]} - {produto[2]} - {produto[3]}")


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
        codigo = input("Insira o Código do produto a pesquisar: ")
        produto = procurar_produto(codigo)
        if produto:
            print(f"Quantidade: {produto[1]}")
        else:
            print("Produto não existe.")

    elif opcao == "2":
        codigo = input("Insira o Código do produto a pesquisar: ")
        produto = procurar_produto(codigo)
        if produto:
            print(f"Código: {produto[0]} - Tipo: {produto[3]} - Quantidade: {produto[1]} - Preço: {produto[2]}")
        else:
            print("Produto não existe.")


    elif opcao == "3":
       listar_produtos()

    elif opcao == "4":
       total = valor_total_produtos()
       print(f"Valor Total dos Produtos em stock: {total}")
 

    elif opcao.upper()=="S":
        print("Obrigado!")
        break #sai do ciclo while
    
    else:
        print("Opção inválida.")