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
    
def potencia_n (a,b):
    return print(a ** b)

def raiz_quadrada_n (a):
    return print(a**(1/2)) 

soma_n(3,9) 
subtracao_n(28,5) 
multiplicacao_n(6,2)
divisao_n(8,2)
potencia_n(2,5)   

"""
#Programa de Potencia
print("\nInício do programa de potência")
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1
contador = 1    #2^3 = 2*2*2
while contador <= expoente:
    resultado = base * resultado
    contador = contador + 1
print(f"{base} elevado a {expoente} é igual a {resultado:.2f}")  
print("Fim")      
    
    """
 