from flask import Flask, request
from flask_restful import Resource, Api
import json

from habilidades import Habilidades, ListaHabilidades

app = Flask(__name__)
api = Api(app)

#pre cadastro
desenvolvedores = [
    {
        'id': 0,
        'nome': 'Rafael',
        'habilidade': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Nanderson',
        'habilidade': ['Python', 'Django']
    }
]

class Desenvolvedor(Resource):

    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            msg = 'Desenvolvedor de ID {} nao existe'.format(id)
            response = {'status': 'erro', 'mensagem': msg}
        except Exception:
            msg = 'Erro desconhecido, Procure o administrador!'
            response = {'status': 'erro', 'mensagem': msg}
        return response

    def put(self, id):
        try:
            dados = json.loads(request.data)
            if dados not in desenvolvedores:
                desenvolvedores[id] = dados
                response = desenvolvedores[id]
            else:
                msg = 'O Desenvolvedor {} já existe'.format(dados)
                response = {'status': 'erro', 'mensagem': msg}
        except IndexError:
            msg = 'Desenvolvedor de ID {} nao existe'.format(id)
            response = {'status': 'erro', 'mensagem': msg}
        except Exception:
            msg = 'Erro desconhecido, Procure o administrador!'
            response = {'status': 'erro', 'mensagem': msg}
        return response

    def delete(self, id):
        try:
            desenvolvedores.pop(id)
            response = desenvolvedores[id]
        except IndexError:
            msg = 'Desenvolvedor de ID {} nao existe'.format(id)
            response = {'status': 'erro', 'mensagem': msg}
        except Exception:
            msg = 'Erro desconhecido, Procure o administrador!'
            response = {'status': 'erro', 'mensagem': msg}
        return response

class ListaDesenvolvedores(Resource):

    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return {'status': 'sucesso', 'mensagem': 'Registro inserido'}

api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaHabilidades, '/habilidades/')
api.add_resource(Habilidades, '/habilidades/<int:pos>/')


if __name__ == "__main__":
    app.run(debug=True)

