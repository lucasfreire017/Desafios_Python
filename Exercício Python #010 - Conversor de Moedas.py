USD = float(input('Quanto de dinheiro você tem? R$'))
BR = 3.27
print('Com R${:.2f} você pode comprar U${}'.format(USD, BR * USD))