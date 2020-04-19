from pprint import pprint
from MyCar import MyCar
from MyEngine import MyEngine
from itertools import product


#tuareg = MyCar("VolksWagen", "Tuareg", 2014, MyEngine('дизель', 265), 2500, 1)
#lc200 = MyCar("Toyota", "LC200", 2019, MyEngine('дизель', 248), 3200, 1)
#rr_sport = MyCar("Range_Rover", "Sport", 2015, MyEngine('бензин', 550), 8500, 3)
#bmw_x6m = MyCar("BMW", "X6M", 2016, MyEngine('бензин', 720), 10000, 5)
#lex_rx450 = MyCar("Lexus", "RX450", 2018, MyEngine('бензин', 300), 2800, 4)
#amarok = MyCar("VolksWagen", "Amarok", 2018, MyEngine('дизель', 170), 1800, 7)

#cars = {
#    tuareg.key: tuareg,
#    lc200.key: lc200,
#    rr_sport.key: rr_sport,
#    bmw_x6m.key: bmw_x6m,
#    lex_rx450.key: lex_rx450,
#    amarok.key: amarok
#}

cars1={}
for line in open('test_data.txt'):
    b, m, y, e_t, e_p, c, v = [i for i in line.split()]
    c=MyCar(b, m, y, MyEngine(e_t, e_p), c, v)
    cars1[c.key]=c

queries = [
    'марка VolksWagen',
    'гв 2018',
    'старше 2015',
    'младше 2017',
    'мощность 255',
    'цена 3000',
    'модель X6M',
    'бренд Toyta',
    'дизель 180',
    'двигатель бензин',
    'двигатель биодизель',
    ]
print(cars1)

#while 1:
#    q = input('Введите запрос для поиска: ')
#    if q=='exit':
#        break
#    elif len(q)>0:
#        for i in cars.keys():
#            #if cars[i].search_on_param(q) or cars[i].fuzzy_search_on_param(q):
#            if cars[i].fuzzy_search_on_param(q):
#                pprint(i)
    
#    input('...')

for query, cars1 in product(queries, cars1.values()):
    if cars1 == query:
        pprint((query, cars1))
    else:
        pprint((query, cars1.key, 'false'))
