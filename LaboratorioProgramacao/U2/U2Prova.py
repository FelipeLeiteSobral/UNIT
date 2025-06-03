# Parte 1 – Estrutura de Controle e Fluxo, Exceções e Subprogramas
# 7. Jogo de Adivinhação com Tentativas

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
# 1. Classe Pessoa com Atributos e Métodos Básicos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome
        self.idade
    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")
    
# 2. Classe Conta Bancária
class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
        print(f"Você depositou R${valor} e seu saldo é de R${self.saldo}")
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Você sacou R${valor} e seu saldo é de R${self.saldo}")
        else:
            print(f"Saldo insuficiente, você tem R${self.saldo}")
    def verSaldo(self):
        print(f"Olá {self.nome} Seu saldo é de R${self.saldo}")

# 3. Classe Retângulo com Cálculo de Área e Perímetro
class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.altura * self.largura
    def perimetro(self):
        return 2 * (self.altura + self.largura)

# 4. Sistema de Login Simples
class Login():
    def __init__(self, senha, usuario):
        self.senha = senha
        self.usuario = usuario
    def autenticar(self, entradaSenha,entradaUsuario):
        return self.senha == entradaSenha and self.usuario == entradaUsuario    

# 5. Registro de Estudantes
class Estudante():
    def __init__(self, nome, matricula, cpf, idade):
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.idade = idade
    def verDados(self):
        print(f"Nome: {self.nome} \nMatrícula: {self.matricula} \nCPF: {self.cpf} \nIdade: {self.idade} ")

# 6. Classe Produto com Estoque
class Produto():
    def __init__(self, estoque, nome, categoria):
        self.nome = nome
        self.estoque = estoque
        self.categoria = categoria
    def adicionarEstoque(self, quantidade):
        self.estoque += quantidade
    def removerEstoque(self, quantidade):
        if self.estoque >= quantidade:
            estoque -= quantidade
        else:
            print(f"Estoque insuficiente, você possui {self.estoque} de {self.nome}.")

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

