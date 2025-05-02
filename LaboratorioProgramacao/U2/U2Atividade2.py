import random
# 1. Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a
# área do terreno.
def informarMedidas():
    largura = float(input("Informe a largura da figura(em m): "))
    comprimento = float(input("Informe a comprimento da figura(em m): "))
    print(f"O terreno possui as seguintes dimensões: {largura}m X {comprimento}m")
    return largura, comprimento
def calcularArea(comprimento, largura):
    area = comprimento * largura
    return area

#Execução

medidas = informarMedidas()
area = calcularArea(*medidas)
print(f"O valor da área é de {area} m²")

# 2. Faça um programa que tenha uma função chamada contador(), que
# receba três parâmetros: início, fim e passo. Seu programa tem que
# realizar três contagens através da função criada:
# de 1 até 10, de 1 em 1;
# de 10 até 0, de 2 em 2

def contador(inicio, fim, passo):
    for numero in range(inicio, fim, passo):
        print(numero)
    return

#Execução

contador(1,10,1)
contador(10,0,-2)

# 3. Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.

def listarNumeros():
    listaNumeros = []
    while True:
        try: 
            numero = float(input("Coloque um número na lista: "))
            listaNumeros.append(numero)
            saida = input("Você tem interesse em sair do programa?(digite 's' se sim): ").upper()
        except ValueError:
            ("O valor digitado não é um número.")
        if saida == "S":
            break
    return listaNumeros

def maior(lista):
    valorMaximo = max(lista)
    return print(f"O maior valor da lista é: {valorMaximo}")

#Execução

lista1 = listarNumeros()
maior(lista1)

# 4. Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
# números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.
def sorteia(lista):
    quantidade = len(lista)
    listaSorteados = set()
    repeticoes = 0
    while(repeticoes < 5):
        sorteado = random.randint(0,quantidade-1)
        numeroSorteado = lista[sorteado]
        listaSorteados.add(numeroSorteado)
        repeticoes += 1
    return listaSorteados
def somaPar(lista):
    resultado = 0
    for numero in lista:
        if (numero % 2) == 0:
            resultado += numero
    return resultado

#Execução
lista2 = listarNumeros()
listaSorteados = sorteia(lista2)
somaParesSorteados = somaPar(listaSorteados)
print(f"A lista de números é: {lista2}")
print(f"A lista de números sorteados é: {listaSorteados}")
print(f"O resultado da soma dos sorteados pares é: {somaParesSorteados}")

# 5. Crie um programa que tenha uma função fatorial() e retorno o valor fatorial
# de três variáveis em tela.

def fatorial(numero):
    resultado = 1
    for i in range(numero, 1, -1):
        resultado *= i
        print(resultado)
    return resultado

#Execução
valor = fatorial(5)
print(valor)

# 6. Faça um programa, com uma função que necessite de um argumento. A
# função retorna o valor de caractere ‘P’, se seu argumento for positivo, e
# ‘N’, se seu argumento for zero ou negativo.

def julgarValor(numero):
    if numero > 0:
        return print("P")
    if numero < 0:
        return print("N")
    else:
        return print("Nulo")

#Execução
julgarValor(3)

# 7. Faça um programa com uma função chamada somaImposto. A função
# possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
# sobre vendas expressa em porcentagem e custo, que é o custo de um
# item antes do imposto. A função “altera” o valor de custo para incluir o
# imposto sobre vendas.
def informar():
    custo = float(input("Informe o valor total de custo do item: R$"))
    imposto = float(input("Informe quantos '%' o imposto incide sobre o custo: "))
    return custo, imposto

def somaImposto(taxaImposto, custo):
    valor = custo + (custo * taxaImposto / 100)
    return valor

#Execução
custo, imposto = (informar())
venda = somaImposto(imposto, custo)
print(f"O valor final com os impostos é de: R${venda}")

# 8. Faça um programa que converta da notação de 24 horas para a notação de 12
# horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada
# é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer
# a conversão e uma para a saída. Registre a informação A.M./P.M. como um
# valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões
# terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que
# permita que o usuário repita esse cálculo para novos valores de entrada todas
# as vezes que desejar.

def informarHora():
    try:
        horas = int(input("Informe o tempo em horas: "))
        minutos = int(input("Informe o tempo em minutos: "))
        if (horas < 0 or minutos < 0) or (horas > 23) or (minutos > 59):
            raise ValueError
        return horas, minutos
    except ValueError:
        print("Informe corretamente o valor das horas e dos minutos (Horas - entre 0-23)/(Minutos - entre 0-59)")
        return informarHora()

def converter(horas, minutos):
    if horas >= 12:
        horas -= 12
        turno = "P.M."
    else:
        turno = "A.M"
    return print(f"O tempo informado é {horas}:{minutos} {turno}")

#Execução
tempo = informarHora()
converter(*tempo)