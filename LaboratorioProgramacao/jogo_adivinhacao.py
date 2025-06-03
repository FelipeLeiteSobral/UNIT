import random

def jogoAdivinhacao():
    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 5
    
    print("🎯 BEM-VINDO AO JOGO DE ADIVINHAÇÃO! 🎯")
    print("=" * 40)
    print("Eu pensei em um número entre 1 e 100.")
    print(f"Você tem {tentativas} tentativas para adivinhar!")
    print("=" * 40)
    
    for tentativa in range(1, tentativas + 1):
        print(f"\n🔢 Tentativa {tentativa}/{tentativas}")
        
        try:
            # Solicita o palpite do jogador
            palpite = int(input("Digite seu palpite: "))
            
            # Verifica se o palpite está correto
            if palpite == numero_secreto:
                print(f"🎉 PARABÉNS! Você acertou!")
                print(f"O número era {numero_secreto}!")
                print(f"Você conseguiu em {tentativa} tentativa(s)!")
                return
            elif palpite < numero_secreto:
                print("📈 Muito baixo! Tente um número maior.")
            else:
                print("📉 Muito alto! Tente um número menor.")
            # Mostra quantas tentativas restam
            restantes = tentativas - tentativa
            if restantes > 0:
                print(f"Tentativas restantes: {restantes}")
        except ValueError:
            print("❌ Por favor, digite apenas números!")
            continue
    
    # Se chegou aqui, o jogador perdeu
    print(f"\n💔 Que pena! Suas tentativas acabaram.")
    print(f"O número secreto era: {numero_secreto}")
    print("Tente novamente!")

# Executa o jogo
if __name__ == "__main__":
    jogoAdivinhacao()
    
    # Pergunta se quer jogar novamente
    while True:
        jogar_novamente = input("\n🔄 Quer jogar novamente? (s/n): ").lower()
        if jogar_novamente == 's':
            print("\n" + "="*50)
            jogoAdivinhacao()
        elif jogar_novamente == 'n':
            print("👋 Obrigado por jogar! Até a próxima!")
            break
        else:
            print("Digite 's' para sim ou 'n' para não.")