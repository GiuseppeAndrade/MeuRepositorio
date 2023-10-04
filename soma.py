def soma(a,b):
    soma = a + b
    return soma

def subtracao(a,b):
    subtracao = a - b
    return subtracao

def divisao (a,b):
    divisao = a/b
    return divisao

def multiplicacao (a,b):
    multiplicacao = a*b
    return multiplicacao


def validar (x):
    while True:
         
        try:
            x = float(x)
            break
        except:
            print("Valor inválido")
            x = input("Digite um número: ")
            continue
    return x


def conta():
   
    x = input("Digite mais um número: ")
    x = validar(x)
    y = input("Digite mais um número: ")
    y = validar(y)
    op = input("Digite o operador | x, +, -, / |:")
   
    
    if op == "+":
        print(soma(x,y))

    elif op == "-":
         print(subtracao(x,y))

    elif op == "/":
         print(divisao(x,y))

    elif op == "x":
         print(multiplicacao(x,y))

conta()

