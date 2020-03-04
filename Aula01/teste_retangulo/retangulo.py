class Retangulo:
    def __init__(self,ladoA, ladoB):
        self.__ladoA = ladoA
        self.__ladoB = ladoB


    def set_ladoA(self, ladoA):
        self.__ladoA = ladoA

    def set_ladoB(self, ladoB):
        self.__ladoB = ladoB

    def get_ladoA(self):
        return self.__ladoA

    def get_ladoB(self):
        return self.__ladoB

    def calc_area(self):
        self.area = self.__ladoA * self.__ladoB
        return self.area

obj = Retangulo('','')
obj.set_ladoA(9)
obj.set_ladoB(3)
print(obj.get_ladoA())
print(obj.get_ladoB())
print(obj.calc_area())