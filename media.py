
quantidade = int(input("Quantas notas deseja inserir?  "))
soma = 0 
for i in range (0,quantidade,1):
    n1 = float(input("Digite a nota = "))
    soma += n1


media = (soma) / (quantidade)

print(media)