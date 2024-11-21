
def validar_nome(nomeContacto:str):
    # O Nome só pode ser constituído por letras e ter no máximo 10 caracteres
    while True:
        try:
            if(len(nomeContacto) == 0 or len(nomeContacto) >10):
                raise ValueError("O nome deve ser constituído entre 1 e 10 letras")
            

            if not nomeContacto.isalpha():
                raise ValueError("O nome deve ser constituído por letras.")
            #if not nome.replace(" ", "").isalpha():
                #raise ValueError("O nome só pode ser constituído por letras.")
            
            break

        except ValueError as e:
            print(f"\033[91m Erro: {e} \033[0m")
            nomeContacto = input("Insira o nome no formato correto. Nome: ")

    return nomeContacto


def validar_telefone(telefoneContacto:str):
    # O Telefone deve estar validado para entradas do tipo telemóvel
    indicativos = ["91", "92", "93", "94", "95", "96"]
    while True:
        try:

            if(len(telefoneContacto) != 9):
                raise ValueError("O telefone deve ser constituído por 9 dígitos numéricos.")

            if not telefoneContacto.isdigit():
                raise ValueError("O telefone deve ser constituído por dígitos numéricos.") 

            if telefoneContacto[0:2] not in indicativos:
                raise ValueError("O telefone deve ser constituído por um indicatívo de rede móvel.")
                    
            break

        except ValueError as e:
            print(f"\033[91m Erro: {e} \033[0m")
            telefoneContacto = input("Insira o telefone no formato correto. Telefone: ")

    return telefoneContacto


def validar_email(emailContacto:str):
    # O email deve garantir a existência do @ e do .
    while True:
        try:

            utilizador = emailContacto.split("@")[-0]
            dominio = emailContacto.split("@")[-1]

            if not ("@" in emailContacto and "." in dominio):
                raise ValueError("O e-mail deve conter '@' e um '.' após o '@'.")
             
            break

        except ValueError as e:
            print(f"\033[91m Erro: {e} \033[0m")
            emailContacto = input("Insira o email no formato correto. Email: ")

    return emailContacto 






    