from Desafio_115_b.lib.interface import *
from Desafio_115_b.lib.arquivos import *

arquivo = 'pessoas.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:

    escolha = menu('Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema')
    if escolha == 1:
        lerArquivo(arquivo)
    elif escolha == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Digite o nome: '))
        idade = int(input('Digite a idade: '))
        cadastrar(arquivo, nome, idade)
    elif escolha == 3:
        print('Opção 3')
        break
    else:
        print('\033[31mERRO! Digite apenas valores compátiveis com as opções acima.\033[m')
