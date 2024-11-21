class Estudante:

    def __init__(self, nome, curso, nota, situacao):
        self.nome = nome #atributo da classe
        self.curso = curso
        self.nota = nota
        self.situacao = situacao


    def mostrarDados(self):

        print(f"{self.nome:10} {self.curso:5} {self.nota:10} {self.situacao:10}\n")

