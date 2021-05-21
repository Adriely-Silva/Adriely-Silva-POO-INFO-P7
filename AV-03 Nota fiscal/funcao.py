def imprimirNotaFiscal(self):       
        print("---------------------------------------------------------------------------------------------------------------")
        print("%s %99s "  % ("NOTA FISCAL", self._data.strftime("%d/%m/%Y"))) 
        print("%s %4s %8s %4s" % ("Cliente:", self._cliente._codigo, "Nome:", self._cliente._nome))
        print("%s %4s" % ("CPF/CNPJ:", self._cliente._cnpjcpf))
        print("---------------------------------------------------------------------------------------------------------------")
        print("%s" % ("ITENS"))
        print("---------------------------------------------------------------------------------------------------------------")
        print("%s %12s %55s %15s %15s" % ("Seq", "Descrição", "QTD", "Valor Unit", "Preço"))
        print("----   --------------------------------------------------------     -----    ------------    ------------------")
        for item in self._itens:
            print("%03d %20s %48s %15s %21s" % (item._sequencial, item._descricao, item._quantidade, item._valorUnitario, item._valorItem))
        print("_______________________________________________________________________________________________________________")
        print("%s %.2f" % ("Valor Total:", self.valorNota))
    
    