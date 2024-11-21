from reservas import Reserva

baseDados = []

def CriarReserva():
    nome = input("Indique o nome para a reserva: ")
    contacto = input("Indique o contacto: ")
    data = input("Indique o dia: ")
    hora = input("Indique a hora: ")
    npessoas = input("Indique quantas pessoas: ")

    novaReserva = Reserva(nome, contacto, data, hora, npessoas)
    baseDados.append(novaReserva)

    print("\n Reserva criada com sucesso!\n")


def ListarReservas():
    if not baseDados:
        print("Não existem reservas criadas...\n")
    else:
        for reservas in baseDados:
            reservas.mostrarDados()


def ConsultarReserva():
    if not baseDados:
        print("Não existem reservas criadas!")
        return
    encontrado = False
    reservaConsultar = input("Indique a reserva que deseja consultar: ")
    for reservas in baseDados:
        if reservaConsultar == reservas.getNome():
            encontrado = True
            reservas.mostrarDados
            break
    if not encontrado:
        print("\n Essa Reserva não existe!!\n")


def ConsultarReservaData():
    if not baseDados:
        print("Não existem reservas criadas!")
        return
    encontrado = False
    reservaConsultar = input("Indique a data para a qual pretende pesquisar reservas: ")
    for reservas in baseDados:
        if reservaConsultar == reservas.getData():
            encontrado = True
            reservas.mostrarDados()

    if not encontrado:
        print("\n Essa Reserva não existe!!\n")


def ConsultarReservaCliente():
    if not baseDados:
        print("Não existem reservas criadas!")
        return
    encontrado = False
    reservaConsultar = input("Indique o cliente para a qual pretende pesquisar reservas: ")
    for reservas in baseDados:
        if reservaConsultar == reservas.getNome():
            encontrado = True
            reservas.mostrarDados()

    if not encontrado:
        print("\n Essa Reserva não existe!!\n")


def AtualizarReserva():
    if not baseDados:
        print("Não existem reservas criados!")
        return
    encontrado = False
    nomeAtualizar = input("Indique a reserva que deseja atualizar: ")

    for reservas in baseDados:
        if nomeAtualizar == reservas.getNome():
            encontrado = True
            novaHora = input("Indique a nova hora: ")
            reservas.setHora(novaHora)
            novoNpessoas = input("Indique a nova quantidaade de pessoas: ")
            reservas.setNpessoas(novoNpessoas)
            print("Dados atualizados com sucesso!\n")
            break
    if not encontrado:
        print("\n Essa Reserva não existe!!\n")


def RemoverReserva():
    if not baseDados:
        print("Não existem reservas criadas!")
        return
    encontrado = False
    reservaRemover = input("Indique a reserva que deseja remover: ")
    for reservas in baseDados:
        if reservaRemover == reservas.getNome():
            encontrado = True
            baseDados.remove(reservas)
            print("Reserva removida com sucesso!\n")
            break
    if not encontrado:
        print("\n Essa reserva não existe!!\n")

