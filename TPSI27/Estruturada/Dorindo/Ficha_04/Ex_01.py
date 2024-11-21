
dados = []

for i in range (1, 6):
    print(f"*** Insira os dados da pessoa {i} ***")
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    dados.append((idade, altura))


print("\nLista de dados:")
for idade, altura  in dados:
    print(f"Idade: {idade}; Altura: {altura}")

# Ordenar a lista de tuplas pela altura da menor para a maior (alterando a lista original)
#dados.sort(key=lambda x: x[1])  # x[1] refere-se ao segundo elemento da tupla (altura)

# Ordenar a lista de tuplas pela altura da menor para a maior (criando uma nova lista)
dados_ordenados_asc = sorted(dados, key=lambda x: x[1]) # x[1] refere-se ao segundo elemento da tupla (altura)


# Exibir a lista ordenada
print("\nLista de dados ordenada por altura (menor para maior):")
for idade, altura in dados_ordenados_asc:
    print(f"Idade: {idade}; Altura: {altura}")
