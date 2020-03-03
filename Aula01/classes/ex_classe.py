class Endereco:
    def __init__(self, rua, logradouro, cep, numero):
        self.__rua = rua
        self.__logradouro = logradouro
        self.__cep = cep
        self.__numero = numero

    def set_rua(self,__rua):
        self.__rua = __rua

    def set_logradouro(self,__logradouro):
        self.__logradouro = __logradouro

    def set_cep(self,__cep):
        self.__cep = __cep

    def set_numero(self,__numero):
        self.__numero = __numero

    def get_rua(self, __rua):
        return self.__rua

    def get_logradouro(self, __logradouro):
        return self.__logradouro

    def get_cep(self, __cep):
        return self.__cep

    def get_numero(self, __numero):
        return self.__numero


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.endereco = Endereco()

    def set_nome(self,__nome):
        self.__nome = __nome

    def set_sobrenome(self,__sobrenome):
        self.__sobrenome = __sobrenome

    def set_idade(self,__idade):
        self.__idade = __idade

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_idade(self):
        return self.__idade
