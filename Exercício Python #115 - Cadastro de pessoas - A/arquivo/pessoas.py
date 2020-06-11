def leia():
    """
    Leitura de todas as pessoas cadastradas
    :return: listagem de todas pessoas cadastradas
    """
    pessoas = open('bd/pessoas.txt', 'r', encoding='utf-8')
    leitura = pessoas.read()
    pessoas.close()

    return leitura


def cadastro(nome, idade):
    """
    Cadastro de pessoas
    :param valor: nova pessoas a ser cadastrada
    :return: (Sem retorno)
    """

    arquivo = open('bd/pessoas.txt', 'r', encoding='utf-8') # Abre o arquivo (leitura)
    conteudo = arquivo.readlines()
    conteudo.append(f'\n{nome}\t\t\t\t{idade} Anos') # conteúdo a ser inserido


    arquivo = open('bd/pessoas.txt', 'w', encoding='utf-8') # Abre o arquivo (escrita)
    arquivo.writelines(conteudo)
    arquivo.close()


def validarNome(nome):
    "Verificação de números no nome"
    string = nome.replace(' ','')

    return string.isalpha()

