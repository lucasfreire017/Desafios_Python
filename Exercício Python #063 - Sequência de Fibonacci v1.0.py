print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos deseja ver: '))
t1 = 0
t2 = 1
t3 = 0
cont = 1
while cont <= n:
    print('{} ->'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    cont += 1
print('FIM')