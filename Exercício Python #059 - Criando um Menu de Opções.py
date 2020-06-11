from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
cores = '\033[1;37m-\033[m\033[1m-\033[m'
escolha = int(0)

while escolha != 5:
    print('{}'.format(cores * 10))
    print(''' [\033[1;31m1\033[m] \033[1;31mSomar\033[m
 [\033[1;32m2\033[m] \033[1;32mMultiplicar\33[m
 [\033[1;33m3\033[m] \033[1;33mMaior\33[m
 [\033[1;34m4\033[m] \033[1;34mNovos Números\33[m
 [\033[1;35m5\033[m] \033[1;35mSair\033[m'''.format(cores * 10, cores * 10))

    escolha = int(input('>>> Digite sua opção:  '))
    if escolha == 1:
        print('\033[1;35m{}\033[1m + \033[1;35m{}\033[1m = \033[1;36m{}\033[m'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('\033[1;35m{} \033[1mX \033[1;35m{}\033[1m = \033[1;36m{}\033[m'.format(n1, n2, n1 * n2))
    elif escolha == 2:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        if n1 == n2:
            maior = str('\033[1;31m"Os valores são iguais!"\033[m')
        print('\033[1mEntre \033[1;35m{}\033[m \033[1me \033[1;35m{}\033[m\033[1m o maior valor é:\033[m \033[1;36m{}\033[m'.format(n1, n2, maior))
    if escolha == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segudo número: '))
        print('\033[1mAGUARDE\033[m')
        sleep(2)
        print('\033[1;32mNovos números adcionados com sucesso!\033[m')
    if escolha > 5:
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
    sleep(2)
print('\033[1m>>> FINALIZANDO\033[m')
sleep(2)
print('{}'.format(cores * 10))
print('\033[1mObrigado por usar o programa.\nVolte sempre!')
