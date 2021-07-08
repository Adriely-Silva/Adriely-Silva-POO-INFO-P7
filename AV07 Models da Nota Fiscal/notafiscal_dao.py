import pymysql

from notafiscal import NotaFiscal
from cliente import Cliente
from tipocliente import TipoCliente

class NotaFiscalDao:
    def __init__(self):
        self.conexao = pymysql.connect(db = 'nf', user = 'root', passwd = '1234')
        self.cursor = self.conexao.cursor()

    def __del__(self):
        self.cursor.close()
        self.conexao.close()

    def inserir(self, notafiscal : NotaFiscal):
        self.cursor.execute("INSERT INTO notafiscal (idNotaFiscal, codigo, Cliente_idCliente) VALUES ({}, {}, {})".format(notafiscal._id, notafiscal._codigo, notafiscal._cliente._id))
        self.conexao.commit()

    def consultar(self):
        self.cursor.execute("SELECT n.idNotaFiscal, n.codigo, c.idCliente, c.nome, c.codigo, c.cnpjcpf, c.tipo FROM notafiscal AS n JOIN cliente AS c ON (c.idCliente = n.Cliente_idCliente)")
        resultados = self.cursor.fetchall()
        notas = []
        for linha in resultados:
            notas.append(NotaFiscal(linha[0], linha[1], Cliente(linha[2], linha[3], linha[4], linha[5], TipoCliente.retonar_enum(int(linha[6])))))
        return notas

    def atualizar(self, notafiscal : NotaFiscal):
        self.cursor.execute("UPDATE notafiscal SET codigo = {}, Cliente_idCliente = {} WHERE idNotaFiscal = {}".format(notafiscal._codigo, notafiscal._cliente._id, notafiscal._id))
        self.conexao.commit()

    def excluir(self, notafiscal : NotaFiscal):
        self.cursor.execute("DELETE FROM notafiscal WHERE idNotaFiscal = {}".format(notafiscal._id))
        self.conexao.commit()
    
    def serial(self):
        self.cursor.execute("SELECT coalesce(MAX(idNotaFiscal), 0) + 1 FROM notafiscal")
        resultado = self.cursor.fetchone()
        return int(resultado[0])