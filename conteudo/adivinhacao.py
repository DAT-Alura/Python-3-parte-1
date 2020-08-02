import random

print("*************************************")
print("* Bem vindo no jogo de Adivinhação! *")
print("*************************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você chutou ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100", end="\n\n")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print(
                "Você errou! O seu chute foi maior do que o número secreto.",
                end="\n\n"
            )
        elif(menor):
            print(
                "Você errou! O seu chute foi menor do que o número secreto.",
                end="\n\n"
            )

print("Fim do jogo!")
