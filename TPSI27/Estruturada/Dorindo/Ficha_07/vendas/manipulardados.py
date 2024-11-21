# importar modulos
import os

nome_ficheiro="produtos.txt"


# definição de Funções

def existe_produto(codigoProduto):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            produto = linha.strip().split(";")
            if codigoProduto == produto[0]:
                return True
        return False


def inserir_produto(codigoProduto, quantidadeProduto, precoProduto, tipoProduto):
    if not existe_produto(codigoProduto):
        with open(nome_ficheiro, 'a', encoding="UTF-8") as ficheiro:
            novalinha = f"{codigoProduto};{quantidadeProduto};{precoProduto};{tipoProduto}\n"
            ficheiro.write(novalinha)
        print("Produto inserido com sucesso!")
    else:
        print("Produto já existe")


def procurar_produto(codigoProduto):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            produto = linha.strip().split(";")
            if codigoProduto == produto[0]:
                return (produto[0], produto[1], produto[2], produto[3]) 
    return None


def atualizar_produto(codigoProduto, quantidadeProduto, precoProduto):
    if existe_produto(codigoProduto):
        #Atualiza
        with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
            linhas = ficheiro.readlines()
            for pos, linha in enumerate(linhas):
                produto = linha.strip().split(";")
                
                if codigoProduto == produto[0]:
                    linhas[pos] = f"{codigoProduto};{quantidadeProduto};{precoProduto};{produto[3]}\n"
                    break

        with open(nome_ficheiro, 'w', encoding="UTF-8") as ficheiro:
            ficheiro.writelines(linhas)

        print("Produto atualizado com sucesso!")

    else:
         print("Produto não encontrado.")




def listar_produtos():
    
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        produtos = [linha.strip().split(";") for linha in ficheiro.readlines()]

    if produtos:
        imprimir_lista_produtos(produtos)     
    else:
        print("Não existem registos de Produtos.")  


def apagar_produto(codigoProduto:str):
    if existe_produto(codigoProduto):
        #Apaga
        with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
            linhas = ficheiro.readlines()
            for pos, linha in enumerate(linhas):
                produto = linha.strip().split(";")
                
                if codigoProduto == produto[0]:
                    linhas.pop(pos)
                    break

        with open(nome_ficheiro, 'w', encoding="UTF-8") as ficheiro:
            ficheiro.writelines(linhas)

        print("Produto apagado com sucesso!")

    else:
        print("Produto não encontrado.")


def imprimir_lista_produtos(listaLinhas):
    if listaLinhas:
        print("-"*80)  # Linha separadora opcional para dar destaque
        print(f"{'Código':<10} {'Qtd':<10} {'Preço':<10} {'Tipo':<50}")
        print("-"*80)  # Linha separadora opcional para dar destaque

        for linha in listaLinhas:
                print(f"{linha[0]:<10} {linha[1]:<10} {linha[2]:10} {linha[3]:<50}")


            