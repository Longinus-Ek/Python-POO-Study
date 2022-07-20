import random #Biblioteca random

def jogar(): #Criando função para chamar código

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101) #Gerando número de 1 a 100
    chute = 0
    total_de_tentativas = 3
    pontos = 300

    print("Qual nível de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        maior = chute > numero_secreto
        menor = chute < numero_secreto
        acertou = numero_secreto == chute

        print("Você Digitou", chute)

        if(acertou):
            print("Você Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você Errou!! O número é menor")
            elif (menor):
                print("Você Errou!! O número é maior")
            pontos_perdidos = abs(numero_secreto - chute) #Cálculo valor absoluto (Módulo) 40-60 = 20 pontos perdidos
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")
    print("O numero era {}".format(numero_secreto))

if(__name__ == "__main__"):
    jogar()