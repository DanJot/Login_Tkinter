#é uma variavel que vai aceitar varios valores
#pode aceitar valores de varios tipos de dados (Strings, int etc)
#EX:

lista = [1,2,3,4,5,6,7,8,9]
for i in lista:
    print(i) #mostra lista inteira
print(len(lista)) #mostra quantos elementos tem a lista
numero = int(input("Diga um numero: "))
lista.append(numero) #acrescenta no fim da lista o valor pedido ao utilizador
print("max:", max(lista)) #apresenta o maior valor
print("min:", min(lista)) #apresenta o menor valor
lista.pop() # funcao remove o ultimo digito da lista
lista.sort() #ordena a lista
lista.sort(reverse=true) #ordena de forma inversa
sum.lista() # apresenta a soma dos digitos
lista[0] = 0 #substitui o valor da posição zero para 0
lista.insert(20, 0 ) #inserir na posição 20 o numero 0
