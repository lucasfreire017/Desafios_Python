def leiaInt(msg):
    """
    Validar se o valor é inteiro ou não
    :param msg: Valor a ser verificado
    :return:
    """
    val = False
    valor = 0

    while True:
        n = str(input(msg))
        if n.isnumeric() == True:
            valor = int(n)
            val = True
        else:
            print(f'\033[31mValor incorreto, digite uma valor númerico!\033[m')
        if val == True:
            break

    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
