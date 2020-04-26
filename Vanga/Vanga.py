from pprint import pprint
import random
from str_functions import compare
from VQuest import VQuest

STOP_WORDS = ['stop', 'exit', 'хватит', 'пока']

def ans_gen(q):
    ans = bool(random.getrandbits(1))
    if ans:
        return VQuest(q,'Да')
    else:
        return VQuest(q,'Нет')

vquests = {}

q=input('Задавай вопрос: ')
if q in STOP_WORDS: 
    quit()

vquest=ans_gen(q)
vquests[vquest.key]=vquest
pprint(vquest)

while q not in STOP_WORDS:
    q = input('Задавай вопрос: ')
    if q!='':
        if len(vquests)!=0: 
            for i in vquests.keys():
                if (len(vquests)!=0) & (compare(q,i)>0.8):
                    print('Помню', vquests[i])
                    break
            else:
                vquest=ans_gen(q)
                vquests[vquest.key]=vquest
                pprint(vquest)



    

            