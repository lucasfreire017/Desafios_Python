idade = cont_h = cont_18 = cont_m = 0
sexo = parada = str
titulo = 'CADASTRE UMA PESSOA'
while True:
    print(f'{titulo:=^40}')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    
    while sexo not in 'FfMm':
        sexo = input('Sexo [M/F]: ').strip()[0]
    
    if idade >= 18:
        cont_18 += 1
    
    if sexo in 'Mm':
        cont_h += 1
    
    if sexo in 'Ff' and idade < 20:
        cont_m += 1
    parada = input('Quer continuar? [S/N] ').strip()[0]
    
    while parada not in 'SsNn':
        parada = input('Quer continuar? [S/N] ').strip()[0]
    
    if parada in 'Nn':
        print('\033[1mANÁLISE\033[m')
        break

print(f'{cont_18} pessoas têm mais de 18 anos.')
print(f'{cont_h} homens foram cadastrados.')
print(f'{cont_m} mulheres têm menos de 20 anos.')
