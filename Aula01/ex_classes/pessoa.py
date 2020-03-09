# crie uma classe Pessoa com:
# 3 atributos e 7 métodos

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.__nome = ''
        self.__sobrenome = ''
        self.__idade = 0
        if self.verifica_nome(nome):
            self.__nome = nome
        if self.verifica_sobrenome(sobrenome):
            self.__sobrenome = sobrenome
        if self.verifica_idade(idade):
            self.__idade = idade

    def verifica_idade(self,idade):
        if type(idade) == int and idade > 0:
            return True
        return False

    def verifica_nome(self,nome):
        if type(nome) == str:
            return True
        return False

    def verifica_sobrenome(self,sobrenome):
        if type(sobrenome) == str:
            return True
        return False

    def set_nome(self, nome) ->None:
        if self.verifica_nome(nome):
            self.__nome = nome

    def set_sobrenome(self, sobrenome)->None:
        if self.verifica_sobrenome(sobrenome):
            self.__sobrenome = sobrenome

    def set_idade(self, idade)-> None:
        if self.verifica_idade(idade):
            self.__idade = idade

    def get_nome(self) ->str:
        return self.__nome

    def get_sobrenome(self) ->str:
        return self.__sobrenome

    def get_idade(self) ->int:
        return self.__idade