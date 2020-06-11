print('-='*10)
print('Empréstimo Bancário')
print('-='*10)

casa = float(input('Valor da casa: R$'))
salário = float(input('Qual o salário do comprador: R$'))
anos = int(input('Em quantos anos o comprador pretende pagar a casa? '))
meses = anos * 12
vmensal = casa / anos
sal = (salário * 30 / 100)
if vmensal > sal:
    print('-='*50)
    print("""\033[1;31mEMPRÉSTIMO NEGADO\033[m
A prestação mensal que é de \033[32mR${:.2f}\033[m é maior que \033[33m30%\033[m do salário do comprador.""".format(vmensal))
else:
    print('-='*50)
    print("""\033[1;32mEMPRÉSTIMO SUCEDIDO\033[m
Comprando uma casa no valor de \033[32mR${}\033[m dividido em uma prestação mensal de \033[1;4m{} anos\033[m ({} meses).
O valor mensal ficará: \033[32mR${:.2f}.\033[m""".format(casa, anos, meses, vmensal))
