class Car:
#Автомобиль: имеет атрибуты: марка (бренд), модель, год выпуска,
#пробег, цвет, тип двигателя, мощность двигателя, тип трансмиссии, стоимость, 
#расход топлива, тип колес
    def __init__(self, brand, model, age, millage, collor, en_type, en_pow,
                 transmission, cost, fuel_consuption, wheel):
        pass

    def check_systems():
        #проверка систем автомобиля при включении зажигания
        pass

    def alarm_activ():
        #активация сигнализации
        pass


class Engine:
#Двигатель - является составной частью автомобиля
    def __init__(self, en_type, en_pow):
        self.en_type, self.en_pow = en_type, en_pow

    def show_errors():
        #показать ошибки работы двигателя
        pass

    def check_temp():
        #проверка ткмпературы двигателя
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