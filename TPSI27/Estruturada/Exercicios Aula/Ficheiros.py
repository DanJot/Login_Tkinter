#totalsalario = 0
existe = False
nome = input("Insira o nome do funcionário: ")
with open("CINEL.txt", "r", encoding="UTF-8") as ficheiro:
    print(f"{'Nome':<10} {'Ordenado':<9} {'Localidade':<10}")
    for linha in ficheiro:
        #a função strip permite remover o caracter que faz mudança de linha no ficheiro
        #a função split "corta" a linha de dados pelo delimitador(;)
        dados = linha.strip().split(';')
        totalsalario += int(dados[1])
        if "Porto" in dados[2]:
            print(f"{dados[0]:<10} {dados[1]:<9} {dados[2]:<10}")
        if nome.lower() in dados[0].lower():
            existe = True
    print(totalsalario)
    if(existe):
        print("Funcionário encontrado")
    else:
        print("Não encontrado")