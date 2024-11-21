print("Hello World")

nome=input("Indique um nome:")
print("Nome:", nome)
numero=int(input("Indique um número\n")) #MUDAR DE LINHA \n
print("numero:", numero)
numero2=int(input("Indique um segundo numero\n"))
print("Numero2:", numero2)
print("Soma:", numero + numero2)
print("Divisão:", numero / numero2)
print(f"Divisão: {numero / numero2:.2f}") #FORMULA DOS NUMEROS DE CASAS DECIMAIS: :.xf

#ÁREA DO TRAPÉZIO A=(BASE MAIOR + BASE MENOR) X A / 2 - APRESENTAR COM 3 CASAS DECIMAIS

base_maior = int(input("Indique a base maior"))
base_menor = int(input("Indique a base menor"))
altura = int(input("Indique a altura"))
print(f"A área do trapézio é: {((base_maior + base_menor) * altura) / 2:.3f}")

# FUNÇOES QUE EXISTEM NA MATEMÁTICA
import math
Ex: print("O valor de Pi é", math.pi)
ou from math import pi #IMPORTA UMA FUNÇÃO ESPECIFICA
Ex: print("O valor de Pi é", pi)