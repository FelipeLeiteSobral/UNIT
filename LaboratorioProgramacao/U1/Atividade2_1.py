# Você está iniciando um novo negócio: uma locadora de veículos. Para iniciar o controle do aluguel de carros 
# é necessário um sistema simples. Dessa forma, desenvolva um programa em Python para:

# a) Solicitar ao usuário informações sobre as locações: nome do cliente, sexo (F – Feminino, M – Masculino), 
# placa do carro alugado, quantidade de quilômetros contratados, quantidade de dias contratados;
def solicitacaoUsuario():
    usuario = {"nome":str, "sexo":str, "placa":str,"quilometrosContratados":int,"diasContratados":float}

    usuario["nome"] = input("Informe seu nome completo: ")
    usuario["sexo"] = input("Informe o sexo (F – Feminino, M – Masculino): ").upper()
    usuario["placa"] = input("Informe a placa do carro alugado: ")
    usuario["quilometrosContratados"] = int(input("Informe a quantidade de quilômetros contratados: "))
    usuario["diasContratados"] = int(input("Informe a quantidade de dias contratados: "))
    
    return  usuario


# b) Calcular e imprimir a placa do carro e valor total a pagar para CADA cliente, considerando que deverá ser 
# cobrado o valor de R$ 70,00 por dia contratado, e R$ 0,10 para cada quilômetro contratado;

def cobrarMulta(listaClientes):
    listaClientes = []
    for cliente in listaClientes:
        multaPorDias = cliente["diasContratados"] * 70
        multaPorQuilometros = cliente["quilometrosContratados"] * 0.10
        totalPagar = multaPorDias + multaPorQuilometros
        print(f"Placa do carro: {cliente['placa']}, Valor total a pagar: R$ {totalPagar:.2f}")
    return

# c) Calcular e imprimir a média de quilômetros contratados pelos clientes;

def mediaQuilometrosContratados(listaClientes):
    for cliente in listaClientes:
        totalQuilometros = 0
        totalQuilometros += cliente["quilometrosContratados"]
    media = totalQuilometros / len(listaClientes)
    return print(f"A média dos quilômetros contratados dos clientes é {media:.2f}")

# d) Calcular e imprimir o nome das clientes de sexo feminino que fecharam aluguéis acima de 7 dias contratados.

def clientesFemininosAcimaDeSeteDias(listaClientes):
    for cliente in listaClientes:
        if cliente["sexo"] == "F" and cliente["diasContratados"] > 7:
            print(f"Nome da cliente do sexo Feminino que contratou um veículo por mais de 7 dias: {cliente['nome']}")
    return

# Obs.: o programa encerra quando o usuário informa o texto SAIR.

def sistemaLocadoraVeiculos():
    valorEntrada = "SIM"
    listaClientes = []
    while valorEntrada != "SAIR":
        valorEntrada = input("Você gostaria de cadastrar algum cliente?(caso não, digite 'SAIR', caso deseje, digite 'SIM') ").upper()
        if valorEntrada == "SIM":
            listaClientes.append(solicitacaoUsuario())
            print("Cliente cadastrado com sucesso!")
        elif valorEntrada != "SAIR":
            print("Valor inválido! Por favor, digite 'SIM' ou 'SAIR'")
        else:
            valorEntrada
    if len(listaClientes) > 0:
        cobrarMulta(listaClientes)
        mediaQuilometrosContratados(listaClientes)
        clientesFemininosAcimaDeSeteDias(listaClientes)
        return listaClientes
    return            

sistemaLocadoraVeiculos()

