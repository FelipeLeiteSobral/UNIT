import random
# Função de decisão (Repetir/Parar)
def decidirAcao(funcao):
    while True:
        funcao()
        opcao = input("\nQuer tentar novamente? (s/n): ").lower()
        if opcao == 's':
            continue
        else:
            print("Obrigado! Até a próxima!\n")
            break

# Parte 1 – Estrutura de Controle e Fluxo, Exceções e Subprogramas
# 7. Jogo de Adivinhação com Tentativas
def jogoAdivinhacao():
    print("="*80)
    print("\nJOGO DE ADIVINHAÇÃO, TENTE ACERTAR!\n")
    print("Foi sorteado um número entre 1 e 10.")
    numeroSorteado = random.randint(1, 10)
    while True:
        try:
            tentativas = int(input("Informe quantas tentativas você deseja para adivinhar o número sorteado: "))
            if tentativas <= 0:
                raise ValueError
            break
        except ValueError:
            print("Escolha um número inteiro positivo!")
    print(f"Você tem {tentativas} tentativas para adivinhar!")
    tentativa = 1
    while tentativa <= tentativas:
        print(f"\nTentativa {tentativa}/{tentativas}")
        try:
            palpite = int(input("Digite seu palpite: "))
            if palpite == numeroSorteado:
                print(f"PARABÉNS! Você acertou na {tentativa}ª tentativa! O número era {numeroSorteado}!")
                return
            elif palpite < numeroSorteado:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")
            tentativa += 1
        except ValueError:
            print("Digite apenas números inteiros.")
            continue
    print(f"Suas tentativas acabaram. O número era: {numeroSorteado}\n")

# Parte 2: Linguagens Procedurais
# 5. Fibonacci com Recursão
def Fibonacci():
    print("="*80)
    print("\nDESCUBRA A SEQUÊNCIA DE FIBONACCI!\n")
    def informarNumero():
        try:
            numero = int(input("Informe até qual termo deseja ver: "))
            if numero <= 0:
                raise ValueError
            else:
                return numero
        except ValueError:
            print("Digite um número inteiro positivo.")
            return informarNumero()    
    numero = informarNumero()
    i = 0
    listaFibonacci = [0, 1]
    def calcularFibonacci(i, numero):
        if numero > i:
            soma = listaFibonacci[i] + listaFibonacci[i+1]
            listaFibonacci.append(soma)
            return calcularFibonacci(i + 1, numero)
        else:
            return listaFibonacci 
    calcularFibonacci(i, numero - 1)
    listaFibonacci.remove(0)
    print(f"Sequência de Fibonacci até o {numero}º termo: {listaFibonacci}")
    return listaFibonacci

# Parte 3: Programação Orientada a Objetos (Python)
# 7. Classe Triângulo com Verificação de Tipo
def verificarTriangulo():
    print("="*80)
    print("\nCRIE UM TRIÂNGULO E DESCUBRA O SEU TIPO!\n")
    class Triangulo:
        def __init__(self, a, b, c):
            self.ladoA = a
            self.ladoB = b
            self.ladoC = c

        def tipo(self):
            if self.ladoA == self.ladoB == self.ladoC:
                return "Triângulo Equilátero"
            elif self.ladoA == self.ladoB or self.ladoA == self.ladoC or self.ladoB == self.ladoC:
                return "Triângulo Isósceles"
            else:
                return "Triângulo Escaleno"
    def informarLados():
        try:
            a = abs(int(input("Informe o primeiro lado: ")))
            b = abs(int(input("Informe o segundo lado: ")))
            c = abs(int(input("Informe o terceiro lado: ")))
            if a + b > c and b + c > a and c + a > b:
                return a, b, c
            else:
                raise ValueError
        except ValueError:
            print("Lado(s) inválido(s). Digite valores que formem um triângulo.")
            return informarLados()
    lados = informarLados()
    triangulo = Triangulo(*lados)
    print(f"\n{triangulo.tipo()} com lados: A={triangulo.ladoA}, B={triangulo.ladoB}, C={triangulo.ladoC}")

# Menu principal
def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Jogo de adivinhação")
        print("2. Sequência de Fibonacci")
        print("3. Verificar tipo de Triângulo")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            decidirAcao(jogoAdivinhacao)
        elif escolha == '2':
            decidirAcao(Fibonacci)
        elif escolha == '3':
            decidirAcao(verificarTriangulo)
        elif escolha == '0':
            print("Encerrando programa.\n")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução
menu()