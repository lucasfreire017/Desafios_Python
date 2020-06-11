from math import factorial
n = int(input('Digite um número para ver seu fatorial: '))
c = n
f = 1
print('Calculando \033[1m{}\033[1;32m! =\033[m '.format(n), end='')
while c > 0:
    print('\033[1m{}\033[m '.format(c), end='')
    print('\033[32mX\033[m ' if c > 1 else '\033[32m=\033[m ', end='')
    f *= c
    c -= 1
print('\033[1;35m{}\033[m'.format(f))
