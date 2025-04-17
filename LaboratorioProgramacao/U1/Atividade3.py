import random

# 1 
# Peça ao usuário para inserir cinco notas. Calcule e exiba a média das notas. Se a média for maior ou igual a 7, 
# exiba "Aprovado"; se a média for entre 5 e 7, exiba "Em recuperação"; caso contrário, exiba "Reprovado". 
# Garanta que as notas estejam entre 0 e 10.
def inserirNota(numero):
    print(f"Olá, informe {numero} notas (valores numéricos, entre 0 e 10)\n")
    i = 0
    listaNotas =[]
    while i < numero:
        nota = float(input(f"nota{i+1}: "))
        if 0 <= nota <= 10:
            listaNotas.append(nota)
            i += 1
    media = (sum(listaNotas))/ 5
    if media >= 7:
        print(f"Sua média é {media:.2f}, você foi aprovado(a)!")
    elif media >= 5:
        print(f"Sua média é {media:.2f}, você está de recuperação!")
    else:
        print(f"Sua média é {media:.2f}, você foi reprovado(a)!")

inserirNota(5)
    
# 2
# Solicite ao usuário um número inteiro e verifique se ele é par ou ímpar. 
# Em seguida, exiba todos os números pares ou ímpares, conforme a escolha do usuário, no intervalo de 1 a 100.

numeroInteiro = int(input("Insira um número inteiro: "))
if numeroInteiro %  2 == 0:
    print(f"{numeroInteiro} é um número par")
else:
    print(f"{numeroInteiro} é um número ímpar")

# 3
# Crie um programa que exiba uma contagem regressiva a partir de um número fornecido pelo usuário, até 1. 
# Pergunte se o usuário deseja que a contagem pule de 2 em 2 ou 3 em 3.
def decrementoValor():
    numeroEscolhido = int(input("Escolha um número inteiro: "))
    numeroDecremento = int(input("Qual valor você gostaria de decremento? 2 ou 3? "))
    while numeroDecremento != 2 and numeroDecremento != 3:
        numeroDecremento = int(input("Valor inválido! Qual valor você gostaria de decremento? 2 ou 3? "))
        

    for i in range(numeroEscolhido, 0, -numeroDecremento):
        print(i)
decrementoValor()

# 4
# Peça ao usuário um número inteiro e um limite (por exemplo, até onde ele deseja ver a tabuada). 
# Exiba a tabuada desse número até o limite fornecido pelo usuário. Inclua uma verificação para garantir que o limite seja maior que 0. 

numeroTabuada = int(input("informe o número que você deseje que comece a tabuada: "))
numeroLimite = int(input("Informe o número limite para até onde vai a tabuada: "))
def tabuada(numero, limite):
    while limite <= 0:
        limite = int(input("Valor inválido! Informe o número limite para até onde vai a tabuada: "))
    for i in range(1, limite+1):
        print(f"{numero} x {i} = {numero*i}")

aluno = tabuada(numeroTabuada, numeroLimite)

# 5
# Solicite ao usuário um número inteiro n. Em seguida, calcule e exiba a soma de todos os números primos de 1 até n. 
# Inclua uma função para verificar se um número é primo. 

# 5.1 verifica se o número é primo
def eh_primo(n):
    """Função para verificar se um número é primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 5.2 Calcula a soma dos números primos até o número informado
def numerosPrimos():
    numeroN = int(input("Insira um número inteiro: "))
    listaPrimos = [i for i in range(2, numeroN + 1) if eh_primo(i)]

    print(f"Números primos até {numeroN}: {listaPrimos}")
    print(f"A soma de todos os números primos é {sum(listaPrimos)}")

numerosPrimos()

# 6
# Pergunte ao usuário sua idade. Se a idade for menor de 18, exiba "Você é menor de idade" e quantos anos faltam para
# ele completar 18. Se a idade estiver entre 18 e 65, exiba "Você é maior de idade" e quantos anos faltam para 
# completar 65. Se for maior que 65, exiba "Você é idoso".  

idadeUsuario = int(input("Insira a sua idade: "))
if idadeUsuario < 18:
    print("Você é menor de idade.")
elif idadeUsuario >= 18 and idadeUsuario <= 65:
    print("Você é maior de idade.")
else:
    print("Você é idoso.")

# 7
# Peça ao usuário um número inteiro e exiba todos os números de 1 a 100 que são divisíveis por esse número, 
# juntamente com a contagem total de números divisíveis encontrados. 

numeroSelecionado = int(input("Insira um número:"))
def numerosDivisiveis(numeroDivisao):
    numerosEncontrados = 0
    for i in range(100, 0, -1):
        if i % numeroDivisao == 0:
            print(f"O número {i} é divisível por {numeroDivisao}")
            numerosEncontrados = numerosEncontrados + 1
    print(f"{numerosEncontrados} número(s) de 0 a 100 é(são) divisível(is) por {numeroDivisao}")

numerosDivisiveis(numeroSelecionado)

# 8
# Crie um programa que gere e exiba todos os números da sequência de Fibonacci até um valor n fornecido pelo usuário. 
# Pergunte ao usuário qual o limite máximo para a sequência  
numero1 = int(input("Insira um número inteiro qualquer:"))
def fibonacci(numero):
    numeroCorrente = 1
    numeroAnterior = 1

    if numero <= 0:
        print("Por favor insira um número inteiro positivo.")
    else:
        print("Fibonacci:")
        while numero >= numeroCorrente:
            print(numeroCorrente)
            numeroAnterior, numeroCorrente = numeroCorrente, numeroAnterior + numeroCorrente

fibonacci(numero1)

# 9
# 9.1 Escolha um número aleatório entre 1 e 100. Peça ao usuário para adivinhar o número e informe se o palpite é muito 
# alto, muito baixo ou correto. Permita que o usuário continue tentando até adivinhar corretamente. 
# Adicione um contador para mostrar quantas tentativas foram feitas.  

def sorteio():
    numeroSorteado = random.randint(0, 10)
    numeroParaSorteio = int(input("Adivinhe o número sorteado selecionando um número no intervalo de 0 a 100: "))
    listaNumerosEscolhidos = set()
    while numeroParaSorteio!= numeroSorteado:
        listaNumerosEscolhidos.add(numeroParaSorteio)
        numeroParaSorteio = int(input(f"Tente novamente, o número selecionado não confere com o de sorteio (voce já executou os números {listaNumerosEscolhidos}): "))
    numeroTentativas = len(listaNumerosEscolhidos) + 1
    print(f"Você acertou! O número sorteado foi {numeroSorteado}. Foram feitas {numeroTentativas} tentativas.")

sorteio()

# 9.2
# Solicite ao usuário que insira uma frase. Conte e exiba o número de vogais (a, e, i, o, u)
# e consoantes presentes na frase. Considere apenas letras e desconsidere espaços e caracteres especiais.

fraseUsuario = input("Insira uma frase: ")
def contagemLetras(frase):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    numVogais = 0
    numConsoantes = 0
    for letra in frase:
        if letra in vogais:
            numVogais += 1
        elif letra in consoantes:
            numConsoantes += 1
    print(f"O número de vogais encontradas foi {numVogais}, o número de consoantes encontradas foi {numConsoantes}")

contagemLetras(fraseUsuario)