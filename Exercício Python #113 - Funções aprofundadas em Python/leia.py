def leiaInt(msg):
    """
    Função para a leitura de valores tipo inteiro
    :param msg: enuciado
    :return: valor convertido para int
    """

    while True:
        try:
            # Conversão do valor para int
            number = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro! Digite um valor inteiro!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usúario preferiu não digitar o valor\033[m')
            number = 0
            break
        else:
            return number
            break


def leiaFloat(msg):
    """
    Função para a leitura de valores tipo float
    :param msg: enuciado
    :return: valor convertido para float
    """

    while True:
        # Conversão do valor para float
        try:
            number = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro! Digite um valor real!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usúario preferiu não digitar o valor\033[m')
            number = 0
            break
        else:
            return number
        break
