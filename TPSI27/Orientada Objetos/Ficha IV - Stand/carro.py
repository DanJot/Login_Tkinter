class Carro:

    def __init__(self, marca, modelo, matricula, estado):

        self.__marca = marca
        self.__modelo = modelo
        self.__matricula = matricula
        self.__estado = estado

    def getMarca(self):
       return self.__marca

    def getModelo(self):
        return self.__modelo

    def getMatricula(self):
        return self.__matricula

    def getEstado(self):
        return self.__estado

    def setMarca(self, marca):
        self.__marca = marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def setEstado(self, estado):
        self.__estado = estado

    def mostrarDados(self):
        print(f"{self.__marca} {self.__modelo} {self.__matricula} {self.__estado}")

        