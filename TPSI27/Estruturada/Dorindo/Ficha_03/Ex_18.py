# 18. Elabore um programa que com a ajuda de uma função, peça seis números ao utilizador, 
# que os guarde numa lista e no fim apresente a média dos números inseridos.

def media(lista):
    return sum(lista)/len(lista)


numeros=[]

print("Insira 6 números")
for i in range (1,7):
    numero = float(input(f"Número {i}: "))
    numeros.append(numero)

print(f"Média: {media(numeros)}")

