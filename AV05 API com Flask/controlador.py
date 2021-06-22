from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from cliente import Cliente
from tipocliente import TipoCliente

app = Flask(__name__) #Inicializa a aplicação
api = Api(app)

CLIENTES = []

resource_fields = {
    'nome': fields.String('_nome', '_nome'),
    'codigo': fields.Integer('_codigo', '_codigo'),
    'cnpjcpf': fields.String('_cnpjcpf', '_cnpjcpf'),
    '_tipo.name': fields.String('_tipo.name', '_tipo.name')
}

def encontrar_cliente(cliente_id):
    for cliente in CLIENTES:
        if cliente_id == cliente._id:
            return cliente
    return None

def cancelar_se_clinte_nao_existir(cliente_id):
    if (encontrar_cliente(cliente_id) == None):
        abort(404, message="Cliente {} não existe".format(cliente_id))

parser = reqparse.RequestParser()
parser.add_argument('nome')
parser.add_argument('codigo', type = int)
parser.add_argument('cnpjcpf')
parser.add_argument('tipo', type = int)

class ClienteControlador(Resource):
    @marshal_with(resource_fields)
    def get(self, cliente_id):
        cancelar_se_clinte_nao_existir(int(cliente_id))
        return encontrar_cliente(int(cliente_id))

    def delete(self, cliente_id):
        cancelar_se_clinte_nao_existir(int(cliente_id))
        CLIENTES.remove(encontrar_cliente(int(cliente_id)))
        return '', 204

    @marshal_with(resource_fields)
    def put(self, cliente_id):
        args = parser.parse_args()
        cliente = encontrar_cliente(int(cliente_id))
        cliente._nome = args['nome']
        cliente._codigo = args['codigo']
        cliente._cnpjcpf = args['cnpjcpf']
        cliente._tipo = TipoCliente.retonar_enum(args['tipo'])
        return cliente, 201

class ClientesControlador(Resource):
    SERIAL_ID = 1

    @marshal_with(resource_fields)
    def get(self):
        return CLIENTES

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        cliente = Cliente(self.SERIAL_ID, args['nome'], args['codigo'], args['cnpjcpf'], TipoCliente.retonar_enum(args['tipo']))
        CLIENTES.append(cliente)
        self.SERIAL_ID += 1
        return cliente, 201

api.add_resource(ClientesControlador, '/cliente')
api.add_resource(ClienteControlador, '/cliente/<cliente_id>')

if __name__ == '__main__':
    app.run() #Executa a aplicação