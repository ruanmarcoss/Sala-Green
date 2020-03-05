# Polimorfismo, altera o comportamento de acordo com a entrada;
def soma(n1:int,n2:int) -> int:
    return int(n1 + n2)


def multiplicacao(n1:int,n2:int,n3=1) -> int:
    return n1 * n2 * n3

def string(l1:str,l2:str) -> str:
    return l1 + l2



print(soma(5,15))
print(multiplicacao(2,5))
print(string('Ru','an'))
