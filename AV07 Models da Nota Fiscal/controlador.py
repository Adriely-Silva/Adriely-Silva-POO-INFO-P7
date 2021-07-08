from flask_restful import reqparse, abort, Resource, fields, marshal_with

from cliente import Cliente
from cliente_dao import ClienteDao
from tipocliente import TipoCliente

from produto import Produto
from produto_dao import ProdutoDao

from notafiscal import NotaFiscal
from notafiscal_dao import NotaFiscalDao

from itemnotafiscal import ItemNotaFiscal
from itemnotafiscal_dao import ItemNotaFiscalDao

#
clienteDao = ClienteDao()
produtoDao = ProdutoDao()
notafiscalDao = NotaFiscalDao()
itemnotafiscalDao = ItemNotaFiscalDao()

#
cliente_resource_fields = {
    'id': fields.String('', '_id'),
    'nome': fields.String('', '_nome'),
    'codigo': fields.String('', '_codigo'),
    'cnpjcpf': fields.String('', '_cnpjcpf'),
    'tipo': fields.String('', '_tipo.name')
}

produto_resource_fields = {
    'id': fields.String('', '_id'),
    'codigo': fields.String('', '_codigo'),
    'descricao': fields.String('', '_descricao'),
    'valorUnitario': fields.String('', '_valorUnitario')
}

nota_resource_fields = {
    'id': fields.String('', '_id'),
    'codigo': fields.String('', '_codigo'),
    'cliente': fields.String('', '_cliente._nome'),
    'data': fields.String('', '_data'),
    'itens': fields.String('', '_itens'),
    'valorNota': fields.String('', '_valorNota')
}

item_resource_fields = {
    'id': fields.String('', '_id'),
    'sequencial': fields.String('', '_sequencial'),
    'quantidade': fields.String('', '_quantidade'),
    'produto': fields.String('', '_descricao')
}

#
def encontrar_cliente(cliente_id):
    for cliente in clienteDao.consultar():
        if cliente_id == cliente._id:
            return cliente
    return None

def encontrar_produto(produto_id):
    for produto in produtoDao.consultar():
        if produto_id == produto._id:
            return produto
    return None

def encontrar_notafiscal(notafiscal_id):
    for notafiscal in notafiscalDao.consultar():
        if notafiscal_id == notafiscal._id:
            return notafiscal
    return None

def encontrar_item(item_id):
    for item in itemnotafiscalDao.consultar():
        if item_id == item._id:
            return item
    return None

#

def cancelar_cliente_se_nao_existir(cliente_id):
    if (encontrar_cliente(cliente_id) == None):
        abort(404, message="Cliente {} não existe".format(cliente_id))

def cancelar_produto_se_nao_existir(produto_id):
    if (encontrar_produto(produto_id) == None):
        abort(404, message="Produto {} não existe".format(produto_id))

def cancelar_notafiscal_se_nao_existir(notafiscal_id):
    if (encontrar_notafiscal(notafiscal_id) == None):
        abort(404, message="Nota Fiscal {} não existe".format(notafiscal_id))

def cancelar_item_se_nao_existir(item_id):
    if (encontrar_item(item_id) == None):
        abort(404, message="Item {} não existe".format(item_id))

#
cliente_parser = reqparse.RequestParser()
cliente_parser.add_argument('nome', required = True, help = "Este campo é obrigatório")
cliente_parser.add_argument('codigo', type = int, required = True, help = "Este campo é obrigatório")
cliente_parser.add_argument('cnpjcpf', required = True, help = "Este campo é obrigatório")
cliente_parser.add_argument('tipo', type = int, required = True, help = "Este campo é obrigatório")

produto_parser = reqparse.RequestParser()
produto_parser.add_argument('codigo', type = int, required = True, help = "Este campo é obrigatório")
produto_parser.add_argument('descricao', required = True, help = "Este campo é obrigatório")
produto_parser.add_argument('valorUnitario', type = float, required = True, help = "Este campo é obrigatório")

nota_parser = reqparse.RequestParser()
nota_parser.add_argument('codigo', type = int, required = True, help = "Este campo é obrigatório")
nota_parser.add_argument('cliente', type = int, required = True, help = "Este campo é obrigatório")

item_parser = reqparse.RequestParser()
item_parser.add_argument('sequencial', type = int, required = True, help = "Este campo é obrigatório")
item_parser.add_argument('quantidade', type = int, required = True, help = "Este campo é obrigatório")
item_parser.add_argument('produto', type = int, required = True, help = "Este campo é obrigatório")
item_parser.add_argument('notafiscal', type = int, required = True, help = "Este campo é obrigatório")

#CLIENTE
class ClienteControlador(Resource):

    @marshal_with(cliente_resource_fields)
    def get(self, cliente_id):
        cancelar_cliente_se_nao_existir(int(cliente_id))
        return encontrar_cliente(int(cliente_id))

    def delete(self, cliente_id):
        cancelar_cliente_se_nao_existir(int(cliente_id))
        clienteDao.excluir(encontrar_cliente(int(cliente_id)))
        return '', 204

    @marshal_with(cliente_resource_fields)
    def put(self, cliente_id):
        cancelar_cliente_se_nao_existir(int(cliente_id))
        cliente = encontrar_cliente(int(cliente_id))
        args = cliente_parser.parse_args()
        cliente._nome = args['nome']
        cliente._codigo = args['codigo']
        cliente._cnpjcpf = args['cnpjcpf']
        cliente._tipo = TipoCliente.retonar_enum(args['tipo'])
        clienteDao.atualizar(cliente)
        return cliente, 201

