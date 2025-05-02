import random

# Questão 1: Manipulação de Listas

# Crie uma lista chamada frutas que contenha os nomes de pelo menos cinco frutas. Em seguida, escreva um programa que:

# Adicione uma nova fruta à lista.
# Remova uma fruta da lista.
# Imprima a lista final de frutas em ordem alfabética.

frutas = ["Banana","Jaboticaba","Limão","Morango","Pinha","Pêra", "Limão", "Jaboticaba"]
frutas.append("Abacaxi")
frutas.remove("Banana")
frutas.sort()
print(frutas)


# Questão 2: Contagem de Elementos

# Crie um dicionário chamado contagem_frutas que armazene a quantidade de cada fruta na lista criada na 
# Questão 1. O programa deve:
# Contar a ocorrência de cada fruta.
# Imprimir o dicionário resultante.

def criarFrutas(frutas):
    contagem_frutas = {}
    for fruta in frutas:
        quantidade = frutas.count(fruta)
        contagem_frutas[fruta] = quantidade
    return contagem_frutas

print(criarFrutas(frutas))



# Questão 3: Uso de Sets

# Escreva um programa que utilize um set para armazenar as frutas da lista da Questão 1. O programa deve:

# Adicionar mais algumas frutas, incluindo duplicatas.
# Imprimir o set, demonstrando que ele não permite duplicatas.
# Exibir a quantidade de frutas únicas.

frutas.extend(["Melão", "Uva", "Jaboticaba", "Uva"])
listaDeFrutas = set(frutas)
print(listaDeFrutas)

# Questão 4: Dicionários e Sets

# Crie um dicionário chamado estoque que armazene os nomes das frutas como chaves e suas 
# quantidades disponíveis como valores. O programa deve:

# Permitir que o usuário adicione frutas e quantidades ao dicionário.
# Imprimir o dicionário final mostrando todas as frutas e suas quantidades.
estoque = criarFrutas(frutas)
def adicionarFruta(dicionario, fruta, quantidade):
    dicionario[fruta] = quantidade 
def removerFruta(dicionario, fruta):
    del dicionario[fruta] 
adicionarFruta(estoque,"Melancia", "6")
removerFruta(estoque,"Uva")
print(estoque)

# Questão 5: Relacionando Listas e Dicionários
# Crie uma lista chamada compras que armazene os nomes das frutas que o usuário deseja comprar. O programa deve:

# Comparar essa lista com o dicionário estoque.
# Imprimir quais frutas estão disponíveis e quais não estão, com base na lista de compras.


def colocarCarrinho():
    compras = set()
    while True:
        fruta = input("Informe a fruta que deseja inserir na sua lista de compras: ").strip().lower().capitalize()
        compras.add(fruta)
        sair = input("Deseja sair da lista de compras? (S para caso queira sair) ").upper()
        if sair == "S":
            break
    for fruta in compras:
        if fruta in estoque:
            print(f"{fruta} está disponível")
        else:
            print(f"{fruta} não está disponível")
colocarCarrinho()
