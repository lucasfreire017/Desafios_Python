from random import randint
from time import sleep
computador = randint(0,10)
print('\033[32m-=-'*20)
print('\033[34mVou pensar em um número entre 0 e 10. Tente Adivinhar...\033[m')
print('\033[32m-=-\033[m'*20)
jogador = int(input('Palpite:'))
print('\033[36mPROCESSANDO...\033[m')
sleep(3)
if jogador == computador:
    print('PARABÉS!, você ganhou!.')
else:
    print('GANHEI! eu pensei no número {} e não no {}.'.format(computador, jogador))
