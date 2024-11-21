from espetaculo import Espetaculo

baseDados = []

def CriarEspetaculo():
    nome = input("Refira o nome do espetaculo: ")
    capacidade = input("Refira a capacidade do espetaculo: ")

    novoEspetaculo = Espetaculo(nome, capacidade)
    baseDados.append(novoEspetaculo)

    print("\n Espetaculo criado om sucesso!\n")


def ListarEspetaculos():
    if not baseDados:
        print("Não existem espetáculos criados...\n")
    else:
        for espetaculos in baseDados:
            espetaculos.mostrarDados()


def ConsultarEspetaculo():
    if not baseDados:
        print("Não existem espetaculos criados!")
        return
    encontrado = False
    espetaculoConsultar = input("Indique o espetaculo que deseja consultar: ")
    for espetaculos in baseDados:
        if espetaculoConsultar == espetaculos.getNome():
            encontrado = True
            print("Nome: " + espetaculos.getNome())
            bilhetesVendidos = int(espetaculos.getCapacidadeMax()) - int(espetaculos.getCapacidade())
            print("Capacidade: " ,bilhetesVendidos)
            print("Capacidade Máxima: " ,espetaculos.getCapacidadeMax())
            break
    if not encontrado:
        print("\n Esse Espetáculo não existe!!\n")


def AtualizarEspetaculo():
    if not baseDados:
        print("Não existem espetaculos criados!")
        return
    encontrado = False
    nomeAtualizar = input("Indique o espetaculo que deseja atualizar: ")

    for espetaculos in baseDados:
        if nomeAtualizar == espetaculos.getNome():
            encontrado = True
            novoNome = input("Indique o novo nome: ")
            espetaculos.setNome(novoNome)
            print("Nome do espetaculo atualizado com sucesso!\n")
            break
    if not encontrado:
        print("\n Esse Espetáculo não existe!!\n")


def RemoverEspetaculo():
    if not baseDados:
        print("Não existem espetaculos criados!")
        return
    encontrado = False
    espetaculoRemover = input("Indique o espetaculo que deseja remover: ")
    for espetaculos in baseDados:
        if espetaculoRemover == espetaculos.getNome():
            encontrado = True
            baseDados.remove(espetaculos)
            print("Espetaculo removido com sucesso!\n")
            break
    if not encontrado:
        print("\n Esse Espetáculo não existe!!\n")


def Venderbilhetes():
    if not baseDados:
        print("Não existem espetaculos criados!")
        return

    encontrado = False
    espetaculoProcurar = input("Indique o espetaculo que pretende assistir: ")
    for espetaculos in baseDados:
        if espetaculoProcurar == espetaculos.getNome():
            encontrado = True
            quantidade = int(input("Indique quantos bilhetes deseja comprar: "))
            if espetaculos.verificarVenda(quantidade):
                print("Venda efetuada com sucesso!\n")
            else:
                print("Não existe disponibilidade para satisfazer o seu pedido\n")

        if not encontrado:
            print("\n Esse Espetáculo não existe!!\n")





