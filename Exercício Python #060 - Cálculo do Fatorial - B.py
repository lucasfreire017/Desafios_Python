n = int(input('Digite um número para ver seu fatorial:'))
f = 1
print('Calculando \033[1m{}\033[1;32m! =\033[m '.format(n),end='')
for c in range(n, 0, -1):
    print('\033[1m{}\033[m'.format(c), end=' ')
    print('\033[1;32mX\033[m 'if c > 1 else '\033[1;32m=\33[m ', end='')
    f *= c
print('\033[1m{}\033[m'.format(f))
