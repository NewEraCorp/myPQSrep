from pprint import pprint
import random
from str_functions import compare
from VQuest import VQuest

def ans_gen(q):
    ans = bool(random.getrandbits(1))
    if ans:
        return VQuest(q,'Да')
    else:
        return VQuest(q,'Нет')

vquests = {}

vquest=ans_gen(input('Задавай вопрос: '))
vquests[vquest.key]=vquest
pprint(vquest)

while 1:
    q = input('Задавай вопрос: ')
    if q!='':
        if len(vquests)!=0: 
            for i in vquests.keys():
                if (len(vquests)!=0) & (compare(q,i)>0.8):
                    pprint(vquests[i])
                    break
            else:
                vquest=ans_gen(q)
                vquests[vquest.key]=vquest
                pprint(vquest)



    

            