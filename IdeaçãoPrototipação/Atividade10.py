# 1. Ler dois números e imprimir a soma dos números lidos.
def lerNumeros(quantidade):
    listaNumeros = list()
    while(quantidade != 0):
        try:
            numero = float(input("Digite um número: "))
            listaNumeros.append(numero)
            quantidade = quantidade - 1

        except ValueError:
            print("Você deve informar um número como valor")
    return listaNumeros

#Execução
print(f"A soma dos números é {sum(lerNumeros(2)):.2f}")
            
# 2. Ler três números e imprimir a soma, média e produto dos números lidos
def multiplicarNumeros(lista):
    produto = 1
    for numero in lista:
        produto *= numero
    return produto

#Execução
listaNumeros = lerNumeros(3)
soma = sum(listaNumeros)
media = soma / len(listaNumeros)
produto = multiplicarNumeros(listaNumeros)
print(f"A soma dos números é {soma}")
print(f"A média dos números é {media}")
print(f"O produto dos números é {produto}")

# 3. Leia o preço de compra de uma mercadoria e calcule e imprima o seu preço de venda para que possa ser obtido um lucro
# de 30%

def lerPreco(lucro):
    preco = float(input("Insira o preço de compra: "))
    venda = preco * (1+lucro/100)
    return venda

#Execução
print(f"O preço de venda para se ter 30% de lucro deverá ser de R${lerPreco(30)}")

# 4. Ler duas variáveis caractere e concatená-las em uma terceira.

def lerVariaveis(quantidade):
    listaVariaveis = list()
    while(quantidade != 0):
        try:
            variavel = str(input("Digite um número: "))
            listaVariaveis.append(variavel)
            quantidade = quantidade - 1

        except ValueError:
            print("Você informado incorretamente")
    return listaVariaveis

def concatenarLista(lista):
    concatenado = ""
    for variavel in lista:
        concatenado += variavel
    return concatenado

#Execução
listaVariaveis = lerVariaveis(2)
print(f"A concatenação das variáveis resultará em {concatenarLista(listaVariaveis)}")

# 5. Ler duas variáveis inteiras e trocar o conteúdo lido de uma pela outra. Dica : use uma terceira variável auxiliar.
variavel1 = 1
variavel2 = 2
def trocar(var1, var2):
    var1, var2 = var2, var1
    return var1, var2
trocar(variavel1,variavel2)

#Execução
print(f"A primeira variável agora é {variavel1} e a segunda variável é {variavel2}")

# 6. Ler dois números e imprimir se são ‘IGUAIS’
def compararNumeros(lista):
    for i in (len(lista)-1):
        if lista[i] == lista[i+1]:
            return print(f"O número {lista[i]} e {lista[i+1]} são IGUAIS")
        else:
            return print(f"O número {lista[i]} e {lista[i+1]} são DIFERENTES")

#Execução
numeros = lerNumeros(2)
compararNumeros(numeros)

# 7. Ler dois números e imprimir se são ‘IGUAIS’ ou ‘DIFERENTES’

#Execução
numeros = lerNumeros(2)
compararNumeros(numeros)

# 8. Ler um número inteiro e imprimir se este número é “PAR” ou “ÍMPAR”

def julgarNumero():
    numero = lerNumeros(1)
    if (numero[0] % 0) == 0 :
        return print(f"O número {numero} é PAR")
    else:
        return print(f"O número {numero} é ÍMPAR")

#Execução
julgarNumero()

# 9. Ler dois números inteiros A e B e dizer se A, é ou não, divisível inteiramente por B

def julgarNumeros():
    listaNumeros = lerNumeros(2)
    if (listaNumeros[0] % listaNumeros[1]) == 0 :
        return print(f"O número {listaNumeros[0]} é divisível por {listaNumeros[1]}")
    else:
        return print(f"O número {listaNumeros[0]} não é divisível por {listaNumeros[1]}")

#Execução
julgarNumeros()

# 10. Ler dois números e imprimir o maior

#Execução
listaNumeros = lerNumeros(2)
print(f"O maior número é {max(listaNumeros)}")

# 11. Ler dois números e imprimi-los em ordem crescente

#Execução
listaNumeros = lerNumeros(2)
print(f"A ordem crescente dos números é {listaNumeros.sort()}")


# 12. Ler dois números e imprimi-los em ordem decrescente e calcular e imprimir a diferença do maior pelo menor

#Execução
listaNumeros = lerNumeros(2)
print(f"A ordem decrescente dos números é {listaNumeros.sort(reverse = True)}")

# 13. Ler três números e imprimir o menor e o maior

#Execução
listaNumeros = lerNumeros(2)
print(f"O maior número é {max(listaNumeros)} e o menor é {min(listaNumeros)}")
