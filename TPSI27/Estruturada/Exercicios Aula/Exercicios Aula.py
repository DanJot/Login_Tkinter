#Ficha 1

#EX. 6
nota1 = int(input("Indique a primeira nota\n"))
nota2 = int(input("Indique a segunda nota\n"))
print("A média das duas notas é:", (nota1 + nota2) / 2)

#EX. 8
import math
numero = int(input("Indique um número\n"))
print(f"A raiz quadrada desse número é, {math.sqrt(numero):.3f})

#EX. 9	Escreva um algoritmo que leia o nome de um aluno
# e as notas das três provas que ele obteve no periodo.
# No final deve mostrar o nome do aluno e a sua média (aritmética).
nome=input("Indique o nome do aluno: ")
nota1 = int(input("Indique a nota da primeira prova\n"))
nota2 = int(input("Indique a nota da segunda prova\n"))
nota3 = int(input("Indique a nota da terceira prova\n"))
print("A média do", nome , "é:", (nota1+nota2+nota3) / 3)

#EX. 10	Desenvolva um programa que permita calcular a potencia de um número de base 2.
numero=int(input("Indique um numero"))
print("A potencia de", numero, "é", 2**numero)
ou print(math.pow(2, numero))

#EX. 22 Desenvolva um programa que substitua a palavra “Python” por “revolução” (dica: replace)
nome="Python"
print(nome.replace("Python", "revolução"))

#EX. 23.Faça um programa que escreva todo o texto em letras maiúsculas (dica: upper)
nome = "Hello World"
print(nome.upper())

#EX. 27 Faça um programa que duplique e apresente a string inicial
nome = "STOP"
print(nome + nome)


