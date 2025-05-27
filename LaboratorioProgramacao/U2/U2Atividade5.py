import math
from abc import ABC, abstractmethod
# Conversões – Resolva usando funções
# 1. Converta metros para quilômetros. Fórmula: km = m / 1000
def metros_para_km(metros):
    return metros / 1000

# 2. Converta Celsius para Fahrenheit. Fórmula: F = (C * 9/5) + 32
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 3. Converta m/s para km/h. Fórmula: km/h = m/s * 3.6
def ms_para_kmh(velocidade_ms):
    return velocidade_ms * 3.6

# 4. Converta energia de joules para calorias. Fórmula: cal = J / 4.184
def joules_para_calorias(joules):
    return joules / 4.184

# 5. Converta horas para segundos. Fórmula: s = h * 3600
def horas_para_segundos(horas):
    return horas * 3600

# 6. Calcule a massa molar da água (H2O). Fórmula: 2*1.008 + 15.999
def massa_molar_agua():
    return 2 * 1.008 + 15.999  # ≈ 18.015 g/mol

# 7. Calcule a quantidade de mols: mol = massa / massa molar
def calcular_mols(massa, massa_molar):
    return massa / massa_molar

# 8. Converta mol/L para g/L: g/L = mol/L * massa molar
def mol_por_litro_para_g_por_litro(mol_l, massa_molar):
    return mol_l * massa_molar

# 9. Calcule diluição: C1*V1 = C2*V2, onde V2 = (C1*V1)/C2
def calcular_diluicao(C1, V1, C2):
    if C2 == 0:
        raise ValueError("C2 não pode ser zero.")
    V2 = (C1 * V1) / C2
    return V2

# 10. Calcule o número de partículas: N = mol * 6.022e23
def numero_de_particulas(mol):
    return mol * 6.022e23

# Execução
print("1. 5000 metros são", metros_para_km(5000), "km")
print("2. 25°C são", celsius_para_fahrenheit(25), "°F")
print("3. 10 m/s são", ms_para_kmh(10), "km/h")
print("4. 1000 Joules são", joules_para_calorias(1000), "calorias")
print("5. 2 horas são", horas_para_segundos(2), "segundos")
print("6. Massa molar da água é", massa_molar_agua(), "g/mol")
massa_agua = 36  # exemplo
mols_agua = calcular_mols(massa_agua, massa_molar_agua())
print(f"7. {massa_agua}g de água tem", mols_agua, "mols")
print("8. 2 mol/L de água são", mol_por_litro_para_g_por_litro(2, massa_molar_agua()), "g/L")
print("9. Para diluir 1L de solução 2M para 0.5M, V2 é", calcular_diluicao(2, 1, 0.5), "L")
print("10. Número de partículas em 1 mol é", numero_de_particulas(1))
print()


# ---------------------------------------------------------------------------------
# Matemática - Resolva usando funções
# 1. Calcule a área de um círculo. Fórmula: A = π * r2

def area_circulo(raio):
    return math.pi * raio ** 2

# 2. Calcule o fatorial de um número.
def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# 3. Calcule o MDC entre dois números.
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

# 4. Verifique se um número é primo.
def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# 5. Calcule a média aritmética de uma lista.
def media(lista):
    if not lista:
        raise ValueError("A lista não pode ser vazia.")
    return sum(lista) / len(lista)

# Execução
print("1. Área de um círculo de raio 5:", area_circulo(5))
print("2. Fatorial de 5:", fatorial(5))
print("3. MDC de 60 e 48:", mdc(60, 48))
print("4. O número 17 é primo?", eh_primo(17))
print("5. Média de [10, 20, 30, 40]:", media([10, 20, 30, 40]))
print()


# ---------------------------------------------------------------------------------
# Ciência da Computação / Sistemas de Informação - Resolva usando funções (Python) 
# 1. Inverta uma string.
# número.
def inverter_string(s):
    return s[::-1]

# 2. Conte o número de vogais em uma string.
def contar_vogais(s):
    vogais = "aeiouAEIOU"
    return sum(1 for char in s if char in vogais)

# 3. Some os valores de um dicionário.
def somar_dicionario(dicionario):
    return sum(dicionario.values())

# 4. Retorne os números pares de uma lista.
def numeros_pares(lista):
    return [num for num in lista if num % 2 == 0]

# 5. Verifique se uma senha tem pelo menos 8 caracteres, uma letra maiúscula e um
def senha_forte(senha):
    tem_8_caracteres = len(senha) >= 8
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)

    return tem_8_caracteres and tem_maiuscula and tem_numero

# Execução
print("1. Inverter 'Python':", inverter_string("Python"))
print("2. Número de vogais em 'Inteligência Artificial':", contar_vogais("Inteligência Artificial"))
print("3. Soma dos valores {'a': 10, 'b': 20, 'c': 30}:", somar_dicionario({'a': 10, 'b': 20, 'c': 30}))
print("4. Números pares de [1, 2, 3, 4, 5, 6]:", numeros_pares([1, 2, 3, 4, 5, 6]))
print("5. A senha 'Senha123' é forte?", senha_forte("Senha123"))
print()


