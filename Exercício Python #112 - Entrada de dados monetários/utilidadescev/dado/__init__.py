def leiaDinheiro(msg):
    """
    Função para validação de valores numéricos
    :param msg: valor a ser processado
    :return: valor convertido
    """
    validador = False
    valor = 0

    while True:
        teste = str(input(msg))
        if teste.isnumeric() == True:
            valor = int(teste)
            validador = True
        else:
            print(f'\033[31m"{teste}" não é um valor monetário válido!\033[m')
        if validador == True:
            break

    return valor
