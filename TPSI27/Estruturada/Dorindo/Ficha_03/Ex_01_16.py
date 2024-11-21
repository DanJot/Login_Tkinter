# letras = [“A”, “B”, “C”, “*”, “E”, “F”, “G”, “H”]
# numeros = [1,2,3]
# 1. Escreva um programa que liste todo o conteúdo da lista letras.
# 2. Desenvolva um programa que insira a letra “D” na posição do asterisco.
# 3. Implemente um programa que insira a letra “I” no fim da lista.
# 4. Crie um programa que escreva a letra “E”.
# 5. Faça um programa que escreva apenas as seguintes letras [“E”, “F”, “G”].
# 6. Escreva um programa que remova a letra “F” da lista.
# 7. Elabore um programa que apresente a posição da letra “G”.
# 8. Crie um programa que inverta a posição dos elementos da lista letras.
# 9. Elabore um programa que liste apenas as letras que estão na posição par da lista.
# 10. Elabore um programa que some os elementos da lista numeros.
# 11. Crie um programa que apresente o maior e menor número da lista numeros.
# 12. Implemente um programa que adicione à lista numeros um novo elemento.
# 13. Faça um programa que retorne o número de vezes que o número 1 aparece na lista.
# 14. Insira o número zero na posição correta da lista.
# 15. Desenvolva um programa que remova o número 1 da lista.
# 16. Crie um programa que adicione à lista numeros três vezes o número 7.


# definicao de funções
def mostrar_menu():
    print("")
    print("--- MENU ---")
    print("1. Listar o conteúdo da lista letras")
    print("2. Inserir a letra “D” na posição do asterisco")
    print("3. Inserir a letra “I” no fim da lista")
    print("4. Escrever a letra “E” ")
    print("5. Escrever apenas as letras [“E”, “F”, “G”]")
    print("6. Remover a letra “F” da lista")
    print("7. Apresentar a posição da letra “G” ")
    print("8. Inverter a posição dos elementos da lista letras")
    print("9. Liste apenas as letras que estão na posição par da lista")
    print("10. Soma dos elementos da lista numeros")
    print("11. Maior e menor número da lista numeros")
    print("12. Adicionar um novo elemento à lista numeros")
    print("13. Número de vezes que o número 1 aparece na lista")
    print("14. Inserir o número zero na posição correta da lista")
    print("15. Remover o número 1 da lista")
    print("16. Adicionar à lista numeros três vezes o número 7")

def opcao_1():
    print(f"Lista letras: {letras}")

def opcao_2():
    print(f"Lista letras (antes): {letras}")
    pos = letras.index("*")
    letras[pos] = "D"
    print(f"Lista letras (depois): {letras}")

def opcao_3():
    print(f"Lista letras (antes): {letras}")
    letras.append("I")
    print(f"Lista letras (depois): {letras}")

def opcao_4():
    print(f"Elemento de índice 4 = {letras[4]} ")

def opcao_5():
    print(f"Elementos de índice 4, 4 e 6 = {letras[4:7]} ")

def opcao_6():
    print(f"Lista letras (antes): {letras}")
    letras.remove("F")
    print(f"Lista letras (depois): {letras}")

def opcao_7():
    pos = letras.index("G")
    print(f"Posição/indíce da letra “G”: {pos}")

def opcao_8():
    print(f"Lista letras (antes): {letras}")
    letras.reverse()
    print(f"Lista letras (depois): {letras}")

def opcao_9():
    novalista = [letra for pos, letra in enumerate(letras) if pos % 2 == 0 ]
    print(f"Lista letras de posição/indíce par : {novalista}")

def opcao_10():
    soma = sum(numeros)
    print(f"Soma dos elementos da lista numeros : {soma}")

def opcao_11():
    maior = max(numeros)
    menor = min(numeros)
    print(f"Maior número da lista numeros : {maior}")
    print(f"Menor número da lista numeros : {menor}")

def opcao_12():
    numero = int(input("Insira um número: "))
    print(f"Lista numeros (antes): {numeros}")
    numeros.append(numero)
    print(f"Lista numeros (depois): {numeros}")

def opcao_13():
    contador = numeros.count(1)
    print(f"Número de vezes que o número 1 aparece na lista : {contador}")

def opcao_14():
    print(f"Lista numeros (antes): {numeros}")
    numeros.insert(0, 0)
    print(f"Lista numeros (depois): {numeros}")  

def opcao_15():
    print(f"Lista numeros (antes): {numeros}")
    for numero in numeros:
        if numero == 1:
            numeros.remove(1)
 
    print(f"Lista numeros (depois): {numeros}")  

def opcao_16():
    print(f"Lista numeros (antes): {numeros}")
    for i in range(3):
        numeros.append(7)
 
    print(f"Lista numeros (depois): {numeros}")  

# main program
letras = ["A","B","C", "*", "E", "F", "G", "H"]
numeros = [1,2,3]

while(True):
    mostrar_menu()
    opcao = input("Indique a sua opção: ") 

    if opcao == "1":
        opcao_1()
    
    elif opcao == "2":
        opcao_2() 
    
    elif opcao == "3":
        opcao_3() 

    elif opcao == "4":
        opcao_4()

    elif opcao == "5":
        opcao_5()

    elif opcao == "6":
        opcao_6()

    elif opcao == "7":
        opcao_7()

    elif opcao == "8":
        opcao_8()

    elif opcao == "9":
        opcao_9()

    elif opcao == "10":
        opcao_10()

    elif opcao == "11":
        opcao_11()

    elif opcao == "12":
        opcao_12()

    elif opcao == "13":
        opcao_13()

    elif opcao == "14":
        opcao_14()

    elif opcao == "15":
        opcao_15()

    elif opcao == "16":
        opcao_16()

    elif opcao.lower() =="s":
        #print("Obrigado!")
        break #sai do ciclo while
    else:
        print("opção inválida.")