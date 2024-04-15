import random


def jogar():
    mensagem_abertura()

    palavra_secreta = gera_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = pede_chute_jogador()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!!!")
    else:
        print("Você perdeu")

    print("Fim do jogo")


def mensagem_abertura():
    print("")
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print("")


def gera_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_secreta = random.choice(palavras)
    palavra_secreta = palavra_secreta.upper()
    return palavra_secreta


def pede_chute_jogador():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1
    return letras_acertadas


if __name__ == "__main__":
    jogar()
