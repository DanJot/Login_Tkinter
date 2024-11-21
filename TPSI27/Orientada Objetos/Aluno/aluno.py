class Aluno: #criação da classe - é constituido por atributos do aluno

    def __init__(self, nome, idade): #metodo construtor para inicializar as variaveis
        self.nome = nome
        self.idade = idade



    def mostrarDados(self):
        print(f"Nome:{self.nome}\nIdade:{self.idade}")


