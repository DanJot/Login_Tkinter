# 19. Escreva função que receba como parâmetro um número inteiro 
# e retorne -1, 0 ou 1 se este número for negativo, nulo ou positivo, respetivamente.

# definição de funções
def verifica_inteiro(n):
    if n>0 :
        return 1
    elif n==0 :
        return 0
    else:
        return -1

# main program
numero = int(input("Insira o número inteiro: "))
print(f"Retorno da função: {verifica_inteiro(numero)}")
