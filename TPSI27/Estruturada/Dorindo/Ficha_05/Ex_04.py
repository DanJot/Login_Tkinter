# importação de módulos
import os

# decalaração de funções
def mostrar_menu():
    print("")
    print("--- CINEL DOCE, SA ---")
    print("1. Listar informação do ficheiro")
    print("2. Listar informação do Cliente com maior valor gasto")
    print("3. Apresentar número de Clientes")
    print("4. Listar informação dos Clientes do Porto")
    print("5. Total de vales oferecidos (vendas > 100€)")
    print("S. Sair")


def listar_ficheiro():
    # Verificar se o ficheiro existe
    if os.path.exists(nome_ficheiro):
        with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
            linhas = ficheiro.readlines()
            for linha in linhas:
                venda = linha.strip().split(";")
                print(f"{venda[0]} - {venda[1]} - {venda[2]}")
    else:
        print(f"Erro: O ficheiro '{nome_ficheiro}' não existe no diretório atual.")



def lista_de_clientes():
    # venda -> nome, totalVenda, cidade
    # cliente -> nome, totalCliente, cidade
    
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        vendas = [linha.strip().split(";") for linha in ficheiro.readlines()]

    clientes = []

    for venda in vendas:

        encontrei = False

        for pos, cliente in enumerate(clientes):
            #print(f"Cliente: {pos}")
            if cliente[0] == venda[0]:
                encontrei = True
                clientes[pos] = [venda[0], float(cliente[1]) + float(venda[1]), venda[2]]
                break

        if not encontrei:
            clientes.append([venda[0], float(venda[1]), venda[2]])   
    
    return clientes



def cliente_max_total():

    clientes = lista_de_clientes()
    max=0
    for i, cliente in enumerate(clientes):
        if cliente[1] > max:
            max = cliente[1]
            indice = i

    clientemaiortotal = clientes[indice]
    print(f"{clientemaiortotal[0]} - {clientemaiortotal[1]} - {clientemaiortotal[2]}")


def numero_clientes():

    clientes = lista_de_clientes()
    numclientes = len(clientes)
    print(f"Número total de Clientes: {numclientes}")


def listar_clientes_cidade(cidadeCliente):
    listaClientes = lista_de_clientes()
    listaClientesCidade = [cliente for cliente in listaClientes if cliente[2] == cidadeCliente]

    if listaClientesCidade:
        for cliente in listaClientesCidade:
            print(f"{cliente[0]} - {cliente[1]} - {cliente[2]}")
    else:
        print(f"Não existem Clientes na cidade {cidadeCliente}")        



def num_vales_oferecidos():
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        vendas = [linha.strip().split(";") for linha in ficheiro.readlines()]

    vendascomvale = [venda for venda in vendas if float(venda[1])>100]

    print(f"Número de Vales de Desconto oferecidos: {len(vendascomvale)}")





# main program
nome_ficheiro="clientes.txt"

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        listar_ficheiro()

    elif opcao == "2":
       cliente_max_total()

    elif opcao == "3":
       numero_clientes()

    elif opcao == "4":
       listar_clientes_cidade("Porto")

    elif opcao == "5":
       num_vales_oferecidos()
 

    elif opcao.upper()=="S":
        print("Obrigado!")
        break #sai do ciclo while
    else:
        print("opção inválida.")