quantidade = int(input("Quantas notas deseja informar? "))
soma = 0
somapeso = 0

for x in range(0,quantidade,1):
    nota = float(input(f"Digite a nota : "))
    peso = float(input(f"Digite o peso : "))
    soma = soma + nota * peso
    somapeso = somapeso + peso
    

    

media = (soma)/somapeso


print(f"A média é: {media:.2f}")