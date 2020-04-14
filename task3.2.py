#задание 3.2 и 3.3
Cars = {'VW Tuareg':{'ГВ': 2014, 'hp': 265, "cost": 2500},
        "LC 200": {'ГВ':2019, "hp": 248, "cost": 3200},
        "RR Sport":{'ГВ': 2015, "hp": 550, "cost": 8500},
        "BMW X6M":{'ГВ': 2016, "hp": 720, "cost": 10000},
        "Lexus RX450":{'ГВ': 2018, "hp": 300, "cost": 2800},
        "VW Amarok":{'ГВ': 2018, "hp": 170, "cost": 1800}}
       
#поиск определнного значения
x1=input('1. Введите параметр поиска:')
x2=input('1. Введите значение:')
#print(x1, type(x1))
for i in Cars.keys():
    if str(Cars[i][x1])==x2:           
        print('1:', i, ':', Cars[i])
        
#поиск в диапазоне       
x1=input('2. Введите параметр поиска:')
xmin=input('2. Введите MIN значение:')
xmax=input('2. Введите MAX значение:')
for i in Cars.keys():
    if xmin<=str(Cars[i][x1])<=xmax:
        print('2:', i, ':', Cars[i])
        
#вывести машины одной фирмы 
x=input('3. Введите фразу для поиска:')
for i in Cars.keys():
    if str(i).find(x)!=-1:
        print('3:', i)
#поиск максимума по параметру
x1=input('4. Введите параметр поиска:')
M = max(Cars[i][x1] for i in Cars.keys())
for i in Cars.keys():
    for j in Cars[i].keys():
        if Cars[i][j]==M:
            print('4:', i, Cars[i])
