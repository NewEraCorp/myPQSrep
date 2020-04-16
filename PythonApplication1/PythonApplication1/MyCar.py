class MyCar:

    def __init__(self, brand, model, year, hp, cost, vin):
        self.brand, self.model, self.year, self.hp, self.cost, self.vin =\
           brand, model, year, hp, cost, vin
        self.key=(brand, model, vin)

    def __repr__(self):
        return "Car('%s', '%s', %s, %s, %s, %s)" %\
           (self.brand, self.model, self.year, self.hp, self.cost, self.vin)

