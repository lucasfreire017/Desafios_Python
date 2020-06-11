from datetime import date

dados = dict()
pessoas = list()
ano = date.today().year

dados = {'Nome':str(input('Nome: ')),
          'Idade':int(input('Ano de Nascimento: ')),
          'Carteira': int(input('Carteira de Trabalho (0 não tem): '))}

# Se carteira for igual a zero
if dados['Carteira'] != 0:
    dados['CTPS'] = int(input('Ano de Contratação: '))
    dados['Salário'] = int(input('Salário: R$ '))
    
    # 35 anos de colaboração
    dados['Aposentadoria'] = (dados['CTPS'] + 35) - dados['Idade']

# Calculo da idade
dados['Idade'] = ano - dados['Idade']

# Apresentação dos Valores
print('-=' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor de: {v}')
