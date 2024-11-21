from imoveis import Imoveis

class Venda(Imoveis):

    def __init__(self, id, valor, localidade, tipologia, tipoCasa, estado, dataVenda):

        super().__init__(id, valor, localidade, tipologia, tipoCasa, estado)
        self.__dataVenda = dataVenda


    def getdataVenda(self):
        return self.__dataVenda

    def setdataVenda(selfself, dataVenda):
        self.__dataVenda = dataVenda

    def mostrarDados(self):
        #super().mostrarDados()
        print(f"{self.__id} {self.__valor} {self.__localidade} {self.__tipologia} {self.__tipoCasa} {self.__estado} {self.__dataVenda}")
