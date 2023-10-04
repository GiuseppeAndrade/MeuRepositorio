print ("Jogue Pedra, Papel ou Tesoura")

jogador1 = input("Jogador 1, sua jogada será = ").lower()
jogador2 = input("Jogador 2, sua jogada será = ").lower()


if jogador1 == jogador2 :
    print ("Empate")

elif jogador1 == "pedra" and jogador2 == "tesoura" :
    print ("Jogador 1 venceu") 
elif jogador1 == "tesoura" and jogador2 == "pedra" :
    print ("Jogador 2 venceu") 

elif jogador1 == "tesoura" and jogador2 == "papel" :
    print ("Jogador 1 venceu") 
elif jogador1 == "papel" and jogador2 == "tesoura" :
    print ("Jogador 2 venceu") 

elif jogador1 == "papel" and jogador2 == "pedra" :
    print ("Jogador 1 venceu") 
else :
    print ("Jogador 2 venceu") 
  