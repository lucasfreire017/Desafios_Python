dados = list()
pessoas = dict()
mulheres = list()
up_media = list()
x = 0
soma = 0

while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo: [M/F] ')).upper()           
    pessoas['Idade'] = int(input('Idade: '))
    dados.append(pessoas.copy())

    # -=-=-=-= Análise de dados -=-=-=-=
    soma += pessoas['Idade']

    if pessoas['Sexo'] == 'F':
        mulheres.append(pessoas['Nome'])
    
    resp = str(input('Deseja continuar [S/N]: '))[0].upper()
    print()
    
    if resp not in 'Ss':
        break

# Quantas pessoas foram cadastradas
print(f' - Foram cadastradas {len(dados)} pessoas')

# A média de idade do grupo
media = soma / len(dados)
print(f' - A média de idade é de {media} anos')

# Uma lista com todas as mulheres
print(f' - As mulheres cadastradas foram: ', end='')

if not mulheres:
    print('\033[31mNão há mulheres cadastradas!\033[m')
else:
    for c in range(0, len(mulheres)):
        print(f'{mulheres[c]}', end='')

# Lista de todas as pessoas com idade acima da média
print(' - Lista de pessoas com idade acima da média:')
for c in dados:
    if c['Idade'] >= (media):
        for k, v in c.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<< ENCERRADO >>')
