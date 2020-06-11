dados = dict()
gols = list()
jogadores = list()
Id = int()
soma = int()

while True:
    print('-'*40)
    Id += 1
    dados['Id'] = Id
    print(dados['Id'])
    dados['Nome'] = str(input('Nome do Jogador: '))
    dados['Partidas'] = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    
    # Adição de gols feitos em cada partida
    for c in range(0, dados['Partidas']):
        x = int(input(f'Quantos gols na {c+1}° partida? '))
        gols.append(x)
        soma += x
        
    dados['Gols'] = gols
    dados['Total'] = soma

    jogadores.append(dados.copy())

    # Parar repetição
    resp = str(input('Deseja continuar [S/N]: '))[0].upper()
    if resp not in 'Ss':
        break
        
print('-'*40)
# Tabela dos Jogadores
print('Cod Nome        Gols      Total')
for c in range(0, len(jogadores)):
    print(jogadores[c], end=' ')
print('-'*40)

# [{'Id': 1, 'Nome': 'Lucas', 'Partidas': 4, 'Gols': [2, 1, 1, 0], 'Total': 4}

# Mostrar Levantamento
escolha = int(input('Mostrar dados de qual jogador? '))
for c in range(0, len(jogadores)):
    if escolha == jogadores[c]['Id']:
       for d in range(0, 1):
           print(jogadores[c])
    else:
        print('Erro')
