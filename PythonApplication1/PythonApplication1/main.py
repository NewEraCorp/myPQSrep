from pprint import pprint
from MyCar import MyCar
from task5.search_in_list import l_search_on_val

vw_tuareg = MyCar("VW", "Tuareg", 2014, 265, 2500, 1)
lc200 = MyCar("Toyota", "LC200", 2019, 248, 3200, 1)
rr_sport = MyCar("Range Rover", "Sport", 2015, 550, 8500, 3)
bmw_x6m = MyCar("BMW", "X6M", 2016, 720, 10000, 5)
lex_rx450 = MyCar("Lexus", "RX450", 2018, 300, 2800, 4)
vw_am = MyCar("VW", "Amarok", 2018, 170, 1800, 7)

cars = {
    vw_tuareg.key: vw_tuareg,
    lc200.key: lc200,
    rr_sport.key: rr_sport,
    bmw_x6m.key: bmw_x6m,
    lex_rx450.key: lex_rx450,
    vw_am.key: vw_am
}

#pprint(lc200.hp)

while 1:
    q = input('Введите запрос для поиска: ')
    for i in cars.keys():
        if cars[i].search_on_param(q):
            pprint(i)
    input('...')


