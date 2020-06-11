Times = ('Flamengo', 'Atlético', 'São Paulo', 'Internacional',
        'Grêmio', 'Sem Mundial', 'Sport Recife', 'Cruzeiro',
        'Botafogo', 'Corinthians', 'Vasco da Gama', 'Fluminense',
        'América MG', 'Chapecoense', 'Santos', 'EC Vitória',
        'Bahia', 'Paraná', 'Atlético-PR', 'Ceará SC')

print('='*16)
print(f'Lista de times do Brasileirão: {Times}')
print('='*16)
print(f'Os primeiros 5 colocados são: {Times[0:5]}')
print('='*16)
print(f'Os últimos 4 colocados são: {Times[-4:]}')
print('='*16)
print(f'Os times em ordem alfabética: {sorted(Times)}')
print('='*16)
print(f'O Chapecoense está em {Times.index("Chapecoense")+1}ª posição')
