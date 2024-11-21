###BIBLIOTECAS

##FUNÇÕES
def lclientes():
    cursor = con.cursor()
    sql = "select * from utilizador order by firstname;"
    cursor.execute(sql)
    dados = cursor.fetchall()
    cursor.close()

    for pessoa in dados:
        #print(pessoa) #(4, 'Ferreira', 'Francisco', 'Aveiro', 'Esgueira')
        nome = pessoa[2] + " " + pessoa[1] #Franciso Ferreira
        print(nome)

    return


def lcidades():
    cursor = con.cursor()
    sql = "select DISTINCT cidade from utilizador order by cidade;"
    cursor.execute(sql)
    dados = cursor.fetchall()
    print(dados)
    cursor.close()

def numpessoas():
    cursor = con.cursor()
    sql = "select cidade, count(firstname) from utilizador group by cidade" #o count podia ser por qualquer campo
    cursor.execute(sql)
    dados = cursor.fetchall()
    print("Nº de Pessoas\t Nome cidade")
    for elem in dados: #[(cidade1, qt1)...]
        #elem -> (cidade1, qt1)
        print(f"{elem[1]:^13}\t\t{elem[0]}") # ^ Alinha ao centro o elemento 1
    cursor.close()


def inserir():
    #tabela utilizador(id,lastname,firstname,cidade,freguesia)
    apelido = input("Apelido?")
    nome = input("Nome?")
    cid = input("Cidade?")
    freg = input("Freguesia?")
    sql = "insert into utilizador(lastname,firstname,cidade,freguesia) values (?,?,?,?);"
    valores = (apelido,nome,cid,freg)
    cursor = con.cursor()
    cursor.execute(sql, valores)
    con.commit()  # gravar a informação no SQL
    cursor.close()

def atualizar():
    sql = "select * from utilizador;"
    cursor = con.cursor()
    cursor.execute(sql)
    dados = cursor.fetchall()
    print("Dados dos utilizadores:\nID\tApelido\tNome\tCidade\tFreguesia")
    for pessoa in dados:
        print(f"{pessoa[0]}\t{pessoa[1]}\t{pessoa[2]}\t{pessoa[3]}\t{pessoa[4]}")

    id = int(input("Qual o ID do utilizador que pretende atualizar?"))
    #obter os dados do que queremos atualizar
    sql = f"select * from utilizador where id = {id}"
    cursor.execute(sql)
    dados = cursor.fetchone() #apenas uma tupla com os dados da pessoa
    dados = list(dados) #converte tupla para lista
    for ind, elem in enumerate(dados):
        op = input(f"{elem}: mantém (s/n)?")
        if op =="n":
            novo = input("Qual a palavra a substituir?")
            dados[ind] = novo

    sql = f"update utilizador set lastname = ?, firstname = ?, cidade = ?, freguesia = ? where id = {id}"
    cursor.execute(sql, dados)
    con.commit(sql)
    print("Dados atualizados com sucesso!")
    cursor.close()

def remover():
    pass

################################

import ligacao as liga
con = liga.conexao()
if con:
    while True:
        print("\n1 - Listar clientes")
        print("2 - Listar cidades")
        print("3 - Num. de pessoas por cidade")
        print("4 - Inserir novo cliente")
        print("5 - Atualizar dados do cliente")
        print("6 - Remover cliente")
        print("0 - Sair")

        op = int(input("Indique a sua escolha: "))
        match op:
            case 1:
                lclientes()
            case 2:
                lcidades()
            case 3:
                numpessoas()
            case 4:
                inserir()
            case 5:
                atualizar()
            case 6:
                remover()
            case 0:
                print("Foi um gosto.\nVolte sempre")
                break #pára o ciclo
        input("Carregue «Enter» para continuar...")

else:
    print("Não foi possível establecer conexão.\n"
          "Verifique as credenciais...")