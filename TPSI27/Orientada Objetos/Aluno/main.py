from aluno import Aluno
from aluno import Livro

nome = input("Refira o nome do aluno: ")
idade = int(input("Indique a idade do aluno: "))

novoAluno1 = Aluno(nome, idade) #Objeto novo aluno, que está presente na classe Aluno e tem os atributos x e y

novoAluno1.mostrarDados()



