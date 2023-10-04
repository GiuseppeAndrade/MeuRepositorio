numero1 = int(input("Digite o cateto A = ")) 
numero2 = int(input("Digite o cateto B = "))
h2 = (numero1*numero1) + (numero2*numero2)
h2 = (h2 ** 0.5)

print (f"A hipotenusa é = {h2} ")

print (f"Perimetro = {numero1 + numero2 + h2} ")

print (f"Área = {numero1 * numero2 /2 :.0f} ")

