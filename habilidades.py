from flask_restful import Resource
from flask import Flask, request
import json

lista_habilidades = ['Python', 'Java', 'Flask']

class ListaHabilidades(Resource):

    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        if dados in lista_habilidades:
            msg = 'Essa habilidade já existe na lista de habilidades!'
            response = {'status': 'erro', 'mensagem': msg}
        else:
            lista_habilidades.append(dados)
            msg = 'Nova habilidade inserida com sucesso!'
            response = {'status': 'Sucesso!', 'mensagem': msg}
        return response


class Habilidades(Resource):

    def put(self, pos):
        try:
            dados = json.loads(request.data)
            if dados not in lista_habilidades:
                lista_habilidades[pos] = dados
                response = lista_habilidades[pos]
            else:
                msg = 'A habilidade {} já existe'.format(dados)
                response = {'status': 'erro', 'mensagem': msg}
        except IndexError:
            msg = 'Desenvolvedor de índice {} nao existe'.format(pos)
            response = {'status': 'erro', 'mensagem': msg}
        except Exception:
            msg = 'Erro desconhecido, Procure o administrador!'
            response = {'status': 'erro', 'mensagem': msg}
        return response

    def delete(self, pos):
        try:
            lista_habilidades.pop(pos)
            response = lista_habilidades[pos]
        except IndexError:
            msg = 'Desenvolvedor de ID {} nao existe'.format(pos)
            response = {'status': 'erro', 'mensagem': msg}
        except Exception:
            msg = 'Erro desconhecido, Procure o administrador!'
            response = {'status': 'erro', 'mensagem': msg}
        return response