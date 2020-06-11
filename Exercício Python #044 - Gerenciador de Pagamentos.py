print('{:=^40}'.format(' Lojas Freire '))
produto = float(input('Preço das compras: R$'))
print('''\033[1;36mFORMAS DE PAGAMENTO\033[m
[\033[34m1\033[m] À vista / com cheque: 10% de desconto
[\033[34m2\033[m] À vista no cartão: 5% de desconto
[\033[34m3\033[m] Em até 2x no cartão: Preço normal
[\033[34m4\033[m] 3x ou mais no cartão: 20% de juros
''')
opção = int(input('Qual sua forma de pagamento? ')) # Escolha da forma de pagamento

if  opção == 1:
    desconto = (produto * 10 / 100)
    print('Sua compra de \033[1;32mR${:.2f}\033[m vai custar \033[1;32mR${:.2f}\033[m no final'.format(produto ,produto - desconto))

elif opção == 2:
    desconto = (produto * 5 / 100)
    print('Sua compra de \033[1;32mR${:.2f}\033[m vai custar \033[1;32mR${}\033[m no final'.format(produto, produto - desconto))

elif opção == 3:
    print('Sua compra de \033[1;32mR${:.2f}\033[m, será parcelada em 2x de \033[1;32mR${:.2f}\033[m \033[1;36mSEM JUROS\033[m'.format(produto, produto / 2))
    print('Sua compra que custa \033[1;32mR${:.2f}\033[m vai custar \033[1;32mR${:.2f}\033[m no final.'.format(produto, produto))

elif opção == 4:
    parcela = int(input('Quantas vezes deseja parcelar? '))
    juros = (produto * 20 / 100) # 20% do produto
    preço = (produto + juros) / parcela # Preço final (com juros) dividido pelas parcelas
    print('{}'.format('-' * 20))
    print('Sua compra será parcelada em {}x de \033[1;32mR${:.2f}\033[m \033[1;31mCOM JUROS\033[m'.format(parcela, preço))
    print('Sua compra que custa \033[1;32mR${:.2f}\033[m vai custar \033[1;32mR${:.2f}\033[m no final'.format(produto, produto + juros))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA\033[m. Tente novamente')
