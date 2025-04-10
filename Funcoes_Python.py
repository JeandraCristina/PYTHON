"""FUNÇÕES
Uma função em Python é uma estrutura que permite agrupar um
conjunto de instruções para que possam ser executadas várias vezes,
sem que seja necessário repetir todo o código. 
A sintaxe básica para criar uma função em Python é a seguinte:

def nome_da_funcao(argumentos):
    # corpo da função
    return resultado
    
A palavra-chave "def" indica o início da definição da função.
"nome_da_funcao" é o nome que você escolhe para identificar a função. 
É uma boa prática usar nomes descritivos que indiquem o que a função faz.
"argumentos" são valores que você pode passar para a função para que ela possa trabalhar com eles.
Os argumentos são opcionais e você pode ter quantos quiser (ou nenhum). 
Eles são separados por vírgulas.
O corpo da função é onde você coloca as instruções que serão executadas quando a função for chamada. 
O corpo é identado com quatro espaços (ou um tab).
"return" é uma palavra-chave que indica qual é o valor de retorno da função. 
Quando a função é chamada, ela executa o código no seu corpo e, em seguida, 
retorna o valor especificado pelo "return". Se a função não tiver um "return", ela retorna "None".
"""

#Criando a Função
def quadrado(numero):
    resultado = numero ** 2
    return resultado

#Chamando a Função
resultado = quadrado(5)
print(resultado)

#----------------------------------------------------------------------------------------------

#Criando uma função do programador sem passagem de parâmetro
#Início da função
#def linha():
#    print("#"*100)
#Fim da Função  

#-------------------------------------------------------------------------------------------------

#Início do programa
#print("Inicio do Programa")
#linha()
#print("Fim do programa")
#Fim de Programa   