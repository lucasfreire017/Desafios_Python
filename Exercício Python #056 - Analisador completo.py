cores = '\033[1;36m-\033[m\033[1;31m-\033[m'
sexo = 'M' and 'F'
totidade = 0
totsexo = 0
maior_idade = 0
for c in range(1, 5):
    print('{} {}ºPESSOA {}'.format(cores * 5, c, cores * 5))
    nome = input('Nome: ')
    sexo = str(input('[M/F]: ').upper())
    idade = int(input('Idade: '))
    totidade += idade
    if c == 1 and sexo == 'M':
        v = nome
        maior_idade = idade
    if sexo == 'M' and idade > maior_idade:
        v = nome
        maior_idade = idade
    if sexo == 'F' and idade < 20:
        totsexo += 1
print('{}'.format(cores * 15))
print('\n\033[1mO nome do homem mais velho é\033[1;35m{}\033[m \033[1me ele têm \033[1;35m{} \033[1manos.\033[m'.format(v, maior_idade))
print('\033[1mA média de idade do grupo é de:\033[m \033[1;35m{} anos\033[m'.format(totidade / 4))
if totsexo == 1:
    print('\033[1;35m{}\033[m \033[1mmulher têm menos de 20 anos de idade\033[m'.format(totsexo))
else:
    print('\033[1;35m{}\033[m \033[1mmulheres têm menos de 20 anos de idade.\033[m'.format(totsexo))
