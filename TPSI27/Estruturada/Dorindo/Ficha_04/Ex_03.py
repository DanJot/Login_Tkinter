
temperaturas = []
temp_media = 22

for i in range (10):
    temperatura = float(input(f"Temperatura {i+1}: "))
    temperaturas.append(temperatura)


print(f"\nTemperaturas superiores à média do país ({temp_media} ºC):")
for index, temperatura  in enumerate(temperaturas):
    if(temperatura > temp_media ):
        print(f"Número: {index + 1}; Temperatura: {temperatura}")

