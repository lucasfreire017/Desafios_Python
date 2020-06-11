# A soma de todos os valores pares digitdos
# A soma dos valores da 3° coluna
# O maior valor da segunda linha

matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = x = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para a posição [{l},{c}]: ')))

        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

        if matriz[l][2]:
            x += matriz[l][2]

        if matriz[1][c] > maior:
            maior = matriz[1][c]

print('-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print()
print(f'A soma de todos os valores pares digitdos: {par}')
print(f'A soma dos valores da 3° coluna: {x}')
print(f'O maior valor da segunda linha: {maior}')