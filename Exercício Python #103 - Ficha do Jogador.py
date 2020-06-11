def ficha(nome, gols):
    print(f"O jogador {nome} fez {gols} gol(s)")

try:
    nome = input('Nome do Jogador: ')
    gols = int(input('Número de gols: '))


except ValueError:
    gols = 0

if nome == "":
    nome = "<desconhecido>"

ficha(nome, gols)

