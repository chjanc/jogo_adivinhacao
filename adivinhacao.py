import random

print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_tentativas = 0
rodada = 1
pontos = 1000

print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = input("Digite um número entre 1 e 100: ")
    numero = int(chute)
    print("Você digitou: ", chute)

    if(numero < 1 or numero > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = numero == numero_secreto
    chute_maior = numero > numero_secreto
    chute_menor = numero < numero_secreto

    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        pontos_perdidos = abs(numero_secreto - numero)
        pontos = pontos - pontos_perdidos
        if(chute_maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
            if (rodada == total_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
        elif(chute_menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            if (rodada == total_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
        rodada = rodada + 1

print("Fim do jogo.")
