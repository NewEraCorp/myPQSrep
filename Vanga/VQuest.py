from str_functions import compare

class VQuest:
    def __init__(self, quest, answ):
        self.quest, self.answ = quest, answ 
        self.key = quest

    def __repr__(self):
        return "VQuest('%s', '%s')" % (self.quest, self.answ)

    def __eq__(self, obj):
        if type(obj) == VQuest:
            return (self.quest, self.answ) == (self.quest, self.answ)
        elif type(obj) == str:
            return self.__fuzzy_compare(obj)
        else:
            return self.__repr__() == obj.__repr__()

        def __fuzzy_compare(self, query):
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
            return max(rez)[0]

               
            return score > 0.49