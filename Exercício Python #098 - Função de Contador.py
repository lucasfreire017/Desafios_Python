def contador():

    print('-=' * 20)
    print('Contagem de 1 até 10, de 1 em 1')
    for c in range(1, 11):
        print(c, end=' ')
    print('FIM!')

    print('-=' * 20)
    print('Contagem de 10 até 1, de 2 em 2')
    for c in range(10, 0, -2):
        print(c, end=' ')
    print('FIM!')

    print('-=' * 30)
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))

    print('-=' * 20)
    print(f'Contagem de {i} até {f}, de {p} em {p}')
    for c in range(i, f+1, p):
        print(c, end=' ')
    print('FIM!')


contador()