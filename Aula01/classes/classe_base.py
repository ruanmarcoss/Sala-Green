from Aula01.classes.ex_classe import Pessoa

class Engenheiro(Pessoa):
    def __init__(self, tipo, cargo, nome, sobrenome, idade):
        self.__tipo = tipo
        self.__cargo = cargo
        super().__init__(nome,sobrenome,idade)


    def set_nome(self, tipo):
        self.__tipo = tipo

    def set_cargo(self,cargo):
        self.__cargo = cargo

    def get_nome(self):
        return self.__tipo

    def get_cargo(self):
        return self.__cargo