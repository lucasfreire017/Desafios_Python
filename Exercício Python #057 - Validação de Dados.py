sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('\033[1;31mValor incorreto. Tente novamente.\033[m\n'
             'Digite o sexo da pessoa [M/N]: ')).strip().upper()[0]
print('{}'.format('-' * 30))
print('Sexo \033[1m{}\033[m cadastrado com sucesso.'.format(sexo))
