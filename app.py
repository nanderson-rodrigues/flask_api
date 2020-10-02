from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'nome': 'Rafael',
        'habilidade': ['Python', 'Flask']
    },
    {
        'nome': 'Nanderson',
        'habilidade': ['Python', 'Django']
    }
]
 
#recupera (pelo id), altera e deleta desenvolvedores
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            msg = 'Desenvolvedor de ID {} nao existe'.format(id
            response = {'status': 'erro', 'mensagem': msg}
        except Exception:
            msg = 'Erro desconhecido, Procure o administrador!'
            response = {'status': 'erro', 'mensagem': msg}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido'})

#lista desenvolvedores
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
