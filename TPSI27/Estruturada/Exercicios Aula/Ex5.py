import csv

# Função para carregar produtos do ficheiro
def carregar_produtos(caminho):
    produtos = []
    try:
        with open("produtos.txt", 'r') as file:
            leitor = csv.reader(file)
            for linha in leitor:
                if linha:  # Ignorar linhas vazias
                    try:
                        codigo, quantidade, preco, tipo = linha
                        produtos.append({'codigo': int(codigo),'quantidade': int(quantidade),'preco': float(preco),'tipo': (tipo),})
    return produtos

# Função para informar a quantidade de um produto
def informar_quantidade(produtos, codigo):
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto['quantidade']
    return 'Produto não encontrado.'

# Função para apresentar a informação de um produto
def apresentar_info(produtos, codigo):
    for produto in produtos:
        if produto['codigo'] == codigo:
            return produto
    return 'Produto não encontrado.'

# Função para listar toda a informação existente no ficheiro
def listar_todos(produtos):
    return produtos

# Função para somar e apresentar o preço de todos os produtos
def somar_precos(produtos):
    total = sum(produto['preco'] for produto in produtos)
    return total

def main():
    caminho = 'produtos.txt'
    produtos = carregar_produtos(caminho)

    while True:
        print("\nEscolha uma opção:")
        print("1. Informar a quantidade de um produto")
        print("2. Apresentar a informação de um produto")
        print("3. Listar toda a informação existente no ficheiro")
        print("4. Somar e apresentar o preço de todos os produtos")
        print("5. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            codigo = input("Digite o código do produto: ")
            quantidade = informar_quantidade(produtos, codigo)
            print(f"Quantidade do produto {codigo}: {quantidade}")

        elif opcao == '2':
            codigo = input("Digite o código do produto: ")
            info = apresentar_info(produtos, codigo)
            if isinstance(info, dict):
                print(f"Informações do produto {codigo}:")
                for chave, valor in info.items():
                    print(f"{chave.capitalize()}: {valor}")
            else:
                print(info)

        elif opcao == '3':
            print("Informações de todos os produtos:")
            todos = listar_todos(produtos)
            for produto in todos:
                print(produto)

        elif opcao == '4':
            total = somar_precos(produtos)
            print(f"Preço total de todos os produtos: {total:.2f}")

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

