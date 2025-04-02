nome = 'Jeandra'.upper()
idade = 36

nome = 'Hugo'
idade = 17

print(nome, idade)

dados_pessoais = f'meu nome e {nome.upper()} e tenho {idade} anos.'

print(dados_pessoais)

for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print(i)
print('done looping')

x = 4
x *= 2
x -= 3

print(x)