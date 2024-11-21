#5.	Faça um programa que leia dois valores
# inteiros A e B, se os valores forem iguais
# deverá somar os dois, caso contrário multiplique A por B.

A = int(input("Diga um número:\n"))
B = int(input("Diga um número:\n"))

if A == B :
    print("A soma dos dois é:", A+B )

else:
    print("A multiplicação dos dois é: ", A * B)


#7.	Elabore um programa que dada a idade de um jogador de futebol
# classifique-o em uma das seguintes categorias:
#Infantil A=5 a 7 anos
#Infantil B=8 a 11 anos
#Juvenil A= 12 a 13 anos
#Juvenil B=14 a 17 anos
#Senior= maiores de 18 anos

idade = int(input("Indique a idade do jogador:\n"))

if 5 <= idade <= 7:
    print("Infantil A")
elif 8 <= idade <= 11:
    print("Infantil B")
elif 12 <= idade <= 13:
    print("Juvenil A")
elif 14 <= idade <= 17:
    print("Juvenil B")
else:
    print("Senior")

#19. Elabore uma função que calcule a média de três números inseridos pelo utilizador





# 21.Crie uma função que utilize uma função que peça duas palavras ao
# utilizador e no fim diga qual é a maior palavra.

p1 = input("Indique uma palavra:"))
p2 = input("Indique outra palavra:"))

n1 = (len(p1))
n2 = (len(p2))

if n1 > n2:
    print("A primeira palavra é a maior")
else:
    print(" segunda palavra é a maior")

