from random import randint
from time import sleep
numeros = [[0],[0],[0],[0],[0],[0]]

print('======== MEGA SENA ========')
question = int(input('Quantos jogos você quer? '))
print(f'======== SORTEANDO {question} JOGOS ========')
sleep(1)

for e in range(0, question):
        for c in range(0, 6):
                games = randint(1, 60)

                if games not in numeros:
                        numeros[c] = games   
        numeros.sort()   
         
        print(f'Jogo {e+1}: {numeros}', end='\n')
        #sleep(1)
print('======== BOA SORTE ========')
