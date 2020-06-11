preço = total = mais = preço_barato = cont = 0
nome_produto = next = nome_barato = str
while True:
    nome_produto = input('Nome do Produto: ')
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if cont == 1 or preço < preço_barato:
        nome_barato = nome_produto
        preço_barato = preço
    if preço >= 1000:
        mais += 1
    next = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if next in 'Nn':
        print('\033[1mFIM DO PROGRAMA\033[m\n')
        break

print(f'O total gasto foi de \033[1mR${total:.2f}\033[m')
print(f'Temos \033[1m{mais}\033[m produtos que custam mais de R$1000.')
print(f'O produto mais barato foi \033[1m{nome_barato}\033[m que custou \033[1mR${preço_barato}\033[m.')
