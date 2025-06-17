class Elemento:

    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo
    
    def lacoDoFimDoMundo(self):
        while(self.proximo != None):
            print(self.valor)
            self = self.proximo