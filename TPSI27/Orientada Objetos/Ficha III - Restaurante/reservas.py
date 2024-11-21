

class Reserva:
    def __init__(self, nome, contacto, data, hora, npessoas):
        self.__nome = nome          # __ é para tornar os atributos privados
        self.__contacto = contacto
        self.__data = data
        self.__hora = hora
        self.__npessoas = npessoas

    def getNome(self):
        return self.__nome

    def getContacto(self):
        return self.__contacto

    def getData(self):
        return self.__data

    def getHora(self):
        return self.__hora

    def getNpessoas(self):
        return self.__npessoas

    # set é para alterar o conteudo
    def setHora(self, hora):
        self.__hora = hora

    def setNpessoas(self, npessoas):
        self.__npessoas = npessoas

    def mostrarDados(self):
        print(f"\n{self.__nome} {self.__contacto} {self.__data} {self.__hora} {self.__npessoas}\n")


