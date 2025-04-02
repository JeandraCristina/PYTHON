#Funções para calculadora
def soma_n (a,b):
    return print(a + b)

def subtracao_n (a,b):
    return print(a - b)

def multiplicacao_n (a,b):
    return print(a * b)

def divisao_n (a,b):
    if (b <= 0):
        return print("Não é possível dividir por zero")
    else:
        return print(a / b)