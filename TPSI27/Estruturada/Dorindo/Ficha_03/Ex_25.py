# 25. Desenvolva o programa em Python que peça a idade e o género a n pessoas. 
# O programa deve parar quando o utilizador utilizar a letra ‘s’. 
# No fim deve apresentar a quantidade de pessoas do género Feminino e do género Masculino. 
# Deve ainda apresentar a média das idades, a idade da pessoa mais nova e 
# a idade da pessoa mais velha.

pessoas = []

idade = int(input("Insira a idade: "))
genero = input("Insira o género [F - Feminino ; M - Maculino]: ")
pessoas.append((idade, genero))

while(True): 
    opcao = input("Pretende inserir uma nova pessoa? [S-Sim ; N-Não]: ")

    if opcao.upper() == "S":
        idade = int(input("Insira a idade: "))
        genero = input("Insira o género [F - Feminino ; M - Maculino]: ").upper()
        pessoas.append((idade, genero))  

    elif opcao.upper() == "N":
        break #sai do ciclo while

    else:
        print("Opção inválida.")


print()
# Quantidade de pessoas do género Feminino
listaPessoasFeminino = [pessoa for pessoa in pessoas if "F" in pessoa[1]]
print(f"Quantidade de pessoas do género Feminino: {len(listaPessoasFeminino)}")

# Quantidade de pessoas do género Masculino
listaPessoasMasculino = [pessoa for pessoa in pessoas if "M" in pessoa[1]]
print(f"Quantidade de pessoas do género Masculino: {len(listaPessoasMasculino)}")


# Média das idades
listaIdades = [pessoa[0] for pessoa in pessoas]
mediaIdade = sum(listaIdades)/len(pessoas)
print(f"Idade média das pessoas: {mediaIdade}")

# Idade da pessoa mais nova
minIdade = min(listaIdades)
print(f"Idade da pessoa mais nova: {minIdade}")

# Idade da pessoa mais velha
maxIdade = max(listaIdades)
print(f"Idade da pessoa mais velha: {maxIdade}")