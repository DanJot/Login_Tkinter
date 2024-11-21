import datetime
import csv

VEHICLES_FILE = 'veiculos.csv'
RECORDS_FILE = 'registos.csv'
CLASSES = {'A': 1.5, 'B': 2.5, 'C': 3.5}  # Valores das portagens por classe


def load_vehicles():
    vehicles = {}
    try:
        with open(VEHICLES_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                vehicles[row['matricula']] = {
                    'classe': row['classe'],
                    'saldo': float(row['saldo'])
                }
    except FileNotFoundError:
        pass
    return vehicles


def save_vehicles(vehicles):
    with open(VEHICLES_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['matricula', 'classe', 'saldo'])
        writer.writeheader()
        for matricula, data in vehicles.items():
            writer.writerow({'matricula': matricula, 'classe': data['classe'], 'saldo': data['saldo']})


def register_vehicle(vehicles):
    matricula = input("Introduza a matrícula (6 a 8 caracteres alfanuméricos): ")
    while not (6 <= len(matricula) <= 8 and matricula.isalnum() and matricula not in vehicles):
        matricula = input("Matrícula inválida ou já registada. Introduza novamente: ")

    classe = input("Introduza a classe do veículo (A, B, ou C): ")
    while classe not in CLASSES:
        classe = input("Classe inválida. Introduza novamente a classe (A, B, ou C): ")

    saldo = input("Introduza o saldo inicial da Via Verde (número positivo ou zero): ")
    while not saldo.isdigit() or float(saldo) < 0:
        saldo = input("Saldo inválido. Introduza o saldo inicial da Via Verde (número positivo ou zero): ")

    vehicles[matricula] = {'classe': classe, 'saldo': float(saldo)}
    save_vehicles(vehicles)
    print(f"Veículo {matricula} registado com sucesso.")


def remove_vehicle(vehicles):
    matricula = input("Introduza a matrícula do veículo a ser removido: ")
    if matricula in vehicles:
        del vehicles[matricula]
        save_vehicles(vehicles)
        print(f"Veículo {matricula} removido com sucesso.")
    else:
        print("Veículo não encontrado.")


def record_passage(vehicles):
    matricula = input("Introduza a matrícula do veículo: ")
    if matricula not in vehicles:
        print("Veículo não encontrado.")
        return

    passage_number = input("Introduza o número de passagem (número inteiro positivo): ")
    while not passage_number.isdigit() or int(passage_number) <= 0:
        passage_number = input("Número de passagem inválido. Introduza novamente: ")

    data = input("Introduza a data da passagem (DD/MM/AAAA): ")
    try:
        datetime.datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        print("Data inválida.")
        return

    classe = vehicles[matricula]['classe']
    valor_cobrado = CLASSES[classe]
    saldo = vehicles[matricula]['saldo']

    if saldo < valor_cobrado:
        valor_cobrado *= 1.10  # Adicionar taxa de 10%
        print(f"Saldo insuficiente. Taxa adicional de 10% aplicada. Valor total: {valor_cobrado:.2f}")
    else:
        print(f"Valor cobrado: {valor_cobrado:.2f}")

    vehicles[matricula]['saldo'] -= valor_cobrado
    save_vehicles(vehicles)

    with open(RECORDS_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['numero_passagem', 'matricula', 'data', 'valor'])
        writer.writerow(
            {'numero_passagem': passage_number, 'matricula': matricula, 'data': data, 'valor': valor_cobrado})

    print("Passagem registada com sucesso.")


def view_vehicle_details(vehicles):
    matricula = input("Introduza a matrícula do veículo: ")
    if matricula in vehicles:
        details = vehicles[matricula]
        print(f"Matrícula: {matricula}")
        print(f"Classe: {details['classe']}")
        print(f"Saldo: {details['saldo']:.2f}")
    else:
        print("Veículo não encontrado.")


def list_passages_by_date():
    data = input("Introduza a data das passagens a listar (DD/MM/AAAA): ")
    try:
        datetime.datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        print("Data inválida.")
        return

    try:
        with open(RECORDS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            found = False
            for row in reader:
                if row['data'] == data:
                    print(
                        f"Número da passagem: {row['numero_passagem']}, Matrícula: {row['matricula']}, Data: {row['data']}, Valor: {row['valor']}")
                    found = True
            if not found:
                print("Nenhuma passagem encontrada nesta data.")
    except FileNotFoundError:
        print("Nenhuma passagem registada ainda.")


def recharge_balance(vehicles):
    matricula = input("Introduza a matrícula do veículo: ")
    if matricula in vehicles:
        recarga = input("Introduza o valor a recarregar (número positivo): ")
        while not recarga.isdigit() or float(recarga) <= 0:
            recarga = input("Valor inválido. Introduza novamente: ")

        vehicles[matricula]['saldo'] += float(recarga)
        save_vehicles(vehicles)
        print(f"Saldo recarregado com sucesso. Novo saldo: {vehicles[matricula]['saldo']:.2f}")
    else:
        print("Veículo não encontrado.")


def main():
    vehicles = load_vehicles()

    while True:
        print("\n--- Menu Interativo ---")
            print("1. Registar Veículo")
            print("2. Remover Veículo")
            print("3. Registar Passagem")
            print("4. Exibir Informações do Veículo")
            print("5. Listar Passagens por Data")
            print("6. Recarregar Saldo")
            print("7. Sair")

        option = input("Escolha uma opção: ")
        if option == '1':
            register_vehicle(vehicles)
        elif option == '2':
            remove_vehicle(vehicles)
        elif option == '3':
            record_passage(vehicles)
        elif option == '4':
            view_vehicle_details(vehicles)
        elif option == '5':
            list_passages_by_date()
        elif option == '6':
            recharge_balance(vehicles)
        elif option == '7':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()