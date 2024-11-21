def media (num1: int, num2:int, num3:int) -> float:
    resultado = (num1 + num2 + num3) /3
    return resultado

n1 = int(input("Insira o 1º número: "))
n2 = int(input("Insira o 2º número: "))
n3 = int(input("Insira o 3º número: "))

print(f"Média: {media(n1, n2, n3):.2f}")
