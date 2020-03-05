import random
import math

class Circulo:

    def __init__(self,cor,raio,material):
        self.__cor = cor
        self.__raio = raio
        self.__material = material

    def set_cor(self, cor):
        self.__cor = cor

    def set_raio(self, raio):
        self.__raio = raio

    def set_material(self, material):
        self.__material = material

    def get_cor(self):
        return self.__cor

    def get_raio(self):
        return self.__raio

    def get_material(self):
        return self.__material

    def get_cores(self):
        return self.cores

    def sorteio(self):
        a = ['Abóbora', 'Açafrão', 'Amarelo', 'Âmbar', 'Ameixa', 'Amêndoa', 'Ametista',
             'Anil', 'Azul', 'Bege', 'Bordô', 'Branco', 'Bronze', 'Cáqui', 'Caramelo',
             'Carmesim', 'Carmim', 'Castanho', 'Cereja', 'Chocolate', 'Ciano', 'Cinza',
             'Cinzento', 'Cobre', 'Coral', 'Creme', 'Damasco', 'Dourado', 'Escarlate',
             'Esmeralda', 'Ferrugem', 'Fúcsia', 'Gelo', 'Grená', 'Gris', 'Índigo', 'Jade',
             'Jambo', 'Laranja', 'Lavanda', 'Lilás', 'Limão', 'Loiro', 'Magenta', 'Malva',
             'Marfim', 'Marrom', 'Mostarda', 'Negro', 'Ocre', 'Oliva', 'Ouro', 'Pêssego',
             'Prata', 'Preto', 'Púrpura', 'Rosa', 'Roxo', 'Rubro', 'Salmão', 'Sépia', 'Terracota',
             'Tijolo', 'Turquesa', 'Uva', 'Verde', 'Vermelho', 'Vinho', 'Violeta']

        self.cor = random.choice(a)
        return self.cor

    def troca_cor(self):
        self.opcao = input('Digite um opção: ')
        if self.opcao == 'sim':
            self.set_cor(self.sorteio())
        else:
            return self.get_cor()

    def mostra_cor(self):
        return self.get_cor()

    def area(self):
        self.resultado = (math.pi*self.get_raio()**2)
        return self.resultado


# ob = Circulo('','','')
# ob.set_cor('azul')
# print(ob.get_cor())
# ob.troca_cor()
# print(f'objeto get {ob.get_cor()}')



