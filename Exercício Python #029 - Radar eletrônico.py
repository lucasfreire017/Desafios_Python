speed = float(input('Digite a velocidade do carro:'))

multa = (speed - 80) * 7.00

if speed > 80:
  print('\nMULTADO! Você excedeu a velocidade limite que é de 80Km/h')
  print(f'Sua multa custará R${multa}')
else:
  print('\nDirija com segurança! Tenha um bom dia.')