class Imoveis:

    def __init__(self, id, valor, localidade, tipologia, tipoCasa, estado):
        self.__id = id
        self.__valor = valor
        self.__localidade = localidade
        self.__tipologia = tipologia
        self.__tipoCasa = tipoCasa
        self.__estado = estado

    def getId(self):
        return self.__id

    def getValor(self):
        return self.__valor

    def getLocalidade(self):
        return self.__localidade

    def getTipologia(self):
        return self.__tipologia

    def getTipoCasa(self):
        return self.__tipoCasa

    def getEstado(self):
        return self.__estado

    def setId(self, id):
        self.__id = id

    def setValor(self, valor):
        self.__valor = valor

    def setLocalidade(self, localidade):
        self.__localidade = localidade

    def setTipologia(self, tipologia):
        self.__tipologia = tipologia

    def setTipologia(self, tipoCasa):
        self.__tipoCasa = tipoCasa

    def setEstado(self, estado):
        self.__estado = estado

    def mostrarDados(self):
        print(f"{self.__id} {self.__valor} {self.__localidade} {self.__tipologia} {self.__tipoCasa} {self.__estado}")

