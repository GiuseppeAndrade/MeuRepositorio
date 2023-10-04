while True:
    num = input("Digite um número = ")
    try:
        num = int(num)
        break
    except:
        print("Valor inválido")
        continue

if num == 0 or num == 1 :
    print("Não é primo")

elif num == 2 or num == 3 or num == 5 or num == 7:
    print(" é primo")

elif num < 0:
    print("Número negativo nunca será primo")

elif num %2 != 0 and num %3 != 0 and num %5 !=0 and num %7 !=0 :
    print (f"{num} é primo")

else:
    print(f"{num} não é primo")