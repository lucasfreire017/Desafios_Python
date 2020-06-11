from random import randint
from time import sleep
import emoji

emoji_pedra = (emoji.emojize(':fist:', use_aliases=True))
emoji_papel = (emoji.emojize('\033[30m:wave:\033[m', use_aliases=True))
emoji_tesoura = (emoji.emojize('\033[33m:v:\033[m', use_aliases=True))

d = '\033[1;36m-\033[m\033[1;31m=\033[m'
print('{:-^40}'.format(' JOKENPO '))

while True:
    PC = randint(1, 3)
    print(emoji.emojize('''
\033[1;32mOpções:\033[m
{}
[\033[1;30m1\033[m] PEDRA \033[37m:fist:\033[m
[\033[1;30m2\033[m] PAPEL \033[30m:wave:\033[m
[\033[1;30m3\033[m] TESOURA \033[33m:v:\033[m''', use_aliases=True).format(d * 7))

    jogador = int(input('Digite sua opção: '))

    #---------------------------
    if PC == 1 and jogador == 1:
        PC1 = emoji_pedra
        jogador1 = emoji_pedra
        v = '\033[1;34mEMPATE\033[m'
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print('-=' * 10)
        print('\033[36mJogador\033[m jogou: {}'.format(jogador1))
        print('\033[35mNotebook\033[m jogou: {}'.format(PC1))
        print('-=' * 10)
        print(v)

    elif PC == 2 and jogador == 2:
        PC1 = emoji_papel
        jogador1 = emoji_papel
        v = '\033[1;34mEMPATE\033[m'
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print('-=' * 10)
        print('\033[36mJogador\033[m jogou: {}'.format(jogador1))
        print('\033[35mNotebook\033[m jogou: {}'.format(PC1))
        print('-=' * 10)
        print(v)

    elif PC == 3 and jogador == 3:
        PC1 = emoji_tesoura
        jogador1 = emoji_tesoura
        v = '\033[1;34mEMPATE\033[m'
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print('-=' * 10)
        print('\033[36mJogador\033[m jogou: {}'.format(jogador1))
        print('\033[35mNotebook\033[m jogou: {}'.format(PC1))
        print('-=' * 10)
        print(v)

    #----------------------------
    elif PC == 1 and jogador == 2:
        jogador1 = emoji_papel
        PC1 = emoji_pedra
        v = 'Vencedor: \033[1;36mJOGADOR\033[m'
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print('-=' * 10)
        print('\033[36mJogador\033[m jogou: {}'.format(jogador1))
        print('\033[35mNotebook\033[m jogou: {}'.format(PC1))
        print('-=' * 10)
        print(v)

    elif PC == 2 and jogador == 3:
        jogador1 = emoji_tesoura
        PC1 = emoji_papel
        v = 'Vencedor: \033[1;36mJOGADOR\033[m'
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print('-=' * 10)
        print('\033[36mJogador\033[m jogou: {}'.format(jogador1))
        print('\033[35mNotebook\033[m jogou: {}'.format(PC1))
        print('-=' * 10)
        print(v)

    elif PC == 3 and jogador == 1:
        jogador1 = emoji_pedra
        PC1 = emoji_tesoura
        v = 'Vencedor: \033[1;36mJOGADOR\033[m'
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print('-=' * 10)
        print('\033[36mJogador\033[m jogou: {}'.format(jogador1))
        print('\033[35mNotebook\033[m jogou: {}'.format(PC1))
        print('-=' * 10)
        print(v)
    #-----------------------------
    elif PC == 1 and jogador == 3:
        PC1 = emoji_pedra
        jogador1 = emoji_tesoura
        v ='Vencedor: \033[1;35mNotebook\033[m'
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print('-=' * 10)
        print('\033[36mJogador\033[m jogou: {}'.format(jogador1))
        print('\033[35mNotebook\033[m jogou: {}'.format(PC1))
        print('-=' * 10)
        print(v)

    elif PC == 2 and jogador == 1:
        PC1 = emoji_papel
        jogador1 = emoji_pedra
        v ='Vencedor: \033[1;35mNotebook\033[m'
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print('-=' * 10)
        print('\033[36mJogador\033[m jogou: {}'.format(jogador1))
        print('\033[35mNotebook\033[m jogou: {}'.format(PC1))
        print('-=' * 10)
        print(v)

    elif PC == 3 and jogador == 2:
        PC1 = emoji_tesoura
        jogador1 = emoji_papel
        v ='Vencedor: \033[1;35mNotebook\033[m'
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print('-=' * 10)
        print('\033[36mJogador\033[m jogou: {}'.format(jogador1))
        print('\033[35mNotebook\033[m jogou: {}'.format(PC1))
        print('-=' * 10)
        print(v)

    else:
        print('\033[1;31mOPÇÃO INVÁLIDA\033[m')

    cont = input('\033[1mVocê deseja continuar? [\033[m\033[1;32mS\033[m\033[1m/\033[m\033[1;31mN\033[m\033[1m]\033[m: ').upper()[0]

    if cont not in 'Ss':
        print('\033[36;1mJogo Finalizado\033[m')
        break
