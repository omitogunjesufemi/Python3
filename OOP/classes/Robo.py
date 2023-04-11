class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year


    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")

        if self.__build_year:
            print("I was built in " + str(self.__build_year))
        else:
            print("Build date unknown!")


    def set_name(self, name):
        self.__name = name


    def get_name(self):
        return self.__name


    def get_build_year(self):
        return self.__build_year


    def set_build_year(self, build_year):
        self.__build_year = build_year


x = Robot("Henry", 2008)
y = Robot("Marvin", 2010)

for rob in [x, y]:
    rob.say_hi()
    if rob.get_name() == "Henry":
        rob.set_build_year(1993)
    print("I was built in the year " + str(rob.get_build_year()) + "!")
