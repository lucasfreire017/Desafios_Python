# Quantas pessoas cadastradas / mais pesadas / mais leves
from typing import List, Union

dados = list()
pessoas = list()

pesadas = float(0)
leves = float(0)

nome_p = list()
nome_l = list()

while True:

    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        pesadas = dados[1]
        leves = dados[1]
    else:
        if dados[1] > pesadas:
            pesadas = dados[1]

        if dados[1] < leves:
            leves = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resp = input('Deseja continuar? [Sim/Não]: ').upper()[0]
    if resp in 'Nn':
        break




print('=-'*25)
print(f'Foram contabilizadas {len(pessoas)} pessoas cadastradas.')

print(f'O maior peso foi de {pesadas}Kg e pertecente a: ', end='')
for p in pessoas:
    if p[1] == pesadas:
        print(f'[{p[0]}] ', end='')
print()

print(f'O menor peso foi de {leves}Kg e pertecente a: ', end='')
for c in pessoas:
    if c[1] == leves:
        print(f'[{c[0]}] ', end='')
print()
