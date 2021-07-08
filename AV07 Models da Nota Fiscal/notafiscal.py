"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from itemnotafiscal import ItemNotaFiscal

class NotaFiscal():         

    def __init__(self, id, codigo, cliente):
        self._id = id
        self._codigo = codigo
        self._cliente = cliente 
        self._data = datetime.datetime.now()   
        self._itens = []
        self._valorNota = 0.0        

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente    

    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self._valorNota = valor

    def imprimirNotaFiscal(self):  
        texto = ''     
        texto += "---------------------------------------------------------------------------------------------------------------"
        texto += "%s %99s "  % ("NOTA FISCAL", self._data.strftime("%d/%m/%Y")) 
        texto +="%s %4s %8s %4s" % ("Cliente:", self._cliente._codigo, "Nome:", self._cliente._nome)
        texto +="%s %4s" % ("CPF/CNPJ:", self._cliente._cnpjcpf)
        texto +="---------------------------------------------------------------------------------------------------------------"
        texto +="%s" % ("ITENS")
        texto +="---------------------------------------------------------------------------------------------------------------"
        texto += "%s %12s %55s %15s %15s" % ("Seq", "Descrição", "QTD", "Valor Unit", "Preço")
        texto += "----   --------------------------------------------------------     -----    ------------    ------------------"
        for item in self._itens:
            texto += "%03d %20s %48s %15s %21s" % (item._sequencial, item._descricao, item._quantidade, item._valorUnitario, item._valorItem)
        texto +="_______________________________________________________________________________________________________________"
        texto +="%s %.2f" % ("Valor Total:", self._valorNota)
        return texto