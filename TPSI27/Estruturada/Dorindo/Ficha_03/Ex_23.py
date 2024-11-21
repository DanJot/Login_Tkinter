# 23. Desenvolva uma função que permita determinar se um 
# determinado número inserido pelo utilizador é divisível por dez.

# definição de funções
def divisivel_dez(n):
    if(n % 10 == 0):
        print(f"O número {n} é divisível por 10.")
    else:
         print(f"O número {n} não é divisível por 10.")

# main program
numero = int(input("Insira um número: "))
divisivel_dez(numero)