# 1. Implemente um programa que permita a digitação de um número e informe, após uma avaliação, se o número 
# digitado é divisível por 10, por 5 e por 2 ou
# se não é divisível por nenhum destes.
def inserirNumero():
    numero = int(input("Insira um número: "))
    return numero

def avaliarNumero(numero):
    restoDivisaoPor10 = numero % 10
    restoDivisaoPor5 = numero % 5
    restoDivisaoPor2 = numero % 2
    if restoDivisaoPor10 == 0:
        print(f"O número {numero} é divisível por 10")
    else:
        print(f"O número {numero} não é divisível por 10")
    if restoDivisaoPor5 == 0:
        print(f"O número {numero} é divisível por 5")
    else:
        print(f"O número {numero} não é divisível por 5")
    if restoDivisaoPor2 == 0:
        print(f"O número {numero} é divisível por 2")
    else:
        print(f"O número {numero} não é divisível por 2")
    return

# Execução
numero1 = inserirNumero()
avaliarNumero(numero1)

# 2. Desenvolva um programa que solicite ao usuário o nome e senha. Caso o nome do usuário seja igual à senha, 
# informe que a senha não está correta,
# caso contrário, informe o aceite da senha.

def cadastro():
    usuario = input("Informe seu usuário: ")
    senha = input("Informe a sua senha: ")
    if usuario.upper() == senha.upper():
        print("Tente novamente, o usuário e senha não devem ser iguais")
        return cadastro()
    return usuario, senha

# Execução
cadastro()

# 3. Implemente um programa para que, ao serem fornecidos o primeiro termo de uma Progressão Aritmética e a razão, 
# seja possível calcular e exibir seu
# vigésimo termo. Caso o valor informado para a razão seja negativo, assuma seu valor absoluto.

def valoresParaPA():
    termo1 = float(input("Informe o primeiro termo da PA: "))
    razao = float(input("Informe a razão da PA: "))
    return termo1, razao
def progressaoAritimetica(termo1, razao):
    listaPA = []
    for indiceTermo in range(20):
        termoCorrente = indiceTermo * razao + termo1
        listaPA.append(termoCorrente)
    print(listaPA)

# Execução
progressaoAritimetica(*valoresParaPA())


# 4. Implemente um programa que, ao receber a razão de uma Progressão Geométrica e o valor do primeiro termo, 
# possa calcular e imprimir o quinto termo
# da série. Caso a razão seja negativa, faça uso de seu valor absoluto.

def valoresParaPG():
    termo1 = float(input("Informe o primeiro termo da PG: "))
    razao = float(input("Informe a razão da PG: "))
    return termo1, razao
def progressaoGeometrica(termo1, razao):
    listaPG = []
    for indiceTermo in range(20):
        if indiceTermo != 0:
            termoCorrente = razao * listaPG[-1]
            listaPG.append(termoCorrente)
        else:
            listaPG.append(termo1)
    print(listaPG)

# Execução
progressaoGeometrica(*valoresParaPG())

# 5. Desenvolva um programa que deva receber o valor de uma venda e, caso o valor total desta venda seja superior 
# a R$ 50, aplique um desconto de 18% e
# informe. Tendo ou não o desconto, informe ao usuário o valor a ser cobrado do cliente.

def vender():
    valorTotalVenda = int(input("Informe o valor total da venda: "))
    if valorTotalVenda > 50:
        valorVenda = valorTotalVenda * 0.82
        print(f"O valor que o cliente deverá pagar é de R${valorVenda} (possui 18% de desconto)")
    else:
        print(f"O valor que o cliente deverá pagar é de R${valorTotalVenda}")

# Execução
vender()

# 6. Criar um programa que solicite ao usuário, que é um professor, o valor da hora\aula, número de aulas dadas por semana e, caso o valor obtido como
# salário mensal for inferior a R$ 1.000,00, informe ao professor que ele está isento de contribuição sindical. Para obter o salário mensal, multiplique o valor
# da hora/aula pela quantidade de aulas dadas multiplicada por 4,5.

def calcularSalario():
    horaAula = float(input("Informe o valor de hora/aula: "))
    numeroDeAulasSemanais = float(input("Informe a quantidade de aulas por semana: "))
    salario = horaAula * numeroDeAulasSemanais * 4.5
    if salario < 1000:
        return print(f"Seu salário é de R${salario:.2f} e é inferior a R$1000,00. Portanto você está isento de contribuição sindical")
    else:
        return print(f"Seu salário é de R${salario:.2f} e é superior a R$1000,00. Portanto você não está isento de contribuição sindical")

