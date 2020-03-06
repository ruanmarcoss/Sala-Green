from Aula01.ex_classes.endereco import Endereco
from Aula01.ex_classes.pessoa import Pessoa

e = Endereco('','','')
p = Pessoa('','','')


e.set_rua('progresso')
e.set_bairro('jordao')
e.set_cidade('blumenau')
print(e.get_rua())
print(e.get_bairro())
print(e.get_cidade())
p.set_nome('ruan')
p.set_idade(17)
p.set_sobrenome('silva')
print(p.get_nome())
print(p.get_sobrenome())
print(p.get_idade())