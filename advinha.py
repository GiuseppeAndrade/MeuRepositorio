
print("Pense um número de 1 a 10")
lista = [0,1,2,3,4,5,6,7,8,9,10]


resposta = input("Seu número é par? (S/N)").upper()
if resposta == "S" :
    lista =[0,2,4,6,8,10] 
    resposta = input("Seu número é menor que 5? (S/N)").upper()
    if resposta == "S" :
        lista=[0,2,4]
        resposta = input("Seu número é primo? (S/N)").upper()
        if resposta =="S" :
            lista = [2]
            print (lista)
        elif resposta == "N":
            lista = [0,4]
            resposta = input("Seu número é divisível por 2? (S/N)").upper()
            if resposta == "S" :
                lista = [4]
                print (lista)
            elif resposta == "N":
                lista = [0]
                print(lista)

    elif resposta == "N":
            lista=[6,8,10]
            resposta = input("Seu número é divisível por 4? (S/N)").upper()
            if resposta == "S" :
                lista=[8]
                print(lista)
            elif resposta == "N":
                lista=[6,10]
                resposta = input("Seu número é maior que 7? (S/N)").upper()
                if resposta == "S" :
                    lista=[10]
                    print(lista)
                elif resposta == "N":
                    lista=[6]
                    print(lista)
else:    
    lista =[1,3,5,7,9] 
    resposta = input("Seu número é menor ou igual a 5? (S/N)").upper()
    if resposta == "S" :
        lista=[1,3,5]
        resposta = input("Seu número é primo? (S/N)").upper()
        if resposta =="N" :
            lista=[1]
            print(lista)
        elif resposta == "S":
            lista=[3,5]
            resposta = input("Seu número é divisível por 5? (S/N)").upper()
            if resposta =="S" :
                lista=[5]
                print (lista)
            elif resposta == "N":
                lista = [3]
                print(lista)
        
    elif resposta == "N":
                lista=[7,9]
                resposta = input("Seu número é maior que 8? (S/N)").upper()
                if resposta == "S" :
                    lista = [9]
                    print(lista)
                elif resposta == "N":
                    lista = [7]
                    print(lista)
                   
    