#Execução
calcularSalario()
    
# Crie um programa que apresente a soma acumulada de todos os valores entre 1 e 100.

def somarValores():
    lista = []  
    for indice in range(1,101):
        lista.append(indice)
    somatorioLista = sum(lista)
    print(f"A soma dos números dará {somatorioLista}")

# Execução
somarValores()

# 8. Desenvolva um programa que solicite dez números ao usuário e, a cada número recebido, ,
# informe seu valor ao quadrado.

def retornarQuadrado(numero):
    quadrado = numero ** 2
    return quadrado

def solicitarNumeros():
    lista = []
    for i in range(10):
        try:
            numero = float(input("Informe um numero para que se retorne seu valor ao quadrado: "))
            lista.append(numero)
            
        except ValueError:
            print("Tente Novamente. Lembre de inserir somente números.")
            continue
    for numero in lista:
        quadrado = retornarQuadrado(numero)
        print(f"O numero {numero} ao quadrado é igual a {quadrado}")
    return

# Execução
solicitarNumeros()

# 9. Implemente um programa que solicite um número ao usuário. Esse número representará a quantidade de valores que 
# deverão ser solicitados, pelo seu
# programa. Para cada valor informado pelo usuário, seu programa deverá informar o triplo do mesmo.

def solicitarNumeros():
    quantidade = int(input("Informe quantas vezes que deseja solicitar um número: "))
    listaNumeros = []
    for i in range(quantidade):
        try:
            numero = float(input("Informe um número: "))
            listaNumeros.append(numero)
        except ValueError:
            print("Problema na inserção!")
    for numero in listaNumeros:
        triploNumero = numero*3
        print(f"O triplo de {numero} é {triploNumero}")
    return

# Execução
solicitarNumeros()
   
# 10. Faça um programa que permita ao usuário informar números enquanto os valores informados forem positivos. 
# Ao final, informe ao usuário quantos
# números foram digitados.

def listarNumeros():
    listaNumeros = []
    while True:
        try:
            numero = float(input("Informe um número positivo para adicionar: "))
            if numero < 0:
                raise ValueError
            listaNumeros.append(numero)
        except ValueError:
            print("O valor não é um número positivo. Portanto sairá do loop")
            break
    return print(f"{len(listaNumeros)} foram digitados")

# Execução
listarNumeros()

# 11. Uma agência de uma cidade do interior tem, no máximo, 10.000 clientes. Desenvolva um programa que permita a 
# entrada do número da conta, nome e
# saldo de cada cliente. Seu programa deverá imprimir para cada conta informada, além de seu saldo, uma das 
# mensagens: positivo ou negativo. A
# digitação acaba no momento em que o usuário informar o número -999 como sendo número de uma conta. 
# Ao final, deverá sair o total de clientes com
# saldo negativo, o total de clientes da agência e o saldo da agência.


clientes = dict()
def cadastrarCliente():
    while True:
        if len(clientes) <= 10000:
            numeroConta = int(input("Digite o número da conta do cliente: "))
            nome = input("Digite o nome cliente: ")
            saldoConta = float(input("Digite o valor que o cliente possui em conta: "))
            clientes[numeroConta] = [nome, saldoConta]
            sair = input("Pressione S para caso deseje sair: ").upper()
            if sair == "S":
                break
        else:
            print("A empresa atingiu o número máximo de clientes.")
        
    print(clientes)


# Execução
cadastrarCliente()



# 12. Desenvolva um programa que permita ao usuário informar valores inteiros até o momento em que um valor negativo 
# seja informado. Quando isso ocorrer,
# informe a quantidade de números lidos, a quantidade de números que sejam múltiplos de 6 dentre os informados e a 
# média de todos os números lidos.

def trabalharNumeros():
    listaNumeros = []
    while True:
        try:
            numero = int(input("Informe um número positivo para adicionar: "))
            if numero < 0:
                raise ValueError
            listaNumeros.append(numero)
        except ValueError:
            print("O valor não é um número positivo. Portanto sairá do loop")
            break

    print(f"{len(listaNumeros)} foram digitados")
    for numero in listaNumeros:
        if (numero % 6) == 0:
            print(f"O numero {numero} é divisível por 6")
    media = sum(listaNumeros)/len(listaNumeros)
    print(f"A média dos valores inseridos é {media:.2f}")

# Execução
trabalharNumeros()