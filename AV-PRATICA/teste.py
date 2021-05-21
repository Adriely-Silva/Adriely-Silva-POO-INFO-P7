from tipomovimento import TipoMovimento
from movimentofolha import MovimentoFolha
from folhapagamento import FolhaPagamento
from colaborador import Colaborador

class Teste:
    def main():

        FP = FolhaPagamento(9, 2019)

        #Cinco objetos CL (Colaborador)
        CL01 = Colaborador(100, "Manoel Claudino", "Av 13 de Maio 2081", "88671020", "Benfica", "60020-060" , "124543556-89", 4500.00)

        CL02 = Colaborador(200,"Carmelina da Silva", "Avenida dos Expedicionários 1200", "3035-1280", "Aeroporto", "60530-020" , "301789435-54", 2500.00)

        CL03 = Colaborador(300, "Gurmelina Castro Saraiva", "Av João Pessoa 1020","3235-1089", "Damas", "60330-090" , "350245632-76", 3000.00) 

        CL04 = Colaborador(400, "José Guimarães", "R. Sátiro Dias", "89346754", "Montese", "60420-430", "560285652-86", 3500.00)

        CL05 = Colaborador(500, "Carol Freitas da Silva", "R. Haroldo Torres", "92345678", "Alagadico Sao Gerardo", "60320-104","780238662-93", 4000.00 )

        #Objetos MovimentoFolha
        MF01 = MovimentoFolha(100, "Salario", 4500.00, TipoMovimento.P)

        MF02 = MovimentoFolha(100, "Plano Saúde", 1000.00, TipoMovimento.P)

        MF03 = MovimentoFolha(100, "Pensão", 600.00, TipoMovimento.D)

        MF04 = MovimentoFolha(200, "Salario", 2500.00, TipoMovimento.P)

        MF05 = MovimentoFolha(200, "Gratificação", 1000.00, TipoMovimento.P)

        MF06 = MovimentoFolha(200, "Faltas", 600.00, TipoMovimento.D)

        MF07 = MovimentoFolha(300, "Salario", 4500.00, TipoMovimento.P)

        MF08 = MovimentoFolha(300, "Plano Saúde", 1000.00, TipoMovimento.P)

        MF09 = MovimentoFolha(300, "Pensão", 600.00, TipoMovimento.D)

        #Inserir todos os objetos do tipo MovimentoFolha da lista movimentos do objeto FP
        FP.inserir_movimentos(MF01)

        FP.inserir_movimentos(MF02)

        FP.inserir_movimentos(MF03)

        FP.inserir_movimentos(MF04)

        FP.inserir_movimentos(MF05)

        FP.inserir_movimentos(MF06)

        FP.inserir_movimentos(MF07)

        FP.inserir_movimentos(MF08)

        FP.inserir_movimentos(MF09)

        #Inserir os objetos do tipo MovimentoFolha na lista movimentos de cada objeto Colaborador.
        CL01.inserir_movimentos(MF01)

        CL01.inserir_movimentos(MF02)

        CL01.inserir_movimentos(MF03)

        CL02.inserir_movimentos(MF04)

        CL02.inserir_movimentos(MF05)

        CL02.inserir_movimentos(MF06)

        CL03.inserir_movimentos(MF07)

        CL03.inserir_movimentos(MF08)

        CL03.inserir_movimentos(MF09)

        #Inserir os colaboradres na Folha de Pagamento

        FP.inserir_colaboradores(CL01)

        FP.inserir_colaboradores(CL02)

        FP.inserir_colaboradores(CL03)

        FP.inserir_colaboradores(CL04)

        FP.inserir_colaboradores(CL05)

        #Imprimir Folha de Pagamento
        FP.calcular_folha()

        #Imprimir Salário do CL01
        CL01.calcular_salario()

        #Imprimir Salário do CL02
        CL02.calcular_salario()

        #Imprimir Salário do CL03
        CL03.calcular_salario()

        #Imprimir Salário do CL04
        CL04.calcular_salario()

        #Imprimir Salário do CL05
        CL05.calcular_salario()

if __name__ == '__main__':
    Teste.main()