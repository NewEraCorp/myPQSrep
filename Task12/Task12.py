from pprint import pprint

class Car:
#Автомобиль: имеет атрибуты: марка (бренд), модель, год выпуска,
#тип двигателя, мощность двигателястоимость
    def __init__(self, brand, model, age, cost, *engine):
        self.brand, self.model, self.age, self.cost = brand, model, age, cost
        if len(engine)==0:
            self.engine = None
        elif type(engine[0]) == Engine:
            self.engine=engine[0]
        else:
            self.engine = Engine(*engine)
    
    def __repr__(self):
        return "Car('%s', '%s', %s, %s, %s)" %\
               (self.brand, self.model, self.age, self.engine, self.cost)

    def en_inst(self, engine):
        #engine_installation
        if self.engine==None:
            self.engine=engine
        else:
            self.en_swap(engine)

    def en_swap(self, engine):
        #замена двигателя
        if self.engine!=None:
            self.engine=engine
        else:
            self.en_inst(engine)


class Engine:
#Двигатель - является составной частью автомобиля
    def __init__(self, *args):
        self.en_type = args[0]
        self.en_pow = args[1]

    def __repr__(self):
        return "Engine('%s', '%s')" % (self.en_type, self.en_pow)
        

if __name__ == '__main__':
    car1 = Car('VolksWagen', 'Tuareg', 2014, 2500, 'биодизель', 265)
    pprint(car1)
    en1 = Engine('turbodisel', 250)
    pprint(en1)
    car2 = Car('Toyota', 'LC200', 2019, 3200, en1)
    pprint(car2)
    car3 = Car('Range_Rover', 'Sport', 2015, 8500)
    pprint(car3)
    car3.en_inst(en1)
    pprint(car3)
    car1.en_swap(en1)
    pprint(car1)
    

