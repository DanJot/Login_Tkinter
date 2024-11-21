from imoveis import Imoveis
from apartamento import Apartamento
from venda import Venda

baseDados = []

def InserirImovel():

    id = input("Indique o código do imóvel: ")

#Garantir que o código é unica:
    encontrada = False
    for dados in baseDados:
        if dados.getId() == id:
            print("\nEsse código já está registado!")
            encontrada = True
            break
    if not encontrada:

        valor = input("Indique o valor do imóvel: ")
        localidade = input("Indique a localidade do imóvel: ")
        tipologia = input("Indique a tipologia: ")
        tipoCasa = input("Indique o tipo de habitação (Moradia / Apartamento): ")
        if tipoCasa == "Apartamento":
            andar = input("Indique em que andar se situa o imóvel: ")
            valorCondominio = input("Indique o valor atual do condomínio: ")
            novoImovel = Apartamento(id, valor, localidade, tipologia, tipoCasa, "D", andar, valorCondominio)
            baseDados.append(novoImovel)
            print("Imovel inserido com sucesso !")
            return

        novoImovel = Imoveis(id, valor, localidade, tipologia, tipoCasa, "D")
        baseDados.append(novoImovel)
        print("Imovel inserido com sucesso !")



def ListarImoveisDisponiveis():

    if not baseDados:
        print("\nAinda não existem Imóveis criados")
    else:
        for dados in baseDados:
            if dados.getEstado() == "D":
                dados.mostrarDados()

def VenderImovel():

    if not baseDados:
        print("\nAinda não existem Imóveis criados!!")
    else:
        for dados in baseDados:
            dados.mostrarDados()

        vender = input("Indique o código do imóvel: ")

    #Garantir que o código existe e o estado está Disponivel
        encontrada = False
        for posicao, dados in enumerate (baseDados):
            if dados.getId() == vender and dados.getEstado() =="D":

                # dados.setEstado("V") altera o estado do carro
                dataVenda = input("Indique a data da venda: ")
                novaVenda = Venda(dados.getId(), dados.getValor(), dados.getLocalidade(), dados.getTipologia(), "V", dataVenda)
                baseDados[posicao] = novaVenda
                print("Venda efetuada com sucesso!")
                break

def ListarImoveisVendidos():

    if not baseDados:
        print("\nAinda não existem Imóveis criados")
    else:
        for dados in baseDados:
            if dados.getEstado() == "V":
                dados.mostrarDados()



def RemoverImovel():

    if not baseDados:
        print("\nAinda não existem Imóveis criados")
        return
    print("Imóveis Guardados:" + str(len(baseDados)) + "\n")
    for posicao, dados in enumerate(baseDados, start=1): #para a lista começar na posicao 1

        print(f"{posicao} {dados.getId()} {dados.getValor()} {dados.getLocalidade()} {dados.getTipologia()} {dados.getEstado()}")
    removeImovel = int(input("Indique a posição que pretende remover: "))

    if removeImovel > posicao: # confirmar que não introduz um numero maior que o numero de linhas da lista, podia ser também if removeCar > posicao :
        print("Essa posição está fora da listagem!")
    else:
        baseDados.pop(removeImovel-1)
        print("Imóvel removido com sucesso!")


def EditarImovel():

    if not baseDados:
        print("\nAinda não existem Imóveis criados")
        return

    ListarImoveisDisponiveis()

    editarImovel = input("Indique o código do imovel a editar: ")
    encontrar = False
    for dados in baseDados:
        if editarImovel == dados.getId():
            encontrar = True
            preco = input("Indique o novo valor do imóvel: ")
            dados.setPreco(preco)
            print("Dados atualizados com sucesso!")
            break
    if not encontrar:
        print("Essa matricula não está disponivel!")






## break é para os ciclos
## return é para os metodos



