salario = float(input('Qual é o salário do funcionário?'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Quem ganhava {} passa a receber {}'.format(salario, novo))
else:
    novo = salario + (salario * 10 / 100)
    print('Quem ganhava {} passa a receber {}'.format(salario, novo))
