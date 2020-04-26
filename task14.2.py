class MyList(list):
    def __init__(self, *args, **kwargs):
        if (len(args)+len(kwargs))<=10:
            return super().__init__(args, *kwargs)
        else:
            raise Exception('>10')

    def append(self, obj):
        if len(self)<10:
            return super().append(obj)
        else:
            raise Exception('>10')
        

a=MyList(input('Введите данные: ')).split(' ')

a.append(12)


print(a)

