import pymysql

from cliente import Cliente
from tipocliente import TipoCliente

class ClienteDao:
    def __init__(self):
        self.conexao = pymysql.connect(db = 'nf', user = 'root', passwd = '1234')
        self.cursor = self.conexao.cursor()

    def __del__(self):
        self.cursor.close()
        self.conexao.close()

    def inserir(self, cliente : Cliente):
        self.cursor.execute("INSERT INTO cliente (idCliente, nome, codigo, cnpjcpf, tipo) VALUES ({}, '{}', {}, '{}', {})".format(cliente._id, cliente._nome, cliente._codigo, cliente._cnpjcpf, cliente._tipo.value))
        self.conexao.commit()

    def consultar(self):
        self.cursor.execute("SELECT idCliente, nome, codigo, cnpjcpf, tipo FROM cliente")
        resultados = self.cursor.fetchall()
        clientes = []
        for linha in resultados:
            clientes.append(Cliente(linha[0], linha[1], linha[2], linha[3], TipoCliente.retonar_enum(int(linha[4]))))
        return clientes

    def atualizar(self, cliente : Cliente):
        self.cursor.execute("UPDATE cliente SET nome = '{}', codigo = {}, cnpjcpf = '{}', tipo = {} WHERE idCliente = {}".format(cliente._nome, cliente._codigo, cliente._cnpjcpf, cliente._tipo.value, cliente._id))
        self.conexao.commit()

    def excluir(self, cliente : Cliente):
        self.cursor.execute("DELETE FROM cliente WHERE idCliente = {}".format(cliente._id))
        self.conexao.commit()
    
    def serial(self):
        self.cursor.execute("SELECT coalesce(MAX(idCliente), 0) + 1 FROM cliente")
        resultado = self.cursor.fetchone()
        return int(resultado[0])