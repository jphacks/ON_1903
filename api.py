from flask import Flask, jsonify, make_response, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def route():
    resp = make_response(jsonify({'message': 'Hello, world'}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/q', methods=['GET'])
def q():
    resp = make_response(jsonify({'question': '米が使われている？'}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/choice', methods=['POST'])
def choice():
    print(request.json)
    resp = make_response(jsonify({'message': 'ok'}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
