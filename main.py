from flask import Flask, jsonify
from flask_cors import CORS
import random


app = Flask(__name__)
CORS(app)


@app.route('/charadas', methods=['GET'])
def charadas():
    lista_charadas = [
        {"pergunta": "Qual A Semelhança Entre Uma mulher e Uma Granada?", "resposta": "Se Tirar O Anel As 2 Levam Metade Da Casa."},
        {"pergunta": "Porque As Criancas Do Orfanato Não Vao Para A Viagem?", "resposta": "Porque Precisa Da Autorizacao Dos Pais."},
        {"pergunta": "O Que é Um Ponto e Virgula No Final Do JavaScript?", "resposta": "Um Aluno Programador WEB."},
    ]
    charada = random.choice(lista_charadas)
    return jsonify([charada])

@app.route('/')
def index():
    return 'API CHARADA ESTÁ ONLINE!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



