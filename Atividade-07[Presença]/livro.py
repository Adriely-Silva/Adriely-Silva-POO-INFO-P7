from autor import Autor
from editora import Editora

class Livro:
    def __init__ (self, ISBN: int, exemplar: int, titulo: str, local_de_edicao: str, palavra_chaves: str[8], autor: Autor, editora: Editora):
        self.ISBN = ISBN
        self.exemplar = exemplar
        self.titulo = titulo
        self.local_de_edicao =  local_de_edicao
        self.palavra_chaves = palavra_chaves


