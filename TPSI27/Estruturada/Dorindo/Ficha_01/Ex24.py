print("*** Exercício 24 ***")
texto = "Não podes brincar. Tens que estudar!"

resultado = texto.find("brincar", 0, len(texto))

if resultado != -1:
    print("Encontrei a palavra brincar!")
else:
    print("Não encontrei a palavra brincar!")

