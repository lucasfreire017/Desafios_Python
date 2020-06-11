def escreva(txt):
    print('\033[1m-' * (len(txt)+4))
    print(f'  {txt}')
    print('-' * (len(txt)+4))
    '\033[m'


#escreva('Lucas')
#escreva('Etec Raposo Tavares')
#escreva('Uva')