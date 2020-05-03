#14.1
class MyInt(int):
    def __add__(self, p):
        return super().__add__(p)+1


x = MyInt(2)
y = 2
print(x+y)
