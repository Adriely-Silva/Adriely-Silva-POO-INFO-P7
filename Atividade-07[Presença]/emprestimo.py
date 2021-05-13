from livro import Livro
from associado import Associado

class Emprestimo:
    def __init__(self, data: int, livro: Livro, associado: Associado):
        self.data = data
    
