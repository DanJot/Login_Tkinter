# 28. Elabora um programa que solicite ao utilizador o nome e a idade de N utilizadores. 
# No fim deve apresentar toda a informação de forma organizada e 
# indicar qual foi o utilizador mais velho inserido.


def mostrar_menu():
    print("")
    print("--- MENU ---")
    print("1. Inserir Utilizador")
    print("S. Apresentar dados e Sair")

def listar_utilizadores():
    if utilizadores:
        print("\nLista de utilizadores")
        for utilizador in utilizadores:
            print(f"Nome: {utilizador[0]} ; Idade: {utilizador[1]}")

    else:
        print("Sem utilizadores registados.")



# main program
utilizadores = []


while(True):
    mostrar_menu()
    opcao = input("Indique a sua opção: ") 

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        utilizadores.append((nome, idade)) 

    elif opcao.upper() =="S":
        #print("Obrigado!")
        break #sai do ciclo while
    else:
        print("opção inválida.")
        


listar_utilizadores()
if utilizadores:
    # Idade da pessoa mais velha
    listaIdades = [utilizador[1] for utilizador in utilizadores]
    maxIdade = max(listaIdades)
    print(f"Idade do utilizador mais velho: {maxIdade}")