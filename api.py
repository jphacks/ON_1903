from flask import Flask, jsonify, make_response, request, render_template
from flask_cors import CORS
import os
from aki import Jinn

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

jinns = {}

user_id = 0

@app.route('/', methods=['GET'])
def route():
    return render_template('index.html')

@app.route('/jinn/<int:user_id>/question', methods=['GET'])
def question(user_id):
    global jinns

    jinn = jinns[user_id]

    (target, flag) = jinn.update_target() # 質問するtargetを返す

    if flag == 1:
        resp = make_response(jsonify({'question': f'{target}ですか？', 'continue': True}))
    elif flag == 2:
        resp = make_response(jsonify({'question': f'{target}', 'continue': False}))
    else:
        resp = make_response(jsonify({'question': f'{target}を使用していますか？', 'continue': True}))

    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/jinn/<int:user_id>/answer', methods=['POST'])
def choice(user_id):
    global jinns

    jinn = jinns[user_id]
    choiced = request.json['answer']
    df = jinn.update_remining_df(choiced)

    return jsonify({'result': True})

@app.route('/jinn/new')
def new_instance():
    global jinns
    global user_id

    _id = user_id
    jinns[_id] = Jinn(path='tmp.csv')
    user_id = _id + 1

    return jsonify({'user_id': _id})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
