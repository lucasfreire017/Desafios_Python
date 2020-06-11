n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O \033[1;33mPRIMEIRO\033[m valor foi maior!')
elif n2 > n1:
    print('O \033[1;34mSEGUNDO\033[m valor foi maior!')
else:
    print('Os dois valores são \033[1;36mIGUAIS\033[m!')