class ClientesControlador(Resource):

    @marshal_with(cliente_resource_fields)
    def get(self):
        return clienteDao.consultar()
    
    @marshal_with(cliente_resource_fields)
    def post(self):
        args = cliente_parser.parse_args()
        serial = clienteDao.serial()
        cliente = Cliente(serial, args['nome'], args['codigo'], args['cnpjcpf'], TipoCliente.retonar_enum(args['tipo']))
        clienteDao.inserir(cliente)
        return cliente, 201

#PRODUTO
class ProdutoControlador(Resource):

    @marshal_with(produto_resource_fields)
    def get(self, produto_id):
        cancelar_produto_se_nao_existir(int(produto_id))
        return encontrar_produto(int(produto_id))

    def delete(self, produto_id):
        cancelar_produto_se_nao_existir(int(produto_id))
        produtoDao.excluir(encontrar_produto(int(produto_id)))
        return '', 204
    
    @marshal_with(produto_resource_fields)
    def put(self, produto_id):
        cancelar_produto_se_nao_existir(int(produto_id))
        produto = encontrar_produto(int(produto_id))
        args = produto_parser.parse_args()
        produto._codigo = args['codigo']
        produto._descricao = args['descricao']
        produto._valorUnitario = args['valorUnitario']
        produtoDao.atualizar(produto)
        return produto, 201

class ProdutosControlador(Resource):

    @marshal_with(produto_resource_fields)
    def get(self):
        return produtoDao.consultar()
    
    @marshal_with(produto_resource_fields)
    def post(self):
        args = produto_parser.parse_args()
        serial = produtoDao.serial()
        produto = Produto(serial, args['codigo'], args['descricao'], args['valorUnitario'])
        produtoDao.inserir(produto)
        return produto, 201

#NOTA FISCAL
class NotaFiscalControlador(Resource):

    @marshal_with(nota_resource_fields)
    def get(self, notafiscal_id):
        cancelar_notafiscal_se_nao_existir(int(notafiscal_id))
        return encontrar_notafiscal(int(notafiscal_id))

    def delete(self, notafiscal_id):
        cancelar_notafiscal_se_nao_existir(int(notafiscal_id))
        notafiscalDao.excluir(encontrar_notafiscal(int(notafiscal_id)))
        return '', 204
    
    @marshal_with(nota_resource_fields)
    def put(self, notafiscal_id):
        cancelar_notafiscal_se_nao_existir(int(notafiscal_id))
        nota = encontrar_notafiscal(int(notafiscal_id))
        args = nota_parser.parse_args()
        cancelar_cliente_se_nao_existir(int(args['cliente']))
        cliente = encontrar_cliente(int(args['cliente']))
        nota._codigo = args['codigo']
        nota.setCliente(cliente)
        notafiscalDao.atualizar(nota)
        return nota, 201

class NotasFiscaisControlador(Resource):

    @marshal_with(nota_resource_fields)
    def get(self):
        return notafiscalDao.consultar()
    
    @marshal_with(nota_resource_fields)
    def post(self):
        args = nota_parser.parse_args()
        cancelar_cliente_se_nao_existir(int(args['cliente']))
        cliente = encontrar_cliente(int(args['cliente']))
        serial = notafiscalDao.serial()
        nota = NotaFiscal(serial, args['codigo'], cliente)
        notafiscalDao.inserir(nota)
        return nota, 201

class CalcularNotaFiscalControlador(Resource):

    def get(self, notafiscal_id):
        cancelar_notafiscal_se_nao_existir(int(notafiscal_id))
        nota = encontrar_notafiscal(int(notafiscal_id))
        nota.calcularNotaFiscal()
        return ''

class ImprimirNotaFiscalContolador(Resource):
 
    def get(self, notafiscal_id):
        cancelar_notafiscal_se_nao_existir(int(notafiscal_id))
        nota = encontrar_notafiscal(int(notafiscal_id))
        return nota.imprimirNotaFiscal()

#ITEM NOTA FISCAL

class ItemNotaFiscalControlador(Resource):
 
    @marshal_with(item_resource_fields)
    def get(self, item_id):
        cancelar_item_se_nao_existir(int(item_id))
        return encontrar_item(int(item_id))
    
    @marshal_with(item_resource_fields)
    def put(self, item_id):
        cancelar_item_se_nao_existir(int(item_id))
        item = encontrar_item(int(item_id))
        args = item_parser.parse_args()

        cancelar_produto_se_nao_existir(int(args['produto']))
        produto = encontrar_produto(int(args['produto']))

        item = encontrar_item(int(item_id))
        item._sequencial = args['sequencial']
        item._quantidade = args['quantidade']
        item._produto = produto
        itemnotafiscalDao.atualizar(item)
        return item, 201
        
    def delete(self, item_id):
        cancelar_item_se_nao_existir(int(item_id))
        itemnotafiscalDao.excluir(encontrar_item(int(item_id)))
        return '', 204

class ItensNotaFiscalControlador(Resource):

    @marshal_with(item_resource_fields)
    def get(self, notafiscal_id):
        cancelar_notafiscal_se_nao_existir(int(notafiscal_id))
        itens = itemnotafiscalDao.consultar_por_nota(int(notafiscal_id))
        return itens

class CriarItemNotaFiscalControlador(Resource):

    @marshal_with(item_resource_fields)
    def post(self):
        args = item_parser.parse_args()

        cancelar_produto_se_nao_existir(int(args['produto']))
        produto = encontrar_produto(int(args['produto']))

        cancelar_notafiscal_se_nao_existir(int(args['notafiscal']))
        nota = encontrar_notafiscal(int(args['notafiscal']))

        serial = itemnotafiscalDao.serial()
        item = ItemNotaFiscal(serial, args['sequencial'], args['quantidade'], produto)
        itemnotafiscalDao.inserir(item, nota)
        return item, 201


