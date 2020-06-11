pritermo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = pritermo
cont = 0
while cont < 10:
    print('\033[1;32m{}\033[m'.format(termo), end=' \033[1;34m->\033[m ')
    termo += razão
    cont += 1
print('\033[1;31mFIM\033[m')
