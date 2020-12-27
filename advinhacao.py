import os
import time
import random

os.system('cls')  # Limpa o terminal.
print("\n\n\n\tBem vindo ao jogo de advinhação!")
print("\n       Neste jogo, você tem três chances\n\tpara advinhar o numero correto.\n\tEsse numero está entre 0 a 10.")
input("\n\tAperte enter para continuar...")
os.system('cls')
numero_secreto = random.randint(0, 10)
acertou = False
tentativa = 1

while tentativa < 4:

    try:
        chute = int(input("\n\n\n\n\t     Tentativa numero {}\n     Digite um numero entre 0 a 10: ".format(tentativa)))
        # Formata a string, alterando a quantidade de tentativas toda vez que for alterada.

    except ValueError:
        print("\n\n\n  Por favor, siga as intruções corretamente!")
        time.sleep(3)
        os.system('cls')
        continue

    if chute < 0 or chute > 10:
        print("\n\t Por favor, digite um numero\n\tmaior que zero e menor que 10")
        time.sleep(3)
        os.system('cls')
        continue
    elif chute > numero_secreto:
        print("\n\n\tEsse não é o numero correto!\n\n      O seu chute foi acima do número.\n")
    elif chute < numero_secreto:
        print("\n\n\tEsse não é o numero correto!\n\n      O seu chute foi abaixo do número.\n")
    else:
        os.system('cls')
        print("\n\n\n\n\n      Parabéns, você acertou o numero!")
        acertou = True
        break

    input("\n       Aperte enter para continuar...")
    tentativa += 1
    os.system('cls')

if not acertou:
    print("\n\n\n\n\n\tVocê não acertou o numero!")

print("\n\n\t       Fim do jogo!")
time.sleep(5)  # Faz o terminal esperar 5 segundos.
os.system('cls')
