import validarMedicamentos
import manipulardadosMedicamentos
import manipulardadosVendas
def menu():
    print(" CINEL | 24H")
    print("1 - Adicionar Medicamentos")
    print("2 - Registar Venda")
    print("3 - Verificar Disponivilidade Medicamento")
    print("4 - Listar Medicamento - Nome")
    print("5 - Listar Vendas")
    print("6 - Remover Medicamento")
    print("7 - Atualizar Medicamento")
    print("8 - Fechar Aplicação\n")

while True:

    menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":

        codMedicamento = input("Insira o código do medicamento: ")
        codMedicamento = validarMedicamentos.ValidarCodigo(codMedicamento)

        quantidadeMedicamento = input("Insira a quantidade do medicamento: ")
        quantidadeMedicamento = validarMedicamentos.ValidarQuantidade(quantidadeMedicamento)

        precoMedicamento = input("Insira o preço do medicamento: ")
        precoMedicamento = validarMedicamentos.ValidarPreco(precoMedicamento)

        nomeMedicamento = input("Insira o nome do medicamento: ")
        nomeMedicamento = validarMedicamentos.ValidarNome(nomeMedicamento)

        manipulardadosMedicamentos.AdicionarMedicamento(codMedicamento, quantidadeMedicamento, precoMedicamento, nomeMedicamento)

    elif opcao == "2":
        
        codMedicamento = input("Insira o código do medicamento: ")
        codMedicamento = validarMedicamentos.ValidarCodigo(codMedicamento)

        quantidadeMedicamento = input("Insira a quantidade do medicamento: ")
        quantidadeMedicamento = validarMedicamentos.ValidarQuantidade(quantidadeMedicamento)
        
        manipulardadosVendas.RegistarVenda(codMedicamento, quantidadeMedicamento)

    elif opcao == "3":
        
        codMedicamento = input("Insira o código do medicamento: ")
        codMedicamento = validarMedicamentos.ValidarCodigo(codMedicamento)

        manipulardadosMedicamentos.VerificarDisponibilidade(codMedicamento)

    elif opcao == "4":

        manipulardadosMedicamentos.ListagemMedicamentosNomeCodigo()

    elif opcao == "5":

        manipulardadosVendas.ListarVendas()

    elif opcao == "6":
        
        codMedicamento = input("Insira o código do medicamento: ")
        codMedicamento = validarMedicamentos.ValidarCodigo(codMedicamento)

        manipulardadosMedicamentos.RemoverMedicamento(codMedicamento)

    elif opcao == "7":
        
        codMedicamento = input("Insira o código do medicamento: ")
        codMedicamento = validarMedicamentos.ValidarCodigo(codMedicamento)

        manipulardadosMedicamentos.AtualizarMedicamento(codMedicamento)

    elif opcao == "8":
        print("\nObrigado pela sua colaboração !!\n")
        break
    else:
        print("\nOpção Inválida\n")
