from task5.str_functions import compare, int_val
from itertools import product

BRAND_WORDS = {'марка', 'бренд', 'фирма'}
MODEL_WORDS = {'модель', 'название'}
YEAR_WORDS = {'год выпуска', 'гв', 'старше', 'младше'}
HP_WORDS = {'лс', 'мощность', 'hp', 'мощнее', 'выше', 'ниже'}
COST_WORDS = {'цена', 'стоимость', 'дороже', 'дешевле'}

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
            
    def __eq__(self, obj):
        if type(obj) == MyCar:
            return (self.brand, self.model, self.year, self.hp, self.cost, self.vin) ==\
              (obj.brand, obj.model, obj.year, obj.hp, obj.cost, obj.vin)
        elif type(obj) == str:
            return self.__fuzzy_compare(obj)
        else:
            return self.__repr__() == obj.__repr__()

    def __fuzzy_compare(self, query):
        def by_brand(Q):
            Q = Q - BRAND_WORDS
            W = set(self.brand.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
            return max(rez)[0]
           
       
        def by_model(Q):
            Q = Q - MODEL_WORDS
            W = set(self.model.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
            return max(rez)[0]
       
        def by_year(Q):
            query_year = max([ int_val(q) for q in Q ])
            if 'младше' in Q:
                return query_year < self.year
            if 'старше' in Q:
                return query_year > self.year
            return query_year + 1 >= self.year >= query_year - 1
       
        def by_hp(Q):
            query_hp = max([ int_val(q) for q in Q ])
            if 'мощнее' in Q or 'выше' in Q:
                return query_hp < self.hp
            if 'меньше' in Q:
                return query_hp> self.hp
            return query_hp + 10 >= self.hp >= query_hp - 10

        def by_cost(Q):
            query_cost = max([ int_val(q) for q in Q ])
            if 'дороже' in Q:
                return query_cost < self.cost
            if 'дешевле' in Q:
                return query_cost > self.cost
            return query_cost + 1000 >= self.cost >= query_cost - 1000

        q_words = set(query.split())
        score = 0
        for m_words, method in zip([BRAND_WORDS, MODEL_WORDS, YEAR_WORDS, HP_WORDS, COST_WORDS],
                                   [by_brand, by_model, by_year, by_hp, by_cost]):
            if m_words & q_words:
                score += method(q_words)
               
        return score > 0.49
