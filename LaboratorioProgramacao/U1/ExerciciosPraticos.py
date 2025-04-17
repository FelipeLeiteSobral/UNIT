# Exercício 1
usuario = input("Qual seu nome? ")
idade = float(input("Qual sua idade? "))

print(f"O nome do usuário é {usuario}, e ele(a) tem {idade} ")

# Exercício 2
nota1 = float(input("Informe a primeira nota? "))
nota2 = float(input("Informe a segunda nota? "))
media = (nota1 + nota2) / 2

if media >= 6:
    print(f"A média das notas é: {media:.2f}, você foi aprovado(a)")
else:
    print(f"A média das notas é: {media:.2f}, você foi reprovado(a)")

# Exercício 3
pesoUsuario = float(input("Informe o seu peso em quilogramas? "))
alturaUsuario = float(input("Informe o sua altura em centímetros? "))
imc = pesoUsuario/(alturaUsuario/100)**2
print(f"O Indice de massa corporal é: {imc}")