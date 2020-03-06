
class Endereco:
    def __init__(self, rua, bairro, cidade):
        self.__rua = ''
        self.__bairro = ''
        self.__cidade = ''
        if self.verifica_rua(rua):
            self.__rua = rua
        if self.verifica_bairro(bairro):
            self.__bairro = bairro
        if self.verifica_cidade(cidade):
            self.__cidade = cidade

    def verifica_rua(self,rua):
        if type(rua) == str:
            return True
        return False

    def verifica_bairro(self, bairro):
        if type(bairro) == str:
            return True
        return False

    def verifica_cidade(self, cidade):
        if type(cidade) == str:
            return True
        return False

    def set_rua(self, rua):
        if self.verifica_rua(rua):
            self.__rua = rua

    def set_bairro(self, bairro):
        if self.verifica_bairro(bairro):
            self.__bairro = bairro

    def set_cidade(self, cidade):
        if self.verifica_cidade(cidade):
            self.__cidade = cidade

    def get_rua(self)->str:
        return self.__rua

    def get_bairro(self)->str:
        return self.__bairro

    def get_cidade(self)->str:
        return self.__cidade