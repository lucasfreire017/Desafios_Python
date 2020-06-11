viagem = float(input('Qual é a distância da viagem em Km?'))
preço = viagem * 0.50 if viagem <=200 else viagem * 0.45
print('O preço será de R${}'.format(preço))
