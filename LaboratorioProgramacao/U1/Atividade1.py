import math
# 1. Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]"

numero = float(input("Informe um número: "))
print("O número informado foi %f" % numero)

# 2. Faça um programa que peça dois números e imprima a soma

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
soma = numero1 + numero2
print("A soma dos dois números é: %f" % soma)

# 3. Faça um programa que peça 4 nota bimestrais e mostre a média

nota1 = float(input("Informe a primeira nota de seu primeiro mês: "))
nota2 = float(input("Informe a segunda nota de seu primeiro mês: "))
nota3 = float(input("Informe a primeira nota de seu segundo mês: "))
nota4 = float(input("Informe a segunda nota de seu segundo mês: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print("A média de suas notas é: %f" % media)

# 4. Faça um programa que converta metros para centímetros

numeroParaConveter = float(
    input("Informe um número para converter de metro para centímetros: "))
numeroConvertido = numeroParaConveter * 100
print("O número em centímetros é: %f" % numeroConvertido)

# 5. Faça um programa que peça o raio de um círculo, calcule e mostre sua área

raioDoCirculo = float(input("informe o raio do círculo em centímetros: "))
areaDoCirculo = math.pi * raioDoCirculo**2
print("A área do círculo é : %f cm²" % areaDoCirculo)

# 6. Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

ladoDoQuadrado1 = float(
    input("informe o primeiro lado do quadrado em centímetros: "))
ladoDoQuadrado2 = float(
    input("informe o segundo lado do quadrado em centímetros: "))
areaDoQuadrado = ladoDoQuadrado1 * ladoDoQuadrado2
print("A área do quadrado é: %f cm²" % areaDoQuadrado)

# 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês

salarioHora = float(input("Informe o salário que você recebe por hora: R$"))
horaTrabalhadas = float(input("Informe o tempo trabalhado em horas por mês: "))
salarioMensal = salarioHora * horaTrabalhadas
print("O seu salário mensal é: R$ %f" % salarioMensal)

# 8. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celcius

temperaturaFahrenheit = float(
    input("Informe a temperatura em graus Fahrenheit: "))
temperaturaDeFahrenheitParaCelcius = (temperaturaFahrenheit-32)*100/180
print("A temperatura convertida é de %f °C" %
      temperaturaDeFahrenheitParaCelcius)


# 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre a temperatura em graus Fahrenheit

temperaturaFahrenheit = float(
    input("Informe a temperatura em graus Celsius: "))
temperaturaDeCelsiusParaFahrenheit = 1.8*temperaturaFahrenheit + 32
print("A temperatura convertida é de %f °F" %
      temperaturaDeCelsiusParaFahrenheit)

# 10. Faça um programa que peça dois números inteiros e um número real. Calcule e mostre:


# o produto do dobro do primeiro com metade do segundo
# a soma do triplo do primeiro com o terceiro
# o terceiro elevado ao cubo

numeroInteiro1 = float(input("Informe o primeiro número inteiro: "))
numeroInteiro2 = float(input("Informe o segundo número inteiro: "))
produtoDobroPrimeiroMetadeSegundo = (numeroInteiro1*2) * (numeroInteiro2/2)
somaTriploPrimeiroComTerceiro = produtoDobroPrimeiroMetadeSegundo + numeroInteiro1*3
cuboDoTerceiro = produtoDobroPrimeiroMetadeSegundo ** 3
print("O produto do dobro do primeiro com metade do segundo é: %f " %
      produtoDobroPrimeiroMetadeSegundo)
print("A soma do triplo do primeiro com o terceiro é: %f " %
      somaTriploPrimeiroComTerceiro)
print("O terceiro número ao cubo é: %f " % cuboDoTerceiro)

# 11. Tendo como dados de entrada a altura de uma pessoa, construa um algorítimo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura)-58

altura = float(input("Informe sua altura em centímetros: "))
pesoIdeal = (72.7 * altura/100) - 58
print("Seu peso ideal é: %f Kg" % pesoIdeal)

# 12. Tendo como dado de entrada a altura(h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: ((72.7*h)-58)
# Para mulheres: ((62.1*h)-44.7)

altura = float(input("Informe sua altura em centímetros: "))
sexo = str(input("Informe seu gênero(Masculino/Feminino): "))

if sexo == "Masculino":
    pesoIdeal = (72.7*altura/100) - 58
else:
    pesoIdeal = (62.1*altura/100) - 44.7

print("Seu peso ideal é: %f Kg" % pesoIdeal)

# 13. João Papo-de-Pescador... Imprima os dados do programa com as mensagens adequadas.

# regulamento SP = 50Kg (multa de R$4,00 por quilo a mais)

pesoPeixes = float(input(
    "Informe o peso, em Quilogramos, dos peixes pescados hoje:  "))
excessoDePeso = pesoPeixes - 50
if excessoDePeso > 0:
    multa = math.ceil(excessoDePeso)*4
    print("Você excedeu o peso máximo no valor de %f Kg" % excessoDePeso)
    print("Sua multa é de R$ %f " % multa)
else:
    print("Você não excedeu o peso máximo, portanto, não haverá multa ")

# 14. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros que a tinta é vendida em latas de 18 litros, que custam R$80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total
# lata de 18l - R$80,00 / 1l/3m³
areaParaPintar = float(
    input("Informe a área a ser pintada, em metros quadrados: "))
coberturaPorLata = 18*3
precoPorLata = 80
quantidadeDeLatas = math.ceil(float(areaParaPintar) / coberturaPorLata)
precoTotal = quantidadeDeLatas * precoPorLata
print("O total de latas a serem compradas são %f. O valor será de R$%f" %
      (quantidadeDeLatas, precoTotal))

# 15. Faça um programa que peça ao usuário seu CEP, e após a digitação do mesmo, imprima de qual estado o CEP é:

cep = int(input("Informe o CEP: "))

digitoDoEstado = int(str(cep)[:2])
if digitoDoEstado == 49:
    print("O CEP está no estado de Sergipe")
elif digitoDoEstado >= 1 and digitoDoEstado <= 19:
    print("O CEP está no estado de São Paulo")
elif digitoDoEstado >= 88 and digitoDoEstado <= 89:
    print("O CEP está no estado de Santa Catarina")
elif digitoDoEstado >= 90 and digitoDoEstado <= 99:
    print("O CEP está no estado do Rio Grande do Sul")
elif digitoDoEstado >= 20 and digitoDoEstado <= 28:
    print("O CEP está no estado do Rio de Janeiro")
