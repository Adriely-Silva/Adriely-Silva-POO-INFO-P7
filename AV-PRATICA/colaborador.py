from movimentofolha import MovimentoFolha
from tipomovimento import TipoMovimento

class Colaborador:
    def __init__(self, codigo : int, nome : str, endereco : str, telefone : str, bairro: str, cep : str, cpf : str, salario_atual: float):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.bairro = bairro
        self.cep = cep
        self.cpf = cpf
        self.salario_atual = salario_atual
        self.movimentos = []

    def calcular_salario(self):
        total_proventos = 0.0
        total_descontos = 0.0

        for movimento in self.movimentos:
            if movimento.tipo_movimento == TipoMovimento.P:
                total_proventos += movimento.valor
            elif movimento.tipo_movimento == TipoMovimento.D:
                total_descontos += movimento.valor

        valor_liquido = (self.salario_atual + total_proventos) - total_descontos

        print("MÉTODO CALCULAR_SALÁRIO")
        print("===============================================================================================================")
        print("%s %s %4s %s" % ("Código:", self.codigo, "Nome:", self.nome))
        print("%s %s %4s %s %4s %s %4s %s" % ("Sálario:", self.salario_atual, "Total de proventos:", total_proventos, "Total de descontos:",total_descontos, "Valor Liquido a Receber:", valor_liquido))
        print("_______________________________________________________________________________________________________________\n\n")
 
    def inserir_movimentos(self, movimento_folha : MovimentoFolha):
        self.movimentos.append(movimento_folha)