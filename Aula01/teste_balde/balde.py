from random import randint


class Balde:
    def __init__(self,__balde,__balde_atual):
        self.__balde = 0
        self.__balde_atual = 0

    def set_volume_balde(self,volume_balde):
        self.volume_balde = volume_balde
        if type(self.volume_balde) == int and self.volume_balde > 0:
            return self.volume_balde

    def get_volume_balde(self):
        return self.__balde

    def enchendo_balde(self,volume_agua):
        if self.__balde == 0:




    def sorteio(self):
        self.volume = randint(10,50)
        return self.volume