# ---------------------------------------------------------------------------------
# Problemas de Programação Orientada a Objetos em Python

# 1. Animais no Zoológico: Crie uma classe abstrata chamada Animal com os métodos
# abstratos fazer_som e mover. Crie subclasses Leao, Elefante e Macaco que
# sobrescrevam os métodos com comportamentos específicos. Crie uma lista com os
# animais e teste seus métodos.

# Classe abstrata
class Animal():
    @abstractmethod
    def fazer_som(self):
        pass
    @abstractmethod
    def mover(self):
        pass

# Subclasses
class Leao(Animal):
    def fazer_som(self):
        return "Rrraaawwwhhhh"
    def mover(self):
        return "Leão correndo."

class Elefante(Animal):
    def fazer_som(self):
        return "Rhiiiihhinn!"
    def mover(self):
        return "Elefante andando."

class Macaco(Animal):
    def fazer_som(self):
        return "Uuuhaaahaahuuuhaa!"
    def mover(self):
        return "Macaco pulando."

# Execução
animais = [Leao(), Elefante(), Macaco()]
for animal in animais:
    print(f"{animal.__class__.__name__} faz som: {animal.fazer_som()}")
    print(f"{animal.__class__.__name__} se move: {animal.mover()}")
print()

# 2. Funcionários de uma Empresa: Crie uma classe abstrata Funcionario com um
# método abstrato calcular_pagamento. Crie as subclasses Gerente e Operario com
# diferentes formas de cálculo. Crie objetos de cada tipo e exiba o pagamento.

# Classe abstrata
class Funcionario():
    @abstractmethod
    def calcular_pagamento(self):
        pass

# Subclasse Gerente
class Gerente(Funcionario):
    def __init__(self, salario_base, bonus):
        self.salario_base = salario_base
        self.bonus = bonus
    def calcular_pagamento(self):
        return self.salario_base + self.bonus

# Subclasse Operario
class Operario(Funcionario):
    def __init__(self, horas_trabalhadas, valor_hora):
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora

# Execução
gerente = Gerente(salario_base=5000, bonus=2000)
operario = Operario(horas_trabalhadas=160, valor_hora=25)

print(f"Pagamento do Gerente: R$ {gerente.calcular_pagamento()}")
print(f"Pagamento do Operário: R$ {operario.calcular_pagamento()}")
print()

# 3. Formas Geométricas: Crie uma classe abstrata Forma com um método abstrato
# area. Crie subclasses Circulo, Quadrado e Triangulo que implementam o cálculo de
# área. Teste chamando o método area de cada forma.

# Classe abstrata
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

# Circulo
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * self.raio ** 2

# Quadrado
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

# Triangulo
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2

# Execução
formas = [Circulo(raio=5), Quadrado(lado=4), Triangulo(base=6, altura=3)]
for forma in formas:
    print(f"A área do {forma.__class__.__name__} é {forma.area():.2f}")
print()

# 4. Veículos: Crie uma classe abstrata Veiculo com os métodos ligar e desligar. Crie
# subclasses Carro, Moto e Caminhao que implementem esses métodos. Instancie cada
# tipo e teste os métodos.

# Classe abstrata
class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

# Subclasse Carro
class Carro(Veiculo):
    def ligar(self):
        return "Carro ligado"
    def desligar(self):
        return "Carro desligado"

# Subclasse Moto
class Moto(Veiculo):
    def ligar(self):
        return "Moto ligada"
    def desligar(self):
        return "Moto desligada"

# Subclasse Caminhao
class Caminhao(Veiculo):
    def ligar(self):
        return "Caminhão ligado"
    def desligar(self):
        return "Caminhão desligado"


# Execução
veiculos = [Carro(), Moto(), Caminhao()]
for veiculo in veiculos:
    print(f"{veiculo.__class__.__name__}: {veiculo.ligar()}")
    print(f"{veiculo.__class__.__name__}: {veiculo.desligar()}")
print()



# 5. Instrumentos Musicais: Crie uma classe abstrata Instrumento com um método
# tocar. Crie subclasses Violao, Piano e Bateria com implementações distintas do
# método. Teste os métodos com uma lista de instrumentos.

# Classe abstrata
class Instrumento(ABC):
    @abstractmethod
    def tocar(self):
        pass

# Subclasse Violao
class Violao(Instrumento):
    def tocar(self):
        return "Som de violão"

# Subclasse Piano
class Piano(Instrumento):
    def tocar(self):
        return "Som de piano"

# Subclasse Bateria
class Bateria(Instrumento):
    def tocar(self):
        return "Som de bateria"

# Execução
instrumentos = [Violao(), Piano(), Bateria()]
for instrumento in instrumentos:
    print(f"{instrumento.__class__.__name__}: {instrumento.tocar()}")
print()

# 6. Sistema de Pagamento: Crie uma classe abstrata MetodoPagamento com um
# método abstrato pagar. Crie classes CartaoCredito, BoletoBancario e Pix que
# implementam pagar de formas distintas. Simule pagamentos.

# Classe abstrata
class MetodoPagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

