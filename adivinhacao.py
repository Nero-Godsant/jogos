print ("Bem vindo no jogo de Adivinhação!")

numero_secreto = 74
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite seu numero: ")
    print("Voce digitou ", chute)
    chute = int(chute)

    if(chute < 1 or chute > 100):
        print("voce deve digitar um numero entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (numero_secreto == chute):
        print("Voce acertou")
        break
    else:
        if (maior):
            print("Voce errou! O seu chute foi maior que o numero secreto.")
        elif (menor):
            print("Voce errou! O seu chute foi menor que o numero secreto.")

    rodada = rodada + 1

print("Fim do jogo")