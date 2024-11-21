letra = input("Diga uma letra:\n")

match letra.lower():

    case 'a' | 'i' | 'o' | 'u' :
        print("vogal")
    case 'e' :
        print("vogal")
    case _:
        print("consoante")
