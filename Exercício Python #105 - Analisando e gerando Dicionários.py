def notas(*n, sit=False):

    """
    --> Função que analiza as notas dos alunos e traz alguns dados da mesma
    :param n: uma ou mais notas que serão verificadas
    :param sit: (opcional) exibir a situação da turma
    :return: um dicionário com algumas informações sobre as notas
    """

    grades = dict()

    grades['Total'] = len(n)
    grades['Maior'] = max(n)
    grades['Menor'] = min(n)
    grades['Media'] = sum(n) / len(n)


    if sit == True:
        if grades['Media'] >= 7:
            grades['Sitacao'] = "Boa"

        elif grades['Media'] >= 5:
            grades['Situacao'] = "Razoável"

        else:
            grades['Situacao'] = 'Ruim'

    return grades


# Programa Principal

n = notas(4.5, 6, 7.5, 10, sit=True)
print(n)
help(notas)