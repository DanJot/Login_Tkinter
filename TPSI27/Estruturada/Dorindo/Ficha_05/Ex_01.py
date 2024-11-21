

# Nome do ficheiro
nome_ficheiro = 'notas.txt'

# Dicionário para armazenar os dados
dados = []

# Ler o ficheiro
with open(nome_ficheiro, 'r', encoding="UTF-8") as ficheiro:
    for linha in ficheiro:
        # Remover espaços em branco e quebras de linha
        linha = linha.strip()
        # Separar o nome e a pontuação
        nome, pontuacao = linha.split(',')
        # Adicionar ao dicionário convertendo a pontuação para um número inteiro
        dados.append((nome, float(pontuacao)))

# Exibir os dados
print("Dados lidos do ficheiro:")
for nome, pontuacao in dados:
    print(f"{nome}: {pontuacao}")


listaaprovados = [ i for i in dados if i[1]>= 50]
print(f"Total de alunos aprovados: {len(listaaprovados)}")



