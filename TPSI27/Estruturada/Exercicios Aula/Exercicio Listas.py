#Ex. Faz uma lista que peça 5 numeros e apresente o max, min e media

lista = []
for i in range (5):

    numero = int(input("Diga um numero: "))
    lista.append(numero)

print(f"max:, {max(lista)}")
print(f"min:, {min(lista)}")
print(f"Media: {sum(lista) / len(lista)}")


#Pede 4 nomes e apresenta em lista ordenada
lista = []
for i in range (4):
    nome = input("Diga um nome: ")
    lista.append(nome)

lista.sort()
print(lista)


