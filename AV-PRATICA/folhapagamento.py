from movimentofolha import MovimentoFolha
from tipomovimento import TipoMovimento
from colaborador import Colaborador

class FolhaPagamento:
    def __init__(self, mes : int, ano : int):
        self.mes = mes
        self.ano = ano
        self.total_descontos = 0.0
        self.total_proventos = 0.0
        self.movimentos = []
        self.colaboradores = []


    def calcular_folha(self):
        for movimento in self.movimentos:
            if movimento.tipo_movimento == TipoMovimento.P:
                self.total_proventos += movimento.valor
            elif movimento.tipo_movimento == TipoMovimento.D:
                self.total_descontos += movimento.valor

        total_salarios = 0
        for colaborador in self.colaboradores:
            total_salarios += colaborador.salario_atual

        total_pagar = (total_salarios + self.total_proventos) - self.total_descontos
        print("======================================")
        print("MÉTODO CALCULAR_FOLHA")
        print("Total de sálarios:", total_salarios, "\nTotal de proventos:", self.total_proventos, "\nTotal de descontos:", self.total_descontos, "\nTotal a pagar:", total_pagar)
        print("======================================\n")

    def inserir_movimentos(self, movimento_folha : MovimentoFolha):
        self.movimentos.append(movimento_folha)
    
    def inserir_colaboradores(self, colaborador : Colaborador):
        self.colaboradores.append(colaborador)