# Subclasse CartaoCredito
class CartaoCredito(MetodoPagamento):
    def pagar(self, valor):
        return f"Pagamento de R$ {valor:.2f} realizado via cartão de crédito."

# Subclasse BoletoBancario
class BoletoBancario(MetodoPagamento):
    def pagar(self, valor):
        return f"Pagamento de R$ {valor:.2f} realizado via boleto bancário."

# Subclasse Pix
class Pix(MetodoPagamento):
    def pagar(self, valor):
        return f"Pagamento de R$ {valor:.2f} realizado via Pix."


# Execução
pagamentos = [CartaoCredito(), BoletoBancario(), Pix()]
for metodo in pagamentos:
    print(metodo.pagar(150.00))
print()

# 7. Personagens de um Jogo: Crie uma classe abstrata Personagem com os métodos
# atacar e defender. Implemente as classes Guerreiro, Mago e Arqueiro com
# comportamentos diferentes. Simule uma ação de cada personagem.

# Classe abstrata
class Personagem(ABC):
    @abstractmethod
    def atacar(self):
        pass
    @abstractmethod
    def defender(self):
        pass

# Subclasses
class Guerreiro(Personagem):
    def atacar(self):
        return "Guerreiro ataca com espada"
    def defender(self):
        return "Guerreiro usa escudo"

class Mago(Personagem):
    def atacar(self):
        return "Mago lança bola de fogo"
    def defender(self):
        return "Mago usa barreira mágica"

class Arqueiro(Personagem):
    def atacar(self):
        return "Arqueiro dispara flecha"
    def defender(self):
        return "Arqueiro desvia"

# Execução
personagens = [Guerreiro(), Mago(), Arqueiro()]
for p in personagens:
    print(f"{p.__class__.__name__}: {p.atacar()}")
    print(f"{p.__class__.__name__}: {p.defender()}")
print()

# 8. Equipamentos Eletrônicos: Crie uma classe abstrata Equipamento com métodos
# ligar e desligar. Crie subclasses Computador, Televisao e Microondas. Teste os
# métodos com diferentes objetos.

# Classe abstrata
class Equipamento(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

# Subclasses
class Computador(Equipamento):
    def ligar(self):
        return "Computador ligado."
    def desligar(self):
        return "Computador desligado."

class Televisao(Equipamento):
    def ligar(self):
        return "Televisão ligada."
    def desligar(self):
        return "Televisão desligada."

class Microondas(Equipamento):
    def ligar(self):
        return "Microondas ligado."
    def desligar(self):
        return "Microondas desligado."

# Execução
equipamentos = [Computador(), Televisao(), Microondas()]
for e in equipamentos:
    print(f"{e.__class__.__name__}: {e.ligar()}")
    print(f"{e.__class__.__name__}: {e.desligar()}")
print()


# 9. Sistema Bancário: Crie uma classe abstrata ContaBancaria com métodos sacar e
# depositar. Crie ContaCorrente e ContaPoupanca com comportamentos distintos para
# saque e depósito. Simule operações em contas.

# Classe abstrata
class ContaBancaria(ABC):
    def __init__(self, saldo=0):
        self.saldo = saldo
    @abstractmethod
    def sacar(self, valor):
        pass
    @abstractmethod
    def depositar(self, valor):
        pass

# Conta Corrente
class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}"
        else:
            return "Saldo insuficiente para saque na conta corrente."
    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}"

# Conta Poupança
class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado na poupança. Saldo atual: R$ {self.saldo:.2f}"
        else:
            return "Saldo insuficiente na conta poupança."
    def depositar(self, valor):
        self.saldo += valor * 1.01  # Simula juros na poupança
        return f"Depósito de R$ {valor:.2f} com rendimento. Saldo atual: R$ {self.saldo:.2f}"

# Execução 
cc = ContaCorrente(500)
cp = ContaPoupanca(1000)
print(cc.depositar(200))
print(cc.sacar(100))
print(cp.depositar(500))
print(cp.sacar(300))
print()

# 10. Editor de Desenhos: Crie uma classe abstrata FerramentaDesenho com métodos
# desenhar e apagar. Implemente as classes Lapiseira, Pincel e Spray com
# comportamentos próprios. Teste cada ferramenta.

# Classe abstrata
class FerramentaDesenho(ABC):
    @abstractmethod
    def desenhar(self):
        pass
    @abstractmethod
    def apagar(self):
        pass

# Subclasses
class Lapiseira(FerramentaDesenho):
    def desenhar(self):
        return "Desenhando com a lapiseira."
    def apagar(self):
        return "Apagando lapiseira."

class Pincel(FerramentaDesenho):
    def desenhar(self):
        return "Pintando com pincel."
    def apagar(self):
        return "Apagando pincel."

class Spray(FerramentaDesenho):
    def desenhar(self):
        return "Aplicando spray."
    def apagar(self):
        return "Apagando spray."

# Execução
ferramentas = [Lapiseira(), Pincel(), Spray()]
for f in ferramentas:
    print(f"{f.__class__.__name__}: {f.desenhar()}")
    print(f"{f.__class__.__name__}: {f.apagar()}")
print()
