preco = float(input("Digite o valor = "))
quantidade = int(input("Digite a quantidade = "))
total = preco*quantidade

if quantidade < 9 : 
    print(f"O preço com desconto será de = {total:.2f} \n O preço era de {total:.2f}" )

if quantidade >= 10 and quantidade < 100 : 
    print(f"O preço será de = {total*0.95:.2f}\n O preço era de {total:.2f}")

elif quantidade >=100 and quantidade <1000 :
    print(f"O preço será de = {total*0.9:.2f}\n O preço era de {total:.2f}")

elif quantidade >=1000 :
    print(f"O preço será de = {total*0.85:.2f}\n O preço era de {total:.2f}")
