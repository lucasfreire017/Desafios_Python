from Desafio_097 import escreva

def aumento(valor, p=10, form=False):
    """
    Função para aumento do valor em 10%
    :param valor: valor numérico a ser passado
    :param p: Porcentagem a ser calculada
    :param form: (Opcional) formatação do valor
    :return: valor aumentado em 10%
    """
    x = (valor * p) / 100
    # x --> 10% do valor
    res = valor + x

    return res if form == False else moeda(res)


def diminuir(valor, p=13, form=False):
    """
    Função para diminuir 13% do valor
    :param valor: valor numérico a ser passado
    :param p: Porcentagem a ser calculada
    :param form: (Opcional) formatação do valor
    :return: valor diminuido em 13%
    """
    x = (valor * p) / 100
    # x --> 13% do valor
    res = valor - x

    return res if form == False else moeda(res)

def dobro(valor, form=False):
    """
    Função para dobrar o valor
    :param valor: valor numérico a ser passado
    :param form: (Opcional) formatação do valor
    :return: retorna medate do valor passado
    """
    x = valor*2
    res = x

    return res if form == False else moeda(res)

def metade(valor, form=False):
    """
    Função para dividir o valor pela metade
    :param valor: valor numérico a ser passado
    :param form: (Opcional) formatação do valor
    :return: retorna a metade do valor passado
    """
    x = valor/2
    res = x

    return res if form == False else moeda(res  )

def moeda(valor):
    return f"R${valor:.2f}".replace(".", ",")


def resumo(valor, p1=10, p2=5):
    """
    Função pata a exibição resumida do valor
    :param valor: valor (float) a ser passado
    :param p1: porcentagem de aumento
    :param p2: porcentagem de redução
    :return:
    """
    escreva('     RESUMO DO VALOR     ')
    print(f'Preço Analisado:  \t{moeda(valor)}')
    print(f'Dobro do Preço:   \t{dobro(valor, True)}')
    print(f'Metade do Preço:  \t{metade(valor, True)}')
    print(f'{p1}% de Aumento: \t{aumento(valor, p1, True)}')
    print(f'{p2}% de Redução: \t{diminuir(valor, p2, True)}')
    print('\033[1m-'*29)