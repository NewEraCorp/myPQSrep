from search_in_dict import df_search_brand

d_Cars = {'Volks Wagen Tuareg':{'ГВ': 2014, 'hp': 265, "cost": 2500},
        "Land Cruser 200": {'ГВ':2019, "hp": 248, "cost": 3200},
        "Range Rover Sport":{'ГВ': 2015, "hp": 550, "cost": 8500},
        "BMW X6M":{'ГВ': 2016, "hp": 720, "cost": 10000},
        "Lexus RX450":{'ГВ': 2018, "hp": 300, "cost": 2800},
        "Volks Wagen Amarok":{'ГВ': 2018, "hp": 170, "cost": 1800}}

print(df_search_brand(input('Введите фразу:'), d_Cars))
