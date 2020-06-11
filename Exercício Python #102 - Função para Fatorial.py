def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: Número a ser calculado
    :param show: (opcioal) Mostrar ou não o calculo
    :return: O valor fatorial do número n
    """
    c = n
    f = 1
    print(f'Calculando \033[1m{n}\033[1;32m! =\033[m ', end='')
    while c > 0:
        if show == True:
            print(f'\033[1m{c}\033[m ', end='')
            print('\033[32mX\033[m ' if c > 1 else '\033[32m=\033[m ', end='')
        f *= c
        c -= 1

    return f'\033[1;35m{f}\033[m'

print(fatorial(5, show=True))
help(fatorial)