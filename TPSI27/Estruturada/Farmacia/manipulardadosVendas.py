import manipulardadosMedicamentos
from datetime import date

codigoVenda = 0

def RegistarVenda(codMedicamento, quantidadeMedicamento):
    global codigoVenda #uso a variável global para não criar um metodo de incremento do códigoVenda
    
    registarVenda = 0
    with open("medicamentos.txt", "r", encoding="UTF-8") as ficheiro:
        for linha in ficheiro:
            dados = linha.strip().split(';')
            if dados[0] == codMedicamento :
                registarVenda = 1
                if int(dados[1]) >= int(quantidadeMedicamento):
                    registarVenda = 2
                    break
            
        if registarVenda == 0:
            print("\nO código do medicamento está errado!\n")
        
        elif registarVenda == 1:
            print("\nQuantidade em stock insuficiente para registar venda!\n")
        
        else:
            manipulardadosMedicamentos.AtualizarMedicamentoVenda(codMedicamento, quantidadeMedicamento)
            codigoVenda += 1
            today = date.today()
            total = int(dados[1]) * float(dados[2])
            linhas = (f"{codigoVenda};{dados[0]};{dados[1]};{total};{today}\n")
            with open("vendas.txt", "a", encoding="UTF-8") as ficheiro:
                ficheiro.write(linhas)
            print("\nVenda registada com sucesso!\n\n")


def ListarVendas():

    with open("vendas.txt", "r", encoding="UTF-8") as ficheiro:
        print("\nListagem do Ficheiro Vendas\n")
        for linha in ficheiro:
            dados = linha.strip().split(';')
            print(f"{dados[0]} {dados[1]} {dados[2]} {dados[3]} {dados[4]}\n")
        print("------")
