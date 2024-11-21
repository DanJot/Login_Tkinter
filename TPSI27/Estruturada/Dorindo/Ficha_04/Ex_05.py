
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
    print("1. Inserir Atleta")
    print("2. Listar Atletas")
    print("3. Listar Atletas por Competição")
    print("4. Listar Atletas por Federação")
    print("0. Sair")



def existe_numero(numero):
    # Verifica se a lista 'atletas' não está vazia
    if atletas and numero in atletas[0]:
        return True   
    return False


def inserir_atleta():
    limpar_ecra()

    print("Insira os dados do Atleta")
    numero = int(input("Número: "))

    if not existe_numero(numero):
        nome = input("Nome: ")  
        competicao = input("Competição: ")
        federacao = input("Federação: ")        
        atletas.append((numero, nome, competicao, federacao))
    else:
        print("O Número já existe. Não é possível inserir.")    


def listar_atletas():
    limpar_ecra()

    # cria nova lista de atletas orenada pelo numero (coluna 0)
    #nova = sorted(atletas, key= lambda x : x[0])

    if atletas:
        print("Lista de Atletas")
        for atleta in sorted(atletas, key= lambda x : x[0]):
            print(f"Numero: {atleta[0]}; Nome: {atleta[1]}; Competição: {atleta[2]}; Federação: {atleta[3]};")

    else:
        print("Não existem Atletas inscritos.")



def listar_atletas_competicao(competicao: str):
    limpar_ecra()

    novalista = [atleta for atleta in atletas if competicao.lower() in atleta[2].lower() ]
    if novalista:
        print("Lista de Atletas por Competição")
        for atleta in sorted(novalista, key= lambda x : x[0]):
            print(f"Numero: {atleta[0]}; Nome: {atleta[1]}; Competição: {atleta[2]}; Federação: {atleta[3]};")
    else:
        print("Não existem Atletas inscritos nesta Competição.")



def listar_atletas_federacao(federacao: str):
    limpar_ecra()

    novalista = [atleta for atleta in atletas if federacao.lower() in atleta[3].lower() ]
    if novalista:
        print("Lista de Atletas por Federação")       
        for atleta in sorted(novalista, key= lambda x : x[0]):
            print(f"Numero: {atleta[0]}; Nome: {atleta[1]}; Competição: {atleta[2]}; Federação: {atleta[3]};")
    
    else: 
        print("Não existem Atletas inscritos através desta Federação.")



# Main Program
atletas=[]

while True:
    mostrar_menu()
    opcao = input("Indique a sua opção: ")

    if opcao == "1":
        inserir_atleta()

    elif opcao == "2":
        listar_atletas()
    
    elif opcao == "3":
        competicao = input("Indique a Competição a pesquisar: ")
        listar_atletas_competicao(competicao)

    elif opcao == "4":
        federacao = input("Indique a Federação a pesquisar: ")
        listar_atletas_federacao(federacao)

    elif opcao=="0":
        print("Obrigado!")
        break #sai do ciclo while
    else:
        print("opção inválida.")