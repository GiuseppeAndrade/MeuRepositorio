quantidade = int(input("Quantas notas deseja informar? "))
soma = 0
lista = [ ]
for i in range (0,quantidade):
    numeros = int(input("Digite sua nota = "))
    lista.append(numeros)
    soma = soma + numeros
media = (soma)/quantidade
print (str(f"Suas notas são= {lista}").replace("[","").replace("]",""))
print(f"E sua média é: {media}")