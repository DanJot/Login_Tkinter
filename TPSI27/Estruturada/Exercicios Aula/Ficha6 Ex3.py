def menu():
    print("--------MENU------")
    print("1 - Listar todos os formandos")
    print("2 - Inserir formando")
    print("3 - Procurar formando")
    print("4 - Atualizar dados de um formando")
    print("5 - Eliminar um aluno")
    print("6 - Sair")

def opcao_1():     #Listar todos os formandos
    with open("../CINEL.txt", "r", encoding="UTF-8") as ficheiro:
        print(f"{'Nome':<10} {'Num':<5} {'Cidade':<5}")
        for linha in ficheiro:
           dados = linha.strip().split(";")
           print(f"{dados[0]:<10} {dados[1]:<5} {dados[2]:<10}")

def opcao_2(): #Inserir alunos mas não pode ter o mesmo nome
     nome = input("Qual o nome do aluno que gostaria de inserir: ")
     existe = False
     with open("../CINEL.txt", "r", encoding="UTF-8") as ficheiro:
        for linha in ficheiro:
            dados = linha.strip().split(";")
            if nome == dados[0]:
                print("Esse nome já existe!")
                existir = True
     if not existe:
         num = int(input("Qual o numero do formando: "))
         cidade = input("Qual a cidade do formando: ")
         dado = f"{nome};{num};{cidade}"
         print("Dados Atualizados!")
         with open("../CINEL.txt", "a", encoding="UTF-8") as ficheiro:
             ficheiro.write(dado)


def opcao_3(): #Procurar formando
    procurarnome= input("Qual o nome do aluno que pretende encontrar: ")
    existe = False
    with open("../CINEL.txt", "r", encoding="UTF-8") as ficheiro:
        for linha in ficheiro:
            dados = linha.strip().split(";")
            if procurarnome == dados[0]:
                print(f"{'Nome':<10} {'Num':<5} {'Cidade':<5}")
                print(f"{dados[0]:<10} {dados[1]:<5} {dados[2]:<10}")
                existe = True
    if not existe:
        print("Com esse nome não existe nenhum aluno!")

def opcao_4(): #Atualizar um aluno
    nome = input("Qual o nome do formando que pretende alterar: ")
    existe = False
    with open("../CINEL.txt", "r", encoding="UTF-8") as ficheiro:
        lista = ficheiro.readlines()
        for posicao,linha in enumerate(lista):
            dados = linha.strip().split(";")
            if nome == dados[0]:
                novonumero = int(input("Qual o novo numero do formando: "))
                novacidade = input("Qual a nova cidade do formando: ")
                existe = True
                print("Dados atualizados")
                lista[posicao] = f"{nome};{novonumero};{novacidade}\n"
            with open("../CINEL.txt", "w", encoding="UTF-8") as ficheiro:
                ficheiro.writelines(lista)
    if not existe:
        print("Nome Invalido!2")

def opcao_5(): #Eliminar um aluno
    nome = input("Qual o nome do formando que pretende alterar: ")
    existe = False
    with open("../CINEL.txt", "r", encoding="UTF-8") as ficheiro:
        lista = ficheiro.readlines()
        for posicao,linha in enumerate(lista):
            dados = linha.strip().split(";")
            if nome == dados[0]:
               lista.pop(posicao)
               existe = True
               print("Dados apagados")
               with open("../CINEL.txt", "w", encoding="UTF-8") as ficheiro:
                   ficheiro.writelines(lista)
    if not existe:
        print("Nome invalido!")

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        opcao_1()
    elif opcao == "2":
        opcao_2()
    elif opcao == "3":
        opcao_3()
    elif opcao == "4":
        opcao_4()
    elif opcao == "5":
        opcao_5()
    elif opcao == "6":
        print("Obrigado!")
        break