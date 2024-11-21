# Deve ser AlfaNumerico e ter 5 caracteres
def ValidarCodigo(codigoMedicamento):
    while True:
        try:
            if len(codigoMedicamento) != 5 : # comprimento diferente de 5
                raise ValueError("O Código deve ter 5 caracteres")
            if not codigoMedicamento.isalnum(): #código ser alfanumerico
                raise ValueError("O código só pode ser constituido por números e letras")
            return codigoMedicamento
        except ValueError as e:
            print(f"Erro: {e}")
            codigoMedicamento = input("Insira o código no formato correto\n")

#Deve ser Inteiro e Positivo
def ValidarQuantidade(quantidadeMedicamento):
   while True:
        try:
            quantidadeMedicamento = int(quantidadeMedicamento)
            if quantidadeMedicamento <= 0:
                raise ValueError("A quantidade deve ser um número inteiro maior que zero")
            return quantidadeMedicamento  
        except ValueError as e:
            print(f"Erro: {e}")
            quantidadeMedicamento = input("Insira a quantidade no formato correto!\n")

#Deve ser Numero Positivo
def ValidarPreco(precoMedicamento):
    while True:
        try:
            precoMedicamento = float(precoMedicamento)
            if precoMedicamento <= 0:
                raise ValueError("O preço deve ser um número maior que zero")
            return precoMedicamento  
        except ValueError as e:
            print(f"Erro: {e}")
            precoMedicamento = input("Insira o preço no formato correto!\n")

# Deve ter no maximo 40 caracteres
def ValidarNome(nomeMedicamento):
    while True:
        try:
            if  len(nomeMedicamento) <= 0 or len(nomeMedicamento) > 40:
                raise ValueError("O nome não tem o número de caracteres permitidos! ")
            if not nomeMedicamento.isalpha():
                raise ValueError("O nome só pode conter letras ")
            return nomeMedicamento
        except ValueError as e:
            print(f"Erro: {e}")
            nomeMedicamento = input("Insira o nome no formato correto!\n")