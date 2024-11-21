from os import remove

from carro import Carro
from venda import Venda

baseDados = []

def InserirCarro():

    matricula = input("Indique a matricula do carro: ")

#Garantir que a matricula é unica:
    encontrada = False
    for dados in baseDados:
        if dados.getMatricula() == matricula:
            print("\nEssa matricula já está registada!")
            encontrada = True
            break
    if not encontrada:

        marca = input("Indique a marca do carro: ")
        modelo = input("Indique o modelo do carro: ")

        novoCarro = Carro(marca, modelo, matricula, "D")
        baseDados.append(novoCarro)
        print("Carro inserido com sucesso !")


def ListarCarrosDisponiveis():

    if not baseDados:
        print("\nAinda não existem Carros criados")
    else:
        for dados in baseDados:
            if dados.getEstado() == "D":
                dados.mostrarDados()


def VenderCarro():

    if not baseDados:
        print("Ainda não existem carros criados!")
    else:
        for dados in baseDados:
            dados.mostrarDados()

        vender = input("Indique a matricula do carro: ")

    #Garantir que a matricula existe e o estado está Disponivel
        encontrada = False
        for posicao, dados in enumerate (baseDados):
            if dados.getMatricula() == vender and dados.getEstado() =="D":

                # dados.setEstado("V") altera o estado do carro
                preco = input("Indique o preço de venda: ")
                dataVenda = input("Indique a data da venda: ")
                novaVenda = Venda(dados.getMarca(), dados.getModelo(), dados.getMatricula(), "V", preco, dataVenda)
                baseDados[posicao] = novaVenda
                print("Venda efetuada com sucesso!")
                break

def ListarCarrosVendidos():

    if not baseDados:
        print("\nAinda não existem Carros criados")
    else:
        for dados in baseDados:
            if dados.getEstado() == "V":
                dados.mostrarDados()



def RemoverCarro():

    if not baseDados:
        print("\n Ainda não existem carros criados!")
        return
    print("Carros Guardados:" + str(len(baseDados)) + "\n")
    for posicao, dados in enumerate(baseDados, start=1): #para a lista começar na posicao 1

        print(f"{posicao} {dados.getMatricula()} {dados.getMarca()} {dados.getModelo()} {dados.getEstado()}")

    removeCar = int(input("Indique a posição que pretende remover: "))

    if removeCar > len(baseDados): # confirmar que não introduz um numero maior que o numero de linhas da lista, podia ser também if removeCar > posicao :
        print("Essa posição está fora da listagem!")
    else:
        baseDados.pop(removeCar-1)
        print("Carro removido com sucesso!")


def EditarCarro():

    if not baseDados:
        print("\n Ainda não existem carros criados!")
        return

    print("--- Editar Carro ---")
    print("1 - Editar carros Disponiveis")
    print("2 - Editar carros Vendidos")
    opcao = input("Indique a sua opção: ")

    match opcao:
        case "1":
            EditarCarroD()
        case _:
            print("Opção Inválida")


def EditarCarroD():

    ListarCarrosDisponiveis()

    editarCarro = input("Indique a matricula a editar: ")
    encontrar = False
    for dados in baseDados:
        if editarCarro == dados.getMatricula():
            encontrar = True
            marca = input("Indique a nova marca: ")
            modelo = input("Indique o novo modelo: ")
            dados.setMarca(marca)
            dados.setModelo(modelo)
            print("Dados atualizados com sucesso!")
            break
    if not encontrar:
        print("Essa matricula não está disponivel!")









## break é para os ciclos
## return é para os metodos



