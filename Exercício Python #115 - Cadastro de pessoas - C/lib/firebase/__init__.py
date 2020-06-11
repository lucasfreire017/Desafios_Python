import pyrebase
import urllib
import urllib.request
from lib.interface import *
from time import sleep


def online():
    try:
        urllib.request.urlopen('http://www.firebase.com')
        return True
    except urllib.error.URLError:
        return False


# Configurações do Banco de Dados
config = {
    "apiKey": "AIzaSyAPLbBAE4brJ1ypWcDDjeKZMrMvc0F5wCs",
    "authDomain": "python-9cfc2.firebaseapp.com",
    "databaseURL": "https://python-9cfc2.firebaseio.com",
    "projectId": "python-9cfc2",
    "storageBucket": "python-9cfc2.appspot.com",
    "messagingSenderId": "867241550247",
    "appId": "1:867241550247:web:3fb01c73950344c0381682",
    "measurementId": "G-1MBW88N0M0"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def saved():
    title('PESSSOAS CADASTRADAS')
    try:
        data = db.child('Data').get()
        lista = data.val()
        del(lista[0])
        cor = 0
        for item in lista:
            cor += 1
            if cor % 2 == 0:
                print(f'\033[107m{item["Nome"]:<30}{item["Idade"]:>3} Anos\033[m')
            else:
                print(f'{item["Nome"]:<30}{item["Idade"]:>3} Anos')

    except:
        print('Não existem dados no banco de dados')




def register(name='unknown', age=0):
    data = db.child('Data').get()
    try:
        total = len(data.each())
    except:
        total = 1
    db.child('Data').child(total).set({'Nome': name, 'Idade': age})
    print('Salvando...')
    sleep(1.5)
    print('\033[92mDados salvos com sucesso!\033[m')
    sleep(1)


