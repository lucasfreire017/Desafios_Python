import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
s = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(s))
