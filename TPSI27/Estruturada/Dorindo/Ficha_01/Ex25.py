print("*** Exercício 25 ***")
texto = input("Insira um texto: ")

resultado = texto.find("brincar", 0, len(texto))

if resultado != -1:
    print("Encontrei a palavra brincar!")
else:
    print("Não encontrei a palavra brincar!")