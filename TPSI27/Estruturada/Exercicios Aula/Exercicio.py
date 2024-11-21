# PEDIR O NOME E A PASS, SE PASS = CINEL SENAO ERRO
nome = input("Indique o nome:")
password = input("Indique a sua password:")

if password.lower() == "cinel":
    print("A pass está correta")
else:
    print("Pass incorreta!")
