# 21. Construa um programa que por intermédio de uma função coloque 
# uma determinada palavra inserida pelo utilizador em letras minúsculas.

# definição de funções
def minusculas(texto):
    return texto.lower()


# main program
palavra = input("Insira uma palavra: ")
print(f"Palavra em minúsculas: {minusculas(palavra)}")