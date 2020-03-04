from Aula01.teste_retangulo.retangulo import Retangulo

dado = 9
dado2 = 3

obj = Retangulo(dado,dado2)

print('Inicio do teste''\n'*2)

print('Teste do get_tamanho_lado()')
assert obj.set_ladoA() == obj.get_ladoA(), f'Erro, o valor não estão sendo repassados'
assert obj.calc_area() == 27, f'Erro de calculo'
print('Teste do get_tamanho_lado(): OK')






