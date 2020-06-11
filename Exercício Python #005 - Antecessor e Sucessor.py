v = int(input('Digite um valor: '))
print('Analisando o valor {}, é possivel ver que:'.format(v))
print('\033[36mAntecessor:\033[m {}{}'.format('\033[30m',v - 1))
print('\033[33mSucessor:\033[m {}{}'.format('\033[30m', v + 1))

