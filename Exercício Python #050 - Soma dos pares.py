s = 0
cont = 0
d = '\033[1;33m-\033[m\033[1;31m-\033[m'
for c in range(1, 7):
    v = int(input('Digite o {}º valor: '.format(c)))
    print('{}'.format(d * 10))
    if v % 2 == 0:
        s += v
        cont += 1
print('Você informou \033[4;36m{}\033[m números \033[32mPARES\033[m e a soma entre eles igual à: {}'.format(cont, s))
