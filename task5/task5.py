from search_in_list import l_search_on_val
from search_in_list import l_search_cost_in_range
from search_in_list import l_search_brand
from search_in_list import l_search_Max_on_param

from search_in_dict import d_search_on_val 
from search_in_dict import d_search_in_range
from search_in_dict import d_search_brand
from search_in_dict import d_search_Max_on_param
from search_in_dict import df_search_brand

l_Cars = [('VW Tuareg', 2014, "hp", 265, "cost", 2500),
        ("LC 200", 2019, "hp", 248, "cost", 3200),
        ("RR Sport", 2015, "hp", 550, "cost", 8500),
        ("BMW X6M", 2016, "hp", 720, "cost", 10000),
        ("Lexus RX450", 2018, "hp", 300, "cost", 2800),
        ("VW Amarok", 2018, "hp", 170, "cost", 1800)]

d_Cars = {'VW Tuareg':{'ГВ': 2014, 'hp': 265, "cost": 2500},
        "LC 200": {'ГВ':2019, "hp": 248, "cost": 3200},
        "RR Sport":{'ГВ': 2015, "hp": 550, "cost": 8500},
        "BMW X6M":{'ГВ': 2016, "hp": 720, "cost": 10000},
        "Lexus RX450":{'ГВ': 2018, "hp": 300, "cost": 2800},
        "VW Amarok":{'ГВ': 2018, "hp": 170, "cost": 1800}}

#запросы к списку
print('запросы к списку')
print(l_search_on_val(input('Введите значение:'),l_Cars))
print(l_search_cost_in_range(
    input('Введите мин: '), input('Введите макс: '), l_Cars))
print(l_search_brand(input('Введите марку:'),l_Cars))
print(l_search_Max_on_param(
    int(input('Введите номер параметра:')), l_Cars))
#запросы к словарю
print('запросы к словарю')
print(d_search_on_val(input('Введите параметр поиска:'),
                     input('Введите значение параметра:'), d_Cars))
print(d_search_in_range(input('Введите параметр поиска:'),
                     input('Введите Min значение параметра:'),
                     input('Введите Max значение параметра:'), d_Cars))
print(d_search_brand(input('Введите марку авто:'), d_Cars))
print(d_search_Max_on_param(input('Введите параметр:'), d_Cars))






