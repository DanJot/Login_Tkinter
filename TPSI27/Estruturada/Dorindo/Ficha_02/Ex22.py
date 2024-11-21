def contaInteiros(numero):
    contador = 0
    quociente = numero

    while(quociente >= 10):
        quociente = quociente / 10
        contador = contador + 1

    contador = contador + 1
    return contador



num = float(input("Insira um número: "))
contaInteiros(num)
print(f"Quantidade de dígitos: {contaInteiros(num)}")
