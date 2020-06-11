from time import sleep
pritermo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = pritermo
cont = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont < total:
        print('\033[1;32m{}\033[m'.format(termo), end=' \033[1;34m->\033[m ')
        termo += razão
        cont += 1
    print('\033[1;31mPAUSA\033[m')
    mais = int(input('Quantos termos você quer ver: '))
print('\033[1m>>> FINALIZANDO\033[m')
sleep(2)
print('\033[1mNo total foram \033[1;35m{}\033[m \033[1mtermos mostrados.'.format(total))
