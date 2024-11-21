class Quarto:

    def __init__(self, numero, preco, status):
            self.__numero = numero
            self.__preco = preco
            self.__status = status

    def getNumero(self):
        return self.__numero

    def getPreco(self):
        return self.__preco

    def getStatus(self):
        return self.__status

    def setNumero(self, numero):
        self.__numero = numero

    def setPreco(self, preco):
        self.__preco = preco

    def setStatus(self, status):
        self.__status = status

    def mostrarDados(self):
        print(f"{self.__numero} {self.__preco} {self.__status}")
