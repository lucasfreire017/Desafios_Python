cidade = str(input('Digite o nome de uma cidade:'))
cid = cidade.split()
v = 'Santo' in cid[0]
if v == True:
    print('A cidade {} começa com a palavra SANTO'.format(cidade))
else:
    print('A cidade {} não começa com a palavra SANTO'.format(cidade))
