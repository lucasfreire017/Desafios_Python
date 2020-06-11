from time import sleep
import emoji
from datetime import date
input('Aperte <\033[31mENTER\033[m> para começar:')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':boom: Feliz \033[1;30m{}\033[m :boom:', use_aliases=True).format(date.today().year + 1))
