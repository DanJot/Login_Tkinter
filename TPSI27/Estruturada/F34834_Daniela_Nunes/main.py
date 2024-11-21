import validar_veiculos
import manipulardadosVeiculos
import validar_registos
import manipulardadosregistos

CLASSES = ["A", "B", "C"]

def menu():
    print("  CINEL VERDE SA")
    print("1. Registar Veículo")
    print("2. Remover Veículo")
    print("3. Registar Passagem")
    print("4. Exibir Informações do Veículo")
    print("5. Listar Passagens por Data")
    print("6. Recarregar Saldo")
    print("7. Sair")

while True:

    menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        matricula = input("Insira a matricula do veiculo: ")
        matricula = validar_veiculos.ValidarMatricula(matricula)

        classe = input("Introduza a classe do veículo (A, B, ou C): ")
        while classe not in CLASSES:
            classe = input("Classe inválida. Introduza novamente a classe (A, B, ou C): ")

        saldo = input("Introduza o saldo inicial da Via Verde (número positivo ou zero): ")
        saldo = validar_veiculos.ValidarSaldo(saldo)

        manipulardadosVeiculos.AdicionarVeiculo(matricula, classe, saldo)

    elif opcao == "2":
        matricula = input("Insira a matricula do veiculo a remover: ")
        matricula = validar_veiculos.ValidarMatricula(matricula)
        manipulardadosVeiculos.RemoverVeiculo(matricula)

    # NÃO CONSEGUI ACABAR
    #elif opcao == "3":
            #matricula = input("Insira a matricula do veiculo: ")
            #matricula = validar_veiculos.ValidarMatricula(matricula)

            #numpassagem = input("Insira a quantidade de passagens: ")
            #numpassagem = validar_registos.ValidarPassagem(numpassagem)

            #data = validar_registos.ValidarDataPassagem()

            #classe = input("\nIndique a classe do veiculo: ")

            #manipulardadosregistos.RegistarPassagem(numpassagem, matricula, data.strftime('%d/%m/%Y'), valor)

    elif opcao == "4":
        manipulardadosVeiculos.ListarVeiculos()

    elif opcao == "5":#NÃO CONSEGUI ACABAR
        pass

    elif opcao == "6":
        matricula = input("Insira a matricula do veiculo: ")
        matricula = validar_veiculos.ValidarMatricula(matricula)

        manipulardadosVeiculos.RecarregarSaldo(matricula)

    elif opcao == "7":
        print("\nObrigado e até à próxima !!\n")
        break

    else:
        print("\nOpção Inválida\n")