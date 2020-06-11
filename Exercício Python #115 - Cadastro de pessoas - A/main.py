from Desafio_115_a.arquivo import pessoas
from time import sleep

# Tratamento de erro caso o arquivo não exista
try:
    arquivo = open('bd/pessoas.txt', 'r', encoding='utf-8')

except FileNotFoundError:
    arquivo = open('bd/pessoas.txt', 'w', encoding='utf-8')
arquivo.close()


def titulo(msg, cor=36):
    "Exibição elegante dos menus"
    print('\033[1m-''\033[m' * 40)
    print(f'\033[{cor};1m{msg:^40}\033[m')
    print('\033[1m-''\033[m' * 40)


# Programa Principal
while True:
    # ----- Menu Principal -----1
    titulo('MENU PRINCIPAL')
    print('\033[32;1m1 -\033[m Ver pessoas cadastradas')
    print('\033[32;1m2 -\033[m Cadastrar nova pessoa')
    print('\033[32;1m3 -\033[m Sair do sistema\n')

    while True:
        try:
            opcao_select = int(input('Digite sua opção: '))
            if  opcao_select > 0 and opcao_select < 4:
                break
            else:
                print('\n\033[31mErro! Digite uma opção entre 1 e 3\033[m')

        except (ValueError, TypeError, KeyboardInterrupt, Exception):
            print('\n\033[31mErro! Valor inválido. Por favor, digite uma opção válida\033[m')

    # ----- Leitura de Pessoas -----
    if opcao_select == 1:
        # LIMPAR TELA
        titulo('LISTA DE PESSOAS', 32)
        print(f'{pessoas.leia()}\n')
        sleep(3)

    # ----- Cadastro de Pessoas -----
    if opcao_select == 2:
        # LIMPAR TELA
        titulo('CADASTRO DE PESSOAS', 31)

        while True:
            # Tratamento de erros (Nome)
            while True:
                try:
                    nome = str(input('Nome: ')).title().strip()
                    if pessoas.validarNome(nome) == False:
                        print('\033[31mDigite um nome válido\033[m')
                    else:
                        break
                except (KeyboardInterrupt):
                    print('\033[31mNome inválido')


            # Tratamento de erros (Idade)
            while True:
                try:
                    idade = int(input('Idade: '))
                    erro = False
                    if idade <= 0:
                        print('\033[31mDigite uma idade válida\033[m')
                        erro = True
                    elif idade >150:
                        print('\033[31mDigite uma idade válida\033[m')
                        erro = True
                except (ValueError, TypeError, KeyboardInterrupt):
                    print('\033[31mDigite uma idade válida\033[m')
                else:
                    if erro == False:
                        break
            break

        # ----- Animação -----
        print('\033[1m\nSALVANDO DADOS...\033[m')
        sleep(1.5)
        print('\033[32;1mDADOS SALVOS COM SUCESSO!\033[m')
        sleep(1)
        pessoas.cadastro(nome, idade)

    # ----- Saída do Programa -----
    if opcao_select == 3:
        print('\033[1mENCERRANDO...\033[m')
        sleep(3)
        print('\033[1m\n----- OBRIGADO POR USAR O PROGRAMA -----\033[m')
        print('\033[1m              VOLTE SEMPRE\033[m')
        sleep(1)
        break
