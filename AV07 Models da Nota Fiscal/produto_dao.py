import pymysql

from produto import Produto

class ProdutoDao:
    def __init__(self):
        self.conexao = pymysql.connect(db = 'nf', user = 'root', passwd = '1234')
        self.cursor = self.conexao.cursor()

    def __del__(self):
        self.cursor.close()
        self.conexao.close()

    def inserir(self, produto : Produto):
        self.cursor.execute("INSERT INTO produto (idProduto, codigo, descricao, valorUnitario) VALUES ({}, {}, '{}', {})".format(produto._id, produto._codigo, produto._descricao, produto._valorUnitario))
        self.conexao.commit()

    def consultar(self):
        self.cursor.execute("SELECT idProduto, codigo, descricao, valorUnitario FROM produto")
        resultados = self.cursor.fetchall()
        produtos = []
        for linha in resultados:
            produtos.append(Produto(linha[0], linha[1], linha[2], linha[3]))
        return produtos

    def atualizar(self, produto : Produto):
        self.cursor.execute("UPDATE produto SET codigo = {}, descricao = '{}', valorUnitario = {} WHERE idProduto = {}".format(produto._codigo, produto._descricao, produto._valorUnitario, produto._id))
        self.conexao.commit()

    def excluir(self, produto : Produto):
        self.cursor.execute("DELETE FROM produto WHERE idProduto = {}".format(produto._id))
        self.conexao.commit()
    
    def serial(self):
        self.cursor.execute("SELECT coalesce(MAX(idProduto), 0) + 1 FROM produto")
        resultado = self.cursor.fetchone()
        return int(resultado[0])