import random


def jogar():
    print("")
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")
    print("")

    numero_secreto = random.randrange(1, 101)

    print("Qual o nível de dificuldade?")
    print("(1) Fácil, (2) médio, (3) difícil")

    dificuldade = int(input("digite o número da dificuldade: "))

    if dificuldade == 1:
        total_de_tentativas = 20
    elif dificuldade == 2:
        total_de_tentativas = 10
    elif dificuldade == 3:
        total_de_tentativas = 5
    else:
        print("")
        print("número inválido!")
        print("")
        total_de_tentativas = 0

    pontuacao = 1000

    for rodada in range(1, total_de_tentativas + 1):
        print("")
        print("******************")
        print("")
        print("tentativa {} de {}".format(rodada, total_de_tentativas))
        print("")
        chute = int(input("Digite o seu número entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print("o número deve ser entre 1 e 100!")
            continue

        if numero_secreto == chute:
            print("")
            print("Você acertou!! Sua pontuação é {}".format(pontuacao))
            break
        elif chute > numero_secreto:
            print("O número é menor")
        else:
            print("o número é maior")

        pontuacao = pontuacao - abs(numero_secreto - chute)

    print("")
    print("**************")
    print("O jogo acabou!")
    print("**************")


if __name__ == "__main__":
    jogar()
