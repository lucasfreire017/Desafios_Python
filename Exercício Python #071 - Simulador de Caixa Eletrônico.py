print('=' * 30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('=' * 30)
num = int(input('Qual valor deseja sacar: '))
total = num
céd = 50
cont_céd = 0
while True:
    if total >= céd:
        total -= céd
        cont_céd += 1
    else:
        if cont_céd > 0:
            print(f'Total de \033[1m{cont_céd}\033[m cédulas de \033[1;32mR${céd}\033[m')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        cont_céd = 0
        if total == 0:
            break
print('=' * 30)
print('\033[1mObrigado por usar o Caixa Eletônico. Tenha um bom dia!\033[m')
