def readInt(msg):
    """
    Função para a leitura de valores tipo int
    :param msg: valor a ser processado
    :return: valor convertido para int
    """
    try:
        number = int(input(msg))
    except (ValueError, TypeError, UnboundLocalError):
        print('\033[31mERRO! O valor digitado é inválido, digite um valor inteiro\033[m')
    except (KeyboardInterrupt):
        print('\033[31mO usúario preferiu não digitar o valor\033[m')
        number = 0
    else:
        return number

def line():
    print('\033[1m-\033[m'*42)


def title(msg):
    print('\033[1m-\033[m'*42)
    print(f'{msg:^42}')
    print('\033[1m-\033[m' * 42)


def menu(*option):
    title('MENU')
    count = 1
    for item in option:
        print(f'\033[94m{count}° - \033[m\033[93m{item}\033[m')
        count += 1

    answer = readInt('\nDigite sua opção: ')


    return answer



