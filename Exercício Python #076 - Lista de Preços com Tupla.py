listagem = ('pão', 2.00,
            'sacola', 2.50,
            'Toddy', 7.90,
            'Nescau', 7.80,
            'Laranja', 3.50,
            'Picles', 4.20,
            'Peixe', 1.00,
            'Frango', 130.80)
print('-'*10, 'LISTAGEM DE PRODUTOS', '-'*10)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}R$ ', end='')

    elif c % 2 == 1:
        print(f'{listagem[c]:.2f}')
print('-'*40)
