pritermo = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
formula = pritermo + (10 - 1) * razão
for c in range(pritermo, formula + razão, razão):
    print('\033[1;32m{}\033[m'.format(c), end= '\033[36m -> \033[m')
print('\033[1;31mACABOU\033[m')
