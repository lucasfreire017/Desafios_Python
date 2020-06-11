from Desafio_115_b.lib.interface import *
from time import sleep

def arquivoExiste(arq):
    try:
        arquivo = open(f'{arq}', 'rt')
        arquivo.close()

    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        arquivo = open(f'{arq}', 'wt+', encoding='utf-8')
        arquivo.close()
    except:
        print('\033[31mNão foi possível criar o arquivo!\033[m')
    else:
        print(f'\033[32mArquivo {arq} criado com sucesso!\033[m')


def lerArquivo(arq):
    titulo('PESSOAS CADASTRADAS')
    try:
        arquivo = open(f'{arq}', 'rt', encoding='utf-8')
    except:
        print('\033[31mNão foi possível abrir o arquivo para leitura\033[m')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos')
    finally:
        arquivo.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        arquivo = open(f'{arq}', 'at', encoding='utf-8')
    except:
        print('\033[31mHouve um erro ao tentar abrir o arquivo\033[m')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um erro ao tentar escrever no arquivo\033[m')
        else:
            print('\033[32mNovo regristro adicionado com sucesso\033[m')
    finally:
        arquivo.close()





