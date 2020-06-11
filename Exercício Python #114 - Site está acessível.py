import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Não foi possível acessar o site!')
else:
    print('O site foi acessado com sucesso')
