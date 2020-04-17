ENGINE_WORDS = {'лс', 'мощность', 'hp', 'мощнее', 'выше', 'ниже', 'бензин', 'дизель'}


class MyEngine:
    """description of class"""
    def __init__(self, en_type, en_pow):
        self.en_type, self.en_pow = en_type, en_pow

    def __repr__(self):
        return "Engine('%s', %s)" % (self.en_type, self.en_pow)

    def by_en_type(Q, W):     
        return

    def by_en_pow(Q):
        return 



