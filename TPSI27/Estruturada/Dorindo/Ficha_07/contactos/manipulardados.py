# importar modulos
import os

nome_ficheiro="contactos.txt"

# definição de Funções

def criar_ficheiro_se_nao_existe():
    # Verifica se o ficheiro existe
    if not os.path.exists(nome_ficheiro):
        # Se não existir, cria um ficheiro vazio
        with open(nome_ficheiro, 'w') as file:
            pass  # 'pass' significa que não fazemos nada (ficheiro vazio)
        print(f"Ficheiro '{nome_ficheiro}' criado.")
    else:
        print(f"Ficheiro '{nome_ficheiro}' já existe.")


def existe_contacto(telefoneContacto):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            dados = linha.strip().split(";")
            if telefoneContacto == dados[1]:
                return True
        return False


def inserir_contacto(nomeContacto, telefoneContacto, emailContacto):
    if not existe_contacto(nomeContacto):
        with open(nome_ficheiro, 'a', encoding="UTF-8") as ficheiro:
            novalinha = f"{nomeContacto};{telefoneContacto};{emailContacto}\n"
            ficheiro.write(novalinha)
        print("Contacto inserido com sucesso!")
    else:
        print("Contacto já existe")


def procurar_contacto(telefoneContacto):
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            contacto = linha.strip().split(";")
            if telefoneContacto == contacto[1]:
                return (contacto[0], contacto[1], contacto[2]) 
    return None


def atualizar_contacto(nomeContacto, telefoneContacto, emailContacto):
    if existe_contacto(telefoneContacto):
        #Atualiza
        with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
            linhas = ficheiro.readlines()
            for pos, linha in enumerate(linhas):
                contacto = linha.strip().split(";")
                
                if telefoneContacto == contacto[1]:
                    linhas[pos] = f"{nomeContacto};{telefoneContacto};{emailContacto}\n"
                    break

    
        with open(nome_ficheiro, 'w', encoding="UTF-8") as ficheiro:
            ficheiro.writelines(linhas)

        print("Contacto atualizado com sucesso!")

    else:
         print("Contacto não encontrado.")


def apagar_contacto(telefoneContacto):
    if existe_contacto(telefoneContacto):
        #Atualiza
        with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
            linhas = ficheiro.readlines()
            for pos, linha in enumerate(linhas):
                contacto = linha.strip().split(";")
                
                if telefoneContacto == contacto[1]:
                    linhas.pop(pos)
                    break

    
        with open(nome_ficheiro, 'w', encoding="UTF-8") as ficheiro:
            ficheiro.writelines(linhas)

        print("Contacto apagado com sucesso!")

    else:
        print("Contacto não encontrado.")


def listar_contactos():
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas:
            contacto = linha.strip().split(";")
            print(f"{contacto[0]} - {contacto[1]} - {contacto[2]}")

        if not linhas:
            print("Não existem registos de Contactos.")

        #listaContatos = [linha.strip().split(";") for linha in ficheiro.readlines()]


def listar_contactos_ordNome_asc():
    with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
        listaContactos = [linha.strip().split(";") for linha in ficheiro.readlines()]

    #listaContactosOrdenados = sorted(listaContactos, key= lambda x: x[0] )
    for contacto in sorted(listaContactos, key= lambda x: x[0] ):
        print(f"{contacto[0]} - {contacto[1]} - {contacto[2]}")
         

