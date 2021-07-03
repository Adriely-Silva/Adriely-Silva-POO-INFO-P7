from flask_restful import reqparse, abort, Resource, fields, marshal_with

from cliente import Cliente
from tipocliente import TipoCliente
from produto import Produto
from notafiscal import NotaFiscal
from itemnotafiscal import ItemNotaFiscal

CLIENTES = []
PRODUTOS = []
NOTAS = []

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
nota_parser.add_argument('clienteId', type = int, required = True, help = "Este campo é obrigatório")

item_parser = reqparse.RequestParser()
item_parser.add_argument('sequencial', type = int, required = True, help = "Este campo é obrigatório")
item_parser.add_argument('quantidade', type = int, required = True, help = "Este campo é obrigatório")
item_parser.add_argument('produtoId', type = int, required = True, help = "Este campo é obrigatório")
item_parser.add_argument('notafiscalId', type = int, required = True, help = "Este campo é obrigatório")

def serial_id(lista):
    serial = 1
    for o in lista:
        serial += 1
    return serial

def serial_item_id():
    serial = 1
    for nota in NOTAS:
        for item in nota._itens:
            serial +=1
    return serial

def encontrar_cliente(cliente_id):
    for cliente in CLIENTES:
        if cliente_id == cliente._id:
            return cliente
    return None

def cancelar_se_clinte_nao_existir(cliente_id):
    if (encontrar_cliente(cliente_id) == None):
        abort(404, message="Cliente {} não existe".format(cliente_id))

def encontrar_produto(produto_id):
    for produto in PRODUTOS:
        if produto_id == produto._id:
            return produto
    return None

def cancelar_se_produto_nao_existir(produto_id):
    if (encontrar_produto(produto_id) == None):
        abort(404, message="Produto {} não existe".format(produto_id))

def encontrar_notafiscal(notafiscal_id):
    for nota in NOTAS:
        if notafiscal_id == nota._id:
            return nota
    return None

def cancelar_se_notafiscal_nao_existir(notafiscal_id):
    if (encontrar_notafiscal(notafiscal_id) == None):
        abort(404, message="Nota {} não existe".format(notafiscal_id))

def encontrar_nota_item(item_id):
    for nota in NOTAS:
        for item in nota._itens:
            if item_id == item._id:
                return nota
    return None

def encontrar_item(item_id):
    for nota in NOTAS:
        for item in nota._itens:
            if item_id == item._id:
                return item
    return None

def cancelar_se_item_nao_existir(item_id):
    if (encontrar_item(item_id) == None):
        abort(404, message="Item {} não existe".format(item_id))

class ClienteControlador(Resource):
    @marshal_with(cliente_resource_fields)
    def get(self, cliente_id):
        cancelar_se_clinte_nao_existir(int(cliente_id))
        return encontrar_cliente(int(cliente_id))

    def delete(self, cliente_id):
        cancelar_se_clinte_nao_existir(int(cliente_id))
        CLIENTES.remove(encontrar_cliente(int(cliente_id)))
        return '', 204

    @marshal_with(cliente_resource_fields)
    def put(self, cliente_id):
        cancelar_se_clinte_nao_existir(int(cliente_id))
        cliente = encontrar_cliente(int(cliente_id))
        args = cliente_parser.parse_args()
        cliente._nome = args['nome']
        cliente._codigo = args['codigo']
        cliente._cnpjcpf = args['cnpjcpf']
        cliente._tipo = TipoCliente.retonar_enum(args['tipo'])
        return cliente, 201

class ClientesControlador(Resource):

    @marshal_with(cliente_resource_fields)
    def get(self):
        return CLIENTES

    @marshal_with(cliente_resource_fields)
    def post(self):
        args = cliente_parser.parse_args()
        cliente = Cliente(serial_id(CLIENTES), args['nome'], args['codigo'], args['cnpjcpf'], TipoCliente.retonar_enum(args['tipo']))
        CLIENTES.append(cliente)
        return cliente, 201

class ProdutoControlador(Resource):
    @marshal_with(produto_resource_fields)
    def get(self, produto_id):
        cancelar_se_produto_nao_existir(int(produto_id))
        return encontrar_produto(int(produto_id))

    def delete(self, produto_id):
        cancelar_se_produto_nao_existir(int(produto_id))
        PRODUTOS.remove(encontrar_produto(int(produto_id)))
        return '', 204

    @marshal_with(produto_resource_fields)
    def put(self, produto_id):
        cancelar_se_produto_nao_existir(int(produto_id))
        produto = encontrar_produto(int(produto_id))
        args = produto_parser.parse_args()
        produto._codigo = args['codigo']
        produto._descricao = args['descricao']
        produto._valorUnitario = args['valorUnitario']
        return produto, 201

