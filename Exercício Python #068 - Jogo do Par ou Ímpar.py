from random import randint
cont = 0
linha = '\033[1;m-\33[m\033[1;37m-\033[m'
while True:
    jogador = int(input('Diga um valor: '))
    opção = input('Par ou Impar? [P/I] ').strip()[0]
    while not opção in 'PpIi':
        print('\033[1;31mDADOS INCORRETOS\033[m \033[31mTente Novamente.\033[m')
        opção = input('Par ou Impar? [P/I] ')
    computador = randint(0, 10)
    soma = jogador + computador
    print(f'{linha}' * 30)
    print(f'Você jogou {jogador} e computador jogou {computador}. Total de {soma}', end=' ')
    print('\033[1mDEU PAR\033[m' if soma % 2 == 0 else '\033[1mDEU IMPAR\033[m')
    print(f'{linha}' * 30)
    if soma % 2 == 0:
        # Se ganhou PAR
        if opção in 'Pp':
            cont += 1
            print('\033[1;32mVOCÊ GANHOU!\033[m Vamos jogar novamente...')
            print('\033[1m-=\033[m' * 20)
        # Se perdeu PAR
        else:
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            print('\033[1m-=\033[m' * 20)
            print(f'\033[1mVocê teve {cont} vitórias.\033[m')
            break
    else:
        # Se perdeu IMPAR
        if opção in 'Pp':
            print(f'\033[1;31mVOCÊ PERDEU!\033[m')
            print('\033[1m-=\033[m' * 20)
            print(f'\033[1mVocê teve {cont} vitórias.\033[1m')
            break
        # Se ganhou IMPAR
        else:
            cont += 1
            print('\033[1;32mVOCÊ GANHOU!\033[m Vamos jogar novamente...')
            print('\033[1m-=\033[m' * 20)
