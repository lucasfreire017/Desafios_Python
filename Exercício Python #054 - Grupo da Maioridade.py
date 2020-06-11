from datetime import date
ano = date.today().year
cont = 0
cont18 = 0
for c in range(1, 8):
    print('\033[1;36m ------ {}º PESSOA ------ \033[m'.format(c))
    idade = int(input('Ano de Nascimento: '))
    if ano - idade <21:
        cont += 1
    else:
        cont18 += 1
print('\n\033[1m{0}\033[m pessoas já são maiores de idade'.format(cont18))
print('\033[1m{0}\033[m pessoas ainda não atingiram a maioridade que, no caso é de \033[1m21 anos\033[m.'.format(cont))
