from datetime import date

nasc = int(input('Qual é seu ano de nascimento? '))
atual = date.today().year
x = 18 - (atual - nasc)

if x >= 2:
    print('Ainda falta \033[1;33m{}\033[m anos para você se alistar ao serviço militar.'.format(x))

elif x == 1:
    print('Falta apenas \033[1;33m{}\033[m ano para você se alistar ao serviço militar. Fique esperto!'.format(x))

elif x == 0:
    print('Você deve se alistar \033[1;32mIMEDIATAMENTE\033[m!')

else:
    print('Já passou seu tempo de alistamento. '
          'Você deveria ter se alistado a \033[1;31m{}\033[m anos atras'.format(18 - x))
