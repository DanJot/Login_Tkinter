# 17. Faça um programa que leia um número indeterminado de notas. 
# Após esta entrada de dados, faça o seguinte:
# a. Mostre a quantidade de notas que foram lidas.
# b. Exiba todas as notas na ordem em que foram informadas.
# c. Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
# d. Calcule e mostre a soma das notas.
# e. Calcule e mostre a média das notas.
# f. Calcule e mostre a quantidade de notas acima da média calculada

notas = []

nota = float(input("Insira a nota: "))
notas.append(nota)

while(True): 
    opcao = input("Pretende inserir uma nova nota? [S-Sim ; N-Não]: ")

    if opcao.upper() == "S":
        nota = float(input("Insira a nota: "))
        notas.append(nota)  

    elif opcao.upper() == "N":
        break #sai do ciclo while

    else:
        print("Opção inválida.")


# a. Mostre a quantidade de notas que foram lidas.
qtd = len(notas)
print(f"\nQuantidade de notas inseridas: {qtd}")

# b. Exiba todas as notas na ordem em que foram informadas.
print("\nLista de Notas (ordem em que foram inseridas)")
for nota in notas:
    print(nota)

# c. Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
print("\nLista de Notas (ordem inversa em que foram inseridas)")
for nota in reversed(notas):
    print(nota)

#ATENÇÃO: notas.reverse() altera a lista original, por isso usei reversed(notas)
#notas.reverse() 

# d. Calcule e mostre a soma das notas.
soma = sum(notas)
print(f"\nSoma das notas inseridas: {soma}")

# e. Calcule e mostre a média das notas.
media = sum(notas)/len(notas)
print(f"\nMédia das notas inseridas: {media}")

# f. Calcule e mostre a quantidade de notas acima da média calculada
notas_acima_media = [nota for nota in notas if nota>media]
qtd_acima_media = len(notas_acima_media)
print(f"\nQuantidade de notas acima da média: {qtd_acima_media}")
