from flask import Flask
from flask_restful import Api

from controlador import ClienteControlador, ClientesControlador, ProdutoControlador, ProdutosControlador, NotaFiscalControlador, NotasFiscaisControlador, CalcularNotaFiscalControlador, ImprimirNotaFiscalContolador, ItemNotaFiscalControlador, ItensNotaFiscalControlador, CriarItemNotaFiscalControlador

app = Flask(__name__) #Inicializa a aplicação
api = Api(app)

api.add_resource(ClientesControlador, '/cliente')
api.add_resource(ClienteControlador, '/cliente/<cliente_id>')

api.add_resource(ProdutosControlador, '/produto')
api.add_resource(ProdutoControlador, '/produto/<produto_id>')

api.add_resource(NotasFiscaisControlador, '/notafiscal')
api.add_resource(NotaFiscalControlador, '/notafiscal/<notafiscal_id>')

api.add_resource(CalcularNotaFiscalControlador, '/calculanf/<notafiscal_id>')
api.add_resource(ImprimirNotaFiscalContolador, '/imprimenf/<notafiscal_id>')

api.add_resource(ItemNotaFiscalControlador, '/itemnf/<item_id>')
api.add_resource(ItensNotaFiscalControlador, '/itensnf/<notafiscal_id>')
api.add_resource(CriarItemNotaFiscalControlador, '/itemnf')

if __name__ == '__main__':
    app.run() #Executa a aplicação