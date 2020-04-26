from str_functions import compare

class VQuest:
    def __init__(self, quest, answ):
        self.quest, self.answ = quest, answ 
        self.key = quest

    def __repr__(self):
        return "VQuest('%s', '%s')" % (self.quest, self.answ)