'''
num1 = 0
if num1 > 0 :
    print ("Positivo")
else:
    print ("Negativo")

idade = int(input("Digite sua idade = "))
if idade <= 15 :
    print ("Você não pode votar")
elif idade == 16 or 17 :
    print ("Voto opcional")      
elif idade >= 70 :
    print ("Voto opcional")     
else : 
    print ("Voto obrigatório")    



numero = int(input("Digite um número para ver a tabuada: "))

for i in range (0,11,1):
    print(f"{numero} x {i} = {numero*i}")
    """
    

for a in range (0,11,1):

    for i in range (0,11):
        print (f"{a} x {i} = {a*i}")

for a in range (0,101,1):

    for i in range (0,1):
        print (f"{a} + {i} = {a+i}")
        






        
soma = 0
for i in range (1,101):
    soma +=i 
print(f"A soma de todos os números será = {soma}")


x = 0
while (x <= 10):
    if x %2 == 0:
     print(x)
    x = x+1

sdf= ["maça","banana","manga"]
print(sdf.index("banana"))


lista = [1,2,3,4,5]
a = lista.copy()
a.clear()
print(lista)


lista = [0,1,2,3,4,5]
lista.remove(0)
lista.remove(5)
lista.insert(6,0)
lista.insert(0,5)
print(lista)
'''

lista = [ ]
for i in range (0,3):
    numeros = int(input("Digite algum número = "))
    lista.append(numeros)
    print (lista)
