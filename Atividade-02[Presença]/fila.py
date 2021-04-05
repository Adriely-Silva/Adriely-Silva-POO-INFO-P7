class Fila:
    def __init__(self):
        self.lista = []
    def inserir(self, valor):
        self.lista.append(valor)      
    def remover(self):
        self.lista.pop(0)
    def retornar_lista(self):
        return self.lista