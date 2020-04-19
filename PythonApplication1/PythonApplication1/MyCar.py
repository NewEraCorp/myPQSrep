from task5.str_functions import compare, int_val
from itertools import product
from MyEngine import MyEngine

BRAND_WORDS = {'марка', 'бренд', 'фирма'}
MODEL_WORDS = {'модель', 'название'}
YEAR_WORDS = {'год выпуска', 'гв', 'старше', 'младше'}
ENGINE_WORDS = {'двигатель', 'лс', 'мощность', 'hp', 'мощнее', 'выше', 'ниже'}
COST_WORDS = {'цена', 'стоимость', 'дороже', 'дешевле'}

class MyCar:

    def __init__(self, brand, model, year, engine, cost, vin):
        self.brand, self.model, self.year, self.engine, self.cost, self.vin =\
          brand, model, year, engine, cost, vin     #Строгой рекомендации нет, по-моему так лучше
        self.key=(brand, model, vin)

    def __repr__(self):
        return "Car('%s', '%s', %s, %s, %s, %s)" %\
               (self.brand, self.model, self.year, self.engine, self.cost, self.vin)    #Выровнял по оператору

    def search_on_param (self, req):
        list_req = req.split()    #Изменил название переменной, стало понятнее ее назначение (если я сам правильно помню
        if list_req[0]=='year' and len(list_req)==3:
           if list_req[1]=='больше':
              if self.year >=int(list_req[2]):
                  return True    #Отсутп 4 пробела
              else: return False    #Если один оператор, можно в той же строчке
           elif list_req[1]=='меньше':
              if self.year <=int(list_req[2]):
                  return True    #Отсутп 4 пробела   
              else:
                  return False
        elif list_req[0]=='hp':    #Исправил отступы по всей функции
            if list_req[1]=='больше' and len(list_req)==3:
                if self.hp >=int(list_req[2]):
                    return True
                else: return False
            elif list_req[1]=='меньше':
                if self.hp <=int(list_req[2]):
                    return True
                else:
                    return False
        elif list_req[0]=='cost':
            if list_req[1]=='больше' and len(list_req)==3:
                if self.cost >=int(list_req[2]):
                    return True
                else: return False
            elif list_req[1]=='меньше':
                if self.cost <=int(list_req[2]):
                    return True
                else:
                    return False
        elif list_req[0]=='vin':
            if list_req[1]=='больше' and len(list_req)==3:
                if self.vin >=int(list_req[2]):
                    return True
                else: return False
            elif list_req[1]=='меньше':
                if self.vin <=int(list_req[2]):
                    return True
                else:
                    return False
        elif list_req[0]=='марка':
            if self.brand==l_req[1]:
                if len(list_req)==2:
                    return True
                elif self.model==list_req[2]:
                    return True
            else: return False
    
    def fuzzy_search_on_param (self, req):    #Исправил отступы по всей функции
        list_req = req.split()
        if list_req[0]=='year':
            if list_req[1]=='больше' and len(list_req)==3:
              if self.year >=(int(list_req[2])-1) :
                return True
              else: return False
            elif list_req[1]=='меньше' and len(list_req)==3:
              if self.year <=(int(l_req[2])+1):
                    return True
              else: return False
            elif len(list_req)==2 and (self.year<=(int(list_req[1])+1)\
                 and self.year>=(int(list_req[1])-1)):
                return True
            else: return False
        elif list_req[0]=='hp':    #Название поля класса не меняю, т.к. оно устарело
            if list_req[1]=='больше' and len(list_req)==3:
                if self.hp >=(int(list_req[2])-10):
                    return True
                else: return False
            elif list_req[1]=='меньше' and len(list_req)==3:
                if self.hp <=(int(list_req[2])+10):
                    return True
                else: return False
            elif (len(list_req)==2 and (self.hp<=(int(list_req[1])+10) and\
                 self.hp>=(int(list_req[1])-10))):
                return True
            else: return False
        elif list_req[0]=='cost':
            if list_req[1]=='больше' and len(list_req)==3:
                if self.cost >=(int(list_req[2])-1000):
                    return True
                else: return False
            elif list_req[1]=='меньше' and len(list_req)==3:
                if self.cost <=(int(list_req[2])-1000):
                    return True
                else: return False
            elif len(list_req)==2 and (self.cost<=(int(list_req[1])+1000) and\
                self.cost>=(int(list_req[1])-1000)):
                return True
            else: return False
        elif list_req[0]=='vin':
            if list_req[1]=='больше':
                if self.vin >=int(list_req[2]):
                    return True
                else: return False
            elif list_req[1]=='меньше':
                if self.vin <=int(list_req[2]):
                    return True
                else:
                    return False
        elif list_req[0]=='марка':
            if compare(list_req[1],self.brand)>=0.3:
                if len(list_req)==2:
                    return True
                elif compare(list_req[2],self.model)>=0.3:
                    return True
            else: return False
            
    def __eq__(self, obj):
        if type(obj) == MyCar:
            return (self.brand, self.model, self.year, self.engine, self.cost, self.vin) ==\
                   (obj.brand, obj.model, obj.year, obj.engine, obj.cost, obj.vin)
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
                return query_year < int(self.year)
            if 'старше' in Q:
                return query_year > int(self.year)
            return query_year + 1 >= int(self.year) >= query_year - 1
       
        def by_en_type(Q):
            Q = Q - ENGINE_WORDS
            W = set(self.engine.en_type.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
            return max(rez)[0]

        def by_en_pow(Q):
            query_engine = max([ int_val(q) for q in Q ])
            if 'выше' in Q:
                return query_engine < self.engine.en_pow
            if 'ниже' in Q:
                return query_engine > self.engine.en_pow
            return query_engine + 10 >= int(self.engine.en_pow) >= query_engine - 10          

        def by_cost(Q):
            query_cost = max([ int_val(q) for q in Q ])
            if 'дороже' in Q:
                return query_cost < int(self.cost)
            if 'дешевле' in Q:
                return query_cost > int(self.cost)
            return query_cost + 1000 >= int(self.cost) >= query_cost - 1000

        q_words = set(query.split())
        score = 0
        for m_words, method in zip([BRAND_WORDS, MODEL_WORDS, YEAR_WORDS, 
                                    ENGINE_WORDS, ENGINE_WORDS, COST_WORDS],
                                   [by_brand, by_model, by_year, by_en_type, 
                                    by_en_pow, by_cost]):
            if m_words & q_words:
                score += method(q_words)
               
        return score > 0.49
