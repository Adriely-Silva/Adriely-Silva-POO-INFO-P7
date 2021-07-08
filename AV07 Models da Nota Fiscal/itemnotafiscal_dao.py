import pymysql

from itemnotafiscal import ItemNotaFiscal
from produto import Produto
from notafiscal import NotaFiscal

class ItemNotaFiscalDao:
    def __init__(self):
        self.conexao = pymysql.connect(db = 'nf', user = 'root', passwd = '1234')
        self.cursor = self.conexao.cursor()

    def __del__(self):
        self.cursor.close()
        self.conexao.close()

    def inserir(self, itemnotafiscal : ItemNotaFiscal, notafiscal : NotaFiscal):
        self.cursor.execute("INSERT INTO itemnotafiscal (idItemNotaFiscal, sequencial, quantidade, Produto_idProduto, NotaFiscal_idNotaFiscal) VALUES ({}, {}, {}, {}, {})".format(itemnotafiscal._id, itemnotafiscal._sequencial, itemnotafiscal._quantidade, itemnotafiscal._produto._id, notafiscal._id))
        self.conexao.commit()

    def consultar(self):
        self.cursor.execute("SELECT i.idItemNotaFiscal, i.sequencial, i.quantidade, p.idProduto, p.codigo, p.descricao, p.valorUnitario FROM itemnotafiscal AS i JOIN produto AS p ON (p.idProduto = i.Produto_idProduto)")
        resultados = self.cursor.fetchall()
        itens = []
        for linha in resultados:
            itens.append(ItemNotaFiscal(linha[0], linha[1], linha[2], Produto(linha[3], linha[4], linha[5], linha[6]) ))
        return itens

    def atualizar(self, itemnotafiscal : ItemNotaFiscal):
        self.cursor.execute("UPDATE itemnotafiscal SET sequencial = {}, quantidade = {}, Produto_idProduto = {} WHERE idItemNotaFiscal = {}".format(itemnotafiscal._sequencial, itemnotafiscal._quantidade, itemnotafiscal._produto._id, itemnotafiscal._id))
        self.conexao.commit()

    def excluir(self, itemnotafiscal : ItemNotaFiscal):
        self.cursor.execute("DELETE FROM itemnotafiscal WHERE idItemNotaFiscal = {}".format(itemnotafiscal._id))
        self.conexao.commit()
    
    def serial(self):
        self.cursor.execute("SELECT coalesce(MAX(idItemNotaFiscal), 0) + 1 FROM itemnotafiscal")
        resultado = self.cursor.fetchone()
        return int(resultado[0])
    
    def consultar_por_nota(self, nota_id):
        self.cursor.execute("SELECT i.idItemNotaFiscal, i.sequencial, i.quantidade, p.idProduto, p.codigo, p.descricao, p.valorUnitario FROM itemnotafiscal AS i JOIN produto AS p ON (p.idProduto = i.Produto_idProduto) WHERE i.NotaFiscal_idNotaFiscal = {}".format(nota_id))
        resultados = self.cursor.fetchall()
        itens = []
        for linha in resultados:
            itens.append(ItemNotaFiscal(linha[0], linha[1], linha[2], Produto(linha[3], linha[4], linha[5], linha[6]) ))
        return itens