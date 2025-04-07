import calculadora

c = 's'

while c == "s":
    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite o segundo numero: "))
    print("Escolha uma função matematica.")
    e = int(input("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potência\n: "))
    
    if e == 1:
         calculadora.soma_n(a,b)
    elif e == 2:
        calculadora.subtracao_n(a,b)
    elif e == 3:
        calculadora.multiplicacao_n(a,b)
     elif e == 4:
        calculadora.divisao_n(a,b)
            