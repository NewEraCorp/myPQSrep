#задание 3.1
Cars = [('VW Tuareg', 2014, "hp", 265, "cost", 2500),
        ("LC 200", 2019, "hp", 248, "cost", 3200),
        ("RR Sport", 2015, "hp", 550, "cost", 8500),
        ("BMW X6M", 2016, "hp", 720, "cost", 10000),
        ("Lexus RX450", 2018, "hp", 300, "cost", 2800),
        ("VW Amarok", 2018, "hp", 170, "cost", 1800)]
        
#поиск определнного значения
x1="LC 200"        
for i in Cars:
    if x1 in i:
        print('1:', i)
        
#поиск в диапазоне по цене        
Xmin=2800
Xmax=5000
for row in Cars:
    if str(Xmin)<=str(row[5])<=str(Xmax):
        print('2:', row)
        
#вывести машины одной фирмы 
x2="VW"
for i in Cars:
    if str(i).find(x2)!=-1:
        print('3:', i)

#вывести самую молодую машину
M = max(i[1] for i in Cars)
for i in Cars:
    if i[1]==M:
        print('4:', i)
