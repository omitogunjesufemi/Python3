class P2:
    def __init__(self, x):
        self.x = x


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

p1 = P2(42)
p1.x = 1001
p1.x = -12
print(help(P2))
