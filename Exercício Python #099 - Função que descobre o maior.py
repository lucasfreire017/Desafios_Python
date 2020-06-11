from random import randint
from time import sleep

def maior(valores):
    maior = 0

    for c in valores:
        if c > maior:
            maior = c

    print('-='*20)
    print(f'Analisando os valores passados...')
    for c in valores:
        print(f'{c}', end=' ')
        sleep(0.5)
    print(f'Foram informados ao todo {len(valores)} valores')
    print(f'O maior valor informado foi {maior}')


# Programa Principal
numeros = list()

for c in range(0, 5):

    for c in range(0, randint(1, 10)):
        numeros.append(randint(1, 10))

    sleep(1)
    maior(numeros)
    numeros.clear()





