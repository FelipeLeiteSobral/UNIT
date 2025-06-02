# 1. Escreva um algoritmo que leia o número de andares de um prédio e, a seguir, para cada andar do prédio, 
# leia o número de pessoas que entraram e saíram do elevador. 
# Considere que o elevador está vazio e está subindo, os dados se referem a apenas uma subida 
# do elevador e que o número de pessoas
# dentro do elevador será sempre maior ou igual a zero.
# Se o número de pessoas, após a entrada e saída, for maior que 15, deve ser mostrada a mensagem “Excesso 
# de Passageiros. Devem sair X”, sendo X
# o número de pessoas que devem sair do elevador, de modo que seja obedecido o limite de 15 passageiros. 
# Após a entrada e saída no último andar, o
# algoritmo deve mostrar quantas pessoas permaneceram no elevador para descer.
quantidadeElevador = 0
andarCorrente = 0
def definirPredio():
    try: 
        numeroAndares = int(input("Informe a quantidade de andares do prédio: "))
        listaAndares = []
        for i in range(0, numeroAndares):          
            listaAndares.append(i) 
    except ValueError:
        print("Informe um valor numérico inteiro.")   
    return numeroAndares

def chamarElevador(quantidadeElevador, andarCorrente):
    for andarCorrente in range(0, numeroAndares):
        try:
            print()
            print(f"====================== Andar: {andarCorrente} ======================")
            pessoasSaindo = int(input("Quantas pessoas estão saindo do elevador? "))
            quantidadeElevador = quantidadeElevador - pessoasSaindo
            if quantidadeElevador < 0:
                quantidadeElevador = 0
                raise ValueError
            pessoasEntrando = int(input("Quantas pessoas estão entrando no elevador? "))
            quantidadeElevador = quantidadeElevador + pessoasEntrando
            if  andarCorrente < 0 or andarCorrente > numeroAndares:
                raise ValueError
            if quantidadeElevador > 15:
                quantidadeElevador = 15
                print("Lotação máxima, o elevador chegou a 15 pessoas!")
        except ValueError:
            print("O número de pessoas do elevador não pode ficar negativo.")
        print(f"Pessoas no elevador: {quantidadeElevador}")
    return quantidadeElevador, andarCorrente

numeroAndares = definirPredio()
quantidadeElevador, andarCorrente = chamarElevador(quantidadeElevador, andarCorrente)
print(quantidadeElevador)

# 2. Desenvolva um programa que exiba a tabuada dos números de 10 a 20, tendo como base os números de 1 a 10. 
# Por exemplo: 10x1, 10x2, 10x3, 10x..
# 10x10.

# 3. Elabore um algoritmo que solicite dois números inteiros até que o primeiro não seja divisível pelo segundo. Você deverá informar ao final quantos
# números digitados são divisíveis.

# 4. Crie um algoritmo que mostre todos os números pares existentes entre 1 e 50.

# 5. Dada uma lista com o número do aluno, número da matéria e nota do aluno de uma turma com 10 alunos e 
# 3 matérias, sabendo que os números dos
# alunos variam de 1 a 10 e os números das matérias de 101 a 103, faça um algoritmo que escreva o número 
# dos alunos que tiveram a nota maior que
# cinco na matéria 101 e nota maior que sete nas matérias 102 e 103.

# 6. Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
# a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00.
# b. Em 1996, recebeu um aumento de 1,5% sobre seu salário inicial.
# c. A partir de 1997 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do 
# ano anterior.

# 7. Um comerciante deseja saber qual é o lucro percentual que ele está obtendo com a venda diária de 
# mercadorias. Calcule o lucro percentual diário ao
# serem fornecidos o preço de compra e o preço de venda das mercadorias. A entrada de dados será finalizada 
# quando o código do produto receber o valor
# Fim.

# 8. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
# Foram obtidos os seguintes dados:
# a. Código da cidade;
# b. Número de veículos de passeio (em 1999);
# c. Número de acidentes de trânsito com vítimas (em 1999).
# Deve-se saber:
# a. Qual o maior e menor índice de acidentes de trânsito e a que cidades pertencem;
# b. Qual a média de veículos nas cinco cidades juntas;
# c. Qual a média de acidentes de trânsito nas cidades com menor de 2.000 veículos de passeio.

# 9. Uma empresa possui dez funcionários com as seguintes características: código, número de horas 
# trabalhadas no mês, turno de trabalho (M – Matutino; V
# – Vespertino ou N – Noturno), categoria (O – Operário ou G – Gerente), valor da hora trabalhada. 
# Sabendo-se que essa empresa deseja informatizar sua
# folha de pagamento, elabore um programa que:
# a. Leia as informações dos funcionários, exceto o valor da hora trabalhada, não permitindo que sejam 
# informados turnos nem categorias existentes.
# Assuma que será trabalhado sempre com a digitação de letras maiúsculas;
# b. Calcule o valor da hora trabalhada, conforme a tabela a seguir:

# Adote o valor vigente para o salário mínimo.
# c. Calcule o salário inicial dos funcionários com base no valor da hora trabalhada e no número de horas 
# trabalhadas;
# d. Calcule o valor do auxílio-alimentação recebido por funcionário de acordo com o seu salário inicial, 
# conforme a tabela a seguir:

# e. Mostre o código, número de horas trabalhadas, valor da hora trabalhada, salário inicial, 
# auxílio-alimentação e o salário final (salário inicial + auxílio-
# alimentação).