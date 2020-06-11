largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = altura*largura
tinta = area/2

print('Em uma parede com a a dimensão de {}X{}, sua área será de {}m².'.format(largura, altura, area))
print('Será necessário {}l de tinta para pintá-la.'.format(tinta))