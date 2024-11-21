# 27. Escreva uma função que leia 12 números e que os guarde numa lista. 
# Posteriormente apresente a soma dos números, o maior número e o menor número.

def ler_dados():
    for i in range(12):
        numero = int(input(f"Número {i+1} :"))
        numeros.append(numero)


numeros = []
ler_dados()

soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)

print()
print(f"Soma: {soma}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")

print("*** Fim! ***")
