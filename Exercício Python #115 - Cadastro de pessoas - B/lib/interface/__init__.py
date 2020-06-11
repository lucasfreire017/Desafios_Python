def leiaInt(msg):
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


def linha():
    print('\033[1m-\033[m'*42)

def titulo(msg):
    linha()
    print(msg.center(42))
    linha()

def menu(*opcoes):
    titulo('MENU')
    n = 0
    for item in opcoes:
        n+=1
        print(f'{n} ➡ {item}')
    linha()
    num = leiaInt('Digite sua opção: ')

    return num





