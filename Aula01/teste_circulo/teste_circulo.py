import random
from Aula01.teste_circulo.circulo import Circulo

a = ['Abóbora','Açafrão','Amarelo','Âmbar','Ameixa','Amêndoa','Ametista',
     'Anil','Azul','Bege','Bordô','Branco','Bronze','Cáqui','Caramelo',
     'Carmesim','Carmim','Castanho','Cereja','Chocolate','Ciano','Cinza',
     'Cinzento','Cobre','Coral','Creme','Damasco','Dourado','Escarlate',
     'Esmeralda','Ferrugem','Fúcsia','Gelo','Grená','Gris','Índigo','Jade',
     'Jambo','Laranja','Lavanda','Lilás','Limão','Loiro','Magenta','Malva',
     'Marfim','Marrom','Mostarda','Negro','Ocre','Oliva','Ouro','Pêssego',
     'Prata','Preto','Púrpura','Rosa','Roxo','Rubro','Salmão','Sépia','Terracota',
     'Tijolo','Turquesa','Uva','Verde','Vermelho','Vinho','Violeta']

for i in a:
    pass


cor = 'azul'
raio = 5
material = 'ferro'

circulo = Circulo(cor,raio,material)

print('Inicio do teste')

assert cor == circulo._Circulo__cor ,'Erro, cor está atribuida'
print('Teste OK')