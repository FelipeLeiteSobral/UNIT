# A prefeitura de uma cidade deseja realizar uma pesquisa entre seus habitantes para avaliar
# oportunidades para os cidadãos. Você foi contratado para ajudar nessa iniciativa desenvolvendo um
# programa em Python que permita a coleta dos dados dos responsáveis de cada residência. O programa
# deve coletar as seguintes informações:
# Nome do responsável. Salário do responsável. Após a coleta das informações, o programa deverá
# exibir:
# a) A relação dos nomes das pessoas com salário superior a R$1.000,00.
# b) A média de salário dos responsáveis entrevistados.
# c) O nome do responsável com o maior salário entre os entrevistados.


def cadastrarUsuario():
    listaHabitantes = {}
    while True:
        nomeUsuario = input("Informe seu nome: ")
        try:
            salarioUsuario = float(input("Informe seu salário: R$"))
        except ValueError:
            print("Salário inválido. Tente novamente inserindo um número.")
            continue
        listaHabitantes[nomeUsuario] = salarioUsuario
        sair = input("Digite 'S' para sair do cadastro: ").strip().upper()
        if sair == "S":
            break
    for nome, salario in listaHabitantes.items():
        if salario > 1000:
            print(f"- {nome} : {salario} ")
    mediaSalarios = sum(listaHabitantes.values())/(len(listaHabitantes))
    print(f"A média dos salários dos responsáveis é {mediaSalarios:.2f}")
    maiorSalario = max(listaHabitantes, key=listaHabitantes.get)
    print(f"O maior salário é de {maiorSalario} \n")
    return listaHabitantes
cadastrarUsuario()


# Em determinada universidade o professor de Engenharia elaborou uma prova objetiva
# composta de 6 questões, todas elas com cinco opções de resposta. Além disso estabeleceu que as qua-
# tro primeiras valem 1,5 pontos cada e as duas últimas valem 2,0 pontos cada. A média mínima para a
# aprovação é de 6,0 pontos. Para otimizar a correção, o professor solicitou aos alunos de programação
# um programa em Python com as seguintes características:

# • O programa deve permitir o cadastramento do gabarito da prova (por exemplo: questão 1, res-
# posta a; questão 2, resposta b; questão 3, resposta d, etc); (0,1)

# • O programa deve solicitar a quantidade de alunos que realizaram a prova, e permitir o cadastra-
# mento da matrícula, do nome do aluno e das suas 6 respostas. (0,3)

# Ao término da digitação o programa deve imprimir:
# a) O gabarito da prova; (0,1)
# b) Relatório com a matrícula, nome, respectivas respostas e nota obtida por cada aluno; (1,0)

def cadastrarGabarito():
    gabarito = {}
    print("Cadastro do Gabarito da Prova")
    for questao in range(1, 7):
        while True:
            resposta = input(f"Informe a resposta da questão {questao} (a, b, c, d ou e): ").strip().lower()
            if resposta in ['a', 'b', 'c', 'd', 'e']:
                gabarito[questao] = resposta
                break
            else:
                print("Resposta inválida. Digite apenas a, b, c, d ou e.")
    return gabarito

def calcularNota(respostas, gabarito):
    nota = 0
    for i in range(1, 7):
        if respostas[i - 1] == gabarito[i]:
            if i <= 4:
                nota += 1.5
            else:
                nota += 2.0
    return nota

def cadastrarAlunos(gabarito):
    alunos = []
    qtd = int(input("Quantos alunos fizeram a prova? "))

    for _ in range(qtd):
        print("\nCadastro do aluno:")
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        respostas = []

        for questao in range(1, 7):
            while True:
                resp = input(f"Resposta da questão {questao}: ").strip().lower()
                if resp in ['a', 'b', 'c', 'd', 'e']:
                    respostas.append(resp)
                    break
                else:
                    print("Resposta inválida. Digite apenas a, b, c, d ou e.")
        
        nota = calcularNota(respostas, gabarito)
        alunos.append({
            "matricula": matricula,
            "nome": nome,
            "respostas": respostas,
            "nota": nota
        })

    return alunos

def exibirRelatorio(gabarito, alunos):
    print("\nGabarito da Prova:")
    for q, resp in gabarito.items():
        print(f"Questão {q}: {resp}")

    print("\nResposta dos Alunos:")
    for aluno in alunos:
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Respostas: {aluno['respostas']}")
        print(f"Nota: {aluno['nota']:.2f}")

gabarito = cadastrarGabarito()
alunos = cadastrarAlunos(gabarito)
exibirRelatorio(gabarito, alunos)

# #  Construa um programa que receba do usuário o valor do salário mínimo atual. Na sequência,
# # o programa deve solicitar que o usuário informe o valor do seu salário mensal. Ao fim, o programa
# # deve calcular a quantidade de salários mínimos recebidos pelo usuário.

def calcularSalariosMinimos():
    try:
        salario_minimo = float(input("\nInforme o valor do salário mínimo atual: R$ "))
        salario_usuario = float(input("Informe o valor do seu salário mensal: R$ "))

        if salario_minimo <= 0:
            print("O valor do salário mínimo deve ser maior que zero.")
            return

        qtd_salarios = salario_usuario / salario_minimo

        print(f"\nVocê recebe aproximadamente {qtd_salarios:.2f} salários mínimos.")

    except ValueError:
        print("Por favor, informe apenas números válidos.")

calcularSalariosMinimos()


# uma loja de roupas está vendendo camisas básicas com descontos, mas seus funcionários
# têm dificuldades no cálculo do valor final a ser cobrado. Por isso, seu Tanaka, dono da loja, convidou
# você para criar um programa para calcular o preço final a partir do número de camisas. Seu Tanaka
# definiu as seguintes regras de desconto:
# Até 5 camisas, desconto de 3%
# Acima de 5 camisas e até 10 camisas, desconto de 5%; e
# Acima de 10 camisas, desconto de 7%.

def valorTotal():
    valorCamisa = float(input("Informe o valor da camisa: "))
    quantidadeCamisa = int(input("Informe a quantidade de camisas a serem compradas: "))
    if quantidadeCamisa <6:
        precoTotal = quantidadeCamisa * valorCamisa * 0.97
        valorDesconto = (quantidadeCamisa * valorCamisa - precoTotal)
    elif quantidadeCamisa < 11:
        precoTotal = quantidadeCamisa * valorCamisa * 0.95
        valorDesconto = (quantidadeCamisa * valorCamisa - precoTotal)
    else:
        precoTotal = quantidadeCamisa * valorCamisa * 0.93
        valorDesconto = (quantidadeCamisa * valorCamisa - precoTotal)
    print(f"O valor total é de R${precoTotal:.2f}, com desconto de R${valorDesconto}")

valorTotal()