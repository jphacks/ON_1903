from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    return jsonify({"question": "豚は入っている？"})

if __name__ == "__main__":
    app.run(debug=True)
