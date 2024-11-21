# 5.	O Comité Olímpico Internacional (COI) teve que informatizar toda a informação
# referente os diversos atletas que participam nos Jogos Olímpicos de França. Nesse sentido
# elabore um programa que permita guardar a seguinte informação de cada atleta.
# O COI pretende guardar o número único atribuído a cada atleta, o nome do atleta, a
# competição em que participa (admita que só pode participar numa competição) e a federação a
# que pertence. É importante também garantir que existe a possibilidade de listar os atletas por competição
# e federação. Garanta ainda que as listagens dos atletas são sempre feitas em função do número atribuído ao dorsal.

atletas = []


def mostrar_menu():  # Definir a função
    print("")
    print("--- MENU ---")
    print("1. Inserir Atleta")
    print("2. Consultar Atleta por código")
    print("3. Listar todos os Atletas")
    print("4. Listar por federação")
    print("5. Listar por competição")
    print("6. Sair")


def opcao1():
    codigoAtleta = int(input("Indique o código do Atleta:"))
    procurar = False
    for atleta in atletas:
        if codigoAtleta == atleta[0]:
            print("O código já existe")
            procurar = True

    if not procurar:
        nome = input("Indique o nome do Atleta: ")
        competicao = input("Indique a competição: ")
        federacao = input("Indique a federação:")

        atletas.append((codigoAtleta, nome, competicao, federacao))
        print("Atleta guardado com sucesso!")


def opcao2():
    procurarcodigo = int(input("Indique o código do atleta a pesquisar:"))
    procurar = False
    for atleta in atletas:
        if procurarcodigo == atleta[0]:
            print("O atleta existe e tem a seguinte informação:")
            print("Código:", atleta[0], " | Nome:", atleta[1], " | Competição:", atleta[2], " | Federação:", atleta[3])
            procurar = True
        if not procurar:
            print("O atleta não existe!")


def opcao3():
    print(f" {'Código': <7} {'Nome': <7} {'Competição': <7} {'Federação': <7}")
    for codigoAtleta, nome, competicao, federacao in atletas:
        print(f" {codigoAtleta:<7} {nome:<8} {competicao:<9} {federacao:<9}")


def opcao4():
    federacao_selecionada = input("Indique a Federação para listar os atletas: ")
    print(f" {'Código': <7} {'Nome': <7} {'Competição': <7} {'Federação': <7}")
    for codigoAtleta, nome, competicao, federacao in atletas:
        if federacao == federacao_selecionada:
            print(f" {codigoAtleta:<7} {nome:<8} {competicao:<9} {federacao:<9}")


def opcao5():
    competicao_selecionada = input("Indique a competição para listar os atletas: ")
    print(f" {'Código': <7} {'Nome': <7} {'Competição': <7} {'Federação': <7}")
    for codigoAtleta, nome, competicao, federacao in atletas:
        if competicao == competicao_selecionada:
            print(f" {codigoAtleta:<7} {nome:<8} {competicao:<9} {federacao:<9}")


while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        opcao1()
    elif opcao == "2":
        opcao2()
    elif opcao == "3":
        opcao3()
    elif opcao == "4":
        opcao4()
    elif opcao == "5":
        opcao5()
    elif opcao == "6":
        print("Obrigado !")
        break
    else:
        print("Opção inválida")
