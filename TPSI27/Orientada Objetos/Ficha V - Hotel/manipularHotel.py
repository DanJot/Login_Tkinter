from quarto import Quarto
import validar

baseDados = []



def VerificarNumeroQuarto(numero):

    numero = input("Indique o numero do novo Quarto: ")
    encontrado = False
    for dados in baseDados:
        if dados.getNumero() == numero:
            encontrado = True
            print("Esse quarto já existe!")
            break
    if not encontrado:
        return numero

def CriarQuarto():

    numero = VerificarNumeroQuarto(numero)

    if numero:

        preco = input("Indique o valor da noite do Quarto: ")
        novoQuarto = Quarto(numero, preco, "D")
        baseDados.append(novoQuarto)
        print("Quarto criado com sucesso!\n")
    else:
        return



def ListarQuatoDisponiveis():

    if not baseDados:
        print("Não existem Quartos criados!!")
        return
    for dados in baseDados:

        if dados.getStatus() == "D":
            dados.mostrarDados()
