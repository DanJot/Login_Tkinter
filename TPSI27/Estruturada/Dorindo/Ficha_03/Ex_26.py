# 26. Crie um programa que peça o utilizador para acertar o número secreto gerado pelo computador. 
# Sempre que o utilizador não acertar no número o programa deve informar o utilizador 
# se o seu palpite é menor ou maior que o número gerado. 
# Quando o utilizador acertar no número o programa deve apresentar 
# o número de tentativas que levaram o utilizar acertar no número. 
# a.	numero_secreto = random.randint(1, 100) # Gera um número aleatório entre 1 e 100 
# b.	devemos importar o random para ter acesso à função desejada

# importação de módulos
import random


# main
palpites = []
print("Vou sortear um número entre 1 e 100.")
numero_secreto = random.randint(1, 100)
print("Já está. Qual o seu palpite?")


while(True):
    
    palpite = int(input("Indique um número: "))
    palpites.append(palpite)

    if (palpite>=1 and palpite<=100):
        if(numero_secreto<palpite):
            print(f"Falhou, o número secreto é menor do que {palpite}.")
        elif numero_secreto == palpite :
            print(f"Parabéns, acertou!")
            break
        else:
            print(f"Falhou, o número secreto é maior do que {palpite}.")
    else:
        print("Lembre-se, o número sorteado encontra-se entre 1 e 100.")


print(f"Número de tentativas: {len(palpites)}")

