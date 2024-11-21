
def validar_codigo(codigoProduto:str):
    # O Código do produto pode variar entre 3 e 4 dígitos
    while True:
        try:

            if (len(codigoProduto)<3) or (len(codigoProduto) > 4):
                raise ValueError("O código deve ser constituído entre 3 e 4 dígitos numéricos.")

            if not codigoProduto.isdigit():
                raise ValueError("O código deve ser constituído por dígitos numéricos.") 
                  
            break

        except ValueError as e:
            print(f"\033[91m Erro: {e} \033[0m")
            codigoProduto = input("Insira o telefone no formato correto. Código: ")

    return codigoProduto


def validar_quantidade(quantidadeProduto:str):
# A Quantidade deve ser um número interior maior que zero
    while True:
        try:
            quantidade = int(quantidadeProduto)
            if quantidade <= 0:
                raise ValueError() 
           
            break

        except ValueError as e:
            #print(f"\033[91m Erro: {e} \033[0m")
            print(f"\033[91m Erro: A quantidade deve ser um número inteiro maior do que zero. \033[0m")
            quantidadeProduto = input("Insira a quantidade no formato correto. Quantidade: ")

    return quantidadeProduto


def validar_preco(precoProduto:str):
# O preço deve ser um número maior que zero
    while True:
        try:
            preco = float(precoProduto)
            if preco <= 0:
                raise ValueError() 
                   
            break

        except ValueError as e:
            #print(f"\033[91m Erro: {e} \033[0m")
            print(f"\033[91m Erro: O preço deve ser um número maior do que zero. \033[0m")
            precoProduto = input("Insira o preço no formato correto. Preço: ")

    return precoProduto


def validar_tipo(tipoProduto:str):
    # O tipo de produto deve aceitar até 50 caracteres de entrada
    while True:
        try:
            if len(tipoProduto) > 50:
                raise ValueError("O tipo deve ser constituído até 50 carateres")
                  
            break

        except ValueError as e:
            print(f"\033[91m Erro: {e} \033[0m")
            tipoProduto = input("Insira o nome no formato correto. Nome: ")

    return tipoProduto