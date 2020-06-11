num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')

if cont == 2:
    print('\n\033[mO número \033[1m{}\033[m foi divisível \033[1m{}\033[m vezes.'.format(num, cont))
    print('\033[1;32mTEMOS UM NÚMERO PRIMO!\033[m')

else:
    print('\n\033[mO número \033[1m{}\033[m foi divisível \033[1m{}\033[m vezes.'.format(num, cont))
    print('\033[1;31mNÃO É UM NÚMERO PRIMO!\033[m')