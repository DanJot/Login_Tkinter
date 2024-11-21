

def mostrar_menu():
    print("")
    print("--- MENU ---")
    print("1. Inserir Resultados do Atleta")
    print("2. Apresentar Resultados")
    print("0. Sair")


def inserir_atleta():
    nome = input("Atleta: ")    
    saltos=[]
    for j in range(5):
        salto = float(input(f"Salto {j+1}: ?"))
        saltos.append(salto)
    
    atletas.append((nome,saltos))


def apresentar_resultados():
    print("\nResultado final")
    for atleta in atletas:
        print()
        print(f"Atleta: {atleta[0]}")
        print("Saltos: " + " - ".join(map(str, atleta[1])))





atletas=[]


while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        inserir_atleta()

    elif opcao == "2":
        apresentar_resultados()

    elif opcao=="0":
        print("Obrigado!")
        break #sai do ciclo while
    else:
        print("opção inválida.")


