from carro import Carro

class Venda(Carro):

    def __init__(self, marca, modelo, matricula, estado, preco, dataVenda):

        super().__init__(marca, modelo, matricula, estado) #tem acesso ao construtor da super classe Carro
        self.__preco = preco
        self.__dataVenda = dataVenda


    def getPreco(self):
        return self.__preco

    def getdataVenda(self):
        return self.__dataVenda

    def setPreco(self, preco):
        self.__preco = preco

    def setdataVenda(selfself, dataVenda):
        self.__dataVenda = dataVenda

    def mostrarDados(self):
        #super().mostrarDados()
        print(f"{self.getMarca()} {self.getModelo()} {self.getMatricula()} {self.getEstado()} {self.__preco} {self.__dataVenda}")
        # é o get para poder aceder ao conteudo privado da classe Carro
