import random

def jogar():
    # Variáveis
    enforcou = False
    acertou = False
    erradas = []
    erros = 0
    imprime_abertura()
    palavra_secreta = carregar_palavra()
    letras_acertadas = iniciar_letras_acertadas(palavra_secreta)
    desenhar_forca(erros, erradas)
    escrever_letras_acertadas(letras_acertadas)




    while(not enforcou and not acertou):

        chute = pedir_chute()
        if(chute.isdigit()):
            print("Digite apenas letras!")
            desenhar_forca(erros, erradas)
        else:
            if(chute in palavra_secreta):
                marcar_letras_corretas(chute, palavra_secreta, letras_acertadas)
                desenhar_forca(erros, erradas)
            elif(chute in erradas):
                print("Você já digitou essa letra!!")
                desenhar_forca(erros, erradas)
            else:
                erradas.append(chute)
                erros += 1
                desenhar_forca(erros, erradas)




            enforcou = erros == 6
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)

    if(acertou):
        escrever_mensagem_ganhador()
    else:
        escrever_mensagem_perdedor(palavra_secreta)

def imprime_abertura():
    print("\n*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************\n")

def carregar_palavra():
    arquivo = open("frutas.txt", "r")
    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta

def iniciar_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pedir_chute():
    chute = input("Escolha uma letra: ")
    chute = chute.strip().upper()
    return chute

def escrever_letras_acertadas(escrever):
    escrever = print("\n", escrever, "\n")
    return escrever

def marcar_letras_corretas(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def escrever_mensagem_ganhador():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def escrever_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!\n")
    print("A palavra era {}\n".format(palavra_secreta))
    print("     _______________         ")
    print("    /               \       ")
    print("   /                 \      ")
    print("/\/                   \/\  ")
    print("\ |   XXXX     XXXX   | /   ")
    print(" \|   XXXX     XXXX   |/     ")
    print("  |   XXX       XXX   |      ")
    print("  |                   |      ")
    print("  \__      XXX      __/     ")
    print("    |\     XXX     /|       ")
    print("    | |           | |        ")
    print("    | I I I I I I I |        ")
    print("    |  I I I I I I  |        ")
    print("    \_             _/       ")
    print("      \_         _/         ")
    print("        \_______/           ")

def desenhar_forca(erros, erradas):
    letra_errada = erradas

    if(erros == 0):
        print("  _______     ", "Letras erradas")
        print(" |/      |    ", letra_errada)
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    if(erros == 1):
        print("  _______     ", "Letras erradas")
        print(" |/      |    ", letra_errada)
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")

    if(erros == 2):
        print("  _______     ", "Letras erradas")
        print(" |/      |    ", letra_errada)
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")

    if(erros == 3):
        print("  _______     ", "Letras erradas")
        print(" |/      |    ", letra_errada)
        print(" |      (_)   ")
        print(" |      \ /   ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")

    if(erros == 4):
        print("  _______     ", "Letras erradas")
        print(" |/      |    ", letra_errada)
        print(" |      (_)   ")
        print(" |      \ /   ")
        print(" |       |    ")
        print(" |            ")
        print("_|___         ")
    if(erros == 5):
        print("  _______     ", "Letras erradas")
        print(" |/      |    ", letra_errada)
        print(" |      (_)   ")
        print(" |      \ /   ")
        print(" |       |    ")
        print(" |      /     ")
        print("_|___         ")
    if (erros == 6):
        print("  _______     ", "Letras erradas")
        print(" |/      |    ", letra_errada)
        print(" |      (_)   ")
        print(" |      \ /   ")
        print(" |       |    ")
        print(" |      / \   ")
        print("_|___         ")

if(__name__ == "__main__"):
    jogar()