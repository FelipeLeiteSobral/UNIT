# Explique com suas palavras o conceito de função em programação. Quais as principais vantagens de se utilizar funções em 
# um programa? 

# Resposta: 
# Funções em programação são blocos de código reutilizáveis que executam tarefas específicas, podendo receber parâmetros 
# e retornar resultados. Suas principais vantagens incluem evitar repetição de código, facilitar manutenção, melhorar 
# legibilidade, permitir modularização e simplificar o debugging, tornando os programas mais organizados e eficientes.


# Considere o seguinte código Python:

def calcular_area_retangulo(largura, altura):
  area = largura * altura
  return area

larg = 5
alt = 10
resultado = calcular_area_retangulo(larg, alt)
print(f"A área do retângulo é: {resultado}")

# a) Identifique e explique cada parte da definição da função calcular_area_retangulo.
# b) Qual o valor retornado pela função quando chamada com os argumentos larg = 5 e alt = 10?

# Respostas: 
# a) existe a definição/declaração da função, a passagem de parâmetros, o corpo da função e seu retorno
# b) O valor retornado será 50 



# Escreva uma função em Python chamada maior_de_tres que receba três números como argumentos e retorne o maior entre eles. Em seguida, faça uma chamada à função com três valores de sua escolha e imprima o resultado.

def maiorDeTres(numero1, numero2, numero3):
  lista = [numero1, numero2, numero3]
  maiorNumero = max(lista)
  return print(f"O maior número dos 3 informados é {maiorNumero}")

maiorDeTres(80,25,39)

# Explique a diferença entre parâmetros e argumentos de uma função em Python. Dê um exemplo prático para ilustrar essa 
# diferença.

# Resposta: Parâmetros são as variáveis definidas na declaração da função, enquanto argumentos são os valores concretos 
# passados para ela quando chamada. Por exemplo, na função def soma(a, b):, a e b são parâmetros; já em soma(5, 3), 
# 5 e 3 são os argumentos.


# Crie uma função chamada converter_temperatura que receba a temperatura em graus Celsius como argumento e retorne a 
# temperatura equivalente em graus Fahrenheit. A fórmula de conversão é:
# F=(C×9/5​)+32

def converterTemperatura(celsius):
  farenheit = (celsius*9/5)+32
  return print(f"A temperatura transformada de {celsius}ºC para Farenheit, é de {farenheit} ºF")

# Em seguida, utilize essa função para converter a temperatura de 25 graus Celsius e imprima o resultado.

converterTemperatura(25)