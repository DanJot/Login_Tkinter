import os


# Definição de Funções

def limpar_ecra():
    # Verifica o sistema operacional e usa o comando apropriado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux e macOS
        os.system('clear')



def mostrar_menu():
    print("")
    print("--- MENU ---")
    print("1. Inserir Alunos e suas Notas")
    print("2. Listar Dados")
    print("3. Listar Dados por ordem alfabética (ascendente)")
    print("4. Listar Dados pela nota média obtida (descendente)")
    print("5. Aluno com maior Nota Média")
    print("0. Sair")



def inserir_alunos():
    limpar_ecra()

    numero = int(input("Quantidade de Alunos a inserir : "))

    for i in range(numero):
        nome = input("Nome: ")  
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))       
        alunos.append((nome, nota1, nota2))


def listar_alunos():
    limpar_ecra()

    if alunos:
        print("Lista de Alunos")
        for aluno in alunos:       
             media = (aluno[1] + aluno[2]) / 2 # Calcula a média
             resultado = "Aprovado" if media >= 9.5 else "Não aprovado" # Define o resultado com base na média
             print(f" Nome: {aluno[0]}; Nota 1: {aluno[1]}; Nota 2: {aluno[2]}; Média: {(aluno[1] + aluno[2])/2}; Resultado: {resultado}")
    else:
        print("Não existem Alunos inseridos.")


def listar_alunos_ord_nome_asc():
    limpar_ecra()

    if alunos:
        print("Lista de Alunos ordenada pelo Nome do Aluno (ascendente)")
        for aluno in sorted(alunos, key= lambda x: x[0]):       
             media = (aluno[1] + aluno[2]) / 2 # Calcula a média
             resultado = "Aprovado" if media >= 9.5 else "Não aprovado" # Define o resultado com base na média
             print(f" Nome: {aluno[0]}; Nota 1: {aluno[1]}; Nota 2: {aluno[2]}; Média: {(aluno[1] + aluno[2])/2}; Resultado: {resultado}")
    else:
        print("Não existem Alunos inseridos.")


def listar_alunos_ord_media_desc():
    limpar_ecra()

    if alunos:
        print("Lista de Alunos ordenada pela Nota Média (descendente)")
        for aluno in sorted(alunos, key= lambda x: (x[1] + x[2]) / 2, reverse=True):       
             media = (aluno[1] + aluno[2]) / 2 # Calcula a média
             resultado = "Aprovado" if media >= 9.5 else "Não aprovado" # Define o resultado com base na média
             print(f" Nome: {aluno[0]}; Nota 1: {aluno[1]}; Nota 2: {aluno[2]}; Média: {(aluno[1] + aluno[2])/2}; Resultado: {resultado}")
    else:
        print("Não existem Alunos inseridos.")


def aluno_com_maior_media():
    limpar_ecra()
    
    if alunos:
        # Usa max() com uma key personalizada para encontrar o aluno com a maior média
        aluno_maior_media = max(alunos, key=lambda x: (x[1] + x[2]) / 2)
        print("Aluno com maior Nota Média")
        print(f"Nome: {aluno_maior_media[0]}")
    else:
        print("Não existem Alunos inseridos.")
   

# Main Program
alunos=[]

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        inserir_alunos()

    elif opcao == "2":
        listar_alunos()
    
    elif opcao == "3":
        listar_alunos_ord_nome_asc()

    elif opcao == "4":
        listar_alunos_ord_media_desc()

    elif opcao == "5":
        aluno_com_maior_media()

    elif opcao=="0":
        print("Obrigado!")
        break #sai do ciclo while
    else:
        print("opção inválida.")