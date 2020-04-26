class Car:
#јвтомобиль: имеет атрибуты: марка (бренд), модель, год выпуска,
#пробег, цвет, тип двигател€, мощность двигател€, тип трансмиссии, стоимость, 
#расход топлива, тип колес
    def __init__(self, brand, model, age, millage, collor, en_type, en_pow,
                 transmission, cost, fuel_consuption, wheel):
        pass


class Engine:
#ƒвигатель - €вл€етс€ составной частью автомобил€
    def __init__(self, en_type, en_pow):
        self.en_type, self.en_pow = en_type, en_pow


    

class Transmission:
#“рансмисси€ - €вл€етс€ составной частью автомобил€
    def __init__(self, tr_type, num_gear):
        pass


class Wheel:
# олесо - €вл€етс€ частью автомобил€
#радиус, ширина, высота покрышки, давление
    def __init__(self, R, W, H, P):
        pass

    def pump_up():
        #накачать колесо
        pass