class ProdutosControlador(Resource):

    @marshal_with(produto_resource_fields)
    def get(self):
        return PRODUTOS

    @marshal_with(produto_resource_fields)
    def post(self):
        args = produto_parser.parse_args()
        produto = Produto(serial_id(PRODUTOS), args['codigo'], args['descricao'], args['valorUnitario'])
        PRODUTOS.append(produto)
        return produto, 201

class NotaFiscalControlador(Resource):
    @marshal_with(nota_resource_fields)
    def get(self, notafiscal_id):
        cancelar_se_notafiscal_nao_existir(int(notafiscal_id))
        return encontrar_notafiscal(int(notafiscal_id))

    def delete(self, notafiscal_id):
        cancelar_se_notafiscal_nao_existir(int(notafiscal_id))
        NOTAS.remove(encontrar_notafiscal(int(notafiscal_id)))
        return '', 204

    @marshal_with(nota_resource_fields)
    def put(self, notafiscal_id):
        cancelar_se_notafiscal_nao_existir(int(notafiscal_id))
        nota = encontrar_notafiscal(int(notafiscal_id))
        args = nota_parser.parse_args()
        cancelar_se_clinte_nao_existir(int(args['clienteId']))
        cliente = encontrar_cliente(int(args['clienteId']))
        nota._codigo = args['codigo']
        nota.setCliente(cliente)
        return nota, 201

class NotasFiscaisControlador(Resource):

    @marshal_with(nota_resource_fields)
    def get(self):
        return NOTAS

    @marshal_with(nota_resource_fields)
    def post(self):
        args = nota_parser.parse_args()
        cancelar_se_clinte_nao_existir(int(args['clienteId']))
        cliente = encontrar_cliente(int(args['clienteId']))
        nota = NotaFiscal(serial_id(NOTAS), args['codigo'], cliente)
        NOTAS.append(nota)
        return nota, 201

class CalcularNotaFiscalControlador(Resource):

    def get(self, notafiscal_id):
        cancelar_se_notafiscal_nao_existir(int(notafiscal_id))
        nota = encontrar_notafiscal(int(notafiscal_id))
        nota.calcularNotaFiscal()
        return ''

class ImprimirNotaFiscalContolador(Resource):
 
    def get(self, notafiscal_id):
        cancelar_se_notafiscal_nao_existir(int(notafiscal_id))
        nota = encontrar_notafiscal(int(notafiscal_id))
        return nota.imprimirNotaFiscal()

class ItemNotaFiscalControlador(Resource):
 
    @marshal_with(item_resource_fields)
    def get(self, item_id):
        cancelar_se_item_nao_existir(int(item_id))
        return encontrar_item(int(item_id))
    
    @marshal_with(item_resource_fields)
    def put(self, item_id):
        cancelar_se_item_nao_existir(int(item_id))
        item = encontrar_item(int(item_id))
        args = item_parser.parse_args()

        cancelar_se_produto_nao_existir(int(args['produtoId']))
        produto = encontrar_produto(int(args['produtoId']))

        item = encontrar_item(int(item_id))
        item._sequencial = args['sequencial']
        item._quantidade = args['quantidade']
        item._produto = produto

        return item, 201

    def delete(self, item_id):
        cancelar_se_item_nao_existir(int(item_id))
        nota = encontrar_nota_item(int(item_id))
        nota._itens.remove(encontrar_item(int(item_id)))
        return '', 204

class ItensNotaFiscalControlador(Resource):

    @marshal_with(item_resource_fields)
    def get(self, notafiscal_id):
        cancelar_se_notafiscal_nao_existir(int(notafiscal_id))
        nota = encontrar_notafiscal(int(notafiscal_id))
        return nota._itens

class CriarItemNotaFiscalControlador(Resource):

    @marshal_with(item_resource_fields)
    def post(self):
        args = item_parser.parse_args()

        cancelar_se_produto_nao_existir(int(args['produtoId']))
        produto = encontrar_produto(int(args['produtoId']))

        cancelar_se_notafiscal_nao_existir(int(args['notafiscalId']))
        nota = encontrar_notafiscal(int(args['notafiscalId']))

        item = ItemNotaFiscal(serial_item_id(), args['sequencial'], args['quantidade'], produto)
        nota.adicionarItem(item)
        return item, 201