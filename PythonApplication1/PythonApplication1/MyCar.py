from task5.my_str_cmp import compare

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
        if l_req[0]=='year' and len(l_req)==3:
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
           if l_req[1]=='больше' and len(l_req)==3:
              if self.hp >=int(l_req[2]):
                return True
              else: return False
           elif l_req[1]=='меньше':
                if self.hp <=int(l_req[2]):
                    return True
                else:
                    return False
        elif l_req[0]=='cost':
           if l_req[1]=='больше' and len(l_req)==3:
              if self.cost >=int(l_req[2]):
                return True
              else: return False
           elif l_req[1]=='меньше':
                if self.cost <=int(l_req[2]):
                    return True
                else:
                    return False
        elif l_req[0]=='vin':
           if l_req[1]=='больше' and len(l_req)==3:
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
    
    def fuzzy_search_on_param (self, req):
        l_req = req.split()
        if l_req[0]=='year':
           if l_req[1]=='больше' and len(l_req)==3:
              if self.year >=(int(l_req[2])-1) :
                return True
              else: return False
           elif l_req[1]=='меньше' and len(l_req)==3:
              if self.year <=(int(l_req[2])+1):
                    return True
              else: return False
           elif len(l_req)==2 and (self.year<=(int(l_req[1])+1) and self.year>=(int(l_req[1])-1)):
               return True
           else: return False
        elif l_req[0]=='hp':
           if l_req[1]=='больше' and len(l_req)==3:
              if self.hp >=(int(l_req[2])-10):
                return True
              else: return False
           elif l_req[1]=='меньше' and len(l_req)==3:
                if self.hp <=(int(l_req[2])+10):
                    return True
                else: return False
           elif (len(l_req)==2 and (self.hp<=(int(l_req[1])+10) and self.hp>=(int(l_req[1])-10))):
               return True
           else: return False
        elif l_req[0]=='cost':
           if l_req[1]=='больше' and len(l_req)==3:
              if self.cost >=(int(l_req[2])-1000):
                return True
              else: return False
           elif l_req[1]=='меньше' and len(l_req)==3:
                if self.cost <=(int(l_req[2])-1000):
                    return True
                else: return False
           elif len(l_req)==2 and (self.cost<=(int(l_req[1])+1000) and self.cost>=(int(l_req[1])-1000)):
               return True
           else: return False
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
            if compare(l_req[1],self.brand)>=0.3:
                if len(l_req)==2:
                    return True
                elif compare(l_req[2],self.model)>=0.3:
                    return True
            else: return False               


