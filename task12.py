from pprint import pprint

class Car:
#Автомобиль: имеет атрибуты: марка (бренд), модель, год выпуска,
#пробег, цвет, тип двигателя, мощность двигателя, тип трансмиссии, стоимость, 
#расход топлива, тип колес
    def __init__(self, brand, model, age, engine, cost):
        self.brand, self.model, self.age, self.cost, = brand, model, age, cost
        if type(engine) == Engine:
            self.engine=engine
        elif type(engine) == list:
            pass
    
    def __repr__(self):
        return "Car('%s', '%s', %s, %s, %s)" %\
               (self.brand, self.model, self.age, self.engine, self.cost)

    def en_inst(self, engine):
        pass

    def check_systems():
        #проверка систем автомобиля при включении зажигания
        pass

    def alarm_activ():
        #активация сигнализации
        pass


class Engine:
#Двигатель - является составной частью автомобиля
    def __init__(self, *args):
        print(args[1])

    #def __repr__(self):
    #    return "Engine('%s', '%s')" % self.en_type, self.en_pow

    def show_errors():
        #показать ошибки работы двигателя
        pass

    def check_temp():
        #проверка ткемпературы двигателя
        pass

    def en_start():
        #завести двигатель
        pass

    def en_stop():
        #заглушить двигатель
        pass
    

class Transmission:
#Трансмиссия - является составной частью автомобиля
    def __init__(self, tr_type, num_gear):
        pass

    def shift_up():
        #повысить передачу
        pass

    def shift_down():
        #понизить передачу
        pass

    def dif_lock():
        #заблокировать дифференциал
        pass

    def dif_unlock():
        #разблокировать дифференциал
        pass


class Wheel:
#Колесо - является частью автомобиля
#радиус, ширина, высота покрышки, давление
    def __init__(self, R, W, H, P):
        pass

    def pump_up():
        #накачать колесо
        pass


class Car_Alarm():
#сигнализация
    def __init__(self):
        pass

    def alarm_on():
        #включить
        pass

    def alarm_off():
        #отключить
        pass
        

if __name__ == '__main__':
    #car1 = ('VolksWagen', 'Tuareg', 2014, ['биодизель', 265], 2500)
    #pprint(type(car1[3]))
    #en1 = Engine('turbodisel', 250)
    #pprint(en1)
    #car2 = Car('Toyota', 'LC200', 2019, en1, 3200)
    #pprint(car2)
    #car1.en_inst(en1)
    #pprint(car1)
    def adder(p1,p2, *nums):
        print(type(nums), nums[0], nums[1])

    adder('ee', 3, '5', 4)

    
