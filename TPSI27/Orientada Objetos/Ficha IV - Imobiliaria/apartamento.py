from imoveis import Imoveis

class Apartamento(Imoveis):

    def __init__(self, id, valor, localidade, tipologia, tipoCasa, estado, andar, valorCondominio):

        super().__init__(id, valor, localidade, tipologia, tipoCasa, estado)
        self.__andar = andar
        self.__valorCondominio = valorCondominio

    def getAndar(self):
        return self.__andar


    def getValorCondominio(self):
        return self.__valorCondominio


    def setAndar(self, andar):
        self.__andar = andar


    def setValorCondominio(self, valorCondominio):
        self.__valorCondominio = valorCondominio


    def mostrarDados(self):
        # super().mostrarDados()
        print(f"{self.__id} {self.__valor} {self.__localidade} {self.__tipologia} {self.__tipoCasa} {self.__estado} {self.__andar} {self.__valorCondominio}")
        # é o get para poder aceder ao conteudo privado da classe Imoveis