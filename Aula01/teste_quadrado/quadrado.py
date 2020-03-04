class Quadrado:
    def __init__(self, tamanho_lado):
        self.__tamanho_lado = tamanho_lado


    def set_tamanho_lado(self, tamanho_lado):
        self.__tamanho_lado = tamanho_lado

    def get_tamanho_lado(self):
        return self.__tamanho_lado

    def calc_area(self):
        self.area = self.__tamanho_lado * self.__tamanho_lado
        return self.area



obj = Quadrado('')
# obj.set_tamanho_lado(5)
# print(obj.get_tamanho_lado())

if obj.set_tamanho_lado(5) == obj.get_tamanho_lado():
    print('deu boa')
else:
    print('deu ruim')