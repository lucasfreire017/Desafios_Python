from random import randint
from time import sleep

numeros = list()

# Função que sorteia 5 números aleatórios
def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 5))
    return numeros


# Função para somar números pares
def somaPar(valores):
    soma = 0
    for c in valores:
        if c %2 == 0:
            soma += c
    return soma


#Programa Inicial
val = sorteia()

print(f'Sorteando 5 valores da lista: ',end='')
for c in val:
    print(f'{c}', end=' ')
    sleep(0.5)
print('FIM!')

print(f'Somando os valores pares de {val}, temos {somaPar(val)}')
