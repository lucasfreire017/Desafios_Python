r1 = float(input('Primeiro Seguimento:'))
r2 = float(input('Segundo Seguimento:'))
r3 = float(input('Terceiro Seguimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima \033[1;32mPODEM\033[m formar um triângulo.')
# Todos os lados iguais: EQUILÁTERO
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Os seguimentos correspondem a um \033[1;36mTRIÂNGULO EQUILÁTERO\033[m')
# Dois lados iguais: ISÓCELES
    elif r1 == r2 != r3 or r3 == r2 != r1 or r1 == r3 != r2:
        print('Os seguimentos correspondem a um \033[1;36mTRIÂNGULO ISÓCELES\033[m.')
# Todos os lados diferentes: ESCALENO
    elif r1 != r2 and r3 or r2 != r1 and r3 or r3 != r1 and r2:
        print('Os seguimentos correspondem a um \033[1;36mTRIÂNGULO ESCALENO\033[m.')

else:
    print('Os seguimentos acima \033[1;31mNÃO PODEM\033[m formar um triângulo.')