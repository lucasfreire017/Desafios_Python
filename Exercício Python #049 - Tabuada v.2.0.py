num = int(input('Digite um número: '))
for c in range(1, 11):
    print('\033[34m{}\033[m X \033[36m{}\033[m = {}'.format(num, c, num * c))