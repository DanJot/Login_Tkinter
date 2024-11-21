from evento import *

class Espetaculo:
    def __init__(self, nome, capacidade):
        self.__nome = nome          # __ é para tornar os atributos privados
        self.__capacidade = capacidade
        self.__capacidadeMax = capacidade


    def getNome(self):
        return self.__nome

    def getCapacidade(self):
        return self.__capacidade

    def getCapacidadeMax(self):
        return self.__capacidadeMax

    def setNome(self, nome):   #set é para alterar o conteudo
        self.__nome = nome

    def setCapacidade(self, capacidade):
        self.__capacidade = capacidade

    def setCapacidadeMax(self, capacidadeMax):
        self.__capacidadeMax = capacidadeMax

    def verificarVenda(self, quantidade):
    # verificar se a quantidade desejada é maior que a capacidade disponivel
        if int(quantidade) > int(self.__capacidade):
            return False
        else:
            self.__capacidade = int(self.__capacidade) - int(quantidade)
            return True

        
    def mostrarDados(self):
        print(f"\n{self.__nome} {self.__capacidade} {self.__capacidadeMax}\n")


