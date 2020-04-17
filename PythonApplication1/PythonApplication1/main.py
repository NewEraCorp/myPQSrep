from pprint import pprint
from MyCar import MyCar
from itertools import product


tuareg = MyCar("VolksWagen", "Tuareg", 2014, 265, 2500, 1)
lc200 = MyCar("Toyota", "LC200", 2019, 248, 3200, 1)
rr_sport = MyCar("Range_Rover", "Sport", 2015, 550, 8500, 3)
bmw_x6m = MyCar("BMW", "X6M", 2016, 720, 10000, 5)
lex_rx450 = MyCar("Lexus", "RX450", 2018, 300, 2800, 4)
amarok = MyCar("VolksWagen", "Amarok", 2018, 170, 1800, 7)

cars = {
    tuareg.key: tuareg,
    lc200.key: lc200,
    rr_sport.key: rr_sport,
    bmw_x6m.key: bmw_x6m,
    lex_rx450.key: lex_rx450,
    amarok.key: amarok
}

queries = [
    'марка VolksWagen',
    'гв 2018',
    'старше 2015',
    'младше 2017',
    'мощность 255',
    'цена 3000',
    'модель X6M',
    'бренд Tiyta',
    ]
#pprint(lc200.hp)

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

for query, cars in product(queries, cars.values()):
    if cars == query:
        pprint((query, cars))
