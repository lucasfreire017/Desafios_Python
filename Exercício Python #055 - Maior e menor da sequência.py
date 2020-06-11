maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ºpessoa: '.format(c)))
    print('\033[1m{}\033[m'.format('-=' * 17))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\n\033[1mO maior\033[m peso lido foi de: \033[1m{}Kg\033[m.'.format(maior))
print('\033[1mO menor\033[m peso lido foi de: \033[1m{}Kg\033[m.'.format(menor))
