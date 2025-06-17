from Elemento import Elemento

class Lista:

                #INICIAR

    def __init__(self):
        self.primeiro = None

                #CRIAR

    #fabrica de criar novos elementos:
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None)
        return e

                #IMPRIMIR ultimo

    def print_lista(self):
        aux = self.primeiro
        while (aux != None):
            print(aux.valor)
            aux = aux.proximo

                #ADICIONAR penultimo

    def add(self, valorQualquer):
        aux = self.primeiro
        if aux != None:
            while aux.proximo != None:
                aux = aux.proximo
            aux.proximo = self.criarNovoElemento(valorQualquer)
        else:
            self.primeiro = self.criarNovoElemento(valorQualquer)

                #REMOVER
testando!
    def remove(self):
        aux = self.primeiro
        if aux != None:
            while aux.proximo != None:
                aux = aux.proximo
        del aux


minhaLista = Lista()

minhaLista.add(1)
minhaLista.add(10)
minhaLista.add(100)
minhaLista.add(1000)
minhaLista.add(10000)

minhaLista.remove()

minhaLista.print_lista()
