class Dobradura:

    def get_dobrar(self,numero_dobradura):
        self.numero_dobradura = 1
        if type(numero_dobradura) == int and numero_dobradura > 0:
            for i in range(0, numero_dobradura):
                self.numero_dobradura = self.numero_dobradura * 2
            return self.numero_dobradura
        else:
            return False






