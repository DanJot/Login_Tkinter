class Video:

    def __init__(self, titulo, duracao, ano, classificacao):
        self.titulo = titulo #atributo da classe
        self.duracao = duracao
        self.ano = ano
        self.classificacao = classificacao


    def mostrarDados(self):

        print(f"{self.titulo:10} {self.duracao:11} {self.ano:12} {self.classificacao:15}\n")
