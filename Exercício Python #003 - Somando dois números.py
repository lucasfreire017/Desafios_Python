n = int(input('\033[1;32mDigite um número:\033[m'))
n2 = int(input('\033[1;33mDigite outro número:\033[m'))
print('\033[1;30m-\033[m'*20)
print('A soma entre \033[1;34m{}\033[m e \033[1;36m{}\033[m é igual a: \033[1;35m{}\033[m'.format(n, n2, n+n2))