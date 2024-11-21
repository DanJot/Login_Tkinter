
print("*** Exercício 07 ***")

idade = int(input("Insira a idade do jogador:"))

if(5 <= idade <= 7):
    print("Infantil A")
elif (8 <= idade <= 11):
    print("Infantil A")
elif (12 <= idade <= 13):
    print("Juvenil A")
elif (14 <= idade <= 17):
    print("Juvenil B")
elif (idade >= 18):
    print("Sénior")
else:
    print("Idade inválida para a prática do futebol.")

