def aumento(valor, porc=10, form=False):
    """
    Função para aumento do valor em 10%
    :param valor: valor numérico a ser passado
    :param porc: Porcentagem a ser calculada
    :param form: (Opcional) formatação do valor
    :return: valor aumentado em 10%
    """
    x = (valor * porc) / 100
    # x --> 10% do valor
    res = valor + x

    return res if form == False else moeda(res)


def diminuir(valor, porc=13, form=False):
    """
    Função para diminuir 13% do valor
    :param valor: valor numérico a ser passado
    :param porc: Porcentagem a ser calculada
    :param form: (Opcional) formatação do valor
    :return: valor diminuido em 13%
    """
    x = (valor * porc) / 100
    res = valor - x
    # x --> 13% do valor

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

    return res if form == False else moeda(res)

def moeda(valor):
    return f"R${valor:.2f}".replace(".", ",")


