lista = ["pastilha de freio","trambulador","bronzina","pistão"]

while True:
    print("DIGITE 0 PARA SAIR")
    print("DIGITE 1 PARA MOSTRAR A LISTA")
    print("DIGITE 2 PARA ADICIONAR UM ITEM NA LISTA")
    print("DIGITE 3 PARA EXCLUIR UM ITEM DA LISTA")
    print("DIGITE 4 PARA ALTERAR UM ITEM DA LISTA")

    codigo = int(input("digite o codigo desejado: "))
    while codigo !=0 and codigo !=1 and codigo !=2 and codigo !=3 and codigo !=4:
        print("codigo invalido")
        codigo = int(input("digite o codigo desejado: "))
  
    if codigo == 0:
        print("Você saiu!")
        exit()
       

    elif codigo ==1:
       print (str(f"Os itens disponíveis são: {lista}").replace("[","").replace("]","").replace("'",""))

    elif codigo == 2:
        item = input("Adicione um item: ")
        lista.append(item)
        print(lista)

    elif codigo == 3:
        print(lista)
        item3 = input("Remova um item: ")
        lista.remove(item3)
        print(lista)

    elif codigo == 4:
        print(lista)
        item4 = input("Selecione um item: ")
        if item4 in lista:
            pos = lista.index(item4)
            lista.remove(item4)
            item5 = input("Qual seu novo item? ")
            lista.insert(pos,item5)
            print(lista)
        else:
            print("Item inválido")
        
    opcao = input("Deseja fazer algo a mais? (SIM/NÃO)").lower()
    
    if opcao == "s" or "sim":
        continue
    elif opcao == "n" or "nao" or "não": 
        print("Você saiu!")  
        


