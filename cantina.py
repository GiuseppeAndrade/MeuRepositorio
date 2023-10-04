print ("BEM VINDO À NOSSA CANTINA\n\n Descrição dos Produtos\n |Código|     |Produto|       |Valor|\n   100     Cachorro-Quente     9,00\n   101  Cachorro-Quente Duplo  11,00\n   102          X-Egg          12,00\n   103          X-Salada       12,00\n   104          X-Bacon        14,00\n   105          X-Tudo         17,00\n   200     Refrigerante Lata   5,00\n   201        Chá Gelado       4,00\n")
produto = int(input("Digite o código do produto que deseja: "))
while True:
    while (produto != 100 and produto !=101 and produto !=102 and produto !=103 and produto !=104 and produto !=105 and produto !=200 and produto !=201):
        print("Opção inválida!")
        produto = int(input("Digite o código do produto que deseja: "))

    if produto == 100:
        print("Você pediu um Cachorro Quente \n Sua conta será de 9 reais")
    elif produto == 101:
        print("Você pediu um Cachorro Quente Duplo \n Sua conta será de 11 reais")
    elif produto == 102:
        print("Você pediu um X-Egg \n Sua conta será de 12 reais")
    elif produto == 103:
        print("Você pediu um X-Salada \n Sua conta será de 12 reais")
    elif produto == 104:
        print("Você pediu um X-Bacon \n Sua conta será de 14 reais")
    elif produto == 105:
        print("Você pediu um X-Tudo \n Sua conta será de 17 reais")
    elif produto == 200:
        print("Você pediu um Refrigerante Lata \n Sua conta será de 5 reais")
    elif produto == 100:
        print("Você pediu um Chá Gelado \n Sua conta será de 4 reais")

    opcao = input("Deseja pedir algo a mais? (S/N)").upper()
    while (opcao!= "S" and opcao != "N"):
        print("Opção inválida!")
        opcao = input("Deseja pedir algo a mais? (S/N)").upper()
    if opcao == "S":
        print("A")
    elif opcao =="N":
     break


