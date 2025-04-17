import math, random

# Gerar os números aleatórios e colocá-los na lista
def gerarListaNumerosAleatórios(totalDeNumeros):
    listaNumerosAleatorios = set()
    i=1
    numeroAdicionado = None
    while (totalDeNumeros>=i):
        numeroAdicionar = random.randint(1,25)
        if numeroAdicionar in listaNumerosAleatorios:
            None
        else:
            listaNumerosAleatorios.add(numeroAdicionar)
            i += 1
    return listaNumerosAleatorios
listaAleatoria1 = gerarListaNumerosAleatórios(15)

# a) Solicitar ao usuário a quantidade de dezenas qeu ele deseja marcar na primeira aposta...

def informarQuantidadeDeNumeros():
    primeiraAposta = int(input("Com quantos números você deseja apostar? Informe um valor dentre os seguintes números 15, 16, 17, 18: "))
    if primeiraAposta < 15 or primeiraAposta > 18:
        informarQuantidadeDeNumeros()
    else:
        return primeiraAposta
quantidadeDeNumeros = informarQuantidadeDeNumeros() #CHAMADA DE FUNÇÃO

# b) Informar numeros da primeira aposta sem repetição. Pedindo para inserir novamente tanto para numero repetido 
# como para numeros fora do intervalo
def informarNumeros(quantidade):
    listaNumerosAposta = set()
    i=1
    while (quantidade >= i ):
        numeroParaAdicionar = int(input(f"Informe o número que deseja apostar, (lembrando que {listaNumerosAposta} ja foram selecionados por você!) :"))
        if numeroParaAdicionar < 1 or numeroParaAdicionar > 25:
            print("Dezena inválida, por favor tente outro!")
        elif numeroParaAdicionar in listaNumerosAposta:
            print("Você inseriu um número repetido, por favor tente outro!")
        else:
            listaNumerosAposta.add(numeroParaAdicionar)
            i += 1
    return listaNumerosAposta      
listaAposta = informarNumeros(quantidadeDeNumeros) #CHAMADA DE FUNÇÃO
print(f"Os números selecionados foram {listaAposta}")    

# c) Gerar aleatoriamente duas apostas com 18 números, usando "Surpresinha"

surpresinha1 = gerarListaNumerosAleatórios(18) #CHAMADA DE FUNÇÃO
surpresinha2 = gerarListaNumerosAleatórios(18) #CHAMADA DE FUNÇÃO
print(f"surpresinha!: {surpresinha1}")
print(f"surpresinha!: {surpresinha2}")

# d) Simular o resultado (15 dezenas sorteadas) de um concurso da Lotofácil

lotofacilResultado = gerarListaNumerosAleatórios(15) #CHAMADA DE FUNÇÃO
print(f"O resultado da Lotofácil foi: {lotofacilResultado}")

# e) Imprimir de forma crescente as dezenas da primeira aposta, das duas apostas surpresinha1/surpresinha2 e do resultado 
# da lotofácil simulado

apostaOrdenada = sorted(listaAposta)
surpresinha1Ordenada = sorted(surpresinha1)
surpresinha2Ordenada = sorted(surpresinha2)
lotofacilResultadoOrdenada = sorted(lotofacilResultado)

print(f"\nA aposta ordenada foi: {apostaOrdenada} \nA primeira surpresinha ordenada foi: {surpresinha1Ordenada} \nA segunda surpresinha ordenada foi: {surpresinha2Ordenada} \nO resultado da lotofácil ordernada foi: {lotofacilResultadoOrdenada}\n")