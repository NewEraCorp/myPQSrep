class MyList(set):
    def __init__(self, *args, **kwargs):
            return super().__init__(args, *kwargs)


a=MyList(1, 1, 2, 3, 6, 4, 6)

print(a)

