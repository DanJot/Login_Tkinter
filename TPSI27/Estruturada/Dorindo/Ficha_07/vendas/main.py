# importação modulos
import validardados
import manipulardados
import os

# definição de Funções

def limpar_ecra():
    # Verifica o sistema operacional e usa o comando apropriado
    if os.name == 'nt':
        # Para Windows  
        os.system('cls')
    else:
        # Para Linux e macOS  
        os.system('clear')


def mostrar_menu():
    print("")
    print("--- CINEL Ferragens ---")
    print("1. Inserir Produto")
    print("2. Consultar informação do Produto")
    print("3. Atualizar Produto")
    print("4. Listar Produtos")
    print("5. Remover Produto")
    print("S. Sair")


    # main program
# produto -> codigo, quantidade, preco, tipo

#manipulardados.criar_ficheiro_se_nao_existe()

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        limpar_ecra()
        print("*** Inserir Contacto ***")
        codigo = input("Código: ")
        codigo = validardados.validar_codigo(codigo)
        if not manipulardados.existe_produto(codigo):
            tipo = input("Tipo: ")
            tipo = validardados.validar_tipo(tipo)
            quantidade = input("Quantidade: ")
            quantidade = validardados.validar_quantidade(quantidade)
            preco = input("Preço: ")
            preco = validardados.validar_preco(preco)
            manipulardados.inserir_produto(codigo, quantidade, preco, tipo)
        else:
            print("Produto já existe.")

        input("\nPressione qualquer tecla para continuar...")


    elif opcao == "2":
        limpar_ecra()
        print("*** Informação do Produto ***")
        codigo = input("Código: ")
        codigo = validardados.validar_codigo(codigo)
        produto = manipulardados.procurar_produto(codigo)
        if produto:
            manipulardados.imprimir_lista_produtos([list(produto)])
        else:
            print("Produto não encontrado.")

        input("\nPressione a tecla ENTER para continuar...")
    

    elif opcao == "3":
        limpar_ecra()
        print("*** Atualização de Produto ***")
        codigo = input("Código: ")
        codigo = validardados.validar_codigo(codigo)
        produto = manipulardados.procurar_produto(codigo)
        if produto:
            manipulardados.imprimir_lista_produtos([list(produto)])

            quantidade = input("Quantidade (novo): ")
            quantidade = validardados.validar_quantidade(quantidade)
            preco = input("Preço (novo): ")
            preco = validardados.validar_preco(preco)
            
            manipulardados.atualizar_produto(codigo, quantidade, preco)
        else:
            print("Produto não encontrado.")

        input("\nPressione a tecla ENTER para continuar...")


    elif opcao == "4":
        limpar_ecra()
        print("*** Lista de Produtos ***")
        manipulardados.listar_produtos()
        input("\nPressione a tecla ENTER para continuar...")


    elif opcao == "5":
        limpar_ecra()
        print("*** Remover Produto ***")
        codigo = input("Código: ")
        codigo = validardados.validar_codigo(codigo)
        produto = manipulardados.procurar_produto(codigo)
        if produto:
            manipulardados.imprimir_lista_produtos([list(produto)])
            confirmacao = input("Pretende prosseguir com a remoção do Produto? [S-Sim; Outra tecla - Cancelar]: ")
            if confirmacao.lower() == "s":
                manipulardados.apagar_produto(codigo)
            else:
                print("Operação de remoção cancelada.")
        else:
            print("Produto não encontrado.")

        input("\nPressione a tecla ENTER para continuar...")


    elif opcao.upper()=="S":
        limpar_ecra()
        print("Obrigado!")
        break #sai do ciclo while


    else:
        limpar_ecra()
        print("Opção inválida.")
        input("\nPressione a tecla ENTER para continuar...")