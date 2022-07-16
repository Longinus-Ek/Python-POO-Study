import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha seu jogo!*********")
    print("*********************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Escolha o jogo: "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()  # Usado para chamar uma função criada
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()


if (__name__ == "__main__"):
    escolhe_jogo()
