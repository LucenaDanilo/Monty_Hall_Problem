# Mostrando na "força bruta" o Monty Hall Paradox

from random import randrange

print("\nSIMULAÇÃO MONTY HALL!\n")
n = int(input("Insira a quantidade de vezes que você deseja que o programa simule um jogo!\n"))

acertou_mantendo = 0
errou_mantendo = 0

acertou_trocando = 0
errou_trocando = 0

for i in range(n):
    porta_correta = randrange(3)
    chute_fixo = randrange(3)
    
    while True:
        porta_aberta = randrange(3)
        if porta_aberta != porta_correta and porta_aberta != chute_fixo:
            if porta_aberta in [0, 1] and chute_fixo in [0, 1]:
                novo_chute = 2
            elif porta_aberta in [0, 2] and chute_fixo in [0, 2]:
                novo_chute = 1
            else:
                novo_chute = 0
            break

    if porta_correta == chute_fixo:
        acertou_mantendo += 1
    else:
        errou_mantendo += 1

    if novo_chute == porta_correta:
        acertou_trocando += 1
    else:
        errou_trocando += 1
    
print("\nTrocando: ")
print("acertos:", acertou_trocando, "erros:", errou_trocando, "|", "{:.2f}%".format(acertou_trocando/n*100))

print("\nMantendo: ")
print("acertos:",acertou_mantendo, "erros:", errou_mantendo, "|", "{:.2f}%".format(acertou_mantendo/n*100))