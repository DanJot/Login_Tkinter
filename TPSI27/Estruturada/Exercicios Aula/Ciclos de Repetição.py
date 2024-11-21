"""
# CICLO FOR
for i in range(2,6,2):   # intervalo de 2 a 5 e de 2 em dois passos
    print(i)
"""
"""
# CICLO WHILE - A CONDIÇÃO TEM QUE VIR ANTES DO WHILE
numero = 1
while numero != 0: # enquanto numero DIFERENTE de 0
    numero = int(input("Diga um numero\n"))
else:
    print("Sou o zero")

"""
#EX FOR:
#PEÇA 5 NUMEROS, NO FIM DIGA QUANTOS PARES E QUANTOS IMPARES

"""par = 0
impar = 0

for i in range (5):
    numero = int(input("Indique um numero"))

    if numero % 2 == 0 :
        par += 1 # isto é um contador (significa par é igual a par +1)
    else:
        impar += 1

print("Par ->", par)
print("impar ->", impar)
"""
#EX WHILE:
#VAMOS PEDIR N TEMPERATURAS POSITIVAS AO UTILIZADOR
#SEMPRE QUE UMA TEMPERATURA FOR NEGATIVA O PROGRAMA PARA
#QUANDO PARAR TEMOS QUE APRESENTAR O MAX. TEMP, O MIN E A MEDIA COM 2 CASAS DECIMAIS

temp = 1
while temp > 0:
    temp = float(input("Indique a temperatura\n"))

    if temp < 0:
        break

max_temp = max(temp)
min_temp = min(temp)
media_temp = sum(temp) / len(temp)

print(f"Temperatura máxima: {max_temp:.2f}")
print(f"Temperatura mínima: {min_temp:.2f}")
print(f"Média das temperaturas: {media_temp:.2f}")
