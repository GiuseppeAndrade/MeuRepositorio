a = int(input("Digite o valor de a = "))
b = int(input("Digite o valor de b = "))
c = int(input("Digite o valor de c = "))
delta =  b**2 - 4*a*c
bhaskara1 = (-b + (delta**0.5)) / 2*a
bhaskara2  =  (-b - (delta**0.5)) / 2*a

if delta < 0 :
    print("Não há raiz real")
elif delta == 0 :
    print(f"Há uma raiz real = {bhaskara1:.2f}")
    
elif delta > 0 :
    print(f"Há duas raízes reais = {bhaskara1:.2f} e {bhaskara2:.2f}")


