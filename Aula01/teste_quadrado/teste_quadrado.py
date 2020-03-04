from Aula01.teste_quadrado.quadrado import Quadrado

dado = 5
obj = Quadrado(dado)
obj.set_tamanho_lado()
print(obj.get_tamanho_lado())

print('Inicio do teste''\n'*2)

print('Teste do get_tamanho_lado()')
assert set == obj.get_tamanho_lado(), f'Erro, o valor: {set} não estão sendo repassados'
assert obj.calc_area() == 25, f'Erro de calculo'
print('Teste do get_tamanho_lado(): OK')
