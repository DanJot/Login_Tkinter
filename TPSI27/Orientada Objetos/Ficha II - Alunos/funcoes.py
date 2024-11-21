from estudante import Estudante

Turma = []

def InserirEstudante():

    nome = input("Indique o nome do estudante: ")
    curso = input("Indique o curso que o aluno frequenta: ")
    nota = int(input("Indique a nota do aluno: "))
    situacao = input("Indique a situação final do aluno: ")

    novoEstudante = Estudante(nome, curso, nota, situacao)
    Turma.append(novoEstudante) #criação de lista  composta por objetos da classe estudante

    print("\n Infomação guardada com sucesso !")


def ListarEstudantes():

    if not Turma: # Se não existir aluno na listagem...
        print("\n Não existem alunos registados!")
    else:
        print(f"{"Nome":10} {"Curso":10} {"Nota":10} {"Situação Final":10}")
        for Estudante in Turma:
            Estudante.mostrarDados()


def ListarEstudanteEsp():
    if not Turma:
        print("\n Não existem alunos registados!")
    else:
        mostrar = False
        for Estudante in Turma:
            nome = input("Indique o nome do aluno: ")
            if Estudante.nome == nome:
                Estudante.mostrarDados()
                mostrar = True

        if not mostrar:
            print("Não existem alunos com esse nome para apresentar")

def RemoverEstudante():
    if not Turma:
        print("\n Não existem alunos registados!")
    else:
        encontrado = False
        nomeRemover = input("Indique o nome do Aluno a remover: ")
        for posicao, Estudante in enumerate(Turma):
            if Estudante.nome == nomeRemover:
                encontrado = True
                Turma.pop(posicao)
                print("Aluno removido com sucesso!")

        if not encontrado:
            print("O Aluno procurado não existe")

def ListarEstudanteAprovados():
    if not Turma:
        print("\n Não existem alunos registados!")
    else:
        mostrar = False
        for Estudante in Turma:
            if Estudante.situacao == "Aprovado":
                Estudante.mostrarDados()
                mostrar = True

        if not mostrar:
            print("Não existem alunos Aprovados para apresentar")

def AtualizarEstudante():
    encontrado = False
    nomeAtualizar = input("Indique o nome do Aluno a atualizar: ")
    for Estudante in Turma:
        if nomeAtualizar == Estudante.nome:
            encontrado = True
            novoCurso = input("Indique o novo curso do Aluno: ")
            Estudante.curso = novoCurso
            novaNota = int(input("Indique a nova nota do Aluno: "))
            Estudante.nota = novaNota
            novaSituacao = input("Indique a nova situacao do Aluno: ")
            Estudante.situacao = novaSituacao
            print("Aluno atualizado com sucesso!")

