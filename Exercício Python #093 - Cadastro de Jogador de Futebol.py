dados = dict()
gols = list()

dados['Nome'] = str(input('Nome do Jogador: '))
dados['Partidas'] = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
print()

# Adição de gols feitos em cada partida 
for c in range(0, dados['Partidas']):
    gols.append(int(input(f'Quantos gols na {c+1}° partida? ')))

# Adcionando a lista "gols" como valor da chave "Gols" do dicionário "dados"    
dados['Gols'] = gols

# Exibição dos dados
print('-=' * 30)
print(dados)

print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {dados["Nome"]} Jogou {dados["Partidas"]} Partidas')
for c in range(0, dados['Partidas']):
    print(f'  => Na {c+1}° partida, fez {dados["Gols"][c]} Gols')
