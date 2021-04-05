class Lista_Encadeada:
    def __init__(self):
        self.lista = []
    def inserir(self, posicao, valor):
        self.lista.insert(posicao, valor)
    def remover(self, posicao):
        self.lista.pop(posicao)
    def retornar_lista(self):
        return self.lista