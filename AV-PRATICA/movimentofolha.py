from tipomovimento import TipoMovimento

class MovimentoFolha:
    def __init__(self, codigo_colaborador : int, descricao : str, valor : float, tipo_movimento : TipoMovimento):
        self.codigo_colaborador = codigo_colaborador
        self.descricao = descricao
        self.valor = valor
        self.tipo_movimento = tipo_movimento