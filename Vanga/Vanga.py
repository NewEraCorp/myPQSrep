from pprint import pprint
import random

while 1:
    if(input('Задавай вопрос: ')!=''):
        ans = bool(random.getrandbits(1))
        if ans:
            pprint('Ответ: Да')
        else:
            pprint('Ответ: Нет')