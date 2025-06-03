import random

# Função de decisão(Repetir/Parar)
def decidirAcao(funcao):
    funcao
    while True:
        opcao = input("Quer tentar novamente? (s/n): ").lower()
        if opcao == 's':
            funcao
        elif opcao == 'n':
            print("Obrigado! Até a próxima!")
            break
        else:
            print("Digite 's' para sim ou 'n' para não.")

# Parte 1 – Estrutura de Controle e Fluxo, Exceções e Subprogramas
# 7. Jogo de Adivinhação com Tentativas
def jogoAdivinhacao():
    print("BEM-VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("Eu sorteei um número entre 1 e 10.")
    numeroSorteado = random.randint(1, 10)
    while(True):
        try: 
            tentativas = int(input("Informe quantas tentativas você deseja para adivinhar o número sorteado: "))
            if tentativas < 0:
                raise ValueError
            break
        except ValueError: 
            print("Escolha um número adequado de tentativas!")
    print(f"Você tem {tentativas} tentativas para adivinhar!")
    tentativa = 1
    while(tentativa <= tentativas):
        print(f"\n Tentativa {tentativa}/{tentativas}")
        try:
            palpite = int(input("Digite seu palpite: "))
            if palpite == numeroSorteado:
                print(f"PARABÉNS! Você acertou na sua {tentativa}ª tentativa! O número era {numeroSorteado}!")
                return
            elif palpite < numeroSorteado:
                print("Não foi dessa vez! Tente um número maior.")
            else:
                print("Não foi dessa vez! Tente um número menor.")
            tentativa += 1
        except ValueError:
            print("Digite apenas números inteiros!")
            continue
    print(f"Suas tentativas acabaram. O número sorteado foi: {numeroSorteado}\n")

# Execução
decidirAcao(jogoAdivinhacao())

# Parte 2: Linguagens Procedurais
# 5. Fibonacci com Recursão
def somaValores(primeiroValor, segundoValor):
    soma = primeiroValor + segundoValor
    return soma
def Fibonacci(numero):
    listaFibonacci = []
    listaFibonacci.append(0)
    listaFibonacci.append(1)
    for i in range(0,numero-1):
        primeiroTermo = listaFibonacci[i]
        segundoTermo = listaFibonacci[i+1]
        listaFibonacci.append(somaValores(primeiroTermo, segundoTermo))
        i += 1
    listaFibonacci.remove(0)
    return listaFibonacci
lista = Fibonacci(5)
print(lista)

# Parte 3: Programação Orientada a Objetos (Python)
# 7. Classe Triângulo com Verificação de Tipo
class Triangulo():
    def __init__(self, ladoA, ladoB, ladoC ):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    def tipo(self):
        if self.ladoA == self.ladoB == self.ladoC:
            return "Equilátero"
        if self.ladoA == self.ladoB or self.ladoA == self.ladoC or self.ladoB == self.ladoC:
            return "Isósceles"
        else:
            return "Escaleno"

 
triangulo1 = Triangulo(3,4,5)
print(f"O triangulo informado é considerado: Triângulo {triangulo1.tipo()}")
