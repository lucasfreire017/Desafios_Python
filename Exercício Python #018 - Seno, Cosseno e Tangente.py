from math import radians, sin, cos, tan
v = float(input('Digite um ângulo:'))
sen = sin(radians(v))
cos = cos(radians(v))
tan = tan(radians(v))
print('O SENO de {} é: {:.2f}'.format(v, sen))
print('O COSSENO de {} é: {:.2f}'.format(v, cos))
print('A TANGENTE de {} é: {:.2f}'.format(v, tan))
