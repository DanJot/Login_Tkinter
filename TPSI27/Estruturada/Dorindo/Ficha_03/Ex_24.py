# 24. Escreva uma função que peça 10 números e posteriormente apresente 
# a quantidade de números inseridos maiores que 30.

# definição de funções
def qtd_numeros_maiores30(lista):
    novaLista = [item for item in lista if(item>30)]
    return len(novaLista)


# main program
numeros=[]

print("Insira 10 números")
for i in range (1,11):
    numero = float(input(f"Número {i}: "))
    numeros.append(numero)

print(f"Quantidade de números maiores do que 30: {qtd_numeros_maiores30(numeros)}")
