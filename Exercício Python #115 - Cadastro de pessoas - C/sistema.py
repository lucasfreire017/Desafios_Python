from lib.interface import *
from lib.firebase import *
from time import sleep


if online():
    while True:
        try:
            choice = menu('Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema')

        except:
            print('\033[31mAlgum erro aconteceu, tente novamente\033[m')

        else:
            if choice not in [1,2,3]:
                print('\033[31mDigite apenas um número compátivel com as opções exibidas!\033[m')

            elif choice in [1]:
                saved()

            elif choice in [2]:
                title('NOVO CADASTRO')
                name = str(input('Nome: '))
                age = int(input('Idade: '))
                register(name, age)

            elif choice in [3]:
                print('\033[1mFINALIZANDO...\033[m')
                sleep(2)
                print('Obrigado por usar o sistema :3')
                sleep(1)
                break
else:
    print('\033[91mERRO! Falha com conexão a internet. ')




