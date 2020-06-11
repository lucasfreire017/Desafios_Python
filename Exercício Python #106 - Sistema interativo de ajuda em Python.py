def help_Function(msg):

    """
    Função para verificar o Interactive Help das demais funções ou bibliotecas
    :param msg: comando a ser passado
    :return: (none)
    """

    intro = f'Acessando o manual do comando {msg}'

    print('\033[1;30;43m~' * (len(intro) + 4))
    print(f'  {intro}')
    print('~' * (len(intro) + 4))
    print('\033[m')

    print('\033[1;30;47m')
    print(f'{help(msg)}')
    print('\033[m')


# Programa principal
val = str()
intro = 'SISTEMA DE AJUDA PyHELP'
fim = 'ATÉ LOGO'

while val != 'fim':
    print('\033[30;42m~' * (len(intro)+4))
    print(f'  {intro}')
    print('~' * (len(intro)+4))
    print('\033[m')

    val = input('Função ou Biblioteca > ').lower()
    if val != 'fim':
        help_Function(val)

print('\033[30;41m~' * (len(fim)+4))
print(f'  {fim}')
print('~' * (len(fim)+4))
print('\033[m')