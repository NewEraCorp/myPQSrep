class MyCar:

    def __init__(self, brand, model, year, hp, cost, vin):
        self.brand, self.model, self.year, self.hp, self.cost, self.vin =\
           brand, model, year, hp, cost, vin
        self.key=(brand, model, vin)

    def __repr__(self):
        return "Car('%s', '%s', %s, %s, %s, %s)" %\
           (self.brand, self.model, self.year, self.hp, self.cost, self.vin)

    def search_on_param (self, req):
        l_req = req.split()
        if l_req[0]=='year':
           if l_req[1]=='больше':
              if self.year >=int(l_req[2]):
                return True
              else: return False
           elif l_req[1]=='меньше':
              if self.year <=int(l_req[2]):
                    return True
              else:
                  return False
        elif l_req[0]=='hp':
           if l_req[1]=='больше':
              if self.hp >=int(l_req[2]):
                return True
              else: return False
           elif l_req[1]=='меньше':
                if self.hp <=int(l_req[2]):
                    return True
                else:
                    return False
        elif l_req[0]=='cost':
           if l_req[1]=='больше':
              if self.cost >=int(l_req[2]):
                return True
              else: return False
           elif l_req[1]=='меньше':
                if self.cost <=int(l_req[2]):
                    return True
                else:
                    return False
        elif l_req[0]=='vin':
           if l_req[1]=='больше':
              if self.vin >=int(l_req[2]):
                return True
              else: return False
           elif l_req[1]=='меньше':
                if self.vin <=int(l_req[2]):
                    return True
                else:
                    return False
        elif l_req[0]=='марка':
            if self.brand==l_req[1]:
                if len(l_req)==2:
                    return True
                elif self.model==l_req[2]:
                    return True
            else: return False
                   


