from random import randint
pc = randint(0, 100)
cores = '\033[1;31m-\033[m\033[1;36m-\033[m'
jogador = int(input('\033[1mPensei em um número. Tente Adivinhar!\033[m\n'
                    'Palpite:'))
cont = 0
while jogador != pc:
    if pc > jogador:
        print('{}'.format(cores * 11))
        print('\033[1;31mChute um valor MAIOR!\033[m')
        jogador = int(input('Palpite: '))
        cont += 1
    else:
        print('{}'.format(cores * 11))
        print('\033[1;32mChute um valor MENOR!\033[m')
        jogador = int(input('Palpite: '))
        cont += 1
print('{}'.format(cores * 11))
print('\033[1;32mPARABÉNS!!!\033[m \033[1mVocê acertou com\033[m \033[1;35m{}\033[m \033[1mtentativas.\033[m'.format(cont + 1))
