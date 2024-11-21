
def maiorPalavra(palavra1: str, palavra2: str):
    if(len(palavra1) > len(palavra2)):
        print("A maior palavra é a 1")
    elif(len(palavra1) == len(palavra2)):
        print("As palavras tem a mesma dimensao")
    else:
        print("A maior palavra é a 2")





p1 = input("Insira a Palavra 1: ")
p2 = input("Insira a Palavra 2: ")


maiorPalavra(p1, p2)


