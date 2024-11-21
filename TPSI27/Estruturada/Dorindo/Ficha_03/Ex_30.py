# 30. O Banco CINEL Exchange precisa da sua ajuda para a criação de uma aplicação para 
# a gestão das despesas diárias de um cliente. Nesse sentido, é necessário criar um 
# programa que permita guardar o nome e o saldo de cada Cliente. 
# A aplicação em Python deve utilizar listas para a gestão da informação permitir 
# realizar as seguintes opções:
# a. Inserir um Cliente
# b. Consultar Saldo de um Cliente
# c. Realizar um Levantamento - Cliente
# d. Listar todos os Clientes
# e. Realizar um Depósito - Cliente
# f. Fechar Aplicação



# Nota: os clientes são guardados numa lista de tuple(numero, nome, saldo)

# definicao de funções
def mostrar_menu():
    print("")
    print("--- MENU ---")
    print("a. Inserir Cliente")
    print("b. Consultar Saldo")
    print("c. Levantamento")
    print("d. Listar Clientes")
    print("e. Depósito")
    print("s. Sair")


def inserir_cliente(nomeCliente, saldoinicialCliente):

    if not clientes:
        numeroCliente = 1
    else:
        listaNumeros = [cliente[0] for cliente in clientes]
        maxnumeroCliente = max(listaNumeros)
        numeroCliente = maxnumeroCliente + 1
        
    cliente = (numeroCliente, nomeCliente, saldoinicialCliente)
    clientes.append(cliente)
    print("Cliente inserido com sucesso.")


def pesquisa_cliente_numero(numeroCliente):
    for cliente in clientes:
        if numeroCliente == cliente[0]:
            return (cliente[0], cliente[1], cliente[2])
    
    return None


def levantamento_cliente_numero(numeroCliente, montanteCliente):

    for pos, cliente in enumerate(clientes):
        if numeroCliente == cliente[0]:
            print("Encontrei cliente")
            if montanteCliente <= cliente[2]:
                clientes[pos] = (cliente[0], cliente[1], cliente[2] - montanteCliente)
            else:
                print("O seu Saldo não é suficiente para efetuar o levantamento.")

    if not clientes:    
        print("Não encontrei o Cliente com o Número introduzido!")


def deposito_cliente_numero(numeroCliente, montanteCliente):

    for pos, cliente in enumerate(clientes):
        if numeroCliente == cliente[0]:
            print("Encontrei cliente")
            clientes[pos] = (cliente[0], cliente[1], cliente[2] + montanteCliente)

    if not clientes:    
        print("Não encontrei o Cliente com o Número introduzido!")


def listar_clientes():
    if clientes:
        for cliente in clientes:        
            print(f"Número: {cliente[0]} - Nome: {cliente[1]} - Saldo: {cliente[2]}")
    else:
        print("Sem Clientes registados.")



# main program

clientes = []

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao.lower() == "a":
        print("Escolheste Inserir Cliente")
        nome = input("Nome: ")
        saldoInicial = float(input("Saldo Inicial: "))   
        inserir_cliente(nome, saldoInicial)


    elif opcao.lower() == "b":
        print("Escolheste Consultar Saldo")
        numero = int(input("Número: "))   
        cliente = pesquisa_cliente_numero(numero)
        if cliente:
            print(f"Saldo: {cliente[2]}")
        else:
            print("Não encontrei o Cliente com o Número introduzido!")


    elif opcao.lower() == "c":
        print("Escolheste Levantamento")
        numero = int(input("Número: "))   
        cliente = pesquisa_cliente_numero(numero)
        if cliente:
            montante = float(input("Montante: "))
            levantamento_cliente_numero(numero, montante)
        else:
            print("Não encontrei o Cliente com o Número introduzido!")


    elif opcao.lower() == "d":
        print("Escolheste Listar todos os Clientes")
        listar_clientes()


    elif opcao.lower() == "e":
        print("Escolheste Depósito")
        numero = int(input("Número: "))   
        cliente = pesquisa_cliente_numero(numero)
        if cliente:
            montante = float(input("Montante: "))
            deposito_cliente_numero(numero, montante)
        else:
            print("Não encontrei o Cliente com o Número introduzido!")


    elif opcao.lower() =="s":
        print("Obrigado!")
        break #sai do ciclo while
    else:
        print("opção inválida.")