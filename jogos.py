import forca
import adivinhacao


def escolher_jogo():
    print("")
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")
    print("")
    print("(1) Forca (2) Adivinhação")
    print("")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("")
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        print("")
        print("Jogando adivinhação")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolher_jogo()