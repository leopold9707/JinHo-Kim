from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"text" : "Hello, world!"})

@app.route('/iam/<name>')
def whoami(name):
    return jsonify({"Your name" : name})

@app.route('/login', methods = ['POST'])
def login():
    uid = request.get_json()
    return jsonify(uid)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
