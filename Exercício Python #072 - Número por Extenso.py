números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    x = int(input('Digite um número entre 0 e 20: '))

    while x<0 or x>20:
      x = int(input('\033[1;31mValor Incorreto\033[m Digite um número entre 0 e 20: '))

    if x>=0 and x<=20:
        print(f'Você digitou o número: \033[1m{números[x]}\033[m')

    print('-='*20)
    resp = str(input('Deseja Continuar [\033[1;33mS\033[m/\033[1;31mN\033[m]')).upper()[0]
    print('-='*20)

    if resp == 'N':
        break